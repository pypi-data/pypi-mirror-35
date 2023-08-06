import datetime
import typing
import autoboto
from enum import Enum
import botocore.response
import dataclasses


@dataclasses.dataclass
class AuthorizationData(autoboto.ShapeBase):
    """
    An object representing authorization data for an Amazon ECR registry.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorization_token",
                "authorizationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "expires_at",
                "expiresAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "proxy_endpoint",
                "proxyEndpoint",
                autoboto.TypeInfo(str),
            ),
        ]

    # A base64-encoded string that contains authorization data for the specified
    # Amazon ECR registry. When the string is decoded, it is presented in the
    # format `user:password` for private registry authentication using `docker
    # login`.
    authorization_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Unix time in seconds and milliseconds when the authorization token
    # expires. Authorization tokens are valid for 12 hours.
    expires_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The registry URL to use for this authorization token in a `docker login`
    # command. The Amazon ECR registry URL format is
    # `https://aws_account_id.dkr.ecr.region.amazonaws.com`. For example,
    # `https://012345678910.dkr.ecr.us-east-1.amazonaws.com`..
    proxy_endpoint: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchCheckLayerAvailabilityRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_digests",
                "layerDigests",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository that is associated with the image layers to
    # check.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The digests of the image layers to check.
    layer_digests: typing.List[str] = dataclasses.field(default_factory=list, )

    # The AWS account ID associated with the registry that contains the image
    # layers to check. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchCheckLayerAvailabilityResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "layers",
                "layers",
                autoboto.TypeInfo(typing.List[Layer]),
            ),
            (
                "failures",
                "failures",
                autoboto.TypeInfo(typing.List[LayerFailure]),
            ),
        ]

    # A list of image layer objects corresponding to the image layer references
    # in the request.
    layers: typing.List["Layer"] = dataclasses.field(default_factory=list, )

    # Any failures associated with the call.
    failures: typing.List["LayerFailure"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchDeleteImageRequest(autoboto.ShapeBase):
    """
    Deletes specified images within a specified repository. Images are specified
    with either the `imageTag` or `imageDigest`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "image_ids",
                "imageIds",
                autoboto.TypeInfo(typing.List[ImageIdentifier]),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The repository that contains the image to delete.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of image ID references that correspond to images to delete. The
    # format of the `imageIds` reference is `imageTag=tag` or
    # `imageDigest=digest`.
    image_ids: typing.List["ImageIdentifier"] = dataclasses.field(
        default_factory=list,
    )

    # The AWS account ID associated with the registry that contains the image to
    # delete. If you do not specify a registry, the default registry is assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchDeleteImageResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image_ids",
                "imageIds",
                autoboto.TypeInfo(typing.List[ImageIdentifier]),
            ),
            (
                "failures",
                "failures",
                autoboto.TypeInfo(typing.List[ImageFailure]),
            ),
        ]

    # The image IDs of the deleted images.
    image_ids: typing.List["ImageIdentifier"] = dataclasses.field(
        default_factory=list,
    )

    # Any failures associated with the call.
    failures: typing.List["ImageFailure"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchGetImageRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "image_ids",
                "imageIds",
                autoboto.TypeInfo(typing.List[ImageIdentifier]),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "accepted_media_types",
                "acceptedMediaTypes",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The repository that contains the images to describe.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of image ID references that correspond to images to describe. The
    # format of the `imageIds` reference is `imageTag=tag` or
    # `imageDigest=digest`.
    image_ids: typing.List["ImageIdentifier"] = dataclasses.field(
        default_factory=list,
    )

    # The AWS account ID associated with the registry that contains the images to
    # describe. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The accepted media types for the request.

    # Valid values: `application/vnd.docker.distribution.manifest.v1+json` |
    # `application/vnd.docker.distribution.manifest.v2+json` |
    # `application/vnd.oci.image.manifest.v1+json`
    accepted_media_types: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchGetImageResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "images",
                "images",
                autoboto.TypeInfo(typing.List[Image]),
            ),
            (
                "failures",
                "failures",
                autoboto.TypeInfo(typing.List[ImageFailure]),
            ),
        ]

    # A list of image objects corresponding to the image references in the
    # request.
    images: typing.List["Image"] = dataclasses.field(default_factory=list, )

    # Any failures associated with the call.
    failures: typing.List["ImageFailure"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CompleteLayerUploadRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id",
                "uploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_digests",
                "layerDigests",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository to associate with the image layer.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The upload ID from a previous InitiateLayerUpload operation to associate
    # with the image layer.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The `sha256` digest of the image layer.
    layer_digests: typing.List[str] = dataclasses.field(default_factory=list, )

    # The AWS account ID associated with the registry to which to upload layers.
    # If you do not specify a registry, the default registry is assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CompleteLayerUploadResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id",
                "uploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_digest",
                "layerDigest",
                autoboto.TypeInfo(str),
            ),
        ]

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The upload ID associated with the layer.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The `sha256` digest of the image layer.
    layer_digest: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateRepositoryRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name to use for the repository. The repository name may be specified on
    # its own (such as `nginx-web-app`) or it can be prepended with a namespace
    # to group the repository into a category (such as `project-a/nginx-web-
    # app`).
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateRepositoryResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository",
                "repository",
                autoboto.TypeInfo(Repository),
            ),
        ]

    # The repository that was created.
    repository: "Repository" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteLifecyclePolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry that contains the
    # repository. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLifecyclePolicyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "lifecycle_policy_text",
                "lifecyclePolicyText",
                autoboto.TypeInfo(str),
            ),
            (
                "last_evaluated_at",
                "lastEvaluatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The JSON lifecycle policy text.
    lifecycle_policy_text: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time stamp of the last time that the lifecycle policy was run.
    last_evaluated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteRepositoryPolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository that is associated with the repository policy to
    # delete.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry that contains the
    # repository policy to delete. If you do not specify a registry, the default
    # registry is assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRepositoryPolicyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_text",
                "policyText",
                autoboto.TypeInfo(str),
            ),
        ]

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The JSON repository policy that was deleted from the repository.
    policy_text: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRepositoryRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "force",
                "force",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the repository to delete.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry that contains the
    # repository to delete. If you do not specify a registry, the default
    # registry is assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If a repository contains images, forces the deletion.
    force: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRepositoryResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository",
                "repository",
                autoboto.TypeInfo(Repository),
            ),
        ]

    # The repository that was deleted.
    repository: "Repository" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeImagesFilter(autoboto.ShapeBase):
    """
    An object representing a filter on a DescribeImages operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_status",
                "tagStatus",
                autoboto.TypeInfo(TagStatus),
            ),
        ]

    # The tag status with which to filter your DescribeImages results. You can
    # filter results based on whether they are `TAGGED` or `UNTAGGED`.
    tag_status: "TagStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeImagesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "image_ids",
                "imageIds",
                autoboto.TypeInfo(typing.List[ImageIdentifier]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "filter",
                "filter",
                autoboto.TypeInfo(DescribeImagesFilter),
            ),
        ]

    # A list of repositories to describe. If this parameter is omitted, then all
    # repositories in a registry are described.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry that contains the
    # repository in which to describe images. If you do not specify a registry,
    # the default registry is assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of image IDs for the requested repository.
    image_ids: typing.List["ImageIdentifier"] = dataclasses.field(
        default_factory=list,
    )

    # The `nextToken` value returned from a previous paginated `DescribeImages`
    # request where `maxResults` was used and the results exceeded the value of
    # that parameter. Pagination continues from the end of the previous results
    # that returned the `nextToken` value. This value is `null` when there are no
    # more results to return. This option cannot be used when you specify images
    # with `imageIds`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of repository results returned by `DescribeImages` in
    # paginated output. When this parameter is used, `DescribeImages` only
    # returns `maxResults` results in a single page along with a `nextToken`
    # response element. The remaining results of the initial request can be seen
    # by sending another `DescribeImages` request with the returned `nextToken`
    # value. This value can be between 1 and 100. If this parameter is not used,
    # then `DescribeImages` returns up to 100 results and a `nextToken` value, if
    # applicable. This option cannot be used when you specify images with
    # `imageIds`.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The filter key and value with which to filter your `DescribeImages`
    # results.
    filter: "DescribeImagesFilter" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeImagesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image_details",
                "imageDetails",
                autoboto.TypeInfo(typing.List[ImageDetail]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of ImageDetail objects that contain data about the image.
    image_details: typing.List["ImageDetail"] = dataclasses.field(
        default_factory=list,
    )

    # The `nextToken` value to include in a future `DescribeImages` request. When
    # the results of a `DescribeImages` request exceed `maxResults`, this value
    # can be used to retrieve the next page of results. This value is `null` when
    # there are no more results to return.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRepositoriesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_names",
                "repositoryNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The AWS account ID associated with the registry that contains the
    # repositories to be described. If you do not specify a registry, the default
    # registry is assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of repositories to describe. If this parameter is omitted, then all
    # repositories in a registry are described.
    repository_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The `nextToken` value returned from a previous paginated
    # `DescribeRepositories` request where `maxResults` was used and the results
    # exceeded the value of that parameter. Pagination continues from the end of
    # the previous results that returned the `nextToken` value. This value is
    # `null` when there are no more results to return. This option cannot be used
    # when you specify repositories with `repositoryNames`.

    # This token should be treated as an opaque identifier that is only used to
    # retrieve the next items in a list and not for other programmatic purposes.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of repository results returned by `DescribeRepositories`
    # in paginated output. When this parameter is used, `DescribeRepositories`
    # only returns `maxResults` results in a single page along with a `nextToken`
    # response element. The remaining results of the initial request can be seen
    # by sending another `DescribeRepositories` request with the returned
    # `nextToken` value. This value can be between 1 and 100. If this parameter
    # is not used, then `DescribeRepositories` returns up to 100 results and a
    # `nextToken` value, if applicable. This option cannot be used when you
    # specify repositories with `repositoryNames`.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRepositoriesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repositories",
                "repositories",
                autoboto.TypeInfo(typing.List[Repository]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of repository objects corresponding to valid repositories.
    repositories: typing.List["Repository"] = dataclasses.field(
        default_factory=list,
    )

    # The `nextToken` value to include in a future `DescribeRepositories`
    # request. When the results of a `DescribeRepositories` request exceed
    # `maxResults`, this value can be used to retrieve the next page of results.
    # This value is `null` when there are no more results to return.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EmptyUploadException(autoboto.ShapeBase):
    """
    The specified layer upload does not contain any layer parts.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message associated with the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAuthorizationTokenRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_ids",
                "registryIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A list of AWS account IDs that are associated with the registries for which
    # to get authorization tokens. If you do not specify a registry, the default
    # registry is assumed.
    registry_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class GetAuthorizationTokenResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorization_data",
                "authorizationData",
                autoboto.TypeInfo(typing.List[AuthorizationData]),
            ),
        ]

    # A list of authorization token data objects that correspond to the
    # `registryIds` values in the request.
    authorization_data: typing.List["AuthorizationData"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetDownloadUrlForLayerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_digest",
                "layerDigest",
                autoboto.TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository that is associated with the image layer to
    # download.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The digest of the image layer to download.
    layer_digest: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry that contains the image
    # layer to download. If you do not specify a registry, the default registry
    # is assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDownloadUrlForLayerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "download_url",
                "downloadUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_digest",
                "layerDigest",
                autoboto.TypeInfo(str),
            ),
        ]

    # The pre-signed Amazon S3 download URL for the requested layer.
    download_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The digest of the image layer to download.
    layer_digest: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLifecyclePolicyPreviewRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "image_ids",
                "imageIds",
                autoboto.TypeInfo(typing.List[ImageIdentifier]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "filter",
                "filter",
                autoboto.TypeInfo(LifecyclePolicyPreviewFilter),
            ),
        ]

    # The name of the repository.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry that contains the
    # repository. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of imageIDs to be included.
    image_ids: typing.List["ImageIdentifier"] = dataclasses.field(
        default_factory=list,
    )

    # The `nextToken` value returned from a previous paginated
    # `GetLifecyclePolicyPreviewRequest` request where `maxResults` was used and
    # the results exceeded the value of that parameter. Pagination continues from
    # the end of the previous results that returned the `nextToken` value. This
    # value is `null` when there are no more results to return. This option
    # cannot be used when you specify images with `imageIds`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of repository results returned by
    # `GetLifecyclePolicyPreviewRequest` in paginated output. When this parameter
    # is used, `GetLifecyclePolicyPreviewRequest` only returns `maxResults`
    # results in a single page along with a `nextToken` response element. The
    # remaining results of the initial request can be seen by sending another
    # `GetLifecyclePolicyPreviewRequest` request with the returned `nextToken`
    # value. This value can be between 1 and 100. If this parameter is not used,
    # then `GetLifecyclePolicyPreviewRequest` returns up to 100 results and a
    # `nextToken` value, if applicable. This option cannot be used when you
    # specify images with `imageIds`.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional parameter that filters results based on image tag status and
    # all tags, if tagged.
    filter: "LifecyclePolicyPreviewFilter" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetLifecyclePolicyPreviewResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "lifecycle_policy_text",
                "lifecyclePolicyText",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(LifecyclePolicyPreviewStatus),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "preview_results",
                "previewResults",
                autoboto.TypeInfo(typing.List[LifecyclePolicyPreviewResult]),
            ),
            (
                "summary",
                "summary",
                autoboto.TypeInfo(LifecyclePolicyPreviewSummary),
            ),
        ]

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The JSON lifecycle policy text.
    lifecycle_policy_text: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the lifecycle policy preview request.
    status: "LifecyclePolicyPreviewStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The `nextToken` value to include in a future `GetLifecyclePolicyPreview`
    # request. When the results of a `GetLifecyclePolicyPreview` request exceed
    # `maxResults`, this value can be used to retrieve the next page of results.
    # This value is `null` when there are no more results to return.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The results of the lifecycle policy preview request.
    preview_results: typing.List["LifecyclePolicyPreviewResult"
                                ] = dataclasses.field(
                                    default_factory=list,
                                )

    # The list of images that is returned as a result of the action.
    summary: "LifecyclePolicyPreviewSummary" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetLifecyclePolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry that contains the
    # repository. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLifecyclePolicyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "lifecycle_policy_text",
                "lifecyclePolicyText",
                autoboto.TypeInfo(str),
            ),
            (
                "last_evaluated_at",
                "lastEvaluatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The JSON lifecycle policy text.
    lifecycle_policy_text: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time stamp of the last time that the lifecycle policy was run.
    last_evaluated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetRepositoryPolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository with the policy to retrieve.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry that contains the
    # repository. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRepositoryPolicyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_text",
                "policyText",
                autoboto.TypeInfo(str),
            ),
        ]

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The JSON repository policy text associated with the repository.
    policy_text: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Image(autoboto.ShapeBase):
    """
    An object representing an Amazon ECR image.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "image_id",
                "imageId",
                autoboto.TypeInfo(ImageIdentifier),
            ),
            (
                "image_manifest",
                "imageManifest",
                autoboto.TypeInfo(str),
            ),
        ]

    # The AWS account ID associated with the registry containing the image.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the repository associated with the image.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An object containing the image tag and image digest associated with an
    # image.
    image_id: "ImageIdentifier" = dataclasses.field(default_factory=dict, )

    # The image manifest associated with the image.
    image_manifest: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ImageActionType(Enum):
    EXPIRE = "EXPIRE"


@dataclasses.dataclass
class ImageAlreadyExistsException(autoboto.ShapeBase):
    """
    The specified image has already been pushed, and there were no changes to the
    manifest or image tag after the last push.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message associated with the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImageDetail(autoboto.ShapeBase):
    """
    An object that describes an image returned by a DescribeImages operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "image_digest",
                "imageDigest",
                autoboto.TypeInfo(str),
            ),
            (
                "image_tags",
                "imageTags",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "image_size_in_bytes",
                "imageSizeInBytes",
                autoboto.TypeInfo(int),
            ),
            (
                "image_pushed_at",
                "imagePushedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The AWS account ID associated with the registry to which this image
    # belongs.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the repository to which this image belongs.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The `sha256` digest of the image manifest.
    image_digest: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of tags associated with this image.
    image_tags: typing.List[str] = dataclasses.field(default_factory=list, )

    # The size, in bytes, of the image in the repository.

    # Beginning with Docker version 1.9, the Docker client compresses image
    # layers before pushing them to a V2 Docker registry. The output of the
    # `docker images` command shows the uncompressed image size, so it may return
    # a larger image size than the image sizes returned by DescribeImages.
    image_size_in_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time, expressed in standard JavaScript date format, at which
    # the current image was pushed to the repository.
    image_pushed_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ImageFailure(autoboto.ShapeBase):
    """
    An object representing an Amazon ECR image failure.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image_id",
                "imageId",
                autoboto.TypeInfo(ImageIdentifier),
            ),
            (
                "failure_code",
                "failureCode",
                autoboto.TypeInfo(ImageFailureCode),
            ),
            (
                "failure_reason",
                "failureReason",
                autoboto.TypeInfo(str),
            ),
        ]

    # The image ID associated with the failure.
    image_id: "ImageIdentifier" = dataclasses.field(default_factory=dict, )

    # The code associated with the failure.
    failure_code: "ImageFailureCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The reason for the failure.
    failure_reason: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ImageFailureCode(Enum):
    InvalidImageDigest = "InvalidImageDigest"
    InvalidImageTag = "InvalidImageTag"
    ImageTagDoesNotMatchDigest = "ImageTagDoesNotMatchDigest"
    ImageNotFound = "ImageNotFound"
    MissingDigestAndTag = "MissingDigestAndTag"


