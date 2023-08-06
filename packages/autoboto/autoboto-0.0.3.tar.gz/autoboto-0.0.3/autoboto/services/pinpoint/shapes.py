import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class ADMChannelRequest(autoboto.ShapeBase):
    """
    Amazon Device Messaging channel definition.
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
                "client_secret",
                "ClientSecret",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The Client ID that you obtained from the Amazon App Distribution Portal.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Client Secret that you obtained from the Amazon App Distribution
    # Portal.
    client_secret: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates whether or not the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ADMChannelResponse(autoboto.ShapeBase):
    """
    Amazon Device Messaging channel definition.
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
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                autoboto.TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                autoboto.TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the application to which the channel applies.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time when this channel was created.
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates whether or not the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # (Deprecated) An identifier for the channel. Retained for backwards
    # compatibility.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Indicates whether or not the channel is archived.
    is_archived: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user who last updated this channel.
    last_modified_by: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time when this channel was last modified.
    last_modified_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The platform type. For this channel, the value is always "ADM."
    platform: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The channel version.
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ADMMessage(autoboto.ShapeBase):
    """
    ADM Message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(Action),
            ),
            (
                "body",
                "Body",
                autoboto.TypeInfo(str),
            ),
            (
                "consolidation_key",
                "ConsolidationKey",
                autoboto.TypeInfo(str),
            ),
            (
                "data",
                "Data",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "expires_after",
                "ExpiresAfter",
                autoboto.TypeInfo(str),
            ),
            (
                "icon_reference",
                "IconReference",
                autoboto.TypeInfo(str),
            ),
            (
                "image_icon_url",
                "ImageIconUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "image_url",
                "ImageUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "md5",
                "MD5",
                autoboto.TypeInfo(str),
            ),
            (
                "raw_content",
                "RawContent",
                autoboto.TypeInfo(str),
            ),
            (
                "silent_push",
                "SilentPush",
                autoboto.TypeInfo(bool),
            ),
            (
                "small_image_icon_url",
                "SmallImageIconUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "sound",
                "Sound",
                autoboto.TypeInfo(str),
            ),
            (
                "substitutions",
                "Substitutions",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "title",
                "Title",
                autoboto.TypeInfo(str),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
        ]

    # The action that occurs if the user taps a push notification delivered by
    # the campaign: OPEN_APP - Your app launches, or it becomes the foreground
    # app if it has been sent to the background. This is the default action.
    # DEEP_LINK - Uses deep linking features in iOS and Android to open your app
    # and display a designated user interface within the app. URL - The default
    # mobile browser on the user's device launches and opens a web page at the
    # URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
    action: "Action" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message body of the notification.
    body: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Optional. Arbitrary string used to indicate multiple messages are logically
    # the same and that ADM is allowed to drop previously enqueued messages in
    # favor of this one.
    consolidation_key: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The data payload used for a silent push. This payload is added to the
    # notifications' data.pinpoint.jsonBody' object
    data: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Optional. Number of seconds ADM should retain the message if the device is
    # offline
    expires_after: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The icon image name of the asset saved in your application.
    icon_reference: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URL that points to an image used as the large icon to the notification
    # content view.
    image_icon_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URL that points to an image used in the push notification.
    image_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Optional. Base-64-encoded MD5 checksum of the data parameter. Used to
    # verify data integrity
    md5: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Raw JSON formatted string to be used as the payload. This value
    # overrides the message.
    raw_content: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Indicates if the message should display on the users device. Silent pushes
    # can be used for Remote Configuration and Phone Home use cases.
    silent_push: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL that points to an image used as the small icon for the notification
    # which will be used to represent the notification in the status bar and
    # content view
    small_image_icon_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates a sound to play when the device receives the notification.
    # Supports default, or the filename of a sound resource bundled in the app.
    # Android sound files must reside in /res/raw/
    sound: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Default message substitutions. Can be overridden by individual address
    # substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The message title that displays above the message on the user's device.
    title: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL to open in the user's mobile browser. Used if the value for Action
    # is URL.
    url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class APNSChannelRequest(autoboto.ShapeBase):
    """
    Apple Push Notification Service channel definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_id",
                "BundleId",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate",
                "Certificate",
                autoboto.TypeInfo(str),
            ),
            (
                "default_authentication_method",
                "DefaultAuthenticationMethod",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "private_key",
                "PrivateKey",
                autoboto.TypeInfo(str),
            ),
            (
                "team_id",
                "TeamId",
                autoboto.TypeInfo(str),
            ),
            (
                "token_key",
                "TokenKey",
                autoboto.TypeInfo(str),
            ),
            (
                "token_key_id",
                "TokenKeyId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The bundle id used for APNs Tokens.
    bundle_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The distribution certificate from Apple.
    certificate: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The default authentication method used for APNs.
    default_authentication_method: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The certificate private key.
    private_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The team id used for APNs Tokens.
    team_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token key used for APNs Tokens.
    token_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token key used for APNs Tokens.
    token_key_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class APNSChannelResponse(autoboto.ShapeBase):
    """
    Apple Distribution Push Notification Service channel definition.
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
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "default_authentication_method",
                "DefaultAuthenticationMethod",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                autoboto.TypeInfo(bool),
            ),
            (
                "has_token_key",
                "HasTokenKey",
                autoboto.TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                autoboto.TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the application that the channel applies to.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time when this channel was created.
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default authentication method used for APNs.
    default_authentication_method: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates whether the channel is configured with a key for APNs token
    # authentication. Provide a token key by setting the TokenKey attribute.
    has_token_key: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # (Deprecated) An identifier for the channel. Retained for backwards
    # compatibility.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Indicates whether or not the channel is archived.
    is_archived: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user who last updated this channel.
    last_modified_by: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time when this channel was last modified.
    last_modified_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The platform type. For this channel, the value is always "ADM."
    platform: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The channel version.
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class APNSMessage(autoboto.ShapeBase):
    """
    APNS Message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(Action),
            ),
            (
                "badge",
                "Badge",
                autoboto.TypeInfo(int),
            ),
            (
                "body",
                "Body",
                autoboto.TypeInfo(str),
            ),
            (
                "category",
                "Category",
                autoboto.TypeInfo(str),
            ),
            (
                "collapse_id",
                "CollapseId",
                autoboto.TypeInfo(str),
            ),
            (
                "data",
                "Data",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "media_url",
                "MediaUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "preferred_authentication_method",
                "PreferredAuthenticationMethod",
                autoboto.TypeInfo(str),
            ),
            (
                "priority",
                "Priority",
                autoboto.TypeInfo(str),
            ),
            (
                "raw_content",
                "RawContent",
                autoboto.TypeInfo(str),
            ),
            (
                "silent_push",
                "SilentPush",
                autoboto.TypeInfo(bool),
            ),
            (
                "sound",
                "Sound",
                autoboto.TypeInfo(str),
            ),
            (
                "substitutions",
                "Substitutions",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "thread_id",
                "ThreadId",
                autoboto.TypeInfo(str),
            ),
            (
                "time_to_live",
                "TimeToLive",
                autoboto.TypeInfo(int),
            ),
            (
                "title",
                "Title",
                autoboto.TypeInfo(str),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
        ]

    # The action that occurs if the user taps a push notification delivered by
    # the campaign: OPEN_APP - Your app launches, or it becomes the foreground
    # app if it has been sent to the background. This is the default action.
    # DEEP_LINK - Uses deep linking features in iOS and Android to open your app
    # and display a designated user interface within the app. URL - The default
    # mobile browser on the user's device launches and opens a web page at the
    # URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
    action: "Action" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Include this key when you want the system to modify the badge of your app
    # icon. If this key is not included in the dictionary, the badge is not
    # changed. To remove the badge, set the value of this key to 0.
    badge: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message body of the notification.
    body: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Provide this key with a string value that represents the notification's
    # type. This value corresponds to the value in the identifier property of one
    # of your app's registered categories.
    category: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An ID that, if assigned to multiple messages, causes APNs to coalesce the
    # messages into a single push notification instead of delivering each message
    # individually. The value must not exceed 64 bytes. Amazon Pinpoint uses this
    # value to set the apns-collapse-id request header when it sends the message
    # to APNs.
    collapse_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The data payload used for a silent push. This payload is added to the
    # notifications' data.pinpoint.jsonBody' object
    data: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URL that points to a video used in the push notification.
    media_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The preferred authentication method, either "CERTIFICATE" or "TOKEN"
    preferred_authentication_method: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The message priority. Amazon Pinpoint uses this value to set the apns-
    # priority request header when it sends the message to APNs. Accepts the
    # following values: "5" - Low priority. Messages might be delayed, delivered
    # in groups, and throttled. "10" - High priority. Messages are sent
    # immediately. High priority messages must cause an alert, sound, or badge on
    # the receiving device. The default value is "10". The equivalent values for
    # FCM or GCM messages are "normal" and "high". Amazon Pinpoint accepts these
    # values for APNs messages and converts them. For more information about the
    # apns-priority parameter, see Communicating with APNs in the APNs Local and
    # Remote Notification Programming Guide.
    priority: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Raw JSON formatted string to be used as the payload. This value
    # overrides the message.
    raw_content: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Indicates if the message should display on the users device. Silent pushes
    # can be used for Remote Configuration and Phone Home use cases.
    silent_push: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Include this key when you want the system to play a sound. The value of
    # this key is the name of a sound file in your app's main bundle or in the
    # Library/Sounds folder of your app's data container. If the sound file
    # cannot be found, or if you specify defaultfor the value, the system plays
    # the default alert sound.
    sound: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Default message substitutions. Can be overridden by individual address
    # substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Provide this key with a string value that represents the app-specific
    # identifier for grouping notifications. If you provide a Notification
    # Content app extension, you can use this value to group your notifications
    # together.
    thread_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The length of time (in seconds) that APNs stores and attempts to deliver
    # the message. If the value is 0, APNs does not store the message or attempt
    # to deliver it more than once. Amazon Pinpoint uses this value to set the
    # apns-expiration request header when it sends the message to APNs.
    time_to_live: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message title that displays above the message on the user's device.
    title: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL to open in the user's mobile browser. Used if the value for Action
    # is URL.
    url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class APNSSandboxChannelRequest(autoboto.ShapeBase):
    """
    Apple Development Push Notification Service channel definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_id",
                "BundleId",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate",
                "Certificate",
                autoboto.TypeInfo(str),
            ),
            (
                "default_authentication_method",
                "DefaultAuthenticationMethod",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "private_key",
                "PrivateKey",
                autoboto.TypeInfo(str),
            ),
            (
                "team_id",
                "TeamId",
                autoboto.TypeInfo(str),
            ),
            (
                "token_key",
                "TokenKey",
                autoboto.TypeInfo(str),
            ),
            (
                "token_key_id",
                "TokenKeyId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The bundle id used for APNs Tokens.
    bundle_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The distribution certificate from Apple.
    certificate: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The default authentication method used for APNs.
    default_authentication_method: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The certificate private key.
    private_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The team id used for APNs Tokens.
    team_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token key used for APNs Tokens.
    token_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token key used for APNs Tokens.
    token_key_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class APNSSandboxChannelResponse(autoboto.ShapeBase):
    """
    Apple Development Push Notification Service channel definition.
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
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "default_authentication_method",
                "DefaultAuthenticationMethod",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                autoboto.TypeInfo(bool),
            ),
            (
                "has_token_key",
                "HasTokenKey",
                autoboto.TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                autoboto.TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the application to which the channel applies.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When was this segment created
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default authentication method used for APNs.
    default_authentication_method: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates whether the channel is configured with a key for APNs token
    # authentication. Provide a token key by setting the TokenKey attribute.
    has_token_key: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Channel ID. Not used, only for backwards compatibility.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Is this channel archived
    is_archived: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Who last updated this entry
    last_modified_by: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Last date this was updated
    last_modified_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The platform type. Will be APNS_SANDBOX.
    platform: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Version of channel
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class APNSVoipChannelRequest(autoboto.ShapeBase):
    """
    Apple VoIP Push Notification Service channel definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_id",
                "BundleId",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate",
                "Certificate",
                autoboto.TypeInfo(str),
            ),
            (
                "default_authentication_method",
                "DefaultAuthenticationMethod",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "private_key",
                "PrivateKey",
                autoboto.TypeInfo(str),
            ),
            (
                "team_id",
                "TeamId",
                autoboto.TypeInfo(str),
            ),
            (
                "token_key",
                "TokenKey",
                autoboto.TypeInfo(str),
            ),
            (
                "token_key_id",
                "TokenKeyId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The bundle id used for APNs Tokens.
    bundle_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The distribution certificate from Apple.
    certificate: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The default authentication method used for APNs.
    default_authentication_method: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The certificate private key.
    private_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The team id used for APNs Tokens.
    team_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token key used for APNs Tokens.
    token_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token key used for APNs Tokens.
    token_key_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class APNSVoipChannelResponse(autoboto.ShapeBase):
    """
    Apple VoIP Push Notification Service channel definition.
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
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "default_authentication_method",
                "DefaultAuthenticationMethod",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                autoboto.TypeInfo(bool),
            ),
            (
                "has_token_key",
                "HasTokenKey",
                autoboto.TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                autoboto.TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
        ]

    # Application id
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When was this segment created
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default authentication method used for APNs.
    default_authentication_method: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the channel is registered with a token key for authentication.
    has_token_key: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Channel ID. Not used, only for backwards compatibility.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Is this channel archived
    is_archived: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Who made the last change
    last_modified_by: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Last date this was updated
    last_modified_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The platform type. Will be APNS.
    platform: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Version of channel
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class APNSVoipSandboxChannelRequest(autoboto.ShapeBase):
    """
    Apple VoIP Developer Push Notification Service channel definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_id",
                "BundleId",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate",
                "Certificate",
                autoboto.TypeInfo(str),
            ),
            (
                "default_authentication_method",
                "DefaultAuthenticationMethod",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "private_key",
                "PrivateKey",
                autoboto.TypeInfo(str),
            ),
            (
                "team_id",
                "TeamId",
                autoboto.TypeInfo(str),
            ),
            (
                "token_key",
                "TokenKey",
                autoboto.TypeInfo(str),
            ),
            (
                "token_key_id",
                "TokenKeyId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The bundle id used for APNs Tokens.
    bundle_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The distribution certificate from Apple.
    certificate: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The default authentication method used for APNs.
    default_authentication_method: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The certificate private key.
    private_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The team id used for APNs Tokens.
    team_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token key used for APNs Tokens.
    token_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token key used for APNs Tokens.
    token_key_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class APNSVoipSandboxChannelResponse(autoboto.ShapeBase):
    """
    Apple VoIP Developer Push Notification Service channel definition.
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
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "default_authentication_method",
                "DefaultAuthenticationMethod",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                autoboto.TypeInfo(bool),
            ),
            (
                "has_token_key",
                "HasTokenKey",
                autoboto.TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                autoboto.TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
        ]

    # Application id
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When was this segment created
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default authentication method used for APNs.
    default_authentication_method: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the channel is registered with a token key for authentication.
    has_token_key: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Channel ID. Not used, only for backwards compatibility.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Is this channel archived
    is_archived: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Who made the last change
    last_modified_by: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Last date this was updated
    last_modified_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The platform type. Will be APNS.
    platform: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Version of channel
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class Action(Enum):
    OPEN_APP = "OPEN_APP"
    DEEP_LINK = "DEEP_LINK"
    URL = "URL"


@dataclasses.dataclass
class ActivitiesResponse(autoboto.ShapeBase):
    """
    Activities for campaign.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                autoboto.TypeInfo(typing.List[ActivityResponse]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # List of campaign activities
    item: typing.List["ActivityResponse"] = dataclasses.field(
        default_factory=list,
    )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ActivityResponse(autoboto.ShapeBase):
    """
    Activity definition
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
                "campaign_id",
                "CampaignId",
                autoboto.TypeInfo(str),
            ),
            (
                "end",
                "End",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "result",
                "Result",
                autoboto.TypeInfo(str),
            ),
            (
                "scheduled_start",
                "ScheduledStart",
                autoboto.TypeInfo(str),
            ),
            (
                "start",
                "Start",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(str),
            ),
            (
                "successful_endpoint_count",
                "SuccessfulEndpointCount",
                autoboto.TypeInfo(int),
            ),
            (
                "timezones_completed_count",
                "TimezonesCompletedCount",
                autoboto.TypeInfo(int),
            ),
            (
                "timezones_total_count",
                "TimezonesTotalCount",
                autoboto.TypeInfo(int),
            ),
            (
                "total_endpoint_count",
                "TotalEndpointCount",
                autoboto.TypeInfo(int),
            ),
            (
                "treatment_id",
                "TreatmentId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the application to which the campaign applies.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the campaign to which the activity applies.
    campaign_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The actual time the activity was marked CANCELLED or COMPLETED. Provided in
    # ISO 8601 format.
    end: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique activity ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Indicates whether the activity succeeded. Valid values: SUCCESS, FAIL
    result: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The scheduled start time for the activity in ISO 8601 format.
    scheduled_start: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The actual start time of the activity in ISO 8601 format.
    start: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The state of the activity. Valid values: PENDING, INITIALIZING, RUNNING,
    # PAUSED, CANCELLED, COMPLETED
    state: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The total number of endpoints to which the campaign successfully delivered
    # messages.
    successful_endpoint_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The total number of timezones completed.
    timezones_completed_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The total number of unique timezones present in the segment.
    timezones_total_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The total number of endpoints to which the campaign attempts to deliver
    # messages.
    total_endpoint_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of a variation of the campaign used for A/B testing.
    treatment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AddressConfiguration(autoboto.ShapeBase):
    """
    Address configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body_override",
                "BodyOverride",
                autoboto.TypeInfo(str),
            ),
            (
                "channel_type",
                "ChannelType",
                autoboto.TypeInfo(ChannelType),
            ),
            (
                "context",
                "Context",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "raw_content",
                "RawContent",
                autoboto.TypeInfo(str),
            ),
            (
                "substitutions",
                "Substitutions",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "title_override",
                "TitleOverride",
                autoboto.TypeInfo(str),
            ),
        ]

    # Body override. If specified will override default body.
    body_override: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP |
    # APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
    channel_type: "ChannelType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A map of custom attributes to attributes to be attached to the message for
    # this address. This payload is added to the push notification's
    # 'data.pinpoint' object or added to the email/sms delivery receipt event
    # attributes.
    context: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Raw JSON formatted string to be used as the payload. This value
    # overrides the message.
    raw_content: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A map of substitution values for the message to be merged with the
    # DefaultMessage's substitutions. Substitutions on this map take precedence
    # over the all other substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Title override. If specified will override default title if applicable.
    title_override: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ApplicationResponse(autoboto.ShapeBase):
    """
    Application Response.
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
        ]

    # The unique application ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The display name of the application.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ApplicationSettingsResource(autoboto.ShapeBase):
    """
    Application settings.
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
                "campaign_hook",
                "CampaignHook",
                autoboto.TypeInfo(CampaignHook),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(str),
            ),
            (
                "limits",
                "Limits",
                autoboto.TypeInfo(CampaignLimits),
            ),
            (
                "quiet_time",
                "QuietTime",
                autoboto.TypeInfo(QuietTime),
            ),
        ]

    # The unique ID for the application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Default campaign hook.
    campaign_hook: "CampaignHook" = dataclasses.field(default_factory=dict, )

    # The date that the settings were last updated in ISO 8601 format.
    last_modified_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default campaign limits for the app. These limits apply to each
    # campaign for the app, unless the campaign overrides the default with limits
    # of its own.
    limits: "CampaignLimits" = dataclasses.field(default_factory=dict, )

    # The default quiet time for the app. Each campaign for this app sends no
    # messages during this time unless the campaign overrides the default with a
    # quiet time of its own.
    quiet_time: "QuietTime" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ApplicationsResponse(autoboto.ShapeBase):
    """
    Get Applications Result.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                autoboto.TypeInfo(typing.List[ApplicationResponse]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # List of applications returned in this page.
    item: typing.List["ApplicationResponse"] = dataclasses.field(
        default_factory=list,
    )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AttributeDimension(autoboto.ShapeBase):
    """
    Custom attibute dimension
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_type",
                "AttributeType",
                autoboto.TypeInfo(AttributeType),
            ),
            (
                "values",
                "Values",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The type of dimension: INCLUSIVE - Endpoints that match the criteria are
    # included in the segment. EXCLUSIVE - Endpoints that match the criteria are
    # excluded from the segment.
    attribute_type: "AttributeType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The criteria values for the segment dimension. Endpoints with matching
    # attribute values are included or excluded from the segment, depending on
    # the setting for Type.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


class AttributeType(Enum):
    INCLUSIVE = "INCLUSIVE"
    EXCLUSIVE = "EXCLUSIVE"


@dataclasses.dataclass
class AttributesResource(autoboto.ShapeBase):
    """
    Attributes.
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
                "attribute_type",
                "AttributeType",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The unique ID for the application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The attribute type for the application.
    attribute_type: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The attributes for the application.
    attributes: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class BadRequestException(autoboto.ShapeBase):
    """
    Simple message object.
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
                "request_id",
                "RequestID",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message that's returned from the API.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique message body ID.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BaiduChannelRequest(autoboto.ShapeBase):
    """
    Baidu Cloud Push credentials
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_key",
                "ApiKey",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "secret_key",
                "SecretKey",
                autoboto.TypeInfo(str),
            ),
        ]

    # Platform credential API key from Baidu.
    api_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Platform credential Secret key from Baidu.
    secret_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BaiduChannelResponse(autoboto.ShapeBase):
    """
    Baidu Cloud Messaging channel definition
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
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "credential",
                "Credential",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                autoboto.TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                autoboto.TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
        ]

    # Application id
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When was this segment created
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Baidu API key from Baidu.
    credential: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Channel ID. Not used, only for backwards compatibility.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Is this channel archived
    is_archived: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Who made the last change
    last_modified_by: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Last date this was updated
    last_modified_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The platform type. Will be BAIDU
    platform: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Version of channel
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BaiduMessage(autoboto.ShapeBase):
    """
    Baidu Message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(Action),
            ),
            (
                "body",
                "Body",
                autoboto.TypeInfo(str),
            ),
            (
                "data",
                "Data",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "icon_reference",
                "IconReference",
                autoboto.TypeInfo(str),
            ),
            (
                "image_icon_url",
                "ImageIconUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "image_url",
                "ImageUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "raw_content",
                "RawContent",
                autoboto.TypeInfo(str),
            ),
            (
                "silent_push",
                "SilentPush",
                autoboto.TypeInfo(bool),
            ),
            (
                "small_image_icon_url",
                "SmallImageIconUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "sound",
                "Sound",
                autoboto.TypeInfo(str),
            ),
            (
                "substitutions",
                "Substitutions",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "time_to_live",
                "TimeToLive",
                autoboto.TypeInfo(int),
            ),
            (
                "title",
                "Title",
                autoboto.TypeInfo(str),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
        ]

    # The action that occurs if the user taps a push notification delivered by
    # the campaign: OPEN_APP - Your app launches, or it becomes the foreground
    # app if it has been sent to the background. This is the default action.
    # DEEP_LINK - Uses deep linking features in iOS and Android to open your app
    # and display a designated user interface within the app. URL - The default
    # mobile browser on the user's device launches and opens a web page at the
    # URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
    action: "Action" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message body of the notification.
    body: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The data payload used for a silent push. This payload is added to the
    # notifications' data.pinpoint.jsonBody' object
    data: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The icon image name of the asset saved in your application.
    icon_reference: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URL that points to an image used as the large icon to the notification
    # content view.
    image_icon_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URL that points to an image used in the push notification.
    image_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Raw JSON formatted string to be used as the payload. This value
    # overrides the message.
    raw_content: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Indicates if the message should display on the users device. Silent pushes
    # can be used for Remote Configuration and Phone Home use cases.
    silent_push: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL that points to an image used as the small icon for the notification
    # which will be used to represent the notification in the status bar and
    # content view
    small_image_icon_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates a sound to play when the device receives the notification.
    # Supports default, or the filename of a sound resource bundled in the app.
    # Android sound files must reside in /res/raw/
    sound: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Default message substitutions. Can be overridden by individual address
    # substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # This parameter specifies how long (in seconds) the message should be kept
    # in Baidu storage if the device is offline. The and the default value and
    # the maximum time to live supported is 7 days (604800 seconds)
    time_to_live: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message title that displays above the message on the user's device.
    title: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL to open in the user's mobile browser. Used if the value for Action
    # is URL.
    url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CampaignEmailMessage(autoboto.ShapeBase):
    """
    The email message configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body",
                "Body",
                autoboto.TypeInfo(str),
            ),
            (
                "from_address",
                "FromAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "html_body",
                "HtmlBody",
                autoboto.TypeInfo(str),
            ),
            (
                "title",
                "Title",
                autoboto.TypeInfo(str),
            ),
        ]

    # The email text body.
    body: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The email address used to send the email from. Defaults to use FromAddress
    # specified in the Email Channel.
    from_address: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The email html body.
    html_body: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The email title (Or subject).
    title: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CampaignHook(autoboto.ShapeBase):
    """
    Campaign hook information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lambda_function_name",
                "LambdaFunctionName",
                autoboto.TypeInfo(str),
            ),
            (
                "mode",
                "Mode",
                autoboto.TypeInfo(Mode),
            ),
            (
                "web_url",
                "WebUrl",
                autoboto.TypeInfo(str),
            ),
        ]

    # Lambda function name or arn to be called for delivery
    lambda_function_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # What mode Lambda should be invoked in.
    mode: "Mode" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Web URL to call for hook. If the URL has authentication specified it will
    # be added as authentication to the request
    web_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CampaignLimits(autoboto.ShapeBase):
    """
    Campaign Limits are used to limit the number of messages that can be sent to a
    user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "daily",
                "Daily",
                autoboto.TypeInfo(int),
            ),
            (
                "maximum_duration",
                "MaximumDuration",
                autoboto.TypeInfo(int),
            ),
            (
                "messages_per_second",
                "MessagesPerSecond",
                autoboto.TypeInfo(int),
            ),
            (
                "total",
                "Total",
                autoboto.TypeInfo(int),
            ),
        ]

    # The maximum number of messages that the campaign can send daily.
    daily: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The length of time (in seconds) that the campaign can run before it ends
    # and message deliveries stop. This duration begins at the scheduled start
    # time for the campaign. The minimum value is 60.
    maximum_duration: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of messages that the campaign can send per second. The minimum
    # value is 50, and the maximum is 20000.
    messages_per_second: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum total number of messages that the campaign can send.
    total: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CampaignResponse(autoboto.ShapeBase):
    """
    Campaign definition
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "additional_treatments",
                "AdditionalTreatments",
                autoboto.TypeInfo(typing.List[TreatmentResource]),
            ),
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "default_state",
                "DefaultState",
                autoboto.TypeInfo(CampaignState),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "holdout_percent",
                "HoldoutPercent",
                autoboto.TypeInfo(int),
            ),
            (
                "hook",
                "Hook",
                autoboto.TypeInfo(CampaignHook),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "is_paused",
                "IsPaused",
                autoboto.TypeInfo(bool),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(str),
            ),
            (
                "limits",
                "Limits",
                autoboto.TypeInfo(CampaignLimits),
            ),
            (
                "message_configuration",
                "MessageConfiguration",
                autoboto.TypeInfo(MessageConfiguration),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                autoboto.TypeInfo(Schedule),
            ),
            (
                "segment_id",
                "SegmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_version",
                "SegmentVersion",
                autoboto.TypeInfo(int),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(CampaignState),
            ),
            (
                "treatment_description",
                "TreatmentDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "treatment_name",
                "TreatmentName",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
        ]

    # Treatments that are defined in addition to the default treatment.
    additional_treatments: typing.List["TreatmentResource"] = dataclasses.field(
        default_factory=list,
    )

    # The ID of the application to which the campaign applies.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the campaign was created in ISO 8601 format.
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the campaign's default treatment. Only present for A/B test
    # campaigns.
    default_state: "CampaignState" = dataclasses.field(default_factory=dict, )

    # A description of the campaign.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The allocated percentage of end users who will not receive messages from
    # this campaign.
    holdout_percent: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Campaign hook information.
    hook: "CampaignHook" = dataclasses.field(default_factory=dict, )

    # The unique campaign ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Indicates whether the campaign is paused. A paused campaign does not send
    # messages unless you resume it by setting IsPaused to false.
    is_paused: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date the campaign was last updated in ISO 8601 format.
    last_modified_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The campaign limits settings.
    limits: "CampaignLimits" = dataclasses.field(default_factory=dict, )

    # The message configuration settings.
    message_configuration: "MessageConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The custom name of the campaign.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The campaign schedule.
    schedule: "Schedule" = dataclasses.field(default_factory=dict, )

    # The ID of the segment to which the campaign sends messages.
    segment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the segment to which the campaign sends messages.
    segment_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The campaign status. An A/B test campaign will have a status of COMPLETED
    # only when all treatments have a status of COMPLETED.
    state: "CampaignState" = dataclasses.field(default_factory=dict, )

    # A custom description for the treatment.
    treatment_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The custom name of a variation of the campaign used for A/B testing.
    treatment_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The campaign version number.
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CampaignSmsMessage(autoboto.ShapeBase):
    """
    SMS message configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body",
                "Body",
                autoboto.TypeInfo(str),
            ),
            (
                "message_type",
                "MessageType",
                autoboto.TypeInfo(MessageType),
            ),
            (
                "sender_id",
                "SenderId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The SMS text body.
    body: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Is this is a transactional SMS message, otherwise a promotional message.
    message_type: "MessageType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Sender ID of sent message.
    sender_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CampaignState(autoboto.ShapeBase):
    """
    State of the Campaign
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "campaign_status",
                "CampaignStatus",
                autoboto.TypeInfo(CampaignStatus),
            ),
        ]

    # The status of the campaign, or the status of a treatment that belongs to an
    # A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN,
    # COMPLETED, PAUSED
    campaign_status: "CampaignStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class CampaignStatus(Enum):
    SCHEDULED = "SCHEDULED"
    EXECUTING = "EXECUTING"
    PENDING_NEXT_RUN = "PENDING_NEXT_RUN"
    COMPLETED = "COMPLETED"
    PAUSED = "PAUSED"
    DELETED = "DELETED"


@dataclasses.dataclass
class CampaignsResponse(autoboto.ShapeBase):
    """
    List of available campaigns.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                autoboto.TypeInfo(typing.List[CampaignResponse]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of campaigns.
    item: typing.List["CampaignResponse"] = dataclasses.field(
        default_factory=list,
    )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ChannelResponse(autoboto.ShapeBase):
    """
    Base definition for channel response.
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
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                autoboto.TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                autoboto.TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
        ]

    # Application id
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When was this segment created
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Channel ID. Not used, only for backwards compatibility.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Is this channel archived
    is_archived: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Who made the last change
    last_modified_by: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Last date this was updated
    last_modified_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Version of channel
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class ChannelType(Enum):
    GCM = "GCM"
    APNS = "APNS"
    APNS_SANDBOX = "APNS_SANDBOX"
    APNS_VOIP = "APNS_VOIP"
    APNS_VOIP_SANDBOX = "APNS_VOIP_SANDBOX"
    ADM = "ADM"
    SMS = "SMS"
    EMAIL = "EMAIL"
    BAIDU = "BAIDU"
    CUSTOM = "CUSTOM"


