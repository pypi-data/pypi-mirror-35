import datetime
import typing
import autoboto
import botocore.response
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AccountActionRequiredException(autoboto.ShapeBase):
    """
    Account Action is required in order to continue the request.
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

    # The Exception Error Message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BadRequestException(autoboto.ShapeBase):
    """
    The request cannot be processed because some parameter is not valid or the
    project state prevents the operation from being performed.
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

    # The Exception Error Message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BundleDetails(autoboto.ShapeBase):
    """
    The details of the bundle.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_id",
                "bundleId",
                autoboto.TypeInfo(str),
            ),
            (
                "title",
                "title",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "icon_url",
                "iconUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "available_platforms",
                "availablePlatforms",
                autoboto.TypeInfo(typing.List[Platform]),
            ),
        ]

    # Unique bundle identifier.
    bundle_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Title of the download bundle.
    title: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Version of the download bundle.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Description of the download bundle.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Icon for the download bundle.
    icon_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Developer desktop or mobile app or website platforms.
    available_platforms: typing.List["Platform"] = dataclasses.field(
        default_factory=list,
    )


class Contents(botocore.response.StreamingBody):
    """
    Binary file data.
    """
    pass


@dataclasses.dataclass
class CreateProjectRequest(autoboto.ShapeBase):
    """
    Request structure used to request a project be created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "region",
                "region",
                autoboto.TypeInfo(str),
            ),
            (
                "contents",
                "contents",
                autoboto.TypeInfo(typing.Any),
            ),
            (
                "snapshot_id",
                "snapshotId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the project.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Default region where project resources should be created.
    region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # ZIP or YAML file which contains configuration settings to be used when
    # creating the project. This may be the contents of the file downloaded from
    # the URL provided in an export project operation.
    contents: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique identifier for an exported snapshot of project configuration. This
    # snapshot identifier is included in the share URL when a project is
    # exported.
    snapshot_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateProjectResult(autoboto.ShapeBase):
    """
    Result structure used in response to a request to create a project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "details",
                "details",
                autoboto.TypeInfo(ProjectDetails),
            ),
        ]

    # Detailed information about the created AWS Mobile Hub project.
    details: "ProjectDetails" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteProjectRequest(autoboto.ShapeBase):
    """
    Request structure used to request a project be deleted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Unique project identifier.
    project_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProjectResult(autoboto.ShapeBase):
    """
    Result structure used in response to request to delete a project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deleted_resources",
                "deletedResources",
                autoboto.TypeInfo(typing.List[Resource]),
            ),
            (
                "orphaned_resources",
                "orphanedResources",
                autoboto.TypeInfo(typing.List[Resource]),
            ),
        ]

    # Resources which were deleted.
    deleted_resources: typing.List["Resource"] = dataclasses.field(
        default_factory=list,
    )

    # Resources which were not deleted, due to a risk of losing potentially
    # important data or files.
    orphaned_resources: typing.List["Resource"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeBundleRequest(autoboto.ShapeBase):
    """
    Request structure to request the details of a specific bundle.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_id",
                "bundleId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Unique bundle identifier.
    bundle_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeBundleResult(autoboto.ShapeBase):
    """
    Result structure contains the details of the bundle.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "details",
                "details",
                autoboto.TypeInfo(BundleDetails),
            ),
        ]

    # The details of the bundle.
    details: "BundleDetails" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeProjectRequest(autoboto.ShapeBase):
    """
    Request structure used to request details about a project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                autoboto.TypeInfo(str),
            ),
            (
                "sync_from_resources",
                "syncFromResources",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Unique project identifier.
    project_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If set to true, causes AWS Mobile Hub to synchronize information from other
    # services, e.g., update state of AWS CloudFormation stacks in the AWS Mobile
    # Hub project.
    sync_from_resources: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeProjectResult(autoboto.ShapeBase):
    """
    Result structure used for requests of project details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "details",
                "details",
                autoboto.TypeInfo(ProjectDetails),
            ),
        ]

    # Detailed information about an AWS Mobile Hub project.
    details: "ProjectDetails" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ExportBundleRequest(autoboto.ShapeBase):
    """
    Request structure used to request generation of custom SDK and tool packages
    required to integrate mobile web or app clients with backed AWS resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_id",
                "bundleId",
                autoboto.TypeInfo(str),
            ),
            (
                "project_id",
                "projectId",
                autoboto.TypeInfo(str),
            ),
            (
                "platform",
                "platform",
                autoboto.TypeInfo(Platform),
            ),
        ]

    # Unique bundle identifier.
    bundle_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Unique project identifier.
    project_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Developer desktop or target application platform.
    platform: "Platform" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ExportBundleResult(autoboto.ShapeBase):
    """
    Result structure which contains link to download custom-generated SDK and tool
    packages used to integrate mobile web or app clients with backed AWS resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "download_url",
                "downloadUrl",
                autoboto.TypeInfo(str),
            ),
        ]

    # URL which contains the custom-generated SDK and tool packages used to
    # integrate the client mobile app or web app with the AWS resources created
    # by the AWS Mobile Hub project.
    download_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExportProjectRequest(autoboto.ShapeBase):
    """
    Request structure used in requests to export project configuration details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Unique project identifier.
    project_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExportProjectResult(autoboto.ShapeBase):
    """
    Result structure used for requests to export project configuration details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "download_url",
                "downloadUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "share_url",
                "shareUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "snapshot_id",
                "snapshotId",
                autoboto.TypeInfo(str),
            ),
        ]

    # URL which can be used to download the exported project configuation
    # file(s).
    download_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # URL which can be shared to allow other AWS users to create their own
    # project in AWS Mobile Hub with the same configuration as the specified
    # project. This URL pertains to a snapshot in time of the project
    # configuration that is created when this API is called. If you want to share
    # additional changes to your project configuration, then you will need to
    # create and share a new snapshot by calling this method again.
    share_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Unique identifier for the exported snapshot of the project configuration.
    # This snapshot identifier is included in the share URL.
    snapshot_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalFailureException(autoboto.ShapeBase):
    """
    The service has encountered an unexpected error condition which prevents it from
    servicing the request.
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

    # The Exception Error Message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    There are too many AWS Mobile Hub projects in the account or the account has
    exceeded the maximum number of resources in some AWS service. You should create
    another sub-account using AWS Organizations or remove some resources and retry
    your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "retry_after_seconds",
                "retryAfterSeconds",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Exception Error Message.
    retry_after_seconds: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Exception Error Message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBundlesRequest(autoboto.ShapeBase):
    """
    Request structure to request all available bundles.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Maximum number of records to list in a single response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Pagination token. Set to null to start listing bundles from start. If non-
    # null pagination token is returned in a result, then pass its value in here
    # in another request to list more bundles.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBundlesResult(autoboto.ShapeBase):
    """
    Result structure contains a list of all available bundles with details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_list",
                "bundleList",
                autoboto.TypeInfo(typing.List[BundleDetails]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of bundles.
    bundle_list: typing.List["BundleDetails"] = dataclasses.field(
        default_factory=list,
    )

    # Pagination token. If non-null pagination token is returned in a result,
    # then pass its value in another request to fetch more entries.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListProjectsRequest(autoboto.ShapeBase):
    """
    Request structure used to request projects list in AWS Mobile Hub.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Maximum number of records to list in a single response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Pagination token. Set to null to start listing projects from start. If non-
    # null pagination token is returned in a result, then pass its value in here
    # in another request to list more projects.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListProjectsResult(autoboto.ShapeBase):
    """
    Result structure used for requests to list projects in AWS Mobile Hub.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "projects",
                "projects",
                autoboto.TypeInfo(typing.List[ProjectSummary]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # List of projects.
    projects: typing.List["ProjectSummary"] = dataclasses.field(
        default_factory=list,
    )

    # Pagination token. Set to null to start listing records from start. If non-
    # null pagination token is returned in a result, then pass its value in here
    # in another request to list more entries.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotFoundException(autoboto.ShapeBase):
    """
    No entity can be found with the specified identifier.
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

    # The Exception Error Message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class Platform(Enum):
    """
    Developer desktop or target mobile app or website platform.
    """
    OSX = "OSX"
    WINDOWS = "WINDOWS"
    LINUX = "LINUX"
    OBJC = "OBJC"
    SWIFT = "SWIFT"
    ANDROID = "ANDROID"
    JAVASCRIPT = "JAVASCRIPT"


@dataclasses.dataclass
class ProjectDetails(autoboto.ShapeBase):
    """
    Detailed information about an AWS Mobile Hub project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "project_id",
                "projectId",
                autoboto.TypeInfo(str),
            ),
            (
                "region",
                "region",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "state",
                autoboto.TypeInfo(ProjectState),
            ),
            (
                "created_date",
                "createdDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "console_url",
                "consoleUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "resources",
                "resources",
                autoboto.TypeInfo(typing.List[Resource]),
            ),
        ]

    # Name of the project.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Unique project identifier.
    project_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Default region to use for AWS resource creation in the AWS Mobile Hub
    # project.
    region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Synchronization state for a project.
    state: "ProjectState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Date the project was created.
    created_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Date of the last modification of the project.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Website URL for this project in the AWS Mobile Hub console.
    console_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # List of AWS resources associated with a project.
    resources: typing.List["Resource"] = dataclasses.field(
        default_factory=list,
    )


