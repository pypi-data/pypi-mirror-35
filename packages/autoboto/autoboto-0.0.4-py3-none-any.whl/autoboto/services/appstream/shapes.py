import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


class Action(Enum):
    CLIPBOARD_COPY_FROM_LOCAL_DEVICE = "CLIPBOARD_COPY_FROM_LOCAL_DEVICE"
    CLIPBOARD_COPY_TO_LOCAL_DEVICE = "CLIPBOARD_COPY_TO_LOCAL_DEVICE"
    FILE_UPLOAD = "FILE_UPLOAD"
    FILE_DOWNLOAD = "FILE_DOWNLOAD"
    PRINTING_TO_LOCAL_DEVICE = "PRINTING_TO_LOCAL_DEVICE"


@dataclasses.dataclass
class Application(autoboto.ShapeBase):
    """
    Describes an application in the application catalog.
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
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "icon_url",
                "IconURL",
                autoboto.TypeInfo(str),
            ),
            (
                "launch_path",
                "LaunchPath",
                autoboto.TypeInfo(str),
            ),
            (
                "launch_parameters",
                "LaunchParameters",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "metadata",
                "Metadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the application.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The application name for display.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The URL for the application icon. This URL might be time-limited.
    icon_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The path to the application executable in the instance.
    launch_path: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The arguments that are passed to the application at launch.
    launch_parameters: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If there is a problem, the application can be disabled after image
    # creation.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Additional attributes that describe the application.
    metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociateFleetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_name",
                "FleetName",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_name",
                "StackName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the fleet.
    fleet_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the stack.
    stack_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateFleetResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


class AuthenticationType(Enum):
    API = "API"
    SAML = "SAML"
    USERPOOL = "USERPOOL"


@dataclasses.dataclass
class ComputeCapacity(autoboto.ShapeBase):
    """
    Describes the capacity for a fleet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "desired_instances",
                "DesiredInstances",
                autoboto.TypeInfo(int),
            ),
        ]

    # The desired number of streaming instances.
    desired_instances: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ComputeCapacityStatus(autoboto.ShapeBase):
    """
    Describes the capacity status for a fleet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "desired",
                "Desired",
                autoboto.TypeInfo(int),
            ),
            (
                "running",
                "Running",
                autoboto.TypeInfo(int),
            ),
            (
                "in_use",
                "InUse",
                autoboto.TypeInfo(int),
            ),
            (
                "available",
                "Available",
                autoboto.TypeInfo(int),
            ),
        ]

    # The desired number of streaming instances.
    desired: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total number of simultaneous streaming instances that are running.
    running: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances in use for streaming.
    in_use: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of currently available instances that can be used to stream
    # sessions.
    available: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConcurrentModificationException(autoboto.ShapeBase):
    """
    An API error occurred. Wait a few minutes and try again.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CopyImageRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_image_name",
                "SourceImageName",
                autoboto.TypeInfo(str),
            ),
            (
                "destination_image_name",
                "DestinationImageName",
                autoboto.TypeInfo(str),
            ),
            (
                "destination_region",
                "DestinationRegion",
                autoboto.TypeInfo(str),
            ),
            (
                "destination_image_description",
                "DestinationImageDescription",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the image to copy.
    source_image_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name that the image will have when it is copied to the destination.
    destination_image_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The destination region to which the image will be copied. This parameter is
    # required, even if you are copying an image within the same region.
    destination_region: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description that the image will have when it is copied to the
    # destination.
    destination_image_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CopyImageResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_image_name",
                "DestinationImageName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the destination image.
    destination_image_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDirectoryConfigRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_name",
                "DirectoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "organizational_unit_distinguished_names",
                "OrganizationalUnitDistinguishedNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "service_account_credentials",
                "ServiceAccountCredentials",
                autoboto.TypeInfo(ServiceAccountCredentials),
            ),
        ]

    # The fully qualified name of the directory (for example, corp.example.com).
    directory_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The distinguished names of the organizational units for computer accounts.
    organizational_unit_distinguished_names: typing.List[
        str
    ] = dataclasses.field(
        default_factory=list,
    )

    # The credentials for the service account used by the streaming instance to
    # connect to the directory.
    service_account_credentials: "ServiceAccountCredentials" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateDirectoryConfigResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_config",
                "DirectoryConfig",
                autoboto.TypeInfo(DirectoryConfig),
            ),
        ]

    # Information about the directory configuration.
    directory_config: "DirectoryConfig" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateFleetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                autoboto.TypeInfo(str),
            ),
            (
                "compute_capacity",
                "ComputeCapacity",
                autoboto.TypeInfo(ComputeCapacity),
            ),
            (
                "image_name",
                "ImageName",
                autoboto.TypeInfo(str),
            ),
            (
                "image_arn",
                "ImageArn",
                autoboto.TypeInfo(str),
            ),
            (
                "fleet_type",
                "FleetType",
                autoboto.TypeInfo(FleetType),
            ),
            (
                "vpc_config",
                "VpcConfig",
                autoboto.TypeInfo(VpcConfig),
            ),
            (
                "max_user_duration_in_seconds",
                "MaxUserDurationInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "disconnect_timeout_in_seconds",
                "DisconnectTimeoutInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "enable_default_internet_access",
                "EnableDefaultInternetAccess",
                autoboto.TypeInfo(bool),
            ),
            (
                "domain_join_info",
                "DomainJoinInfo",
                autoboto.TypeInfo(DomainJoinInfo),
            ),
        ]

    # A unique name for the fleet.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance type to use when launching fleet instances. The following
    # instance types are available:

    #   * stream.standard.medium

    #   * stream.standard.large

    #   * stream.compute.large

    #   * stream.compute.xlarge

    #   * stream.compute.2xlarge

    #   * stream.compute.4xlarge

    #   * stream.compute.8xlarge

    #   * stream.memory.large

    #   * stream.memory.xlarge

    #   * stream.memory.2xlarge

    #   * stream.memory.4xlarge

    #   * stream.memory.8xlarge

    #   * stream.graphics-design.large

    #   * stream.graphics-design.xlarge

    #   * stream.graphics-design.2xlarge

    #   * stream.graphics-design.4xlarge

    #   * stream.graphics-desktop.2xlarge

    #   * stream.graphics-pro.4xlarge

    #   * stream.graphics-pro.8xlarge

    #   * stream.graphics-pro.16xlarge
    instance_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The desired capacity for the fleet.
    compute_capacity: "ComputeCapacity" = dataclasses.field(
        default_factory=dict,
    )

    # The name of the image used to create the fleet.
    image_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the public, private, or shared image to use.
    image_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The fleet type.

    # ALWAYS_ON

    # Provides users with instant-on access to their apps. You are charged for
    # all running instances in your fleet, even if no users are streaming apps.

    # ON_DEMAND

    # Provide users with access to applications after they connect, which takes
    # one to two minutes. You are charged for instance streaming when users are
    # connected and a small hourly fee for instances that are not streaming apps.
    fleet_type: "FleetType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The VPC configuration for the fleet.
    vpc_config: "VpcConfig" = dataclasses.field(default_factory=dict, )

    # The maximum time that a streaming session can run, in seconds. Specify a
    # value between 600 and 57600.
    max_user_duration_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time after disconnection when a session is considered to have ended, in
    # seconds. If a user who was disconnected reconnects within this time
    # interval, the user is connected to their previous session. Specify a value
    # between 60 and 57600.
    disconnect_timeout_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description for display.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The fleet name for display.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Enables or disables default internet access for the fleet.
    enable_default_internet_access: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The information needed to join a Microsoft Active Directory domain.
    domain_join_info: "DomainJoinInfo" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateFleetResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet",
                "Fleet",
                autoboto.TypeInfo(Fleet),
            ),
        ]

    # Information about the fleet.
    fleet: "Fleet" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateImageBuilderRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                autoboto.TypeInfo(str),
            ),
            (
                "image_name",
                "ImageName",
                autoboto.TypeInfo(str),
            ),
            (
                "image_arn",
                "ImageArn",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_config",
                "VpcConfig",
                autoboto.TypeInfo(VpcConfig),
            ),
            (
                "enable_default_internet_access",
                "EnableDefaultInternetAccess",
                autoboto.TypeInfo(bool),
            ),
            (
                "domain_join_info",
                "DomainJoinInfo",
                autoboto.TypeInfo(DomainJoinInfo),
            ),
            (
                "appstream_agent_version",
                "AppstreamAgentVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique name for the image builder.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance type to use when launching the image builder.
    instance_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the image used to create the builder.
    image_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the public, private, or shared image to use.
    image_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description for display.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The image builder name for display.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The VPC configuration for the image builder. You can specify only one
    # subnet.
    vpc_config: "VpcConfig" = dataclasses.field(default_factory=dict, )

    # Enables or disables default internet access for the image builder.
    enable_default_internet_access: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The information needed to join a Microsoft Active Directory domain.
    domain_join_info: "DomainJoinInfo" = dataclasses.field(
        default_factory=dict,
    )

    # The version of the AppStream 2.0 agent to use for this image builder. To
    # use the latest version of the AppStream 2.0 agent, specify [LATEST].
    appstream_agent_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateImageBuilderResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image_builder",
                "ImageBuilder",
                autoboto.TypeInfo(ImageBuilder),
            ),
        ]

    # Information about the image builder.
    image_builder: "ImageBuilder" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateImageBuilderStreamingURLRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "validity",
                "Validity",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the image builder.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time that the streaming URL will be valid, in seconds. Specify a value
    # between 1 and 604800 seconds. The default is 3600 seconds.
    validity: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateImageBuilderStreamingURLResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "streaming_url",
                "StreamingURL",
                autoboto.TypeInfo(str),
            ),
            (
                "expires",
                "Expires",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The URL to start the AppStream 2.0 streaming session.
    streaming_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The elapsed time, in seconds after the Unix epoch, when this URL expires.
    expires: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateStackRequest(autoboto.ShapeBase):
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
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "storage_connectors",
                "StorageConnectors",
                autoboto.TypeInfo(typing.List[StorageConnector]),
            ),
            (
                "redirect_url",
                "RedirectURL",
                autoboto.TypeInfo(str),
            ),
            (
                "feedback_url",
                "FeedbackURL",
                autoboto.TypeInfo(str),
            ),
            (
                "user_settings",
                "UserSettings",
                autoboto.TypeInfo(typing.List[UserSetting]),
            ),
        ]

    # The name of the stack.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description for display.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack name for display.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The storage connectors to enable.
    storage_connectors: typing.List["StorageConnector"] = dataclasses.field(
        default_factory=list,
    )

    # The URL that users are redirected to after their streaming session ends.
    redirect_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The URL that users are redirected to after they click the Send Feedback
    # link. If no URL is specified, no Send Feedback link is displayed.
    feedback_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The actions that are enabled or disabled for users during their streaming
    # sessions. By default, these actions are enabled.
    user_settings: typing.List["UserSetting"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateStackResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack",
                "Stack",
                autoboto.TypeInfo(Stack),
            ),
        ]

    # Information about the stack.
    stack: "Stack" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateStreamingURLRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                autoboto.TypeInfo(str),
            ),
            (
                "fleet_name",
                "FleetName",
                autoboto.TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                autoboto.TypeInfo(str),
            ),
            (
                "application_id",
                "ApplicationId",
                autoboto.TypeInfo(str),
            ),
            (
                "validity",
                "Validity",
                autoboto.TypeInfo(int),
            ),
            (
                "session_context",
                "SessionContext",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the stack.
    stack_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the fleet.
    fleet_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the user.
    user_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the application to launch after the session starts. This is the
    # name that you specified as **Name** in the Image Assistant.
    application_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time that the streaming URL will be valid, in seconds. Specify a value
    # between 1 and 604800 seconds. The default is 60 seconds.
    validity: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The session context. For more information, see [Session
    # Context](http://docs.aws.amazon.com/appstream2/latest/developerguide/managing-
    # stacks-fleets.html#managing-stacks-fleets-parameters) in the _Amazon
    # AppStream 2.0 Developer Guide_.
    session_context: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateStreamingURLResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "streaming_url",
                "StreamingURL",
                autoboto.TypeInfo(str),
            ),
            (
                "expires",
                "Expires",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The URL to start the AppStream 2.0 streaming session.
    streaming_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The elapsed time, in seconds after the Unix epoch, when this URL expires.
    expires: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDirectoryConfigRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_name",
                "DirectoryName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the directory configuration.
    directory_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDirectoryConfigResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteFleetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the fleet.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFleetResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteImageBuilderRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the image builder.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteImageBuilderResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image_builder",
                "ImageBuilder",
                autoboto.TypeInfo(ImageBuilder),
            ),
        ]

    # Information about the image builder.
    image_builder: "ImageBuilder" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteImagePermissionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "shared_account_id",
                "SharedAccountId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the private image.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The 12-digit ID of the AWS account for which to delete image permissions.
    shared_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteImagePermissionsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteImageRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the image.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteImageResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image",
                "Image",
                autoboto.TypeInfo(Image),
            ),
        ]

    # Information about the image.
    image: "Image" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteStackRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the stack.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteStackResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeDirectoryConfigsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_names",
                "DirectoryNames",
                autoboto.TypeInfo(typing.List[str]),
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

    # The directory names.
    directory_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The maximum size of each page of results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If this value is null, it retrieves the first page.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDirectoryConfigsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_configs",
                "DirectoryConfigs",
                autoboto.TypeInfo(typing.List[DirectoryConfig]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the directory configurations. Note that although the
    # response syntax in this topic includes the account password, this password
    # is not returned in the actual response.
    directory_configs: typing.List["DirectoryConfig"] = dataclasses.field(
        default_factory=list,
    )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If there are no more pages, this value is null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFleetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The names of the fleets to describe.
    names: typing.List[str] = dataclasses.field(default_factory=list, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If this value is null, it retrieves the first page.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFleetsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleets",
                "Fleets",
                autoboto.TypeInfo(typing.List[Fleet]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the fleets.
    fleets: typing.List["Fleet"] = dataclasses.field(default_factory=list, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If there are no more pages, this value is null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeImageBuildersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                autoboto.TypeInfo(typing.List[str]),
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

    # The names of the image builders to describe.
    names: typing.List[str] = dataclasses.field(default_factory=list, )

    # The maximum size of each page of results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If this value is null, it retrieves the first page.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeImageBuildersResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image_builders",
                "ImageBuilders",
                autoboto.TypeInfo(typing.List[ImageBuilder]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the image builders.
    image_builders: typing.List["ImageBuilder"] = dataclasses.field(
        default_factory=list,
    )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If there are no more pages, this value is null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeImagePermissionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "shared_aws_account_ids",
                "SharedAwsAccountIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the private image for which to describe permissions. The image
    # must be one that you own.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum size of each results page.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The 12-digit ID of one or more AWS accounts with which the image is shared.
    shared_aws_account_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The pagination token to use to retrieve the next page of results. If this
    # value is empty, only the first page is retrieved.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeImagePermissionsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "shared_image_permissions_list",
                "SharedImagePermissionsList",
                autoboto.TypeInfo(typing.List[SharedImagePermissions]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the private image.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The permissions for a private image that you own.
    shared_image_permissions_list: typing.List["SharedImagePermissions"
                                              ] = dataclasses.field(
                                                  default_factory=list,
                                              )

    # The pagination token to use to retrieve the next page of results. If this
    # value is empty, only the first page is retrieved.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeImagesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "arns",
                "Arns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(VisibilityType),
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

    # The names of the images to describe.
    names: typing.List[str] = dataclasses.field(default_factory=list, )

    # The ARNs of the public, private, and shared images to describe.
    arns: typing.List[str] = dataclasses.field(default_factory=list, )

    # The type of image (public, private, or shared) to describe.
    type: "VisibilityType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The pagination token to use to retrieve the next page of results. If this
    # value is empty, only the first page is retrieved.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum size of each page of results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeImagesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "images",
                "Images",
                autoboto.TypeInfo(typing.List[Image]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the images.
    images: typing.List["Image"] = dataclasses.field(default_factory=list, )

    # The pagination token to use to retrieve the next page of results. If there
    # are no more pages, this value is null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSessionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                autoboto.TypeInfo(str),
            ),
            (
                "fleet_name",
                "FleetName",
                autoboto.TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "authentication_type",
                "AuthenticationType",
                autoboto.TypeInfo(AuthenticationType),
            ),
        ]

    # The name of the stack. This value is case-sensitive.
    stack_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the fleet. This value is case-sensitive.
    fleet_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user ID.
    user_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If this value is null, it retrieves the first page.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The size of each page of results. The default value is 20 and the maximum
    # value is 50.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The authentication method. Specify `API` for a user authenticated using a
    # streaming URL or `SAML` for a SAML federated user. The default is to
    # authenticate users using a streaming URL.
    authentication_type: "AuthenticationType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeSessionsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sessions",
                "Sessions",
                autoboto.TypeInfo(typing.List[Session]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the streaming sessions.
    sessions: typing.List["Session"] = dataclasses.field(default_factory=list, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If there are no more pages, this value is null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStacksRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The names of the stacks to describe.
    names: typing.List[str] = dataclasses.field(default_factory=list, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If this value is null, it retrieves the first page.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStacksResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stacks",
                "Stacks",
                autoboto.TypeInfo(typing.List[Stack]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the stacks.
    stacks: typing.List["Stack"] = dataclasses.field(default_factory=list, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If there are no more pages, this value is null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DirectoryConfig(autoboto.ShapeBase):
    """
    Configuration information for the directory used to join domains.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_name",
                "DirectoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "organizational_unit_distinguished_names",
                "OrganizationalUnitDistinguishedNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "service_account_credentials",
                "ServiceAccountCredentials",
                autoboto.TypeInfo(ServiceAccountCredentials),
            ),
            (
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The fully qualified name of the directory (for example, corp.example.com).
    directory_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The distinguished names of the organizational units for computer accounts.
    organizational_unit_distinguished_names: typing.List[
        str
    ] = dataclasses.field(
        default_factory=list,
    )

    # The credentials for the service account used by the streaming instance to
    # connect to the directory.
    service_account_credentials: "ServiceAccountCredentials" = dataclasses.field(
        default_factory=dict,
    )

    # The time the directory configuration was created.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateFleetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_name",
                "FleetName",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_name",
                "StackName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the fleet.
    fleet_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the stack.
    stack_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateFleetResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DomainJoinInfo(autoboto.ShapeBase):
    """
    Contains the information needed to join a Microsoft Active Directory domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_name",
                "DirectoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "organizational_unit_distinguished_name",
                "OrganizationalUnitDistinguishedName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The fully qualified name of the directory (for example, corp.example.com).
    directory_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The distinguished name of the organizational unit for computer accounts.
    organizational_unit_distinguished_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ExpireSessionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "session_id",
                "SessionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the streaming session.
    session_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExpireSessionResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Fleet(autoboto.ShapeBase):
    """
    Contains the parameters for a fleet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                autoboto.TypeInfo(str),
            ),
            (
                "compute_capacity_status",
                "ComputeCapacityStatus",
                autoboto.TypeInfo(ComputeCapacityStatus),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(FleetState),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "image_name",
                "ImageName",
                autoboto.TypeInfo(str),
            ),
            (
                "image_arn",
                "ImageArn",
                autoboto.TypeInfo(str),
            ),
            (
                "fleet_type",
                "FleetType",
                autoboto.TypeInfo(FleetType),
            ),
            (
                "max_user_duration_in_seconds",
                "MaxUserDurationInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "disconnect_timeout_in_seconds",
                "DisconnectTimeoutInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "vpc_config",
                "VpcConfig",
                autoboto.TypeInfo(VpcConfig),
            ),
            (
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "fleet_errors",
                "FleetErrors",
                autoboto.TypeInfo(typing.List[FleetError]),
            ),
            (
                "enable_default_internet_access",
                "EnableDefaultInternetAccess",
                autoboto.TypeInfo(bool),
            ),
            (
                "domain_join_info",
                "DomainJoinInfo",
                autoboto.TypeInfo(DomainJoinInfo),
            ),
        ]

    # The ARN for the fleet.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the fleet.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance type to use when launching fleet instances.
    instance_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The capacity status for the fleet.
    compute_capacity_status: "ComputeCapacityStatus" = dataclasses.field(
        default_factory=dict,
    )

    # The current state for the fleet.
    state: "FleetState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The fleet name for display.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description for display.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the image used to create the fleet.
    image_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN for the public, private, or shared image.
    image_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The fleet type.

    # ALWAYS_ON

    # Provides users with instant-on access to their apps. You are charged for
    # all running instances in your fleet, even if no users are streaming apps.

    # ON_DEMAND

    # Provide users with access to applications after they connect, which takes
    # one to two minutes. You are charged for instance streaming when users are
    # connected and a small hourly fee for instances that are not streaming apps.
    fleet_type: "FleetType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum time that a streaming session can run, in seconds. Specify a
    # value between 600 and 57600.
    max_user_duration_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time after disconnection when a session is considered to have ended, in
    # seconds. If a user who was disconnected reconnects within this time
    # interval, the user is connected to their previous session. Specify a value
    # between 60 and 57600.
    disconnect_timeout_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The VPC configuration for the fleet.
    vpc_config: "VpcConfig" = dataclasses.field(default_factory=dict, )

    # The time the fleet was created.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The fleet errors.
    fleet_errors: typing.List["FleetError"] = dataclasses.field(
        default_factory=list,
    )

    # Indicates whether default internet access is enabled for the fleet.
    enable_default_internet_access: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The information needed to join a Microsoft Active Directory domain.
    domain_join_info: "DomainJoinInfo" = dataclasses.field(
        default_factory=dict,
    )


class FleetAttribute(Enum):
    """
    The fleet attribute.
    """
    VPC_CONFIGURATION = "VPC_CONFIGURATION"
    VPC_CONFIGURATION_SECURITY_GROUP_IDS = "VPC_CONFIGURATION_SECURITY_GROUP_IDS"
    DOMAIN_JOIN_INFO = "DOMAIN_JOIN_INFO"


@dataclasses.dataclass
class FleetError(autoboto.ShapeBase):
    """
    Describes a fleet error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                autoboto.TypeInfo(FleetErrorCode),
            ),
            (
                "error_message",
                "ErrorMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error code.
    error_code: "FleetErrorCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The error message.
    error_message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class FleetErrorCode(Enum):
    IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION = "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION"
    IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION = "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION"
    IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION = "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION"
    NETWORK_INTERFACE_LIMIT_EXCEEDED = "NETWORK_INTERFACE_LIMIT_EXCEEDED"
    INTERNAL_SERVICE_ERROR = "INTERNAL_SERVICE_ERROR"
    IAM_SERVICE_ROLE_IS_MISSING = "IAM_SERVICE_ROLE_IS_MISSING"
    SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES = "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES"
    IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION = "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION"
    SUBNET_NOT_FOUND = "SUBNET_NOT_FOUND"
    IMAGE_NOT_FOUND = "IMAGE_NOT_FOUND"
    INVALID_SUBNET_CONFIGURATION = "INVALID_SUBNET_CONFIGURATION"
    SECURITY_GROUPS_NOT_FOUND = "SECURITY_GROUPS_NOT_FOUND"
    IGW_NOT_ATTACHED = "IGW_NOT_ATTACHED"
    IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION = "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION"
    DOMAIN_JOIN_ERROR_FILE_NOT_FOUND = "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND"
    DOMAIN_JOIN_ERROR_ACCESS_DENIED = "DOMAIN_JOIN_ERROR_ACCESS_DENIED"
    DOMAIN_JOIN_ERROR_LOGON_FAILURE = "DOMAIN_JOIN_ERROR_LOGON_FAILURE"
    DOMAIN_JOIN_ERROR_INVALID_PARAMETER = "DOMAIN_JOIN_ERROR_INVALID_PARAMETER"
    DOMAIN_JOIN_ERROR_MORE_DATA = "DOMAIN_JOIN_ERROR_MORE_DATA"
    DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN = "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN"
    DOMAIN_JOIN_ERROR_NOT_SUPPORTED = "DOMAIN_JOIN_ERROR_NOT_SUPPORTED"
    DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME = "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME"
    DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED = "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED"
    DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED = "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED"
    DOMAIN_JOIN_NERR_PASSWORD_EXPIRED = "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED"
    DOMAIN_JOIN_INTERNAL_SERVICE_ERROR = "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR"


class FleetState(Enum):
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class FleetType(Enum):
    ALWAYS_ON = "ALWAYS_ON"
    ON_DEMAND = "ON_DEMAND"


@dataclasses.dataclass
class Image(autoboto.ShapeBase):
    """
    Describes an image.
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
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "base_image_arn",
                "BaseImageArn",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(ImageState),
            ),
            (
                "visibility",
                "Visibility",
                autoboto.TypeInfo(VisibilityType),
            ),
            (
                "image_builder_supported",
                "ImageBuilderSupported",
                autoboto.TypeInfo(bool),
            ),
            (
                "platform",
                "Platform",
                autoboto.TypeInfo(PlatformType),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "state_change_reason",
                "StateChangeReason",
                autoboto.TypeInfo(ImageStateChangeReason),
            ),
            (
                "applications",
                "Applications",
                autoboto.TypeInfo(typing.List[Application]),
            ),
            (
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "public_base_image_released_date",
                "PublicBaseImageReleasedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "appstream_agent_version",
                "AppstreamAgentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "image_permissions",
                "ImagePermissions",
                autoboto.TypeInfo(ImagePermissions),
            ),
        ]

    # The name of the image.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the image.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the image from which this image was created.
    base_image_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The image name for display.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The image starts in the `PENDING` state. If image creation succeeds, the
    # state is `AVAILABLE`. If image creation fails, the state is `FAILED`.
    state: "ImageState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the image is public or private.
    visibility: "VisibilityType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether an image builder can be launched from this image.
    image_builder_supported: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The operating system platform of the image.
    platform: "PlatformType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description for display.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The reason why the last state change occurred.
    state_change_reason: "ImageStateChangeReason" = dataclasses.field(
        default_factory=dict,
    )

    # The applications associated with the image.
    applications: typing.List["Application"] = dataclasses.field(
        default_factory=list,
    )

    # The time the image was created.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The release date of the public base image. For private images, this date is
    # the release date of the base image from which the image was created.
    public_base_image_released_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The version of the AppStream 2.0 agent to use for instances that are
    # launched from this image.
    appstream_agent_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The permissions to provide to the destination AWS account for the specified
    # image.
    image_permissions: "ImagePermissions" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ImageBuilder(autoboto.ShapeBase):
    """
    Describes a streaming instance used for editing an image. New images are created
    from a snapshot through an image builder.
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
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "image_arn",
                "ImageArn",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_config",
                "VpcConfig",
                autoboto.TypeInfo(VpcConfig),
            ),
            (
                "instance_type",
                "InstanceType",
                autoboto.TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                autoboto.TypeInfo(PlatformType),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(ImageBuilderState),
            ),
            (
                "state_change_reason",
                "StateChangeReason",
                autoboto.TypeInfo(ImageBuilderStateChangeReason),
            ),
            (
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "enable_default_internet_access",
                "EnableDefaultInternetAccess",
                autoboto.TypeInfo(bool),
            ),
            (
                "domain_join_info",
                "DomainJoinInfo",
                autoboto.TypeInfo(DomainJoinInfo),
            ),
            (
                "image_builder_errors",
                "ImageBuilderErrors",
                autoboto.TypeInfo(typing.List[ResourceError]),
            ),
            (
                "appstream_agent_version",
                "AppstreamAgentVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the image builder.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN for the image builder.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the image from which this builder was created.
    image_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description for display.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The image builder name for display.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The VPC configuration of the image builder.
    vpc_config: "VpcConfig" = dataclasses.field(default_factory=dict, )

    # The instance type for the image builder.
    instance_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The operating system platform of the image builder.
    platform: "PlatformType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The state of the image builder.
    state: "ImageBuilderState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The reason why the last state change occurred.
    state_change_reason: "ImageBuilderStateChangeReason" = dataclasses.field(
        default_factory=dict,
    )

    # The time stamp when the image builder was created.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Enables or disables default internet access for the image builder.
    enable_default_internet_access: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The information needed to join a Microsoft Active Directory domain.
    domain_join_info: "DomainJoinInfo" = dataclasses.field(
        default_factory=dict,
    )

    # The image builder errors.
    image_builder_errors: typing.List["ResourceError"] = dataclasses.field(
        default_factory=list,
    )

    # The version of the AppStream 2.0 agent that is currently being used by this
    # image builder.
    appstream_agent_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ImageBuilderState(Enum):
    PENDING = "PENDING"
    UPDATING_AGENT = "UPDATING_AGENT"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    REBOOTING = "REBOOTING"
    SNAPSHOTTING = "SNAPSHOTTING"
    DELETING = "DELETING"
    FAILED = "FAILED"


@dataclasses.dataclass
class ImageBuilderStateChangeReason(autoboto.ShapeBase):
    """
    Describes the reason why the last image builder state change occurred.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                autoboto.TypeInfo(ImageBuilderStateChangeReasonCode),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The state change reason code.
    code: "ImageBuilderStateChangeReasonCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The state change reason message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ImageBuilderStateChangeReasonCode(Enum):
    INTERNAL_ERROR = "INTERNAL_ERROR"
    IMAGE_UNAVAILABLE = "IMAGE_UNAVAILABLE"


@dataclasses.dataclass
class ImagePermissions(autoboto.ShapeBase):
    """
    Describes the permissions for an image.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "allow_fleet",
                "allowFleet",
                autoboto.TypeInfo(bool),
            ),
            (
                "allow_image_builder",
                "allowImageBuilder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Indicates whether the image can be used for a fleet.
    allow_fleet: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether the image can be used for an image builder.
    allow_image_builder: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ImageState(Enum):
    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    FAILED = "FAILED"
    COPYING = "COPYING"
    DELETING = "DELETING"


@dataclasses.dataclass
class ImageStateChangeReason(autoboto.ShapeBase):
    """
    Describes the reason why the last image state change occurred.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                autoboto.TypeInfo(ImageStateChangeReasonCode),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The state change reason code.
    code: "ImageStateChangeReasonCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The state change reason message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ImageStateChangeReasonCode(Enum):
    INTERNAL_ERROR = "INTERNAL_ERROR"
    IMAGE_BUILDER_NOT_AVAILABLE = "IMAGE_BUILDER_NOT_AVAILABLE"
    IMAGE_COPY_FAILURE = "IMAGE_COPY_FAILURE"


@dataclasses.dataclass
class IncompatibleImageException(autoboto.ShapeBase):
    """
    The image does not support storage connectors.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidAccountStatusException(autoboto.ShapeBase):
    """
    The resource cannot be created because your AWS account is suspended. For
    assistance, contact AWS Support.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterCombinationException(autoboto.ShapeBase):
    """
    Indicates an incorrect combination of parameters, or a missing parameter.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRoleException(autoboto.ShapeBase):
    """
    The specified role is invalid.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    The requested limit exceeds the permitted limit for an account.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssociatedFleetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the stack.
    stack_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If this value is null, it retrieves the first page.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssociatedFleetsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the fleet.
    names: typing.List[str] = dataclasses.field(default_factory=list, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If there are no more pages, this value is null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssociatedStacksRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet_name",
                "FleetName",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the fleet.
    fleet_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If this value is null, it retrieves the first page.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssociatedStacksResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the stack.
    names: typing.List[str] = dataclasses.field(default_factory=list, )

    # The pagination token to use to retrieve the next page of results for this
    # operation. If there are no more pages, this value is null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The information about the tags.
    tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NetworkAccessConfiguration(autoboto.ShapeBase):
    """
    The network details of the fleet instance for the streaming session.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "eni_private_ip_address",
                "EniPrivateIpAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "eni_id",
                "EniId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The private IP address of the elastic network interface that is attached to
    # instances in your VPC.
    eni_private_ip_address: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The resource identifier of the elastic network interface that is attached
    # to instances in your VPC. All network interfaces have the eni-xxxxxxxx
    # resource identifier.
    eni_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OperationNotPermittedException(autoboto.ShapeBase):
    """
    The attempted operation is not permitted.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class Permission(Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class PlatformType(Enum):
    WINDOWS = "WINDOWS"


@dataclasses.dataclass
class ResourceAlreadyExistsException(autoboto.ShapeBase):
    """
    The specified resource already exists.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceError(autoboto.ShapeBase):
    """
    Describes a resource error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                autoboto.TypeInfo(FleetErrorCode),
            ),
            (
                "error_message",
                "ErrorMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "error_timestamp",
                "ErrorTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The error code.
    error_code: "FleetErrorCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The error message.
    error_message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time the error occurred.
    error_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceInUseException(autoboto.ShapeBase):
    """
    The specified resource is in use.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotAvailableException(autoboto.ShapeBase):
    """
    The specified resource exists and is not in use, but isn't available.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    The specified resource was not found.
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

    # The error message in the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceAccountCredentials(autoboto.ShapeBase):
    """
    Describes the credentials for the service account used by the streaming instance
    to connect to the directory.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_name",
                "AccountName",
                autoboto.TypeInfo(str),
            ),
            (
                "account_password",
                "AccountPassword",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user name of the account. This account must have the following
    # privileges: create computer objects, join computers to the domain, and
    # change/reset the password on descendant computer objects for the
    # organizational units specified.
    account_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The password for the account.
    account_password: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Session(autoboto.ShapeBase):
    """
    Describes a streaming session.
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
                "user_id",
                "UserId",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_name",
                "StackName",
                autoboto.TypeInfo(str),
            ),
            (
                "fleet_name",
                "FleetName",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(SessionState),
            ),
            (
                "authentication_type",
                "AuthenticationType",
                autoboto.TypeInfo(AuthenticationType),
            ),
            (
                "network_access_configuration",
                "NetworkAccessConfiguration",
                autoboto.TypeInfo(NetworkAccessConfiguration),
            ),
        ]

    # The ID of the streaming session.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of the user for whom the session was created.
    user_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the stack for the streaming session.
    stack_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the fleet for the streaming session.
    fleet_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The current state of the streaming session.
    state: "SessionState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The authentication method. The user is authenticated using a streaming URL
    # (`API`) or SAML federation (`SAML`).
    authentication_type: "AuthenticationType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The network details for the streaming session.
    network_access_configuration: "NetworkAccessConfiguration" = dataclasses.field(
        default_factory=dict,
    )


class SessionState(Enum):
    """
    Possible values for the state of a streaming session.
    """
    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    EXPIRED = "EXPIRED"


@dataclasses.dataclass
class SharedImagePermissions(autoboto.ShapeBase):
    """
    Describes the permissions that are available to the specified AWS account for a
    shared image.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "shared_account_id",
                "sharedAccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "image_permissions",
                "imagePermissions",
                autoboto.TypeInfo(ImagePermissions),
            ),
        ]

    # The 12-digit ID of the AWS account with which the image is shared.
    shared_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Describes the permissions for a shared image.
    image_permissions: "ImagePermissions" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class Stack(autoboto.ShapeBase):
    """
    Describes a stack.
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
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "storage_connectors",
                "StorageConnectors",
                autoboto.TypeInfo(typing.List[StorageConnector]),
            ),
            (
                "redirect_url",
                "RedirectURL",
                autoboto.TypeInfo(str),
            ),
            (
                "feedback_url",
                "FeedbackURL",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_errors",
                "StackErrors",
                autoboto.TypeInfo(typing.List[StackError]),
            ),
            (
                "user_settings",
                "UserSettings",
                autoboto.TypeInfo(typing.List[UserSetting]),
            ),
        ]

    # The name of the stack.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the stack.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description for display.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack name for display.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time the stack was created.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The storage connectors to enable.
    storage_connectors: typing.List["StorageConnector"] = dataclasses.field(
        default_factory=list,
    )

    # The URL that users are redirected to after their streaming session ends.
    redirect_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The URL that users are redirected to after they click the Send Feedback
    # link. If no URL is specified, no Send Feedback link is displayed.
    feedback_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The errors for the stack.
    stack_errors: typing.List["StackError"] = dataclasses.field(
        default_factory=list,
    )

    # The actions that are enabled or disabled for users during their streaming
    # sessions. By default these actions are enabled.
    user_settings: typing.List["UserSetting"] = dataclasses.field(
        default_factory=list,
    )


class StackAttribute(Enum):
    STORAGE_CONNECTORS = "STORAGE_CONNECTORS"
    STORAGE_CONNECTOR_HOMEFOLDERS = "STORAGE_CONNECTOR_HOMEFOLDERS"
    STORAGE_CONNECTOR_GOOGLE_DRIVE = "STORAGE_CONNECTOR_GOOGLE_DRIVE"
    STORAGE_CONNECTOR_ONE_DRIVE = "STORAGE_CONNECTOR_ONE_DRIVE"
    REDIRECT_URL = "REDIRECT_URL"
    FEEDBACK_URL = "FEEDBACK_URL"
    THEME_NAME = "THEME_NAME"
    USER_SETTINGS = "USER_SETTINGS"


@dataclasses.dataclass
class StackError(autoboto.ShapeBase):
    """
    Describes a stack error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                autoboto.TypeInfo(StackErrorCode),
            ),
            (
                "error_message",
                "ErrorMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error code.
    error_code: "StackErrorCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The error message.
    error_message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class StackErrorCode(Enum):
    STORAGE_CONNECTOR_ERROR = "STORAGE_CONNECTOR_ERROR"
    INTERNAL_SERVICE_ERROR = "INTERNAL_SERVICE_ERROR"


@dataclasses.dataclass
class StartFleetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the fleet.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartFleetResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StartImageBuilderRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "appstream_agent_version",
                "AppstreamAgentVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the image builder.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version of the AppStream 2.0 agent to use for this image builder. To
    # use the latest version of the AppStream 2.0 agent, specify [LATEST].
    appstream_agent_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartImageBuilderResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image_builder",
                "ImageBuilder",
                autoboto.TypeInfo(ImageBuilder),
            ),
        ]

    # Information about the image builder.
    image_builder: "ImageBuilder" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class StopFleetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the fleet.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopFleetResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StopImageBuilderRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the image builder.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopImageBuilderResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image_builder",
                "ImageBuilder",
                autoboto.TypeInfo(ImageBuilder),
            ),
        ]

    # Information about the image builder.
    image_builder: "ImageBuilder" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class StorageConnector(autoboto.ShapeBase):
    """
    Describes a connector to enable persistent storage for users.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connector_type",
                "ConnectorType",
                autoboto.TypeInfo(StorageConnectorType),
            ),
            (
                "resource_identifier",
                "ResourceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "domains",
                "Domains",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The type of storage connector.
    connector_type: "StorageConnectorType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the storage connector.
    resource_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The names of the domains for the G Suite account.
    domains: typing.List[str] = dataclasses.field(default_factory=list, )


class StorageConnectorType(Enum):
    """
    The type of storage connector.
    """
    HOMEFOLDERS = "HOMEFOLDERS"
    GOOGLE_DRIVE = "GOOGLE_DRIVE"
    ONE_DRIVE = "ONE_DRIVE"


@dataclasses.dataclass
class TagResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tags to associate. A tag is a key-value pair (the value is optional).
    # For example, `Environment=Test`, or, if you do not specify a value,
    # `Environment=`.

    # If you do not specify a value, we set the value to an empty string.
    tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TagResourceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UntagResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tag keys for the tags to disassociate.
    tag_keys: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UntagResourceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateDirectoryConfigRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_name",
                "DirectoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "organizational_unit_distinguished_names",
                "OrganizationalUnitDistinguishedNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "service_account_credentials",
                "ServiceAccountCredentials",
                autoboto.TypeInfo(ServiceAccountCredentials),
            ),
        ]

    # The name of the Directory Config object.
    directory_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The distinguished names of the organizational units for computer accounts.
    organizational_unit_distinguished_names: typing.List[
        str
    ] = dataclasses.field(
        default_factory=list,
    )

    # The credentials for the service account used by the streaming instance to
    # connect to the directory.
    service_account_credentials: "ServiceAccountCredentials" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateDirectoryConfigResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_config",
                "DirectoryConfig",
                autoboto.TypeInfo(DirectoryConfig),
            ),
        ]

    # Information about the Directory Config object.
    directory_config: "DirectoryConfig" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateFleetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image_name",
                "ImageName",
                autoboto.TypeInfo(str),
            ),
            (
                "image_arn",
                "ImageArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                autoboto.TypeInfo(str),
            ),
            (
                "compute_capacity",
                "ComputeCapacity",
                autoboto.TypeInfo(ComputeCapacity),
            ),
            (
                "vpc_config",
                "VpcConfig",
                autoboto.TypeInfo(VpcConfig),
            ),
            (
                "max_user_duration_in_seconds",
                "MaxUserDurationInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "disconnect_timeout_in_seconds",
                "DisconnectTimeoutInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "delete_vpc_config",
                "DeleteVpcConfig",
                autoboto.TypeInfo(bool),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "enable_default_internet_access",
                "EnableDefaultInternetAccess",
                autoboto.TypeInfo(bool),
            ),
            (
                "domain_join_info",
                "DomainJoinInfo",
                autoboto.TypeInfo(DomainJoinInfo),
            ),
            (
                "attributes_to_delete",
                "AttributesToDelete",
                autoboto.TypeInfo(typing.List[FleetAttribute]),
            ),
        ]

    # The name of the image used to create the fleet.
    image_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the public, private, or shared image to use.
    image_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A unique name for the fleet.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance type to use when launching fleet instances. The following
    # instance types are available:

    #   * stream.standard.medium

    #   * stream.standard.large

    #   * stream.compute.large

    #   * stream.compute.xlarge

    #   * stream.compute.2xlarge

    #   * stream.compute.4xlarge

    #   * stream.compute.8xlarge

    #   * stream.memory.large

    #   * stream.memory.xlarge

    #   * stream.memory.2xlarge

    #   * stream.memory.4xlarge

    #   * stream.memory.8xlarge

    #   * stream.graphics-design.large

    #   * stream.graphics-design.xlarge

    #   * stream.graphics-design.2xlarge

    #   * stream.graphics-design.4xlarge

    #   * stream.graphics-desktop.2xlarge

    #   * stream.graphics-pro.4xlarge

    #   * stream.graphics-pro.8xlarge

    #   * stream.graphics-pro.16xlarge
    instance_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The desired capacity for the fleet.
    compute_capacity: "ComputeCapacity" = dataclasses.field(
        default_factory=dict,
    )

    # The VPC configuration for the fleet.
    vpc_config: "VpcConfig" = dataclasses.field(default_factory=dict, )

    # The maximum time that a streaming session can run, in seconds. Specify a
    # value between 600 and 57600.
    max_user_duration_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time after disconnection when a session is considered to have ended, in
    # seconds. If a user who was disconnected reconnects within this time
    # interval, the user is connected to their previous session. Specify a value
    # between 60 and 57600.
    disconnect_timeout_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Deletes the VPC association for the specified fleet.
    delete_vpc_config: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description for display.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The fleet name for display.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Enables or disables default internet access for the fleet.
    enable_default_internet_access: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The information needed to join a Microsoft Active Directory domain.
    domain_join_info: "DomainJoinInfo" = dataclasses.field(
        default_factory=dict,
    )

    # The fleet attributes to delete.
    attributes_to_delete: typing.List["FleetAttribute"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateFleetResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fleet",
                "Fleet",
                autoboto.TypeInfo(Fleet),
            ),
        ]

    # Information about the fleet.
    fleet: "Fleet" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateImagePermissionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "shared_account_id",
                "SharedAccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "image_permissions",
                "ImagePermissions",
                autoboto.TypeInfo(ImagePermissions),
            ),
        ]

    # The name of the private image.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The 12-digit ID of the AWS account for which you want add or update image
    # permissions.
    shared_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The permissions for the image.
    image_permissions: "ImagePermissions" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateImagePermissionsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateStackRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "storage_connectors",
                "StorageConnectors",
                autoboto.TypeInfo(typing.List[StorageConnector]),
            ),
            (
                "delete_storage_connectors",
                "DeleteStorageConnectors",
                autoboto.TypeInfo(bool),
            ),
            (
                "redirect_url",
                "RedirectURL",
                autoboto.TypeInfo(str),
            ),
            (
                "feedback_url",
                "FeedbackURL",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes_to_delete",
                "AttributesToDelete",
                autoboto.TypeInfo(typing.List[StackAttribute]),
            ),
            (
                "user_settings",
                "UserSettings",
                autoboto.TypeInfo(typing.List[UserSetting]),
            ),
        ]

    # The name of the stack.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack name for display.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description for display.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The storage connectors to enable.
    storage_connectors: typing.List["StorageConnector"] = dataclasses.field(
        default_factory=list,
    )

    # Deletes the storage connectors currently enabled for the stack.
    delete_storage_connectors: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL that users are redirected to after their streaming session ends.
    redirect_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The URL that users are redirected to after they click the Send Feedback
    # link. If no URL is specified, no Send Feedback link is displayed.
    feedback_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack attributes to delete.
    attributes_to_delete: typing.List["StackAttribute"] = dataclasses.field(
        default_factory=list,
    )

    # The actions that are enabled or disabled for users during their streaming
    # sessions. By default, these actions are enabled.
    user_settings: typing.List["UserSetting"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateStackResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack",
                "Stack",
                autoboto.TypeInfo(Stack),
            ),
        ]

    # Information about the stack.
    stack: "Stack" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UserSetting(autoboto.ShapeBase):
    """
    Describes an action and whether the action is enabled or disabled for users
    during their streaming sessions.
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
                "permission",
                "Permission",
                autoboto.TypeInfo(Permission),
            ),
        ]

    # The action that is enabled or disabled.
    action: "Action" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether the action is enabled or disabled.
    permission: "Permission" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class VisibilityType(Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"
    SHARED = "SHARED"


@dataclasses.dataclass
class VpcConfig(autoboto.ShapeBase):
    """
    Describes VPC configuration information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_ids",
                "SubnetIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The subnets to which a network interface is established from the fleet
    # instance.
    subnet_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The security groups for the fleet.
    security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )
