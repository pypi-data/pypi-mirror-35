import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class Alias(autoboto.ShapeBase):
    """
    An alias for an edge.
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
                "names",
                "Names",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
        ]

    # The canonical name of the alias.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of names for the alias, including the canonical name.
    names: typing.List[str] = dataclasses.field(default_factory=list, )

    # The type of the alias.
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AnnotationValue(autoboto.ShapeBase):
    """
    Value of a segment annotation. Has one of three value types: Number, Boolean or
    String.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "number_value",
                "NumberValue",
                autoboto.TypeInfo(float),
            ),
            (
                "boolean_value",
                "BooleanValue",
                autoboto.TypeInfo(bool),
            ),
            (
                "string_value",
                "StringValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # Value for a Number annotation.
    number_value: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Value for a Boolean annotation.
    boolean_value: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Value for a String annotation.
    string_value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BackendConnectionErrors(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timeout_count",
                "TimeoutCount",
                autoboto.TypeInfo(int),
            ),
            (
                "connection_refused_count",
                "ConnectionRefusedCount",
                autoboto.TypeInfo(int),
            ),
            (
                "http_code4_xx_count",
                "HTTPCode4XXCount",
                autoboto.TypeInfo(int),
            ),
            (
                "http_code5_xx_count",
                "HTTPCode5XXCount",
                autoboto.TypeInfo(int),
            ),
            (
                "unknown_host_count",
                "UnknownHostCount",
                autoboto.TypeInfo(int),
            ),
            (
                "other_count",
                "OtherCount",
                autoboto.TypeInfo(int),
            ),
        ]

    timeout_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    connection_refused_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    http_code4_xx_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    http_code5_xx_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    unknown_host_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    other_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchGetTracesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trace_ids",
                "TraceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Specify the trace IDs of requests for which to retrieve segments.
    trace_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # Pagination token. Not used.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchGetTracesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "traces",
                "Traces",
                autoboto.TypeInfo(typing.List[Trace]),
            ),
            (
                "unprocessed_trace_ids",
                "UnprocessedTraceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Full traces for the specified requests.
    traces: typing.List["Trace"] = dataclasses.field(default_factory=list, )

    # Trace IDs of requests that haven't been processed.
    unprocessed_trace_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Pagination token. Not used.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Edge(autoboto.ShapeBase):
    """
    Information about a connection between two services.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reference_id",
                "ReferenceId",
                autoboto.TypeInfo(int),
            ),
            (
                "start_time",
                "StartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "summary_statistics",
                "SummaryStatistics",
                autoboto.TypeInfo(EdgeStatistics),
            ),
            (
                "response_time_histogram",
                "ResponseTimeHistogram",
                autoboto.TypeInfo(typing.List[HistogramEntry]),
            ),
            (
                "aliases",
                "Aliases",
                autoboto.TypeInfo(typing.List[Alias]),
            ),
        ]

    # Identifier of the edge. Unique within a service map.
    reference_id: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The start time of the first segment on the edge.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The end time of the last segment on the edge.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Response statistics for segments on the edge.
    summary_statistics: "EdgeStatistics" = dataclasses.field(
        default_factory=dict,
    )

    # A histogram that maps the spread of client response times on an edge.
    response_time_histogram: typing.List["HistogramEntry"] = dataclasses.field(
        default_factory=list,
    )

    # Aliases for the edge.
    aliases: typing.List["Alias"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class EdgeStatistics(autoboto.ShapeBase):
    """
    Response statistics for an edge.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ok_count",
                "OkCount",
                autoboto.TypeInfo(int),
            ),
            (
                "error_statistics",
                "ErrorStatistics",
                autoboto.TypeInfo(ErrorStatistics),
            ),
            (
                "fault_statistics",
                "FaultStatistics",
                autoboto.TypeInfo(FaultStatistics),
            ),
            (
                "total_count",
                "TotalCount",
                autoboto.TypeInfo(int),
            ),
            (
                "total_response_time",
                "TotalResponseTime",
                autoboto.TypeInfo(float),
            ),
        ]

    # The number of requests that completed with a 2xx Success status code.
    ok_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Information about requests that failed with a 4xx Client Error status code.
    error_statistics: "ErrorStatistics" = dataclasses.field(
        default_factory=dict,
    )

    # Information about requests that failed with a 5xx Server Error status code.
    fault_statistics: "FaultStatistics" = dataclasses.field(
        default_factory=dict,
    )

    # The total number of completed requests.
    total_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The aggregate response time of completed requests.
    total_response_time: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EncryptionConfig(autoboto.ShapeBase):
    """
    A configuration document that specifies encryption configuration settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(EncryptionStatus),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(EncryptionType),
            ),
        ]

    # The ID of the customer master key (CMK) used for encryption, if applicable.
    key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The encryption status. After modifying encryption configuration with
    # PutEncryptionConfig, the status can be `UPDATING` for up to one hour before
    # X-Ray starts encrypting data with the new key.
    status: "EncryptionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of encryption. Set to `KMS` for encryption with CMKs. Set to
    # `NONE` for default encryption.
    type: "EncryptionType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class EncryptionStatus(Enum):
    UPDATING = "UPDATING"
    ACTIVE = "ACTIVE"


class EncryptionType(Enum):
    NONE = "NONE"
    KMS = "KMS"


@dataclasses.dataclass
class ErrorStatistics(autoboto.ShapeBase):
    """
    Information about requests that failed with a 4xx Client Error status code.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "throttle_count",
                "ThrottleCount",
                autoboto.TypeInfo(int),
            ),
            (
                "other_count",
                "OtherCount",
                autoboto.TypeInfo(int),
            ),
            (
                "total_count",
                "TotalCount",
                autoboto.TypeInfo(int),
            ),
        ]

    # The number of requests that failed with a 419 throttling status code.
    throttle_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of requests that failed with untracked 4xx Client Error status
    # codes.
    other_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total number of requests that failed with a 4xx Client Error status
    # code.
    total_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FaultStatistics(autoboto.ShapeBase):
    """
    Information about requests that failed with a 5xx Server Error status code.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "other_count",
                "OtherCount",
                autoboto.TypeInfo(int),
            ),
            (
                "total_count",
                "TotalCount",
                autoboto.TypeInfo(int),
            ),
        ]

    # The number of requests that failed with untracked 5xx Server Error status
    # codes.
    other_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total number of requests that failed with a 5xx Server Error status
    # code.
    total_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetEncryptionConfigRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetEncryptionConfigResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption_config",
                "EncryptionConfig",
                autoboto.TypeInfo(EncryptionConfig),
            ),
        ]

    # The encryption configuration document.
    encryption_config: "EncryptionConfig" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetServiceGraphRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start_time",
                "StartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The start of the time frame for which to generate a graph.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The end of the time frame for which to generate a graph.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Pagination token. Not used.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetServiceGraphResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start_time",
                "StartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "services",
                "Services",
                autoboto.TypeInfo(typing.List[Service]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The start of the time frame for which the graph was generated.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The end of the time frame for which the graph was generated.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The services that have processed a traced request during the specified time
    # frame.
    services: typing.List["Service"] = dataclasses.field(default_factory=list, )

    # Pagination token. Not used.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTraceGraphRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trace_ids",
                "TraceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Trace IDs of requests for which to generate a service graph.
    trace_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # Pagination token. Not used.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTraceGraphResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "services",
                "Services",
                autoboto.TypeInfo(typing.List[Service]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The services that have processed one of the specified requests.
    services: typing.List["Service"] = dataclasses.field(default_factory=list, )

    # Pagination token. Not used.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTraceSummariesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start_time",
                "StartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "sampling",
                "Sampling",
                autoboto.TypeInfo(bool),
            ),
            (
                "filter_expression",
                "FilterExpression",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The start of the time frame for which to retrieve traces.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The end of the time frame for which to retrieve traces.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Set to `true` to get summaries for only a subset of available traces.
    sampling: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specify a filter expression to retrieve trace summaries for services or
    # requests that meet certain requirements.
    filter_expression: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specify the pagination token returned by a previous request to retrieve the
    # next page of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTraceSummariesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trace_summaries",
                "TraceSummaries",
                autoboto.TypeInfo(typing.List[TraceSummary]),
            ),
            (
                "approximate_time",
                "ApproximateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "traces_processed_count",
                "TracesProcessedCount",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Trace IDs and metadata for traces that were found in the specified time
    # frame.
    trace_summaries: typing.List["TraceSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The start time of this page of results.
    approximate_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The total number of traces processed, including traces that did not match
    # the specified filter expression.
    traces_processed_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the requested time frame contained more than one page of results, you
    # can use this token to retrieve the next page. The first page contains the
    # most most recent results, closest to the end of the time frame.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HistogramEntry(autoboto.ShapeBase):
    """
    An entry in a histogram for a statistic. A histogram maps the range of observed
    values on the X axis, and the prevalence of each value on the Y axis.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                autoboto.TypeInfo(float),
            ),
            (
                "count",
                "Count",
                autoboto.TypeInfo(int),
            ),
        ]

    # The value of the entry.
    value: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The prevalence of the entry.
    count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Http(autoboto.ShapeBase):
    """
    Information about an HTTP request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "http_url",
                "HttpURL",
                autoboto.TypeInfo(str),
            ),
            (
                "http_status",
                "HttpStatus",
                autoboto.TypeInfo(int),
            ),
            (
                "http_method",
                "HttpMethod",
                autoboto.TypeInfo(str),
            ),
            (
                "user_agent",
                "UserAgent",
                autoboto.TypeInfo(str),
            ),
            (
                "client_ip",
                "ClientIp",
                autoboto.TypeInfo(str),
            ),
        ]

    # The request URL.
    http_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The response status.
    http_status: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The request method.
    http_method: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The request's user agent string.
    user_agent: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The IP address of the requestor.
    client_ip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRequestException(autoboto.ShapeBase):
    """
    The request is missing required parameters or has invalid parameters.
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
class PutEncryptionConfigRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(EncryptionType),
            ),
            (
                "key_id",
                "KeyId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of encryption. Set to `KMS` to use your own key for encryption.
    # Set to `NONE` for default encryption.
    type: "EncryptionType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An AWS KMS customer master key (CMK) in one of the following formats:

    #   * **Alias** \- The name of the key. For example, `alias/MyKey`.

    #   * **Key ID** \- The KMS key ID of the key. For example, `ae4aa6d49-a4d8-9df9-a475-4ff6d7898456`.

    #   * **ARN** \- The full Amazon Resource Name of the key ID or alias. For example, `arn:aws:kms:us-east-2:123456789012:key/ae4aa6d49-a4d8-9df9-a475-4ff6d7898456`. Use this format to specify a key in a different account.

    # Omit this key if you set `Type` to `NONE`.
    key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutEncryptionConfigResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption_config",
                "EncryptionConfig",
                autoboto.TypeInfo(EncryptionConfig),
            ),
        ]

    # The new encryption configuration.
    encryption_config: "EncryptionConfig" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutTelemetryRecordsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "telemetry_records",
                "TelemetryRecords",
                autoboto.TypeInfo(typing.List[TelemetryRecord]),
            ),
            (
                "ec2_instance_id",
                "EC2InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "hostname",
                "Hostname",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_arn",
                "ResourceARN",
                autoboto.TypeInfo(str),
            ),
        ]

    telemetry_records: typing.List["TelemetryRecord"] = dataclasses.field(
        default_factory=list,
    )

    ec2_instance_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    hostname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutTelemetryRecordsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PutTraceSegmentsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trace_segment_documents",
                "TraceSegmentDocuments",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A string containing a JSON document defining one or more segments or
    # subsegments.
    trace_segment_documents: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class PutTraceSegmentsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "unprocessed_trace_segments",
                "UnprocessedTraceSegments",
                autoboto.TypeInfo(typing.List[UnprocessedTraceSegment]),
            ),
        ]

    # Segments that failed processing.
    unprocessed_trace_segments: typing.List["UnprocessedTraceSegment"
                                           ] = dataclasses.field(
                                               default_factory=list,
                                           )