@dataclasses.dataclass
class ChannelsResponse(autoboto.ShapeBase):
    """
    Get channels definition
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channels",
                "Channels",
                autoboto.TypeInfo(typing.Dict[str, ChannelResponse]),
            ),
        ]

    # A map of channels, with the ChannelType as the key and the Channel as the
    # value.
    channels: typing.Dict[str, "ChannelResponse"] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateAppRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "create_application_request",
                "CreateApplicationRequest",
                autoboto.TypeInfo(CreateApplicationRequest),
            ),
        ]

    # Application Request.
    create_application_request: "CreateApplicationRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateAppResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_response",
                "ApplicationResponse",
                autoboto.TypeInfo(ApplicationResponse),
            ),
        ]

    # Application Response.
    application_response: "ApplicationResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateApplicationRequest(autoboto.ShapeBase):
    """
    Application Request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The display name of the application. Used in the Amazon Pinpoint console.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateCampaignRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "write_campaign_request",
                "WriteCampaignRequest",
                autoboto.TypeInfo(WriteCampaignRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Used to create a campaign.
    write_campaign_request: "WriteCampaignRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateCampaignResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "campaign_response",
                "CampaignResponse",
                autoboto.TypeInfo(CampaignResponse),
            ),
        ]

    # Campaign definition
    campaign_response: "CampaignResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateExportJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "export_job_request",
                "ExportJobRequest",
                autoboto.TypeInfo(ExportJobRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Export job request.
    export_job_request: "ExportJobRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateExportJobResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_job_response",
                "ExportJobResponse",
                autoboto.TypeInfo(ExportJobResponse),
            ),
        ]

    # Export job response.
    export_job_response: "ExportJobResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateImportJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "import_job_request",
                "ImportJobRequest",
                autoboto.TypeInfo(ImportJobRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Import job request.
    import_job_request: "ImportJobRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateImportJobResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "import_job_response",
                "ImportJobResponse",
                autoboto.TypeInfo(ImportJobResponse),
            ),
        ]

    # Import job response.
    import_job_response: "ImportJobResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateSegmentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "write_segment_request",
                "WriteSegmentRequest",
                autoboto.TypeInfo(WriteSegmentRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Segment definition.
    write_segment_request: "WriteSegmentRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateSegmentResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "segment_response",
                "SegmentResponse",
                autoboto.TypeInfo(SegmentResponse),
            ),
        ]

    # Segment definition.
    segment_response: "SegmentResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DefaultMessage(autoboto.ShapeBase):
    """
    The default message to use across all channels.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body",
                "Body",
                autoboto.TypeInfo(str),
            ),
            (
                "substitutions",
                "Substitutions",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
        ]

    # The message body of the notification, the email body or the text message.
    body: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Default message substitutions. Can be overridden by individual address
    # substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DefaultPushNotificationMessage(autoboto.ShapeBase):
    """
    Default Push Notification Message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(Action),
            ),
            (
                "body",
                "Body",
                autoboto.TypeInfo(str),
            ),
            (
                "data",
                "Data",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "silent_push",
                "SilentPush",
                autoboto.TypeInfo(bool),
            ),
            (
                "substitutions",
                "Substitutions",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "title",
                "Title",
                autoboto.TypeInfo(str),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
        ]

    # The action that occurs if the user taps a push notification delivered by
    # the campaign: OPEN_APP - Your app launches, or it becomes the foreground
    # app if it has been sent to the background. This is the default action.
    # DEEP_LINK - Uses deep linking features in iOS and Android to open your app
    # and display a designated user interface within the app. URL - The default
    # mobile browser on the user's device launches and opens a web page at the
    # URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
    action: "Action" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message body of the notification.
    body: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The data payload used for a silent push. This payload is added to the
    # notifications' data.pinpoint.jsonBody' object
    data: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates if the message should display on the users device. Silent pushes
    # can be used for Remote Configuration and Phone Home use cases.
    silent_push: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Default message substitutions. Can be overridden by individual address
    # substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The message title that displays above the message on the user's device.
    title: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL to open in the user's mobile browser. Used if the value for Action
    # is URL.
    url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteAdmChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteAdmChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "adm_channel_response",
                "ADMChannelResponse",
                autoboto.TypeInfo(ADMChannelResponse),
            ),
        ]

    # Amazon Device Messaging channel definition.
    adm_channel_response: "ADMChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteApnsChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteApnsChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_channel_response",
                "APNSChannelResponse",
                autoboto.TypeInfo(APNSChannelResponse),
            ),
        ]

    # Apple Distribution Push Notification Service channel definition.
    apns_channel_response: "APNSChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteApnsSandboxChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteApnsSandboxChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_sandbox_channel_response",
                "APNSSandboxChannelResponse",
                autoboto.TypeInfo(APNSSandboxChannelResponse),
            ),
        ]

    # Apple Development Push Notification Service channel definition.
    apns_sandbox_channel_response: "APNSSandboxChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteApnsVoipChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteApnsVoipChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_voip_channel_response",
                "APNSVoipChannelResponse",
                autoboto.TypeInfo(APNSVoipChannelResponse),
            ),
        ]

    # Apple VoIP Push Notification Service channel definition.
    apns_voip_channel_response: "APNSVoipChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteApnsVoipSandboxChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteApnsVoipSandboxChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_voip_sandbox_channel_response",
                "APNSVoipSandboxChannelResponse",
                autoboto.TypeInfo(APNSVoipSandboxChannelResponse),
            ),
        ]

    # Apple VoIP Developer Push Notification Service channel definition.
    apns_voip_sandbox_channel_response: "APNSVoipSandboxChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteAppRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteAppResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_response",
                "ApplicationResponse",
                autoboto.TypeInfo(ApplicationResponse),
            ),
        ]

    # Application Response.
    application_response: "ApplicationResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteBaiduChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteBaiduChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baidu_channel_response",
                "BaiduChannelResponse",
                autoboto.TypeInfo(BaiduChannelResponse),
            ),
        ]

    # Baidu Cloud Messaging channel definition
    baidu_channel_response: "BaiduChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteCampaignRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "campaign_id",
                "CampaignId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the campaign.
    campaign_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteCampaignResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "campaign_response",
                "CampaignResponse",
                autoboto.TypeInfo(CampaignResponse),
            ),
        ]

    # Campaign definition
    campaign_response: "CampaignResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteEmailChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteEmailChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "email_channel_response",
                "EmailChannelResponse",
                autoboto.TypeInfo(EmailChannelResponse),
            ),
        ]

    # Email Channel Response.
    email_channel_response: "EmailChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteEndpointRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_id",
                "EndpointId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the endpoint.
    endpoint_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteEndpointResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_response",
                "EndpointResponse",
                autoboto.TypeInfo(EndpointResponse),
            ),
        ]

    # Endpoint response
    endpoint_response: "EndpointResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteEventStreamRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteEventStreamResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_stream",
                "EventStream",
                autoboto.TypeInfo(EventStream),
            ),
        ]

    # Model for an event publishing subscription export.
    event_stream: "EventStream" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteGcmChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteGcmChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gcm_channel_response",
                "GCMChannelResponse",
                autoboto.TypeInfo(GCMChannelResponse),
            ),
        ]

    # Google Cloud Messaging channel definition
    gcm_channel_response: "GCMChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteSegmentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the segment.
    segment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteSegmentResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "segment_response",
                "SegmentResponse",
                autoboto.TypeInfo(SegmentResponse),
            ),
        ]

    # Segment definition.
    segment_response: "SegmentResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteSmsChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteSmsChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sms_channel_response",
                "SMSChannelResponse",
                autoboto.TypeInfo(SMSChannelResponse),
            ),
        ]

    # SMS Channel Response.
    sms_channel_response: "SMSChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteUserEndpointsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the user.
    user_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteUserEndpointsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoints_response",
                "EndpointsResponse",
                autoboto.TypeInfo(EndpointsResponse),
            ),
        ]

    # List of endpoints
    endpoints_response: "EndpointsResponse" = dataclasses.field(
        default_factory=dict,
    )


class DeliveryStatus(Enum):
    SUCCESSFUL = "SUCCESSFUL"
    THROTTLED = "THROTTLED"
    TEMPORARY_FAILURE = "TEMPORARY_FAILURE"
    PERMANENT_FAILURE = "PERMANENT_FAILURE"
    UNKNOWN_FAILURE = "UNKNOWN_FAILURE"
    OPT_OUT = "OPT_OUT"
    DUPLICATE = "DUPLICATE"


class DimensionType(Enum):
    INCLUSIVE = "INCLUSIVE"
    EXCLUSIVE = "EXCLUSIVE"


