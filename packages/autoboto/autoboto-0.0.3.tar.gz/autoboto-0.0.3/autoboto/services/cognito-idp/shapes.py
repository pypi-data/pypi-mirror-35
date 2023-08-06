import datetime
import typing
import autoboto
from enum import Enum
import botocore.response
import dataclasses


@dataclasses.dataclass
class AccountTakeoverActionType(autoboto.ShapeBase):
    """
    Account takeover action type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notify",
                "Notify",
                autoboto.TypeInfo(bool),
            ),
            (
                "event_action",
                "EventAction",
                autoboto.TypeInfo(AccountTakeoverEventActionType),
            ),
        ]

    # Flag specifying whether to send a notification.
    notify: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The event action.

    #   * `BLOCK` Choosing this action will block the request.

    #   * `MFA_IF_CONFIGURED` Throw MFA challenge if user has configured it, else allow the request.

    #   * `MFA_REQUIRED` Throw MFA challenge if user has configured it, else block the request.

    #   * `NO_ACTION` Allow the user sign-in.
    event_action: "AccountTakeoverEventActionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AccountTakeoverActionsType(autoboto.ShapeBase):
    """
    Account takeover actions type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "low_action",
                "LowAction",
                autoboto.TypeInfo(AccountTakeoverActionType),
            ),
            (
                "medium_action",
                "MediumAction",
                autoboto.TypeInfo(AccountTakeoverActionType),
            ),
            (
                "high_action",
                "HighAction",
                autoboto.TypeInfo(AccountTakeoverActionType),
            ),
        ]

    # Action to take for a low risk.
    low_action: "AccountTakeoverActionType" = dataclasses.field(
        default_factory=dict,
    )

    # Action to take for a medium risk.
    medium_action: "AccountTakeoverActionType" = dataclasses.field(
        default_factory=dict,
    )

    # Action to take for a high risk.
    high_action: "AccountTakeoverActionType" = dataclasses.field(
        default_factory=dict,
    )


class AccountTakeoverEventActionType(Enum):
    BLOCK = "BLOCK"
    MFA_IF_CONFIGURED = "MFA_IF_CONFIGURED"
    MFA_REQUIRED = "MFA_REQUIRED"
    NO_ACTION = "NO_ACTION"


