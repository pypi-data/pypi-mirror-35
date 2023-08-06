import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AddressBook(autoboto.ShapeBase):
    """
    An address book with attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address_book_arn",
                "AddressBookArn",
                autoboto.TypeInfo(str),
            ),
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

    # The ARN of the address book.
    address_book_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the address book.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the address book.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddressBookData(autoboto.ShapeBase):
    """
    Information related to an address book.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address_book_arn",
                "AddressBookArn",
                autoboto.TypeInfo(str),
            ),
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

    # The ARN of the address book.
    address_book_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the address book.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the address book.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AlreadyExistsException(autoboto.ShapeBase):
    """
    The resource being created already exists. HTTP Status Code: 400
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
class AssociateContactWithAddressBookRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "contact_arn",
                "ContactArn",
                autoboto.TypeInfo(str),
            ),
            (
                "address_book_arn",
                "AddressBookArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the contact to associate with an address book.
    contact_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the address book with which to associate the contact.
    address_book_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociateContactWithAddressBookResponse(autoboto.OutputShapeBase):
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
class AssociateDeviceWithRoomRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_arn",
                "DeviceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "room_arn",
                "RoomArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the device to associate to a room. Required.
    device_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the room with which to associate the device. Required.
    room_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateDeviceWithRoomResponse(autoboto.OutputShapeBase):
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
class AssociateSkillGroupWithRoomRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_arn",
                "SkillGroupArn",
                autoboto.TypeInfo(str),
            ),
            (
                "room_arn",
                "RoomArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the skill group to associate with a room. Required.
    skill_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the room with which to associate the skill group. Required.
    room_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateSkillGroupWithRoomResponse(autoboto.OutputShapeBase):
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


class ConnectionStatus(Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"


@dataclasses.dataclass
class Contact(autoboto.ShapeBase):
    """
    A contact with attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "contact_arn",
                "ContactArn",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "first_name",
                "FirstName",
                autoboto.TypeInfo(str),
            ),
            (
                "last_name",
                "LastName",
                autoboto.TypeInfo(str),
            ),
            (
                "phone_number",
                "PhoneNumber",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the contact.
    contact_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the contact to display on the console.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The first name of the contact, used to call the contact on the device.
    first_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The last name of the contact, used to call the contact on the device.
    last_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The phone number of the contact.
    phone_number: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ContactData(autoboto.ShapeBase):
    """
    Information related to a contact.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "contact_arn",
                "ContactArn",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "first_name",
                "FirstName",
                autoboto.TypeInfo(str),
            ),
            (
                "last_name",
                "LastName",
                autoboto.TypeInfo(str),
            ),
            (
                "phone_number",
                "PhoneNumber",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the contact.
    contact_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the contact to display on the console.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The first name of the contact, used to call the contact on the device.
    first_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The last name of the contact, used to call the contact on the device.
    last_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The phone number of the contact.
    phone_number: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAddressBookRequest(autoboto.ShapeBase):
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
            (
                "client_request_token",
                "ClientRequestToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the address book.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the address book.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A unique, user-specified identifier for the request that ensures
    # idempotency.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateAddressBookResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "address_book_arn",
                "AddressBookArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the newly created address book.
    address_book_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateContactRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "first_name",
                "FirstName",
                autoboto.TypeInfo(str),
            ),
            (
                "phone_number",
                "PhoneNumber",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "last_name",
                "LastName",
                autoboto.TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The first name of the contact that is used to call the contact on the
    # device.
    first_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The phone number of the contact in E.164 format.
    phone_number: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the contact to display on the console.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The last name of the contact that is used to call the contact on the
    # device.
    last_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A unique, user-specified identifier for this request that ensures
    # idempotency.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateContactResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "contact_arn",
                "ContactArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the newly created address book.
    contact_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "profile_name",
                "ProfileName",
                autoboto.TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                autoboto.TypeInfo(str),
            ),
            (
                "address",
                "Address",
                autoboto.TypeInfo(str),
            ),
            (
                "distance_unit",
                "DistanceUnit",
                autoboto.TypeInfo(DistanceUnit),
            ),
            (
                "temperature_unit",
                "TemperatureUnit",
                autoboto.TypeInfo(TemperatureUnit),
            ),
            (
                "wake_word",
                "WakeWord",
                autoboto.TypeInfo(WakeWord),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                autoboto.TypeInfo(str),
            ),
            (
                "setup_mode_disabled",
                "SetupModeDisabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "max_volume_limit",
                "MaxVolumeLimit",
                autoboto.TypeInfo(int),
            ),
            (
                "pstn_enabled",
                "PSTNEnabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of a room profile.
    profile_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time zone used by a room profile.
    timezone: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The valid address for the room.
    address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The distance unit to be used by devices in the profile.
    distance_unit: "DistanceUnit" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The temperature unit to be used by devices in the profile.
    temperature_unit: "TemperatureUnit" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A wake word for Alexa, Echo, Amazon, or a computer.
    wake_word: "WakeWord" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The user-specified token that is used during the creation of a profile.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether room profile setup is enabled.
    setup_mode_disabled: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum volume limit for a room profile.
    max_volume_limit: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether PSTN calling is enabled.
    pstn_enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateProfileResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "profile_arn",
                "ProfileArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the newly created room profile in the response.
    profile_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateRoomRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "room_name",
                "RoomName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "profile_arn",
                "ProfileArn",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_calendar_id",
                "ProviderCalendarId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name for the room.
    room_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description for the room.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The profile ARN for the room.
    profile_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The calendar ARN for the room.
    provider_calendar_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A unique, user-specified identifier for this request that ensures
    # idempotency.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The tags for the room.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateRoomResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "room_arn",
                "RoomArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the newly created room in the response.
    room_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSkillGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_name",
                "SkillGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name for the skill group.
    skill_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description for the skill group.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A unique, user-specified identifier for this request that ensures
    # idempotency.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateSkillGroupResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "skill_group_arn",
                "SkillGroupArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the newly created skill group in the response.
    skill_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateUserRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_id",
                "UserId",
                autoboto.TypeInfo(str),
            ),
            (
                "first_name",
                "FirstName",
                autoboto.TypeInfo(str),
            ),
            (
                "last_name",
                "LastName",
                autoboto.TypeInfo(str),
            ),
            (
                "email",
                "Email",
                autoboto.TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The ARN for the user.
    user_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The first name for the user.
    first_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The last name for the user.
    last_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The email address for the user.
    email: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A unique, user-specified identifier for this request that ensures
    # idempotency.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The tags for the user.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateUserResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_arn",
                "UserArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the newly created user in the response.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAddressBookRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address_book_arn",
                "AddressBookArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the address book to delete.
    address_book_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteAddressBookResponse(autoboto.OutputShapeBase):
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
class DeleteContactRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "contact_arn",
                "ContactArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the contact to delete.
    contact_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteContactResponse(autoboto.OutputShapeBase):
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
class DeleteProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "profile_arn",
                "ProfileArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the room profile to delete. Required.
    profile_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProfileResponse(autoboto.OutputShapeBase):
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
class DeleteRoomRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "room_arn",
                "RoomArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the room to delete. Required.
    room_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRoomResponse(autoboto.OutputShapeBase):
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
class DeleteRoomSkillParameterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_id",
                "SkillId",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_key",
                "ParameterKey",
                autoboto.TypeInfo(str),
            ),
            (
                "room_arn",
                "RoomArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the skill from which to remove the room skill parameter details.
    skill_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The room skill parameter key for which to remove details.
    parameter_key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the room from which to remove the room skill parameter details.
    room_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRoomSkillParameterResponse(autoboto.OutputShapeBase):
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
class DeleteSkillGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_arn",
                "SkillGroupArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the skill group to delete. Required.
    skill_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteSkillGroupResponse(autoboto.OutputShapeBase):
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
class DeleteUserRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enrollment_id",
                "EnrollmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_arn",
                "UserArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the user's enrollment in the organization. Required.
    enrollment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the user to delete in the organization. Required.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUserResponse(autoboto.OutputShapeBase):
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
class Device(autoboto.ShapeBase):
    """
    A device with attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_arn",
                "DeviceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "device_serial_number",
                "DeviceSerialNumber",
                autoboto.TypeInfo(str),
            ),
            (
                "device_type",
                "DeviceType",
                autoboto.TypeInfo(str),
            ),
            (
                "device_name",
                "DeviceName",
                autoboto.TypeInfo(str),
            ),
            (
                "software_version",
                "SoftwareVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "mac_address",
                "MacAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "room_arn",
                "RoomArn",
                autoboto.TypeInfo(str),
            ),
            (
                "device_status",
                "DeviceStatus",
                autoboto.TypeInfo(DeviceStatus),
            ),
            (
                "device_status_info",
                "DeviceStatusInfo",
                autoboto.TypeInfo(DeviceStatusInfo),
            ),
        ]

    # The ARN of a device.
    device_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The serial number of a device.
    device_serial_number: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of a device.
    device_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of a device.
    device_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The software version of a device.
    software_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The MAC address of a device.
    mac_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The room ARN of a device.
    room_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of a device. If the status is not READY, check the
    # DeviceStatusInfo value for details.
    device_status: "DeviceStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Detailed information about a device's status.
    device_status_info: "DeviceStatusInfo" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeviceData(autoboto.ShapeBase):
    """
    Device attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_arn",
                "DeviceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "device_serial_number",
                "DeviceSerialNumber",
                autoboto.TypeInfo(str),
            ),
            (
                "device_type",
                "DeviceType",
                autoboto.TypeInfo(str),
            ),
            (
                "device_name",
                "DeviceName",
                autoboto.TypeInfo(str),
            ),
            (
                "software_version",
                "SoftwareVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "mac_address",
                "MacAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "device_status",
                "DeviceStatus",
                autoboto.TypeInfo(DeviceStatus),
            ),
            (
                "room_arn",
                "RoomArn",
                autoboto.TypeInfo(str),
            ),
            (
                "room_name",
                "RoomName",
                autoboto.TypeInfo(str),
            ),
            (
                "device_status_info",
                "DeviceStatusInfo",
                autoboto.TypeInfo(DeviceStatusInfo),
            ),
        ]

    # The ARN of a device.
    device_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The serial number of a device.
    device_serial_number: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of a device.
    device_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of a device.
    device_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The software version of a device.
    software_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The MAC address of a device.
    mac_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of a device.
    device_status: "DeviceStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The room ARN associated with a device.
    room_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the room associated with a device.
    room_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Detailed information about a device's status.
    device_status_info: "DeviceStatusInfo" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeviceEvent(autoboto.ShapeBase):
    """
    The list of device events.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(DeviceEventType),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
            (
                "timestamp",
                "Timestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The type of device event.
    type: "DeviceEventType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The value of the event.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time (in epoch) when the event occurred.
    timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class DeviceEventType(Enum):
    CONNECTION_STATUS = "CONNECTION_STATUS"
    DEVICE_STATUS = "DEVICE_STATUS"


@dataclasses.dataclass
class DeviceNotRegisteredException(autoboto.ShapeBase):
    """
    The request failed because this device is no longer registered and therefore no
    longer managed by this account.
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


class DeviceStatus(Enum):
    READY = "READY"
    PENDING = "PENDING"
    WAS_OFFLINE = "WAS_OFFLINE"
    DEREGISTERED = "DEREGISTERED"


@dataclasses.dataclass
class DeviceStatusDetail(autoboto.ShapeBase):
    """
    Details of a device’s status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                autoboto.TypeInfo(DeviceStatusDetailCode),
            ),
        ]

    # The device status detail code.
    code: "DeviceStatusDetailCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class DeviceStatusDetailCode(Enum):
    DEVICE_SOFTWARE_UPDATE_NEEDED = "DEVICE_SOFTWARE_UPDATE_NEEDED"
    DEVICE_WAS_OFFLINE = "DEVICE_WAS_OFFLINE"