@dataclasses.dataclass
class DirectMessageConfiguration(autoboto.ShapeBase):
    """
    Message definitions for the default message and any messages that are tailored
    for specific channels.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "adm_message",
                "ADMMessage",
                autoboto.TypeInfo(ADMMessage),
            ),
            (
                "apns_message",
                "APNSMessage",
                autoboto.TypeInfo(APNSMessage),
            ),
            (
                "baidu_message",
                "BaiduMessage",
                autoboto.TypeInfo(BaiduMessage),
            ),
            (
                "default_message",
                "DefaultMessage",
                autoboto.TypeInfo(DefaultMessage),
            ),
            (
                "default_push_notification_message",
                "DefaultPushNotificationMessage",
                autoboto.TypeInfo(DefaultPushNotificationMessage),
            ),
            (
                "gcm_message",
                "GCMMessage",
                autoboto.TypeInfo(GCMMessage),
            ),
            (
                "sms_message",
                "SMSMessage",
                autoboto.TypeInfo(SMSMessage),
            ),
        ]

    # The message to ADM channels. Overrides the default push notification
    # message.
    adm_message: "ADMMessage" = dataclasses.field(default_factory=dict, )

    # The message to APNS channels. Overrides the default push notification
    # message.
    apns_message: "APNSMessage" = dataclasses.field(default_factory=dict, )

    # The message to Baidu GCM channels. Overrides the default push notification
    # message.
    baidu_message: "BaiduMessage" = dataclasses.field(default_factory=dict, )

    # The default message for all channels.
    default_message: "DefaultMessage" = dataclasses.field(
        default_factory=dict,
    )

    # The default push notification message for all push channels.
    default_push_notification_message: "DefaultPushNotificationMessage" = dataclasses.field(
        default_factory=dict,
    )

    # The message to GCM channels. Overrides the default push notification
    # message.
    gcm_message: "GCMMessage" = dataclasses.field(default_factory=dict, )

    # The message to SMS channels. Overrides the default message.
    sms_message: "SMSMessage" = dataclasses.field(default_factory=dict, )


class Duration(Enum):
    HR_24 = "HR_24"
    DAY_7 = "DAY_7"
    DAY_14 = "DAY_14"
    DAY_30 = "DAY_30"


@dataclasses.dataclass
class EmailChannelRequest(autoboto.ShapeBase):
    """
    Email Channel Request
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
                "from_address",
                "FromAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "identity",
                "Identity",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The email address used to send emails from.
    from_address: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of an identity verified with SES.
    identity: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of an IAM Role used to submit events to Mobile Analytics' event
    # ingestion service
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EmailChannelResponse(autoboto.ShapeBase):
    """
    Email Channel Response.
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
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "from_address",
                "FromAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "has_credential",
                "HasCredential",
                autoboto.TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "identity",
                "Identity",
                autoboto.TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                autoboto.TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(str),
            ),
            (
                "messages_per_second",
                "MessagesPerSecond",
                autoboto.TypeInfo(int),
            ),
            (
                "platform",
                "Platform",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique ID of the application to which the email channel belongs.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date that the settings were last updated in ISO 8601 format.
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The email address used to send emails from.
    from_address: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Channel ID. Not used, only for backwards compatibility.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of an identity verified with SES.
    identity: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Is this channel archived
    is_archived: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Who last updated this entry
    last_modified_by: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Last date this was updated
    last_modified_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Messages per second that can be sent
    messages_per_second: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Platform type. Will be "EMAIL"
    platform: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of an IAM Role used to submit events to Mobile Analytics' event
    # ingestion service
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Version of channel
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EndpointBatchItem(autoboto.ShapeBase):
    """
    Endpoint update request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address",
                "Address",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "channel_type",
                "ChannelType",
                autoboto.TypeInfo(ChannelType),
            ),
            (
                "demographic",
                "Demographic",
                autoboto.TypeInfo(EndpointDemographic),
            ),
            (
                "effective_date",
                "EffectiveDate",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_status",
                "EndpointStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "location",
                "Location",
                autoboto.TypeInfo(EndpointLocation),
            ),
            (
                "metrics",
                "Metrics",
                autoboto.TypeInfo(typing.Dict[str, float]),
            ),
            (
                "opt_out",
                "OptOut",
                autoboto.TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "user",
                "User",
                autoboto.TypeInfo(EndpointUser),
            ),
        ]

    # The destination for messages that you send to this endpoint. The address
    # varies by channel. For mobile push channels, use the token provided by the
    # push notification service, such as the APNs device token or the FCM
    # registration token. For the SMS channel, use a phone number in E.164
    # format, such as +12065550100. For the email channel, use an email address.
    address: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Custom attributes that describe the endpoint by associating a name with an
    # array of values. For example, an attribute named "interests" might have the
    # values ["science", "politics", "travel"]. You can use these attributes as
    # selection criteria when you create a segment of users to engage with a
    # messaging campaign. The following characters are not recommended in
    # attribute names: # : ? \ /. The Amazon Pinpoint console does not display
    # attributes that include these characters in the name. This limitation does
    # not apply to attribute values.
    attributes: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP |
    # APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
    channel_type: "ChannelType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The endpoint demographic attributes.
    demographic: "EndpointDemographic" = dataclasses.field(
        default_factory=dict,
    )

    # The last time the endpoint was updated. Provided in ISO 8601 format.
    effective_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Unused.
    endpoint_status: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique Id for the Endpoint in the batch.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The endpoint location attributes.
    location: "EndpointLocation" = dataclasses.field(default_factory=dict, )

    # Custom metrics that your app reports to Amazon Pinpoint.
    metrics: typing.Dict[str, float] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates whether a user has opted out of receiving messages with one of
    # the following values: ALL - User has opted out of all messages. NONE -
    # Users has not opted out and receives all messages.
    opt_out: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID for the most recent request to update the endpoint.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Custom user-specific attributes that your app reports to Amazon Pinpoint.
    user: "EndpointUser" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class EndpointBatchRequest(autoboto.ShapeBase):
    """
    Endpoint batch update request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                autoboto.TypeInfo(typing.List[EndpointBatchItem]),
            ),
        ]

    # List of items to update. Maximum 100 items
    item: typing.List["EndpointBatchItem"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class EndpointDemographic(autoboto.ShapeBase):
    """
    Demographic information about the endpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "app_version",
                "AppVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "locale",
                "Locale",
                autoboto.TypeInfo(str),
            ),
            (
                "make",
                "Make",
                autoboto.TypeInfo(str),
            ),
            (
                "model",
                "Model",
                autoboto.TypeInfo(str),
            ),
            (
                "model_version",
                "ModelVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                autoboto.TypeInfo(str),
            ),
            (
                "platform_version",
                "PlatformVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                autoboto.TypeInfo(str),
            ),
        ]

    # The version of the application associated with the endpoint.
    app_version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The endpoint locale in the following format: The ISO 639-1 alpha-2 code,
    # followed by an underscore, followed by an ISO 3166-1 alpha-2 value.
    locale: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The manufacturer of the endpoint device, such as Apple or Samsung.
    make: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The model name or number of the endpoint device, such as iPhone.
    model: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The model version of the endpoint device.
    model_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The platform of the endpoint device, such as iOS or Android.
    platform: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The platform version of the endpoint device.
    platform_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The timezone of the endpoint. Specified as a tz database value, such as
    # Americas/Los_Angeles.
    timezone: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EndpointItemResponse(autoboto.ShapeBase):
    """
    The responses that are returned after you create or update an endpoint and
    record an event.
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
                "status_code",
                "StatusCode",
                autoboto.TypeInfo(int),
            ),
        ]

    # A custom message associated with the registration of an endpoint when
    # issuing a response.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status code to respond with for a particular endpoint id after endpoint
    # registration
    status_code: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EndpointLocation(autoboto.ShapeBase):
    """
    Location data for the endpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
            (
                "latitude",
                "Latitude",
                autoboto.TypeInfo(float),
            ),
            (
                "longitude",
                "Longitude",
                autoboto.TypeInfo(float),
            ),
            (
                "postal_code",
                "PostalCode",
                autoboto.TypeInfo(str),
            ),
            (
                "region",
                "Region",
                autoboto.TypeInfo(str),
            ),
        ]

    # The city where the endpoint is located.
    city: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The two-letter code for the country or region of the endpoint. Specified as
    # an ISO 3166-1 Alpha-2 code, such as "US" for the United States.
    country: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The latitude of the endpoint location, rounded to one decimal place.
    latitude: float = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The longitude of the endpoint location, rounded to one decimal place.
    longitude: float = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The postal code or zip code of the endpoint.
    postal_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The region of the endpoint location. For example, in the United States,
    # this corresponds to a state.
    region: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EndpointMessageResult(autoboto.ShapeBase):
    """
    The result from sending a message to an endpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address",
                "Address",
                autoboto.TypeInfo(str),
            ),
            (
                "delivery_status",
                "DeliveryStatus",
                autoboto.TypeInfo(DeliveryStatus),
            ),
            (
                "message_id",
                "MessageId",
                autoboto.TypeInfo(str),
            ),
            (
                "status_code",
                "StatusCode",
                autoboto.TypeInfo(int),
            ),
            (
                "status_message",
                "StatusMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "updated_token",
                "UpdatedToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Address that endpoint message was delivered to.
    address: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The delivery status of the message. Possible values: SUCCESS - The message
    # was successfully delivered to the endpoint. TRANSIENT_FAILURE - A temporary
    # error occurred. Amazon Pinpoint will attempt to deliver the message again
    # later. FAILURE_PERMANENT - An error occurred when delivering the message to
    # the endpoint. Amazon Pinpoint won't attempt to send the message again.
    # TIMEOUT - The message couldn't be sent within the timeout period.
    # QUIET_TIME - The local time for the endpoint was within the Quiet Hours for
    # the campaign. DAILY_CAP - The endpoint has received the maximum number of
    # messages it can receive within a 24-hour period. HOLDOUT - The endpoint was
    # in a hold out treatment for the campaign. THROTTLED - Amazon Pinpoint
    # throttled sending to this endpoint. EXPIRED - The endpoint address is
    # expired. CAMPAIGN_CAP - The endpoint received the maximum number of
    # messages allowed by the campaign. SERVICE_FAILURE - A service-level failure
    # prevented Amazon Pinpoint from delivering the message. UNKNOWN - An unknown
    # error occurred.
    delivery_status: "DeliveryStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Unique message identifier associated with the message that was sent.
    message_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Downstream service status code.
    status_code: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Status message for message delivery.
    status_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If token was updated as part of delivery. (This is GCM Specific)
    updated_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class EndpointRequest(autoboto.ShapeBase):
    """
    Endpoint update request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address",
                "Address",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "channel_type",
                "ChannelType",
                autoboto.TypeInfo(ChannelType),
            ),
            (
                "demographic",
                "Demographic",
                autoboto.TypeInfo(EndpointDemographic),
            ),
            (
                "effective_date",
                "EffectiveDate",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_status",
                "EndpointStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "location",
                "Location",
                autoboto.TypeInfo(EndpointLocation),
            ),
            (
                "metrics",
                "Metrics",
                autoboto.TypeInfo(typing.Dict[str, float]),
            ),
            (
                "opt_out",
                "OptOut",
                autoboto.TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "user",
                "User",
                autoboto.TypeInfo(EndpointUser),
            ),
        ]

    # The destination for messages that you send to this endpoint. The address
    # varies by channel. For mobile push channels, use the token provided by the
    # push notification service, such as the APNs device token or the FCM
    # registration token. For the SMS channel, use a phone number in E.164
    # format, such as +12065550100. For the email channel, use an email address.
    address: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Custom attributes that describe the endpoint by associating a name with an
    # array of values. For example, an attribute named "interests" might have the
    # values ["science", "politics", "travel"]. You can use these attributes as
    # selection criteria when you create a segment of users to engage with a
    # messaging campaign. The following characters are not recommended in
    # attribute names: # : ? \ /. The Amazon Pinpoint console does not display
    # attributes that include these characters in the name. This limitation does
    # not apply to attribute values.
    attributes: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP |
    # APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
    channel_type: "ChannelType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Demographic attributes for the endpoint.
    demographic: "EndpointDemographic" = dataclasses.field(
        default_factory=dict,
    )

    # The date and time when the endpoint was updated, shown in ISO 8601 format.
    effective_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Unused.
    endpoint_status: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The endpoint location attributes.
    location: "EndpointLocation" = dataclasses.field(default_factory=dict, )

    # Custom metrics that your app reports to Amazon Pinpoint.
    metrics: typing.Dict[str, float] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates whether a user has opted out of receiving messages with one of
    # the following values: ALL - User has opted out of all messages. NONE -
    # Users has not opted out and receives all messages.
    opt_out: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID for the most recent request to update the endpoint.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Custom user-specific attributes that your app reports to Amazon Pinpoint.
    user: "EndpointUser" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class EndpointResponse(autoboto.ShapeBase):
    """
    Endpoint response
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address",
                "Address",
                autoboto.TypeInfo(str),
            ),
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "channel_type",
                "ChannelType",
                autoboto.TypeInfo(ChannelType),
            ),
            (
                "cohort_id",
                "CohortId",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "demographic",
                "Demographic",
                autoboto.TypeInfo(EndpointDemographic),
            ),
            (
                "effective_date",
                "EffectiveDate",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_status",
                "EndpointStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "location",
                "Location",
                autoboto.TypeInfo(EndpointLocation),
            ),
            (
                "metrics",
                "Metrics",
                autoboto.TypeInfo(typing.Dict[str, float]),
            ),
            (
                "opt_out",
                "OptOut",
                autoboto.TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "user",
                "User",
                autoboto.TypeInfo(EndpointUser),
            ),
        ]

    # The address of the endpoint as provided by your push provider. For example,
    # the DeviceToken or RegistrationId.
    address: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the application that is associated with the endpoint.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Custom attributes that describe the endpoint by associating a name with an
    # array of values. For example, an attribute named "interests" might have the
    # following values: ["science", "politics", "travel"]. You can use these
    # attributes as selection criteria when you create segments. The Amazon
    # Pinpoint console can't display attribute names that include the following
    # characters: hash/pound sign (#), colon (:), question mark (?), backslash
    # (\\), and forward slash (/). For this reason, you should avoid using these
    # characters in the names of custom attributes.
    attributes: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP |
    # APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
    channel_type: "ChannelType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A number from 0-99 that represents the cohort the endpoint is assigned to.
    # Endpoints are grouped into cohorts randomly, and each cohort contains
    # approximately 1 percent of the endpoints for an app. Amazon Pinpoint
    # assigns cohorts to the holdout or treatment allocations for a campaign.
    cohort_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date and time when the endpoint was created, shown in ISO 8601 format.
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The endpoint demographic attributes.
    demographic: "EndpointDemographic" = dataclasses.field(
        default_factory=dict,
    )

    # The date and time when the endpoint was last updated, shown in ISO 8601
    # format.
    effective_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Unused.
    endpoint_status: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID that you assigned to the endpoint. The ID should be a
    # globally unique identifier (GUID) to ensure that it doesn't conflict with
    # other endpoint IDs associated with the application.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The endpoint location attributes.
    location: "EndpointLocation" = dataclasses.field(default_factory=dict, )

    # Custom metrics that your app reports to Amazon Pinpoint.
    metrics: typing.Dict[str, float] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates whether a user has opted out of receiving messages with one of
    # the following values: ALL - User has opted out of all messages. NONE -
    # Users has not opted out and receives all messages.
    opt_out: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID for the most recent request to update the endpoint.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Custom user-specific attributes that your app reports to Amazon Pinpoint.
    user: "EndpointUser" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class EndpointSendConfiguration(autoboto.ShapeBase):
    """
    Endpoint send configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body_override",
                "BodyOverride",
                autoboto.TypeInfo(str),
            ),
            (
                "context",
                "Context",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "raw_content",
                "RawContent",
                autoboto.TypeInfo(str),
            ),
            (
                "substitutions",
                "Substitutions",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "title_override",
                "TitleOverride",
                autoboto.TypeInfo(str),
            ),
        ]

    # Body override. If specified will override default body.
    body_override: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A map of custom attributes to attributes to be attached to the message for
    # this address. This payload is added to the push notification's
    # 'data.pinpoint' object or added to the email/sms delivery receipt event
    # attributes.
    context: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Raw JSON formatted string to be used as the payload. This value
    # overrides the message.
    raw_content: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A map of substitution values for the message to be merged with the
    # DefaultMessage's substitutions. Substitutions on this map take precedence
    # over the all other substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Title override. If specified will override default title if applicable.
    title_override: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class EndpointUser(autoboto.ShapeBase):
    """
    Endpoint user specific custom userAttributes
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_attributes",
                "UserAttributes",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "user_id",
                "UserId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Custom attributes that describe the user by associating a name with an
    # array of values. For example, an attribute named "interests" might have the
    # following values: ["science", "politics", "travel"]. You can use these
    # attributes as selection criteria when you create segments. The Amazon
    # Pinpoint console can't display attribute names that include the following
    # characters: hash/pound sign (#), colon (:), question mark (?), backslash
    # (\\), and forward slash (/). For this reason, you should avoid using these
    # characters in the names of custom attributes.
    user_attributes: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the user.
    user_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EndpointsResponse(autoboto.ShapeBase):
    """
    List of endpoints
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                autoboto.TypeInfo(typing.List[EndpointResponse]),
            ),
        ]

    # The list of endpoints.
    item: typing.List["EndpointResponse"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Event(autoboto.ShapeBase):
    """
    Model for creating or updating events.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "client_sdk_version",
                "ClientSdkVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "event_type",
                "EventType",
                autoboto.TypeInfo(str),
            ),
            (
                "metrics",
                "Metrics",
                autoboto.TypeInfo(typing.Dict[str, float]),
            ),
            (
                "session",
                "Session",
                autoboto.TypeInfo(Session),
            ),
            (
                "timestamp",
                "Timestamp",
                autoboto.TypeInfo(str),
            ),
        ]

    # Custom attributes that are associated with the event you're adding or
    # updating.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The version of the SDK that's running on the client device.
    client_sdk_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the custom event that you're recording.
    event_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Event metrics
    metrics: typing.Dict[str, float] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The session
    session: "Session" = dataclasses.field(default_factory=dict, )

    # The date and time when the event occurred, in ISO 8601 format.
    timestamp: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EventItemResponse(autoboto.ShapeBase):
    """
    The responses that are returned after you record an event.
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
                "status_code",
                "StatusCode",
                autoboto.TypeInfo(int),
            ),
        ]

    # A custom message that is associated with the processing of an event.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status code to respond with for a particular event id
    status_code: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EventStream(autoboto.ShapeBase):
    """
    Model for an event publishing subscription export.
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
                "destination_stream_arn",
                "DestinationStreamArn",
                autoboto.TypeInfo(str),
            ),
            (
                "external_id",
                "ExternalId",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_by",
                "LastUpdatedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the application from which events should be published.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose
    # delivery stream to which you want to publish events. Firehose ARN:
    # arn:aws:firehose:REGION:ACCOUNT_ID:deliverystream/STREAM_NAME Kinesis ARN:
    # arn:aws:kinesis:REGION:ACCOUNT_ID:stream/STREAM_NAME
    destination_stream_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # (Deprecated) Your AWS account ID, which you assigned to the ExternalID key
    # in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This
    # requirement is removed, and external IDs are not recommended for IAM roles
    # assumed by Amazon Pinpoint.
    external_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date the event stream was last updated in ISO 8601 format.
    last_modified_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IAM user who last modified the event stream.
    last_updated_by: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IAM role that authorizes Amazon Pinpoint to publish events to the
    # stream in your account.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EventsBatch(autoboto.ShapeBase):
    """
    Events batch definition
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint",
                "Endpoint",
                autoboto.TypeInfo(PublicEndpoint),
            ),
            (
                "events",
                "Events",
                autoboto.TypeInfo(typing.Dict[str, Event]),
            ),
        ]

    # Endpoint information
    endpoint: "PublicEndpoint" = dataclasses.field(default_factory=dict, )

    # Events
    events: typing.Dict[str, "Event"] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class EventsRequest(autoboto.ShapeBase):
    """
    Put Events request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "batch_item",
                "BatchItem",
                autoboto.TypeInfo(typing.Dict[str, EventsBatch]),
            ),
        ]

    # Batch of events with endpoint id as the key and an object of EventsBatch as
    # value. The EventsBatch object has the PublicEndpoint and a map of event
    # Id's to events
    batch_item: typing.Dict[str, "EventsBatch"] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class EventsResponse(autoboto.ShapeBase):
    """
    The results from processing a put events request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "results",
                "Results",
                autoboto.TypeInfo(typing.Dict[str, ItemResponse]),
            ),
        ]

    # A map containing a multi part response for each endpoint, with the endpoint
    # id as the key and item response as the value
    results: typing.Dict[str, "ItemResponse"] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ExportJobRequest(autoboto.ShapeBase):
    """
    Export job request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_url_prefix",
                "S3UrlPrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_version",
                "SegmentVersion",
                autoboto.TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint
    # access to the Amazon S3 location that endpoints will be exported to.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A URL that points to the location within an Amazon S3 bucket that will
    # receive the export. The location is typically a folder with multiple files.
    # The URL should follow this format: s3://bucket-name/folder-name/ Amazon
    # Pinpoint will export endpoints to this location.
    s3_url_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the segment to export endpoints from. If not present, Amazon
    # Pinpoint exports all of the endpoints that belong to the application.
    segment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the segment to export if specified.
    segment_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ExportJobResource(autoboto.ShapeBase):
    """
    Export job resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_url_prefix",
                "S3UrlPrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_version",
                "SegmentVersion",
                autoboto.TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint
    # access to the Amazon S3 location that endpoints will be exported to.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A URL that points to the location within an Amazon S3 bucket that will
    # receive the export. The location is typically a folder with multiple files.
    # The URL should follow this format: s3://bucket-name/folder-name/ Amazon
    # Pinpoint will export endpoints to this location.
    s3_url_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the segment to export endpoints from. If not present, Amazon
    # Pinpoint exports all of the endpoints that belong to the application.
    segment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the segment to export if specified.
    segment_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ExportJobResponse(autoboto.ShapeBase):
    """
    Export job response.
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
                "completed_pieces",
                "CompletedPieces",
                autoboto.TypeInfo(int),
            ),
            (
                "completion_date",
                "CompletionDate",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                autoboto.TypeInfo(ExportJobResource),
            ),
            (
                "failed_pieces",
                "FailedPieces",
                autoboto.TypeInfo(int),
            ),
            (
                "failures",
                "Failures",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                autoboto.TypeInfo(JobStatus),
            ),
            (
                "total_failures",
                "TotalFailures",
                autoboto.TypeInfo(int),
            ),
            (
                "total_pieces",
                "TotalPieces",
                autoboto.TypeInfo(int),
            ),
            (
                "total_processed",
                "TotalProcessed",
                autoboto.TypeInfo(int),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the application associated with the export job.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of pieces that have successfully completed as of the time of the
    # request.
    completed_pieces: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the job completed in ISO 8601 format.
    completion_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the job was created in ISO 8601 format.
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The export job settings.
    definition: "ExportJobResource" = dataclasses.field(default_factory=dict, )

    # The number of pieces that failed to be processed as of the time of the
    # request.
    failed_pieces: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Provides up to 100 of the first failed entries for the job, if any exist.
    failures: typing.List[str] = dataclasses.field(default_factory=list, )

    # The unique ID of the job.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the job. Valid values: CREATED, INITIALIZING, PROCESSING,
    # COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or
    # more pieces failed.
    job_status: "JobStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of endpoints that were not processed; for example, because of
    # syntax errors.
    total_failures: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The total number of pieces that must be processed to finish the job. Each
    # piece is an approximately equal portion of the endpoints.
    total_pieces: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of endpoints that were processed by the job.
    total_processed: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The job type. Will be 'EXPORT'.
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ExportJobsResponse(autoboto.ShapeBase):
    """
    Export job list.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                autoboto.TypeInfo(typing.List[ExportJobResponse]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of export jobs for the application.
    item: typing.List["ExportJobResponse"] = dataclasses.field(
        default_factory=list,
    )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ForbiddenException(autoboto.ShapeBase):
    """
    Simple message object.
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
                "request_id",
                "RequestID",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message that's returned from the API.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique message body ID.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class Format(Enum):
    CSV = "CSV"
    JSON = "JSON"


class Frequency(Enum):
    ONCE = "ONCE"
    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"


@dataclasses.dataclass
class GCMChannelRequest(autoboto.ShapeBase):
    """
    Google Cloud Messaging credentials
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_key",
                "ApiKey",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Platform credential API key from Google.
    api_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GCMChannelResponse(autoboto.ShapeBase):
    """
    Google Cloud Messaging channel definition
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
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "credential",
                "Credential",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                autoboto.TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                autoboto.TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the application to which the channel applies.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When was this segment created
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The GCM API key from Google.
    credential: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Channel ID. Not used. Present only for backwards compatibility.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Is this channel archived
    is_archived: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Who last updated this entry
    last_modified_by: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Last date this was updated
    last_modified_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The platform type. Will be GCM
    platform: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Version of channel
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GCMMessage(autoboto.ShapeBase):
    """
    GCM Message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(Action),
            ),
            (
                "body",
                "Body",
                autoboto.TypeInfo(str),
            ),
            (
                "collapse_key",
                "CollapseKey",
                autoboto.TypeInfo(str),
            ),
            (
                "data",
                "Data",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "icon_reference",
                "IconReference",
                autoboto.TypeInfo(str),
            ),
            (
                "image_icon_url",
                "ImageIconUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "image_url",
                "ImageUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "priority",
                "Priority",
                autoboto.TypeInfo(str),
            ),
            (
                "raw_content",
                "RawContent",
                autoboto.TypeInfo(str),
            ),
            (
                "restricted_package_name",
                "RestrictedPackageName",
                autoboto.TypeInfo(str),
            ),
            (
                "silent_push",
                "SilentPush",
                autoboto.TypeInfo(bool),
            ),
            (
                "small_image_icon_url",
                "SmallImageIconUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "sound",
                "Sound",
                autoboto.TypeInfo(str),
            ),
            (
                "substitutions",
                "Substitutions",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "time_to_live",
                "TimeToLive",
                autoboto.TypeInfo(int),
            ),
            (
                "title",
                "Title",
                autoboto.TypeInfo(str),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
        ]

    # The action that occurs if the user taps a push notification delivered by
    # the campaign: OPEN_APP - Your app launches, or it becomes the foreground
    # app if it has been sent to the background. This is the default action.
    # DEEP_LINK - Uses deep linking features in iOS and Android to open your app
    # and display a designated user interface within the app. URL - The default
    # mobile browser on the user's device launches and opens a web page at the
    # URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
    action: "Action" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message body of the notification.
    body: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # This parameter identifies a group of messages (e.g., with collapse_key:
    # "Updates Available") that can be collapsed, so that only the last message
    # gets sent when delivery can be resumed. This is intended to avoid sending
    # too many of the same messages when the device comes back online or becomes
    # active.
    collapse_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The data payload used for a silent push. This payload is added to the
    # notifications' data.pinpoint.jsonBody' object
    data: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The icon image name of the asset saved in your application.
    icon_reference: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URL that points to an image used as the large icon to the notification
    # content view.
    image_icon_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URL that points to an image used in the push notification.
    image_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message priority. Amazon Pinpoint uses this value to set the FCM or GCM
    # priority parameter when it sends the message. Accepts the following values:
    # "Normal" - Messages might be delayed. Delivery is optimized for battery
    # usage on the receiving device. Use normal priority unless immediate
    # delivery is required. "High" - Messages are sent immediately and might wake
    # a sleeping device. The equivalent values for APNs messages are "5" and
    # "10". Amazon Pinpoint accepts these values here and converts them. For more
    # information, see About FCM Messages in the Firebase documentation.
    priority: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Raw JSON formatted string to be used as the payload. This value
    # overrides the message.
    raw_content: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # This parameter specifies the package name of the application where the
    # registration tokens must match in order to receive the message.
    restricted_package_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates if the message should display on the users device. Silent pushes
    # can be used for Remote Configuration and Phone Home use cases.
    silent_push: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL that points to an image used as the small icon for the notification
    # which will be used to represent the notification in the status bar and
    # content view
    small_image_icon_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates a sound to play when the device receives the notification.
    # Supports default, or the filename of a sound resource bundled in the app.
    # Android sound files must reside in /res/raw/
    sound: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Default message substitutions. Can be overridden by individual address
    # substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The length of time (in seconds) that FCM or GCM stores and attempts to
    # deliver the message. If unspecified, the value defaults to the maximum,
    # which is 2,419,200 seconds (28 days). Amazon Pinpoint uses this value to
    # set the FCM or GCM time_to_live parameter.
    time_to_live: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message title that displays above the message on the user's device.
    title: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL to open in the user's mobile browser. Used if the value for Action
    # is URL.
    url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GPSCoordinates(autoboto.ShapeBase):
    """
    GPS coordinates
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "latitude",
                "Latitude",
                autoboto.TypeInfo(float),
            ),
            (
                "longitude",
                "Longitude",
                autoboto.TypeInfo(float),
            ),
        ]

    # Latitude
    latitude: float = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Longitude
    longitude: float = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GPSPointDimension(autoboto.ShapeBase):
    """
    GPS point location dimension
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "coordinates",
                "Coordinates",
                autoboto.TypeInfo(GPSCoordinates),
            ),
            (
                "range_in_kilometers",
                "RangeInKilometers",
                autoboto.TypeInfo(float),
            ),
        ]

    # Coordinate to measure distance from.
    coordinates: "GPSCoordinates" = dataclasses.field(default_factory=dict, )

    # Range in kilometers from the coordinate.
    range_in_kilometers: float = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetAdmChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetAdmChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "adm_channel_response",
                "ADMChannelResponse",
                autoboto.TypeInfo(ADMChannelResponse),
            ),
        ]

    # Amazon Device Messaging channel definition.
    adm_channel_response: "ADMChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetApnsChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetApnsChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_channel_response",
                "APNSChannelResponse",
                autoboto.TypeInfo(APNSChannelResponse),
            ),
        ]

    # Apple Distribution Push Notification Service channel definition.
    apns_channel_response: "APNSChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetApnsSandboxChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetApnsSandboxChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_sandbox_channel_response",
                "APNSSandboxChannelResponse",
                autoboto.TypeInfo(APNSSandboxChannelResponse),
            ),
        ]

    # Apple Development Push Notification Service channel definition.
    apns_sandbox_channel_response: "APNSSandboxChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetApnsVoipChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetApnsVoipChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_voip_channel_response",
                "APNSVoipChannelResponse",
                autoboto.TypeInfo(APNSVoipChannelResponse),
            ),
        ]

    # Apple VoIP Push Notification Service channel definition.
    apns_voip_channel_response: "APNSVoipChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetApnsVoipSandboxChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetApnsVoipSandboxChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_voip_sandbox_channel_response",
                "APNSVoipSandboxChannelResponse",
                autoboto.TypeInfo(APNSVoipSandboxChannelResponse),
            ),
        ]

    # Apple VoIP Developer Push Notification Service channel definition.
    apns_voip_sandbox_channel_response: "APNSVoipSandboxChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetAppRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetAppResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_response",
                "ApplicationResponse",
                autoboto.TypeInfo(ApplicationResponse),
            ),
        ]

    # Application Response.
    application_response: "ApplicationResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetApplicationSettingsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetApplicationSettingsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_settings_resource",
                "ApplicationSettingsResource",
                autoboto.TypeInfo(ApplicationSettingsResource),
            ),
        ]

    # Application settings.
    application_settings_resource: "ApplicationSettingsResource" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetAppsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(str),
            ),
            (
                "token",
                "Token",
                autoboto.TypeInfo(str),
            ),
        ]

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetAppsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "applications_response",
                "ApplicationsResponse",
                autoboto.TypeInfo(ApplicationsResponse),
            ),
        ]

    # Get Applications Result.
    applications_response: "ApplicationsResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetBaiduChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetBaiduChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baidu_channel_response",
                "BaiduChannelResponse",
                autoboto.TypeInfo(BaiduChannelResponse),
            ),
        ]

    # Baidu Cloud Messaging channel definition
    baidu_channel_response: "BaiduChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetCampaignActivitiesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "campaign_id",
                "CampaignId",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(str),
            ),
            (
                "token",
                "Token",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the campaign.
    campaign_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCampaignActivitiesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activities_response",
                "ActivitiesResponse",
                autoboto.TypeInfo(ActivitiesResponse),
            ),
        ]

    # Activities for campaign.
    activities_response: "ActivitiesResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetCampaignRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "campaign_id",
                "CampaignId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the campaign.
    campaign_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCampaignResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "campaign_response",
                "CampaignResponse",
                autoboto.TypeInfo(CampaignResponse),
            ),
        ]

    # Campaign definition
    campaign_response: "CampaignResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetCampaignVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "campaign_id",
                "CampaignId",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the campaign.
    campaign_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the campaign.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCampaignVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "campaign_response",
                "CampaignResponse",
                autoboto.TypeInfo(CampaignResponse),
            ),
        ]

    # Campaign definition
    campaign_response: "CampaignResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetCampaignVersionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "campaign_id",
                "CampaignId",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(str),
            ),
            (
                "token",
                "Token",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the campaign.
    campaign_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCampaignVersionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "campaigns_response",
                "CampaignsResponse",
                autoboto.TypeInfo(CampaignsResponse),
            ),
        ]

    # List of available campaigns.
    campaigns_response: "CampaignsResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetCampaignsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(str),
            ),
            (
                "token",
                "Token",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCampaignsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "campaigns_response",
                "CampaignsResponse",
                autoboto.TypeInfo(CampaignsResponse),
            ),
        ]

    # List of available campaigns.
    campaigns_response: "CampaignsResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetChannelsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetChannelsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channels_response",
                "ChannelsResponse",
                autoboto.TypeInfo(ChannelsResponse),
            ),
        ]

    # Get channels definition
    channels_response: "ChannelsResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetEmailChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetEmailChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "email_channel_response",
                "EmailChannelResponse",
                autoboto.TypeInfo(EmailChannelResponse),
            ),
        ]

    # Email Channel Response.
    email_channel_response: "EmailChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetEndpointRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_id",
                "EndpointId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the endpoint.
    endpoint_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetEndpointResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_response",
                "EndpointResponse",
                autoboto.TypeInfo(EndpointResponse),
            ),
        ]

    # Endpoint response
    endpoint_response: "EndpointResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetEventStreamRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetEventStreamResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_stream",
                "EventStream",
                autoboto.TypeInfo(EventStream),
            ),
        ]

    # Model for an event publishing subscription export.
    event_stream: "EventStream" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetExportJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "job_id",
                "JobId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetExportJobResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_job_response",
                "ExportJobResponse",
                autoboto.TypeInfo(ExportJobResponse),
            ),
        ]

    # Export job response.
    export_job_response: "ExportJobResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetExportJobsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(str),
            ),
            (
                "token",
                "Token",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetExportJobsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_jobs_response",
                "ExportJobsResponse",
                autoboto.TypeInfo(ExportJobsResponse),
            ),
        ]

    # Export job list.
    export_jobs_response: "ExportJobsResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetGcmChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetGcmChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gcm_channel_response",
                "GCMChannelResponse",
                autoboto.TypeInfo(GCMChannelResponse),
            ),
        ]

    # Google Cloud Messaging channel definition
    gcm_channel_response: "GCMChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetImportJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "job_id",
                "JobId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetImportJobResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "import_job_response",
                "ImportJobResponse",
                autoboto.TypeInfo(ImportJobResponse),
            ),
        ]

    # Import job response.
    import_job_response: "ImportJobResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetImportJobsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(str),
            ),
            (
                "token",
                "Token",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetImportJobsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "import_jobs_response",
                "ImportJobsResponse",
                autoboto.TypeInfo(ImportJobsResponse),
            ),
        ]

    # Import job list.
    import_jobs_response: "ImportJobsResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetSegmentExportJobsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(str),
            ),
            (
                "token",
                "Token",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the segment.
    segment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetSegmentExportJobsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_jobs_response",
                "ExportJobsResponse",
                autoboto.TypeInfo(ExportJobsResponse),
            ),
        ]

    # Export job list.
    export_jobs_response: "ExportJobsResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetSegmentImportJobsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(str),
            ),
            (
                "token",
                "Token",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the segment.
    segment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetSegmentImportJobsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "import_jobs_response",
                "ImportJobsResponse",
                autoboto.TypeInfo(ImportJobsResponse),
            ),
        ]

    # Import job list.
    import_jobs_response: "ImportJobsResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetSegmentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the segment.
    segment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetSegmentResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "segment_response",
                "SegmentResponse",
                autoboto.TypeInfo(SegmentResponse),
            ),
        ]

    # Segment definition.
    segment_response: "SegmentResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetSegmentVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the segment.
    segment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The segment version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetSegmentVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "segment_response",
                "SegmentResponse",
                autoboto.TypeInfo(SegmentResponse),
            ),
        ]

    # Segment definition.
    segment_response: "SegmentResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetSegmentVersionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(str),
            ),
            (
                "token",
                "Token",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the segment.
    segment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetSegmentVersionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "segments_response",
                "SegmentsResponse",
                autoboto.TypeInfo(SegmentsResponse),
            ),
        ]

    # Segments in your account.
    segments_response: "SegmentsResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetSegmentsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(str),
            ),
            (
                "token",
                "Token",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetSegmentsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "segments_response",
                "SegmentsResponse",
                autoboto.TypeInfo(SegmentsResponse),
            ),
        ]

    # Segments in your account.
    segments_response: "SegmentsResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetSmsChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetSmsChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sms_channel_response",
                "SMSChannelResponse",
                autoboto.TypeInfo(SMSChannelResponse),
            ),
        ]

    # SMS Channel Response.
    sms_channel_response: "SMSChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetUserEndpointsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the user.
    user_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetUserEndpointsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoints_response",
                "EndpointsResponse",
                autoboto.TypeInfo(EndpointsResponse),
            ),
        ]

    # List of endpoints
    endpoints_response: "EndpointsResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ImportJobRequest(autoboto.ShapeBase):
    """
    Import job request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "define_segment",
                "DefineSegment",
                autoboto.TypeInfo(bool),
            ),
            (
                "external_id",
                "ExternalId",
                autoboto.TypeInfo(str),
            ),
            (
                "format",
                "Format",
                autoboto.TypeInfo(Format),
            ),
            (
                "register_endpoints",
                "RegisterEndpoints",
                autoboto.TypeInfo(bool),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_url",
                "S3Url",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_name",
                "SegmentName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Sets whether the endpoints create a segment when they are imported.
    define_segment: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # (Deprecated) Your AWS account ID, which you assigned to the ExternalID key
    # in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This
    # requirement is removed, and external IDs are not recommended for IAM roles
    # assumed by Amazon Pinpoint.
    external_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The format of the files that contain the endpoint definitions. Valid
    # values: CSV, JSON
    format: "Format" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Sets whether the endpoints are registered with Amazon Pinpoint when they
    # are imported.
    register_endpoints: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint
    # access to the Amazon S3 location that contains the endpoints to import.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL of the S3 bucket that contains the segment information to import.
    # The location can be a folder or a single file. The URL should use the
    # following format: s3://bucket-name/folder-name/file-name Amazon Pinpoint
    # imports endpoints from this location and any subfolders it contains.
    s3_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the segment to update if the import job is meant to update an
    # existing segment.
    segment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A custom name for the segment created by the import job. Use if
    # DefineSegment is true.
    segment_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ImportJobResource(autoboto.ShapeBase):
    """
    Import job resource
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "define_segment",
                "DefineSegment",
                autoboto.TypeInfo(bool),
            ),
            (
                "external_id",
                "ExternalId",
                autoboto.TypeInfo(str),
            ),
            (
                "format",
                "Format",
                autoboto.TypeInfo(Format),
            ),
            (
                "register_endpoints",
                "RegisterEndpoints",
                autoboto.TypeInfo(bool),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_url",
                "S3Url",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_name",
                "SegmentName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Sets whether the endpoints create a segment when they are imported.
    define_segment: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # (Deprecated) Your AWS account ID, which you assigned to the ExternalID key
    # in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This
    # requirement is removed, and external IDs are not recommended for IAM roles
    # assumed by Amazon Pinpoint.
    external_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The format of the files that contain the endpoint definitions. Valid
    # values: CSV, JSON
    format: "Format" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Sets whether the endpoints are registered with Amazon Pinpoint when they
    # are imported.
    register_endpoints: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint
    # access to the Amazon S3 location that contains the endpoints to import.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL of the S3 bucket that contains the segment information to import.
    # The location can be a folder or a single file. The URL should use the
    # following format: s3://bucket-name/folder-name/file-name Amazon Pinpoint
    # imports endpoints from this location and any subfolders it contains.
    s3_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the segment to update if the import job is meant to update an
    # existing segment.
    segment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A custom name for the segment created by the import job. Use if
    # DefineSegment is true.
    segment_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ImportJobResponse(autoboto.ShapeBase):
    """
    Import job response.
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
                "completed_pieces",
                "CompletedPieces",
                autoboto.TypeInfo(int),
            ),
            (
                "completion_date",
                "CompletionDate",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                autoboto.TypeInfo(ImportJobResource),
            ),
            (
                "failed_pieces",
                "FailedPieces",
                autoboto.TypeInfo(int),
            ),
            (
                "failures",
                "Failures",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                autoboto.TypeInfo(JobStatus),
            ),
            (
                "total_failures",
                "TotalFailures",
                autoboto.TypeInfo(int),
            ),
            (
                "total_pieces",
                "TotalPieces",
                autoboto.TypeInfo(int),
            ),
            (
                "total_processed",
                "TotalProcessed",
                autoboto.TypeInfo(int),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the application to which the import job applies.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of pieces that have successfully imported as of the time of the
    # request.
    completed_pieces: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the import job completed in ISO 8601 format.
    completion_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the import job was created in ISO 8601 format.
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The import job settings.
    definition: "ImportJobResource" = dataclasses.field(default_factory=dict, )

    # The number of pieces that have failed to import as of the time of the
    # request.
    failed_pieces: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Provides up to 100 of the first failed entries for the job, if any exist.
    failures: typing.List[str] = dataclasses.field(default_factory=list, )

    # The unique ID of the import job.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the import job. Valid values: CREATED, INITIALIZING,
    # PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED
    # if one or more pieces failed to import.
    job_status: "JobStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of endpoints that failed to import; for example, because of
    # syntax errors.
    total_failures: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The total number of pieces that must be imported to finish the job. Each
    # piece is an approximately equal portion of the endpoints to import.
    total_pieces: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of endpoints that were processed by the import job.
    total_processed: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The job type. Will be Import.
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ImportJobsResponse(autoboto.ShapeBase):
    """
    Import job list.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                autoboto.TypeInfo(typing.List[ImportJobResponse]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of import jobs for the application.
    item: typing.List["ImportJobResponse"] = dataclasses.field(
        default_factory=list,
    )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class Include(Enum):
    ALL = "ALL"
    ANY = "ANY"
    NONE = "NONE"


@dataclasses.dataclass
class InternalServerErrorException(autoboto.ShapeBase):
    """
    Simple message object.
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
                "request_id",
                "RequestID",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message that's returned from the API.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique message body ID.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ItemResponse(autoboto.ShapeBase):
    """
    The endpoint and events combined response definition
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_item_response",
                "EndpointItemResponse",
                autoboto.TypeInfo(EndpointItemResponse),
            ),
            (
                "events_item_response",
                "EventsItemResponse",
                autoboto.TypeInfo(typing.Dict[str, EventItemResponse]),
            ),
        ]

    # Endpoint item response after endpoint registration
    endpoint_item_response: "EndpointItemResponse" = dataclasses.field(
        default_factory=dict,
    )

    # Events item response is a multipart response object per event Id, with
    # eventId as the key and EventItemResponse object as the value
    events_item_response: typing.Dict[str, "EventItemResponse"
                                     ] = dataclasses.field(
                                         default=autoboto.ShapeBase._NOT_SET,
                                     )


