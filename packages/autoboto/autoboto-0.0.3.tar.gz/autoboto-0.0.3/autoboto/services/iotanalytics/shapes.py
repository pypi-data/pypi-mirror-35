import datetime
import typing
import autoboto
from enum import Enum
import botocore.response
import dataclasses


@dataclasses.dataclass
class AddAttributesActivity(autoboto.ShapeBase):
    """
    An activity that adds other attributes based on existing attributes in the
    message.
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
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next",
                "next",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the 'addAttributes' activity.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of 1-50 "AttributeNameMapping" objects that map an existing
    # attribute to a new attribute.

    # The existing attributes remain in the message, so if you want to remove the
    # originals, use "RemoveAttributeActivity".
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BatchPutMessageErrorEntry(autoboto.ShapeBase):
    """
    Contains informations about errors.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message_id",
                "messageId",
                autoboto.TypeInfo(str),
            ),
            (
                "error_code",
                "errorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "error_message",
                "errorMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the message that caused the error. (See the value corresponding
    # to the "messageId" key in the message object.)
    message_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The code associated with the error.
    error_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message associated with the error.
    error_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class BatchPutMessageRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "channelName",
                autoboto.TypeInfo(str),
            ),
            (
                "messages",
                "messages",
                autoboto.TypeInfo(typing.List[Message]),
            ),
        ]

    # The name of the channel where the messages are sent.
    channel_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The list of messages to be sent. Each message has format: '{ "messageId":
    # "string", "payload": "string"}'.
    messages: typing.List["Message"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class BatchPutMessageResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "batch_put_message_error_entries",
                "batchPutMessageErrorEntries",
                autoboto.TypeInfo(typing.List[BatchPutMessageErrorEntry]),
            ),
        ]

    # A list of any errors encountered when sending the messages to the channel.
    batch_put_message_error_entries: typing.List["BatchPutMessageErrorEntry"
                                                ] = dataclasses.field(
                                                    default_factory=list,
                                                )