@dataclasses.dataclass
class AccountTakeoverRiskConfigurationType(autoboto.ShapeBase):
    """
    Configuration for mitigation actions and notification for different levels of
    risk detected for a potential account takeover.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "actions",
                "Actions",
                autoboto.TypeInfo(AccountTakeoverActionsType),
            ),
            (
                "notify_configuration",
                "NotifyConfiguration",
                autoboto.TypeInfo(NotifyConfigurationType),
            ),
        ]

    # Account takeover risk configuration actions
    actions: "AccountTakeoverActionsType" = dataclasses.field(
        default_factory=dict,
    )

    # The notify configuration used to construct email notifications.
    notify_configuration: "NotifyConfigurationType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class AddCustomAttributesRequest(autoboto.ShapeBase):
    """
    Represents the request to add custom attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_attributes",
                "CustomAttributes",
                autoboto.TypeInfo(typing.List[SchemaAttributeType]),
            ),
        ]

    # The user pool ID for the user pool where you want to add custom attributes.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of custom attributes, such as Mutable and Name.
    custom_attributes: typing.List["SchemaAttributeType"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AddCustomAttributesResponse(autoboto.ShapeBase):
    """
    Represents the response from the server for the request to add custom
    attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AdminAddUserToGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "group_name",
                "GroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The username for the user.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The group name.
    group_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AdminConfirmSignUpRequest(autoboto.ShapeBase):
    """
    Represents the request to confirm user registration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for which you want to confirm user registration.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name for which you want to confirm user registration.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AdminConfirmSignUpResponse(autoboto.ShapeBase):
    """
    Represents the response from the server for the request to confirm registration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AdminCreateUserConfigType(autoboto.ShapeBase):
    """
    The configuration for creating a new user profile.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "allow_admin_create_user_only",
                "AllowAdminCreateUserOnly",
                autoboto.TypeInfo(bool),
            ),
            (
                "unused_account_validity_days",
                "UnusedAccountValidityDays",
                autoboto.TypeInfo(int),
            ),
            (
                "invite_message_template",
                "InviteMessageTemplate",
                autoboto.TypeInfo(MessageTemplateType),
            ),
        ]

    # Set to `True` if only the administrator is allowed to create user profiles.
    # Set to `False` if users can sign themselves up via an app.
    allow_admin_create_user_only: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The user account expiration limit, in days, after which the account is no
    # longer usable. To reset the account after that time limit, you must call
    # `AdminCreateUser` again, specifying `"RESEND"` for the `MessageAction`
    # parameter. The default value for this parameter is 7.
    unused_account_validity_days: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The message template to be used for the welcome message to new users.

    # See also [Customizing User Invitation
    # Messages](http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-
    # user-pool-settings-message-customizations.html#cognito-user-pool-settings-
    # user-invitation-message-customization).
    invite_message_template: "MessageTemplateType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class AdminCreateUserRequest(autoboto.ShapeBase):
    """
    Represents the request to create a user in the specified user pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "user_attributes",
                "UserAttributes",
                autoboto.TypeInfo(typing.List[AttributeType]),
            ),
            (
                "validation_data",
                "ValidationData",
                autoboto.TypeInfo(typing.List[AttributeType]),
            ),
            (
                "temporary_password",
                "TemporaryPassword",
                autoboto.TypeInfo(str),
            ),
            (
                "force_alias_creation",
                "ForceAliasCreation",
                autoboto.TypeInfo(bool),
            ),
            (
                "message_action",
                "MessageAction",
                autoboto.TypeInfo(MessageActionType),
            ),
            (
                "desired_delivery_mediums",
                "DesiredDeliveryMediums",
                autoboto.TypeInfo(typing.List[DeliveryMediumType]),
            ),
        ]

    # The user pool ID for the user pool where the user will be created.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The username for the user. Must be unique within the user pool. Must be a
    # UTF-8 string between 1 and 128 characters. After the user is created, the
    # username cannot be changed.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of name-value pairs that contain user attributes and attribute
    # values to be set for the user to be created. You can create a user without
    # specifying any attributes other than `Username`. However, any attributes
    # that you specify as required (in or in the **Attributes** tab of the
    # console) must be supplied either by you (in your call to `AdminCreateUser`)
    # or by the user (when he or she signs up in response to your welcome
    # message).

    # For custom attributes, you must prepend the `custom:` prefix to the
    # attribute name.

    # To send a message inviting the user to sign up, you must specify the user's
    # email address or phone number. This can be done in your call to
    # AdminCreateUser or in the **Users** tab of the Amazon Cognito console for
    # managing your user pools.

    # In your call to `AdminCreateUser`, you can set the `email_verified`
    # attribute to `True`, and you can set the `phone_number_verified` attribute
    # to `True`. (You can also do this by calling .)

    #   * **email** : The email address of the user to whom the message that contains the code and username will be sent. Required if the `email_verified` attribute is set to `True`, or if `"EMAIL"` is specified in the `DesiredDeliveryMediums` parameter.

    #   * **phone_number** : The phone number of the user to whom the message that contains the code and username will be sent. Required if the `phone_number_verified` attribute is set to `True`, or if `"SMS"` is specified in the `DesiredDeliveryMediums` parameter.
    user_attributes: typing.List["AttributeType"] = dataclasses.field(
        default_factory=list,
    )

    # The user's validation data. This is an array of name-value pairs that
    # contain user attributes and attribute values that you can use for custom
    # validation, such as restricting the types of user accounts that can be
    # registered. For example, you might choose to allow or disallow user sign-up
    # based on the user's domain.

    # To configure custom validation, you must create a Pre Sign-up Lambda
    # trigger for the user pool as described in the Amazon Cognito Developer
    # Guide. The Lambda trigger receives the validation data and uses it in the
    # validation process.

    # The user's validation data is not persisted.
    validation_data: typing.List["AttributeType"] = dataclasses.field(
        default_factory=list,
    )

    # The user's temporary password. This password must conform to the password
    # policy that you specified when you created the user pool.

    # The temporary password is valid only once. To complete the Admin Create
    # User flow, the user must enter the temporary password in the sign-in page
    # along with a new password to be used in all future sign-ins.

    # This parameter is not required. If you do not specify a value, Amazon
    # Cognito generates one for you.

    # The temporary password can only be used until the user account expiration
    # limit that you specified when you created the user pool. To reset the
    # account after that time limit, you must call `AdminCreateUser` again,
    # specifying `"RESEND"` for the `MessageAction` parameter.
    temporary_password: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # This parameter is only used if the `phone_number_verified` or
    # `email_verified` attribute is set to `True`. Otherwise, it is ignored.

    # If this parameter is set to `True` and the phone number or email address
    # specified in the UserAttributes parameter already exists as an alias with a
    # different user, the API call will migrate the alias from the previous user
    # to the newly created user. The previous user will no longer be able to log
    # in using that alias.

    # If this parameter is set to `False`, the API throws an
    # `AliasExistsException` error if the alias already exists. The default value
    # is `False`.
    force_alias_creation: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Set to `"RESEND"` to resend the invitation message to a user that already
    # exists and reset the expiration limit on the user's account. Set to
    # `"SUPPRESS"` to suppress sending the message. Only one value can be
    # specified.
    message_action: "MessageActionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specify `"EMAIL"` if email will be used to send the welcome message.
    # Specify `"SMS"` if the phone number will be used. The default value is
    # `"SMS"`. More than one value can be specified.
    desired_delivery_mediums: typing.List["DeliveryMediumType"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )


@dataclasses.dataclass
class AdminCreateUserResponse(autoboto.ShapeBase):
    """
    Represents the response from the server to the request to create the user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user",
                "User",
                autoboto.TypeInfo(UserType),
            ),
        ]

    # The newly created user.
    user: "UserType" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class AdminDeleteUserAttributesRequest(autoboto.ShapeBase):
    """
    Represents the request to delete user attributes as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "user_attribute_names",
                "UserAttributeNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The user pool ID for the user pool where you want to delete user
    # attributes.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name of the user from which you would like to delete attributes.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of strings representing the user attribute names you wish to
    # delete.

    # For custom attributes, you must prepend the `custom:` prefix to the
    # attribute name.
    user_attribute_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AdminDeleteUserAttributesResponse(autoboto.ShapeBase):
    """
    Represents the response received from the server for a request to delete user
    attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AdminDeleteUserRequest(autoboto.ShapeBase):
    """
    Represents the request to delete a user as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool where you want to delete the user.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name of the user you wish to delete.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AdminDisableProviderForUserRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "user",
                "User",
                autoboto.TypeInfo(ProviderUserIdentifierType),
            ),
        ]

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user to be disabled.
    user: "ProviderUserIdentifierType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class AdminDisableProviderForUserResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AdminDisableUserRequest(autoboto.ShapeBase):
    """
    Represents the request to disable any user as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool where you want to disable the user.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name of the user you wish to disable.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AdminDisableUserResponse(autoboto.ShapeBase):
    """
    Represents the response received from the server to disable the user as an
    administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AdminEnableUserRequest(autoboto.ShapeBase):
    """
    Represents the request that enables the user as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool where you want to enable the user.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name of the user you wish to enable.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AdminEnableUserResponse(autoboto.ShapeBase):
    """
    Represents the response from the server for the request to enable a user as an
    administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AdminForgetDeviceRequest(autoboto.ShapeBase):
    """
    Sends the forgot device request, as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "device_key",
                "DeviceKey",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The device key.
    device_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AdminGetDeviceRequest(autoboto.ShapeBase):
    """
    Represents the request to get the device, as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_key",
                "DeviceKey",
                autoboto.TypeInfo(str),
            ),
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
        ]

    # The device key.
    device_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AdminGetDeviceResponse(autoboto.ShapeBase):
    """
    Gets the device response, as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device",
                "Device",
                autoboto.TypeInfo(DeviceType),
            ),
        ]

    # The device.
    device: "DeviceType" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class AdminGetUserRequest(autoboto.ShapeBase):
    """
    Represents the request to get the specified user as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool where you want to get information about
    # the user.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name of the user you wish to retrieve.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AdminGetUserResponse(autoboto.ShapeBase):
    """
    Represents the response from the server from the request to get the specified
    user as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "user_attributes",
                "UserAttributes",
                autoboto.TypeInfo(typing.List[AttributeType]),
            ),
            (
                "user_create_date",
                "UserCreateDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "user_last_modified_date",
                "UserLastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "user_status",
                "UserStatus",
                autoboto.TypeInfo(UserStatusType),
            ),
            (
                "mfa_options",
                "MFAOptions",
                autoboto.TypeInfo(typing.List[MFAOptionType]),
            ),
            (
                "preferred_mfa_setting",
                "PreferredMfaSetting",
                autoboto.TypeInfo(str),
            ),
            (
                "user_mfa_setting_list",
                "UserMFASettingList",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The user name of the user about whom you are receiving information.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of name-value pairs representing user attributes.
    user_attributes: typing.List["AttributeType"] = dataclasses.field(
        default_factory=list,
    )

    # The date the user was created.
    user_create_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the user was last modified.
    user_last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates that the status is enabled.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user status. Can be one of the following:

    #   * UNCONFIRMED - User has been created but not confirmed.

    #   * CONFIRMED - User has been confirmed.

    #   * ARCHIVED - User is no longer active.

    #   * COMPROMISED - User is disabled due to a potential security threat.

    #   * UNKNOWN - User status is not known.
    user_status: "UserStatusType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the options for MFA (e.g., email or phone number).
    mfa_options: typing.List["MFAOptionType"] = dataclasses.field(
        default_factory=list,
    )

    # The user's preferred MFA setting.
    preferred_mfa_setting: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The list of the user's MFA settings.
    user_mfa_setting_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AdminInitiateAuthRequest(autoboto.ShapeBase):
    """
    Initiates the authorization request, as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "auth_flow",
                "AuthFlow",
                autoboto.TypeInfo(AuthFlowType),
            ),
            (
                "auth_parameters",
                "AuthParameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "client_metadata",
                "ClientMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "analytics_metadata",
                "AnalyticsMetadata",
                autoboto.TypeInfo(AnalyticsMetadataType),
            ),
            (
                "context_data",
                "ContextData",
                autoboto.TypeInfo(ContextDataType),
            ),
        ]

    # The ID of the Amazon Cognito user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The app client ID.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The authentication flow for this call to execute. The API action will
    # depend on this value. For example:

    #   * `REFRESH_TOKEN_AUTH` will take in a valid refresh token and return new tokens.

    #   * `USER_SRP_AUTH` will take in `USERNAME` and `SRP_A` and return the SRP variables to be used for next challenge execution.

    #   * `USER_PASSWORD_AUTH` will take in `USERNAME` and `PASSWORD` and return the next challenge or tokens.

    # Valid values include:

    #   * `USER_SRP_AUTH`: Authentication flow for the Secure Remote Password (SRP) protocol.

    #   * `REFRESH_TOKEN_AUTH`/`REFRESH_TOKEN`: Authentication flow for refreshing the access token and ID token by supplying a valid refresh token.

    #   * `CUSTOM_AUTH`: Custom authentication flow.

    #   * `ADMIN_NO_SRP_AUTH`: Non-SRP authentication flow; you can pass in the USERNAME and PASSWORD directly if the flow is enabled for calling the app client.

    #   * `USER_PASSWORD_AUTH`: Non-SRP authentication flow; USERNAME and PASSWORD are passed directly. If a user migration Lambda trigger is set, this flow will invoke the user migration Lambda if the USERNAME is not found in the user pool.
    auth_flow: "AuthFlowType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The authentication parameters. These are inputs corresponding to the
    # `AuthFlow` that you are invoking. The required values depend on the value
    # of `AuthFlow`:

    #   * For `USER_SRP_AUTH`: `USERNAME` (required), `SRP_A` (required), `SECRET_HASH` (required if the app client is configured with a client secret), `DEVICE_KEY`

    #   * For `REFRESH_TOKEN_AUTH/REFRESH_TOKEN`: `REFRESH_TOKEN` (required), `SECRET_HASH` (required if the app client is configured with a client secret), `DEVICE_KEY`

    #   * For `ADMIN_NO_SRP_AUTH`: `USERNAME` (required), `SECRET_HASH` (if app client is configured with client secret), `PASSWORD` (required), `DEVICE_KEY`

    #   * For `CUSTOM_AUTH`: `USERNAME` (required), `SECRET_HASH` (if app client is configured with client secret), `DEVICE_KEY`
    auth_parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # This is a random key-value pair map which can contain any key and will be
    # passed to your PreAuthentication Lambda trigger as-is. It can be used to
    # implement additional validations around authentication.
    client_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The analytics metadata for collecting Amazon Pinpoint metrics for
    # `AdminInitiateAuth` calls.
    analytics_metadata: "AnalyticsMetadataType" = dataclasses.field(
        default_factory=dict,
    )

    # Contextual data such as the user's device fingerprint, IP address, or
    # location used for evaluating the risk of an unexpected event by Amazon
    # Cognito advanced security.
    context_data: "ContextDataType" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class AdminInitiateAuthResponse(autoboto.ShapeBase):
    """
    Initiates the authentication response, as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "challenge_name",
                "ChallengeName",
                autoboto.TypeInfo(ChallengeNameType),
            ),
            (
                "session",
                "Session",
                autoboto.TypeInfo(str),
            ),
            (
                "challenge_parameters",
                "ChallengeParameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "authentication_result",
                "AuthenticationResult",
                autoboto.TypeInfo(AuthenticationResultType),
            ),
        ]

    # The name of the challenge which you are responding to with this call. This
    # is returned to you in the `AdminInitiateAuth` response if you need to pass
    # another challenge.

    #   * `MFA_SETUP`: If MFA is required, users who do not have at least one of the MFA methods set up are presented with an `MFA_SETUP` challenge. The user must set up at least one MFA type to continue to authenticate.

    #   * `SELECT_MFA_TYPE`: Selects the MFA type. Valid MFA options are `SMS_MFA` for text SMS MFA, and `SOFTWARE_TOKEN_MFA` for TOTP software token MFA.

    #   * `SMS_MFA`: Next challenge is to supply an `SMS_MFA_CODE`, delivered via SMS.

    #   * `PASSWORD_VERIFIER`: Next challenge is to supply `PASSWORD_CLAIM_SIGNATURE`, `PASSWORD_CLAIM_SECRET_BLOCK`, and `TIMESTAMP` after the client-side SRP calculations.

    #   * `CUSTOM_CHALLENGE`: This is returned if your custom authentication flow determines that the user should pass another challenge before tokens are issued.

    #   * `DEVICE_SRP_AUTH`: If device tracking was enabled on your user pool and the previous challenges were passed, this challenge is returned so that Amazon Cognito can start tracking this device.

    #   * `DEVICE_PASSWORD_VERIFIER`: Similar to `PASSWORD_VERIFIER`, but for devices only.

    #   * `ADMIN_NO_SRP_AUTH`: This is returned if you need to authenticate with `USERNAME` and `PASSWORD` directly. An app client must be enabled to use this flow.

    #   * `NEW_PASSWORD_REQUIRED`: For users which are required to change their passwords after successful first login. This challenge should be passed with `NEW_PASSWORD` and any other required attributes.
    challenge_name: "ChallengeNameType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The session which should be passed both ways in challenge-response calls to
    # the service. If `AdminInitiateAuth` or `AdminRespondToAuthChallenge` API
    # call determines that the caller needs to go through another challenge, they
    # return a session with other challenge parameters. This session should be
    # passed as it is to the next `AdminRespondToAuthChallenge` API call.
    session: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The challenge parameters. These are returned to you in the
    # `AdminInitiateAuth` response if you need to pass another challenge. The
    # responses in this parameter should be used to compute inputs to the next
    # call (`AdminRespondToAuthChallenge`).

    # All challenges require `USERNAME` and `SECRET_HASH` (if applicable).

    # The value of the `USER_ID_FOR_SRP` attribute will be the user's actual
    # username, not an alias (such as email address or phone number), even if you
    # specified an alias in your call to `AdminInitiateAuth`. This is because, in
    # the `AdminRespondToAuthChallenge` API `ChallengeResponses`, the `USERNAME`
    # attribute cannot be an alias.
    challenge_parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The result of the authentication response. This is only returned if the
    # caller does not need to pass another challenge. If the caller does need to
    # pass another challenge before it gets tokens, `ChallengeName`,
    # `ChallengeParameters`, and `Session` are returned.
    authentication_result: "AuthenticationResultType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class AdminLinkProviderForUserRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "destination_user",
                "DestinationUser",
                autoboto.TypeInfo(ProviderUserIdentifierType),
            ),
            (
                "source_user",
                "SourceUser",
                autoboto.TypeInfo(ProviderUserIdentifierType),
            ),
        ]

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The existing user in the user pool to be linked to the external identity
    # provider user account. Can be a native (Username + Password) Cognito User
    # Pools user or a federated user (for example, a SAML or Facebook user). If
    # the user doesn't exist, an exception is thrown. This is the user that is
    # returned when the new user (with the linked identity provider attribute)
    # signs in.

    # For a native username + password user, the `ProviderAttributeValue` for the
    # `DestinationUser` should be the username in the user pool. For a federated
    # user, it should be the provider-specific `user_id`.

    # The `ProviderAttributeName` of the `DestinationUser` is ignored.

    # The `ProviderName` should be set to `Cognito` for users in Cognito user
    # pools.
    destination_user: "ProviderUserIdentifierType" = dataclasses.field(
        default_factory=dict,
    )

    # An external identity provider account for a user who does not currently
    # exist yet in the user pool. This user must be a federated user (for
    # example, a SAML or Facebook user), not another native user.

    # If the `SourceUser` is a federated social identity provider user (Facebook,
    # Google, or Login with Amazon), you must set the `ProviderAttributeName` to
    # `Cognito_Subject`. For social identity providers, the `ProviderName` will
    # be `Facebook`, `Google`, or `LoginWithAmazon`, and Cognito will
    # automatically parse the Facebook, Google, and Login with Amazon tokens for
    # `id`, `sub`, and `user_id`, respectively. The `ProviderAttributeValue` for
    # the user must be the same value as the `id`, `sub`, or `user_id` value
    # found in the social identity provider token.

    # For SAML, the `ProviderAttributeName` can be any value that matches a claim
    # in the SAML assertion. If you wish to link SAML users based on the subject
    # of the SAML assertion, you should map the subject to a claim through the
    # SAML identity provider and submit that claim name as the
    # `ProviderAttributeName`. If you set `ProviderAttributeName` to
    # `Cognito_Subject`, Cognito will automatically parse the default unique
    # identifier found in the subject from the SAML token.
    source_user: "ProviderUserIdentifierType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class AdminLinkProviderForUserResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AdminListDevicesRequest(autoboto.ShapeBase):
    """
    Represents the request to list devices, as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "pagination_token",
                "PaginationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The limit of the devices request.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The pagination token.
    pagination_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AdminListDevicesResponse(autoboto.ShapeBase):
    """
    Lists the device's response, as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "devices",
                "Devices",
                autoboto.TypeInfo(typing.List[DeviceType]),
            ),
            (
                "pagination_token",
                "PaginationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The devices in the list of devices response.
    devices: typing.List["DeviceType"] = dataclasses.field(
        default_factory=list,
    )

    # The pagination token.
    pagination_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AdminListGroupsForUserRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The username for the user.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The limit of the request to list groups.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AdminListGroupsForUserResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "groups",
                "Groups",
                autoboto.TypeInfo(typing.List[GroupType]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The groups that the user belongs to.
    groups: typing.List["GroupType"] = dataclasses.field(default_factory=list, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AdminListUserAuthEventsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
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

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user pool username or an alias.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of authentication events to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A pagination token.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AdminListUserAuthEventsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auth_events",
                "AuthEvents",
                autoboto.TypeInfo(typing.List[AuthEventType]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The response object. It includes the `EventID`, `EventType`,
    # `CreationDate`, `EventRisk`, and `EventResponse`.
    auth_events: typing.List["AuthEventType"] = dataclasses.field(
        default_factory=list,
    )

    # A pagination token.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AdminRemoveUserFromGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "group_name",
                "GroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The username for the user.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The group name.
    group_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AdminResetUserPasswordRequest(autoboto.ShapeBase):
    """
    Represents the request to reset a user's password as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool where you want to reset the user's
    # password.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name of the user whose password you wish to reset.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AdminResetUserPasswordResponse(autoboto.ShapeBase):
    """
    Represents the response from the server to reset a user password as an
    administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AdminRespondToAuthChallengeRequest(autoboto.ShapeBase):
    """
    The request to respond to the authentication challenge, as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "challenge_name",
                "ChallengeName",
                autoboto.TypeInfo(ChallengeNameType),
            ),
            (
                "challenge_responses",
                "ChallengeResponses",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "session",
                "Session",
                autoboto.TypeInfo(str),
            ),
            (
                "analytics_metadata",
                "AnalyticsMetadata",
                autoboto.TypeInfo(AnalyticsMetadataType),
            ),
            (
                "context_data",
                "ContextData",
                autoboto.TypeInfo(ContextDataType),
            ),
        ]

    # The ID of the Amazon Cognito user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The app client ID.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The challenge name. For more information, see .
    challenge_name: "ChallengeNameType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The challenge responses. These are inputs corresponding to the value of
    # `ChallengeName`, for example:

    #   * `SMS_MFA`: `SMS_MFA_CODE`, `USERNAME`, `SECRET_HASH` (if app client is configured with client secret).

    #   * `PASSWORD_VERIFIER`: `PASSWORD_CLAIM_SIGNATURE`, `PASSWORD_CLAIM_SECRET_BLOCK`, `TIMESTAMP`, `USERNAME`, `SECRET_HASH` (if app client is configured with client secret).

    #   * `ADMIN_NO_SRP_AUTH`: `PASSWORD`, `USERNAME`, `SECRET_HASH` (if app client is configured with client secret).

    #   * `NEW_PASSWORD_REQUIRED`: `NEW_PASSWORD`, any other required attributes, `USERNAME`, `SECRET_HASH` (if app client is configured with client secret).

    # The value of the `USERNAME` attribute must be the user's actual username,
    # not an alias (such as email address or phone number). To make this easier,
    # the `AdminInitiateAuth` response includes the actual username value in the
    # `USERNAMEUSER_ID_FOR_SRP` attribute, even if you specified an alias in your
    # call to `AdminInitiateAuth`.
    challenge_responses: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The session which should be passed both ways in challenge-response calls to
    # the service. If `InitiateAuth` or `RespondToAuthChallenge` API call
    # determines that the caller needs to go through another challenge, they
    # return a session with other challenge parameters. This session should be
    # passed as it is to the next `RespondToAuthChallenge` API call.
    session: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The analytics metadata for collecting Amazon Pinpoint metrics for
    # `AdminRespondToAuthChallenge` calls.
    analytics_metadata: "AnalyticsMetadataType" = dataclasses.field(
        default_factory=dict,
    )

    # Contextual data such as the user's device fingerprint, IP address, or
    # location used for evaluating the risk of an unexpected event by Amazon
    # Cognito advanced security.
    context_data: "ContextDataType" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class AdminRespondToAuthChallengeResponse(autoboto.ShapeBase):
    """
    Responds to the authentication challenge, as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "challenge_name",
                "ChallengeName",
                autoboto.TypeInfo(ChallengeNameType),
            ),
            (
                "session",
                "Session",
                autoboto.TypeInfo(str),
            ),
            (
                "challenge_parameters",
                "ChallengeParameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "authentication_result",
                "AuthenticationResult",
                autoboto.TypeInfo(AuthenticationResultType),
            ),
        ]

    # The name of the challenge. For more information, see .
    challenge_name: "ChallengeNameType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The session which should be passed both ways in challenge-response calls to
    # the service. If the or API call determines that the caller needs to go
    # through another challenge, they return a session with other challenge
    # parameters. This session should be passed as it is to the next
    # `RespondToAuthChallenge` API call.
    session: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The challenge parameters. For more information, see .
    challenge_parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The result returned by the server in response to the authentication
    # request.
    authentication_result: "AuthenticationResultType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class AdminSetUserMFAPreferenceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "sms_mfa_settings",
                "SMSMfaSettings",
                autoboto.TypeInfo(SMSMfaSettingsType),
            ),
            (
                "software_token_mfa_settings",
                "SoftwareTokenMfaSettings",
                autoboto.TypeInfo(SoftwareTokenMfaSettingsType),
            ),
        ]

    # The user pool username or alias.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The SMS text message MFA settings.
    sms_mfa_settings: "SMSMfaSettingsType" = dataclasses.field(
        default_factory=dict,
    )

    # The time-based one-time password software token MFA settings.
    software_token_mfa_settings: "SoftwareTokenMfaSettingsType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class AdminSetUserMFAPreferenceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AdminSetUserSettingsRequest(autoboto.ShapeBase):
    """
    Represents the request to set user settings as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "mfa_options",
                "MFAOptions",
                autoboto.TypeInfo(typing.List[MFAOptionType]),
            ),
        ]

    # The user pool ID for the user pool where you want to set the user's
    # settings, such as MFA options.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name of the user for whom you wish to set user settings.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the options for MFA (e.g., email or phone number).
    mfa_options: typing.List["MFAOptionType"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AdminSetUserSettingsResponse(autoboto.ShapeBase):
    """
    Represents the response from the server to set user settings as an
    administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AdminUpdateAuthEventFeedbackRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "event_id",
                "EventId",
                autoboto.TypeInfo(str),
            ),
            (
                "feedback_value",
                "FeedbackValue",
                autoboto.TypeInfo(FeedbackValueType),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user pool username.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The authentication event ID.
    event_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The authentication event feedback value.
    feedback_value: "FeedbackValueType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AdminUpdateAuthEventFeedbackResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AdminUpdateDeviceStatusRequest(autoboto.ShapeBase):
    """
    The request to update the device status, as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "device_key",
                "DeviceKey",
                autoboto.TypeInfo(str),
            ),
            (
                "device_remembered_status",
                "DeviceRememberedStatus",
                autoboto.TypeInfo(DeviceRememberedStatusType),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The device key.
    device_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status indicating whether a device has been remembered or not.
    device_remembered_status: "DeviceRememberedStatusType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AdminUpdateDeviceStatusResponse(autoboto.ShapeBase):
    """
    The status response from the request to update the device, as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AdminUpdateUserAttributesRequest(autoboto.ShapeBase):
    """
    Represents the request to update the user's attributes as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "user_attributes",
                "UserAttributes",
                autoboto.TypeInfo(typing.List[AttributeType]),
            ),
        ]

    # The user pool ID for the user pool where you want to update user
    # attributes.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name of the user for whom you want to update user attributes.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of name-value pairs representing user attributes.

    # For custom attributes, you must prepend the `custom:` prefix to the
    # attribute name.
    user_attributes: typing.List["AttributeType"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AdminUpdateUserAttributesResponse(autoboto.ShapeBase):
    """
    Represents the response from the server for the request to update user
    attributes as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AdminUserGlobalSignOutRequest(autoboto.ShapeBase):
    """
    The request to sign out of all devices, as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AdminUserGlobalSignOutResponse(autoboto.ShapeBase):
    """
    The global sign-out response, as an administrator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class AdvancedSecurityModeType(Enum):
    OFF = "OFF"
    AUDIT = "AUDIT"
    ENFORCED = "ENFORCED"


class AliasAttributeType(Enum):
    phone_number = "phone_number"
    email = "email"
    preferred_username = "preferred_username"


@dataclasses.dataclass
class AliasExistsException(autoboto.ShapeBase):
    """
    This exception is thrown when a user tries to confirm the account with an email
    or phone number that has already been supplied as an alias from a different
    account. This exception tells user that an account with this email or phone
    already exists.
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

    # The message sent to the user when an alias exists.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AnalyticsConfigurationType(autoboto.ShapeBase):
    """
    The Amazon Pinpoint analytics configuration for collecting metrics for a user
    pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "external_id",
                "ExternalId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_data_shared",
                "UserDataShared",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The application ID for an Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of an IAM role that authorizes Amazon Cognito to publish events to
    # Amazon Pinpoint analytics.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The external ID.
    external_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If `UserDataShared` is `true`, Amazon Cognito will include user data in the
    # events it publishes to Amazon Pinpoint analytics.
    user_data_shared: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AnalyticsMetadataType(autoboto.ShapeBase):
    """
    An Amazon Pinpoint analytics endpoint.

    An endpoint uniquely identifies a mobile device, email address, or phone number
    that can receive messages from Amazon Pinpoint analytics.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "analytics_endpoint_id",
                "AnalyticsEndpointId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The endpoint ID.
    analytics_endpoint_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AssociateSoftwareTokenRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
            (
                "session",
                "Session",
                autoboto.TypeInfo(str),
            ),
        ]

    # The access token.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The session which should be passed both ways in challenge-response calls to
    # the service. This allows authentication of the user as part of the MFA
    # setup process.
    session: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AssociateSoftwareTokenResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "secret_code",
                "SecretCode",
                autoboto.TypeInfo(str),
            ),
            (
                "session",
                "Session",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique generated shared secret code that is used in the TOTP algorithm to
    # generate a one time code.
    secret_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The session which should be passed both ways in challenge-response calls to
    # the service. This allows authentication of the user as part of the MFA
    # setup process.
    session: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class AttributeDataType(Enum):
    String = "String"
    Number = "Number"
    DateTime = "DateTime"
    Boolean = "Boolean"


@dataclasses.dataclass
class AttributeType(autoboto.ShapeBase):
    """
    Specifies whether the attribute is standard or custom.
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
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the attribute.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value of the attribute.
    value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AuthEventType(autoboto.ShapeBase):
    """
    The authentication event type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_id",
                "EventId",
                autoboto.TypeInfo(str),
            ),
            (
                "event_type",
                "EventType",
                autoboto.TypeInfo(EventType),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "event_response",
                "EventResponse",
                autoboto.TypeInfo(EventResponseType),
            ),
            (
                "event_risk",
                "EventRisk",
                autoboto.TypeInfo(EventRiskType),
            ),
            (
                "challenge_responses",
                "ChallengeResponses",
                autoboto.TypeInfo(typing.List[ChallengeResponseType]),
            ),
            (
                "event_context_data",
                "EventContextData",
                autoboto.TypeInfo(EventContextDataType),
            ),
            (
                "event_feedback",
                "EventFeedback",
                autoboto.TypeInfo(EventFeedbackType),
            ),
        ]

    # The event ID.
    event_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The event type.
    event_type: "EventType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The creation date
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The event response.
    event_response: "EventResponseType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The event risk.
    event_risk: "EventRiskType" = dataclasses.field(default_factory=dict, )

    # The challenge responses.
    challenge_responses: typing.List["ChallengeResponseType"
                                    ] = dataclasses.field(
                                        default_factory=list,
                                    )

    # The user context data captured at the time of an event request. It provides
    # additional information about the client from which event the request is
    # received.
    event_context_data: "EventContextDataType" = dataclasses.field(
        default_factory=dict,
    )

    # A flag specifying the user feedback captured at the time of an event
    # request is good or bad.
    event_feedback: "EventFeedbackType" = dataclasses.field(
        default_factory=dict,
    )


class AuthFlowType(Enum):
    USER_SRP_AUTH = "USER_SRP_AUTH"
    REFRESH_TOKEN_AUTH = "REFRESH_TOKEN_AUTH"
    REFRESH_TOKEN = "REFRESH_TOKEN"
    CUSTOM_AUTH = "CUSTOM_AUTH"
    ADMIN_NO_SRP_AUTH = "ADMIN_NO_SRP_AUTH"
    USER_PASSWORD_AUTH = "USER_PASSWORD_AUTH"


@dataclasses.dataclass
class AuthenticationResultType(autoboto.ShapeBase):
    """
    The authentication result.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
            (
                "expires_in",
                "ExpiresIn",
                autoboto.TypeInfo(int),
            ),
            (
                "token_type",
                "TokenType",
                autoboto.TypeInfo(str),
            ),
            (
                "refresh_token",
                "RefreshToken",
                autoboto.TypeInfo(str),
            ),
            (
                "id_token",
                "IdToken",
                autoboto.TypeInfo(str),
            ),
            (
                "new_device_metadata",
                "NewDeviceMetadata",
                autoboto.TypeInfo(NewDeviceMetadataType),
            ),
        ]

    # The access token.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The expiration period of the authentication result in seconds.
    expires_in: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token type.
    token_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The refresh token.
    refresh_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID token.
    id_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new device metadata from an authentication result.
    new_device_metadata: "NewDeviceMetadataType" = dataclasses.field(
        default_factory=dict,
    )


class ChallengeName(Enum):
    Password = "Password"
    Mfa = "Mfa"


class ChallengeNameType(Enum):
    SMS_MFA = "SMS_MFA"
    SOFTWARE_TOKEN_MFA = "SOFTWARE_TOKEN_MFA"
    SELECT_MFA_TYPE = "SELECT_MFA_TYPE"
    MFA_SETUP = "MFA_SETUP"
    PASSWORD_VERIFIER = "PASSWORD_VERIFIER"
    CUSTOM_CHALLENGE = "CUSTOM_CHALLENGE"
    DEVICE_SRP_AUTH = "DEVICE_SRP_AUTH"
    DEVICE_PASSWORD_VERIFIER = "DEVICE_PASSWORD_VERIFIER"
    ADMIN_NO_SRP_AUTH = "ADMIN_NO_SRP_AUTH"
    NEW_PASSWORD_REQUIRED = "NEW_PASSWORD_REQUIRED"


class ChallengeResponse(Enum):
    Success = "Success"
    Failure = "Failure"