class JobStatus(Enum):
    CREATED = "CREATED"
    INITIALIZING = "INITIALIZING"
    PROCESSING = "PROCESSING"
    COMPLETING = "COMPLETING"
    COMPLETED = "COMPLETED"
    FAILING = "FAILING"
    FAILED = "FAILED"


@dataclasses.dataclass
class Message(autoboto.ShapeBase):
    """
    Message to send
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(Action),
            ),
            (
                "body",
                "Body",
                autoboto.TypeInfo(str),
            ),
            (
                "image_icon_url",
                "ImageIconUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "image_small_icon_url",
                "ImageSmallIconUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "image_url",
                "ImageUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "json_body",
                "JsonBody",
                autoboto.TypeInfo(str),
            ),
            (
                "media_url",
                "MediaUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "raw_content",
                "RawContent",
                autoboto.TypeInfo(str),
            ),
            (
                "silent_push",
                "SilentPush",
                autoboto.TypeInfo(bool),
            ),
            (
                "time_to_live",
                "TimeToLive",
                autoboto.TypeInfo(int),
            ),
            (
                "title",
                "Title",
                autoboto.TypeInfo(str),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
        ]

    # The action that occurs if the user taps a push notification delivered by
    # the campaign: OPEN_APP - Your app launches, or it becomes the foreground
    # app if it has been sent to the background. This is the default action.
    # DEEP_LINK - Uses deep linking features in iOS and Android to open your app
    # and display a designated user interface within the app. URL - The default
    # mobile browser on the user's device launches and opens a web page at the
    # URL you specify.
    action: "Action" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message body. Can include up to 140 characters.
    body: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL that points to the icon image for the push notification icon, for
    # example, the app icon.
    image_icon_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URL that points to the small icon image for the push notification icon,
    # for example, the app icon.
    image_small_icon_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URL that points to an image used in the push notification.
    image_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The JSON payload used for a silent push.
    json_body: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL that points to the media resource, for example a .mp4 or .gif file.
    media_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Raw JSON formatted string to be used as the payload. This value
    # overrides the message.
    raw_content: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Indicates if the message should display on the users device. Silent pushes
    # can be used for Remote Configuration and Phone Home use cases.
    silent_push: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # This parameter specifies how long (in seconds) the message should be kept
    # if the service is unable to deliver the notification the first time. If the
    # value is 0, it treats the notification as if it expires immediately and
    # does not store the notification or attempt to redeliver it. This value is
    # converted to the expiration field when sent to the service. It only applies
    # to APNs and GCM
    time_to_live: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message title that displays above the message on the user's device.
    title: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL to open in the user's mobile browser. Used if the value for Action
    # is URL.
    url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class MessageBody(autoboto.ShapeBase):
    """
    Simple message object.
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
                "request_id",
                "RequestID",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message that's returned from the API.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique message body ID.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class MessageConfiguration(autoboto.ShapeBase):
    """
    Message configuration for a campaign.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "adm_message",
                "ADMMessage",
                autoboto.TypeInfo(Message),
            ),
            (
                "apns_message",
                "APNSMessage",
                autoboto.TypeInfo(Message),
            ),
            (
                "baidu_message",
                "BaiduMessage",
                autoboto.TypeInfo(Message),
            ),
            (
                "default_message",
                "DefaultMessage",
                autoboto.TypeInfo(Message),
            ),
            (
                "email_message",
                "EmailMessage",
                autoboto.TypeInfo(CampaignEmailMessage),
            ),
            (
                "gcm_message",
                "GCMMessage",
                autoboto.TypeInfo(Message),
            ),
            (
                "sms_message",
                "SMSMessage",
                autoboto.TypeInfo(CampaignSmsMessage),
            ),
        ]

    # The message that the campaign delivers to ADM channels. Overrides the
    # default message.
    adm_message: "Message" = dataclasses.field(default_factory=dict, )

    # The message that the campaign delivers to APNS channels. Overrides the
    # default message.
    apns_message: "Message" = dataclasses.field(default_factory=dict, )

    # The message that the campaign delivers to Baidu channels. Overrides the
    # default message.
    baidu_message: "Message" = dataclasses.field(default_factory=dict, )

    # The default message for all channels.
    default_message: "Message" = dataclasses.field(default_factory=dict, )

    # The email message configuration.
    email_message: "CampaignEmailMessage" = dataclasses.field(
        default_factory=dict,
    )

    # The message that the campaign delivers to GCM channels. Overrides the
    # default message.
    gcm_message: "Message" = dataclasses.field(default_factory=dict, )

    # The SMS message configuration.
    sms_message: "CampaignSmsMessage" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class MessageRequest(autoboto.ShapeBase):
    """
    Send message request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "addresses",
                "Addresses",
                autoboto.TypeInfo(typing.Dict[str, AddressConfiguration]),
            ),
            (
                "context",
                "Context",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoints",
                "Endpoints",
                autoboto.TypeInfo(typing.Dict[str, EndpointSendConfiguration]),
            ),
            (
                "message_configuration",
                "MessageConfiguration",
                autoboto.TypeInfo(DirectMessageConfiguration),
            ),
            (
                "trace_id",
                "TraceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A map of key-value pairs, where each key is an address and each value is an
    # AddressConfiguration object. An address can be a push notification token, a
    # phone number, or an email address.
    addresses: typing.Dict[str, "AddressConfiguration"] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A map of custom attributes to attributes to be attached to the message.
    # This payload is added to the push notification's 'data.pinpoint' object or
    # added to the email/sms delivery receipt event attributes.
    context: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A map of key-value pairs, where each key is an endpoint ID and each value
    # is an EndpointSendConfiguration object. Within an EndpointSendConfiguration
    # object, you can tailor the message for an endpoint by specifying message
    # overrides or substitutions.
    endpoints: typing.Dict[str, "EndpointSendConfiguration"
                          ] = dataclasses.field(
                              default=autoboto.ShapeBase._NOT_SET,
                          )

    # Message configuration.
    message_configuration: "DirectMessageConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # A unique ID that you can use to trace a message. This ID is visible to
    # recipients.
    trace_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class MessageResponse(autoboto.ShapeBase):
    """
    Send message response.
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
                "endpoint_result",
                "EndpointResult",
                autoboto.TypeInfo(typing.Dict[str, EndpointMessageResult]),
            ),
            (
                "request_id",
                "RequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "result",
                "Result",
                autoboto.TypeInfo(typing.Dict[str, MessageResult]),
            ),
        ]

    # Application id of the message.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A map containing a multi part response for each address, with the
    # endpointId as the key and the result as the value.
    endpoint_result: typing.Dict[str, "EndpointMessageResult"
                                ] = dataclasses.field(
                                    default=autoboto.ShapeBase._NOT_SET,
                                )

    # Original request Id for which this message was delivered.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A map containing a multi part response for each address, with the address
    # as the key(Email address, phone number or push token) and the result as the
    # value.
    result: typing.Dict[str, "MessageResult"] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class MessageResult(autoboto.ShapeBase):
    """
    The result from sending a message to an address.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_status",
                "DeliveryStatus",
                autoboto.TypeInfo(DeliveryStatus),
            ),
            (
                "message_id",
                "MessageId",
                autoboto.TypeInfo(str),
            ),
            (
                "status_code",
                "StatusCode",
                autoboto.TypeInfo(int),
            ),
            (
                "status_message",
                "StatusMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "updated_token",
                "UpdatedToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The delivery status of the message. Possible values: SUCCESS - The message
    # was successfully delivered to the endpoint. TRANSIENT_FAILURE - A temporary
    # error occurred. Amazon Pinpoint will attempt to deliver the message again
    # later. FAILURE_PERMANENT - An error occurred when delivering the message to
    # the endpoint. Amazon Pinpoint won't attempt to send the message again.
    # TIMEOUT - The message couldn't be sent within the timeout period.
    # QUIET_TIME - The local time for the endpoint was within the Quiet Hours for
    # the campaign. DAILY_CAP - The endpoint has received the maximum number of
    # messages it can receive within a 24-hour period. HOLDOUT - The endpoint was
    # in a hold out treatment for the campaign. THROTTLED - Amazon Pinpoint
    # throttled sending to this endpoint. EXPIRED - The endpoint address is
    # expired. CAMPAIGN_CAP - The endpoint received the maximum number of
    # messages allowed by the campaign. SERVICE_FAILURE - A service-level failure
    # prevented Amazon Pinpoint from delivering the message. UNKNOWN - An unknown
    # error occurred.
    delivery_status: "DeliveryStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Unique message identifier associated with the message that was sent.
    message_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Downstream service status code.
    status_code: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Status message for message delivery.
    status_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If token was updated as part of delivery. (This is GCM Specific)
    updated_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class MessageType(Enum):
    TRANSACTIONAL = "TRANSACTIONAL"
    PROMOTIONAL = "PROMOTIONAL"


@dataclasses.dataclass
class MethodNotAllowedException(autoboto.ShapeBase):
    """
    Simple message object.
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
                "request_id",
                "RequestID",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message that's returned from the API.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique message body ID.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class MetricDimension(autoboto.ShapeBase):
    """
    Custom metric dimension
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comparison_operator",
                "ComparisonOperator",
                autoboto.TypeInfo(str),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(float),
            ),
        ]

    # GREATER_THAN | LESS_THAN | GREATER_THAN_OR_EQUAL | LESS_THAN_OR_EQUAL |
    # EQUAL
    comparison_operator: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Value to be compared.
    value: float = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class Mode(Enum):
    DELIVERY = "DELIVERY"
    FILTER = "FILTER"