@dataclasses.dataclass
class CancelPipelineReprocessingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
            (
                "reprocessing_id",
                "reprocessingId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of pipeline for which data reprocessing is canceled.
    pipeline_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the reprocessing task (returned by "StartPipelineReprocessing").
    reprocessing_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CancelPipelineReprocessingResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Channel(autoboto.ShapeBase):
    """
    A collection of data from an MQTT topic. Channels archive the raw, unprocessed
    messages before publishing the data to a pipeline.
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
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(ChannelStatus),
            ),
            (
                "retention_period",
                "retentionPeriod",
                autoboto.TypeInfo(RetentionPeriod),
            ),
            (
                "creation_time",
                "creationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the channel.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the channel.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the channel.
    status: "ChannelStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # How long, in days, message data is kept for the channel.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    # When the channel was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When the channel was last updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ChannelActivity(autoboto.ShapeBase):
    """
    The activity that determines the source of the messages to be processed.
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
                "channel_name",
                "channelName",
                autoboto.TypeInfo(str),
            ),
            (
                "next",
                "next",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the 'channel' activity.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the channel from which the messages are processed.
    channel_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ChannelStatistics(autoboto.ShapeBase):
    """
    Statistics information about the channel.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "size",
                "size",
                autoboto.TypeInfo(EstimatedResourceSize),
            ),
        ]

    # The estimated size of the channel.
    size: "EstimatedResourceSize" = dataclasses.field(default_factory=dict, )


class ChannelStatus(Enum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


@dataclasses.dataclass
class ChannelSummary(autoboto.ShapeBase):
    """
    A summary of information about a channel.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "channelName",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(ChannelStatus),
            ),
            (
                "creation_time",
                "creationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the channel.
    channel_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the channel.
    status: "ChannelStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When the channel was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The last time the channel was updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class ComputeType(Enum):
    ACU_1 = "ACU_1"
    ACU_2 = "ACU_2"


@dataclasses.dataclass
class ContainerDatasetAction(autoboto.ShapeBase):
    """
    Information needed to run the "containerAction" to produce data set contents.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image",
                "image",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_role_arn",
                "executionRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_configuration",
                "resourceConfiguration",
                autoboto.TypeInfo(ResourceConfiguration),
            ),
            (
                "variables",
                "variables",
                autoboto.TypeInfo(typing.List[Variable]),
            ),
        ]

    # The ARN of the Docker container stored in your account. The Docker
    # container contains an application and needed support libraries and is used
    # to generate data set contents.
    image: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the role which gives permission to the system to access needed
    # resources in order to run the "containerAction". This includes, at minimum,
    # permission to retrieve the data set contents which are the input to the
    # containerized application.
    execution_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Configuration of the resource which executes the "containerAction".
    resource_configuration: "ResourceConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The values of variables used within the context of the execution of the
    # containerized application (basically, parameters passed to the
    # application). Each variable must have a name and a value given by one of
    # "stringValue", "datasetContentVersionValue", or "outputFileUriValue".
    variables: typing.List["Variable"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "channelName",
                autoboto.TypeInfo(str),
            ),
            (
                "retention_period",
                "retentionPeriod",
                autoboto.TypeInfo(RetentionPeriod),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the channel.
    channel_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # How long, in days, message data is kept for the channel.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    # Metadata which can be used to manage the channel.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "channelName",
                autoboto.TypeInfo(str),
            ),
            (
                "channel_arn",
                "channelArn",
                autoboto.TypeInfo(str),
            ),
            (
                "retention_period",
                "retentionPeriod",
                autoboto.TypeInfo(RetentionPeriod),
            ),
        ]

    # The name of the channel.
    channel_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the channel.
    channel_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # How long, in days, message data is kept for the channel.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateDatasetContentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the data set.
    dataset_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateDatasetContentResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "version_id",
                "versionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The version ID of the data set contents which are being created.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateDatasetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                autoboto.TypeInfo(str),
            ),
            (
                "actions",
                "actions",
                autoboto.TypeInfo(typing.List[DatasetAction]),
            ),
            (
                "triggers",
                "triggers",
                autoboto.TypeInfo(typing.List[DatasetTrigger]),
            ),
            (
                "retention_period",
                "retentionPeriod",
                autoboto.TypeInfo(RetentionPeriod),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the data set.
    dataset_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of actions that create the data set contents.
    actions: typing.List["DatasetAction"] = dataclasses.field(
        default_factory=list,
    )

    # A list of triggers. A trigger causes data set contents to be populated at a
    # specified time interval or when another data set's contents are created.
    # The list of triggers can be empty or contain up to five **DataSetTrigger**
    # objects.
    triggers: typing.List["DatasetTrigger"] = dataclasses.field(
        default_factory=list,
    )

    # [Optional] How long, in days, message data is kept for the data set. If not
    # given or set to null, the latest version of the dataset content plus the
    # latest succeeded version (if they are different) are retained for at most
    # 90 days.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    # Metadata which can be used to manage the data set.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateDatasetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                autoboto.TypeInfo(str),
            ),
            (
                "dataset_arn",
                "datasetArn",
                autoboto.TypeInfo(str),
            ),
            (
                "retention_period",
                "retentionPeriod",
                autoboto.TypeInfo(RetentionPeriod),
            ),
        ]

    # The name of the data set.
    dataset_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the data set.
    dataset_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # How long, in days, message data is kept for the data set.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateDatastoreRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "datastore_name",
                "datastoreName",
                autoboto.TypeInfo(str),
            ),
            (
                "retention_period",
                "retentionPeriod",
                autoboto.TypeInfo(RetentionPeriod),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the data store.
    datastore_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # How long, in days, message data is kept for the data store.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    # Metadata which can be used to manage the data store.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateDatastoreResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "datastore_name",
                "datastoreName",
                autoboto.TypeInfo(str),
            ),
            (
                "datastore_arn",
                "datastoreArn",
                autoboto.TypeInfo(str),
            ),
            (
                "retention_period",
                "retentionPeriod",
                autoboto.TypeInfo(RetentionPeriod),
            ),
        ]

    # The name of the data store.
    datastore_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the data store.
    datastore_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # How long, in days, message data is kept for the data store.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreatePipelineRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
            (
                "pipeline_activities",
                "pipelineActivities",
                autoboto.TypeInfo(typing.List[PipelineActivity]),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the pipeline.
    pipeline_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of pipeline activities.

    # The list can be 1-25 **PipelineActivity** objects. Activities perform
    # transformations on your messages, such as removing, renaming, or adding
    # message attributes; filtering messages based on attribute values; invoking
    # your Lambda functions on messages for advanced processing; or performing
    # mathematical transformations to normalize device data.
    pipeline_activities: typing.List["PipelineActivity"] = dataclasses.field(
        default_factory=list,
    )

    # Metadata which can be used to manage the pipeline.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreatePipelineResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
            (
                "pipeline_arn",
                "pipelineArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the pipeline.
    pipeline_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the pipeline.
    pipeline_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Dataset(autoboto.ShapeBase):
    """
    Information about a data set.
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
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "actions",
                "actions",
                autoboto.TypeInfo(typing.List[DatasetAction]),
            ),
            (
                "triggers",
                "triggers",
                autoboto.TypeInfo(typing.List[DatasetTrigger]),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(DatasetStatus),
            ),
            (
                "creation_time",
                "creationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "retention_period",
                "retentionPeriod",
                autoboto.TypeInfo(RetentionPeriod),
            ),
        ]

    # The name of the data set.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the data set.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The "DatasetAction" objects that automatically create the data set
    # contents.
    actions: typing.List["DatasetAction"] = dataclasses.field(
        default_factory=list,
    )

    # The "DatasetTrigger" objects that specify when the data set is
    # automatically updated.
    triggers: typing.List["DatasetTrigger"] = dataclasses.field(
        default_factory=list,
    )

    # The status of the data set.
    status: "DatasetStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When the data set was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The last time the data set was updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # [Optional] How long, in days, message data is kept for the data set.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DatasetAction(autoboto.ShapeBase):
    """
    A "DatasetAction" object specifying the query that creates the data set content.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_name",
                "actionName",
                autoboto.TypeInfo(str),
            ),
            (
                "query_action",
                "queryAction",
                autoboto.TypeInfo(SqlQueryDatasetAction),
            ),
            (
                "container_action",
                "containerAction",
                autoboto.TypeInfo(ContainerDatasetAction),
            ),
        ]

    # The name of the data set action by which data set contents are
    # automatically created.
    action_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An "SqlQueryDatasetAction" object that contains the SQL query to modify the
    # message.
    query_action: "SqlQueryDatasetAction" = dataclasses.field(
        default_factory=dict,
    )

    # Information which allows the system to run a containerized application in
    # order to create the data set contents. The application must be in a Docker
    # container along with any needed support libraries.
    container_action: "ContainerDatasetAction" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DatasetActionSummary(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_name",
                "actionName",
                autoboto.TypeInfo(str),
            ),
            (
                "action_type",
                "actionType",
                autoboto.TypeInfo(DatasetActionType),
            ),
        ]

    # The name of the action which automatically creates the data set's contents.
    action_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of action by which the data set's contents are automatically
    # created.
    action_type: "DatasetActionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class DatasetActionType(Enum):
    QUERY = "QUERY"
    CONTAINER = "CONTAINER"


class DatasetContentState(Enum):
    CREATING = "CREATING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


@dataclasses.dataclass
class DatasetContentStatus(autoboto.ShapeBase):
    """
    The state of the data set contents and the reason they are in this state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "state",
                autoboto.TypeInfo(DatasetContentState),
            ),
            (
                "reason",
                "reason",
                autoboto.TypeInfo(str),
            ),
        ]

    # The state of the data set contents. Can be one of "READY", "CREATING",
    # "SUCCEEDED" or "FAILED".
    state: "DatasetContentState" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The reason the data set contents are in this state.
    reason: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DatasetContentVersionValue(autoboto.ShapeBase):
    """
    The data set whose latest contents will be used as input to the notebook or
    application.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the data set whose latest contents will be used as input to the
    # notebook or application.
    dataset_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DatasetEntry(autoboto.ShapeBase):
    """
    The reference to a data set entry.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "entry_name",
                "entryName",
                autoboto.TypeInfo(str),
            ),
            (
                "data_uri",
                "dataURI",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the data set item.
    entry_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The pre-signed URI of the data set item.
    data_uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class DatasetStatus(Enum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


@dataclasses.dataclass
class DatasetSummary(autoboto.ShapeBase):
    """
    A summary of information about a data set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(DatasetStatus),
            ),
            (
                "creation_time",
                "creationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "triggers",
                "triggers",
                autoboto.TypeInfo(typing.List[DatasetTrigger]),
            ),
            (
                "actions",
                "actions",
                autoboto.TypeInfo(typing.List[DatasetActionSummary]),
            ),
        ]

    # The name of the data set.
    dataset_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the data set.
    status: "DatasetStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time the data set was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The last time the data set was updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of triggers. A trigger causes data set content to be populated at a
    # specified time interval or when another data set is populated. The list of
    # triggers can be empty or contain up to five DataSetTrigger objects
    triggers: typing.List["DatasetTrigger"] = dataclasses.field(
        default_factory=list,
    )

    # A list of "DataActionSummary" objects.
    actions: typing.List["DatasetActionSummary"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DatasetTrigger(autoboto.ShapeBase):
    """
    The "DatasetTrigger" that specifies when the data set is automatically updated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schedule",
                "schedule",
                autoboto.TypeInfo(Schedule),
            ),
            (
                "dataset",
                "dataset",
                autoboto.TypeInfo(TriggeringDataset),
            ),
        ]

    # The "Schedule" when the trigger is initiated.
    schedule: "Schedule" = dataclasses.field(default_factory=dict, )

    # The data set whose content creation will trigger the creation of this data
    # set's contents.
    dataset: "TriggeringDataset" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class Datastore(autoboto.ShapeBase):
    """
    Information about a data store.
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
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(DatastoreStatus),
            ),
            (
                "retention_period",
                "retentionPeriod",
                autoboto.TypeInfo(RetentionPeriod),
            ),
            (
                "creation_time",
                "creationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the data store.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the data store.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of a data store:

    # CREATING

    # The data store is being created.

    # ACTIVE

    # The data store has been created and can be used.

    # DELETING

    # The data store is being deleted.
    status: "DatastoreStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # How long, in days, message data is kept for the data store.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    # When the data store was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The last time the data store was updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DatastoreActivity(autoboto.ShapeBase):
    """
    The 'datastore' activity that specifies where to store the processed data.
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
                "datastore_name",
                "datastoreName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the 'datastore' activity.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the data store where processed messages are stored.
    datastore_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DatastoreStatistics(autoboto.ShapeBase):
    """
    Statistical information about the data store.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "size",
                "size",
                autoboto.TypeInfo(EstimatedResourceSize),
            ),
        ]

    # The estimated size of the data store.
    size: "EstimatedResourceSize" = dataclasses.field(default_factory=dict, )


class DatastoreStatus(Enum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


@dataclasses.dataclass
class DatastoreSummary(autoboto.ShapeBase):
    """
    A summary of information about a data store.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "datastore_name",
                "datastoreName",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(DatastoreStatus),
            ),
            (
                "creation_time",
                "creationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the data store.
    datastore_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the data store.
    status: "DatastoreStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When the data store was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The last time the data store was updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "channelName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the channel to delete.
    channel_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteDatasetContentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "versionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the data set whose content is deleted.
    dataset_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the data set whose content is deleted. You can also use the
    # strings "$LATEST" or "$LATEST_SUCCEEDED" to delete the latest or latest
    # successfully completed data set. If not specified, "$LATEST_SUCCEEDED" is
    # the default.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteDatasetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the data set to delete.
    dataset_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteDatastoreRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "datastore_name",
                "datastoreName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the data store to delete.
    datastore_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeletePipelineRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the pipeline to delete.
    pipeline_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeltaTime(autoboto.ShapeBase):
    """
    When you create data set contents using message data from a specified time
    frame, some message data may still be "in flight" when processing begins, and so
    will not arrive in time to be processed. Use this field to make allowances for
    the "in flight" time of your message data, so that data not processed from the
    previous time frame will be included with the next time frame. Without this,
    missed message data would be excluded from processing during the next time frame
    as well, because its timestamp places it within the previous time frame.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "offset_seconds",
                "offsetSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "time_expression",
                "timeExpression",
                autoboto.TypeInfo(str),
            ),
        ]

    # The number of seconds of estimated "in flight" lag time of message data.
    offset_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An expression by which the time of the message data may be determined. This
    # may be the name of a timestamp field, or a SQL expression which is used to
    # derive the time the message data was generated.
    time_expression: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "channelName",
                autoboto.TypeInfo(str),
            ),
            (
                "include_statistics",
                "includeStatistics",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the channel whose information is retrieved.
    channel_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If true, additional statistical information about the channel is included
    # in the response.
    include_statistics: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel",
                "channel",
                autoboto.TypeInfo(Channel),
            ),
            (
                "statistics",
                "statistics",
                autoboto.TypeInfo(ChannelStatistics),
            ),
        ]

    # An object that contains information about the channel.
    channel: "Channel" = dataclasses.field(default_factory=dict, )

    # Statistics about the channel. Included if the 'includeStatistics' parameter
    # is set to true in the request.
    statistics: "ChannelStatistics" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeDatasetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the data set whose information is retrieved.
    dataset_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeDatasetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset",
                "dataset",
                autoboto.TypeInfo(Dataset),
            ),
        ]

    # An object that contains information about the data set.
    dataset: "Dataset" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeDatastoreRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "datastore_name",
                "datastoreName",
                autoboto.TypeInfo(str),
            ),
            (
                "include_statistics",
                "includeStatistics",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the data store
    datastore_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If true, additional statistical information about the datastore is included
    # in the response.
    include_statistics: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeDatastoreResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "datastore",
                "datastore",
                autoboto.TypeInfo(Datastore),
            ),
            (
                "statistics",
                "statistics",
                autoboto.TypeInfo(DatastoreStatistics),
            ),
        ]

    # Information about the data store.
    datastore: "Datastore" = dataclasses.field(default_factory=dict, )

    # Additional statistical information about the data store. Included if the
    # 'includeStatistics' parameter is set to true in the request.
    statistics: "DatastoreStatistics" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeLoggingOptionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeLoggingOptionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logging_options",
                "loggingOptions",
                autoboto.TypeInfo(LoggingOptions),
            ),
        ]

    # The current settings of the AWS IoT Analytics logging options.
    logging_options: "LoggingOptions" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribePipelineRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the pipeline whose information is retrieved.
    pipeline_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribePipelineResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline",
                "pipeline",
                autoboto.TypeInfo(Pipeline),
            ),
        ]

    # A "Pipeline" object that contains information about the pipeline.
    pipeline: "Pipeline" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeviceRegistryEnrichActivity(autoboto.ShapeBase):
    """
    An activity that adds data from the AWS IoT device registry to your message.
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
                "attribute",
                "attribute",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "next",
                "next",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the 'deviceRegistryEnrich' activity.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the attribute that is added to the message.
    attribute: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the IoT device whose registry information is added to the
    # message.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the role that allows access to the device's registry
    # information.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeviceShadowEnrichActivity(autoboto.ShapeBase):
    """
    An activity that adds information from the AWS IoT Device Shadows service to a
    message.
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
                "attribute",
                "attribute",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "next",
                "next",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the 'deviceShadowEnrich' activity.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the attribute that is added to the message.
    attribute: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the IoT device whose shadow information is added to the
    # message.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the role that allows access to the device's shadow.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EstimatedResourceSize(autoboto.ShapeBase):
    """
    The estimated size of the resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "estimated_size_in_bytes",
                "estimatedSizeInBytes",
                autoboto.TypeInfo(float),
            ),
            (
                "estimated_on",
                "estimatedOn",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The estimated size of the resource in bytes.
    estimated_size_in_bytes: float = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time when the estimate of the size of the resource was made.
    estimated_on: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class FilterActivity(autoboto.ShapeBase):
    """
    An activity that filters a message based on its attributes.
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
                "filter",
                "filter",
                autoboto.TypeInfo(str),
            ),
            (
                "next",
                "next",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the 'filter' activity.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An expression that looks like a SQL WHERE clause that must return a Boolean
    # value.
    filter: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDatasetContentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "versionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the data set whose contents are retrieved.
    dataset_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the data set whose contents are retrieved. You can also use
    # the strings "$LATEST" or "$LATEST_SUCCEEDED" to retrieve the contents of
    # the latest or latest successfully completed data set. If not specified,
    # "$LATEST_SUCCEEDED" is the default.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDatasetContentResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "entries",
                "entries",
                autoboto.TypeInfo(typing.List[DatasetEntry]),
            ),
            (
                "timestamp",
                "timestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(DatasetContentStatus),
            ),
        ]

    # A list of "DatasetEntry" objects.
    entries: typing.List["DatasetEntry"] = dataclasses.field(
        default_factory=list,
    )

    # The time when the request was made.
    timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the data set content.
    status: "DatasetContentStatus" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class InternalFailureException(autoboto.ShapeBase):
    """
    There was an internal failure.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidRequestException(autoboto.ShapeBase):
    """
    The request was not valid.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LambdaActivity(autoboto.ShapeBase):
    """
    An activity that runs a Lambda function to modify the message.
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
                "lambda_name",
                "lambdaName",
                autoboto.TypeInfo(str),
            ),
            (
                "batch_size",
                "batchSize",
                autoboto.TypeInfo(int),
            ),
            (
                "next",
                "next",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the 'lambda' activity.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the Lambda function that is run on the message.
    lambda_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of messages passed to the Lambda function for processing.

    # The AWS Lambda function must be able to process all of these messages
    # within five minutes, which is the maximum timeout duration for Lambda
    # functions.
    batch_size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    The command caused an internal limit to be exceeded.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListChannelsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return in this request.

    # The default value is 100.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListChannelsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_summaries",
                "channelSummaries",
                autoboto.TypeInfo(typing.List[ChannelSummary]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of "ChannelSummary" objects.
    channel_summaries: typing.List["ChannelSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The token to retrieve the next set of results, or `null` if there are no
    # more results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListDatasetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return in this request.

    # The default value is 100.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListDatasetsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_summaries",
                "datasetSummaries",
                autoboto.TypeInfo(typing.List[DatasetSummary]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of "DatasetSummary" objects.
    dataset_summaries: typing.List["DatasetSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The token to retrieve the next set of results, or `null` if there are no
    # more results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListDatastoresRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return in this request.

    # The default value is 100.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListDatastoresResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "datastore_summaries",
                "datastoreSummaries",
                autoboto.TypeInfo(typing.List[DatastoreSummary]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of "DatastoreSummary" objects.
    datastore_summaries: typing.List["DatastoreSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The token to retrieve the next set of results, or `null` if there are no
    # more results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListPipelinesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return in this request.

    # The default value is 100.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListPipelinesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_summaries",
                "pipelineSummaries",
                autoboto.TypeInfo(typing.List[PipelineSummary]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of "PipelineSummary" objects.
    pipeline_summaries: typing.List["PipelineSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The token to retrieve the next set of results, or `null` if there are no
    # more results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the resource whose tags you want to list.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The tags (metadata) which you have assigned to the resource.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


class LoggingLevel(Enum):
    ERROR = "ERROR"


@dataclasses.dataclass
class LoggingOptions(autoboto.ShapeBase):
    """
    Information about logging options.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "level",
                "level",
                autoboto.TypeInfo(LoggingLevel),
            ),
            (
                "enabled",
                "enabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ARN of the role that grants permission to AWS IoT Analytics to perform
    # logging.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The logging level. Currently, only "ERROR" is supported.
    level: "LoggingLevel" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If true, logging is enabled for AWS IoT Analytics.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class MathActivity(autoboto.ShapeBase):
    """
    An activity that computes an arithmetic expression using the message's
    attributes.
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
                "attribute",
                "attribute",
                autoboto.TypeInfo(str),
            ),
            (
                "math",
                "math",
                autoboto.TypeInfo(str),
            ),
            (
                "next",
                "next",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the 'math' activity.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the attribute that will contain the result of the math
    # operation.
    attribute: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An expression that uses one or more existing attributes and must return an
    # integer value.
    math: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Message(autoboto.ShapeBase):
    """
    Information about a message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message_id",
                "messageId",
                autoboto.TypeInfo(str),
            ),
            (
                "payload",
                "payload",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # The ID you wish to assign to the message. Each "messageId" must be unique
    # within each batch sent.
    message_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The payload of the message. This may be a JSON string or a Base64-encoded
    # string representing binary data (in which case you must decode it by means
    # of a pipeline activity).
    payload: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class MessagePayload(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class OutputFileUriValue(autoboto.ShapeBase):
    """
    The URI of the location where data set contents are stored, usually the URI of a
    file in an S3 bucket.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_name",
                "fileName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The URI of the location where data set contents are stored, usually the URI
    # of a file in an S3 bucket.
    file_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Pipeline(autoboto.ShapeBase):
    """
    Contains information about a pipeline.
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
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "activities",
                "activities",
                autoboto.TypeInfo(typing.List[PipelineActivity]),
            ),
            (
                "reprocessing_summaries",
                "reprocessingSummaries",
                autoboto.TypeInfo(typing.List[ReprocessingSummary]),
            ),
            (
                "creation_time",
                "creationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the pipeline.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the pipeline.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The activities that perform transformations on the messages.
    activities: typing.List["PipelineActivity"] = dataclasses.field(
        default_factory=list,
    )

    # A summary of information about the pipeline reprocessing.
    reprocessing_summaries: typing.List["ReprocessingSummary"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )

    # When the pipeline was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The last time the pipeline was updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PipelineActivity(autoboto.ShapeBase):
    """
    An activity that performs a transformation on a message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel",
                "channel",
                autoboto.TypeInfo(ChannelActivity),
            ),
            (
                "lambda_",
                "lambda",
                autoboto.TypeInfo(LambdaActivity),
            ),
            (
                "datastore",
                "datastore",
                autoboto.TypeInfo(DatastoreActivity),
            ),
            (
                "add_attributes",
                "addAttributes",
                autoboto.TypeInfo(AddAttributesActivity),
            ),
            (
                "remove_attributes",
                "removeAttributes",
                autoboto.TypeInfo(RemoveAttributesActivity),
            ),
            (
                "select_attributes",
                "selectAttributes",
                autoboto.TypeInfo(SelectAttributesActivity),
            ),
            (
                "filter",
                "filter",
                autoboto.TypeInfo(FilterActivity),
            ),
            (
                "math",
                "math",
                autoboto.TypeInfo(MathActivity),
            ),
            (
                "device_registry_enrich",
                "deviceRegistryEnrich",
                autoboto.TypeInfo(DeviceRegistryEnrichActivity),
            ),
            (
                "device_shadow_enrich",
                "deviceShadowEnrich",
                autoboto.TypeInfo(DeviceShadowEnrichActivity),
            ),
        ]

    # Determines the source of the messages to be processed.
    channel: "ChannelActivity" = dataclasses.field(default_factory=dict, )

    # Runs a Lambda function to modify the message.
    lambda_: "LambdaActivity" = dataclasses.field(default_factory=dict, )

    # Specifies where to store the processed message data.
    datastore: "DatastoreActivity" = dataclasses.field(default_factory=dict, )

    # Adds other attributes based on existing attributes in the message.
    add_attributes: "AddAttributesActivity" = dataclasses.field(
        default_factory=dict,
    )

    # Removes attributes from a message.
    remove_attributes: "RemoveAttributesActivity" = dataclasses.field(
        default_factory=dict,
    )

    # Creates a new message using only the specified attributes from the original
    # message.
    select_attributes: "SelectAttributesActivity" = dataclasses.field(
        default_factory=dict,
    )

    # Filters a message based on its attributes.
    filter: "FilterActivity" = dataclasses.field(default_factory=dict, )

    # Computes an arithmetic expression using the message's attributes and adds
    # it to the message.
    math: "MathActivity" = dataclasses.field(default_factory=dict, )

    # Adds data from the AWS IoT device registry to your message.
    device_registry_enrich: "DeviceRegistryEnrichActivity" = dataclasses.field(
        default_factory=dict,
    )

    # Adds information from the AWS IoT Device Shadows service to a message.
    device_shadow_enrich: "DeviceShadowEnrichActivity" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PipelineSummary(autoboto.ShapeBase):
    """
    A summary of information about a pipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
            (
                "reprocessing_summaries",
                "reprocessingSummaries",
                autoboto.TypeInfo(typing.List[ReprocessingSummary]),
            ),
            (
                "creation_time",
                "creationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the pipeline.
    pipeline_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A summary of information about the pipeline reprocessing.
    reprocessing_summaries: typing.List["ReprocessingSummary"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )

    # When the pipeline was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When the pipeline was last updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PutLoggingOptionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logging_options",
                "loggingOptions",
                autoboto.TypeInfo(LoggingOptions),
            ),
        ]

    # The new values of the AWS IoT Analytics logging options.
    logging_options: "LoggingOptions" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class QueryFilter(autoboto.ShapeBase):
    """
    Information which is used to filter message data, to segregate it according to
    the time frame in which it arrives.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delta_time",
                "deltaTime",
                autoboto.TypeInfo(DeltaTime),
            ),
        ]

    # Used to limit data to that which has arrived since the last execution of
    # the action. When you create data set contents using message data from a
    # specified time frame, some message data may still be "in flight" when
    # processing begins, and so will not arrive in time to be processed. Use this
    # field to make allowances for the "in flight" time of you message data, so
    # that data not processed from a previous time frame will be included with
    # the next time frame. Without this, missed message data would be excluded
    # from processing during the next time frame as well, because its timestamp
    # places it within the previous time frame.
    delta_time: "DeltaTime" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class RemoveAttributesActivity(autoboto.ShapeBase):
    """
    An activity that removes attributes from a message.
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
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next",
                "next",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the 'removeAttributes' activity.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of 1-50 attributes to remove from the message.
    attributes: typing.List[str] = dataclasses.field(default_factory=list, )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class ReprocessingStatus(Enum):
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


@dataclasses.dataclass
class ReprocessingSummary(autoboto.ShapeBase):
    """
    Information about pipeline reprocessing.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(ReprocessingStatus),
            ),
            (
                "creation_time",
                "creationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The 'reprocessingId' returned by "StartPipelineReprocessing".
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the pipeline reprocessing.
    status: "ReprocessingStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time the pipeline reprocessing was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ResourceAlreadyExistsException(autoboto.ShapeBase):
    """
    A resource with the same name already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_arn",
                "resourceArn",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the resource.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the resource.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ResourceConfiguration(autoboto.ShapeBase):
    """
    The configuration of the resource used to execute the "containerAction".
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compute_type",
                "computeType",
                autoboto.TypeInfo(ComputeType),
            ),
            (
                "volume_size_in_gb",
                "volumeSizeInGB",
                autoboto.TypeInfo(int),
            ),
        ]

    # The type of the compute resource used to execute the "containerAction".
    # Possible values are: ACU_1 (vCPU=4, memory=16GiB) or ACU_2 (vCPU=8,
    # memory=32GiB).
    compute_type: "ComputeType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The size (in GB) of the persistent storage available to the resource
    # instance used to execute the "containerAction" (min: 1, max: 50).
    volume_size_in_gb: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    A resource with the specified name could not be found.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RetentionPeriod(autoboto.ShapeBase):
    """
    How long, in days, message data is kept.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "unlimited",
                "unlimited",
                autoboto.TypeInfo(bool),
            ),
            (
                "number_of_days",
                "numberOfDays",
                autoboto.TypeInfo(int),
            ),
        ]

    # If true, message data is kept indefinitely.
    unlimited: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of days that message data is kept. The "unlimited" parameter
    # must be false.
    number_of_days: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RunPipelineActivityRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_activity",
                "pipelineActivity",
                autoboto.TypeInfo(PipelineActivity),
            ),
            (
                "payloads",
                "payloads",
                autoboto.TypeInfo(typing.List[typing.Any]),
            ),
        ]

    # The pipeline activity that is run. This must not be a 'channel' activity or
    # a 'datastore' activity because these activities are used in a pipeline only
    # to load the original message and to store the (possibly) transformed
    # message. If a 'lambda' activity is specified, only short-running Lambda
    # functions (those with a timeout of less than 30 seconds or less) can be
    # used.
    pipeline_activity: "PipelineActivity" = dataclasses.field(
        default_factory=dict,
    )

    # The sample message payloads on which the pipeline activity is run.
    payloads: typing.List[typing.Any] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class RunPipelineActivityResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "payloads",
                "payloads",
                autoboto.TypeInfo(typing.List[typing.Any]),
            ),
            (
                "log_result",
                "logResult",
                autoboto.TypeInfo(str),
            ),
        ]

    # The enriched or transformed sample message payloads as base64-encoded
    # strings. (The results of running the pipeline activity on each input sample
    # message payload, encoded in base64.)
    payloads: typing.List[typing.Any] = dataclasses.field(
        default_factory=list,
    )

    # In case the pipeline activity fails, the log message that is generated.
    log_result: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SampleChannelDataRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "channelName",
                autoboto.TypeInfo(str),
            ),
            (
                "max_messages",
                "maxMessages",
                autoboto.TypeInfo(int),
            ),
            (
                "start_time",
                "startTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "endTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the channel whose message samples are retrieved.
    channel_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of sample messages to be retrieved. The limit is 10, the default
    # is also 10.
    max_messages: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The start of the time window from which sample messages are retrieved.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The end of the time window from which sample messages are retrieved.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SampleChannelDataResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "payloads",
                "payloads",
                autoboto.TypeInfo(typing.List[typing.Any]),
            ),
        ]

    # The list of message samples. Each sample message is returned as a
    # base64-encoded string.
    payloads: typing.List[typing.Any] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Schedule(autoboto.ShapeBase):
    """
    The schedule for when to trigger an update.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "expression",
                "expression",
                autoboto.TypeInfo(str),
            ),
        ]

    # The expression that defines when to trigger an update. For more
    # information, see [ Schedule Expressions for
    # Rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html)
    # in the Amazon CloudWatch documentation.
    expression: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SelectAttributesActivity(autoboto.ShapeBase):
    """
    Creates a new message using only the specified attributes from the original
    message.
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
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next",
                "next",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the 'selectAttributes' activity.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of the attributes to select from the message.
    attributes: typing.List[str] = dataclasses.field(default_factory=list, )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ServiceUnavailableException(autoboto.ShapeBase):
    """
    The service is temporarily unavailable.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SqlQueryDatasetAction(autoboto.ShapeBase):
    """
    The SQL query to modify the message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sql_query",
                "sqlQuery",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "filters",
                autoboto.TypeInfo(typing.List[QueryFilter]),
            ),
        ]

    # A SQL query string.
    sql_query: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Pre-filters applied to message data.
    filters: typing.List["QueryFilter"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class StartPipelineReprocessingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
            (
                "start_time",
                "startTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "endTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the pipeline on which to start reprocessing.
    pipeline_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The start time (inclusive) of raw message data that is reprocessed.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The end time (exclusive) of raw message data that is reprocessed.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class StartPipelineReprocessingResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reprocessing_id",
                "reprocessingId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the pipeline reprocessing activity that was started.
    reprocessing_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    """
    A set of key/value pairs which are used to manage the resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                autoboto.TypeInfo(str),
            ),
            (
                "value",
                "value",
                autoboto.TypeInfo(str),
            ),
        ]

    # The tag's key.
    key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The tag's value.
    value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TagResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The ARN of the resource whose tags will be modified.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new or modified tags for the resource.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class TagResourceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ThrottlingException(autoboto.ShapeBase):
    """
    The request was denied due to request throttling.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TriggeringDataset(autoboto.ShapeBase):
    """
    Information about the data set whose content generation will trigger the new
    data set content generation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the data set whose content generation will trigger the new data
    # set content generation.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UntagResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_keys",
                "tagKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN of the resource whose tags will be removed.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The keys of those tags which will be removed.
    tag_keys: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UntagResourceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "channelName",
                autoboto.TypeInfo(str),
            ),
            (
                "retention_period",
                "retentionPeriod",
                autoboto.TypeInfo(RetentionPeriod),
            ),
        ]

    # The name of the channel to be updated.
    channel_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # How long, in days, message data is kept for the channel.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateDatasetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                autoboto.TypeInfo(str),
            ),
            (
                "actions",
                "actions",
                autoboto.TypeInfo(typing.List[DatasetAction]),
            ),
            (
                "triggers",
                "triggers",
                autoboto.TypeInfo(typing.List[DatasetTrigger]),
            ),
            (
                "retention_period",
                "retentionPeriod",
                autoboto.TypeInfo(RetentionPeriod),
            ),
        ]

    # The name of the data set to update.
    dataset_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of "DatasetAction" objects.
    actions: typing.List["DatasetAction"] = dataclasses.field(
        default_factory=list,
    )

    # A list of "DatasetTrigger" objects. The list can be empty or can contain up
    # to five **DataSetTrigger** objects.
    triggers: typing.List["DatasetTrigger"] = dataclasses.field(
        default_factory=list,
    )

    # How long, in days, message data is kept for the data set.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateDatastoreRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "datastore_name",
                "datastoreName",
                autoboto.TypeInfo(str),
            ),
            (
                "retention_period",
                "retentionPeriod",
                autoboto.TypeInfo(RetentionPeriod),
            ),
        ]

    # The name of the data store to be updated.
    datastore_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # How long, in days, message data is kept for the data store.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdatePipelineRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
            (
                "pipeline_activities",
                "pipelineActivities",
                autoboto.TypeInfo(typing.List[PipelineActivity]),
            ),
        ]

    # The name of the pipeline to update.
    pipeline_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of "PipelineActivity" objects.

    # The list can be 1-25 **PipelineActivity** objects. Activities perform
    # transformations on your messages, such as removing, renaming or adding
    # message attributes; filtering messages based on attribute values; invoking
    # your Lambda functions on messages for advanced processing; or performing
    # mathematical transformations to normalize device data.
    pipeline_activities: typing.List["PipelineActivity"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Variable(autoboto.ShapeBase):
    """
    An instance of a variable to be passed to the "containerAction" execution. Each
    variable must have a name and a value given by one of "stringValue",
    "datasetContentVersionValue", or "outputFileUriValue".
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
                "string_value",
                "stringValue",
                autoboto.TypeInfo(str),
            ),
            (
                "double_value",
                "doubleValue",
                autoboto.TypeInfo(float),
            ),
            (
                "dataset_content_version_value",
                "datasetContentVersionValue",
                autoboto.TypeInfo(DatasetContentVersionValue),
            ),
            (
                "output_file_uri_value",
                "outputFileUriValue",
                autoboto.TypeInfo(OutputFileUriValue),
            ),
        ]

    # The name of the variable.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value of the variable as a string.
    string_value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value of the variable as a double (numeric).
    double_value: float = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value of the variable as a structure that specifies a data set content
    # version.
    dataset_content_version_value: "DatasetContentVersionValue" = dataclasses.field(
        default_factory=dict,
    )

    # The value of the variable as a structure that specifies an output file URI.
    output_file_uri_value: "OutputFileUriValue" = dataclasses.field(
        default_factory=dict,
    )