@dataclasses.dataclass
class ChallengeResponseType(autoboto.ShapeBase):
    """
    The challenge response type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "challenge_name",
                "ChallengeName",
                autoboto.TypeInfo(ChallengeName),
            ),
            (
                "challenge_response",
                "ChallengeResponse",
                autoboto.TypeInfo(ChallengeResponse),
            ),
        ]

    # The challenge name
    challenge_name: "ChallengeName" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The challenge response.
    challenge_response: "ChallengeResponse" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ChangePasswordRequest(autoboto.ShapeBase):
    """
    Represents the request to change a user password.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "previous_password",
                "PreviousPassword",
                autoboto.TypeInfo(str),
            ),
            (
                "proposed_password",
                "ProposedPassword",
                autoboto.TypeInfo(str),
            ),
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The old password.
    previous_password: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The new password.
    proposed_password: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The access token.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ChangePasswordResponse(autoboto.ShapeBase):
    """
    The response from the server to the change password request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CodeDeliveryDetailsType(autoboto.ShapeBase):
    """
    The code delivery details being returned from the server.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination",
                "Destination",
                autoboto.TypeInfo(str),
            ),
            (
                "delivery_medium",
                "DeliveryMedium",
                autoboto.TypeInfo(DeliveryMediumType),
            ),
            (
                "attribute_name",
                "AttributeName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The destination for the code delivery details.
    destination: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The delivery medium (email message or phone number).
    delivery_medium: "DeliveryMediumType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The attribute name.
    attribute_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CodeDeliveryFailureException(autoboto.ShapeBase):
    """
    This exception is thrown when a verification code fails to deliver successfully.
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

    # The message sent when a verification code fails to deliver successfully.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CodeMismatchException(autoboto.ShapeBase):
    """
    This exception is thrown if the provided code does not match what the server was
    expecting.
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

    # The message provided when the code mismatch exception is thrown.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CompromisedCredentialsActionsType(autoboto.ShapeBase):
    """
    The compromised credentials actions type
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_action",
                "EventAction",
                autoboto.TypeInfo(CompromisedCredentialsEventActionType),
            ),
        ]

    # The event action.
    event_action: "CompromisedCredentialsEventActionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class CompromisedCredentialsEventActionType(Enum):
    BLOCK = "BLOCK"
    NO_ACTION = "NO_ACTION"


@dataclasses.dataclass
class CompromisedCredentialsRiskConfigurationType(autoboto.ShapeBase):
    """
    The compromised credentials risk configuration type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "actions",
                "Actions",
                autoboto.TypeInfo(CompromisedCredentialsActionsType),
            ),
            (
                "event_filter",
                "EventFilter",
                autoboto.TypeInfo(typing.List[EventFilterType]),
            ),
        ]

    # The compromised credentials risk configuration actions.
    actions: "CompromisedCredentialsActionsType" = dataclasses.field(
        default_factory=dict,
    )

    # Perform the action for these events. The default is to perform all events
    # if no event filter is specified.
    event_filter: typing.List["EventFilterType"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ConcurrentModificationException(autoboto.ShapeBase):
    """
    This exception is thrown if two or more modifications are happening
    concurrently.
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

    # The message provided when the concurrent exception is thrown.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ConfirmDeviceRequest(autoboto.ShapeBase):
    """
    Confirms the device request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
            (
                "device_key",
                "DeviceKey",
                autoboto.TypeInfo(str),
            ),
            (
                "device_secret_verifier_config",
                "DeviceSecretVerifierConfig",
                autoboto.TypeInfo(DeviceSecretVerifierConfigType),
            ),
            (
                "device_name",
                "DeviceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The access token.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The device key.
    device_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The configuration of the device secret verifier.
    device_secret_verifier_config: "DeviceSecretVerifierConfigType" = dataclasses.field(
        default_factory=dict,
    )

    # The device name.
    device_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ConfirmDeviceResponse(autoboto.ShapeBase):
    """
    Confirms the device response.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_confirmation_necessary",
                "UserConfirmationNecessary",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Indicates whether the user confirmation is necessary to confirm the device
    # response.
    user_confirmation_necessary: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ConfirmForgotPasswordRequest(autoboto.ShapeBase):
    """
    The request representing the confirmation for a password reset.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "confirmation_code",
                "ConfirmationCode",
                autoboto.TypeInfo(str),
            ),
            (
                "password",
                "Password",
                autoboto.TypeInfo(str),
            ),
            (
                "secret_hash",
                "SecretHash",
                autoboto.TypeInfo(str),
            ),
            (
                "analytics_metadata",
                "AnalyticsMetadata",
                autoboto.TypeInfo(AnalyticsMetadataType),
            ),
            (
                "user_context_data",
                "UserContextData",
                autoboto.TypeInfo(UserContextDataType),
            ),
        ]

    # The app client ID of the app associated with the user pool.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name of the user for whom you want to enter a code to retrieve a
    # forgotten password.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The confirmation code sent by a user's request to retrieve a forgotten
    # password. For more information, see
    confirmation_code: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The password sent by a user's request to retrieve a forgotten password.
    password: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A keyed-hash message authentication code (HMAC) calculated using the secret
    # key of a user pool client and username plus the client ID in the message.
    secret_hash: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Pinpoint analytics metadata for collecting metrics for
    # `ConfirmForgotPassword` calls.
    analytics_metadata: "AnalyticsMetadataType" = dataclasses.field(
        default_factory=dict,
    )

    # Contextual data such as the user's device fingerprint, IP address, or
    # location used for evaluating the risk of an unexpected event by Amazon
    # Cognito advanced security.
    user_context_data: "UserContextDataType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ConfirmForgotPasswordResponse(autoboto.ShapeBase):
    """
    The response from the server that results from a user's request to retrieve a
    forgotten password.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ConfirmSignUpRequest(autoboto.ShapeBase):
    """
    Represents the request to confirm registration of a user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "confirmation_code",
                "ConfirmationCode",
                autoboto.TypeInfo(str),
            ),
            (
                "secret_hash",
                "SecretHash",
                autoboto.TypeInfo(str),
            ),
            (
                "force_alias_creation",
                "ForceAliasCreation",
                autoboto.TypeInfo(bool),
            ),
            (
                "analytics_metadata",
                "AnalyticsMetadata",
                autoboto.TypeInfo(AnalyticsMetadataType),
            ),
            (
                "user_context_data",
                "UserContextData",
                autoboto.TypeInfo(UserContextDataType),
            ),
        ]

    # The ID of the app client associated with the user pool.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name of the user whose registration you wish to confirm.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The confirmation code sent by a user's request to confirm registration.
    confirmation_code: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A keyed-hash message authentication code (HMAC) calculated using the secret
    # key of a user pool client and username plus the client ID in the message.
    secret_hash: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Boolean to be specified to force user confirmation irrespective of existing
    # alias. By default set to `False`. If this parameter is set to `True` and
    # the phone number/email used for sign up confirmation already exists as an
    # alias with a different user, the API call will migrate the alias from the
    # previous user to the newly created user being confirmed. If set to `False`,
    # the API will throw an **AliasExistsException** error.
    force_alias_creation: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Pinpoint analytics metadata for collecting metrics for
    # `ConfirmSignUp` calls.
    analytics_metadata: "AnalyticsMetadataType" = dataclasses.field(
        default_factory=dict,
    )

    # Contextual data such as the user's device fingerprint, IP address, or
    # location used for evaluating the risk of an unexpected event by Amazon
    # Cognito advanced security.
    user_context_data: "UserContextDataType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ConfirmSignUpResponse(autoboto.ShapeBase):
    """
    Represents the response from the server for the registration confirmation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ContextDataType(autoboto.ShapeBase):
    """
    Contextual user data type used for evaluating the risk of an unexpected event by
    Amazon Cognito advanced security.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip_address",
                "IpAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "server_name",
                "ServerName",
                autoboto.TypeInfo(str),
            ),
            (
                "server_path",
                "ServerPath",
                autoboto.TypeInfo(str),
            ),
            (
                "http_headers",
                "HttpHeaders",
                autoboto.TypeInfo(typing.List[HttpHeader]),
            ),
            (
                "encoded_data",
                "EncodedData",
                autoboto.TypeInfo(str),
            ),
        ]

    # Source IP address of your user.
    ip_address: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Your server endpoint where this API is invoked.
    server_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Your server path where this API is invoked.
    server_path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # HttpHeaders received on your server in same order.
    http_headers: typing.List["HttpHeader"] = dataclasses.field(
        default_factory=list,
    )

    # Encoded data containing device fingerprinting details, collected using the
    # Amazon Cognito context data collection library.
    encoded_data: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "precedence",
                "Precedence",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the group. Must be unique.
    group_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A string containing the description of the group.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The role ARN for the group.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A nonnegative integer value that specifies the precedence of this group
    # relative to the other groups that a user can belong to in the user pool.
    # Zero is the highest precedence value. Groups with lower `Precedence` values
    # take precedence over groups with higher or null `Precedence` values. If a
    # user belongs to two or more groups, it is the group with the lowest
    # precedence value whose role ARN will be used in the `cognito:roles` and
    # `cognito:preferred_role` claims in the user's tokens.

    # Two groups can have the same `Precedence` value. If this happens, neither
    # group takes precedence over the other. If two groups with the same
    # `Precedence` have the same role ARN, that role is used in the
    # `cognito:preferred_role` claim in tokens for users in each group. If the
    # two groups have different role ARNs, the `cognito:preferred_role` claim is
    # not set in users' tokens.

    # The default `Precedence` value is null.
    precedence: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group",
                "Group",
                autoboto.TypeInfo(GroupType),
            ),
        ]

    # The group object for the group.
    group: "GroupType" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateIdentityProviderRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_name",
                "ProviderName",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_type",
                "ProviderType",
                autoboto.TypeInfo(IdentityProviderTypeType),
            ),
            (
                "provider_details",
                "ProviderDetails",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attribute_mapping",
                "AttributeMapping",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "idp_identifiers",
                "IdpIdentifiers",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identity provider name.
    provider_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The identity provider type.
    provider_type: "IdentityProviderTypeType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The identity provider details, such as `MetadataURL` and `MetadataFile`.
    provider_details: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A mapping of identity provider attributes to standard and custom user pool
    # attributes.
    attribute_mapping: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of identity provider identifiers.
    idp_identifiers: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateIdentityProviderResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_provider",
                "IdentityProvider",
                autoboto.TypeInfo(IdentityProviderType),
            ),
        ]

    # The newly created identity provider object.
    identity_provider: "IdentityProviderType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateResourceServerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "identifier",
                "Identifier",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "scopes",
                "Scopes",
                autoboto.TypeInfo(typing.List[ResourceServerScopeType]),
            ),
        ]

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A unique resource server identifier for the resource server. This could be
    # an HTTPS endpoint where the resource server is located. For example,
    # `https://my-weather-api.example.com`.
    identifier: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A friendly name for the resource server.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of scopes. Each scope is map, where the keys are `name` and
    # `description`.
    scopes: typing.List["ResourceServerScopeType"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateResourceServerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_server",
                "ResourceServer",
                autoboto.TypeInfo(ResourceServerType),
            ),
        ]

    # The newly created resource server.
    resource_server: "ResourceServerType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateUserImportJobRequest(autoboto.ShapeBase):
    """
    Represents the request to create the user import job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "cloud_watch_logs_role_arn",
                "CloudWatchLogsRoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The job name for the user import job.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user pool ID for the user pool that the users are being imported into.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The role ARN for the Amazon CloudWatch Logging role for the user import
    # job.
    cloud_watch_logs_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateUserImportJobResponse(autoboto.ShapeBase):
    """
    Represents the response from the server to the request to create the user import
    job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_import_job",
                "UserImportJob",
                autoboto.TypeInfo(UserImportJobType),
            ),
        ]

    # The job object that represents the user import job.
    user_import_job: "UserImportJobType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateUserPoolClientRequest(autoboto.ShapeBase):
    """
    Represents the request to create a user pool client.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_name",
                "ClientName",
                autoboto.TypeInfo(str),
            ),
            (
                "generate_secret",
                "GenerateSecret",
                autoboto.TypeInfo(bool),
            ),
            (
                "refresh_token_validity",
                "RefreshTokenValidity",
                autoboto.TypeInfo(int),
            ),
            (
                "read_attributes",
                "ReadAttributes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "write_attributes",
                "WriteAttributes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "explicit_auth_flows",
                "ExplicitAuthFlows",
                autoboto.TypeInfo(typing.List[ExplicitAuthFlowsType]),
            ),
            (
                "supported_identity_providers",
                "SupportedIdentityProviders",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "callback_urls",
                "CallbackURLs",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "logout_urls",
                "LogoutURLs",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "default_redirect_uri",
                "DefaultRedirectURI",
                autoboto.TypeInfo(str),
            ),
            (
                "allowed_o_auth_flows",
                "AllowedOAuthFlows",
                autoboto.TypeInfo(typing.List[OAuthFlowType]),
            ),
            (
                "allowed_o_auth_scopes",
                "AllowedOAuthScopes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "allowed_o_auth_flows_user_pool_client",
                "AllowedOAuthFlowsUserPoolClient",
                autoboto.TypeInfo(bool),
            ),
            (
                "analytics_configuration",
                "AnalyticsConfiguration",
                autoboto.TypeInfo(AnalyticsConfigurationType),
            ),
        ]

    # The user pool ID for the user pool where you want to create a user pool
    # client.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The client name for the user pool client you would like to create.
    client_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Boolean to specify whether you want to generate a secret for the user pool
    # client being created.
    generate_secret: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time limit, in days, after which the refresh token is no longer valid
    # and cannot be used.
    refresh_token_validity: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The read attributes.
    read_attributes: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The write attributes.
    write_attributes: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The explicit authentication flows.
    explicit_auth_flows: typing.List["ExplicitAuthFlowsType"
                                    ] = dataclasses.field(
                                        default_factory=list,
                                    )

    # A list of provider names for the identity providers that are supported on
    # this client.
    supported_identity_providers: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list of allowed redirect (callback) URLs for the identity providers.

    # A redirect URI must:

    #   * Be an absolute URI.

    #   * Be registered with the authorization server.

    #   * Not use HTTP without TLS (i.e. use HTTPS instead of HTTP).

    #   * Not include a fragment component.

    # See [OAuth 2.0 - Redirection
    # Endpoint](https://tools.ietf.org/html/rfc6749#section-3.1.2).
    callback_urls: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of allowed logout URLs for the identity providers.
    logout_urls: typing.List[str] = dataclasses.field(default_factory=list, )

    # The default redirect URI. Must be in the `CallbackURLs` list.

    # A redirect URI must:

    #   * Be an absolute URI.

    #   * Be registered with the authorization server.

    #   * Not use HTTP without TLS (i.e. use HTTPS instead of HTTP).

    #   * Not include a fragment component.

    # See [OAuth 2.0 - Redirection
    # Endpoint](https://tools.ietf.org/html/rfc6749#section-3.1.2).
    default_redirect_uri: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Set to `code` to initiate a code grant flow, which provides an
    # authorization code as the response. This code can be exchanged for access
    # tokens with the token endpoint.

    # Set to `token` to specify that the client should get the access token (and,
    # optionally, ID token, based on scopes) directly.
    allowed_o_auth_flows: typing.List["OAuthFlowType"] = dataclasses.field(
        default_factory=list,
    )

    # A list of allowed `OAuth` scopes. Currently supported values are `"phone"`,
    # `"email"`, `"openid"`, and `"Cognito"`.
    allowed_o_auth_scopes: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Set to `True` if the client is allowed to follow the OAuth protocol when
    # interacting with Cognito user pools.
    allowed_o_auth_flows_user_pool_client: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Pinpoint analytics configuration for collecting metrics for this
    # user pool.
    analytics_configuration: "AnalyticsConfigurationType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateUserPoolClientResponse(autoboto.ShapeBase):
    """
    Represents the response from the server to create a user pool client.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_client",
                "UserPoolClient",
                autoboto.TypeInfo(UserPoolClientType),
            ),
        ]

    # The user pool client that was just created.
    user_pool_client: "UserPoolClientType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateUserPoolDomainRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "Domain",
                autoboto.TypeInfo(str),
            ),
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The domain string.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateUserPoolDomainResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateUserPoolRequest(autoboto.ShapeBase):
    """
    Represents the request to create a user pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pool_name",
                "PoolName",
                autoboto.TypeInfo(str),
            ),
            (
                "policies",
                "Policies",
                autoboto.TypeInfo(UserPoolPolicyType),
            ),
            (
                "lambda_config",
                "LambdaConfig",
                autoboto.TypeInfo(LambdaConfigType),
            ),
            (
                "auto_verified_attributes",
                "AutoVerifiedAttributes",
                autoboto.TypeInfo(typing.List[VerifiedAttributeType]),
            ),
            (
                "alias_attributes",
                "AliasAttributes",
                autoboto.TypeInfo(typing.List[AliasAttributeType]),
            ),
            (
                "username_attributes",
                "UsernameAttributes",
                autoboto.TypeInfo(typing.List[UsernameAttributeType]),
            ),
            (
                "sms_verification_message",
                "SmsVerificationMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "email_verification_message",
                "EmailVerificationMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "email_verification_subject",
                "EmailVerificationSubject",
                autoboto.TypeInfo(str),
            ),
            (
                "verification_message_template",
                "VerificationMessageTemplate",
                autoboto.TypeInfo(VerificationMessageTemplateType),
            ),
            (
                "sms_authentication_message",
                "SmsAuthenticationMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "mfa_configuration",
                "MfaConfiguration",
                autoboto.TypeInfo(UserPoolMfaType),
            ),
            (
                "device_configuration",
                "DeviceConfiguration",
                autoboto.TypeInfo(DeviceConfigurationType),
            ),
            (
                "email_configuration",
                "EmailConfiguration",
                autoboto.TypeInfo(EmailConfigurationType),
            ),
            (
                "sms_configuration",
                "SmsConfiguration",
                autoboto.TypeInfo(SmsConfigurationType),
            ),
            (
                "user_pool_tags",
                "UserPoolTags",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "admin_create_user_config",
                "AdminCreateUserConfig",
                autoboto.TypeInfo(AdminCreateUserConfigType),
            ),
            (
                "schema",
                "Schema",
                autoboto.TypeInfo(typing.List[SchemaAttributeType]),
            ),
            (
                "user_pool_add_ons",
                "UserPoolAddOns",
                autoboto.TypeInfo(UserPoolAddOnsType),
            ),
        ]

    # A string used to name the user pool.
    pool_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The policies associated with the new user pool.
    policies: "UserPoolPolicyType" = dataclasses.field(default_factory=dict, )

    # The Lambda trigger configuration information for the new user pool.

    # In a push model, event sources (such as Amazon S3 and custom applications)
    # need permission to invoke a function. So you will need to make an extra
    # call to add permission for these event sources to invoke your Lambda
    # function.

    # For more information on using the Lambda API to add permission, see [
    # AddPermission
    # ](https://docs.aws.amazon.com/lambda/latest/dg/API_AddPermission.html).

    # For adding permission using the AWS CLI, see [ add-permission
    # ](https://docs.aws.amazon.com/cli/latest/reference/lambda/add-
    # permission.html).
    lambda_config: "LambdaConfigType" = dataclasses.field(
        default_factory=dict,
    )

    # The attributes to be auto-verified. Possible values: **email** ,
    # **phone_number**.
    auto_verified_attributes: typing.List["VerifiedAttributeType"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )

    # Attributes supported as an alias for this user pool. Possible values:
    # **phone_number** , **email** , or **preferred_username**.
    alias_attributes: typing.List["AliasAttributeType"] = dataclasses.field(
        default_factory=list,
    )

    # Specifies whether email addresses or phone numbers can be specified as
    # usernames when a user signs up.
    username_attributes: typing.List["UsernameAttributeType"
                                    ] = dataclasses.field(
                                        default_factory=list,
                                    )

    # A string representing the SMS verification message.
    sms_verification_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A string representing the email verification message.
    email_verification_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A string representing the email verification subject.
    email_verification_subject: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The template for the verification message that the user sees when the app
    # requests permission to access the user's information.
    verification_message_template: "VerificationMessageTemplateType" = dataclasses.field(
        default_factory=dict,
    )

    # A string representing the SMS authentication message.
    sms_authentication_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies MFA configuration details.
    mfa_configuration: "UserPoolMfaType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The device configuration.
    device_configuration: "DeviceConfigurationType" = dataclasses.field(
        default_factory=dict,
    )

    # The email configuration.
    email_configuration: "EmailConfigurationType" = dataclasses.field(
        default_factory=dict,
    )

    # The SMS configuration.
    sms_configuration: "SmsConfigurationType" = dataclasses.field(
        default_factory=dict,
    )

    # The cost allocation tags for the user pool. For more information, see
    # [Adding Cost Allocation Tags to Your User
    # Pool](http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-
    # user-pools-cost-allocation-tagging.html)
    user_pool_tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The configuration for `AdminCreateUser` requests.
    admin_create_user_config: "AdminCreateUserConfigType" = dataclasses.field(
        default_factory=dict,
    )

    # An array of schema attributes for the new user pool. These attributes can
    # be standard or custom attributes.
    schema: typing.List["SchemaAttributeType"] = dataclasses.field(
        default_factory=list,
    )

    # Used to enable advanced security risk detection. Set the key
    # `AdvancedSecurityMode` to the value "AUDIT".
    user_pool_add_ons: "UserPoolAddOnsType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateUserPoolResponse(autoboto.ShapeBase):
    """
    Represents the response from the server for the request to create a user pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool",
                "UserPool",
                autoboto.TypeInfo(UserPoolType),
            ),
        ]

    # A container for the user pool details.
    user_pool: "UserPoolType" = dataclasses.field(default_factory=dict, )