@dataclasses.dataclass
class NotFoundException(autoboto.ShapeBase):
    """
    Simple message object.
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
                "request_id",
                "RequestID",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message that's returned from the API.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique message body ID.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class NumberValidateRequest(autoboto.ShapeBase):
    """
    Phone Number Information request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "iso_country_code",
                "IsoCountryCode",
                autoboto.TypeInfo(str),
            ),
            (
                "phone_number",
                "PhoneNumber",
                autoboto.TypeInfo(str),
            ),
        ]

    # (Optional) The two-character ISO country code for the country or region
    # where the phone number was originally registered.
    iso_country_code: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The phone number to get information about. The phone number that you
    # provide should include a country code. If the number doesn't include a
    # valid country code, the operation might result in an error.
    phone_number: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class NumberValidateResponse(autoboto.ShapeBase):
    """
    Phone Number Information response.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "carrier",
                "Carrier",
                autoboto.TypeInfo(str),
            ),
            (
                "city",
                "City",
                autoboto.TypeInfo(str),
            ),
            (
                "cleansed_phone_number_e164",
                "CleansedPhoneNumberE164",
                autoboto.TypeInfo(str),
            ),
            (
                "cleansed_phone_number_national",
                "CleansedPhoneNumberNational",
                autoboto.TypeInfo(str),
            ),
            (
                "country",
                "Country",
                autoboto.TypeInfo(str),
            ),
            (
                "country_code_iso2",
                "CountryCodeIso2",
                autoboto.TypeInfo(str),
            ),
            (
                "country_code_numeric",
                "CountryCodeNumeric",
                autoboto.TypeInfo(str),
            ),
            (
                "county",
                "County",
                autoboto.TypeInfo(str),
            ),
            (
                "original_country_code_iso2",
                "OriginalCountryCodeIso2",
                autoboto.TypeInfo(str),
            ),
            (
                "original_phone_number",
                "OriginalPhoneNumber",
                autoboto.TypeInfo(str),
            ),
            (
                "phone_type",
                "PhoneType",
                autoboto.TypeInfo(str),
            ),
            (
                "phone_type_code",
                "PhoneTypeCode",
                autoboto.TypeInfo(int),
            ),
            (
                "timezone",
                "Timezone",
                autoboto.TypeInfo(str),
            ),
            (
                "zip_code",
                "ZipCode",
                autoboto.TypeInfo(str),
            ),
        ]

    # The carrier or servive provider that the phone number is currently
    # registered with.
    carrier: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The city where the phone number was originally registered.
    city: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The cleansed phone number, shown in E.164 format.
    cleansed_phone_number_e164: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The cleansed phone number, shown in the local phone number format.
    cleansed_phone_number_national: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The country or region where the phone number was originally registered.
    country: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The two-character ISO code for the country or region where the phone number
    # was originally registered.
    country_code_iso2: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The numeric code for the country or region where the phone number was
    # originally registered.
    country_code_numeric: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The county where the phone number was originally registered.
    county: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The two-character ISO code for the country or region that you included in
    # the request body.
    original_country_code_iso2: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The phone number that you included in the request body.
    original_phone_number: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the phone type. Possible values are MOBILE, LANDLINE,
    # VOIP, INVALID, PREPAID, and OTHER.
    phone_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The phone type, represented by an integer. Possible values include 0
    # (MOBILE), 1 (LANDLINE), 2 (VOIP), 3 (INVALID), 4 (OTHER), and 5 (PREPAID).
    phone_type_code: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time zone for the location where the phone number was originally
    # registered.
    timezone: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The postal code for the location where the phone number was originally
    # registered.
    zip_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PhoneNumberValidateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "number_validate_request",
                "NumberValidateRequest",
                autoboto.TypeInfo(NumberValidateRequest),
            ),
        ]

    # Phone Number Information request.
    number_validate_request: "NumberValidateRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PhoneNumberValidateResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "number_validate_response",
                "NumberValidateResponse",
                autoboto.TypeInfo(NumberValidateResponse),
            ),
        ]

    # Phone Number Information response.
    number_validate_response: "NumberValidateResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PublicEndpoint(autoboto.ShapeBase):
    """
    Public endpoint attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address",
                "Address",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "channel_type",
                "ChannelType",
                autoboto.TypeInfo(ChannelType),
            ),
            (
                "demographic",
                "Demographic",
                autoboto.TypeInfo(EndpointDemographic),
            ),
            (
                "effective_date",
                "EffectiveDate",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_status",
                "EndpointStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "location",
                "Location",
                autoboto.TypeInfo(EndpointLocation),
            ),
            (
                "metrics",
                "Metrics",
                autoboto.TypeInfo(typing.Dict[str, float]),
            ),
            (
                "opt_out",
                "OptOut",
                autoboto.TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "user",
                "User",
                autoboto.TypeInfo(EndpointUser),
            ),
        ]

    # The unique identifier for the recipient. For example, an address could be a
    # device token or an endpoint ID.
    address: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Custom attributes that your app reports to Amazon Pinpoint. You can use
    # these attributes as selection criteria when you create a segment.
    attributes: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The channel type. Valid values: APNS, GCM
    channel_type: "ChannelType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The endpoint demographic attributes.
    demographic: "EndpointDemographic" = dataclasses.field(
        default_factory=dict,
    )

    # The date and time when the endpoint was last updated.
    effective_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the endpoint. If the update fails, the value is INACTIVE. If
    # the endpoint is updated successfully, the value is ACTIVE.
    endpoint_status: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The endpoint location attributes.
    location: "EndpointLocation" = dataclasses.field(default_factory=dict, )

    # Custom metrics that your app reports to Amazon Pinpoint.
    metrics: typing.Dict[str, float] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates whether a user has opted out of receiving messages with one of
    # the following values: ALL - User has opted out of all messages. NONE -
    # Users has not opted out and receives all messages.
    opt_out: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A unique identifier that is generated each time the endpoint is updated.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Custom user-specific attributes that your app reports to Amazon Pinpoint.
    user: "EndpointUser" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PutEventStreamRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "write_event_stream",
                "WriteEventStream",
                autoboto.TypeInfo(WriteEventStream),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Request to save an EventStream.
    write_event_stream: "WriteEventStream" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutEventStreamResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_stream",
                "EventStream",
                autoboto.TypeInfo(EventStream),
            ),
        ]

    # Model for an event publishing subscription export.
    event_stream: "EventStream" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PutEventsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "events_request",
                "EventsRequest",
                autoboto.TypeInfo(EventsRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Put Events request
    events_request: "EventsRequest" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PutEventsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "events_response",
                "EventsResponse",
                autoboto.TypeInfo(EventsResponse),
            ),
        ]

    # The results from processing a put events request
    events_response: "EventsResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class QuietTime(autoboto.ShapeBase):
    """
    Quiet Time
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "end",
                "End",
                autoboto.TypeInfo(str),
            ),
            (
                "start",
                "Start",
                autoboto.TypeInfo(str),
            ),
        ]

    # The default end time for quiet time in ISO 8601 format.
    end: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The default start time for quiet time in ISO 8601 format.
    start: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RecencyDimension(autoboto.ShapeBase):
    """
    Define how a segment based on recency of use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(Duration),
            ),
            (
                "recency_type",
                "RecencyType",
                autoboto.TypeInfo(RecencyType),
            ),
        ]

    # The length of time during which users have been active or inactive with
    # your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    duration: "Duration" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The recency dimension type: ACTIVE - Users who have used your app within
    # the specified duration are included in the segment. INACTIVE - Users who
    # have not used your app within the specified duration are included in the
    # segment.
    recency_type: "RecencyType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class RecencyType(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


@dataclasses.dataclass
class RemoveAttributesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "attribute_type",
                "AttributeType",
                autoboto.TypeInfo(str),
            ),
            (
                "update_attributes_request",
                "UpdateAttributesRequest",
                autoboto.TypeInfo(UpdateAttributesRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Type of attribute. Can be endpoint-custom-attributes, endpoint-custom-
    # metrics, endpoint-user-attributes.
    attribute_type: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Update attributes request
    update_attributes_request: "UpdateAttributesRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class RemoveAttributesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes_resource",
                "AttributesResource",
                autoboto.TypeInfo(AttributesResource),
            ),
        ]

    # Attributes.
    attributes_resource: "AttributesResource" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SMSChannelRequest(autoboto.ShapeBase):
    """
    SMS Channel Request
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
                "sender_id",
                "SenderId",
                autoboto.TypeInfo(str),
            ),
            (
                "short_code",
                "ShortCode",
                autoboto.TypeInfo(str),
            ),
        ]

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Sender identifier of your messages.
    sender_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # ShortCode registered with phone provider.
    short_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SMSChannelResponse(autoboto.ShapeBase):
    """
    SMS Channel Response.
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
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                autoboto.TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                autoboto.TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                autoboto.TypeInfo(str),
            ),
            (
                "promotional_messages_per_second",
                "PromotionalMessagesPerSecond",
                autoboto.TypeInfo(int),
            ),
            (
                "sender_id",
                "SenderId",
                autoboto.TypeInfo(str),
            ),
            (
                "short_code",
                "ShortCode",
                autoboto.TypeInfo(str),
            ),
            (
                "transactional_messages_per_second",
                "TransactionalMessagesPerSecond",
                autoboto.TypeInfo(int),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique ID of the application to which the SMS channel belongs.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date that the settings were last updated in ISO 8601 format.
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Channel ID. Not used, only for backwards compatibility.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Is this channel archived
    is_archived: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Who last updated this entry
    last_modified_by: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Last date this was updated
    last_modified_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Platform type. Will be "SMS"
    platform: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Promotional messages per second that can be sent
    promotional_messages_per_second: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Sender identifier of your messages.
    sender_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The short code registered with the phone provider.
    short_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Transactional messages per second that can be sent
    transactional_messages_per_second: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Version of channel
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SMSMessage(autoboto.ShapeBase):
    """
    SMS Message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body",
                "Body",
                autoboto.TypeInfo(str),
            ),
            (
                "keyword",
                "Keyword",
                autoboto.TypeInfo(str),
            ),
            (
                "message_type",
                "MessageType",
                autoboto.TypeInfo(MessageType),
            ),
            (
                "origination_number",
                "OriginationNumber",
                autoboto.TypeInfo(str),
            ),
            (
                "sender_id",
                "SenderId",
                autoboto.TypeInfo(str),
            ),
            (
                "substitutions",
                "Substitutions",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
        ]

    # The body of the SMS message.
    body: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The SMS program name that you provided to AWS Support when you requested
    # your dedicated number.
    keyword: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Is this a transaction priority message or lower priority.
    message_type: "MessageType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The phone number that the SMS message originates from. Specify one of the
    # dedicated long codes or short codes that you requested from AWS Support and
    # that is assigned to your account. If this attribute is not specified,
    # Amazon Pinpoint randomly assigns a long code.
    origination_number: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The sender ID that is shown as the message sender on the recipient's
    # device. Support for sender IDs varies by country or region.
    sender_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Default message substitutions. Can be overridden by individual address
    # substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Schedule(autoboto.ShapeBase):
    """
    Shcedule that defines when a campaign is run.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "end_time",
                "EndTime",
                autoboto.TypeInfo(str),
            ),
            (
                "frequency",
                "Frequency",
                autoboto.TypeInfo(Frequency),
            ),
            (
                "is_local_time",
                "IsLocalTime",
                autoboto.TypeInfo(bool),
            ),
            (
                "quiet_time",
                "QuietTime",
                autoboto.TypeInfo(QuietTime),
            ),
            (
                "start_time",
                "StartTime",
                autoboto.TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                autoboto.TypeInfo(str),
            ),
        ]

    # The scheduled time that the campaign ends in ISO 8601 format.
    end_time: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # How often the campaign delivers messages. Valid values: ONCE, HOURLY,
    # DAILY, WEEKLY, MONTHLY
    frequency: "Frequency" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates whether the campaign schedule takes effect according to each
    # user's local time.
    is_local_time: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time during which the campaign sends no messages.
    quiet_time: "QuietTime" = dataclasses.field(default_factory=dict, )

    # The scheduled time that the campaign begins in ISO 8601 format.
    start_time: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The starting UTC offset for the schedule if the value for isLocalTime is
    # true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30
    # UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30
    # UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06
    # UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    timezone: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SegmentBehaviors(autoboto.ShapeBase):
    """
    Segment behavior dimensions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "recency",
                "Recency",
                autoboto.TypeInfo(RecencyDimension),
            ),
        ]

    # The recency of use.
    recency: "RecencyDimension" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class SegmentDemographics(autoboto.ShapeBase):
    """
    Segment demographic dimensions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "app_version",
                "AppVersion",
                autoboto.TypeInfo(SetDimension),
            ),
            (
                "channel",
                "Channel",
                autoboto.TypeInfo(SetDimension),
            ),
            (
                "device_type",
                "DeviceType",
                autoboto.TypeInfo(SetDimension),
            ),
            (
                "make",
                "Make",
                autoboto.TypeInfo(SetDimension),
            ),
            (
                "model",
                "Model",
                autoboto.TypeInfo(SetDimension),
            ),
            (
                "platform",
                "Platform",
                autoboto.TypeInfo(SetDimension),
            ),
        ]

    # The app version criteria for the segment.
    app_version: "SetDimension" = dataclasses.field(default_factory=dict, )

    # The channel criteria for the segment.
    channel: "SetDimension" = dataclasses.field(default_factory=dict, )

    # The device type criteria for the segment.
    device_type: "SetDimension" = dataclasses.field(default_factory=dict, )

    # The device make criteria for the segment.
    make: "SetDimension" = dataclasses.field(default_factory=dict, )

    # The device model criteria for the segment.
    model: "SetDimension" = dataclasses.field(default_factory=dict, )

    # The device platform criteria for the segment.
    platform: "SetDimension" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class SegmentDimensions(autoboto.ShapeBase):
    """
    Segment dimensions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[str, AttributeDimension]),
            ),
            (
                "behavior",
                "Behavior",
                autoboto.TypeInfo(SegmentBehaviors),
            ),
            (
                "demographic",
                "Demographic",
                autoboto.TypeInfo(SegmentDemographics),
            ),
            (
                "location",
                "Location",
                autoboto.TypeInfo(SegmentLocation),
            ),
            (
                "metrics",
                "Metrics",
                autoboto.TypeInfo(typing.Dict[str, MetricDimension]),
            ),
            (
                "user_attributes",
                "UserAttributes",
                autoboto.TypeInfo(typing.Dict[str, AttributeDimension]),
            ),
        ]

    # Custom segment attributes.
    attributes: typing.Dict[str, "AttributeDimension"] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The segment behaviors attributes.
    behavior: "SegmentBehaviors" = dataclasses.field(default_factory=dict, )

    # The segment demographics attributes.
    demographic: "SegmentDemographics" = dataclasses.field(
        default_factory=dict,
    )

    # The segment location attributes.
    location: "SegmentLocation" = dataclasses.field(default_factory=dict, )

    # Custom segment metrics.
    metrics: typing.Dict[str, "MetricDimension"] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Custom segment user attributes.
    user_attributes: typing.Dict[str, "AttributeDimension"] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SegmentGroup(autoboto.ShapeBase):
    """
    Segment group definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dimensions",
                "Dimensions",
                autoboto.TypeInfo(typing.List[SegmentDimensions]),
            ),
            (
                "source_segments",
                "SourceSegments",
                autoboto.TypeInfo(typing.List[SegmentReference]),
            ),
            (
                "source_type",
                "SourceType",
                autoboto.TypeInfo(SourceType),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(Type),
            ),
        ]

    # List of dimensions to include or exclude.
    dimensions: typing.List["SegmentDimensions"] = dataclasses.field(
        default_factory=list,
    )

    # The base segment that you build your segment on. The source segment defines
    # the starting "universe" of endpoints. When you add dimensions to the
    # segment, it filters the source segment based on the dimensions that you
    # specify. You can specify more than one dimensional segment. You can only
    # specify one imported segment.
    source_segments: typing.List["SegmentReference"] = dataclasses.field(
        default_factory=list,
    )

    # Specify how to handle multiple source segments. For example, if you specify
    # three source segments, should the resulting segment be based on any or all
    # of the segments? Acceptable values: ANY or ALL.
    source_type: "SourceType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specify how to handle multiple segment dimensions. For example, if you
    # specify three dimensions, should the resulting segment include endpoints
    # that are matched by all, any, or none of the dimensions? Acceptable values:
    # ALL, ANY, or NONE.
    type: "Type" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SegmentGroupList(autoboto.ShapeBase):
    """
    Segment group definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "groups",
                "Groups",
                autoboto.TypeInfo(typing.List[SegmentGroup]),
            ),
            (
                "include",
                "Include",
                autoboto.TypeInfo(Include),
            ),
        ]

    # A set of segment criteria to evaluate.
    groups: typing.List["SegmentGroup"] = dataclasses.field(
        default_factory=list,
    )

    # Specify how to handle multiple segment groups. For example, if the segment
    # includes three segment groups, should the resulting segment include
    # endpoints that are matched by all, any, or none of the segment groups you
    # created. Acceptable values: ALL, ANY, or NONE.
    include: "Include" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SegmentImportResource(autoboto.ShapeBase):
    """
    Segment import definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_counts",
                "ChannelCounts",
                autoboto.TypeInfo(typing.Dict[str, int]),
            ),
            (
                "external_id",
                "ExternalId",
                autoboto.TypeInfo(str),
            ),
            (
                "format",
                "Format",
                autoboto.TypeInfo(Format),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_url",
                "S3Url",
                autoboto.TypeInfo(str),
            ),
            (
                "size",
                "Size",
                autoboto.TypeInfo(int),
            ),
        ]

    # The number of channel types in the imported segment.
    channel_counts: typing.Dict[str, int] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # (Deprecated) Your AWS account ID, which you assigned to the ExternalID key
    # in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This
    # requirement is removed, and external IDs are not recommended for IAM roles
    # assumed by Amazon Pinpoint.
    external_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The format of the endpoint files that were imported to create this segment.
    # Valid values: CSV, JSON
    format: "Format" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint
    # access to the endpoints in Amazon S3.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL of the S3 bucket that the segment was imported from.
    s3_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of endpoints that were successfully imported to create this
    # segment.
    size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SegmentLocation(autoboto.ShapeBase):
    """
    Segment location dimensions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "country",
                "Country",
                autoboto.TypeInfo(SetDimension),
            ),
            (
                "gps_point",
                "GPSPoint",
                autoboto.TypeInfo(GPSPointDimension),
            ),
        ]

    # The country filter according to ISO 3166-1 Alpha-2 codes.
    country: "SetDimension" = dataclasses.field(default_factory=dict, )

    # The GPS Point dimension.
    gps_point: "GPSPointDimension" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class SegmentReference(autoboto.ShapeBase):
    """
    Segment reference.
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
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
        ]

    # A unique identifier for the segment.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If specified contains a specific version of the segment included.
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SegmentResponse(autoboto.ShapeBase):
    """
    Segment definition.
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
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "dimensions",
                "Dimensions",
                autoboto.TypeInfo(SegmentDimensions),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "import_definition",
                "ImportDefinition",
                autoboto.TypeInfo(SegmentImportResource),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_groups",
                "SegmentGroups",
                autoboto.TypeInfo(SegmentGroupList),
            ),
            (
                "segment_type",
                "SegmentType",
                autoboto.TypeInfo(SegmentType),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the application that the segment applies to.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time when the segment was created.
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The segment dimensions attributes.
    dimensions: "SegmentDimensions" = dataclasses.field(default_factory=dict, )

    # The unique segment ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The import job settings.
    import_definition: "SegmentImportResource" = dataclasses.field(
        default_factory=dict,
    )

    # The date and time when the segment was last modified.
    last_modified_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the segment.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A segment group, which consists of zero or more source segments, plus
    # dimensions that are applied to those source segments.
    segment_groups: "SegmentGroupList" = dataclasses.field(
        default_factory=dict,
    )

    # The segment type: DIMENSIONAL - A dynamic segment built from selection
    # criteria based on endpoint data reported by your app. You create this type
    # of segment by using the segment builder in the Amazon Pinpoint console or
    # by making a POST request to the segments resource. IMPORT - A static
    # segment built from an imported set of endpoint definitions. You create this
    # type of segment by importing a segment in the Amazon Pinpoint console or by
    # making a POST request to the jobs/import resource.
    segment_type: "SegmentType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The segment version number.
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class SegmentType(Enum):
    DIMENSIONAL = "DIMENSIONAL"
    IMPORT = "IMPORT"


@dataclasses.dataclass
class SegmentsResponse(autoboto.ShapeBase):
    """
    Segments in your account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                autoboto.TypeInfo(typing.List[SegmentResponse]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of segments.
    item: typing.List["SegmentResponse"] = dataclasses.field(
        default_factory=list,
    )

    # An identifier used to retrieve the next page of results. The token is null
    # if no additional pages exist.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SendMessagesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "message_request",
                "MessageRequest",
                autoboto.TypeInfo(MessageRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Send message request.
    message_request: "MessageRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SendMessagesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message_response",
                "MessageResponse",
                autoboto.TypeInfo(MessageResponse),
            ),
        ]

    # Send message response.
    message_response: "MessageResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SendUsersMessageRequest(autoboto.ShapeBase):
    """
    Send message request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "context",
                "Context",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "message_configuration",
                "MessageConfiguration",
                autoboto.TypeInfo(DirectMessageConfiguration),
            ),
            (
                "trace_id",
                "TraceId",
                autoboto.TypeInfo(str),
            ),
            (
                "users",
                "Users",
                autoboto.TypeInfo(typing.Dict[str, EndpointSendConfiguration]),
            ),
        ]

    # A map of custom attribute-value pairs. Amazon Pinpoint adds these
    # attributes to the data.pinpoint object in the body of the push notification
    # payload. Amazon Pinpoint also provides these attributes in the events that
    # it generates for users-messages deliveries.
    context: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Message definitions for the default message and any messages that are
    # tailored for specific channels.
    message_configuration: "DirectMessageConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # A unique ID that you can use to trace a message. This ID is visible to
    # recipients.
    trace_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A map that associates user IDs with EndpointSendConfiguration objects.
    # Within an EndpointSendConfiguration object, you can tailor the message for
    # a user by specifying message overrides or substitutions.
    users: typing.Dict[str, "EndpointSendConfiguration"] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SendUsersMessageResponse(autoboto.ShapeBase):
    """
    User send message response.
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
                "request_id",
                "RequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "result",
                "Result",
                autoboto.TypeInfo(
                    typing.Dict[str, typing.Dict[str, EndpointMessageResult]]
                ),
            ),
        ]

    # The unique ID of the Amazon Pinpoint project used to send the message.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID assigned to the users-messages request.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An object that shows the endpoints that were messaged for each user. The
    # object provides a list of user IDs. For each user ID, it provides the
    # endpoint IDs that were messaged. For each endpoint ID, it provides an
    # EndpointMessageResult object.
    result: typing.Dict[str, typing.Dict[str, "EndpointMessageResult"]
                       ] = dataclasses.field(
                           default=autoboto.ShapeBase._NOT_SET,
                       )


