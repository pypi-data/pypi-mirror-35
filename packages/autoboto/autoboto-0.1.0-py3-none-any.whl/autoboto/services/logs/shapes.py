import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AssociateKmsKeyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "kms_key_id",
                "kmsKeyId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
    # For more information, see [Amazon Resource Names - AWS Key Management
    # Service (AWS KMS)](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html#arn-syntax-kms).
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelExportTaskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the export task.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateExportTaskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "from_",
                "from",
                autoboto.TypeInfo(int),
            ),
            (
                "to",
                "to",
                autoboto.TypeInfo(int),
            ),
            (
                "destination",
                "destination",
                autoboto.TypeInfo(str),
            ),
            (
                "task_name",
                "taskName",
                autoboto.TypeInfo(str),
            ),
            (
                "log_stream_name_prefix",
                "logStreamNamePrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "destination_prefix",
                "destinationPrefix",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The start time of the range for the request, expressed as the number of
    # milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp
    # earlier than this time are not exported.
    from_: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The end time of the range for the request, expressed as the number of
    # milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp later
    # than this time are not exported.
    to: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of S3 bucket for the exported log data. The bucket must be in the
    # same AWS region.
    destination: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the export task.
    task_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Export only log streams that match the provided prefix. If you don't
    # specify a value, no prefix filter is applied.
    log_stream_name_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The prefix used as the start of the key for every object exported. If you
    # don't specify a value, the default is `exportedlogs`.
    destination_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateExportTaskResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "task_id",
                "taskId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the export task.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateLogGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "kms_key_id",
                "kmsKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
    # For more information, see [Amazon Resource Names - AWS Key Management
    # Service (AWS KMS)](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html#arn-syntax-kms).
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The key-value pairs to use for the tags.
    tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateLogStreamRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "log_stream_name",
                "logStreamName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the log stream.
    log_stream_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DataAlreadyAcceptedException(autoboto.ShapeBase):
    """
    The event was already logged.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "expected_sequence_token",
                "expectedSequenceToken",
                autoboto.TypeInfo(str),
            ),
        ]

    expected_sequence_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDestinationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_name",
                "destinationName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the destination.
    destination_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteLogGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteLogStreamRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "log_stream_name",
                "logStreamName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the log stream.
    log_stream_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteMetricFilterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "filter_name",
                "filterName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the metric filter.
    filter_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteResourcePolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the policy to be revoked. This parameter is required.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRetentionPolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteSubscriptionFilterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "filter_name",
                "filterName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the subscription filter.
    filter_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDestinationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_name_prefix",
                "DestinationNamePrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # The prefix to match. If you don't specify a value, no prefix filter is
    # applied.
    destination_name_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items returned. If you don't specify a value, the
    # default is up to 50 items.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDestinationsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "destinations",
                "destinations",
                autoboto.TypeInfo(typing.List[Destination]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The destinations.
    destinations: typing.List["Destination"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. The token expires after 24
    # hours.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeExportTasksRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                autoboto.TypeInfo(str),
            ),
            (
                "status_code",
                "statusCode",
                autoboto.TypeInfo(ExportTaskStatusCode),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the export task. Specifying a task ID filters the results to zero
    # or one export tasks.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status code of the export task. Specifying a status code filters the
    # results to zero or more export tasks.
    status_code: "ExportTaskStatusCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items returned. If you don't specify a value, the
    # default is up to 50 items.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeExportTasksResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "export_tasks",
                "exportTasks",
                autoboto.TypeInfo(typing.List[ExportTask]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The export tasks.
    export_tasks: typing.List["ExportTask"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. The token expires after 24
    # hours.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeLogGroupsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name_prefix",
                "logGroupNamePrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # The prefix to match.
    log_group_name_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items returned. If you don't specify a value, the
    # default is up to 50 items.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeLogGroupsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "log_groups",
                "logGroups",
                autoboto.TypeInfo(typing.List[LogGroup]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The log groups.
    log_groups: typing.List["LogGroup"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. The token expires after 24
    # hours.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeLogStreamsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "log_stream_name_prefix",
                "logStreamNamePrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "order_by",
                "orderBy",
                autoboto.TypeInfo(OrderBy),
            ),
            (
                "descending",
                "descending",
                autoboto.TypeInfo(bool),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The prefix to match.

    # If `orderBy` is `LastEventTime`,you cannot specify this parameter.
    log_stream_name_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the value is `LogStreamName`, the results are ordered by log stream
    # name. If the value is `LastEventTime`, the results are ordered by the event
    # time. The default value is `LogStreamName`.

    # If you order the results by event time, you cannot specify the
    # `logStreamNamePrefix` parameter.

    # lastEventTimestamp represents the time of the most recent log event in the
    # log stream in CloudWatch Logs. This number is expressed as the number of
    # milliseconds after Jan 1, 1970 00:00:00 UTC. lastEventTimeStamp updates on
    # an eventual consistency basis. It typically updates in less than an hour
    # from ingestion, but may take longer in some rare situations.
    order_by: "OrderBy" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the value is true, results are returned in descending order. If the
    # value is to false, results are returned in ascending order. The default
    # value is false.
    descending: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items returned. If you don't specify a value, the
    # default is up to 50 items.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeLogStreamsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "log_streams",
                "logStreams",
                autoboto.TypeInfo(typing.List[LogStream]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The log streams.
    log_streams: typing.List["LogStream"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. The token expires after 24
    # hours.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMetricFiltersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "filter_name_prefix",
                "filterNamePrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(int),
            ),
            (
                "metric_name",
                "metricName",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_namespace",
                "metricNamespace",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The prefix to match.
    filter_name_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items returned. If you don't specify a value, the
    # default is up to 50 items.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filters results to include only those with the specified metric name. If
    # you include this parameter in your request, you must also include the
    # `metricNamespace` parameter.
    metric_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filters results to include only those in the specified namespace. If you
    # include this parameter in your request, you must also include the
    # `metricName` parameter.
    metric_namespace: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeMetricFiltersResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metric_filters",
                "metricFilters",
                autoboto.TypeInfo(typing.List[MetricFilter]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The metric filters.
    metric_filters: typing.List["MetricFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. The token expires after 24
    # hours.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeResourcePoliciesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # The token for the next set of items to return. The token expires after 24
    # hours.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of resource policies to be displayed with one call of
    # this API.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeResourcePoliciesResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_policies",
                "resourcePolicies",
                autoboto.TypeInfo(typing.List[ResourcePolicy]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The resource policies that exist in this account.
    resource_policies: typing.List["ResourcePolicy"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. The token expires after 24
    # hours.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSubscriptionFiltersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "filter_name_prefix",
                "filterNamePrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The prefix to match. If you don't specify a value, no prefix filter is
    # applied.
    filter_name_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items returned. If you don't specify a value, the
    # default is up to 50 items.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSubscriptionFiltersResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "subscription_filters",
                "subscriptionFilters",
                autoboto.TypeInfo(typing.List[SubscriptionFilter]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The subscription filters.
    subscription_filters: typing.List["SubscriptionFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. The token expires after 24
    # hours.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Destination(autoboto.ShapeBase):
    """
    Represents a cross-account destination that receives subscription log events.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_name",
                "destinationName",
                autoboto.TypeInfo(str),
            ),
            (
                "target_arn",
                "targetArn",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "access_policy",
                "accessPolicy",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "creationTime",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the destination.
    destination_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the physical target to where the log
    # events are delivered (for example, a Kinesis stream).
    target_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A role for impersonation, used when delivering log events to the target.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An IAM policy document that governs which AWS accounts can create
    # subscription filters against this destination.
    access_policy: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of this destination.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The creation time of the destination, expressed as the number of
    # milliseconds after Jan 1, 1970 00:00:00 UTC.
    creation_time: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateKmsKeyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class Distribution(Enum):
    """
    The method used to distribute log data to the destination, which can be either
    random or grouped by log stream.
    """
    Random = "Random"
    ByLogStream = "ByLogStream"


@dataclasses.dataclass
class ExportTask(autoboto.ShapeBase):
    """
    Represents an export task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_name",
                "taskName",
                autoboto.TypeInfo(str),
            ),
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "from_",
                "from",
                autoboto.TypeInfo(int),
            ),
            (
                "to",
                "to",
                autoboto.TypeInfo(int),
            ),
            (
                "destination",
                "destination",
                autoboto.TypeInfo(str),
            ),
            (
                "destination_prefix",
                "destinationPrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(ExportTaskStatus),
            ),
            (
                "execution_info",
                "executionInfo",
                autoboto.TypeInfo(ExportTaskExecutionInfo),
            ),
        ]

    # The ID of the export task.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the export task.
    task_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the log group from which logs data was exported.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The start time, expressed as the number of milliseconds after Jan 1, 1970
    # 00:00:00 UTC. Events with a time stamp before this time are not exported.
    from_: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The end time, expressed as the number of milliseconds after Jan 1, 1970
    # 00:00:00 UTC. Events with a time stamp later than this time are not
    # exported.
    to: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of Amazon S3 bucket to which the log data was exported.
    destination: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The prefix that was used as the start of Amazon S3 key for every object
    # exported.
    destination_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the export task.
    status: "ExportTaskStatus" = dataclasses.field(default_factory=dict, )

    # Execution info about the export task.
    execution_info: "ExportTaskExecutionInfo" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ExportTaskExecutionInfo(autoboto.ShapeBase):
    """
    Represents the status of an export task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "creation_time",
                "creationTime",
                autoboto.TypeInfo(int),
            ),
            (
                "completion_time",
                "completionTime",
                autoboto.TypeInfo(int),
            ),
        ]

    # The creation time of the export task, expressed as the number of
    # milliseconds after Jan 1, 1970 00:00:00 UTC.
    creation_time: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The completion time of the export task, expressed as the number of
    # milliseconds after Jan 1, 1970 00:00:00 UTC.
    completion_time: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ExportTaskStatus(autoboto.ShapeBase):
    """
    Represents the status of an export task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(ExportTaskStatusCode),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The status code of the export task.
    code: "ExportTaskStatusCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status message related to the status code.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ExportTaskStatusCode(Enum):
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    PENDING_CANCEL = "PENDING_CANCEL"
    RUNNING = "RUNNING"


@dataclasses.dataclass
class FilterLogEventsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "log_stream_names",
                "logStreamNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "start_time",
                "startTime",
                autoboto.TypeInfo(int),
            ),
            (
                "end_time",
                "endTime",
                autoboto.TypeInfo(int),
            ),
            (
                "filter_pattern",
                "filterPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(int),
            ),
            (
                "interleaved",
                "interleaved",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional list of log stream names.
    log_stream_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The start of the time range, expressed as the number of milliseconds after
    # Jan 1, 1970 00:00:00 UTC. Events with a time stamp before this time are not
    # returned.
    start_time: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The end of the time range, expressed as the number of milliseconds after
    # Jan 1, 1970 00:00:00 UTC. Events with a time stamp later than this time are
    # not returned.
    end_time: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The filter pattern to use. If not provided, all the events are matched.
    filter_pattern: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The token for the next set of events to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of events to return. The default is 10,000 events.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the value is true, the operation makes a best effort to provide
    # responses that contain events from multiple log streams within the log
    # group, interleaved in a single response. If the value is false, all the
    # matched log events in the first log stream are searched first, then those
    # in the next log stream, and so on. The default is false.
    interleaved: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FilterLogEventsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "events",
                "events",
                autoboto.TypeInfo(typing.List[FilteredLogEvent]),
            ),
            (
                "searched_log_streams",
                "searchedLogStreams",
                autoboto.TypeInfo(typing.List[SearchedLogStream]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The matched events.
    events: typing.List["FilteredLogEvent"] = dataclasses.field(
        default_factory=list,
    )

    # Indicates which log streams have been searched and whether each has been
    # searched completely.
    searched_log_streams: typing.List["SearchedLogStream"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. The token expires
    # after 24 hours.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FilteredLogEvent(autoboto.ShapeBase):
    """
    Represents a matched event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_stream_name",
                "logStreamName",
                autoboto.TypeInfo(str),
            ),
            (
                "timestamp",
                "timestamp",
                autoboto.TypeInfo(int),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "ingestion_time",
                "ingestionTime",
                autoboto.TypeInfo(int),
            ),
            (
                "event_id",
                "eventId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the log stream this event belongs to.
    log_stream_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the event occurred, expressed as the number of milliseconds after
    # Jan 1, 1970 00:00:00 UTC.
    timestamp: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The data contained in the log event.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time the event was ingested, expressed as the number of milliseconds
    # after Jan 1, 1970 00:00:00 UTC.
    ingestion_time: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the event.
    event_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLogEventsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "log_stream_name",
                "logStreamName",
                autoboto.TypeInfo(str),
            ),
            (
                "start_time",
                "startTime",
                autoboto.TypeInfo(int),
            ),
            (
                "end_time",
                "endTime",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(int),
            ),
            (
                "start_from_head",
                "startFromHead",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the log stream.
    log_stream_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The start of the time range, expressed as the number of milliseconds after
    # Jan 1, 1970 00:00:00 UTC. Events with a time stamp equal to this time or
    # later than this time are included. Events with a time stamp earlier than
    # this time are not included.
    start_time: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The end of the time range, expressed as the number of milliseconds after
    # Jan 1, 1970 00:00:00 UTC. Events with a time stamp equal to or later than
    # this time are not included.
    end_time: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of log events returned. If you don't specify a value,
    # the maximum is as many log events as can fit in a response size of 1 MB, up
    # to 10,000 log events.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the value is true, the earliest log events are returned first. If the
    # value is false, the latest log events are returned first. The default value
    # is false.
    start_from_head: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetLogEventsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "events",
                "events",
                autoboto.TypeInfo(typing.List[OutputLogEvent]),
            ),
            (
                "next_forward_token",
                "nextForwardToken",
                autoboto.TypeInfo(str),
            ),
            (
                "next_backward_token",
                "nextBackwardToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The events.
    events: typing.List["OutputLogEvent"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items in the forward direction. The token
    # expires after 24 hours. If you have reached the end of the stream, it will
    # return the same token you passed in.
    next_forward_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The token for the next set of items in the backward direction. The token
    # expires after 24 hours. This token will never be null. If you have reached
    # the end of the stream, it will return the same token you passed in.
    next_backward_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InputLogEvent(autoboto.ShapeBase):
    """
    Represents a log event, which is a record of activity that was recorded by the
    application or resource being monitored.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timestamp",
                "timestamp",
                autoboto.TypeInfo(int),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The time the event occurred, expressed as the number of milliseconds after
    # Jan 1, 1970 00:00:00 UTC.
    timestamp: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The raw event message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidOperationException(autoboto.ShapeBase):
    """
    The operation is not valid on the specified resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidParameterException(autoboto.ShapeBase):
    """
    A parameter is specified incorrectly.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSequenceTokenException(autoboto.ShapeBase):
    """
    The sequence token is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "expected_sequence_token",
                "expectedSequenceToken",
                autoboto.TypeInfo(str),
            ),
        ]

    expected_sequence_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    You have reached the maximum number of resources that can be created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListTagsLogGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListTagsLogGroupResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The tags for the log group.
    tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LogGroup(autoboto.ShapeBase):
    """
    Represents a log group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "creationTime",
                autoboto.TypeInfo(int),
            ),
            (
                "retention_in_days",
                "retentionInDays",
                autoboto.TypeInfo(int),
            ),
            (
                "metric_filter_count",
                "metricFilterCount",
                autoboto.TypeInfo(int),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "stored_bytes",
                "storedBytes",
                autoboto.TypeInfo(int),
            ),
            (
                "kms_key_id",
                "kmsKeyId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The creation time of the log group, expressed as the number of milliseconds
    # after Jan 1, 1970 00:00:00 UTC.
    creation_time: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of days to retain the log events in the specified log group.
    # Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400,
    # 545, 731, 1827, and 3653.
    retention_in_days: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of metric filters.
    metric_filter_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the log group.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of bytes stored.
    stored_bytes: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LogStream(autoboto.ShapeBase):
    """
    Represents a log stream, which is a sequence of log events from a single emitter
    of logs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_stream_name",
                "logStreamName",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "creationTime",
                autoboto.TypeInfo(int),
            ),
            (
                "first_event_timestamp",
                "firstEventTimestamp",
                autoboto.TypeInfo(int),
            ),
            (
                "last_event_timestamp",
                "lastEventTimestamp",
                autoboto.TypeInfo(int),
            ),
            (
                "last_ingestion_time",
                "lastIngestionTime",
                autoboto.TypeInfo(int),
            ),
            (
                "upload_sequence_token",
                "uploadSequenceToken",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "stored_bytes",
                "storedBytes",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the log stream.
    log_stream_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The creation time of the stream, expressed as the number of milliseconds
    # after Jan 1, 1970 00:00:00 UTC.
    creation_time: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time of the first event, expressed as the number of milliseconds after
    # Jan 1, 1970 00:00:00 UTC.
    first_event_timestamp: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # the time of the most recent log event in the log stream in CloudWatch Logs.
    # This number is expressed as the number of milliseconds after Jan 1, 1970
    # 00:00:00 UTC. lastEventTime updates on an eventual consistency basis. It
    # typically updates in less than an hour from ingestion, but may take longer
    # in some rare situations.
    last_event_timestamp: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ingestion time, expressed as the number of milliseconds after Jan 1,
    # 1970 00:00:00 UTC.
    last_ingestion_time: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The sequence token.
    upload_sequence_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the log stream.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of bytes stored.
    stored_bytes: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricFilter(autoboto.ShapeBase):
    """
    Metric filters express how CloudWatch Logs would extract metric observations
    from ingested log events and transform them into metric data in a CloudWatch
    metric.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter_name",
                "filterName",
                autoboto.TypeInfo(str),
            ),
            (
                "filter_pattern",
                "filterPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_transformations",
                "metricTransformations",
                autoboto.TypeInfo(typing.List[MetricTransformation]),
            ),
            (
                "creation_time",
                "creationTime",
                autoboto.TypeInfo(int),
            ),
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the metric filter.
    filter_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A symbolic description of how CloudWatch Logs should interpret the data in
    # each log event. For example, a log event may contain time stamps, IP
    # addresses, strings, and so on. You use the filter pattern to specify what
    # to look for in the log event message.
    filter_pattern: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The metric transformations.
    metric_transformations: typing.List["MetricTransformation"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )

    # The creation time of the metric filter, expressed as the number of
    # milliseconds after Jan 1, 1970 00:00:00 UTC.
    creation_time: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MetricFilterMatchRecord(autoboto.ShapeBase):
    """
    Represents a matched event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_number",
                "eventNumber",
                autoboto.TypeInfo(int),
            ),
            (
                "event_message",
                "eventMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "extracted_values",
                "extractedValues",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The event number.
    event_number: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The raw event data.
    event_message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The values extracted from the event data by the filter.
    extracted_values: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MetricTransformation(autoboto.ShapeBase):
    """
    Indicates how to transform ingested log events in to metric data in a CloudWatch
    metric.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metric_name",
                "metricName",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_namespace",
                "metricNamespace",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_value",
                "metricValue",
                autoboto.TypeInfo(str),
            ),
            (
                "default_value",
                "defaultValue",
                autoboto.TypeInfo(float),
            ),
        ]

    # The name of the CloudWatch metric.
    metric_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The namespace of the CloudWatch metric.
    metric_namespace: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The value to publish to the CloudWatch metric when a filter pattern matches
    # a log event.
    metric_value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Optional) The value to emit when a filter pattern does not match a log
    # event. This value can be null.
    default_value: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OperationAbortedException(autoboto.ShapeBase):
    """
    Multiple requests to update the same resource were in conflict.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class OrderBy(Enum):
    LogStreamName = "LogStreamName"
    LastEventTime = "LastEventTime"


@dataclasses.dataclass
class OutputLogEvent(autoboto.ShapeBase):
    """
    Represents a log event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timestamp",
                "timestamp",
                autoboto.TypeInfo(int),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "ingestion_time",
                "ingestionTime",
                autoboto.TypeInfo(int),
            ),
        ]

    # The time the event occurred, expressed as the number of milliseconds after
    # Jan 1, 1970 00:00:00 UTC.
    timestamp: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The data contained in the log event.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time the event was ingested, expressed as the number of milliseconds
    # after Jan 1, 1970 00:00:00 UTC.
    ingestion_time: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutDestinationPolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_name",
                "destinationName",
                autoboto.TypeInfo(str),
            ),
            (
                "access_policy",
                "accessPolicy",
                autoboto.TypeInfo(str),
            ),
        ]

    # A name for an existing destination.
    destination_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An IAM policy document that authorizes cross-account users to deliver their
    # log events to the associated destination.
    access_policy: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutDestinationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_name",
                "destinationName",
                autoboto.TypeInfo(str),
            ),
            (
                "target_arn",
                "targetArn",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # A name for the destination.
    destination_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of an Amazon Kinesis stream to which to deliver matching log
    # events.
    target_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of an IAM role that grants CloudWatch Logs permissions to call the
    # Amazon Kinesis PutRecord operation on the destination stream.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutDestinationResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "destination",
                "destination",
                autoboto.TypeInfo(Destination),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The destination.
    destination: "Destination" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PutLogEventsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "log_stream_name",
                "logStreamName",
                autoboto.TypeInfo(str),
            ),
            (
                "log_events",
                "logEvents",
                autoboto.TypeInfo(typing.List[InputLogEvent]),
            ),
            (
                "sequence_token",
                "sequenceToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the log stream.
    log_stream_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The log events.
    log_events: typing.List["InputLogEvent"] = dataclasses.field(
        default_factory=list,
    )

    # The sequence token obtained from the response of the previous
    # `PutLogEvents` call. An upload in a newly created log stream does not
    # require a sequence token. You can also get the sequence token using
    # DescribeLogStreams. If you call `PutLogEvents` twice within a narrow time
    # period using the same value for `sequenceToken`, both calls may be
    # successful, or one may be rejected.
    sequence_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutLogEventsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_sequence_token",
                "nextSequenceToken",
                autoboto.TypeInfo(str),
            ),
            (
                "rejected_log_events_info",
                "rejectedLogEventsInfo",
                autoboto.TypeInfo(RejectedLogEventsInfo),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The next sequence token.
    next_sequence_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The rejected events.
    rejected_log_events_info: "RejectedLogEventsInfo" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutMetricFilterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "filter_name",
                "filterName",
                autoboto.TypeInfo(str),
            ),
            (
                "filter_pattern",
                "filterPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_transformations",
                "metricTransformations",
                autoboto.TypeInfo(typing.List[MetricTransformation]),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A name for the metric filter.
    filter_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A filter pattern for extracting metric data out of ingested log events.
    filter_pattern: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A collection of information that defines how metric data gets emitted.
    metric_transformations: typing.List["MetricTransformation"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )


@dataclasses.dataclass
class PutResourcePolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_document",
                "policyDocument",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the new policy. This parameter is required.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Details of the new policy, including the identity of the principal that is
    # enabled to put logs to this account. This is formatted as a JSON string.

    # The following example creates a resource policy enabling the Route 53
    # service to put DNS query logs in to the specified log group. Replace
    # "logArn" with the ARN of your CloudWatch Logs resource, such as a log group
    # or log stream.

    # `{ "Version": "2012-10-17", "Statement": [ { "Sid":
    # "Route53LogsToCloudWatchLogs", "Effect": "Allow", "Principal": { "Service":
    # [ "route53.amazonaws.com" ] }, "Action":"logs:PutLogEvents", "Resource":
    # "logArn" } ] } `
    policy_document: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutResourcePolicyResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_policy",
                "resourcePolicy",
                autoboto.TypeInfo(ResourcePolicy),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The new policy.
    resource_policy: "ResourcePolicy" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutRetentionPolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "retention_in_days",
                "retentionInDays",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of days to retain the log events in the specified log group.
    # Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400,
    # 545, 731, 1827, and 3653.
    retention_in_days: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutSubscriptionFilterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "filter_name",
                "filterName",
                autoboto.TypeInfo(str),
            ),
            (
                "filter_pattern",
                "filterPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "destination_arn",
                "destinationArn",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "distribution",
                "distribution",
                autoboto.TypeInfo(Distribution),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A name for the subscription filter. If you are updating an existing filter,
    # you must specify the correct name in `filterName`. Otherwise, the call
    # fails because you cannot associate a second filter with a log group. To
    # find the name of the filter currently associated with a log group, use
    # DescribeSubscriptionFilters.
    filter_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A filter pattern for subscribing to a filtered stream of log events.
    filter_pattern: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the destination to deliver matching log events to. Currently,
    # the supported destinations are:

    #   * An Amazon Kinesis stream belonging to the same account as the subscription filter, for same-account delivery.

    #   * A logical destination (specified using an ARN) belonging to a different account, for cross-account delivery.

    #   * An Amazon Kinesis Firehose delivery stream belonging to the same account as the subscription filter, for same-account delivery.

    #   * An AWS Lambda function belonging to the same account as the subscription filter, for same-account delivery.
    destination_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of an IAM role that grants CloudWatch Logs permissions to deliver
    # ingested log events to the destination stream. You don't need to provide
    # the ARN when you are working with a logical destination for cross-account
    # delivery.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The method used to distribute log data to the destination. By default log
    # data is grouped by log stream, but the grouping can be set to random for a
    # more even distribution. This property is only applicable when the
    # destination is an Amazon Kinesis stream.
    distribution: "Distribution" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RejectedLogEventsInfo(autoboto.ShapeBase):
    """
    Represents the rejected events.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "too_new_log_event_start_index",
                "tooNewLogEventStartIndex",
                autoboto.TypeInfo(int),
            ),
            (
                "too_old_log_event_end_index",
                "tooOldLogEventEndIndex",
                autoboto.TypeInfo(int),
            ),
            (
                "expired_log_event_end_index",
                "expiredLogEventEndIndex",
                autoboto.TypeInfo(int),
            ),
        ]

    # The log events that are too new.
    too_new_log_event_start_index: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The log events that are too old.
    too_old_log_event_end_index: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The expired log events.
    expired_log_event_end_index: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceAlreadyExistsException(autoboto.ShapeBase):
    """
    The specified resource already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    The specified resource does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResourcePolicy(autoboto.ShapeBase):
    """
    A policy enabling one or more entities to put logs to a log group in this
    account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_document",
                "policyDocument",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_time",
                "lastUpdatedTime",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the resource policy.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The details of the policy.
    policy_document: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Time stamp showing when this policy was last updated, expressed as the
    # number of milliseconds after Jan 1, 1970 00:00:00 UTC.
    last_updated_time: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SearchedLogStream(autoboto.ShapeBase):
    """
    Represents the search status of a log stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_stream_name",
                "logStreamName",
                autoboto.TypeInfo(str),
            ),
            (
                "searched_completely",
                "searchedCompletely",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the log stream.
    log_stream_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether all the events in this log stream were searched.
    searched_completely: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServiceUnavailableException(autoboto.ShapeBase):
    """
    The service cannot complete the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubscriptionFilter(autoboto.ShapeBase):
    """
    Represents a subscription filter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter_name",
                "filterName",
                autoboto.TypeInfo(str),
            ),
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "filter_pattern",
                "filterPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "destination_arn",
                "destinationArn",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "distribution",
                "distribution",
                autoboto.TypeInfo(Distribution),
            ),
            (
                "creation_time",
                "creationTime",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the subscription filter.
    filter_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A symbolic description of how CloudWatch Logs should interpret the data in
    # each log event. For example, a log event may contain time stamps, IP
    # addresses, strings, and so on. You use the filter pattern to specify what
    # to look for in the log event message.
    filter_pattern: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the destination.
    destination_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The method used to distribute log data to the destination, which can be
    # either random or grouped by log stream.
    distribution: "Distribution" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The creation time of the subscription filter, expressed as the number of
    # milliseconds after Jan 1, 1970 00:00:00 UTC.
    creation_time: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagLogGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The key-value pairs to use for the tags.
    tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TestMetricFilterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter_pattern",
                "filterPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "log_event_messages",
                "logEventMessages",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A symbolic description of how CloudWatch Logs should interpret the data in
    # each log event. For example, a log event may contain time stamps, IP
    # addresses, strings, and so on. You use the filter pattern to specify what
    # to look for in the log event message.
    filter_pattern: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The log event messages to test.
    log_event_messages: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class TestMetricFilterResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "matches",
                "matches",
                autoboto.TypeInfo(typing.List[MetricFilterMatchRecord]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The matched events.
    matches: typing.List["MetricFilterMatchRecord"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UnrecognizedClientException(autoboto.ShapeBase):
    """
    The most likely cause is an invalid AWS access key ID or secret key.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UntagLogGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The tag keys. The corresponding tags are removed from the log group.
    tags: typing.List[str] = dataclasses.field(default_factory=list, )