class DefaultEmailOptionType(Enum):
    CONFIRM_WITH_LINK = "CONFIRM_WITH_LINK"
    CONFIRM_WITH_CODE = "CONFIRM_WITH_CODE"


@dataclasses.dataclass
class DeleteGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the group.
    group_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteIdentityProviderRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_name",
                "ProviderName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identity provider name.
    provider_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteResourceServerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "identifier",
                "Identifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool that hosts the resource server.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identifier for the resource server.
    identifier: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteUserAttributesRequest(autoboto.ShapeBase):
    """
    Represents the request to delete user attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_attribute_names",
                "UserAttributeNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of strings representing the user attribute names you wish to
    # delete.

    # For custom attributes, you must prepend the `custom:` prefix to the
    # attribute name.
    user_attribute_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The access token used in the request to delete user attributes.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteUserAttributesResponse(autoboto.ShapeBase):
    """
    Represents the response from the server to delete user attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteUserPoolClientRequest(autoboto.ShapeBase):
    """
    Represents the request to delete a user pool client.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool where you want to delete the client.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The app client ID of the app associated with the user pool.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteUserPoolDomainRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "Domain",
                autoboto.TypeInfo(str),
            ),
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The domain string.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteUserPoolDomainResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteUserPoolRequest(autoboto.ShapeBase):
    """
    Represents the request to delete a user pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool you want to delete.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteUserRequest(autoboto.ShapeBase):
    """
    Represents the request to delete a user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The access token from a request to delete a user.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class DeliveryMediumType(Enum):
    SMS = "SMS"
    EMAIL = "EMAIL"


@dataclasses.dataclass
class DescribeIdentityProviderRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_name",
                "ProviderName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identity provider name.
    provider_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeIdentityProviderResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_provider",
                "IdentityProvider",
                autoboto.TypeInfo(IdentityProviderType),
            ),
        ]

    # The identity provider that was deleted.
    identity_provider: "IdentityProviderType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeResourceServerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "identifier",
                "Identifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool that hosts the resource server.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identifier for the resource server
    identifier: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeResourceServerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_server",
                "ResourceServer",
                autoboto.TypeInfo(ResourceServerType),
            ),
        ]

    # The resource server.
    resource_server: "ResourceServerType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeRiskConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The app client ID.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeRiskConfigurationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "risk_configuration",
                "RiskConfiguration",
                autoboto.TypeInfo(RiskConfigurationType),
            ),
        ]

    # The risk configuration.
    risk_configuration: "RiskConfigurationType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeUserImportJobRequest(autoboto.ShapeBase):
    """
    Represents the request to describe the user import job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "job_id",
                "JobId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool that the users are being imported into.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The job ID for the user import job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeUserImportJobResponse(autoboto.ShapeBase):
    """
    Represents the response from the server to the request to describe the user
    import job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_import_job",
                "UserImportJob",
                autoboto.TypeInfo(UserImportJobType),
            ),
        ]

    # The job object that represents the user import job.
    user_import_job: "UserImportJobType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeUserPoolClientRequest(autoboto.ShapeBase):
    """
    Represents the request to describe a user pool client.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool you want to describe.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The app client ID of the app associated with the user pool.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeUserPoolClientResponse(autoboto.ShapeBase):
    """
    Represents the response from the server from a request to describe the user pool
    client.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_client",
                "UserPoolClient",
                autoboto.TypeInfo(UserPoolClientType),
            ),
        ]

    # The user pool client from a server response to describe the user pool
    # client.
    user_pool_client: "UserPoolClientType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeUserPoolDomainRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "Domain",
                autoboto.TypeInfo(str),
            ),
        ]

    # The domain string.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeUserPoolDomainResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_description",
                "DomainDescription",
                autoboto.TypeInfo(DomainDescriptionType),
            ),
        ]

    # A domain description object containing information about the domain.
    domain_description: "DomainDescriptionType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeUserPoolRequest(autoboto.ShapeBase):
    """
    Represents the request to describe the user pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool you want to describe.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeUserPoolResponse(autoboto.ShapeBase):
    """
    Represents the response to describe the user pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool",
                "UserPool",
                autoboto.TypeInfo(UserPoolType),
            ),
        ]

    # The container of metadata returned by the server to describe the pool.
    user_pool: "UserPoolType" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeviceConfigurationType(autoboto.ShapeBase):
    """
    The configuration for the user pool's device tracking.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "challenge_required_on_new_device",
                "ChallengeRequiredOnNewDevice",
                autoboto.TypeInfo(bool),
            ),
            (
                "device_only_remembered_on_user_prompt",
                "DeviceOnlyRememberedOnUserPrompt",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Indicates whether a challenge is required on a new device. Only applicable
    # to a new device.
    challenge_required_on_new_device: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If true, a device is only remembered on user prompt.
    device_only_remembered_on_user_prompt: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class DeviceRememberedStatusType(Enum):
    remembered = "remembered"
    not_remembered = "not_remembered"


@dataclasses.dataclass
class DeviceSecretVerifierConfigType(autoboto.ShapeBase):
    """
    The device verifier against which it will be authenticated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "password_verifier",
                "PasswordVerifier",
                autoboto.TypeInfo(str),
            ),
            (
                "salt",
                "Salt",
                autoboto.TypeInfo(str),
            ),
        ]

    # The password verifier.
    password_verifier: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The salt.
    salt: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeviceType(autoboto.ShapeBase):
    """
    The device type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_key",
                "DeviceKey",
                autoboto.TypeInfo(str),
            ),
            (
                "device_attributes",
                "DeviceAttributes",
                autoboto.TypeInfo(typing.List[AttributeType]),
            ),
            (
                "device_create_date",
                "DeviceCreateDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "device_last_modified_date",
                "DeviceLastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "device_last_authenticated_date",
                "DeviceLastAuthenticatedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The device key.
    device_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The device attributes.
    device_attributes: typing.List["AttributeType"] = dataclasses.field(
        default_factory=list,
    )

    # The creation date of the device.
    device_create_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The last modified date of the device.
    device_last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date in which the device was last authenticated.
    device_last_authenticated_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DomainDescriptionType(autoboto.ShapeBase):
    """
    A container for information about a domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_account_id",
                "AWSAccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "domain",
                "Domain",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_bucket",
                "S3Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "cloud_front_distribution",
                "CloudFrontDistribution",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(DomainStatusType),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The AWS account ID for the user pool owner.
    aws_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The domain string.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The S3 bucket where the static files for this domain are stored.
    s3_bucket: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the CloudFront distribution.
    cloud_front_distribution: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The app version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The domain status.
    status: "DomainStatusType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class DomainStatusType(Enum):
    CREATING = "CREATING"
    DELETING = "DELETING"
    UPDATING = "UPDATING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"


@dataclasses.dataclass
class DuplicateProviderException(autoboto.ShapeBase):
    """
    This exception is thrown when the provider is already supported by the user
    pool.
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
class EmailConfigurationType(autoboto.ShapeBase):
    """
    The email configuration type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_arn",
                "SourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "reply_to_email_address",
                "ReplyToEmailAddress",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the email source.
    source_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The destination to which the receiver of the email should reply to.
    reply_to_email_address: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class EnableSoftwareTokenMFAException(autoboto.ShapeBase):
    """
    This exception is thrown when there is a code mismatch and the service fails to
    configure the software token TOTP multi-factor authentication (MFA).
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
class EventContextDataType(autoboto.ShapeBase):
    """
    Specifies the user context data captured at the time of an event request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip_address",
                "IpAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "device_name",
                "DeviceName",
                autoboto.TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                autoboto.TypeInfo(str),
            ),
            (
                "city",
                "City",
                autoboto.TypeInfo(str),
            ),
            (
                "country",
                "Country",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user's IP address.
    ip_address: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user's device name.
    device_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user's time zone.
    timezone: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user's city.
    city: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user's country.
    country: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EventFeedbackType(autoboto.ShapeBase):
    """
    Specifies the event feedback type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "feedback_value",
                "FeedbackValue",
                autoboto.TypeInfo(FeedbackValueType),
            ),
            (
                "provider",
                "Provider",
                autoboto.TypeInfo(str),
            ),
            (
                "feedback_date",
                "FeedbackDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The event feedback value.
    feedback_value: "FeedbackValueType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The provider.
    provider: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The event feedback date.
    feedback_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class EventFilterType(Enum):
    SIGN_IN = "SIGN_IN"
    PASSWORD_CHANGE = "PASSWORD_CHANGE"
    SIGN_UP = "SIGN_UP"


class EventResponseType(Enum):
    Success = "Success"
    Failure = "Failure"


@dataclasses.dataclass
class EventRiskType(autoboto.ShapeBase):
    """
    The event risk type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "risk_decision",
                "RiskDecision",
                autoboto.TypeInfo(RiskDecisionType),
            ),
            (
                "risk_level",
                "RiskLevel",
                autoboto.TypeInfo(RiskLevelType),
            ),
        ]

    # The risk decision.
    risk_decision: "RiskDecisionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The risk level.
    risk_level: "RiskLevelType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class EventType(Enum):
    SignIn = "SignIn"
    SignUp = "SignUp"
    ForgotPassword = "ForgotPassword"


@dataclasses.dataclass
class ExpiredCodeException(autoboto.ShapeBase):
    """
    This exception is thrown if a code has expired.
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

    # The message returned when the expired code exception is thrown.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class ExplicitAuthFlowsType(Enum):
    ADMIN_NO_SRP_AUTH = "ADMIN_NO_SRP_AUTH"
    CUSTOM_AUTH_FLOW_ONLY = "CUSTOM_AUTH_FLOW_ONLY"
    USER_PASSWORD_AUTH = "USER_PASSWORD_AUTH"


class FeedbackValueType(Enum):
    Valid = "Valid"
    Invalid = "Invalid"


@dataclasses.dataclass
class ForgetDeviceRequest(autoboto.ShapeBase):
    """
    Represents the request to forget the device.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_key",
                "DeviceKey",
                autoboto.TypeInfo(str),
            ),
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The device key.
    device_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The access token for the forgotten device request.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ForgotPasswordRequest(autoboto.ShapeBase):
    """
    Represents the request to reset a user's password.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "secret_hash",
                "SecretHash",
                autoboto.TypeInfo(str),
            ),
            (
                "user_context_data",
                "UserContextData",
                autoboto.TypeInfo(UserContextDataType),
            ),
            (
                "analytics_metadata",
                "AnalyticsMetadata",
                autoboto.TypeInfo(AnalyticsMetadataType),
            ),
        ]

    # The ID of the client associated with the user pool.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name of the user for whom you want to enter a code to reset a
    # forgotten password.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A keyed-hash message authentication code (HMAC) calculated using the secret
    # key of a user pool client and username plus the client ID in the message.
    secret_hash: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Contextual data such as the user's device fingerprint, IP address, or
    # location used for evaluating the risk of an unexpected event by Amazon
    # Cognito advanced security.
    user_context_data: "UserContextDataType" = dataclasses.field(
        default_factory=dict,
    )

    # The Amazon Pinpoint analytics metadata for collecting metrics for
    # `ForgotPassword` calls.
    analytics_metadata: "AnalyticsMetadataType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ForgotPasswordResponse(autoboto.ShapeBase):
    """
    Respresents the response from the server regarding the request to reset a
    password.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code_delivery_details",
                "CodeDeliveryDetails",
                autoboto.TypeInfo(CodeDeliveryDetailsType),
            ),
        ]

    # The code delivery details returned by the server in response to the request
    # to reset a password.
    code_delivery_details: "CodeDeliveryDetailsType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetCSVHeaderRequest(autoboto.ShapeBase):
    """
    Represents the request to get the header information for the .csv file for the
    user import job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool that the users are to be imported into.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCSVHeaderResponse(autoboto.ShapeBase):
    """
    Represents the response from the server to the request to get the header
    information for the .csv file for the user import job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "csv_header",
                "CSVHeader",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The user pool ID for the user pool that the users are to be imported into.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The header information for the .csv file for the user import job.
    csv_header: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class GetDeviceRequest(autoboto.ShapeBase):
    """
    Represents the request to get the device.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_key",
                "DeviceKey",
                autoboto.TypeInfo(str),
            ),
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The device key.
    device_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The access token.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDeviceResponse(autoboto.ShapeBase):
    """
    Gets the device response.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device",
                "Device",
                autoboto.TypeInfo(DeviceType),
            ),
        ]

    # The device.
    device: "DeviceType" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the group.
    group_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group",
                "Group",
                autoboto.TypeInfo(GroupType),
            ),
        ]

    # The group object for the group.
    group: "GroupType" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetIdentityProviderByIdentifierRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "idp_identifier",
                "IdpIdentifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identity provider ID.
    idp_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetIdentityProviderByIdentifierResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_provider",
                "IdentityProvider",
                autoboto.TypeInfo(IdentityProviderType),
            ),
        ]

    # The identity provider object.
    identity_provider: "IdentityProviderType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetSigningCertificateRequest(autoboto.ShapeBase):
    """
    Request to get a signing certificate from Cognito.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetSigningCertificateResponse(autoboto.ShapeBase):
    """
    Response from Cognito for a signing certificate request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate",
                "Certificate",
                autoboto.TypeInfo(str),
            ),
        ]

    # The signing certificate.
    certificate: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetUICustomizationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The client ID for the client app.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetUICustomizationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ui_customization",
                "UICustomization",
                autoboto.TypeInfo(UICustomizationType),
            ),
        ]

    # The UI customization information.
    ui_customization: "UICustomizationType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetUserAttributeVerificationCodeRequest(autoboto.ShapeBase):
    """
    Represents the request to get user attribute verification.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
            (
                "attribute_name",
                "AttributeName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The access token returned by the server response to get the user attribute
    # verification code.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The attribute name returned by the server response to get the user
    # attribute verification code.
    attribute_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetUserAttributeVerificationCodeResponse(autoboto.ShapeBase):
    """
    The verification code response returned by the server response to get the user
    attribute verification code.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code_delivery_details",
                "CodeDeliveryDetails",
                autoboto.TypeInfo(CodeDeliveryDetailsType),
            ),
        ]

    # The code delivery details returned by the server in response to the request
    # to get the user attribute verification code.
    code_delivery_details: "CodeDeliveryDetailsType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetUserPoolMfaConfigRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetUserPoolMfaConfigResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sms_mfa_configuration",
                "SmsMfaConfiguration",
                autoboto.TypeInfo(SmsMfaConfigType),
            ),
            (
                "software_token_mfa_configuration",
                "SoftwareTokenMfaConfiguration",
                autoboto.TypeInfo(SoftwareTokenMfaConfigType),
            ),
            (
                "mfa_configuration",
                "MfaConfiguration",
                autoboto.TypeInfo(UserPoolMfaType),
            ),
        ]

    # The SMS text message multi-factor (MFA) configuration.
    sms_mfa_configuration: "SmsMfaConfigType" = dataclasses.field(
        default_factory=dict,
    )

    # The software token multi-factor (MFA) configuration.
    software_token_mfa_configuration: "SoftwareTokenMfaConfigType" = dataclasses.field(
        default_factory=dict,
    )

    # The multi-factor (MFA) configuration.
    mfa_configuration: "UserPoolMfaType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetUserRequest(autoboto.ShapeBase):
    """
    Represents the request to get information about the user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The access token returned by the server response to get information about
    # the user.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetUserResponse(autoboto.ShapeBase):
    """
    Represents the response from the server from the request to get information
    about the user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "user_attributes",
                "UserAttributes",
                autoboto.TypeInfo(typing.List[AttributeType]),
            ),
            (
                "mfa_options",
                "MFAOptions",
                autoboto.TypeInfo(typing.List[MFAOptionType]),
            ),
            (
                "preferred_mfa_setting",
                "PreferredMfaSetting",
                autoboto.TypeInfo(str),
            ),
            (
                "user_mfa_setting_list",
                "UserMFASettingList",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The user name of the user you wish to retrieve from the get user request.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of name-value pairs representing user attributes.

    # For custom attributes, you must prepend the `custom:` prefix to the
    # attribute name.
    user_attributes: typing.List["AttributeType"] = dataclasses.field(
        default_factory=list,
    )

    # Specifies the options for MFA (e.g., email or phone number).
    mfa_options: typing.List["MFAOptionType"] = dataclasses.field(
        default_factory=list,
    )

    # The user's preferred MFA setting.
    preferred_mfa_setting: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The list of the user's MFA settings.
    user_mfa_setting_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GlobalSignOutRequest(autoboto.ShapeBase):
    """
    Represents the request to sign out all devices.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The access token.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GlobalSignOutResponse(autoboto.ShapeBase):
    """
    The response to the request to sign out all devices.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GroupExistsException(autoboto.ShapeBase):
    """
    This exception is thrown when Amazon Cognito encounters a group that already
    exists in the user pool.
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
class GroupType(autoboto.ShapeBase):
    """
    The group type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "precedence",
                "Precedence",
                autoboto.TypeInfo(int),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the group.
    group_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A string containing the description of the group.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The role ARN for the group.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A nonnegative integer value that specifies the precedence of this group
    # relative to the other groups that a user can belong to in the user pool. If
    # a user belongs to two or more groups, it is the group with the highest
    # precedence whose role ARN will be used in the `cognito:roles` and
    # `cognito:preferred_role` claims in the user's tokens. Groups with higher
    # `Precedence` values take precedence over groups with lower `Precedence`
    # values or with null `Precedence` values.

    # Two groups can have the same `Precedence` value. If this happens, neither
    # group takes precedence over the other. If two groups with the same
    # `Precedence` have the same role ARN, that role is used in the
    # `cognito:preferred_role` claim in tokens for users in each group. If the
    # two groups have different role ARNs, the `cognito:preferred_role` claim is
    # not set in users' tokens.

    # The default `Precedence` value is null.
    precedence: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date the group was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the group was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class HttpHeader(autoboto.ShapeBase):
    """
    The HTTP header.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "header_name",
                "headerName",
                autoboto.TypeInfo(str),
            ),
            (
                "header_value",
                "headerValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The header name
    header_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The header value.
    header_value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class IdentityProviderType(autoboto.ShapeBase):
    """
    A container for information about an identity provider.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_name",
                "ProviderName",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_type",
                "ProviderType",
                autoboto.TypeInfo(IdentityProviderTypeType),
            ),
            (
                "provider_details",
                "ProviderDetails",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attribute_mapping",
                "AttributeMapping",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "idp_identifiers",
                "IdpIdentifiers",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identity provider name.
    provider_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The identity provider type.
    provider_type: "IdentityProviderTypeType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The identity provider details, such as `MetadataURL` and `MetadataFile`.
    provider_details: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A mapping of identity provider attributes to standard and custom user pool
    # attributes.
    attribute_mapping: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of identity provider identifiers.
    idp_identifiers: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The date the identity provider was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the identity provider was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class IdentityProviderTypeType(Enum):
    SAML = "SAML"
    Facebook = "Facebook"
    Google = "Google"
    LoginWithAmazon = "LoginWithAmazon"
    OIDC = "OIDC"


class ImageFileType(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class InitiateAuthRequest(autoboto.ShapeBase):
    """
    Initiates the authentication request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auth_flow",
                "AuthFlow",
                autoboto.TypeInfo(AuthFlowType),
            ),
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "auth_parameters",
                "AuthParameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "client_metadata",
                "ClientMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "analytics_metadata",
                "AnalyticsMetadata",
                autoboto.TypeInfo(AnalyticsMetadataType),
            ),
            (
                "user_context_data",
                "UserContextData",
                autoboto.TypeInfo(UserContextDataType),
            ),
        ]

    # The authentication flow for this call to execute. The API action will
    # depend on this value. For example:

    #   * `REFRESH_TOKEN_AUTH` will take in a valid refresh token and return new tokens.

    #   * `USER_SRP_AUTH` will take in `USERNAME` and `SRP_A` and return the SRP variables to be used for next challenge execution.

    #   * `USER_PASSWORD_AUTH` will take in `USERNAME` and `PASSWORD` and return the next challenge or tokens.

    # Valid values include:

    #   * `USER_SRP_AUTH`: Authentication flow for the Secure Remote Password (SRP) protocol.

    #   * `REFRESH_TOKEN_AUTH`/`REFRESH_TOKEN`: Authentication flow for refreshing the access token and ID token by supplying a valid refresh token.

    #   * `CUSTOM_AUTH`: Custom authentication flow.

    #   * `USER_PASSWORD_AUTH`: Non-SRP authentication flow; USERNAME and PASSWORD are passed directly. If a user migration Lambda trigger is set, this flow will invoke the user migration Lambda if the USERNAME is not found in the user pool.

    # `ADMIN_NO_SRP_AUTH` is not a valid value.
    auth_flow: "AuthFlowType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The app client ID.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The authentication parameters. These are inputs corresponding to the
    # `AuthFlow` that you are invoking. The required values depend on the value
    # of `AuthFlow`:

    #   * For `USER_SRP_AUTH`: `USERNAME` (required), `SRP_A` (required), `SECRET_HASH` (required if the app client is configured with a client secret), `DEVICE_KEY`

    #   * For `REFRESH_TOKEN_AUTH/REFRESH_TOKEN`: `REFRESH_TOKEN` (required), `SECRET_HASH` (required if the app client is configured with a client secret), `DEVICE_KEY`

    #   * For `CUSTOM_AUTH`: `USERNAME` (required), `SECRET_HASH` (if app client is configured with client secret), `DEVICE_KEY`
    auth_parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # This is a random key-value pair map which can contain any key and will be
    # passed to your PreAuthentication Lambda trigger as-is. It can be used to
    # implement additional validations around authentication.
    client_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Pinpoint analytics metadata for collecting metrics for
    # `InitiateAuth` calls.
    analytics_metadata: "AnalyticsMetadataType" = dataclasses.field(
        default_factory=dict,
    )

    # Contextual data such as the user's device fingerprint, IP address, or
    # location used for evaluating the risk of an unexpected event by Amazon
    # Cognito advanced security.
    user_context_data: "UserContextDataType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class InitiateAuthResponse(autoboto.ShapeBase):
    """
    Initiates the authentication response.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "challenge_name",
                "ChallengeName",
                autoboto.TypeInfo(ChallengeNameType),
            ),
            (
                "session",
                "Session",
                autoboto.TypeInfo(str),
            ),
            (
                "challenge_parameters",
                "ChallengeParameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "authentication_result",
                "AuthenticationResult",
                autoboto.TypeInfo(AuthenticationResultType),
            ),
        ]

    # The name of the challenge which you are responding to with this call. This
    # is returned to you in the `AdminInitiateAuth` response if you need to pass
    # another challenge.

    # Valid values include the following. Note that all of these challenges
    # require `USERNAME` and `SECRET_HASH` (if applicable) in the parameters.

    #   * `SMS_MFA`: Next challenge is to supply an `SMS_MFA_CODE`, delivered via SMS.

    #   * `PASSWORD_VERIFIER`: Next challenge is to supply `PASSWORD_CLAIM_SIGNATURE`, `PASSWORD_CLAIM_SECRET_BLOCK`, and `TIMESTAMP` after the client-side SRP calculations.

    #   * `CUSTOM_CHALLENGE`: This is returned if your custom authentication flow determines that the user should pass another challenge before tokens are issued.

    #   * `DEVICE_SRP_AUTH`: If device tracking was enabled on your user pool and the previous challenges were passed, this challenge is returned so that Amazon Cognito can start tracking this device.

    #   * `DEVICE_PASSWORD_VERIFIER`: Similar to `PASSWORD_VERIFIER`, but for devices only.

    #   * `NEW_PASSWORD_REQUIRED`: For users which are required to change their passwords after successful first login. This challenge should be passed with `NEW_PASSWORD` and any other required attributes.
    challenge_name: "ChallengeNameType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The session which should be passed both ways in challenge-response calls to
    # the service. If the or API call determines that the caller needs to go
    # through another challenge, they return a session with other challenge
    # parameters. This session should be passed as it is to the next
    # `RespondToAuthChallenge` API call.
    session: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The challenge parameters. These are returned to you in the `InitiateAuth`
    # response if you need to pass another challenge. The responses in this
    # parameter should be used to compute inputs to the next call
    # (`RespondToAuthChallenge`).

    # All challenges require `USERNAME` and `SECRET_HASH` (if applicable).
    challenge_parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The result of the authentication response. This is only returned if the
    # caller does not need to pass another challenge. If the caller does need to
    # pass another challenge before it gets tokens, `ChallengeName`,
    # `ChallengeParameters`, and `Session` are returned.
    authentication_result: "AuthenticationResultType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class InternalErrorException(autoboto.ShapeBase):
    """
    This exception is thrown when Amazon Cognito encounters an internal error.
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

    # The message returned when Amazon Cognito throws an internal error
    # exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidEmailRoleAccessPolicyException(autoboto.ShapeBase):
    """
    This exception is thrown when Amazon Cognito is not allowed to use your email
    identity. HTTP status code: 400.
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

    # The message returned when you have an unverified email address or the
    # identity policy is not set on an email address that Amazon Cognito can
    # access.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidLambdaResponseException(autoboto.ShapeBase):
    """
    This exception is thrown when the Amazon Cognito service encounters an invalid
    AWS Lambda response.
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

    # The message returned when the Amazon Cognito service throws an invalid AWS
    # Lambda response exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidOAuthFlowException(autoboto.ShapeBase):
    """
    This exception is thrown when the specified OAuth flow is invalid.
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
class InvalidParameterException(autoboto.ShapeBase):
    """
    This exception is thrown when the Amazon Cognito service encounters an invalid
    parameter.
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

    # The message returned when the Amazon Cognito service throws an invalid
    # parameter exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidPasswordException(autoboto.ShapeBase):
    """
    This exception is thrown when the Amazon Cognito service encounters an invalid
    password.
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

    # The message returned when the Amazon Cognito service throws an invalid user
    # password exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidSmsRoleAccessPolicyException(autoboto.ShapeBase):
    """
    This exception is returned when the role provided for SMS configuration does not
    have permission to publish using Amazon SNS.
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

    # The message retuned when the invalid SMS role access policy exception is
    # thrown.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidSmsRoleTrustRelationshipException(autoboto.ShapeBase):
    """
    This exception is thrown when the trust relationship is invalid for the role
    provided for SMS configuration. This can happen if you do not trust **cognito-
    idp.amazonaws.com** or the external ID provided in the role does not match what
    is provided in the SMS configuration for the user pool.
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

    # The message returned when the role trust relationship for the SMS message
    # is invalid.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidUserPoolConfigurationException(autoboto.ShapeBase):
    """
    This exception is thrown when the user pool configuration is invalid.
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

    # The message returned when the user pool configuration is invalid.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LambdaConfigType(autoboto.ShapeBase):
    """
    Specifies the configuration for AWS Lambda triggers.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pre_sign_up",
                "PreSignUp",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_message",
                "CustomMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "post_confirmation",
                "PostConfirmation",
                autoboto.TypeInfo(str),
            ),
            (
                "pre_authentication",
                "PreAuthentication",
                autoboto.TypeInfo(str),
            ),
            (
                "post_authentication",
                "PostAuthentication",
                autoboto.TypeInfo(str),
            ),
            (
                "define_auth_challenge",
                "DefineAuthChallenge",
                autoboto.TypeInfo(str),
            ),
            (
                "create_auth_challenge",
                "CreateAuthChallenge",
                autoboto.TypeInfo(str),
            ),
            (
                "verify_auth_challenge_response",
                "VerifyAuthChallengeResponse",
                autoboto.TypeInfo(str),
            ),
            (
                "pre_token_generation",
                "PreTokenGeneration",
                autoboto.TypeInfo(str),
            ),
            (
                "user_migration",
                "UserMigration",
                autoboto.TypeInfo(str),
            ),
        ]

    # A pre-registration AWS Lambda trigger.
    pre_sign_up: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A custom Message AWS Lambda trigger.
    custom_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A post-confirmation AWS Lambda trigger.
    post_confirmation: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A pre-authentication AWS Lambda trigger.
    pre_authentication: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A post-authentication AWS Lambda trigger.
    post_authentication: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Defines the authentication challenge.
    define_auth_challenge: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Creates an authentication challenge.
    create_auth_challenge: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Verifies the authentication challenge response.
    verify_auth_challenge_response: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A Lambda trigger that is invoked before token generation.
    pre_token_generation: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The user migration Lambda config type.
    user_migration: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    This exception is thrown when a user exceeds the limit for a requested AWS
    resource.
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

    # The message returned when Amazon Cognito throws a limit exceeded exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListDevicesRequest(autoboto.ShapeBase):
    """
    Represents the request to list the devices.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "pagination_token",
                "PaginationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The access tokens for the request to list devices.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The limit of the device request.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The pagination token for the list request.
    pagination_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListDevicesResponse(autoboto.ShapeBase):
    """
    Represents the response to list devices.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "devices",
                "Devices",
                autoboto.TypeInfo(typing.List[DeviceType]),
            ),
            (
                "pagination_token",
                "PaginationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The devices returned in the list devices response.
    devices: typing.List["DeviceType"] = dataclasses.field(
        default_factory=list,
    )

    # The pagination token for the list device response.
    pagination_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListGroupsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The limit of the request to list groups.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListGroupsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "groups",
                "Groups",
                autoboto.TypeInfo(typing.List[GroupType]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The group objects for the groups.
    groups: typing.List["GroupType"] = dataclasses.field(default_factory=list, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListIdentityProvidersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
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

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of identity providers to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A pagination token.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListIdentityProvidersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "providers",
                "Providers",
                autoboto.TypeInfo(typing.List[ProviderDescription]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of identity provider objects.
    providers: typing.List["ProviderDescription"] = dataclasses.field(
        default_factory=list,
    )

    # A pagination token.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListResourceServersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
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

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of resource servers to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A pagination token.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListResourceServersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_servers",
                "ResourceServers",
                autoboto.TypeInfo(typing.List[ResourceServerType]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The resource servers.
    resource_servers: typing.List["ResourceServerType"] = dataclasses.field(
        default_factory=list,
    )

    # A pagination token.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListUserImportJobsRequest(autoboto.ShapeBase):
    """
    Represents the request to list the user import jobs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "pagination_token",
                "PaginationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool that the users are being imported into.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of import jobs you want the request to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An identifier that was returned from the previous call to
    # `ListUserImportJobs`, which can be used to return the next set of import
    # jobs in the list.
    pagination_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListUserImportJobsResponse(autoboto.ShapeBase):
    """
    Represents the response from the server to the request to list the user import
    jobs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_import_jobs",
                "UserImportJobs",
                autoboto.TypeInfo(typing.List[UserImportJobType]),
            ),
            (
                "pagination_token",
                "PaginationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user import jobs.
    user_import_jobs: typing.List["UserImportJobType"] = dataclasses.field(
        default_factory=list,
    )

    # An identifier that can be used to return the next set of user import jobs
    # in the list.
    pagination_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListUserPoolClientsRequest(autoboto.ShapeBase):
    """
    Represents the request to list the user pool clients.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
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

    # The user pool ID for the user pool where you want to list user pool
    # clients.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results you want the request to return when listing
    # the user pool clients.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListUserPoolClientsResponse(autoboto.ShapeBase):
    """
    Represents the response from the server that lists user pool clients.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_clients",
                "UserPoolClients",
                autoboto.TypeInfo(typing.List[UserPoolClientDescription]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool clients in the response that lists user pool clients.
    user_pool_clients: typing.List["UserPoolClientDescription"
                                  ] = dataclasses.field(
                                      default_factory=list,
                                  )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListUserPoolsRequest(autoboto.ShapeBase):
    """
    Represents the request to list user pools.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # The maximum number of results you want the request to return when listing
    # the user pools.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListUserPoolsResponse(autoboto.ShapeBase):
    """
    Represents the response to list user pools.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pools",
                "UserPools",
                autoboto.TypeInfo(typing.List[UserPoolDescriptionType]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pools from the response to list users.
    user_pools: typing.List["UserPoolDescriptionType"] = dataclasses.field(
        default_factory=list,
    )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListUsersInGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "group_name",
                "GroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the group.
    group_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The limit of the request to list users.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListUsersInGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "users",
                "Users",
                autoboto.TypeInfo(typing.List[UserType]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The users returned in the request to list users.
    users: typing.List["UserType"] = dataclasses.field(default_factory=list, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListUsersRequest(autoboto.ShapeBase):
    """
    Represents the request to list users.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes_to_get",
                "AttributesToGet",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "pagination_token",
                "PaginationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "filter",
                "Filter",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool on which the search should be performed.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of strings, where each string is the name of a user attribute to
    # be returned for each user in the search results. If the array is null, all
    # attributes are returned.
    attributes_to_get: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Maximum number of users to be returned.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    pagination_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A filter string of the form " _AttributeName_ _Filter-Type_ "
    # _AttributeValue_ "". Quotation marks within the filter string must be
    # escaped using the backslash (\\) character. For example, "`family_name` =
    # \"Reddy\"".

    #   * _AttributeName_ : The name of the attribute to search for. You can only search for one attribute at a time.

    #   * _Filter-Type_ : For an exact match, use =, for example, "`given_name` = \"Jon\"". For a prefix ("starts with") match, use ^=, for example, "`given_name` ^= \"Jon\"".

    #   * _AttributeValue_ : The attribute value that must be matched for each user.

    # If the filter string is empty, `ListUsers` returns all users in the user
    # pool.

    # You can only search for the following standard attributes:

    #   * `username` (case-sensitive)

    #   * `email`

    #   * `phone_number`

    #   * `name`

    #   * `given_name`

    #   * `family_name`

    #   * `preferred_username`

    #   * `cognito:user_status` (called **Enabled** in the Console) (case-sensitive)

    #   * `status` (case-insensitive)

    #   * `sub`

    # Custom attributes are not searchable.

    # For more information, see [Searching for Users Using the ListUsers
    # API](http://docs.aws.amazon.com/cognito/latest/developerguide/how-to-
    # manage-user-accounts.html#cognito-user-pools-searching-for-users-using-
    # listusers-api) and [Examples of Using the ListUsers
    # API](http://docs.aws.amazon.com/cognito/latest/developerguide/how-to-
    # manage-user-accounts.html#cognito-user-pools-searching-for-users-listusers-
    # api-examples) in the _Amazon Cognito Developer Guide_.
    filter: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListUsersResponse(autoboto.ShapeBase):
    """
    The response from the request to list users.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "users",
                "Users",
                autoboto.TypeInfo(typing.List[UserType]),
            ),
            (
                "pagination_token",
                "PaginationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The users returned in the request to list users.
    users: typing.List["UserType"] = dataclasses.field(default_factory=list, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    pagination_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class MFAMethodNotFoundException(autoboto.ShapeBase):
    """
    This exception is thrown when Amazon Cognito cannot find a multi-factor
    authentication (MFA) method.
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

    # The message returned when Amazon Cognito throws an MFA method not found
    # exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class MFAOptionType(autoboto.ShapeBase):
    """
    Specifies the different settings for multi-factor authentication (MFA).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_medium",
                "DeliveryMedium",
                autoboto.TypeInfo(DeliveryMediumType),
            ),
            (
                "attribute_name",
                "AttributeName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The delivery medium (email message or SMS message) to send the MFA code.
    delivery_medium: "DeliveryMediumType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The attribute name of the MFA option type.
    attribute_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class MessageActionType(Enum):
    RESEND = "RESEND"
    SUPPRESS = "SUPPRESS"


@dataclasses.dataclass
class MessageTemplateType(autoboto.ShapeBase):
    """
    The message template structure.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sms_message",
                "SMSMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "email_message",
                "EmailMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "email_subject",
                "EmailSubject",
                autoboto.TypeInfo(str),
            ),
        ]

    # The message template for SMS messages.
    sms_message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message template for email messages.
    email_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The subject line for email messages.
    email_subject: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class NewDeviceMetadataType(autoboto.ShapeBase):
    """
    The new device metadata type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_key",
                "DeviceKey",
                autoboto.TypeInfo(str),
            ),
            (
                "device_group_key",
                "DeviceGroupKey",
                autoboto.TypeInfo(str),
            ),
        ]

    # The device key.
    device_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The device group key.
    device_group_key: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class NotAuthorizedException(autoboto.ShapeBase):
    """
    This exception is thrown when a user is not authorized.
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

    # The message returned when the Amazon Cognito service returns a not
    # authorized exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class NotifyConfigurationType(autoboto.ShapeBase):
    """
    The notify configuration type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_arn",
                "SourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "from_",
                "From",
                autoboto.TypeInfo(str),
            ),
            (
                "reply_to",
                "ReplyTo",
                autoboto.TypeInfo(str),
            ),
            (
                "block_email",
                "BlockEmail",
                autoboto.TypeInfo(NotifyEmailType),
            ),
            (
                "no_action_email",
                "NoActionEmail",
                autoboto.TypeInfo(NotifyEmailType),
            ),
            (
                "mfa_email",
                "MfaEmail",
                autoboto.TypeInfo(NotifyEmailType),
            ),
        ]

    # The Amazon Resource Name (ARN) of the identity that is associated with the
    # sending authorization policy. It permits Amazon Cognito to send for the
    # email address specified in the `From` parameter.
    source_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The email address that is sending the email. It must be either individually
    # verified with Amazon SES, or from a domain that has been verified with
    # Amazon SES.
    from_: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The destination to which the receiver of an email should reply to.
    reply_to: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Email template used when a detected risk event is blocked.
    block_email: "NotifyEmailType" = dataclasses.field(default_factory=dict, )

    # The email template used when a detected risk event is allowed.
    no_action_email: "NotifyEmailType" = dataclasses.field(
        default_factory=dict,
    )

    # The MFA email template used when MFA is challenged as part of a detected
    # risk.
    mfa_email: "NotifyEmailType" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class NotifyEmailType(autoboto.ShapeBase):
    """
    The notify email type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subject",
                "Subject",
                autoboto.TypeInfo(str),
            ),
            (
                "html_body",
                "HtmlBody",
                autoboto.TypeInfo(str),
            ),
            (
                "text_body",
                "TextBody",
                autoboto.TypeInfo(str),
            ),
        ]

    # The subject.
    subject: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The HTML body.
    html_body: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The text body.
    text_body: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class NumberAttributeConstraintsType(autoboto.ShapeBase):
    """
    The minimum and maximum value of an attribute that is of the number data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "min_value",
                "MinValue",
                autoboto.TypeInfo(str),
            ),
            (
                "max_value",
                "MaxValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The minimum value of an attribute that is of the number data type.
    min_value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum value of an attribute that is of the number data type.
    max_value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class OAuthFlowType(Enum):
    code = "code"
    implicit = "implicit"
    client_credentials = "client_credentials"


@dataclasses.dataclass
class PasswordPolicyType(autoboto.ShapeBase):
    """
    The password policy type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "minimum_length",
                "MinimumLength",
                autoboto.TypeInfo(int),
            ),
            (
                "require_uppercase",
                "RequireUppercase",
                autoboto.TypeInfo(bool),
            ),
            (
                "require_lowercase",
                "RequireLowercase",
                autoboto.TypeInfo(bool),
            ),
            (
                "require_numbers",
                "RequireNumbers",
                autoboto.TypeInfo(bool),
            ),
            (
                "require_symbols",
                "RequireSymbols",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The minimum length of the password policy that you have set. Cannot be less
    # than 6.
    minimum_length: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # In the password policy that you have set, refers to whether you have
    # required users to use at least one uppercase letter in their password.
    require_uppercase: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # In the password policy that you have set, refers to whether you have
    # required users to use at least one lowercase letter in their password.
    require_lowercase: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # In the password policy that you have set, refers to whether you have
    # required users to use at least one number in their password.
    require_numbers: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # In the password policy that you have set, refers to whether you have
    # required users to use at least one symbol in their password.
    require_symbols: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PasswordResetRequiredException(autoboto.ShapeBase):
    """
    This exception is thrown when a password reset is required.
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

    # The message returned when a password reset is required.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PreconditionNotMetException(autoboto.ShapeBase):
    """
    This exception is thrown when a precondition is not met.
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

    # The message returned when a precondition is not met.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ProviderDescription(autoboto.ShapeBase):
    """
    A container for identity provider details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "provider_name",
                "ProviderName",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_type",
                "ProviderType",
                autoboto.TypeInfo(IdentityProviderTypeType),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The identity provider name.
    provider_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The identity provider type.
    provider_type: "IdentityProviderTypeType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the provider was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the provider was added to the user pool.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ProviderUserIdentifierType(autoboto.ShapeBase):
    """
    A container for information about an identity provider for a user pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "provider_name",
                "ProviderName",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_attribute_name",
                "ProviderAttributeName",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_attribute_value",
                "ProviderAttributeValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the provider, for example, Facebook, Google, or Login with
    # Amazon.
    provider_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the provider attribute to link to, for example, `NameID`.
    provider_attribute_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value of the provider attribute to link to, for example,
    # `xxxxx_account`.
    provider_attribute_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ResendConfirmationCodeRequest(autoboto.ShapeBase):
    """
    Represents the request to resend the confirmation code.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "secret_hash",
                "SecretHash",
                autoboto.TypeInfo(str),
            ),
            (
                "user_context_data",
                "UserContextData",
                autoboto.TypeInfo(UserContextDataType),
            ),
            (
                "analytics_metadata",
                "AnalyticsMetadata",
                autoboto.TypeInfo(AnalyticsMetadataType),
            ),
        ]

    # The ID of the client associated with the user pool.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name of the user to whom you wish to resend a confirmation code.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A keyed-hash message authentication code (HMAC) calculated using the secret
    # key of a user pool client and username plus the client ID in the message.
    secret_hash: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Contextual data such as the user's device fingerprint, IP address, or
    # location used for evaluating the risk of an unexpected event by Amazon
    # Cognito advanced security.
    user_context_data: "UserContextDataType" = dataclasses.field(
        default_factory=dict,
    )

    # The Amazon Pinpoint analytics metadata for collecting metrics for
    # `ResendConfirmationCode` calls.
    analytics_metadata: "AnalyticsMetadataType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ResendConfirmationCodeResponse(autoboto.ShapeBase):
    """
    The response from the server when the Amazon Cognito Your User Pools service
    makes the request to resend a confirmation code.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code_delivery_details",
                "CodeDeliveryDetails",
                autoboto.TypeInfo(CodeDeliveryDetailsType),
            ),
        ]

    # The code delivery details returned by the server in response to the request
    # to resend the confirmation code.
    code_delivery_details: "CodeDeliveryDetailsType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    This exception is thrown when the Amazon Cognito service cannot find the
    requested resource.
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

    # The message returned when the Amazon Cognito service returns a resource not
    # found exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ResourceServerScopeType(autoboto.ShapeBase):
    """
    A resource server scope.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scope_name",
                "ScopeName",
                autoboto.TypeInfo(str),
            ),
            (
                "scope_description",
                "ScopeDescription",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the scope.
    scope_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A description of the scope.
    scope_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ResourceServerType(autoboto.ShapeBase):
    """
    A container for information about a resource server for a user pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "identifier",
                "Identifier",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "scopes",
                "Scopes",
                autoboto.TypeInfo(typing.List[ResourceServerScopeType]),
            ),
        ]

    # The user pool ID for the user pool that hosts the resource server.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identifier for the resource server.
    identifier: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the resource server.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of scopes that are defined for the resource server.
    scopes: typing.List["ResourceServerScopeType"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class RespondToAuthChallengeRequest(autoboto.ShapeBase):
    """
    The request to respond to an authentication challenge.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "challenge_name",
                "ChallengeName",
                autoboto.TypeInfo(ChallengeNameType),
            ),
            (
                "session",
                "Session",
                autoboto.TypeInfo(str),
            ),
            (
                "challenge_responses",
                "ChallengeResponses",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "analytics_metadata",
                "AnalyticsMetadata",
                autoboto.TypeInfo(AnalyticsMetadataType),
            ),
            (
                "user_context_data",
                "UserContextData",
                autoboto.TypeInfo(UserContextDataType),
            ),
        ]

    # The app client ID.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The challenge name. For more information, see .

    # `ADMIN_NO_SRP_AUTH` is not a valid value.
    challenge_name: "ChallengeNameType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The session which should be passed both ways in challenge-response calls to
    # the service. If `InitiateAuth` or `RespondToAuthChallenge` API call
    # determines that the caller needs to go through another challenge, they
    # return a session with other challenge parameters. This session should be
    # passed as it is to the next `RespondToAuthChallenge` API call.
    session: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The challenge responses. These are inputs corresponding to the value of
    # `ChallengeName`, for example:

    #   * `SMS_MFA`: `SMS_MFA_CODE`, `USERNAME`, `SECRET_HASH` (if app client is configured with client secret).

    #   * `PASSWORD_VERIFIER`: `PASSWORD_CLAIM_SIGNATURE`, `PASSWORD_CLAIM_SECRET_BLOCK`, `TIMESTAMP`, `USERNAME`, `SECRET_HASH` (if app client is configured with client secret).

    #   * `NEW_PASSWORD_REQUIRED`: `NEW_PASSWORD`, any other required attributes, `USERNAME`, `SECRET_HASH` (if app client is configured with client secret).
    challenge_responses: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Pinpoint analytics metadata for collecting metrics for
    # `RespondToAuthChallenge` calls.
    analytics_metadata: "AnalyticsMetadataType" = dataclasses.field(
        default_factory=dict,
    )

    # Contextual data such as the user's device fingerprint, IP address, or
    # location used for evaluating the risk of an unexpected event by Amazon
    # Cognito advanced security.
    user_context_data: "UserContextDataType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class RespondToAuthChallengeResponse(autoboto.ShapeBase):
    """
    The response to respond to the authentication challenge.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "challenge_name",
                "ChallengeName",
                autoboto.TypeInfo(ChallengeNameType),
            ),
            (
                "session",
                "Session",
                autoboto.TypeInfo(str),
            ),
            (
                "challenge_parameters",
                "ChallengeParameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "authentication_result",
                "AuthenticationResult",
                autoboto.TypeInfo(AuthenticationResultType),
            ),
        ]

    # The challenge name. For more information, see .
    challenge_name: "ChallengeNameType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The session which should be passed both ways in challenge-response calls to
    # the service. If the or API call determines that the caller needs to go
    # through another challenge, they return a session with other challenge
    # parameters. This session should be passed as it is to the next
    # `RespondToAuthChallenge` API call.
    session: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The challenge parameters. For more information, see .
    challenge_parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The result returned by the server in response to the request to respond to
    # the authentication challenge.
    authentication_result: "AuthenticationResultType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class RiskConfigurationType(autoboto.ShapeBase):
    """
    The risk configuration type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "compromised_credentials_risk_configuration",
                "CompromisedCredentialsRiskConfiguration",
                autoboto.TypeInfo(CompromisedCredentialsRiskConfigurationType),
            ),
            (
                "account_takeover_risk_configuration",
                "AccountTakeoverRiskConfiguration",
                autoboto.TypeInfo(AccountTakeoverRiskConfigurationType),
            ),
            (
                "risk_exception_configuration",
                "RiskExceptionConfiguration",
                autoboto.TypeInfo(RiskExceptionConfigurationType),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The app client ID.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The compromised credentials risk configuration object including the
    # `EventFilter` and the `EventAction`
    compromised_credentials_risk_configuration: "CompromisedCredentialsRiskConfigurationType" = dataclasses.field(
        default_factory=dict,
    )

    # The account takeover risk configuration object including the
    # `NotifyConfiguration` object and `Actions` to take in the case of an
    # account takeover.
    account_takeover_risk_configuration: "AccountTakeoverRiskConfigurationType" = dataclasses.field(
        default_factory=dict,
    )

    # The configuration to override the risk decision.
    risk_exception_configuration: "RiskExceptionConfigurationType" = dataclasses.field(
        default_factory=dict,
    )

    # The last modified date.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class RiskDecisionType(Enum):
    NoRisk = "NoRisk"
    AccountTakeover = "AccountTakeover"
    Block = "Block"


@dataclasses.dataclass
class RiskExceptionConfigurationType(autoboto.ShapeBase):
    """
    The type of the configuration to override the risk decision.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "blocked_ip_range_list",
                "BlockedIPRangeList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "skipped_ip_range_list",
                "SkippedIPRangeList",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # Overrides the risk decision to always block the pre-authentication
    # requests. The IP range is in CIDR notation: a compact representation of an
    # IP address and its associated routing prefix.
    blocked_ip_range_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Risk detection is not performed on the IP addresses in the range list. The
    # IP range is in CIDR notation.
    skipped_ip_range_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