@dataclasses.dataclass
class SendUsersMessagesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "send_users_message_request",
                "SendUsersMessageRequest",
                autoboto.TypeInfo(SendUsersMessageRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Send message request.
    send_users_message_request: "SendUsersMessageRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SendUsersMessagesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "send_users_message_response",
                "SendUsersMessageResponse",
                autoboto.TypeInfo(SendUsersMessageResponse),
            ),
        ]

    # User send message response.
    send_users_message_response: "SendUsersMessageResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class Session(autoboto.ShapeBase):
    """
    Information about a session.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(int),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "start_timestamp",
                "StartTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "stop_timestamp",
                "StopTimestamp",
                autoboto.TypeInfo(str),
            ),
        ]

    # Session duration in millis
    duration: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A unique identifier for the session.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date and time when the session began.
    start_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time when the session ended.
    stop_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SetDimension(autoboto.ShapeBase):
    """
    Dimension specification of a segment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dimension_type",
                "DimensionType",
                autoboto.TypeInfo(DimensionType),
            ),
            (
                "values",
                "Values",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The type of dimension: INCLUSIVE - Endpoints that match the criteria are
    # included in the segment. EXCLUSIVE - Endpoints that match the criteria are
    # excluded from the segment.
    dimension_type: "DimensionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The criteria values for the segment dimension. Endpoints with matching
    # attribute values are included or excluded from the segment, depending on
    # the setting for Type.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


class SourceType(Enum):
    ALL = "ALL"
    ANY = "ANY"
    NONE = "NONE"


@dataclasses.dataclass
class TooManyRequestsException(autoboto.ShapeBase):
    """
    Simple message object.
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
                "request_id",
                "RequestID",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message that's returned from the API.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique message body ID.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TreatmentResource(autoboto.ShapeBase):
    """
    Treatment resource
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
                "message_configuration",
                "MessageConfiguration",
                autoboto.TypeInfo(MessageConfiguration),
            ),
            (
                "schedule",
                "Schedule",
                autoboto.TypeInfo(Schedule),
            ),
            (
                "size_percent",
                "SizePercent",
                autoboto.TypeInfo(int),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(CampaignState),
            ),
            (
                "treatment_description",
                "TreatmentDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "treatment_name",
                "TreatmentName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique treatment ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message configuration settings.
    message_configuration: "MessageConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The campaign schedule.
    schedule: "Schedule" = dataclasses.field(default_factory=dict, )

    # The allocated percentage of users for this treatment.
    size_percent: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The treatment status.
    state: "CampaignState" = dataclasses.field(default_factory=dict, )

    # A custom description for the treatment.
    treatment_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The custom name of a variation of the campaign used for A/B testing.
    treatment_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class Type(Enum):
    ALL = "ALL"
    ANY = "ANY"
    NONE = "NONE"


@dataclasses.dataclass
class UpdateAdmChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "adm_channel_request",
                "ADMChannelRequest",
                autoboto.TypeInfo(ADMChannelRequest),
            ),
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Amazon Device Messaging channel definition.
    adm_channel_request: "ADMChannelRequest" = dataclasses.field(
        default_factory=dict,
    )

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateAdmChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "adm_channel_response",
                "ADMChannelResponse",
                autoboto.TypeInfo(ADMChannelResponse),
            ),
        ]

    # Amazon Device Messaging channel definition.
    adm_channel_response: "ADMChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateApnsChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_channel_request",
                "APNSChannelRequest",
                autoboto.TypeInfo(APNSChannelRequest),
            ),
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Apple Push Notification Service channel definition.
    apns_channel_request: "APNSChannelRequest" = dataclasses.field(
        default_factory=dict,
    )

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateApnsChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_channel_response",
                "APNSChannelResponse",
                autoboto.TypeInfo(APNSChannelResponse),
            ),
        ]

    # Apple Distribution Push Notification Service channel definition.
    apns_channel_response: "APNSChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateApnsSandboxChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_sandbox_channel_request",
                "APNSSandboxChannelRequest",
                autoboto.TypeInfo(APNSSandboxChannelRequest),
            ),
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Apple Development Push Notification Service channel definition.
    apns_sandbox_channel_request: "APNSSandboxChannelRequest" = dataclasses.field(
        default_factory=dict,
    )

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateApnsSandboxChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_sandbox_channel_response",
                "APNSSandboxChannelResponse",
                autoboto.TypeInfo(APNSSandboxChannelResponse),
            ),
        ]

    # Apple Development Push Notification Service channel definition.
    apns_sandbox_channel_response: "APNSSandboxChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateApnsVoipChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_voip_channel_request",
                "APNSVoipChannelRequest",
                autoboto.TypeInfo(APNSVoipChannelRequest),
            ),
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Apple VoIP Push Notification Service channel definition.
    apns_voip_channel_request: "APNSVoipChannelRequest" = dataclasses.field(
        default_factory=dict,
    )

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateApnsVoipChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_voip_channel_response",
                "APNSVoipChannelResponse",
                autoboto.TypeInfo(APNSVoipChannelResponse),
            ),
        ]

    # Apple VoIP Push Notification Service channel definition.
    apns_voip_channel_response: "APNSVoipChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateApnsVoipSandboxChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_voip_sandbox_channel_request",
                "APNSVoipSandboxChannelRequest",
                autoboto.TypeInfo(APNSVoipSandboxChannelRequest),
            ),
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Apple VoIP Developer Push Notification Service channel definition.
    apns_voip_sandbox_channel_request: "APNSVoipSandboxChannelRequest" = dataclasses.field(
        default_factory=dict,
    )

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateApnsVoipSandboxChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_voip_sandbox_channel_response",
                "APNSVoipSandboxChannelResponse",
                autoboto.TypeInfo(APNSVoipSandboxChannelResponse),
            ),
        ]

    # Apple VoIP Developer Push Notification Service channel definition.
    apns_voip_sandbox_channel_response: "APNSVoipSandboxChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateApplicationSettingsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "write_application_settings_request",
                "WriteApplicationSettingsRequest",
                autoboto.TypeInfo(WriteApplicationSettingsRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Creating application setting request
    write_application_settings_request: "WriteApplicationSettingsRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateApplicationSettingsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_settings_resource",
                "ApplicationSettingsResource",
                autoboto.TypeInfo(ApplicationSettingsResource),
            ),
        ]

    # Application settings.
    application_settings_resource: "ApplicationSettingsResource" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateAttributesRequest(autoboto.ShapeBase):
    """
    Update attributes request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "blacklist",
                "Blacklist",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The GLOB wildcard for removing the attributes in the application
    blacklist: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UpdateBaiduChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "baidu_channel_request",
                "BaiduChannelRequest",
                autoboto.TypeInfo(BaiduChannelRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Baidu Cloud Push credentials
    baidu_channel_request: "BaiduChannelRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateBaiduChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baidu_channel_response",
                "BaiduChannelResponse",
                autoboto.TypeInfo(BaiduChannelResponse),
            ),
        ]

    # Baidu Cloud Messaging channel definition
    baidu_channel_response: "BaiduChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateCampaignRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "campaign_id",
                "CampaignId",
                autoboto.TypeInfo(str),
            ),
            (
                "write_campaign_request",
                "WriteCampaignRequest",
                autoboto.TypeInfo(WriteCampaignRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the campaign.
    campaign_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Used to create a campaign.
    write_campaign_request: "WriteCampaignRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateCampaignResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "campaign_response",
                "CampaignResponse",
                autoboto.TypeInfo(CampaignResponse),
            ),
        ]

    # Campaign definition
    campaign_response: "CampaignResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateEmailChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "email_channel_request",
                "EmailChannelRequest",
                autoboto.TypeInfo(EmailChannelRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Email Channel Request
    email_channel_request: "EmailChannelRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateEmailChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "email_channel_response",
                "EmailChannelResponse",
                autoboto.TypeInfo(EmailChannelResponse),
            ),
        ]

    # Email Channel Response.
    email_channel_response: "EmailChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateEndpointRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_id",
                "EndpointId",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_request",
                "EndpointRequest",
                autoboto.TypeInfo(EndpointRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the endpoint.
    endpoint_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Endpoint update request
    endpoint_request: "EndpointRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateEndpointResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message_body",
                "MessageBody",
                autoboto.TypeInfo(MessageBody),
            ),
        ]

    # Simple message object.
    message_body: "MessageBody" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateEndpointsBatchRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_batch_request",
                "EndpointBatchRequest",
                autoboto.TypeInfo(EndpointBatchRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Endpoint batch update request.
    endpoint_batch_request: "EndpointBatchRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateEndpointsBatchResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message_body",
                "MessageBody",
                autoboto.TypeInfo(MessageBody),
            ),
        ]

    # Simple message object.
    message_body: "MessageBody" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateGcmChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "gcm_channel_request",
                "GCMChannelRequest",
                autoboto.TypeInfo(GCMChannelRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Google Cloud Messaging credentials
    gcm_channel_request: "GCMChannelRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateGcmChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gcm_channel_response",
                "GCMChannelResponse",
                autoboto.TypeInfo(GCMChannelResponse),
            ),
        ]

    # Google Cloud Messaging channel definition
    gcm_channel_response: "GCMChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateSegmentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "write_segment_request",
                "WriteSegmentRequest",
                autoboto.TypeInfo(WriteSegmentRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the segment.
    segment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Segment definition.
    write_segment_request: "WriteSegmentRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateSegmentResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "segment_response",
                "SegmentResponse",
                autoboto.TypeInfo(SegmentResponse),
            ),
        ]

    # Segment definition.
    segment_response: "SegmentResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateSmsChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "sms_channel_request",
                "SMSChannelRequest",
                autoboto.TypeInfo(SMSChannelRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # SMS Channel Request
    sms_channel_request: "SMSChannelRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateSmsChannelResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sms_channel_response",
                "SMSChannelResponse",
                autoboto.TypeInfo(SMSChannelResponse),
            ),
        ]

    # SMS Channel Response.
    sms_channel_response: "SMSChannelResponse" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class WriteApplicationSettingsRequest(autoboto.ShapeBase):
    """
    Creating application setting request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "campaign_hook",
                "CampaignHook",
                autoboto.TypeInfo(CampaignHook),
            ),
            (
                "cloud_watch_metrics_enabled",
                "CloudWatchMetricsEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "limits",
                "Limits",
                autoboto.TypeInfo(CampaignLimits),
            ),
            (
                "quiet_time",
                "QuietTime",
                autoboto.TypeInfo(QuietTime),
            ),
        ]

    # Default campaign hook information.
    campaign_hook: "CampaignHook" = dataclasses.field(default_factory=dict, )

    # The CloudWatchMetrics settings for the app.
    cloud_watch_metrics_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default campaign limits for the app. These limits apply to each
    # campaign for the app, unless the campaign overrides the default with limits
    # of its own.
    limits: "CampaignLimits" = dataclasses.field(default_factory=dict, )

    # The default quiet time for the app. Each campaign for this app sends no
    # messages during this time unless the campaign overrides the default with a
    # quiet time of its own.
    quiet_time: "QuietTime" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class WriteCampaignRequest(autoboto.ShapeBase):
    """
    Used to create a campaign.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "additional_treatments",
                "AdditionalTreatments",
                autoboto.TypeInfo(typing.List[WriteTreatmentResource]),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "holdout_percent",
                "HoldoutPercent",
                autoboto.TypeInfo(int),
            ),
            (
                "hook",
                "Hook",
                autoboto.TypeInfo(CampaignHook),
            ),
            (
                "is_paused",
                "IsPaused",
                autoboto.TypeInfo(bool),
            ),
            (
                "limits",
                "Limits",
                autoboto.TypeInfo(CampaignLimits),
            ),
            (
                "message_configuration",
                "MessageConfiguration",
                autoboto.TypeInfo(MessageConfiguration),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                autoboto.TypeInfo(Schedule),
            ),
            (
                "segment_id",
                "SegmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_version",
                "SegmentVersion",
                autoboto.TypeInfo(int),
            ),
            (
                "treatment_description",
                "TreatmentDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "treatment_name",
                "TreatmentName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Treatments that are defined in addition to the default treatment.
    additional_treatments: typing.List["WriteTreatmentResource"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )

    # A description of the campaign.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The allocated percentage of end users who will not receive messages from
    # this campaign.
    holdout_percent: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Campaign hook information.
    hook: "CampaignHook" = dataclasses.field(default_factory=dict, )

    # Indicates whether the campaign is paused. A paused campaign does not send
    # messages unless you resume it by setting IsPaused to false.
    is_paused: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The campaign limits settings.
    limits: "CampaignLimits" = dataclasses.field(default_factory=dict, )

    # The message configuration settings.
    message_configuration: "MessageConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The custom name of the campaign.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The campaign schedule.
    schedule: "Schedule" = dataclasses.field(default_factory=dict, )

    # The ID of the segment to which the campaign sends messages.
    segment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the segment to which the campaign sends messages.
    segment_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A custom description for the treatment.
    treatment_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The custom name of a variation of the campaign used for A/B testing.
    treatment_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class WriteEventStream(autoboto.ShapeBase):
    """
    Request to save an EventStream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_stream_arn",
                "DestinationStreamArn",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose
    # delivery stream to which you want to publish events. Firehose ARN:
    # arn:aws:firehose:REGION:ACCOUNT_ID:deliverystream/STREAM_NAME Kinesis ARN:
    # arn:aws:kinesis:REGION:ACCOUNT_ID:stream/STREAM_NAME
    destination_stream_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IAM role that authorizes Amazon Pinpoint to publish events to the
    # stream in your account.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WriteSegmentRequest(autoboto.ShapeBase):
    """
    Segment definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dimensions",
                "Dimensions",
                autoboto.TypeInfo(SegmentDimensions),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_groups",
                "SegmentGroups",
                autoboto.TypeInfo(SegmentGroupList),
            ),
        ]

    # The segment dimensions attributes.
    dimensions: "SegmentDimensions" = dataclasses.field(default_factory=dict, )

    # The name of segment
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A segment group, which consists of zero or more source segments, plus
    # dimensions that are applied to those source segments. Your request can only
    # include one segment group. Your request can include either a SegmentGroups
    # object or a Dimensions object, but not both.
    segment_groups: "SegmentGroupList" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class WriteTreatmentResource(autoboto.ShapeBase):
    """
    Used to create a campaign treatment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message_configuration",
                "MessageConfiguration",
                autoboto.TypeInfo(MessageConfiguration),
            ),
            (
                "schedule",
                "Schedule",
                autoboto.TypeInfo(Schedule),
            ),
            (
                "size_percent",
                "SizePercent",
                autoboto.TypeInfo(int),
            ),
            (
                "treatment_description",
                "TreatmentDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "treatment_name",
                "TreatmentName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The message configuration settings.
    message_configuration: "MessageConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The campaign schedule.
    schedule: "Schedule" = dataclasses.field(default_factory=dict, )

    # The allocated percentage of users for this treatment.
    size_percent: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A custom description for the treatment.
    treatment_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The custom name of a variation of the campaign used for A/B testing.
    treatment_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