@dataclasses.dataclass
class ImageIdentifier(autoboto.ShapeBase):
    """
    An object with identifying information for an Amazon ECR image.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image_digest",
                "imageDigest",
                autoboto.TypeInfo(str),
            ),
            (
                "image_tag",
                "imageTag",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `sha256` digest of the image manifest.
    image_digest: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tag used for the image.
    image_tag: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImageNotFoundException(autoboto.ShapeBase):
    """
    The image requested does not exist in the specified repository.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InitiateLayerUploadRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository to which you intend to upload layers.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry to which you intend to
    # upload layers. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InitiateLayerUploadResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "upload_id",
                "uploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "part_size",
                "partSize",
                autoboto.TypeInfo(int),
            ),
        ]

    # The upload ID for the layer upload. This parameter is passed to further
    # UploadLayerPart and CompleteLayerUpload operations.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The size, in bytes, that Amazon ECR expects future layer part uploads to
    # be.
    part_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidLayerException(autoboto.ShapeBase):
    """
    The layer digest calculation performed by Amazon ECR upon receipt of the image
    layer does not match the digest specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message associated with the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidLayerPartException(autoboto.ShapeBase):
    """
    The layer part size is not valid, or the first byte specified is not consecutive
    to the last byte of a previous layer part upload.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id",
                "uploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "last_valid_byte_received",
                "lastValidByteReceived",
                autoboto.TypeInfo(int),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The registry ID associated with the exception.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The repository name associated with the exception.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The upload ID associated with the exception.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The last valid byte received from the layer part upload that is associated
    # with the exception.
    last_valid_byte_received: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The error message associated with the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterException(autoboto.ShapeBase):
    """
    The specified parameter is invalid. Review the available parameters for the API
    request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message associated with the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Layer(autoboto.ShapeBase):
    """
    An object representing an Amazon ECR image layer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "layer_digest",
                "layerDigest",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_availability",
                "layerAvailability",
                autoboto.TypeInfo(LayerAvailability),
            ),
            (
                "layer_size",
                "layerSize",
                autoboto.TypeInfo(int),
            ),
            (
                "media_type",
                "mediaType",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `sha256` digest of the image layer.
    layer_digest: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The availability status of the image layer.
    layer_availability: "LayerAvailability" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The size, in bytes, of the image layer.
    layer_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The media type of the layer, such as
    # `application/vnd.docker.image.rootfs.diff.tar.gzip` or
    # `application/vnd.oci.image.layer.v1.tar+gzip`.
    media_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LayerAlreadyExistsException(autoboto.ShapeBase):
    """
    The image layer already exists in the associated repository.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message associated with the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class LayerAvailability(Enum):
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"


@dataclasses.dataclass
class LayerFailure(autoboto.ShapeBase):
    """
    An object representing an Amazon ECR image layer failure.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "layer_digest",
                "layerDigest",
                autoboto.TypeInfo(str),
            ),
            (
                "failure_code",
                "failureCode",
                autoboto.TypeInfo(LayerFailureCode),
            ),
            (
                "failure_reason",
                "failureReason",
                autoboto.TypeInfo(str),
            ),
        ]

    # The layer digest associated with the failure.
    layer_digest: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The failure code associated with the failure.
    failure_code: "LayerFailureCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The reason for the failure.
    failure_reason: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class LayerFailureCode(Enum):
    InvalidLayerDigest = "InvalidLayerDigest"
    MissingLayerDigest = "MissingLayerDigest"