class RiskLevelType(Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"


@dataclasses.dataclass
class SMSMfaSettingsType(autoboto.ShapeBase):
    """
    The SMS multi-factor authentication (MFA) settings type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "preferred_mfa",
                "PreferredMfa",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Specifies whether SMS text message MFA is enabled.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The preferred MFA method.
    preferred_mfa: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SchemaAttributeType(autoboto.ShapeBase):
    """
    Contains information about the schema attribute.
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
                "attribute_data_type",
                "AttributeDataType",
                autoboto.TypeInfo(AttributeDataType),
            ),
            (
                "developer_only_attribute",
                "DeveloperOnlyAttribute",
                autoboto.TypeInfo(bool),
            ),
            (
                "mutable",
                "Mutable",
                autoboto.TypeInfo(bool),
            ),
            (
                "required",
                "Required",
                autoboto.TypeInfo(bool),
            ),
            (
                "number_attribute_constraints",
                "NumberAttributeConstraints",
                autoboto.TypeInfo(NumberAttributeConstraintsType),
            ),
            (
                "string_attribute_constraints",
                "StringAttributeConstraints",
                autoboto.TypeInfo(StringAttributeConstraintsType),
            ),
        ]

    # A schema attribute of the name type.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The attribute data type.
    attribute_data_type: "AttributeDataType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether the attribute type is developer only.
    developer_only_attribute: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether the value of the attribute can be changed.
    mutable: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies whether a user pool attribute is required. If the attribute is
    # required and the user does not provide a value, registration or sign-in
    # will fail.
    required: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the constraints for an attribute of the number type.
    number_attribute_constraints: "NumberAttributeConstraintsType" = dataclasses.field(
        default_factory=dict,
    )

    # Specifies the constraints for an attribute of the string type.
    string_attribute_constraints: "StringAttributeConstraintsType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ScopeDoesNotExistException(autoboto.ShapeBase):
    """
    This exception is thrown when the specified scope does not exist.
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
class SetRiskConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "compromised_credentials_risk_configuration",
                "CompromisedCredentialsRiskConfiguration",
                autoboto.TypeInfo(CompromisedCredentialsRiskConfigurationType),
            ),
            (
                "account_takeover_risk_configuration",
                "AccountTakeoverRiskConfiguration",
                autoboto.TypeInfo(AccountTakeoverRiskConfigurationType),
            ),
            (
                "risk_exception_configuration",
                "RiskExceptionConfiguration",
                autoboto.TypeInfo(RiskExceptionConfigurationType),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The app client ID. If `ClientId` is null, then the risk configuration is
    # mapped to `userPoolId`. When the client ID is null, the same risk
    # configuration is applied to all the clients in the userPool.

    # Otherwise, `ClientId` is mapped to the client. When the client ID is not
    # null, the user pool configuration is overridden and the risk configuration
    # for the client is used instead.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The compromised credentials risk configuration.
    compromised_credentials_risk_configuration: "CompromisedCredentialsRiskConfigurationType" = dataclasses.field(
        default_factory=dict,
    )

    # The account takeover risk configuration.
    account_takeover_risk_configuration: "AccountTakeoverRiskConfigurationType" = dataclasses.field(
        default_factory=dict,
    )

    # The configuration to override the risk decision.
    risk_exception_configuration: "RiskExceptionConfigurationType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SetRiskConfigurationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "risk_configuration",
                "RiskConfiguration",
                autoboto.TypeInfo(RiskConfigurationType),
            ),
        ]

    # The risk configuration.
    risk_configuration: "RiskConfigurationType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SetUICustomizationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "css",
                "CSS",
                autoboto.TypeInfo(str),
            ),
            (
                "image_file",
                "ImageFile",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The client ID for the client app.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The CSS values in the UI customization.
    css: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The uploaded logo image for the UI customization.
    image_file: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SetUICustomizationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ui_customization",
                "UICustomization",
                autoboto.TypeInfo(UICustomizationType),
            ),
        ]

    # The UI customization information.
    ui_customization: "UICustomizationType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SetUserMFAPreferenceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
            (
                "sms_mfa_settings",
                "SMSMfaSettings",
                autoboto.TypeInfo(SMSMfaSettingsType),
            ),
            (
                "software_token_mfa_settings",
                "SoftwareTokenMfaSettings",
                autoboto.TypeInfo(SoftwareTokenMfaSettingsType),
            ),
        ]

    # The access token.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The SMS text message multi-factor authentication (MFA) settings.
    sms_mfa_settings: "SMSMfaSettingsType" = dataclasses.field(
        default_factory=dict,
    )

    # The time-based one-time password software token MFA settings.
    software_token_mfa_settings: "SoftwareTokenMfaSettingsType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SetUserMFAPreferenceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SetUserPoolMfaConfigRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "sms_mfa_configuration",
                "SmsMfaConfiguration",
                autoboto.TypeInfo(SmsMfaConfigType),
            ),
            (
                "software_token_mfa_configuration",
                "SoftwareTokenMfaConfiguration",
                autoboto.TypeInfo(SoftwareTokenMfaConfigType),
            ),
            (
                "mfa_configuration",
                "MfaConfiguration",
                autoboto.TypeInfo(UserPoolMfaType),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The SMS text message MFA configuration.
    sms_mfa_configuration: "SmsMfaConfigType" = dataclasses.field(
        default_factory=dict,
    )

    # The software token MFA configuration.
    software_token_mfa_configuration: "SoftwareTokenMfaConfigType" = dataclasses.field(
        default_factory=dict,
    )

    # The MFA configuration.
    mfa_configuration: "UserPoolMfaType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SetUserPoolMfaConfigResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sms_mfa_configuration",
                "SmsMfaConfiguration",
                autoboto.TypeInfo(SmsMfaConfigType),
            ),
            (
                "software_token_mfa_configuration",
                "SoftwareTokenMfaConfiguration",
                autoboto.TypeInfo(SoftwareTokenMfaConfigType),
            ),
            (
                "mfa_configuration",
                "MfaConfiguration",
                autoboto.TypeInfo(UserPoolMfaType),
            ),
        ]

    # The SMS text message MFA configuration.
    sms_mfa_configuration: "SmsMfaConfigType" = dataclasses.field(
        default_factory=dict,
    )

    # The software token MFA configuration.
    software_token_mfa_configuration: "SoftwareTokenMfaConfigType" = dataclasses.field(
        default_factory=dict,
    )

    # The MFA configuration.
    mfa_configuration: "UserPoolMfaType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SetUserSettingsRequest(autoboto.ShapeBase):
    """
    Represents the request to set user settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
            (
                "mfa_options",
                "MFAOptions",
                autoboto.TypeInfo(typing.List[MFAOptionType]),
            ),
        ]

    # The access token for the set user settings request.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the options for MFA (e.g., email or phone number).
    mfa_options: typing.List["MFAOptionType"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class SetUserSettingsResponse(autoboto.ShapeBase):
    """
    The response from the server for a set user settings request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SignUpRequest(autoboto.ShapeBase):
    """
    Represents the request to register a user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "password",
                "Password",
                autoboto.TypeInfo(str),
            ),
            (
                "secret_hash",
                "SecretHash",
                autoboto.TypeInfo(str),
            ),
            (
                "user_attributes",
                "UserAttributes",
                autoboto.TypeInfo(typing.List[AttributeType]),
            ),
            (
                "validation_data",
                "ValidationData",
                autoboto.TypeInfo(typing.List[AttributeType]),
            ),
            (
                "analytics_metadata",
                "AnalyticsMetadata",
                autoboto.TypeInfo(AnalyticsMetadataType),
            ),
            (
                "user_context_data",
                "UserContextData",
                autoboto.TypeInfo(UserContextDataType),
            ),
        ]

    # The ID of the client associated with the user pool.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user name of the user you wish to register.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The password of the user you wish to register.
    password: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A keyed-hash message authentication code (HMAC) calculated using the secret
    # key of a user pool client and username plus the client ID in the message.
    secret_hash: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of name-value pairs representing user attributes.

    # For custom attributes, you must prepend the `custom:` prefix to the
    # attribute name.
    user_attributes: typing.List["AttributeType"] = dataclasses.field(
        default_factory=list,
    )

    # The validation data in the request to register a user.
    validation_data: typing.List["AttributeType"] = dataclasses.field(
        default_factory=list,
    )

    # The Amazon Pinpoint analytics metadata for collecting metrics for `SignUp`
    # calls.
    analytics_metadata: "AnalyticsMetadataType" = dataclasses.field(
        default_factory=dict,
    )

    # Contextual data such as the user's device fingerprint, IP address, or
    # location used for evaluating the risk of an unexpected event by Amazon
    # Cognito advanced security.
    user_context_data: "UserContextDataType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SignUpResponse(autoboto.ShapeBase):
    """
    The response from the server for a registration request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_confirmed",
                "UserConfirmed",
                autoboto.TypeInfo(bool),
            ),
            (
                "user_sub",
                "UserSub",
                autoboto.TypeInfo(str),
            ),
            (
                "code_delivery_details",
                "CodeDeliveryDetails",
                autoboto.TypeInfo(CodeDeliveryDetailsType),
            ),
        ]

    # A response from the server indicating that a user registration has been
    # confirmed.
    user_confirmed: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The UUID of the authenticated user. This is not the same as `username`.
    user_sub: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The code delivery details returned by the server response to the user
    # registration request.
    code_delivery_details: "CodeDeliveryDetailsType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SmsConfigurationType(autoboto.ShapeBase):
    """
    The SMS configuration type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sns_caller_arn",
                "SnsCallerArn",
                autoboto.TypeInfo(str),
            ),
            (
                "external_id",
                "ExternalId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the Amazon Simple Notification Service
    # (SNS) caller.
    sns_caller_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The external ID.
    external_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SmsMfaConfigType(autoboto.ShapeBase):
    """
    The SMS text message multi-factor authentication (MFA) configuration type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sms_authentication_message",
                "SmsAuthenticationMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "sms_configuration",
                "SmsConfiguration",
                autoboto.TypeInfo(SmsConfigurationType),
            ),
        ]

    # The SMS authentication message.
    sms_authentication_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The SMS configuration.
    sms_configuration: "SmsConfigurationType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SoftwareTokenMFANotFoundException(autoboto.ShapeBase):
    """
    This exception is thrown when the software token TOTP multi-factor
    authentication (MFA) is not enabled for the user pool.
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
class SoftwareTokenMfaConfigType(autoboto.ShapeBase):
    """
    The type used for enabling software token MFA at the user pool level.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Specifies whether software token MFA is enabled.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SoftwareTokenMfaSettingsType(autoboto.ShapeBase):
    """
    The type used for enabling software token MFA at the user level.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "preferred_mfa",
                "PreferredMfa",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Specifies whether software token MFA is enabled.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The preferred MFA method.
    preferred_mfa: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class StartUserImportJobRequest(autoboto.ShapeBase):
    """
    Represents the request to start the user import job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "job_id",
                "JobId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool that the users are being imported into.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The job ID for the user import job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StartUserImportJobResponse(autoboto.ShapeBase):
    """
    Represents the response from the server to the request to start the user import
    job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_import_job",
                "UserImportJob",
                autoboto.TypeInfo(UserImportJobType),
            ),
        ]

    # The job object that represents the user import job.
    user_import_job: "UserImportJobType" = dataclasses.field(
        default_factory=dict,
    )


