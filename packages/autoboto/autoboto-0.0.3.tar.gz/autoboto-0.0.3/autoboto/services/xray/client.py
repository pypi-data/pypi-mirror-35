import datetime
import typing
import boto3
import autoboto
from . import shapes


class Client:
    def __init__(self, *args, **kwargs):
        self._boto_client = boto3.client("xray", *args, **kwargs)

    def batch_get_traces(
        self,
        _request: shapes.BatchGetTracesRequest = None,
        *,
        trace_ids: typing.List[str],
        next_token: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.BatchGetTracesResult:
        """
        Retrieves a list of traces specified by ID. Each trace is a collection of
        segment documents that originates from a single request. Use `GetTraceSummaries`
        to get a list of trace IDs.
        """
        if _request is None:
            _params = {}
            if trace_ids is not autoboto.ShapeBase._NOT_SET:
                _params['trace_ids'] = trace_ids
            if next_token is not autoboto.ShapeBase._NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.BatchGetTracesRequest(**_params)
        response = self._boto_client.batch_get_traces(**_request.to_boto_dict())

        return shapes.BatchGetTracesResult.from_boto_dict(response)

    def get_encryption_config(
        self,
        _request: shapes.GetEncryptionConfigRequest = None,
    ) -> shapes.GetEncryptionConfigResult:
        """
        Retrieves the current encryption configuration for X-Ray data.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetEncryptionConfigRequest(**_params)
        response = self._boto_client.get_encryption_config(
            **_request.to_boto_dict()
        )

        return shapes.GetEncryptionConfigResult.from_boto_dict(response)

    def get_service_graph(
        self,
        _request: shapes.GetServiceGraphRequest = None,
        *,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        next_token: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.GetServiceGraphResult:
        """
        Retrieves a document that describes services that process incoming requests, and
        downstream services that they call as a result. Root services process incoming
        requests and make calls to downstream services. Root services are applications
        that use the AWS X-Ray SDK. Downstream services can be other applications, AWS
        resources, HTTP web APIs, or SQL databases.
        """
        if _request is None:
            _params = {}
            if start_time is not autoboto.ShapeBase._NOT_SET:
                _params['start_time'] = start_time
            if end_time is not autoboto.ShapeBase._NOT_SET:
                _params['end_time'] = end_time
            if next_token is not autoboto.ShapeBase._NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetServiceGraphRequest(**_params)
        response = self._boto_client.get_service_graph(
            **_request.to_boto_dict()
        )

        return shapes.GetServiceGraphResult.from_boto_dict(response)

    def get_trace_graph(
        self,
        _request: shapes.GetTraceGraphRequest = None,
        *,
        trace_ids: typing.List[str],
        next_token: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.GetTraceGraphResult:
        """
        Retrieves a service graph for one or more specific trace IDs.
        """
        if _request is None:
            _params = {}
            if trace_ids is not autoboto.ShapeBase._NOT_SET:
                _params['trace_ids'] = trace_ids
            if next_token is not autoboto.ShapeBase._NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetTraceGraphRequest(**_params)
        response = self._boto_client.get_trace_graph(**_request.to_boto_dict())

        return shapes.GetTraceGraphResult.from_boto_dict(response)

    def get_trace_summaries(
        self,
        _request: shapes.GetTraceSummariesRequest = None,
        *,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        sampling: bool = autoboto.ShapeBase._NOT_SET,
        filter_expression: str = autoboto.ShapeBase._NOT_SET,
        next_token: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.GetTraceSummariesResult:
        """
        Retrieves IDs and metadata for traces available for a specified time frame using
        an optional filter. To get the full traces, pass the trace IDs to
        `BatchGetTraces`.

        A filter expression can target traced requests that hit specific service nodes
        or edges, have errors, or come from a known user. For example, the following
        filter expression targets traces that pass through `api.example.com`:

        `service("api.example.com")`

        This filter expression finds traces that have an annotation named `account` with
        the value `12345`:

        `annotation.account = "12345"`

        For a full list of indexed fields and keywords that you can use in filter
        expressions, see [Using Filter
        Expressions](http://docs.aws.amazon.com/xray/latest/devguide/xray-console-
        filters.html) in the _AWS X-Ray Developer Guide_.
        """
        if _request is None:
            _params = {}
            if start_time is not autoboto.ShapeBase._NOT_SET:
                _params['start_time'] = start_time
            if end_time is not autoboto.ShapeBase._NOT_SET:
                _params['end_time'] = end_time
            if sampling is not autoboto.ShapeBase._NOT_SET:
                _params['sampling'] = sampling
            if filter_expression is not autoboto.ShapeBase._NOT_SET:
                _params['filter_expression'] = filter_expression
            if next_token is not autoboto.ShapeBase._NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetTraceSummariesRequest(**_params)
        response = self._boto_client.get_trace_summaries(
            **_request.to_boto_dict()
        )

        return shapes.GetTraceSummariesResult.from_boto_dict(response)

    def put_encryption_config(
        self,
        _request: shapes.PutEncryptionConfigRequest = None,
        *,
        type: shapes.EncryptionType,
        key_id: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.PutEncryptionConfigResult:
        """
        Updates the encryption configuration for X-Ray data.
        """
        if _request is None:
            _params = {}
            if type is not autoboto.ShapeBase._NOT_SET:
                _params['type'] = type
            if key_id is not autoboto.ShapeBase._NOT_SET:
                _params['key_id'] = key_id
            _request = shapes.PutEncryptionConfigRequest(**_params)
        response = self._boto_client.put_encryption_config(
            **_request.to_boto_dict()
        )

        return shapes.PutEncryptionConfigResult.from_boto_dict(response)

    def put_telemetry_records(
        self,
        _request: shapes.PutTelemetryRecordsRequest = None,
        *,
        telemetry_records: typing.List[shapes.TelemetryRecord],
        ec2_instance_id: str = autoboto.ShapeBase._NOT_SET,
        hostname: str = autoboto.ShapeBase._NOT_SET,
        resource_arn: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.PutTelemetryRecordsResult:
        """
        Used by the AWS X-Ray daemon to upload telemetry.
        """
        if _request is None:
            _params = {}
            if telemetry_records is not autoboto.ShapeBase._NOT_SET:
                _params['telemetry_records'] = telemetry_records
            if ec2_instance_id is not autoboto.ShapeBase._NOT_SET:
                _params['ec2_instance_id'] = ec2_instance_id
            if hostname is not autoboto.ShapeBase._NOT_SET:
                _params['hostname'] = hostname
            if resource_arn is not autoboto.ShapeBase._NOT_SET:
                _params['resource_arn'] = resource_arn
            _request = shapes.PutTelemetryRecordsRequest(**_params)
        response = self._boto_client.put_telemetry_records(
            **_request.to_boto_dict()
        )

        return shapes.PutTelemetryRecordsResult.from_boto_dict(response)

    def put_trace_segments(
        self,
        _request: shapes.PutTraceSegmentsRequest = None,
        *,
        trace_segment_documents: typing.List[str],
    ) -> shapes.PutTraceSegmentsResult:
        """
        Uploads segment documents to AWS X-Ray. The X-Ray SDK generates segment
        documents and sends them to the X-Ray daemon, which uploads them in batches. A
        segment document can be a completed segment, an in-progress segment, or an array
        of subsegments.

        Segments must include the following fields. For the full segment document
        schema, see [AWS X-Ray Segment
        Documents](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-
        segmentdocuments.html) in the _AWS X-Ray Developer Guide_.

        **Required Segment Document Fields**

          * `name` \- The name of the service that handled the request.

          * `id` \- A 64-bit identifier for the segment, unique among segments in the same trace, in 16 hexadecimal digits.

          * `trace_id` \- A unique identifier that connects all segments and subsegments originating from a single client request.

          * `start_time` \- Time the segment or subsegment was created, in floating point seconds in epoch time, accurate to milliseconds. For example, `1480615200.010` or `1.480615200010E9`.

          * `end_time` \- Time the segment or subsegment was closed. For example, `1480615200.090` or `1.480615200090E9`. Specify either an `end_time` or `in_progress`.

          * `in_progress` \- Set to `true` instead of specifying an `end_time` to record that a segment has been started, but is not complete. Send an in progress segment when your application receives a request that will take a long time to serve, to trace the fact that the request was received. When the response is sent, send the complete segment to overwrite the in-progress segment.

        A `trace_id` consists of three numbers separated by hyphens. For example,
        1-58406520-a006649127e371903a2de979. This includes:

        **Trace ID Format**

          * The version number, i.e. `1`.

          * The time of the original request, in Unix epoch time, in 8 hexadecimal digits. For example, 10:00AM December 2nd, 2016 PST in epoch time is `1480615200` seconds, or `58406520` in hexadecimal.

          * A 96-bit identifier for the trace, globally unique, in 24 hexadecimal digits.
        """
        if _request is None:
            _params = {}
            if trace_segment_documents is not autoboto.ShapeBase._NOT_SET:
                _params['trace_segment_documents'] = trace_segment_documents
            _request = shapes.PutTraceSegmentsRequest(**_params)
        response = self._boto_client.put_trace_segments(
            **_request.to_boto_dict()
        )

        return shapes.PutTraceSegmentsResult.from_boto_dict(response)