@dataclasses.dataclass
class LayerInaccessibleException(autoboto.ShapeBase):
    """
    The specified layer is not available because it is not associated with an image.
    Unassociated image layers may be cleaned up at any time.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message associated with the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class LayerPartBlob(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class LayerPartTooSmallException(autoboto.ShapeBase):
    """
    Layer parts must be at least 5 MiB in size.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message associated with the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LayersNotFoundException(autoboto.ShapeBase):
    """
    The specified layers could not be found, or the specified layer is not valid for
    this repository.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message associated with the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LifecyclePolicyNotFoundException(autoboto.ShapeBase):
    """
    The lifecycle policy could not be found, and no policy is set to the repository.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LifecyclePolicyPreviewFilter(autoboto.ShapeBase):
    """
    The filter for the lifecycle policy preview.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_status",
                "tagStatus",
                autoboto.TypeInfo(TagStatus),
            ),
        ]

    # The tag status of the image.
    tag_status: "TagStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LifecyclePolicyPreviewInProgressException(autoboto.ShapeBase):
    """
    The previous lifecycle policy preview request has not completed. Please try
    again later.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LifecyclePolicyPreviewNotFoundException(autoboto.ShapeBase):
    """
    There is no dry run for this repository.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LifecyclePolicyPreviewResult(autoboto.ShapeBase):
    """
    The result of the lifecycle policy preview.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image_tags",
                "imageTags",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "image_digest",
                "imageDigest",
                autoboto.TypeInfo(str),
            ),
            (
                "image_pushed_at",
                "imagePushedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "action",
                "action",
                autoboto.TypeInfo(LifecyclePolicyRuleAction),
            ),
            (
                "applied_rule_priority",
                "appliedRulePriority",
                autoboto.TypeInfo(int),
            ),
        ]

    # The list of tags associated with this image.
    image_tags: typing.List[str] = dataclasses.field(default_factory=list, )

    # The `sha256` digest of the image manifest.
    image_digest: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date and time, expressed in standard JavaScript date format, at which
    # the current image was pushed to the repository.
    image_pushed_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of action to be taken.
    action: "LifecyclePolicyRuleAction" = dataclasses.field(
        default_factory=dict,
    )

    # The priority of the applied rule.
    applied_rule_priority: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class LifecyclePolicyPreviewStatus(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    EXPIRED = "EXPIRED"
    FAILED = "FAILED"


@dataclasses.dataclass
class LifecyclePolicyPreviewSummary(autoboto.ShapeBase):
    """
    The summary of the lifecycle policy preview request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "expiring_image_total_count",
                "expiringImageTotalCount",
                autoboto.TypeInfo(int),
            ),
        ]

    # The number of expiring images.
    expiring_image_total_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LifecyclePolicyRuleAction(autoboto.ShapeBase):
    """
    The type of action to be taken.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(ImageActionType),
            ),
        ]

    # The type of action to be taken.
    type: "ImageActionType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    The operation did not succeed because it would have exceeded a service limit for
    your account. For more information, see [Amazon ECR Default Service
    Limits](http://docs.aws.amazon.com/AmazonECR/latest/userguide/service_limits.html)
    in the Amazon Elastic Container Registry User Guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message associated with the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListImagesFilter(autoboto.ShapeBase):
    """
    An object representing a filter on a ListImages operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_status",
                "tagStatus",
                autoboto.TypeInfo(TagStatus),
            ),
        ]

    # The tag status with which to filter your ListImages results. You can filter
    # results based on whether they are `TAGGED` or `UNTAGGED`.
    tag_status: "TagStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListImagesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "filter",
                "filter",
                autoboto.TypeInfo(ListImagesFilter),
            ),
        ]

    # The repository with image IDs to be listed.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry that contains the
    # repository in which to list images. If you do not specify a registry, the
    # default registry is assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The `nextToken` value returned from a previous paginated `ListImages`
    # request where `maxResults` was used and the results exceeded the value of
    # that parameter. Pagination continues from the end of the previous results
    # that returned the `nextToken` value. This value is `null` when there are no
    # more results to return.

    # This token should be treated as an opaque identifier that is only used to
    # retrieve the next items in a list and not for other programmatic purposes.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of image results returned by `ListImages` in paginated
    # output. When this parameter is used, `ListImages` only returns `maxResults`
    # results in a single page along with a `nextToken` response element. The
    # remaining results of the initial request can be seen by sending another
    # `ListImages` request with the returned `nextToken` value. This value can be
    # between 1 and 100. If this parameter is not used, then `ListImages` returns
    # up to 100 results and a `nextToken` value, if applicable.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The filter key and value with which to filter your `ListImages` results.
    filter: "ListImagesFilter" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ListImagesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image_ids",
                "imageIds",
                autoboto.TypeInfo(typing.List[ImageIdentifier]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of image IDs for the requested repository.
    image_ids: typing.List["ImageIdentifier"] = dataclasses.field(
        default_factory=list,
    )

    # The `nextToken` value to include in a future `ListImages` request. When the
    # results of a `ListImages` request exceed `maxResults`, this value can be
    # used to retrieve the next page of results. This value is `null` when there
    # are no more results to return.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutImageRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "image_manifest",
                "imageManifest",
                autoboto.TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "image_tag",
                "imageTag",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository in which to put the image.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The image manifest corresponding to the image to be uploaded.
    image_manifest: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry that contains the
    # repository in which to put the image. If you do not specify a registry, the
    # default registry is assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tag to associate with the image. This parameter is required for images
    # that use the Docker Image Manifest V2 Schema 2 or OCI formats.
    image_tag: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutImageResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image",
                "image",
                autoboto.TypeInfo(Image),
            ),
        ]

    # Details of the image uploaded.
    image: "Image" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PutLifecyclePolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "lifecycle_policy_text",
                "lifecyclePolicyText",
                autoboto.TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository to receive the policy.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The JSON repository policy text to apply to the repository.
    lifecycle_policy_text: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry that contains the
    # repository. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutLifecyclePolicyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "lifecycle_policy_text",
                "lifecyclePolicyText",
                autoboto.TypeInfo(str),
            ),
        ]

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The JSON repository policy text.
    lifecycle_policy_text: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Repository(autoboto.ShapeBase):
    """
    An object representing a repository.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_arn",
                "repositoryArn",
                autoboto.TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_uri",
                "repositoryUri",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Resource Name (ARN) that identifies the repository. The ARN
    # contains the `arn:aws:ecr` namespace, followed by the region of the
    # repository, AWS account ID of the repository owner, repository namespace,
    # and repository name. For example,
    # `arn:aws:ecr:region:012345678910:repository/test`.
    repository_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry that contains the
    # repository.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the repository.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URI for the repository. You can use this URI for Docker `push` or
    # `pull` operations.
    repository_uri: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time, in JavaScript date format, when the repository was
    # created.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RepositoryAlreadyExistsException(autoboto.ShapeBase):
    """
    The specified repository already exists in the specified registry.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message associated with the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RepositoryNotEmptyException(autoboto.ShapeBase):
    """
    The specified repository contains images. To delete a repository that contains
    images, you must force the deletion with the `force` parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message associated with the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RepositoryNotFoundException(autoboto.ShapeBase):
    """
    The specified repository could not be found. Check the spelling of the specified
    repository and ensure that you are performing operations on the correct
    registry.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message associated with the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RepositoryPolicyNotFoundException(autoboto.ShapeBase):
    """
    The specified repository and registry combination does not have an associated
    repository policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message associated with the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServerException(autoboto.ShapeBase):
    """
    These errors are usually caused by a server-side issue.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message associated with the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetRepositoryPolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_text",
                "policyText",
                autoboto.TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "force",
                "force",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the repository to receive the policy.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The JSON repository policy text to apply to the repository.
    policy_text: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The AWS account ID associated with the registry that contains the
    # repository. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the policy you are attempting to set on a repository policy would
    # prevent you from setting another policy in the future, you must force the
    # SetRepositoryPolicy operation. This is intended to prevent accidental
    # repository lock outs.
    force: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetRepositoryPolicyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_text",
                "policyText",
                autoboto.TypeInfo(str),
            ),
        ]

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The JSON repository policy text applied to the repository.
    policy_text: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartLifecyclePolicyPreviewRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "lifecycle_policy_text",
                "lifecyclePolicyText",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository to be evaluated.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry that contains the
    # repository. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The policy to be evaluated against. If you do not specify a policy, the
    # current policy for the repository is used.
    lifecycle_policy_text: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartLifecyclePolicyPreviewResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "lifecycle_policy_text",
                "lifecyclePolicyText",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(LifecyclePolicyPreviewStatus),
            ),
        ]

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The JSON repository policy text.
    lifecycle_policy_text: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the lifecycle policy preview request.
    status: "LifecyclePolicyPreviewStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class TagStatus(Enum):
    TAGGED = "TAGGED"
    UNTAGGED = "UNTAGGED"


@dataclasses.dataclass
class UploadLayerPartRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id",
                "uploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "part_first_byte",
                "partFirstByte",
                autoboto.TypeInfo(int),
            ),
            (
                "part_last_byte",
                "partLastByte",
                autoboto.TypeInfo(int),
            ),
            (
                "layer_part_blob",
                "layerPartBlob",
                autoboto.TypeInfo(typing.Any),
            ),
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository to which you are uploading layer parts.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The upload ID from a previous InitiateLayerUpload operation to associate
    # with the layer part upload.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The integer value of the first byte of the layer part.
    part_first_byte: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The integer value of the last byte of the layer part.
    part_last_byte: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The base64-encoded layer part payload.
    layer_part_blob: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS account ID associated with the registry to which you are uploading
    # layer parts. If you do not specify a registry, the default registry is
    # assumed.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UploadLayerPartResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_id",
                "registryId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id",
                "uploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "last_byte_received",
                "lastByteReceived",
                autoboto.TypeInfo(int),
            ),
        ]

    # The registry ID associated with the request.
    registry_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The repository name associated with the request.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The upload ID associated with the request.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The integer value of the last byte received in the request.
    last_byte_received: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UploadNotFoundException(autoboto.ShapeBase):
    """
    The upload could not be found, or the specified upload id is not valid for this
    repository.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message associated with the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