class StatusType(Enum):
    Enabled = "Enabled"
    Disabled = "Disabled"


@dataclasses.dataclass
class StopUserImportJobRequest(autoboto.ShapeBase):
    """
    Represents the request to stop the user import job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "job_id",
                "JobId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID for the user pool that the users are being imported into.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The job ID for the user import job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StopUserImportJobResponse(autoboto.ShapeBase):
    """
    Represents the response from the server to the request to stop the user import
    job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_import_job",
                "UserImportJob",
                autoboto.TypeInfo(UserImportJobType),
            ),
        ]

    # The job object that represents the user import job.
    user_import_job: "UserImportJobType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class StringAttributeConstraintsType(autoboto.ShapeBase):
    """
    The constraints associated with a string attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "min_length",
                "MinLength",
                autoboto.TypeInfo(str),
            ),
            (
                "max_length",
                "MaxLength",
                autoboto.TypeInfo(str),
            ),
        ]

    # The minimum length.
    min_length: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum length.
    max_length: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TooManyFailedAttemptsException(autoboto.ShapeBase):
    """
    This exception is thrown when the user has made too many failed attempts for a
    given action (e.g., sign in).
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

    # The message returned when the Amazon Cognito service returns a too many
    # failed attempts exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TooManyRequestsException(autoboto.ShapeBase):
    """
    This exception is thrown when the user has made too many requests for a given
    operation.
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

    # The message returned when the Amazon Cognito service returns a too many
    # requests exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UICustomizationType(autoboto.ShapeBase):
    """
    A container for the UI customization information for a user pool's built-in app
    UI.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "image_url",
                "ImageUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "css",
                "CSS",
                autoboto.TypeInfo(str),
            ),
            (
                "css_version",
                "CSSVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The client ID for the client app.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The logo image for the UI customization.
    image_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The CSS values in the UI customization.
    css: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The CSS version number.
    css_version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The last-modified date for the UI customization.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The creation date for the UI customization.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UnexpectedLambdaException(autoboto.ShapeBase):
    """
    This exception is thrown when the Amazon Cognito service encounters an
    unexpected exception with the AWS Lambda service.
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

    # The message returned when the Amazon Cognito service returns an unexpected
    # AWS Lambda exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UnsupportedIdentityProviderException(autoboto.ShapeBase):
    """
    This exception is thrown when the specified identifier is not supported.
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
class UnsupportedUserStateException(autoboto.ShapeBase):
    """
    The request failed because the user is in an unsupported state.
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

    # The message returned when the user is in an unsupported state.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateAuthEventFeedbackRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "event_id",
                "EventId",
                autoboto.TypeInfo(str),
            ),
            (
                "feedback_token",
                "FeedbackToken",
                autoboto.TypeInfo(str),
            ),
            (
                "feedback_value",
                "FeedbackValue",
                autoboto.TypeInfo(FeedbackValueType),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user pool username.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The event ID.
    event_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The feedback token.
    feedback_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The authentication event feedback value.
    feedback_value: "FeedbackValueType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateAuthEventFeedbackResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateDeviceStatusRequest(autoboto.ShapeBase):
    """
    Represents the request to update the device status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
            (
                "device_key",
                "DeviceKey",
                autoboto.TypeInfo(str),
            ),
            (
                "device_remembered_status",
                "DeviceRememberedStatus",
                autoboto.TypeInfo(DeviceRememberedStatusType),
            ),
        ]

    # The access token.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The device key.
    device_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of whether a device is remembered.
    device_remembered_status: "DeviceRememberedStatusType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateDeviceStatusResponse(autoboto.ShapeBase):
    """
    The response to the request to update the device status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "precedence",
                "Precedence",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the group.
    group_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A string containing the new description of the group.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new role ARN for the group. This is used for setting the
    # `cognito:roles` and `cognito:preferred_role` claims in the token.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new precedence value for the group. For more information about this
    # parameter, see .
    precedence: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group",
                "Group",
                autoboto.TypeInfo(GroupType),
            ),
        ]

    # The group object for the group.
    group: "GroupType" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateIdentityProviderRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_name",
                "ProviderName",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_details",
                "ProviderDetails",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attribute_mapping",
                "AttributeMapping",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "idp_identifiers",
                "IdpIdentifiers",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identity provider name.
    provider_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The identity provider details to be updated, such as `MetadataURL` and
    # `MetadataFile`.
    provider_details: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The identity provider attribute mapping to be changed.
    attribute_mapping: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of identity provider identifiers.
    idp_identifiers: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateIdentityProviderResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_provider",
                "IdentityProvider",
                autoboto.TypeInfo(IdentityProviderType),
            ),
        ]

    # The identity provider object.
    identity_provider: "IdentityProviderType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateResourceServerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "identifier",
                "Identifier",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "scopes",
                "Scopes",
                autoboto.TypeInfo(typing.List[ResourceServerScopeType]),
            ),
        ]

    # The user pool ID for the user pool.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identifier for the resource server.
    identifier: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the resource server.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The scope values to be set for the resource server.
    scopes: typing.List["ResourceServerScopeType"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateResourceServerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_server",
                "ResourceServer",
                autoboto.TypeInfo(ResourceServerType),
            ),
        ]

    # The resource server.
    resource_server: "ResourceServerType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateUserAttributesRequest(autoboto.ShapeBase):
    """
    Represents the request to update user attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_attributes",
                "UserAttributes",
                autoboto.TypeInfo(typing.List[AttributeType]),
            ),
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of name-value pairs representing user attributes.

    # For custom attributes, you must prepend the `custom:` prefix to the
    # attribute name.
    user_attributes: typing.List["AttributeType"] = dataclasses.field(
        default_factory=list,
    )

    # The access token for the request to update user attributes.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateUserAttributesResponse(autoboto.ShapeBase):
    """
    Represents the response from the server for the request to update user
    attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code_delivery_details_list",
                "CodeDeliveryDetailsList",
                autoboto.TypeInfo(typing.List[CodeDeliveryDetailsType]),
            ),
        ]

    # The code delivery details list from the server for the request to update
    # user attributes.
    code_delivery_details_list: typing.List["CodeDeliveryDetailsType"
                                           ] = dataclasses.field(
                                               default_factory=list,
                                           )


@dataclasses.dataclass
class UpdateUserPoolClientRequest(autoboto.ShapeBase):
    """
    Represents the request to update the user pool client.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_name",
                "ClientName",
                autoboto.TypeInfo(str),
            ),
            (
                "refresh_token_validity",
                "RefreshTokenValidity",
                autoboto.TypeInfo(int),
            ),
            (
                "read_attributes",
                "ReadAttributes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "write_attributes",
                "WriteAttributes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "explicit_auth_flows",
                "ExplicitAuthFlows",
                autoboto.TypeInfo(typing.List[ExplicitAuthFlowsType]),
            ),
            (
                "supported_identity_providers",
                "SupportedIdentityProviders",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "callback_urls",
                "CallbackURLs",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "logout_urls",
                "LogoutURLs",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "default_redirect_uri",
                "DefaultRedirectURI",
                autoboto.TypeInfo(str),
            ),
            (
                "allowed_o_auth_flows",
                "AllowedOAuthFlows",
                autoboto.TypeInfo(typing.List[OAuthFlowType]),
            ),
            (
                "allowed_o_auth_scopes",
                "AllowedOAuthScopes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "allowed_o_auth_flows_user_pool_client",
                "AllowedOAuthFlowsUserPoolClient",
                autoboto.TypeInfo(bool),
            ),
            (
                "analytics_configuration",
                "AnalyticsConfiguration",
                autoboto.TypeInfo(AnalyticsConfigurationType),
            ),
        ]

    # The user pool ID for the user pool where you want to update the user pool
    # client.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the client associated with the user pool.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The client name from the update user pool client request.
    client_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time limit, in days, after which the refresh token is no longer valid
    # and cannot be used.
    refresh_token_validity: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The read-only attributes of the user pool.
    read_attributes: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The writeable attributes of the user pool.
    write_attributes: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Explicit authentication flows.
    explicit_auth_flows: typing.List["ExplicitAuthFlowsType"
                                    ] = dataclasses.field(
                                        default_factory=list,
                                    )

    # A list of provider names for the identity providers that are supported on
    # this client.
    supported_identity_providers: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list of allowed redirect (callback) URLs for the identity providers.

    # A redirect URI must:

    #   * Be an absolute URI.

    #   * Be registered with the authorization server.

    #   * Not use HTTP without TLS (i.e. use HTTPS instead of HTTP).

    #   * Not include a fragment component.

    # See [OAuth 2.0 - Redirection
    # Endpoint](https://tools.ietf.org/html/rfc6749#section-3.1.2).
    callback_urls: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of allowed logout URLs for the identity providers.
    logout_urls: typing.List[str] = dataclasses.field(default_factory=list, )

    # The default redirect URI. Must be in the `CallbackURLs` list.

    # A redirect URI must:

    #   * Be an absolute URI.

    #   * Be registered with the authorization server.

    #   * Not use HTTP without TLS (i.e. use HTTPS instead of HTTP).

    #   * Not include a fragment component.

    # See [OAuth 2.0 - Redirection
    # Endpoint](https://tools.ietf.org/html/rfc6749#section-3.1.2).
    default_redirect_uri: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Set to `code` to initiate a code grant flow, which provides an
    # authorization code as the response. This code can be exchanged for access
    # tokens with the token endpoint.

    # Set to `token` to specify that the client should get the access token (and,
    # optionally, ID token, based on scopes) directly.
    allowed_o_auth_flows: typing.List["OAuthFlowType"] = dataclasses.field(
        default_factory=list,
    )

    # A list of allowed `OAuth` scopes. Currently supported values are `"phone"`,
    # `"email"`, `"openid"`, and `"Cognito"`.
    allowed_o_auth_scopes: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Set to TRUE if the client is allowed to follow the OAuth protocol when
    # interacting with Cognito user pools.
    allowed_o_auth_flows_user_pool_client: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Pinpoint analytics configuration for collecting metrics for this
    # user pool.
    analytics_configuration: "AnalyticsConfigurationType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateUserPoolClientResponse(autoboto.ShapeBase):
    """
    Represents the response from the server to the request to update the user pool
    client.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_client",
                "UserPoolClient",
                autoboto.TypeInfo(UserPoolClientType),
            ),
        ]

    # The user pool client value from the response from the server when an update
    # user pool client request is made.
    user_pool_client: "UserPoolClientType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateUserPoolRequest(autoboto.ShapeBase):
    """
    Represents the request to update the user pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "policies",
                "Policies",
                autoboto.TypeInfo(UserPoolPolicyType),
            ),
            (
                "lambda_config",
                "LambdaConfig",
                autoboto.TypeInfo(LambdaConfigType),
            ),
            (
                "auto_verified_attributes",
                "AutoVerifiedAttributes",
                autoboto.TypeInfo(typing.List[VerifiedAttributeType]),
            ),
            (
                "sms_verification_message",
                "SmsVerificationMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "email_verification_message",
                "EmailVerificationMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "email_verification_subject",
                "EmailVerificationSubject",
                autoboto.TypeInfo(str),
            ),
            (
                "verification_message_template",
                "VerificationMessageTemplate",
                autoboto.TypeInfo(VerificationMessageTemplateType),
            ),
            (
                "sms_authentication_message",
                "SmsAuthenticationMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "mfa_configuration",
                "MfaConfiguration",
                autoboto.TypeInfo(UserPoolMfaType),
            ),
            (
                "device_configuration",
                "DeviceConfiguration",
                autoboto.TypeInfo(DeviceConfigurationType),
            ),
            (
                "email_configuration",
                "EmailConfiguration",
                autoboto.TypeInfo(EmailConfigurationType),
            ),
            (
                "sms_configuration",
                "SmsConfiguration",
                autoboto.TypeInfo(SmsConfigurationType),
            ),
            (
                "user_pool_tags",
                "UserPoolTags",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "admin_create_user_config",
                "AdminCreateUserConfig",
                autoboto.TypeInfo(AdminCreateUserConfigType),
            ),
            (
                "user_pool_add_ons",
                "UserPoolAddOns",
                autoboto.TypeInfo(UserPoolAddOnsType),
            ),
        ]

    # The user pool ID for the user pool you want to update.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A container with the policies you wish to update in a user pool.
    policies: "UserPoolPolicyType" = dataclasses.field(default_factory=dict, )

    # The AWS Lambda configuration information from the request to update the
    # user pool.
    lambda_config: "LambdaConfigType" = dataclasses.field(
        default_factory=dict,
    )

    # The attributes that are automatically verified when the Amazon Cognito
    # service makes a request to update user pools.
    auto_verified_attributes: typing.List["VerifiedAttributeType"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )

    # A container with information about the SMS verification message.
    sms_verification_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The contents of the email verification message.
    email_verification_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The subject of the email verification message.
    email_verification_subject: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The template for verification messages.
    verification_message_template: "VerificationMessageTemplateType" = dataclasses.field(
        default_factory=dict,
    )

    # The contents of the SMS authentication message.
    sms_authentication_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Can be one of the following values:

    #   * `OFF` \- MFA tokens are not required and cannot be specified during user registration.

    #   * `ON` \- MFA tokens are required for all user registrations. You can only specify required when you are initially creating a user pool.

    #   * `OPTIONAL` \- Users have the option when registering to create an MFA token.
    mfa_configuration: "UserPoolMfaType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Device configuration.
    device_configuration: "DeviceConfigurationType" = dataclasses.field(
        default_factory=dict,
    )

    # Email configuration.
    email_configuration: "EmailConfigurationType" = dataclasses.field(
        default_factory=dict,
    )

    # SMS configuration.
    sms_configuration: "SmsConfigurationType" = dataclasses.field(
        default_factory=dict,
    )

    # The cost allocation tags for the user pool. For more information, see
    # [Adding Cost Allocation Tags to Your User
    # Pool](http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-
    # user-pools-cost-allocation-tagging.html)
    user_pool_tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The configuration for `AdminCreateUser` requests.
    admin_create_user_config: "AdminCreateUserConfigType" = dataclasses.field(
        default_factory=dict,
    )

    # Used to enable advanced security risk detection. Set the key
    # `AdvancedSecurityMode` to the value "AUDIT".
    user_pool_add_ons: "UserPoolAddOnsType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateUserPoolResponse(autoboto.ShapeBase):
    """
    Represents the response from the server when you make a request to update the
    user pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UserContextDataType(autoboto.ShapeBase):
    """
    Contextual data such as the user's device fingerprint, IP address, or location
    used for evaluating the risk of an unexpected event by Amazon Cognito advanced
    security.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encoded_data",
                "EncodedData",
                autoboto.TypeInfo(str),
            ),
        ]

    # Contextual data such as the user's device fingerprint, IP address, or
    # location used for evaluating the risk of an unexpected event by Amazon
    # Cognito advanced security.
    encoded_data: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UserImportInProgressException(autoboto.ShapeBase):
    """
    This exception is thrown when you are trying to modify a user pool while a user
    import job is in progress for that pool.
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

    # The message returned when the user pool has an import job running.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class UserImportJobStatusType(Enum):
    Created = "Created"
    Pending = "Pending"
    InProgress = "InProgress"
    Stopping = "Stopping"
    Expired = "Expired"
    Stopped = "Stopped"
    Failed = "Failed"
    Succeeded = "Succeeded"


@dataclasses.dataclass
class UserImportJobType(autoboto.ShapeBase):
    """
    The user import job type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
            (
                "job_id",
                "JobId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "pre_signed_url",
                "PreSignedUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "start_date",
                "StartDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "completion_date",
                "CompletionDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(UserImportJobStatusType),
            ),
            (
                "cloud_watch_logs_role_arn",
                "CloudWatchLogsRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "imported_users",
                "ImportedUsers",
                autoboto.TypeInfo(int),
            ),
            (
                "skipped_users",
                "SkippedUsers",
                autoboto.TypeInfo(int),
            ),
            (
                "failed_users",
                "FailedUsers",
                autoboto.TypeInfo(int),
            ),
            (
                "completion_message",
                "CompletionMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The job name for the user import job.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The job ID for the user import job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user pool ID for the user pool that the users are being imported into.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The pre-signed URL to be used to upload the `.csv` file.
    pre_signed_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the user import job was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date when the user import job was started.
    start_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date when the user import job was completed.
    completion_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the user import job. One of the following:

    #   * `Created` \- The job was created but not started.

    #   * `Pending` \- A transition state. You have started the job, but it has not begun importing users yet.

    #   * `InProgress` \- The job has started, and users are being imported.

    #   * `Stopping` \- You have stopped the job, but the job has not stopped importing users yet.

    #   * `Stopped` \- You have stopped the job, and the job has stopped importing users.

    #   * `Succeeded` \- The job has completed successfully.

    #   * `Failed` \- The job has stopped due to an error.

    #   * `Expired` \- You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job cannot be started.
    status: "UserImportJobStatusType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The role ARN for the Amazon CloudWatch Logging role for the user import
    # job. For more information, see "Creating the CloudWatch Logs IAM Role" in
    # the Amazon Cognito Developer Guide.
    cloud_watch_logs_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of users that were successfully imported.
    imported_users: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of users that were skipped.
    skipped_users: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of users that could not be imported.
    failed_users: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message returned when the user import job is completed.
    completion_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UserLambdaValidationException(autoboto.ShapeBase):
    """
    This exception is thrown when the Amazon Cognito service encounters a user
    validation exception with the AWS Lambda service.
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

    # The message returned when the Amazon Cognito service returns a user
    # validation exception with the AWS Lambda service.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UserNotConfirmedException(autoboto.ShapeBase):
    """
    This exception is thrown when a user is not confirmed successfully.
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

    # The message returned when a user is not confirmed successfully.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UserNotFoundException(autoboto.ShapeBase):
    """
    This exception is thrown when a user is not found.
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

    # The message returned when a user is not found.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UserPoolAddOnNotEnabledException(autoboto.ShapeBase):
    """
    This exception is thrown when user pool add-ons are not enabled.
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
class UserPoolAddOnsType(autoboto.ShapeBase):
    """
    The user pool add-ons type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "advanced_security_mode",
                "AdvancedSecurityMode",
                autoboto.TypeInfo(AdvancedSecurityModeType),
            ),
        ]

    # The advanced security mode.
    advanced_security_mode: "AdvancedSecurityModeType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UserPoolClientDescription(autoboto.ShapeBase):
    """
    The description of the user pool client.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_name",
                "ClientName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the client associated with the user pool.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user pool ID for the user pool where you want to describe the user pool
    # client.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The client name from the user pool client description.
    client_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UserPoolClientType(autoboto.ShapeBase):
    """
    Contains information about a user pool client.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "UserPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_name",
                "ClientName",
                autoboto.TypeInfo(str),
            ),
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_secret",
                "ClientSecret",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "refresh_token_validity",
                "RefreshTokenValidity",
                autoboto.TypeInfo(int),
            ),
            (
                "read_attributes",
                "ReadAttributes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "write_attributes",
                "WriteAttributes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "explicit_auth_flows",
                "ExplicitAuthFlows",
                autoboto.TypeInfo(typing.List[ExplicitAuthFlowsType]),
            ),
            (
                "supported_identity_providers",
                "SupportedIdentityProviders",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "callback_urls",
                "CallbackURLs",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "logout_urls",
                "LogoutURLs",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "default_redirect_uri",
                "DefaultRedirectURI",
                autoboto.TypeInfo(str),
            ),
            (
                "allowed_o_auth_flows",
                "AllowedOAuthFlows",
                autoboto.TypeInfo(typing.List[OAuthFlowType]),
            ),
            (
                "allowed_o_auth_scopes",
                "AllowedOAuthScopes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "allowed_o_auth_flows_user_pool_client",
                "AllowedOAuthFlowsUserPoolClient",
                autoboto.TypeInfo(bool),
            ),
            (
                "analytics_configuration",
                "AnalyticsConfiguration",
                autoboto.TypeInfo(AnalyticsConfigurationType),
            ),
        ]

    # The user pool ID for the user pool client.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The client name from the user pool request of the client type.
    client_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the client associated with the user pool.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The client secret from the user pool request of the client type.
    client_secret: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the user pool client was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the user pool client was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time limit, in days, after which the refresh token is no longer valid
    # and cannot be used.
    refresh_token_validity: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Read-only attributes.
    read_attributes: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The writeable attributes.
    write_attributes: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The explicit authentication flows.
    explicit_auth_flows: typing.List["ExplicitAuthFlowsType"
                                    ] = dataclasses.field(
                                        default_factory=list,
                                    )

    # A list of provider names for the identity providers that are supported on
    # this client.
    supported_identity_providers: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list of allowed redirect (callback) URLs for the identity providers.

    # A redirect URI must:

    #   * Be an absolute URI.

    #   * Be registered with the authorization server.

    #   * Not use HTTP without TLS (i.e. use HTTPS instead of HTTP).

    #   * Not include a fragment component.

    # See [OAuth 2.0 - Redirection
    # Endpoint](https://tools.ietf.org/html/rfc6749#section-3.1.2).
    callback_urls: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of allowed logout URLs for the identity providers.
    logout_urls: typing.List[str] = dataclasses.field(default_factory=list, )

    # The default redirect URI. Must be in the `CallbackURLs` list.

    # A redirect URI must:

    #   * Be an absolute URI.

    #   * Be registered with the authorization server.

    #   * Not use HTTP without TLS (i.e. use HTTPS instead of HTTP).

    #   * Not include a fragment component.

    # See [OAuth 2.0 - Redirection
    # Endpoint](https://tools.ietf.org/html/rfc6749#section-3.1.2).
    default_redirect_uri: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Set to `code` to initiate a code grant flow, which provides an
    # authorization code as the response. This code can be exchanged for access
    # tokens with the token endpoint.

    # Set to `token` to specify that the client should get the access token (and,
    # optionally, ID token, based on scopes) directly.
    allowed_o_auth_flows: typing.List["OAuthFlowType"] = dataclasses.field(
        default_factory=list,
    )

    # A list of allowed `OAuth` scopes. Currently supported values are `"phone"`,
    # `"email"`, `"openid"`, and `"Cognito"`.
    allowed_o_auth_scopes: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Set to TRUE if the client is allowed to follow the OAuth protocol when
    # interacting with Cognito user pools.
    allowed_o_auth_flows_user_pool_client: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Pinpoint analytics configuration for the user pool client.
    analytics_configuration: "AnalyticsConfigurationType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UserPoolDescriptionType(autoboto.ShapeBase):
    """
    A user pool description.
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
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "lambda_config",
                "LambdaConfig",
                autoboto.TypeInfo(LambdaConfigType),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(StatusType),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ID in a user pool description.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name in a user pool description.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The AWS Lambda configuration information in a user pool description.
    lambda_config: "LambdaConfigType" = dataclasses.field(
        default_factory=dict,
    )

    # The user pool status in a user pool description.
    status: "StatusType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the user pool description was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the user pool description was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class UserPoolMfaType(Enum):
    OFF = "OFF"
    ON = "ON"
    OPTIONAL = "OPTIONAL"


@dataclasses.dataclass
class UserPoolPolicyType(autoboto.ShapeBase):
    """
    The policy associated with a user pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "password_policy",
                "PasswordPolicy",
                autoboto.TypeInfo(PasswordPolicyType),
            ),
        ]

    # The password policy.
    password_policy: "PasswordPolicyType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UserPoolTaggingException(autoboto.ShapeBase):
    """
    This exception is thrown when a user pool tag cannot be set or updated.
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
class UserPoolType(autoboto.ShapeBase):
    """
    A container for information about the user pool.
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
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "policies",
                "Policies",
                autoboto.TypeInfo(UserPoolPolicyType),
            ),
            (
                "lambda_config",
                "LambdaConfig",
                autoboto.TypeInfo(LambdaConfigType),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(StatusType),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "schema_attributes",
                "SchemaAttributes",
                autoboto.TypeInfo(typing.List[SchemaAttributeType]),
            ),
            (
                "auto_verified_attributes",
                "AutoVerifiedAttributes",
                autoboto.TypeInfo(typing.List[VerifiedAttributeType]),
            ),
            (
                "alias_attributes",
                "AliasAttributes",
                autoboto.TypeInfo(typing.List[AliasAttributeType]),
            ),
            (
                "username_attributes",
                "UsernameAttributes",
                autoboto.TypeInfo(typing.List[UsernameAttributeType]),
            ),
            (
                "sms_verification_message",
                "SmsVerificationMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "email_verification_message",
                "EmailVerificationMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "email_verification_subject",
                "EmailVerificationSubject",
                autoboto.TypeInfo(str),
            ),
            (
                "verification_message_template",
                "VerificationMessageTemplate",
                autoboto.TypeInfo(VerificationMessageTemplateType),
            ),
            (
                "sms_authentication_message",
                "SmsAuthenticationMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "mfa_configuration",
                "MfaConfiguration",
                autoboto.TypeInfo(UserPoolMfaType),
            ),
            (
                "device_configuration",
                "DeviceConfiguration",
                autoboto.TypeInfo(DeviceConfigurationType),
            ),
            (
                "estimated_number_of_users",
                "EstimatedNumberOfUsers",
                autoboto.TypeInfo(int),
            ),
            (
                "email_configuration",
                "EmailConfiguration",
                autoboto.TypeInfo(EmailConfigurationType),
            ),
            (
                "sms_configuration",
                "SmsConfiguration",
                autoboto.TypeInfo(SmsConfigurationType),
            ),
            (
                "user_pool_tags",
                "UserPoolTags",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sms_configuration_failure",
                "SmsConfigurationFailure",
                autoboto.TypeInfo(str),
            ),
            (
                "email_configuration_failure",
                "EmailConfigurationFailure",
                autoboto.TypeInfo(str),
            ),
            (
                "domain",
                "Domain",
                autoboto.TypeInfo(str),
            ),
            (
                "admin_create_user_config",
                "AdminCreateUserConfig",
                autoboto.TypeInfo(AdminCreateUserConfigType),
            ),
            (
                "user_pool_add_ons",
                "UserPoolAddOns",
                autoboto.TypeInfo(UserPoolAddOnsType),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the user pool.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the user pool.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The policies associated with the user pool.
    policies: "UserPoolPolicyType" = dataclasses.field(default_factory=dict, )

    # The AWS Lambda triggers associated with the user pool.
    lambda_config: "LambdaConfigType" = dataclasses.field(
        default_factory=dict,
    )

    # The status of a user pool.
    status: "StatusType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the user pool was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the user pool was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A container with the schema attributes of a user pool.
    schema_attributes: typing.List["SchemaAttributeType"] = dataclasses.field(
        default_factory=list,
    )

    # Specifies the attributes that are auto-verified in a user pool.
    auto_verified_attributes: typing.List["VerifiedAttributeType"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )

    # Specifies the attributes that are aliased in a user pool.
    alias_attributes: typing.List["AliasAttributeType"] = dataclasses.field(
        default_factory=list,
    )

    # Specifies whether email addresses or phone numbers can be specified as
    # usernames when a user signs up.
    username_attributes: typing.List["UsernameAttributeType"
                                    ] = dataclasses.field(
                                        default_factory=list,
                                    )

    # The contents of the SMS verification message.
    sms_verification_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The contents of the email verification message.
    email_verification_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The subject of the email verification message.
    email_verification_subject: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The template for verification messages.
    verification_message_template: "VerificationMessageTemplateType" = dataclasses.field(
        default_factory=dict,
    )

    # The contents of the SMS authentication message.
    sms_authentication_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Can be one of the following values:

    #   * `OFF` \- MFA tokens are not required and cannot be specified during user registration.

    #   * `ON` \- MFA tokens are required for all user registrations. You can only specify required when you are initially creating a user pool.

    #   * `OPTIONAL` \- Users have the option when registering to create an MFA token.
    mfa_configuration: "UserPoolMfaType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The device configuration.
    device_configuration: "DeviceConfigurationType" = dataclasses.field(
        default_factory=dict,
    )

    # A number estimating the size of the user pool.
    estimated_number_of_users: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The email configuration.
    email_configuration: "EmailConfigurationType" = dataclasses.field(
        default_factory=dict,
    )

    # The SMS configuration.
    sms_configuration: "SmsConfigurationType" = dataclasses.field(
        default_factory=dict,
    )

    # The cost allocation tags for the user pool. For more information, see
    # [Adding Cost Allocation Tags to Your User
    # Pool](http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-
    # user-pools-cost-allocation-tagging.html)
    user_pool_tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The reason why the SMS configuration cannot send the messages to your
    # users.
    sms_configuration_failure: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The reason why the email configuration cannot send the messages to your
    # users.
    email_configuration_failure: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Holds the domain prefix if the user pool has a domain associated with it.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The configuration for `AdminCreateUser` requests.
    admin_create_user_config: "AdminCreateUserConfigType" = dataclasses.field(
        default_factory=dict,
    )

    # The user pool add-ons.
    user_pool_add_ons: "UserPoolAddOnsType" = dataclasses.field(
        default_factory=dict,
    )

    # The Amazon Resource Name (ARN) for the user pool.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class UserStatusType(Enum):
    UNCONFIRMED = "UNCONFIRMED"
    CONFIRMED = "CONFIRMED"
    ARCHIVED = "ARCHIVED"
    COMPROMISED = "COMPROMISED"
    UNKNOWN = "UNKNOWN"
    RESET_REQUIRED = "RESET_REQUIRED"
    FORCE_CHANGE_PASSWORD = "FORCE_CHANGE_PASSWORD"


@dataclasses.dataclass
class UserType(autoboto.ShapeBase):
    """
    The user type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.List[AttributeType]),
            ),
            (
                "user_create_date",
                "UserCreateDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "user_last_modified_date",
                "UserLastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "user_status",
                "UserStatus",
                autoboto.TypeInfo(UserStatusType),
            ),
            (
                "mfa_options",
                "MFAOptions",
                autoboto.TypeInfo(typing.List[MFAOptionType]),
            ),
        ]

    # The user name of the user you wish to describe.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A container with information about the user type attributes.
    attributes: typing.List["AttributeType"] = dataclasses.field(
        default_factory=list,
    )

    # The creation date of the user.
    user_create_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The last modified date of the user.
    user_last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether the user is enabled.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user status. Can be one of the following:

    #   * UNCONFIRMED - User has been created but not confirmed.

    #   * CONFIRMED - User has been confirmed.

    #   * ARCHIVED - User is no longer active.

    #   * COMPROMISED - User is disabled due to a potential security threat.

    #   * UNKNOWN - User status is not known.
    user_status: "UserStatusType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The MFA options for the user.
    mfa_options: typing.List["MFAOptionType"] = dataclasses.field(
        default_factory=list,
    )


