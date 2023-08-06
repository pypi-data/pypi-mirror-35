import datetime
import typing
import autoboto
import botocore.response
import dataclasses


@dataclasses.dataclass
class ConflictException(autoboto.ShapeBase):
    """
    The specified version does not match the version of the document.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteThingShadowRequest(autoboto.ShapeBase):
    """
    The input for the DeleteThingShadow operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the thing.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteThingShadowResponse(autoboto.ShapeBase):
    """
    The output from the DeleteThingShadow operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "payload",
                "payload",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # The state information, in JSON format.
    payload: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetThingShadowRequest(autoboto.ShapeBase):
    """
    The input for the GetThingShadow operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the thing.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetThingShadowResponse(autoboto.ShapeBase):
    """
    The output from the GetThingShadow operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "payload",
                "payload",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # The state information, in JSON format.
    payload: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class InternalFailureException(autoboto.ShapeBase):
    """
    An unexpected error has occurred.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidRequestException(autoboto.ShapeBase):
    """
    The request is not valid.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class JsonDocument(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class MethodNotAllowedException(autoboto.ShapeBase):
    """
    The specified combination of HTTP verb and URI is not supported.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class Payload(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class PublishRequest(autoboto.ShapeBase):
    """
    The input for the Publish operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "topic",
                "topic",
                autoboto.TypeInfo(str),
            ),
            (
                "qos",
                "qos",
                autoboto.TypeInfo(int),
            ),
            (
                "payload",
                "payload",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # The name of the MQTT topic.
    topic: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Quality of Service (QoS) level.
    qos: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The state information, in JSON format.
    payload: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RequestEntityTooLargeException(autoboto.ShapeBase):
    """
    The payload exceeds the maximum size allowed.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    The specified resource does not exist.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ThrottlingException(autoboto.ShapeBase):
    """
    The rate exceeds the limit.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UnauthorizedException(autoboto.ShapeBase):
    """
    You are not authorized to perform this operation.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UnsupportedDocumentEncodingException(autoboto.ShapeBase):
    """
    The document encoding is not supported.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateThingShadowRequest(autoboto.ShapeBase):
    """
    The input for the UpdateThingShadow operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "payload",
                "payload",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # The name of the thing.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The state information, in JSON format.
    payload: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateThingShadowResponse(autoboto.ShapeBase):
    """
    The output from the UpdateThingShadow operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "payload",
                "payload",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # The state information, in JSON format.
    payload: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