@dataclasses.dataclass
class Segment(autoboto.ShapeBase):
    """
    A segment from a trace that has been ingested by the X-Ray service. The segment
    can be compiled from documents uploaded with PutTraceSegments, or an `inferred`
    segment for a downstream service, generated from a subsegment sent by the
    service that called it.

    For the full segment document schema, see [AWS X-Ray Segment
    Documents](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-
    segmentdocuments.html) in the _AWS X-Ray Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "document",
                "Document",
                autoboto.TypeInfo(str),
            ),
        ]

    # The segment's ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The segment document.
    document: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Service(autoboto.ShapeBase):
    """
    Information about an application that processed requests, users that made
    requests, or downstream services, resources and applications that an application
    used.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reference_id",
                "ReferenceId",
                autoboto.TypeInfo(int),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "names",
                "Names",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "root",
                "Root",
                autoboto.TypeInfo(bool),
            ),
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(str),
            ),
            (
                "start_time",
                "StartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "edges",
                "Edges",
                autoboto.TypeInfo(typing.List[Edge]),
            ),
            (
                "summary_statistics",
                "SummaryStatistics",
                autoboto.TypeInfo(ServiceStatistics),
            ),
            (
                "duration_histogram",
                "DurationHistogram",
                autoboto.TypeInfo(typing.List[HistogramEntry]),
            ),
            (
                "response_time_histogram",
                "ResponseTimeHistogram",
                autoboto.TypeInfo(typing.List[HistogramEntry]),
            ),
        ]

    # Identifier for the service. Unique within the service map.
    reference_id: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The canonical name of the service.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of names for the service, including the canonical name.
    names: typing.List[str] = dataclasses.field(default_factory=list, )

    # Indicates that the service was the first service to process a request.
    root: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Identifier of the AWS account in which the service runs.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of service.

    #   * AWS Resource - The type of an AWS resource. For example, `AWS::EC2::Instance` for a application running on Amazon EC2 or `AWS::DynamoDB::Table` for an Amazon DynamoDB table that the application used.

    #   * AWS Service - The type of an AWS service. For example, `AWS::DynamoDB` for downstream calls to Amazon DynamoDB that didn't target a specific table.

    #   * `client` \- Represents the clients that sent requests to a root service.

    #   * `remote` \- A downstream service of indeterminate type.
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The service's state.
    state: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The start time of the first segment that the service generated.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The end time of the last segment that the service generated.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Connections to downstream services.
    edges: typing.List["Edge"] = dataclasses.field(default_factory=list, )

    # Aggregated statistics for the service.
    summary_statistics: "ServiceStatistics" = dataclasses.field(
        default_factory=dict,
    )

    # A histogram that maps the spread of service durations.
    duration_histogram: typing.List["HistogramEntry"] = dataclasses.field(
        default_factory=list,
    )

    # A histogram that maps the spread of service response times.
    response_time_histogram: typing.List["HistogramEntry"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ServiceId(autoboto.ShapeBase):
    """

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
                "names",
                "Names",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
        ]

    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    names: typing.List[str] = dataclasses.field(default_factory=list, )

    account_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceStatistics(autoboto.ShapeBase):
    """
    Response statistics for a service.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ok_count",
                "OkCount",
                autoboto.TypeInfo(int),
            ),
            (
                "error_statistics",
                "ErrorStatistics",
                autoboto.TypeInfo(ErrorStatistics),
            ),
            (
                "fault_statistics",
                "FaultStatistics",
                autoboto.TypeInfo(FaultStatistics),
            ),
            (
                "total_count",
                "TotalCount",
                autoboto.TypeInfo(int),
            ),
            (
                "total_response_time",
                "TotalResponseTime",
                autoboto.TypeInfo(float),
            ),
        ]

    # The number of requests that completed with a 2xx Success status code.
    ok_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Information about requests that failed with a 4xx Client Error status code.
    error_statistics: "ErrorStatistics" = dataclasses.field(
        default_factory=dict,
    )

    # Information about requests that failed with a 5xx Server Error status code.
    fault_statistics: "FaultStatistics" = dataclasses.field(
        default_factory=dict,
    )

    # The total number of completed requests.
    total_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The aggregate response time of completed requests.
    total_response_time: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TelemetryRecord(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timestamp",
                "Timestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "segments_received_count",
                "SegmentsReceivedCount",
                autoboto.TypeInfo(int),
            ),
            (
                "segments_sent_count",
                "SegmentsSentCount",
                autoboto.TypeInfo(int),
            ),
            (
                "segments_spillover_count",
                "SegmentsSpilloverCount",
                autoboto.TypeInfo(int),
            ),
            (
                "segments_rejected_count",
                "SegmentsRejectedCount",
                autoboto.TypeInfo(int),
            ),
            (
                "backend_connection_errors",
                "BackendConnectionErrors",
                autoboto.TypeInfo(BackendConnectionErrors),
            ),
        ]

    timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    segments_received_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    segments_sent_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    segments_spillover_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    segments_rejected_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    backend_connection_errors: "BackendConnectionErrors" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ThrottledException(autoboto.ShapeBase):
    """
    The request exceeds the maximum number of requests per second.
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
class Trace(autoboto.ShapeBase):
    """
    A collection of segment documents with matching trace IDs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(float),
            ),
            (
                "segments",
                "Segments",
                autoboto.TypeInfo(typing.List[Segment]),
            ),
        ]

    # The unique identifier for the request that generated the trace's segments
    # and subsegments.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The length of time in seconds between the start time of the root segment
    # and the end time of the last segment that completed.
    duration: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Segment documents for the segments and subsegments that comprise the trace.
    segments: typing.List["Segment"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class TraceSummary(autoboto.ShapeBase):
    """
    Metadata generated from the segment documents in a trace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(float),
            ),
            (
                "response_time",
                "ResponseTime",
                autoboto.TypeInfo(float),
            ),
            (
                "has_fault",
                "HasFault",
                autoboto.TypeInfo(bool),
            ),
            (
                "has_error",
                "HasError",
                autoboto.TypeInfo(bool),
            ),
            (
                "has_throttle",
                "HasThrottle",
                autoboto.TypeInfo(bool),
            ),
            (
                "is_partial",
                "IsPartial",
                autoboto.TypeInfo(bool),
            ),
            (
                "http",
                "Http",
                autoboto.TypeInfo(Http),
            ),
            (
                "annotations",
                "Annotations",
                autoboto.TypeInfo(
                    typing.Dict[str, typing.List[ValueWithServiceIds]]
                ),
            ),
            (
                "users",
                "Users",
                autoboto.TypeInfo(typing.List[TraceUser]),
            ),
            (
                "service_ids",
                "ServiceIds",
                autoboto.TypeInfo(typing.List[ServiceId]),
            ),
        ]

    # The unique identifier for the request that generated the trace's segments
    # and subsegments.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The length of time in seconds between the start time of the root segment
    # and the end time of the last segment that completed.
    duration: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The length of time in seconds between the start and end times of the root
    # segment. If the service performs work asynchronously, the response time
    # measures the time before the response is sent to the user, while the
    # duration measures the amount of time before the last traced activity
    # completes.
    response_time: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # One or more of the segment documents has a 500 series error.
    has_fault: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more of the segment documents has a 400 series error.
    has_error: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more of the segment documents has a 429 throttling error.
    has_throttle: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more of the segment documents is in progress.
    is_partial: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Information about the HTTP request served by the trace.
    http: "Http" = dataclasses.field(default_factory=dict, )

    # Annotations from the trace's segment documents.
    annotations: typing.Dict[str, typing.List["ValueWithServiceIds"]
                            ] = dataclasses.field(
                                default=autoboto.ShapeBase.NOT_SET,
                            )

    # Users from the trace's segment documents.
    users: typing.List["TraceUser"] = dataclasses.field(default_factory=list, )

    # Service IDs from the trace's segment documents.
    service_ids: typing.List["ServiceId"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class TraceUser(autoboto.ShapeBase):
    """
    Information about a user recorded in segment documents.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                autoboto.TypeInfo(str),
            ),
            (
                "service_ids",
                "ServiceIds",
                autoboto.TypeInfo(typing.List[ServiceId]),
            ),
        ]

    # The user's name.
    user_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Services that the user's request hit.
    service_ids: typing.List["ServiceId"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UnprocessedTraceSegment(autoboto.ShapeBase):
    """
    Information about a segment that failed processing.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The segment's ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The error that caused processing to fail.
    error_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The error message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ValueWithServiceIds(autoboto.ShapeBase):
    """
    Information about a segment annotation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "annotation_value",
                "AnnotationValue",
                autoboto.TypeInfo(AnnotationValue),
            ),
            (
                "service_ids",
                "ServiceIds",
                autoboto.TypeInfo(typing.List[ServiceId]),
            ),
        ]

    # Values of the annotation.
    annotation_value: "AnnotationValue" = dataclasses.field(
        default_factory=dict,
    )

    # Services to which the annotation applies.
    service_ids: typing.List["ServiceId"] = dataclasses.field(
        default_factory=list,
    )