class UsernameAttributeType(Enum):
    phone_number = "phone_number"
    email = "email"


@dataclasses.dataclass
class UsernameExistsException(autoboto.ShapeBase):
    """
    This exception is thrown when Amazon Cognito encounters a user name that already
    exists in the user pool.
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

    # The message returned when Amazon Cognito throws a user name exists
    # exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class VerificationMessageTemplateType(autoboto.ShapeBase):
    """
    The template for verification messages.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sms_message",
                "SmsMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "email_message",
                "EmailMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "email_subject",
                "EmailSubject",
                autoboto.TypeInfo(str),
            ),
            (
                "email_message_by_link",
                "EmailMessageByLink",
                autoboto.TypeInfo(str),
            ),
            (
                "email_subject_by_link",
                "EmailSubjectByLink",
                autoboto.TypeInfo(str),
            ),
            (
                "default_email_option",
                "DefaultEmailOption",
                autoboto.TypeInfo(DefaultEmailOptionType),
            ),
        ]

    # The SMS message template.
    sms_message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The email message template.
    email_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The subject line for the email message template.
    email_subject: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The email message template for sending a confirmation link to the user.
    email_message_by_link: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The subject line for the email message template for sending a confirmation
    # link to the user.
    email_subject_by_link: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default email option.
    default_email_option: "DefaultEmailOptionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class VerifiedAttributeType(Enum):
    phone_number = "phone_number"
    email = "email"