@dataclasses.dataclass
class DeviceStatusInfo(autoboto.ShapeBase):
    """
    Detailed information about a device's status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_status_details",
                "DeviceStatusDetails",
                autoboto.TypeInfo(typing.List[DeviceStatusDetail]),
            ),
            (
                "connection_status",
                "ConnectionStatus",
                autoboto.TypeInfo(ConnectionStatus),
            ),
        ]

    # One or more device status detail descriptions.
    device_status_details: typing.List["DeviceStatusDetail"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )

    # The latest available information about the connection status of a device.
    connection_status: "ConnectionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateContactFromAddressBookRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "contact_arn",
                "ContactArn",
                autoboto.TypeInfo(str),
            ),
            (
                "address_book_arn",
                "AddressBookArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the contact to disassociate from an address book.
    contact_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the address from which to disassociate the contact.
    address_book_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateContactFromAddressBookResponse(autoboto.OutputShapeBase):
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
class DisassociateDeviceFromRoomRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_arn",
                "DeviceArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the device to disassociate from a room. Required.
    device_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateDeviceFromRoomResponse(autoboto.OutputShapeBase):
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
class DisassociateSkillGroupFromRoomRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_arn",
                "SkillGroupArn",
                autoboto.TypeInfo(str),
            ),
            (
                "room_arn",
                "RoomArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the skill group to disassociate from a room. Required.
    skill_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the room from which the skill group is to be disassociated.
    # Required.
    room_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateSkillGroupFromRoomResponse(autoboto.OutputShapeBase):
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


class DistanceUnit(Enum):
    METRIC = "METRIC"
    IMPERIAL = "IMPERIAL"


class EnrollmentStatus(Enum):
    INITIALIZED = "INITIALIZED"
    PENDING = "PENDING"
    REGISTERED = "REGISTERED"
    DISASSOCIATING = "DISASSOCIATING"
    DEREGISTERING = "DEREGISTERING"


class Feature(Enum):
    BLUETOOTH = "BLUETOOTH"
    VOLUME = "VOLUME"
    NOTIFICATIONS = "NOTIFICATIONS"
    LISTS = "LISTS"
    SKILLS = "SKILLS"
    ALL = "ALL"


@dataclasses.dataclass
class Filter(autoboto.ShapeBase):
    """
    A filter name and value pair that is used to return a more specific list of
    results. Filters can be used to match a set of resources by various criteria.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "values",
                "Values",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The key of a filter.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The values of a filter.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class GetAddressBookRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address_book_arn",
                "AddressBookArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the address book for which to request details.
    address_book_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetAddressBookResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "address_book",
                "AddressBook",
                autoboto.TypeInfo(AddressBook),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details of the requested address book.
    address_book: "AddressBook" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetContactRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "contact_arn",
                "ContactArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the contact for which to request details.
    contact_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetContactResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "contact",
                "Contact",
                autoboto.TypeInfo(Contact),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details of the requested contact.
    contact: "Contact" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetDeviceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_arn",
                "DeviceArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the device for which to request details. Required.
    device_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeviceResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "device",
                "Device",
                autoboto.TypeInfo(Device),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details of the device requested. Required.
    device: "Device" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "profile_arn",
                "ProfileArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the room profile for which to request details. Required.
    profile_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetProfileResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "profile",
                "Profile",
                autoboto.TypeInfo(Profile),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details of the room profile requested. Required.
    profile: "Profile" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetRoomRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "room_arn",
                "RoomArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the room for which to request details. Required.
    room_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRoomResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "room",
                "Room",
                autoboto.TypeInfo(Room),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details of the room requested.
    room: "Room" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetRoomSkillParameterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_id",
                "SkillId",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_key",
                "ParameterKey",
                autoboto.TypeInfo(str),
            ),
            (
                "room_arn",
                "RoomArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the skill from which to get the room skill parameter details.
    # Required.
    skill_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The room skill parameter key for which to get details. Required.
    parameter_key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the room from which to get the room skill parameter details.
    room_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRoomSkillParameterResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "room_skill_parameter",
                "RoomSkillParameter",
                autoboto.TypeInfo(RoomSkillParameter),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details of the room skill parameter requested. Required.
    room_skill_parameter: "RoomSkillParameter" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetSkillGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_arn",
                "SkillGroupArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the skill group for which to get details. Required.
    skill_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSkillGroupResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "skill_group",
                "SkillGroup",
                autoboto.TypeInfo(SkillGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details of the skill group requested. Required.
    skill_group: "SkillGroup" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class InvalidUserStatusException(autoboto.ShapeBase):
    """
    The attempt to update a user is invalid due to the user's current status. HTTP
    Status Code: 400
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
class LimitExceededException(autoboto.ShapeBase):
    """
    You are performing an action that would put you beyond your account's limits.
    HTTP Status Code: 400
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
class ListDeviceEventsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_arn",
                "DeviceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "event_type",
                "EventType",
                autoboto.TypeInfo(DeviceEventType),
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

    # The ARN of a device.
    device_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The event type to filter device events. If EventType isn't specified, this
    # returns a list of all device events in reverse chronological order. If
    # EventType is specified, this returns a list of device events for that
    # EventType in reverse chronological order.
    event_type: "DeviceEventType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response only includes results beyond the token, up to the value specified
    # by MaxResults. When the end of results is reached, the response has a value
    # of null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. The default value
    # is 50. If more results exist than the specified MaxResults value, a token
    # is included in the response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


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
                "device_events",
                "DeviceEvents",
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

    # The device events requested for the device ARN.
    device_events: typing.List["DeviceEvent"] = dataclasses.field(
        default_factory=list,
    )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSkillsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_arn",
                "SkillGroupArn",
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

    # The ARN of the skill group for which to list enabled skills. Required.
    skill_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`. Required.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved. Required.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSkillsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "skill_summaries",
                "SkillSummaries",
                autoboto.TypeInfo(typing.List[SkillSummary]),
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

    # The list of enabled skills requested. Required.
    skill_summaries: typing.List["SkillSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
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

    # The ARN of the specified resource for which to list tags.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsResponse(autoboto.OutputShapeBase):
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
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
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

    # The tags requested for the specified resource.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NameInUseException(autoboto.ShapeBase):
    """
    The name sent in the request is already in use. HTTP Status Code: 400
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
class NotFoundException(autoboto.ShapeBase):
    """
    The resource is not found. HTTP Status Code: 400
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
class Profile(autoboto.ShapeBase):
    """
    A room profile with attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "profile_arn",
                "ProfileArn",
                autoboto.TypeInfo(str),
            ),
            (
                "profile_name",
                "ProfileName",
                autoboto.TypeInfo(str),
            ),
            (
                "address",
                "Address",
                autoboto.TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                autoboto.TypeInfo(str),
            ),
            (
                "distance_unit",
                "DistanceUnit",
                autoboto.TypeInfo(DistanceUnit),
            ),
            (
                "temperature_unit",
                "TemperatureUnit",
                autoboto.TypeInfo(TemperatureUnit),
            ),
            (
                "wake_word",
                "WakeWord",
                autoboto.TypeInfo(WakeWord),
            ),
            (
                "setup_mode_disabled",
                "SetupModeDisabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "max_volume_limit",
                "MaxVolumeLimit",
                autoboto.TypeInfo(int),
            ),
            (
                "pstn_enabled",
                "PSTNEnabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ARN of a room profile.
    profile_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of a room profile.
    profile_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The address of a room profile.
    address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time zone of a room profile.
    timezone: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The distance unit of a room profile.
    distance_unit: "DistanceUnit" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The temperature unit of a room profile.
    temperature_unit: "TemperatureUnit" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The wake word of a room profile.
    wake_word: "WakeWord" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The setup mode of a room profile.
    setup_mode_disabled: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The max volume limit of a room profile.
    max_volume_limit: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The PSTN setting of a room profile.
    pstn_enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProfileData(autoboto.ShapeBase):
    """
    The data of a room profile.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "profile_arn",
                "ProfileArn",
                autoboto.TypeInfo(str),
            ),
            (
                "profile_name",
                "ProfileName",
                autoboto.TypeInfo(str),
            ),
            (
                "address",
                "Address",
                autoboto.TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                autoboto.TypeInfo(str),
            ),
            (
                "distance_unit",
                "DistanceUnit",
                autoboto.TypeInfo(DistanceUnit),
            ),
            (
                "temperature_unit",
                "TemperatureUnit",
                autoboto.TypeInfo(TemperatureUnit),
            ),
            (
                "wake_word",
                "WakeWord",
                autoboto.TypeInfo(WakeWord),
            ),
        ]

    # The ARN of a room profile.
    profile_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of a room profile.
    profile_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The address of a room profile.
    address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The timezone of a room profile.
    timezone: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The distance unit of a room profile.
    distance_unit: "DistanceUnit" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The temperature unit of a room profile.
    temperature_unit: "TemperatureUnit" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The wake word of a room profile.
    wake_word: "WakeWord" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutRoomSkillParameterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_id",
                "SkillId",
                autoboto.TypeInfo(str),
            ),
            (
                "room_skill_parameter",
                "RoomSkillParameter",
                autoboto.TypeInfo(RoomSkillParameter),
            ),
            (
                "room_arn",
                "RoomArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the skill associated with the room skill parameter. Required.
    skill_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated room skill parameter. Required.
    room_skill_parameter: "RoomSkillParameter" = dataclasses.field(
        default_factory=dict,
    )

    # The ARN of the room associated with the room skill parameter. Required.
    room_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutRoomSkillParameterResponse(autoboto.OutputShapeBase):
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
class ResolveRoomRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_id",
                "UserId",
                autoboto.TypeInfo(str),
            ),
            (
                "skill_id",
                "SkillId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the user. Required.
    user_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the skill that was requested. Required.
    skill_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResolveRoomResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "room_arn",
                "RoomArn",
                autoboto.TypeInfo(str),
            ),
            (
                "room_name",
                "RoomName",
                autoboto.TypeInfo(str),
            ),
            (
                "room_skill_parameters",
                "RoomSkillParameters",
                autoboto.TypeInfo(typing.List[RoomSkillParameter]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the room from which the skill request was invoked.
    room_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the room from which the skill request was invoked.
    room_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Response to get the room profile request. Required.
    room_skill_parameters: typing.List["RoomSkillParameter"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )


@dataclasses.dataclass
class ResourceInUseException(autoboto.ShapeBase):
    """
    The resource in the request is already in use. HTTP Status Code: 400
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
                "client_request_token",
                "ClientRequestToken",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # User specified token that is used to support idempotency during Create
    # Resource
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RevokeInvitationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "UserArn",
                autoboto.TypeInfo(str),
            ),
            (
                "enrollment_id",
                "EnrollmentId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the user for whom to revoke an enrollment invitation. Required.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the enrollment invitation to revoke. Required.
    enrollment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RevokeInvitationResponse(autoboto.OutputShapeBase):
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
class Room(autoboto.ShapeBase):
    """
    A room with attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "room_arn",
                "RoomArn",
                autoboto.TypeInfo(str),
            ),
            (
                "room_name",
                "RoomName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_calendar_id",
                "ProviderCalendarId",
                autoboto.TypeInfo(str),
            ),
            (
                "profile_arn",
                "ProfileArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of a room.
    room_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of a room.
    room_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of a room.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The provider calendar ARN of a room.
    provider_calendar_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The profile ARN of a room.
    profile_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RoomData(autoboto.ShapeBase):
    """
    The data of a room.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "room_arn",
                "RoomArn",
                autoboto.TypeInfo(str),
            ),
            (
                "room_name",
                "RoomName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_calendar_id",
                "ProviderCalendarId",
                autoboto.TypeInfo(str),
            ),
            (
                "profile_arn",
                "ProfileArn",
                autoboto.TypeInfo(str),
            ),
            (
                "profile_name",
                "ProfileName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of a room.
    room_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of a room.
    room_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of a room.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The provider calendar ARN of a room.
    provider_calendar_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The profile ARN of a room.
    profile_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The profile name of a room.
    profile_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RoomSkillParameter(autoboto.ShapeBase):
    """
    A skill parameter associated with a room.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_key",
                "ParameterKey",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_value",
                "ParameterValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The parameter key of a room skill parameter. ParameterKey is an enumerated
    # type that only takes “DEFAULT” or “SCOPE” as valid values.
    parameter_key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The parameter value of a room skill parameter.
    parameter_value: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SearchAddressBooksRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                autoboto.TypeInfo(typing.List[Sort]),
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

    # The filters to use to list a specified set of address books. The supported
    # filter key is AddressBookName.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The sort order to use in listing the specified set of address books. The
    # supported sort key is AddressBookName.
    sort_criteria: typing.List["Sort"] = dataclasses.field(
        default_factory=list,
    )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response only includes results beyond the token, up to the value specified
    # by MaxResults.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified MaxResults value, a token is included in the
    # response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchAddressBooksResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "address_books",
                "AddressBooks",
                autoboto.TypeInfo(typing.List[AddressBookData]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "total_count",
                "TotalCount",
                autoboto.TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The address books that meet the specified set of filter criteria, in sort
    # order.
    address_books: typing.List["AddressBookData"] = dataclasses.field(
        default_factory=list,
    )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total number of address books returned.
    total_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchContactsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                autoboto.TypeInfo(typing.List[Sort]),
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

    # The filters to use to list a specified set of address books. The supported
    # filter keys are DisplayName, FirstName, LastName, and AddressBookArns.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The sort order to use in listing the specified set of contacts. The
    # supported sort keys are DisplayName, FirstName, and LastName.
    sort_criteria: typing.List["Sort"] = dataclasses.field(
        default_factory=list,
    )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response only includes results beyond the token, up to the value specified
    # by MaxResults.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified MaxResults value, a token is included in the
    # response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchContactsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "contacts",
                "Contacts",
                autoboto.TypeInfo(typing.List[ContactData]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "total_count",
                "TotalCount",
                autoboto.TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The contacts that meet the specified set of filter criteria, in sort order.
    contacts: typing.List["ContactData"] = dataclasses.field(
        default_factory=list,
    )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total number of contacts returned.
    total_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchDevicesRequest(autoboto.ShapeBase):
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
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                autoboto.TypeInfo(typing.List[Sort]),
            ),
        ]

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The filters to use to list a specified set of devices. Supported filter
    # keys are DeviceName, DeviceStatus, DeviceStatusDetailCode, RoomName,
    # DeviceType, DeviceSerialNumber, UnassociatedOnly, and ConnectionStatus
    # (ONLINE and OFFLINE).
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The sort order to use in listing the specified set of devices. Supported
    # sort keys are DeviceName, DeviceStatus, RoomName, DeviceType,
    # DeviceSerialNumber, and ConnectionStatus.
    sort_criteria: typing.List["Sort"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class SearchDevicesResponse(autoboto.OutputShapeBase):
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
                autoboto.TypeInfo(typing.List[DeviceData]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "total_count",
                "TotalCount",
                autoboto.TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The devices that meet the specified set of filter criteria, in sort order.
    devices: typing.List["DeviceData"] = dataclasses.field(
        default_factory=list,
    )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total number of devices returned.
    total_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchProfilesRequest(autoboto.ShapeBase):
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
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                autoboto.TypeInfo(typing.List[Sort]),
            ),
        ]

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The filters to use to list a specified set of room profiles. Supported
    # filter keys are ProfileName and Address. Required.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The sort order to use in listing the specified set of room profiles.
    # Supported sort keys are ProfileName and Address.
    sort_criteria: typing.List["Sort"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class SearchProfilesResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "profiles",
                "Profiles",
                autoboto.TypeInfo(typing.List[ProfileData]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "total_count",
                "TotalCount",
                autoboto.TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The profiles that meet the specified set of filter criteria, in sort order.
    profiles: typing.List["ProfileData"] = dataclasses.field(
        default_factory=list,
    )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total number of room profiles returned.
    total_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchRoomsRequest(autoboto.ShapeBase):
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
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                autoboto.TypeInfo(typing.List[Sort]),
            ),
        ]

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The filters to use to list a specified set of rooms. The supported filter
    # keys are RoomName and ProfileName.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The sort order to use in listing the specified set of rooms. The supported
    # sort keys are RoomName and ProfileName.
    sort_criteria: typing.List["Sort"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class SearchRoomsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rooms",
                "Rooms",
                autoboto.TypeInfo(typing.List[RoomData]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "total_count",
                "TotalCount",
                autoboto.TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The rooms that meet the specified set of filter criteria, in sort order.
    rooms: typing.List["RoomData"] = dataclasses.field(default_factory=list, )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total number of rooms returned.
    total_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchSkillGroupsRequest(autoboto.ShapeBase):
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
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                autoboto.TypeInfo(typing.List[Sort]),
            ),
        ]

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`. Required.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The filters to use to list a specified set of skill groups. The supported
    # filter key is SkillGroupName.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The sort order to use in listing the specified set of skill groups. The
    # supported sort key is SkillGroupName.
    sort_criteria: typing.List["Sort"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class SearchSkillGroupsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "skill_groups",
                "SkillGroups",
                autoboto.TypeInfo(typing.List[SkillGroupData]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "total_count",
                "TotalCount",
                autoboto.TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The skill groups that meet the filter criteria, in sort order.
    skill_groups: typing.List["SkillGroupData"] = dataclasses.field(
        default_factory=list,
    )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total number of skill groups returned.
    total_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchUsersRequest(autoboto.ShapeBase):
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
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                autoboto.TypeInfo(typing.List[Sort]),
            ),
        ]

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`. Required.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved. Required.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The filters to use for listing a specific set of users. Required. Supported
    # filter keys are UserId, FirstName, LastName, Email, and EnrollmentStatus.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The sort order to use in listing the filtered set of users. Required.
    # Supported sort keys are UserId, FirstName, LastName, Email, and
    # EnrollmentStatus.
    sort_criteria: typing.List["Sort"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class SearchUsersResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "users",
                "Users",
                autoboto.TypeInfo(typing.List[UserData]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "total_count",
                "TotalCount",
                autoboto.TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The users that meet the specified set of filter criteria, in sort order.
    users: typing.List["UserData"] = dataclasses.field(default_factory=list, )

    # The token returned to indicate that there is more data available.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total number of users returned.
    total_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendInvitationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "UserArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the user to whom to send an invitation. Required.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendInvitationResponse(autoboto.OutputShapeBase):
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
class SkillGroup(autoboto.ShapeBase):
    """
    A skill group with attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_arn",
                "SkillGroupArn",
                autoboto.TypeInfo(str),
            ),
            (
                "skill_group_name",
                "SkillGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of a skill group.
    skill_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of a skill group.
    skill_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description of a skill group.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SkillGroupData(autoboto.ShapeBase):
    """
    The attributes of a skill group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_arn",
                "SkillGroupArn",
                autoboto.TypeInfo(str),
            ),
            (
                "skill_group_name",
                "SkillGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The skill group ARN of a skill group.
    skill_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The skill group name of a skill group.
    skill_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description of a skill group.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SkillSummary(autoboto.ShapeBase):
    """
    The summary of skills.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_id",
                "SkillId",
                autoboto.TypeInfo(str),
            ),
            (
                "skill_name",
                "SkillName",
                autoboto.TypeInfo(str),
            ),
            (
                "supports_linking",
                "SupportsLinking",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ARN of the skill summary.
    skill_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the skill.
    skill_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Linking support for a skill.
    supports_linking: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Sort(autoboto.ShapeBase):
    """
    An object representing a sort criteria.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(SortValue),
            ),
        ]

    # The sort key of a sort object.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The sort value of a sort object.
    value: "SortValue" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class SortValue(Enum):
    ASC = "ASC"
    DESC = "DESC"


@dataclasses.dataclass
class StartDeviceSyncRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "features",
                "Features",
                autoboto.TypeInfo(typing.List[Feature]),
            ),
            (
                "room_arn",
                "RoomArn",
                autoboto.TypeInfo(str),
            ),
            (
                "device_arn",
                "DeviceArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # Request structure to start the device sync. Required.
    features: typing.List["Feature"] = dataclasses.field(default_factory=list, )

    # The ARN of the room with which the device to sync is associated. Required.
    room_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the device to sync. Required.
    device_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartDeviceSyncResponse(autoboto.OutputShapeBase):
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
class Tag(autoboto.ShapeBase):
    """
    A key-value pair that can be associated with a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
        ]

    # The key of a tag. Tag keys are case-sensitive.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value of a tag. Tag values are case-sensitive and can be null.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The ARN of the resource to which to add metadata tags. Required.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tags to be added to the specified resource. Do not provide system tags.
    # Required.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class TagResourceResponse(autoboto.OutputShapeBase):
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


class TemperatureUnit(Enum):
    FAHRENHEIT = "FAHRENHEIT"
    CELSIUS = "CELSIUS"


@dataclasses.dataclass
class UntagResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN of the resource from which to remove metadata tags. Required.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tags to be removed from the specified resource. Do not provide system
    # tags. Required.
    tag_keys: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UntagResourceResponse(autoboto.OutputShapeBase):
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
class UpdateAddressBookRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address_book_arn",
                "AddressBookArn",
                autoboto.TypeInfo(str),
            ),
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

    # The ARN of the room to update.
    address_book_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated name of the room.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated description of the room.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateAddressBookResponse(autoboto.OutputShapeBase):
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
class UpdateContactRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "contact_arn",
                "ContactArn",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "first_name",
                "FirstName",
                autoboto.TypeInfo(str),
            ),
            (
                "last_name",
                "LastName",
                autoboto.TypeInfo(str),
            ),
            (
                "phone_number",
                "PhoneNumber",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the contact to update.
    contact_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated display name of the contact.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated first name of the contact.
    first_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated last name of the contact.
    last_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated phone number of the contact.
    phone_number: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateContactResponse(autoboto.OutputShapeBase):
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
class UpdateDeviceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_arn",
                "DeviceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "device_name",
                "DeviceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the device to update. Required.
    device_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated device name. Required.
    device_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDeviceResponse(autoboto.OutputShapeBase):
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
class UpdateProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "profile_arn",
                "ProfileArn",
                autoboto.TypeInfo(str),
            ),
            (
                "profile_name",
                "ProfileName",
                autoboto.TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                autoboto.TypeInfo(str),
            ),
            (
                "address",
                "Address",
                autoboto.TypeInfo(str),
            ),
            (
                "distance_unit",
                "DistanceUnit",
                autoboto.TypeInfo(DistanceUnit),
            ),
            (
                "temperature_unit",
                "TemperatureUnit",
                autoboto.TypeInfo(TemperatureUnit),
            ),
            (
                "wake_word",
                "WakeWord",
                autoboto.TypeInfo(WakeWord),
            ),
            (
                "setup_mode_disabled",
                "SetupModeDisabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "max_volume_limit",
                "MaxVolumeLimit",
                autoboto.TypeInfo(int),
            ),
            (
                "pstn_enabled",
                "PSTNEnabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ARN of the room profile to update. Required.
    profile_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated name for the room profile.
    profile_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated timezone for the room profile.
    timezone: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated address for the room profile.
    address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated distance unit for the room profile.
    distance_unit: "DistanceUnit" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated temperature unit for the room profile.
    temperature_unit: "TemperatureUnit" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated wake word for the room profile.
    wake_word: "WakeWord" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether the setup mode of the profile is enabled.
    setup_mode_disabled: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated maximum volume limit for the room profile.
    max_volume_limit: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether the PSTN setting of the room profile is enabled.
    pstn_enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateProfileResponse(autoboto.OutputShapeBase):
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
class UpdateRoomRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "room_arn",
                "RoomArn",
                autoboto.TypeInfo(str),
            ),
            (
                "room_name",
                "RoomName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_calendar_id",
                "ProviderCalendarId",
                autoboto.TypeInfo(str),
            ),
            (
                "profile_arn",
                "ProfileArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the room to update.
    room_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated name for the room.
    room_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated description for the room.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated provider calendar ARN for the room.
    provider_calendar_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated profile ARN for the room.
    profile_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateRoomResponse(autoboto.OutputShapeBase):
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
class UpdateSkillGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skill_group_arn",
                "SkillGroupArn",
                autoboto.TypeInfo(str),
            ),
            (
                "skill_group_name",
                "SkillGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the skill group to update.
    skill_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated name for the skill group.
    skill_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated description for the skill group.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateSkillGroupResponse(autoboto.OutputShapeBase):
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
class UserData(autoboto.ShapeBase):
    """
    Information related to a user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "UserArn",
                autoboto.TypeInfo(str),
            ),
            (
                "first_name",
                "FirstName",
                autoboto.TypeInfo(str),
            ),
            (
                "last_name",
                "LastName",
                autoboto.TypeInfo(str),
            ),
            (
                "email",
                "Email",
                autoboto.TypeInfo(str),
            ),
            (
                "enrollment_status",
                "EnrollmentStatus",
                autoboto.TypeInfo(EnrollmentStatus),
            ),
            (
                "enrollment_id",
                "EnrollmentId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of a user.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The first name of a user.
    first_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The last name of a user.
    last_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The email of a user.
    email: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The enrollment status of a user.
    enrollment_status: "EnrollmentStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The enrollment ARN of a user.
    enrollment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class WakeWord(Enum):
    ALEXA = "ALEXA"
    AMAZON = "AMAZON"
    ECHO = "ECHO"
    COMPUTER = "COMPUTER"
