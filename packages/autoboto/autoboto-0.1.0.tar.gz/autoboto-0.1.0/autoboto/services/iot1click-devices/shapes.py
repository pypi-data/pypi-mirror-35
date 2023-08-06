import datetime
import typing
import autoboto
import dataclasses


@dataclasses.dataclass
class Attributes(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClaimDevicesByClaimCodeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "claim_code",
                "ClaimCode",
                autoboto.TypeInfo(str),
            ),
        ]

    # The claim code, starting with "C-", as provided by the device manufacturer.
    claim_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ClaimDevicesByClaimCodeResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "claim_code",
                "ClaimCode",
                autoboto.TypeInfo(str),
            ),
            (
                "total",
                "Total",
                autoboto.TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The claim code provided by the device manufacturer.
    claim_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total number of devices associated with the claim code that has been
    # processed in the claim request.
    total: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDeviceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_id",
                "DeviceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDeviceResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "device_description",
                "DeviceDescription",
                autoboto.TypeInfo(DeviceDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Device details.
    device_description: "DeviceDescription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class Device(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(Attributes),
            ),
            (
                "device_id",
                "DeviceId",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user specified attributes associated with the device for an event.
    attributes: "Attributes" = dataclasses.field(default_factory=dict, )

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The device type, such as "button".
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeviceClaimResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "State",
                autoboto.TypeInfo(str),
            ),
        ]

    # The device's final claim state.
    state: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeviceDescription(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "device_id",
                "DeviceId",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "remaining_life",
                "RemainingLife",
                autoboto.TypeInfo(float),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of zero or more elements of DeviceAttribute objects providing user
    # specified device attributes.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Boolean value indicating whether or not the device is enabled.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A value between 0 and 1 inclusive, representing the fraction of life
    # remaining for the device.
    remaining_life: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of the device, such as "button".
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeviceEvent(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device",
                "Device",
                autoboto.TypeInfo(Device),
            ),
            (
                "std_event",
                "StdEvent",
                autoboto.TypeInfo(str),
            ),
        ]

    # An object representing the device associated with the event.
    device: "Device" = dataclasses.field(default_factory=dict, )

    # A serialized JSON object representing the device-type specific event.
    std_event: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeviceEventsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "events",
                "Events",
                autoboto.TypeInfo(typing.List[DeviceEvent]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of zero or more elements describing the event(s) associated with
    # the device.
    events: typing.List["DeviceEvent"] = dataclasses.field(
        default_factory=list,
    )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeviceMethod(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_type",
                "DeviceType",
                autoboto.TypeInfo(str),
            ),
            (
                "method_name",
                "MethodName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of the device, such as "button".
    device_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the method applicable to the deviceType.
    method_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Empty(autoboto.ShapeBase):
    """
    On success, an empty object is returned.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class FinalizeDeviceClaimRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_id",
                "DeviceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FinalizeDeviceClaimResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The device's final claim state.
    state: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ForbiddenException(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # 403
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The 403 error message returned by the web server.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeviceMethodsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_id",
                "DeviceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeviceMethodsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "device_methods",
                "DeviceMethods",
                autoboto.TypeInfo(typing.List[DeviceMethod]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # List of available device APIs.
    device_methods: typing.List["DeviceMethod"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class InitiateDeviceClaimRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_id",
                "DeviceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InitiateDeviceClaimResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The device's final claim state.
    state: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalFailureException(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # 500
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The 500 error message returned by the web server.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRequestException(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # 400
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The 400 error message returned by the web server.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvokeDeviceMethodRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_id",
                "DeviceId",
                autoboto.TypeInfo(str),
            ),
            (
                "device_method",
                "DeviceMethod",
                autoboto.TypeInfo(DeviceMethod),
            ),
            (
                "device_method_parameters",
                "DeviceMethodParameters",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The device method to invoke.
    device_method: "DeviceMethod" = dataclasses.field(default_factory=dict, )

    # A JSON encoded string containing the device method request parameters.
    device_method_parameters: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvokeDeviceMethodResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "device_method_response",
                "DeviceMethodResponse",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A JSON encoded string containing the device method response.
    device_method_response: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListDeviceEventsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_id",
                "DeviceId",
                autoboto.TypeInfo(str),
            ),
            (
                "from_time_stamp",
                "FromTimeStamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "to_time_stamp",
                "ToTimeStamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The start date for the device event query, in ISO8061 format. For example,
    # 2018-03-28T15:45:12.880Z
    from_time_stamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The end date for the device event query, in ISO8061 format. For example,
    # 2018-03-28T15:45:12.880Z
    to_time_stamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of results to return per request. If not set, a default
    # value of 100 is used.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDeviceEventsResponse(autoboto.OutputShapeBase):
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
                "Events",
                autoboto.TypeInfo(typing.List[DeviceEvent]),
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

    # An array of zero or more elements describing the event(s) associated with
    # the device.
    events: typing.List["DeviceEvent"] = dataclasses.field(
        default_factory=list,
    )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDevicesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_type",
                "DeviceType",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of the device, such as "button".
    device_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to return per request. If not set, a default
    # value of 100 is used.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDevicesResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "devices",
                "Devices",
                autoboto.TypeInfo(typing.List[DeviceDescription]),
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

    # A list of devices.
    devices: typing.List["DeviceDescription"] = dataclasses.field(
        default_factory=list,
    )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PreconditionFailedException(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # 412
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An error message explaining the error or its remedy.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RangeNotSatisfiableException(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # 416
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The requested number of results specified by nextToken cannot be satisfied.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceConflictException(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # 409
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An error message explaining the error or its remedy.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # 404
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The requested device could not be found.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnclaimDeviceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_id",
                "DeviceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnclaimDeviceResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The device's final claim state.
    state: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDeviceStateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_id",
                "DeviceId",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The unique identifier of the device.
    device_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If true, the device is enabled. If false, the device is disabled.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDeviceStateResponse(autoboto.OutputShapeBase):
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