@dataclasses.dataclass
class VerifySoftwareTokenRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_code",
                "UserCode",
                autoboto.TypeInfo(str),
            ),
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
            (
                "session",
                "Session",
                autoboto.TypeInfo(str),
            ),
            (
                "friendly_device_name",
                "FriendlyDeviceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The one time password computed using the secret code returned by
    user_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The access token.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The session which should be passed both ways in challenge-response calls to
    # the service.
    session: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The friendly device name.
    friendly_device_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class VerifySoftwareTokenResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                autoboto.TypeInfo(VerifySoftwareTokenResponseType),
            ),
            (
                "session",
                "Session",
                autoboto.TypeInfo(str),
            ),
        ]

    # The status of the verify software token.
    status: "VerifySoftwareTokenResponseType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The session which should be passed both ways in challenge-response calls to
    # the service.
    session: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class VerifySoftwareTokenResponseType(Enum):
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"


@dataclasses.dataclass
class VerifyUserAttributeRequest(autoboto.ShapeBase):
    """
    Represents the request to verify user attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_token",
                "AccessToken",
                autoboto.TypeInfo(str),
            ),
            (
                "attribute_name",
                "AttributeName",
                autoboto.TypeInfo(str),
            ),
            (
                "code",
                "Code",
                autoboto.TypeInfo(str),
            ),
        ]

    # Represents the access token of the request to verify user attributes.
    access_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The attribute name in the request to verify user attributes.
    attribute_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The verification code in the request to verify user attributes.
    code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class VerifyUserAttributeResponse(autoboto.ShapeBase):
    """
    A container representing the response from the server from the request to verify
    user attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []
