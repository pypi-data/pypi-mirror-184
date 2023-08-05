import dataclasses
import enum
import logging
import traceback
import typing

import gci.componentmodel as cm

import ccc.oci
import cnudie.iter
import cnudie.retrieve
import cnudie.util
import oci.client as oc
import oci.model as om
import version

logger = logging.getLogger(__name__)


class VersionRestriction(enum.Enum):
    SAME_MINOR = 'same-minor'
    NONE = 'none'


@dataclasses.dataclass
class VersionRetentionPolicy:
    keep: typing.Union[str, int] = 'all'
    restrict: VersionRestriction = VersionRestriction.NONE
    recursive: bool = False

    def matches_version_restriction(self, ref_version, other_version) -> bool:
        if self.restrict is VersionRestriction.NONE:
            return True
        elif self.restrict is VersionRestriction.SAME_MINOR:
            ref_version = version.parse_to_semver(ref_version)
            other_version = version.parse_to_semver(other_version)
            return ref_version.minor == other_version.minor
        else:
            raise RuntimeError(f'not implemented: {self.restrict}')

    @property
    def keep_all(self) -> bool:
        return self.keep == 'all'


@dataclasses.dataclass
class VersionRetentionPolicies:
    name: str
    snapshots: VersionRetentionPolicy
    releases: VersionRetentionPolicy


def iter_componentversions_to_purge(
    component: cm.Component | cm.ComponentDescriptor,
    policy: VersionRetentionPolicies,
    oci_client: oc.Client=None,
    lookup: cnudie.retrieve.ComponentDescriptorLookupById=None,
):
    oci_ref = cnudie.util.oci_ref(component=component)
    if isinstance(component, cm.ComponentDescriptor):
        component = component.component

    snapshots = []
    releases = []

    for v in (version.parse_to_semver(v) for v in oci_client.tags(oci_ref.ref_without_tag)):
        if v.build or v.prerelease:
            if policy.snapshots.keep_all:
                continue
            if not policy.snapshots.matches_version_restriction(
                ref_version=component.version,
                other_version=v
            ):
                continue
            snapshots.append(v)
        else:
            if policy.releases.keep_all:
                continue
            if not policy.snapshots.matches_version_restriction(
                ref_version=component.version,
                other_version=v
            ):
                continue
            releases.append(v)

    yield from version.smallest_versions(
        versions=snapshots,
        keep=policy.snapshots.keep,
    )

    yield from version.smallest_versions(
        versions=releases,
        keep=policy.releases.keep,
    )


def remove_component_descriptor_and_referenced_artefacts(
    component: cm.Component | cm.ComponentDescriptor,
    oci_client: oc.Client=None,
    lookup: cnudie.retrieve.ComponentDescriptorLookupById=None,
    recursive: bool=True,
    on_error: str='abort', # todo: implement, e.g. patch-component-descriptor-and-abort
):
    current_component = None
    resources_with_removal_errors = []
    if not oci_client:
        oci_client = ccc.oci.oci_client()

    for node in cnudie.iter.iter(
        component=component,
        lookup=lookup,
        recursion_depth=-1 if recursive else 0,
    ):
        # cnudie.iter.iter will return sequences of:
        # - component-node (always exactly one per component)
        # - resource-nodes (if any)
        # - source-nodes (if any)
        if isinstance(node, cnudie.iter.ComponentNode):
            if current_component: # skip for first iteration
                _remove_component_descriptor(
                    component=current_component,
                    oci_client=oci_client,
                )
            current_component = node.component
            continue

        if isinstance(node, cnudie.iter.SourceNode):
            continue # we ignore source-nodes for now

        if isinstance(node, cnudie.iter.ResourceNode):
            try:
                did_remove = _remove_resource(
                    node=node,
                    oci_client=oci_client,
                )
                if not did_remove:
                    logger.info(f'do not know how to remove {node.resource=}')
            except Exception as e:
                logger.warning(f'error while trying to remove {node.resource=} - {e=}')
                traceback.print_exc()
                resources_with_removal_errors.append(node)
                if on_error == 'abort':
                    logger.fatal('error encountered - aborting comoponent-descriptor-removal')
                    raise e
                else:
                    raise ValueError(f'unknown value {on_error=}')

    # remove final component (last component-component-descriptor would otherwise not be removed,
    # as we remove component-descriptors only after (trying to) remove referenced resources.
    if current_component:
        _remove_component_descriptor(
            component=component,
            oci_client=oci_client,
        )


def _remove_component_descriptor(
    component: cm.Component,
    oci_client: oc.Client,
):
    oci_ref = cnudie.util.oci_ref(
        component=component,
    )

    oci_client.delete_manifest(
        image_reference=oci_ref,
        purge=True,
    )


def _remove_resource(
    node: cnudie.iter.ResourceNode,
    oci_client: oc.Client,
) -> bool:
    resource = node.resource
    if not resource.type in (cm.ResourceType.OCI_IMAGE, 'ociImage'):
        return False # we only support removal of oci-images for now

    if not resource.relation in (cm.ResourceRelation.LOCAL, 'local'):
        return False # external resources can never be removed (as we do not "own" them)

    if not isinstance(resource.access, cm.OciAccess):
        return False # similar to above: we only support removal of oci-images in oci-registries

    access: cm.OciAccess = resource.access
    image_reference = om.OciImageReference(access.imageReference)

    manifest = oci_client.manifest(
        image_reference=image_reference,
        absent_ok=True,
        accept=om.MimeTypes.prefer_multiarch,
    )

    if not manifest:
        return True # nothing to do if image does not exist

    if image_reference.has_symbolical_tag:
        purge = True
    elif image_reference.has_digest_tag:
        purge = False # no need to "purge" if we were passed a digest-tag
    else:
        raise ValueError(f'cannot remove image w/o tag: {str(image_reference)}')

    oci_client.delete_manifest(
        image_reference=image_reference,
        purge=purge,
    )

    if isinstance(manifest, om.OciImageManifest):
        return True

    if not isinstance(manifest, om.OciImageManifestList):
        raise ValueError(f'did not expect type {manifest=} {type(manifest)} - this is a bug')

    # multi-arch-case - try to guess other tags, and purge those
    manifest: om.OciImageManifestList

    def iter_platform_refs():
        repository = image_reference.ref_without_tag
        base_tag = image_reference.tag

        for submanifest in manifest.manifests:
            p = submanifest.platform
            yield f'{repository}:{base_tag}-{p.os}-{p.architecture}'

    for ref in iter_platform_refs():
        if not oci_client.head_manifest(
            image_reference=ref,
            absent_ok=True,
        ):
            logger.warning(f'did not find {ref=} - ignoring')
            continue

        oci_client.delete_manifest(
            image_reference=ref,
            purge=True,
        )

    return True
