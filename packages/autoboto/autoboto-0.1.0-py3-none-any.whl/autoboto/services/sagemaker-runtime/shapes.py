import datetime
import typing
import autoboto
import botocore.response
import dataclasses


class BodyBlob(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class InternalFailure(autoboto.ShapeBase):
    """
    An internal failure occurred.
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
class InvokeEndpointInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                autoboto.TypeInfo(str),
            ),
            (
                "body",
                "Body",
                autoboto.TypeInfo(typing.Any),
            ),
            (
                "content_type",
                "ContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "accept",
                "Accept",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_attributes",
                "CustomAttributes",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the endpoint that you specified when you created the endpoint
    # using the
    # [CreateEndpoint](http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html)
    # API.
    endpoint_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Provides input data, in the format specified in the `ContentType` request
    # header. Amazon SageMaker passes all of the data in the body to the model.

    # For information about the format of the request body, see [Common Data
    # Formats—Inference](http://docs.aws.amazon.com/sagemaker/latest/dg/cdf-
    # inference.html).
    body: typing.Any = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The MIME type of the input data in the request body.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The desired MIME type of the inference in the response.
    accept: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    custom_attributes: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvokeEndpointOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "body",
                "Body",
                autoboto.TypeInfo(typing.Any),
            ),
            (
                "content_type",
                "ContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "invoked_production_variant",
                "InvokedProductionVariant",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_attributes",
                "CustomAttributes",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Includes the inference provided by the model.

    # For information about the format of the response body, see [Common Data
    # Formats—Inference](http://docs.aws.amazon.com/sagemaker/latest/dg/cdf-
    # inference.html).
    body: typing.Any = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The MIME type of the inference returned in the response body.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Identifies the production variant that was invoked.
    invoked_production_variant: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    custom_attributes: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModelError(autoboto.ShapeBase):
    """
    Model (owned by the customer in the container) returned an error 500.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "original_status_code",
                "OriginalStatusCode",
                autoboto.TypeInfo(int),
            ),
            (
                "original_message",
                "OriginalMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "log_stream_arn",
                "LogStreamArn",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Original status code.
    original_status_code: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Original message.
    original_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the log stream.
    log_stream_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServiceUnavailable(autoboto.ShapeBase):
    """
    The service is unavailable. Try your call again.
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
class ValidationError(autoboto.ShapeBase):
    """
    Inspect your request and try again.
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