class ProjectState(Enum):
    """
    Synchronization state for a project.
    """
    NORMAL = "NORMAL"
    SYNCING = "SYNCING"
    IMPORTING = "IMPORTING"


@dataclasses.dataclass
class ProjectSummary(autoboto.ShapeBase):
    """
    Summary information about an AWS Mobile Hub project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "project_id",
                "projectId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the project.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Unique project identifier.
    project_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Resource(autoboto.ShapeBase):
    """
    Information about an instance of an AWS resource associated with a project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "feature",
                "feature",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Simplified name for type of AWS resource (e.g., bucket is an Amazon S3
    # bucket).
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of
    # the bucket).
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # AWS resource name which uniquely identifies the resource in AWS systems.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Identifies which feature in AWS Mobile Hub is associated with this AWS
    # resource.
    feature: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Key-value attribute pairs.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServiceUnavailableException(autoboto.ShapeBase):
    """
    The service is temporarily unavailable. The request should be retried after some
    time delay.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "retry_after_seconds",
                "retryAfterSeconds",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Exception Error Message.
    retry_after_seconds: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Exception Error Message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyRequestsException(autoboto.ShapeBase):
    """
    Too many requests have been received for this AWS account in too short a time.
    The request should be retried after some time delay.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "retry_after_seconds",
                "retryAfterSeconds",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Exception Error Message.
    retry_after_seconds: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Exception Error Message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnauthorizedException(autoboto.ShapeBase):
    """
    Credentials of the caller are insufficient to authorize the request.
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

    # The Exception Error Message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateProjectRequest(autoboto.ShapeBase):
    """
    Request structure used for requests to update project configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                autoboto.TypeInfo(str),
            ),
            (
                "contents",
                "contents",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # Unique project identifier.
    project_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # ZIP or YAML file which contains project configuration to be updated. This
    # should be the contents of the file downloaded from the URL provided in an
    # export project operation.
    contents: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateProjectResult(autoboto.ShapeBase):
    """
    Result structure used for requests to updated project configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "details",
                "details",
                autoboto.TypeInfo(ProjectDetails),
            ),
        ]

    # Detailed information about the updated AWS Mobile Hub project.
    details: "ProjectDetails" = dataclasses.field(default_factory=dict, )
