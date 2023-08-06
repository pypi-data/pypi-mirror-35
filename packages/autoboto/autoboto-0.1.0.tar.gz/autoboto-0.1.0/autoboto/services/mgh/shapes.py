import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AccessDeniedException(autoboto.ShapeBase):
    """
    You do not have sufficient access to perform this action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ApplicationStatus(Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"


@dataclasses.dataclass
class AssociateCreatedArtifactRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "progress_update_stream",
                "ProgressUpdateStream",
                autoboto.TypeInfo(str),
            ),
            (
                "migration_task_name",
                "MigrationTaskName",
                autoboto.TypeInfo(str),
            ),
            (
                "created_artifact",
                "CreatedArtifact",
                autoboto.TypeInfo(CreatedArtifact),
            ),
            (
                "dry_run",
                "DryRun",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the ProgressUpdateStream.
    progress_update_stream: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique identifier that references the migration task.
    migration_task_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An ARN of the AWS resource related to the migration (e.g., AMI, EC2
    # instance, RDS instance, etc.)
    created_artifact: "CreatedArtifact" = dataclasses.field(
        default_factory=dict,
    )

    # Optional boolean flag to indicate whether any effect should take place.
    # Used to test if the caller has permission to make the call.
    dry_run: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateCreatedArtifactResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociateDiscoveredResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "progress_update_stream",
                "ProgressUpdateStream",
                autoboto.TypeInfo(str),
            ),
            (
                "migration_task_name",
                "MigrationTaskName",
                autoboto.TypeInfo(str),
            ),
            (
                "discovered_resource",
                "DiscoveredResource",
                autoboto.TypeInfo(DiscoveredResource),
            ),
            (
                "dry_run",
                "DryRun",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the ProgressUpdateStream.
    progress_update_stream: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier given to the MigrationTask.
    migration_task_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Object representing a Resource.
    discovered_resource: "DiscoveredResource" = dataclasses.field(
        default_factory=dict,
    )

    # Optional boolean flag to indicate whether any effect should take place.
    # Used to test if the caller has permission to make the call.
    dry_run: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateDiscoveredResourceResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateProgressUpdateStreamRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "progress_update_stream_name",
                "ProgressUpdateStreamName",
                autoboto.TypeInfo(str),
            ),
            (
                "dry_run",
                "DryRun",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the ProgressUpdateStream.
    progress_update_stream_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional boolean flag to indicate whether any effect should take place.
    # Used to test if the caller has permission to make the call.
    dry_run: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateProgressUpdateStreamResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatedArtifact(autoboto.ShapeBase):
    """
    An ARN of the AWS cloud resource target receiving the migration (e.g., AMI, EC2
    instance, RDS instance, etc.).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # An ARN that uniquely identifies the result of a migration task.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A description that can be free-form text to record additional detail about
    # the artifact for clarity or for later reference.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProgressUpdateStreamRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "progress_update_stream_name",
                "ProgressUpdateStreamName",
                autoboto.TypeInfo(str),
            ),
            (
                "dry_run",
                "DryRun",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the ProgressUpdateStream.
    progress_update_stream_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional boolean flag to indicate whether any effect should take place.
    # Used to test if the caller has permission to make the call.
    dry_run: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProgressUpdateStreamResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeApplicationStateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The configurationId in ADS that uniquely identifies the grouped
    # application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeApplicationStateResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "application_status",
                "ApplicationStatus",
                autoboto.TypeInfo(ApplicationStatus),
            ),
            (
                "last_updated_time",
                "LastUpdatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Status of the application - Not Started, In-Progress, Complete.
    application_status: "ApplicationStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp when the application status was last updated.
    last_updated_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeMigrationTaskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "progress_update_stream",
                "ProgressUpdateStream",
                autoboto.TypeInfo(str),
            ),
            (
                "migration_task_name",
                "MigrationTaskName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the ProgressUpdateStream.
    progress_update_stream: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier given to the MigrationTask.
    migration_task_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeMigrationTaskResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "migration_task",
                "MigrationTask",
                autoboto.TypeInfo(MigrationTask),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Object encapsulating information about the migration task.
    migration_task: "MigrationTask" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DisassociateCreatedArtifactRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "progress_update_stream",
                "ProgressUpdateStream",
                autoboto.TypeInfo(str),
            ),
            (
                "migration_task_name",
                "MigrationTaskName",
                autoboto.TypeInfo(str),
            ),
            (
                "created_artifact_name",
                "CreatedArtifactName",
                autoboto.TypeInfo(str),
            ),
            (
                "dry_run",
                "DryRun",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the ProgressUpdateStream.
    progress_update_stream: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique identifier that references the migration task to be disassociated
    # with the artifact.
    migration_task_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An ARN of the AWS resource related to the migration (e.g., AMI, EC2
    # instance, RDS instance, etc.)
    created_artifact_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional boolean flag to indicate whether any effect should take place.
    # Used to test if the caller has permission to make the call.
    dry_run: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateCreatedArtifactResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateDiscoveredResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "progress_update_stream",
                "ProgressUpdateStream",
                autoboto.TypeInfo(str),
            ),
            (
                "migration_task_name",
                "MigrationTaskName",
                autoboto.TypeInfo(str),
            ),
            (
                "configuration_id",
                "ConfigurationId",
                autoboto.TypeInfo(str),
            ),
            (
                "dry_run",
                "DryRun",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the ProgressUpdateStream.
    progress_update_stream: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier given to the MigrationTask.
    migration_task_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # ConfigurationId of the ADS resource to be disassociated.
    configuration_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional boolean flag to indicate whether any effect should take place.
    # Used to test if the caller has permission to make the call.
    dry_run: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateDiscoveredResourceResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DiscoveredResource(autoboto.ShapeBase):
    """
    Object representing the on-premises resource being migrated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_id",
                "ConfigurationId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The configurationId in ADS that uniquely identifies the on-premise
    # resource.
    configuration_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A description that can be free-form text to record additional detail about
    # the discovered resource for clarity or later reference.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DryRunOperation(autoboto.ShapeBase):
    """
    Exception raised to indicate a successfully authorized action when the `DryRun`
    flag is set to "true".
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImportMigrationTaskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "progress_update_stream",
                "ProgressUpdateStream",
                autoboto.TypeInfo(str),
            ),
            (
                "migration_task_name",
                "MigrationTaskName",
                autoboto.TypeInfo(str),
            ),
            (
                "dry_run",
                "DryRun",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the ProgressUpdateStream.
    progress_update_stream: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique identifier that references the migration task.
    migration_task_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional boolean flag to indicate whether any effect should take place.
    # Used to test if the caller has permission to make the call.
    dry_run: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImportMigrationTaskResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalServerError(autoboto.ShapeBase):
    """
    Exception raised when there is an internal, configuration, or dependency error
    encountered.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidInputException(autoboto.ShapeBase):
    """
    Exception raised when the provided input violates a policy constraint or is
    entered in the wrong format or data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCreatedArtifactsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "progress_update_stream",
                "ProgressUpdateStream",
                autoboto.TypeInfo(str),
            ),
            (
                "migration_task_name",
                "MigrationTaskName",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the ProgressUpdateStream.
    progress_update_stream: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique identifier that references the migration task.
    migration_task_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If a `NextToken` was returned by a previous call, there are more results
    # available. To retrieve the next page of results, make the call again using
    # the returned token in `NextToken`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Maximum number of results to be returned per page.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCreatedArtifactsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "created_artifact_list",
                "CreatedArtifactList",
                autoboto.TypeInfo(typing.List[CreatedArtifact]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If there are more created artifacts than the max result, return the next
    # token to be passed to the next call as a bookmark of where to start from.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # List of created artifacts up to the maximum number of results specified in
    # the request.
    created_artifact_list: typing.List["CreatedArtifact"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListDiscoveredResourcesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "progress_update_stream",
                "ProgressUpdateStream",
                autoboto.TypeInfo(str),
            ),
            (
                "migration_task_name",
                "MigrationTaskName",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the ProgressUpdateStream.
    progress_update_stream: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the MigrationTask.
    migration_task_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If a `NextToken` was returned by a previous call, there are more results
    # available. To retrieve the next page of results, make the call again using
    # the returned token in `NextToken`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results returned per page.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDiscoveredResourcesResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "discovered_resource_list",
                "DiscoveredResourceList",
                autoboto.TypeInfo(typing.List[DiscoveredResource]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If there are more discovered resources than the max result, return the next
    # token to be passed to the next call as a bookmark of where to start from.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Returned list of discovered resources associated with the given
    # MigrationTask.
    discovered_resource_list: typing.List["DiscoveredResource"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )


@dataclasses.dataclass
class ListMigrationTasksRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "resource_name",
                "ResourceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # If a `NextToken` was returned by a previous call, there are more results
    # available. To retrieve the next page of results, make the call again using
    # the returned token in `NextToken`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Value to specify how many results are returned per page.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filter migration tasks by discovered resource name.
    resource_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListMigrationTasksResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "migration_task_summary_list",
                "MigrationTaskSummaryList",
                autoboto.TypeInfo(typing.List[MigrationTaskSummary]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If there are more migration tasks than the max result, return the next
    # token to be passed to the next call as a bookmark of where to start from.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Lists the migration task's summary which includes: `MigrationTaskName`,
    # `ProgressPercent`, `ProgressUpdateStream`, `Status`, and the
    # `UpdateDateTime` for each task.
    migration_task_summary_list: typing.List["MigrationTaskSummary"
                                            ] = dataclasses.field(
                                                default_factory=list,
                                            )


@dataclasses.dataclass
class ListProgressUpdateStreamsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # If a `NextToken` was returned by a previous call, there are more results
    # available. To retrieve the next page of results, make the call again using
    # the returned token in `NextToken`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filter to limit the maximum number of results to list per page.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListProgressUpdateStreamsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "progress_update_stream_summary_list",
                "ProgressUpdateStreamSummaryList",
                autoboto.TypeInfo(typing.List[ProgressUpdateStreamSummary]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # List of progress update streams up to the max number of results passed in
    # the input.
    progress_update_stream_summary_list: typing.List[
        "ProgressUpdateStreamSummary"
    ] = dataclasses.field(
        default_factory=list,
    )

    # If there are more streams created than the max result, return the next
    # token to be passed to the next call as a bookmark of where to start from.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MigrationTask(autoboto.ShapeBase):
    """
    Represents a migration task in a migration tool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "progress_update_stream",
                "ProgressUpdateStream",
                autoboto.TypeInfo(str),
            ),
            (
                "migration_task_name",
                "MigrationTaskName",
                autoboto.TypeInfo(str),
            ),
            (
                "task",
                "Task",
                autoboto.TypeInfo(Task),
            ),
            (
                "update_date_time",
                "UpdateDateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "resource_attribute_list",
                "ResourceAttributeList",
                autoboto.TypeInfo(typing.List[ResourceAttribute]),
            ),
        ]

    # A name that identifies the vendor of the migration tool being used.
    progress_update_stream: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique identifier that references the migration task.
    migration_task_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Task object encapsulating task information.
    task: "Task" = dataclasses.field(default_factory=dict, )

    # The timestamp when the task was gathered.
    update_date_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    resource_attribute_list: typing.List["ResourceAttribute"
                                        ] = dataclasses.field(
                                            default_factory=list,
                                        )


@dataclasses.dataclass
class MigrationTaskSummary(autoboto.ShapeBase):
    """
    MigrationTaskSummary includes `MigrationTaskName`, `ProgressPercent`,
    `ProgressUpdateStream`, `Status`, and `UpdateDateTime` for each task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "progress_update_stream",
                "ProgressUpdateStream",
                autoboto.TypeInfo(str),
            ),
            (
                "migration_task_name",
                "MigrationTaskName",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(Status),
            ),
            (
                "progress_percent",
                "ProgressPercent",
                autoboto.TypeInfo(int),
            ),
            (
                "status_detail",
                "StatusDetail",
                autoboto.TypeInfo(str),
            ),
            (
                "update_date_time",
                "UpdateDateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # An AWS resource used for access control. It should uniquely identify the
    # migration tool as it is used for all updates made by the tool.
    progress_update_stream: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique identifier that references the migration task.
    migration_task_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Status of the task.
    status: "Status" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    progress_percent: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Detail information of what is being done within the overall status state.
    status_detail: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The timestamp when the task was gathered.
    update_date_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NotifyApplicationStateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(ApplicationStatus),
            ),
            (
                "dry_run",
                "DryRun",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The configurationId in ADS that uniquely identifies the grouped
    # application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Status of the application - Not Started, In-Progress, Complete.
    status: "ApplicationStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional boolean flag to indicate whether any effect should take place.
    # Used to test if the caller has permission to make the call.
    dry_run: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotifyApplicationStateResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NotifyMigrationTaskStateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "progress_update_stream",
                "ProgressUpdateStream",
                autoboto.TypeInfo(str),
            ),
            (
                "migration_task_name",
                "MigrationTaskName",
                autoboto.TypeInfo(str),
            ),
            (
                "task",
                "Task",
                autoboto.TypeInfo(Task),
            ),
            (
                "update_date_time",
                "UpdateDateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "next_update_seconds",
                "NextUpdateSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "dry_run",
                "DryRun",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the ProgressUpdateStream.
    progress_update_stream: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique identifier that references the migration task.
    migration_task_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the task's progress and status.
    task: "Task" = dataclasses.field(default_factory=dict, )

    # The timestamp when the task was gathered.
    update_date_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Number of seconds after the UpdateDateTime within which the Migration Hub
    # can expect an update. If Migration Hub does not receive an update within
    # the specified interval, then the migration task will be considered stale.
    next_update_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional boolean flag to indicate whether any effect should take place.
    # Used to test if the caller has permission to make the call.
    dry_run: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotifyMigrationTaskStateResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PolicyErrorException(autoboto.ShapeBase):
    """
    Exception raised when there are problems accessing ADS (Application Discovery
    Service); most likely due to a misconfigured policy or the `migrationhub-
    discovery` role is missing or not configured correctly.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProgressUpdateStreamSummary(autoboto.ShapeBase):
    """
    Summary of the AWS resource used for access control that is implicitly linked to
    your AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "progress_update_stream_name",
                "ProgressUpdateStreamName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the ProgressUpdateStream.
    progress_update_stream_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutResourceAttributesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "progress_update_stream",
                "ProgressUpdateStream",
                autoboto.TypeInfo(str),
            ),
            (
                "migration_task_name",
                "MigrationTaskName",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_attribute_list",
                "ResourceAttributeList",
                autoboto.TypeInfo(typing.List[ResourceAttribute]),
            ),
            (
                "dry_run",
                "DryRun",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the ProgressUpdateStream.
    progress_update_stream: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique identifier that references the migration task.
    migration_task_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the resource that is being migrated. This data will be
    # used to map the task to a resource in the Application Discovery Service
    # (ADS)'s repository.

    # Takes the object array of `ResourceAttribute` where the `Type` field is
    # reserved for the following values: `IPV4_ADDRESS | IPV6_ADDRESS |
    # MAC_ADDRESS | FQDN | VM_MANAGER_ID | VM_MANAGED_OBJECT_REFERENCE | VM_NAME
    # | VM_PATH | BIOS_ID | MOTHERBOARD_SERIAL_NUMBER` where the identifying
    # value can be a string up to 256 characters.

    #   * If any "VM" related value is set for a `ResourceAttribute` object, it is required that `VM_MANAGER_ID`, as a minimum, is always set. If `VM_MANAGER_ID` is not set, then all "VM" fields will be discarded and "VM" fields will not be used for matching the migration task to a server in Application Discovery Service (ADS)'s repository. See the [Example](https://docs.aws.amazon.com/migrationhub/latest/ug/API_PutResourceAttributes.html#API_PutResourceAttributes_Examples) section below for a use case of specifying "VM" related values.

    #   * If a server you are trying to match has multiple IP or MAC addresses, you should provide as many as you know in separate type/value pairs passed to the `ResourceAttributeList` parameter to maximize the chances of matching.
    resource_attribute_list: typing.List["ResourceAttribute"
                                        ] = dataclasses.field(
                                            default_factory=list,
                                        )

    # Optional boolean flag to indicate whether any effect should take place.
    # Used to test if the caller has permission to make the call.
    dry_run: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutResourceAttributesResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceAttribute(autoboto.ShapeBase):
    """
    Attribute associated with a resource.

    Note the corresponding format required per type listed below:

    IPV4



    `x.x.x.x`

    _where x is an integer in the range [0,255]_

    IPV6



    `y : y : y : y : y : y : y : y`

    _where y is a hexadecimal between 0 and FFFF. [0, FFFF]_

    MAC_ADDRESS



    `^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$`

    FQDN



    `^[^<>{}\\\\/?,=\\p{Cntrl}]{1,256}$`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(ResourceAttributeType),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
        ]

    # Type of resource.
    type: "ResourceAttributeType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Value of the resource type.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ResourceAttributeType(Enum):
    IPV4_ADDRESS = "IPV4_ADDRESS"
    IPV6_ADDRESS = "IPV6_ADDRESS"
    MAC_ADDRESS = "MAC_ADDRESS"
    FQDN = "FQDN"
    VM_MANAGER_ID = "VM_MANAGER_ID"
    VM_MANAGED_OBJECT_REFERENCE = "VM_MANAGED_OBJECT_REFERENCE"
    VM_NAME = "VM_NAME"
    VM_PATH = "VM_PATH"
    BIOS_ID = "BIOS_ID"
    MOTHERBOARD_SERIAL_NUMBER = "MOTHERBOARD_SERIAL_NUMBER"


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    Exception raised when the request references a resource (ADS configuration,
    update stream, migration task, etc.) that does not exist in ADS (Application
    Discovery Service) or in Migration Hub's repository.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceUnavailableException(autoboto.ShapeBase):
    """
    Exception raised when there is an internal, configuration, or dependency error
    encountered.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class Status(Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"


@dataclasses.dataclass
class Task(autoboto.ShapeBase):
    """
    Task object encapsulating task information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                autoboto.TypeInfo(Status),
            ),
            (
                "status_detail",
                "StatusDetail",
                autoboto.TypeInfo(str),
            ),
            (
                "progress_percent",
                "ProgressPercent",
                autoboto.TypeInfo(int),
            ),
        ]

    # Status of the task - Not Started, In-Progress, Complete.
    status: "Status" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Details of task status as notified by a migration tool. A tool might use
    # this field to provide clarifying information about the status that is
    # unique to that tool or that explains an error state.
    status_detail: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indication of the percentage completion of the task.
    progress_percent: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UnauthorizedOperation(autoboto.ShapeBase):
    """
    Exception raised to indicate a request was not authorized when the `DryRun` flag
    is set to "true".
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
