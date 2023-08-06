import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AssociateRoleToGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the role you wish to associate with this group.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AssociateRoleToGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "associated_at",
                "AssociatedAt",
                autoboto.TypeInfo(str),
            ),
        ]

    # The time, in milliseconds since the epoch, when the role ARN was associated
    # with the group.
    associated_at: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AssociateServiceRoleToAccountRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the service role you wish to associate with your account.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AssociateServiceRoleToAccountResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "associated_at",
                "AssociatedAt",
                autoboto.TypeInfo(str),
            ),
        ]

    # The time when the service role was associated with the account.
    associated_at: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class BadRequestException(autoboto.ShapeBase):
    """
    General error information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_details",
                "ErrorDetails",
                autoboto.TypeInfo(typing.List[ErrorDetail]),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # Details about the error.
    error_details: typing.List["ErrorDetail"] = dataclasses.field(
        default_factory=list,
    )

    # A message containing information about the error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ConnectivityInfo(autoboto.ShapeBase):
    """
    Information about a Greengrass core's connectivity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "host_address",
                "HostAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "metadata",
                "Metadata",
                autoboto.TypeInfo(str),
            ),
            (
                "port_number",
                "PortNumber",
                autoboto.TypeInfo(int),
            ),
        ]

    # The endpoint for the Greengrass core. Can be an IP address or DNS.
    host_address: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the connectivity information.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Metadata for this endpoint.
    metadata: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The port of the Greengrass core. Usually 8883.
    port_number: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Core(autoboto.ShapeBase):
    """
    Information about a core.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "sync_shadow",
                "SyncShadow",
                autoboto.TypeInfo(bool),
            ),
            (
                "thing_arn",
                "ThingArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the certificate associated with the core.
    certificate_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the core.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If true, the core's local shadow is automatically synced with the cloud.
    sync_shadow: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the thing which is the core.
    thing_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CoreDefinitionVersion(autoboto.ShapeBase):
    """
    Information about a core definition version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cores",
                "Cores",
                autoboto.TypeInfo(typing.List[Core]),
            ),
        ]

    # A list of cores in the core definition version.
    cores: typing.List["Core"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateCoreDefinitionRequest(autoboto.ShapeBase):
    """
    Information needed to create a core definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "initial_version",
                "InitialVersion",
                autoboto.TypeInfo(CoreDefinitionVersion),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the initial version of the core definition.
    initial_version: "CoreDefinitionVersion" = dataclasses.field(
        default_factory=dict,
    )

    # The name of the core definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateCoreDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the definition.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the definition.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateCoreDefinitionVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "core_definition_id",
                "CoreDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "cores",
                "Cores",
                autoboto.TypeInfo(typing.List[Core]),
            ),
        ]

    # The ID of the core definition.
    core_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of cores in the core definition version.
    cores: typing.List["Core"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateCoreDefinitionVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the version.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the version was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the version.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID of the version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateDeploymentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "deployment_id",
                "DeploymentId",
                autoboto.TypeInfo(str),
            ),
            (
                "deployment_type",
                "DeploymentType",
                autoboto.TypeInfo(DeploymentType),
            ),
            (
                "group_version_id",
                "GroupVersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the deployment if you wish to redeploy a previous deployment.
    deployment_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of deployment. When used in ''CreateDeployment'', only
    # ''NewDeployment'' and ''Redeployment'' are valid.
    deployment_type: "DeploymentType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the group version to be deployed.
    group_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateDeploymentResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_arn",
                "DeploymentArn",
                autoboto.TypeInfo(str),
            ),
            (
                "deployment_id",
                "DeploymentId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the deployment.
    deployment_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the deployment.
    deployment_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateDeviceDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "initial_version",
                "InitialVersion",
                autoboto.TypeInfo(DeviceDefinitionVersion),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the initial version of the device definition.
    initial_version: "DeviceDefinitionVersion" = dataclasses.field(
        default_factory=dict,
    )

    # The name of the device definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateDeviceDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the definition.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the definition.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateDeviceDefinitionVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_definition_id",
                "DeviceDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "devices",
                "Devices",
                autoboto.TypeInfo(typing.List[Device]),
            ),
        ]

    # The ID of the device definition.
    device_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of devices in the definition version.
    devices: typing.List["Device"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateDeviceDefinitionVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the version.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the version was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the version.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID of the version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateFunctionDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "initial_version",
                "InitialVersion",
                autoboto.TypeInfo(FunctionDefinitionVersion),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the initial version of the function definition.
    initial_version: "FunctionDefinitionVersion" = dataclasses.field(
        default_factory=dict,
    )

    # The name of the function definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateFunctionDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the definition.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the definition.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateFunctionDefinitionVersionRequest(autoboto.ShapeBase):
    """
    Information needed to create a function definition version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_definition_id",
                "FunctionDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "functions",
                "Functions",
                autoboto.TypeInfo(typing.List[Function]),
            ),
        ]

    # The ID of the Lambda function definition.
    function_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of Lambda functions in this function definition version.
    functions: typing.List["Function"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateFunctionDefinitionVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the version.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the version was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the version.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID of the version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateGroupCertificateAuthorityRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateGroupCertificateAuthorityResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_certificate_authority_arn",
                "GroupCertificateAuthorityArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the group certificate authority.
    group_certificate_authority_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "initial_version",
                "InitialVersion",
                autoboto.TypeInfo(GroupVersion),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the initial version of the group.
    initial_version: "GroupVersion" = dataclasses.field(default_factory=dict, )

    # The name of the group.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the definition.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the definition.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateGroupVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "core_definition_version_arn",
                "CoreDefinitionVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "device_definition_version_arn",
                "DeviceDefinitionVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "function_definition_version_arn",
                "FunctionDefinitionVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "logger_definition_version_arn",
                "LoggerDefinitionVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_definition_version_arn",
                "ResourceDefinitionVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "subscription_definition_version_arn",
                "SubscriptionDefinitionVersionArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the core definition version for this group.
    core_definition_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the device definition version for this group.
    device_definition_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the function definition version for this group.
    function_definition_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the logger definition version for this group.
    logger_definition_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The resource definition version ARN for this group.
    resource_definition_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the subscription definition version for this group.
    subscription_definition_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateGroupVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the version.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the version was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the version.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID of the version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateLoggerDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "initial_version",
                "InitialVersion",
                autoboto.TypeInfo(LoggerDefinitionVersion),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the initial version of the logger definition.
    initial_version: "LoggerDefinitionVersion" = dataclasses.field(
        default_factory=dict,
    )

    # The name of the logger definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateLoggerDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the definition.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the definition.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateLoggerDefinitionVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logger_definition_id",
                "LoggerDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "loggers",
                "Loggers",
                autoboto.TypeInfo(typing.List[Logger]),
            ),
        ]

    # The ID of the logger definition.
    logger_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of loggers.
    loggers: typing.List["Logger"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateLoggerDefinitionVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the version.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the version was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the version.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID of the version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateResourceDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "initial_version",
                "InitialVersion",
                autoboto.TypeInfo(ResourceDefinitionVersion),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the initial version of the resource definition.
    initial_version: "ResourceDefinitionVersion" = dataclasses.field(
        default_factory=dict,
    )

    # The name of the resource definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateResourceDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the definition.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the definition.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateResourceDefinitionVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_definition_id",
                "ResourceDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "resources",
                "Resources",
                autoboto.TypeInfo(typing.List[Resource]),
            ),
        ]

    # The ID of the resource definition.
    resource_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of resources.
    resources: typing.List["Resource"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateResourceDefinitionVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the version.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the version was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the version.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID of the version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateSoftwareUpdateJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_url_signer_role",
                "S3UrlSignerRole",
                autoboto.TypeInfo(str),
            ),
            (
                "software_to_update",
                "SoftwareToUpdate",
                autoboto.TypeInfo(SoftwareToUpdate),
            ),
            (
                "update_agent_log_level",
                "UpdateAgentLogLevel",
                autoboto.TypeInfo(UpdateAgentLogLevel),
            ),
            (
                "update_targets",
                "UpdateTargets",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "update_targets_architecture",
                "UpdateTargetsArchitecture",
                autoboto.TypeInfo(UpdateTargetsArchitecture),
            ),
            (
                "update_targets_operating_system",
                "UpdateTargetsOperatingSystem",
                autoboto.TypeInfo(UpdateTargetsOperatingSystem),
            ),
        ]

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IAM Role that Greengrass will use to create pre-signed URLs pointing
    # towards the update artifact.
    s3_url_signer_role: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The piece of software on the Greengrass core that will be updated.
    software_to_update: "SoftwareToUpdate" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The minimum level of log statements that should be logged by the OTA Agent
    # during an update.
    update_agent_log_level: "UpdateAgentLogLevel" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARNs of the targets (IoT things or IoT thing groups) that this update
    # will be applied to.
    update_targets: typing.List[str] = dataclasses.field(default_factory=list, )

    # The architecture of the cores which are the targets of an update.
    update_targets_architecture: "UpdateTargetsArchitecture" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The operating system of the cores which are the targets of an update.
    update_targets_operating_system: "UpdateTargetsOperatingSystem" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateSoftwareUpdateJobResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "iot_job_arn",
                "IotJobArn",
                autoboto.TypeInfo(str),
            ),
            (
                "iot_job_id",
                "IotJobId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The IoT Job ARN corresponding to this update.
    iot_job_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The IoT Job Id corresponding to this update.
    iot_job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateSubscriptionDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "initial_version",
                "InitialVersion",
                autoboto.TypeInfo(SubscriptionDefinitionVersion),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the initial version of the subscription definition.
    initial_version: "SubscriptionDefinitionVersion" = dataclasses.field(
        default_factory=dict,
    )

    # The name of the subscription definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateSubscriptionDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the definition.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the definition.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateSubscriptionDefinitionVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_definition_id",
                "SubscriptionDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "subscriptions",
                "Subscriptions",
                autoboto.TypeInfo(typing.List[Subscription]),
            ),
        ]

    # The ID of the subscription definition.
    subscription_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of subscriptions.
    subscriptions: typing.List["Subscription"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateSubscriptionDefinitionVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the version.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the version was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the version.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID of the version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DefinitionInformation(autoboto.ShapeBase):
    """
    Information about a definition.
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
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the definition.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the definition.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteCoreDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "core_definition_id",
                "CoreDefinitionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the core definition.
    core_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteCoreDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteDeviceDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_definition_id",
                "DeviceDefinitionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the device definition.
    device_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteDeviceDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteFunctionDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_definition_id",
                "FunctionDefinitionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Lambda function definition.
    function_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteFunctionDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteLoggerDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logger_definition_id",
                "LoggerDefinitionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the logger definition.
    logger_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteLoggerDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteResourceDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_definition_id",
                "ResourceDefinitionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the resource definition.
    resource_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteResourceDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteSubscriptionDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_definition_id",
                "SubscriptionDefinitionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the subscription definition.
    subscription_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteSubscriptionDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Deployment(autoboto.ShapeBase):
    """
    Information about a deployment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "deployment_arn",
                "DeploymentArn",
                autoboto.TypeInfo(str),
            ),
            (
                "deployment_id",
                "DeploymentId",
                autoboto.TypeInfo(str),
            ),
            (
                "deployment_type",
                "DeploymentType",
                autoboto.TypeInfo(DeploymentType),
            ),
            (
                "group_arn",
                "GroupArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The time, in milliseconds since the epoch, when the deployment was created.
    created_at: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the deployment.
    deployment_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the deployment.
    deployment_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of the deployment.
    deployment_type: "DeploymentType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the group for this deployment.
    group_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class DeploymentType(Enum):
    NewDeployment = "NewDeployment"
    Redeployment = "Redeployment"
    ResetDeployment = "ResetDeployment"
    ForceResetDeployment = "ForceResetDeployment"


@dataclasses.dataclass
class Device(autoboto.ShapeBase):
    """
    Information about a device.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "sync_shadow",
                "SyncShadow",
                autoboto.TypeInfo(bool),
            ),
            (
                "thing_arn",
                "ThingArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the certificate associated with the device.
    certificate_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the device.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If true, the device's local shadow will be automatically synced with the
    # cloud.
    sync_shadow: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The thing ARN of the device.
    thing_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeviceDefinitionVersion(autoboto.ShapeBase):
    """
    Information about a device definition version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "devices",
                "Devices",
                autoboto.TypeInfo(typing.List[Device]),
            ),
        ]

    # A list of devices in the definition version.
    devices: typing.List["Device"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DisassociateRoleFromGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DisassociateRoleFromGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disassociated_at",
                "DisassociatedAt",
                autoboto.TypeInfo(str),
            ),
        ]

    # The time, in milliseconds since the epoch, when the role was disassociated
    # from the group.
    disassociated_at: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DisassociateServiceRoleFromAccountRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DisassociateServiceRoleFromAccountResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disassociated_at",
                "DisassociatedAt",
                autoboto.TypeInfo(str),
            ),
        ]

    # The time when the service role was disassociated from the account.
    disassociated_at: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Empty(autoboto.ShapeBase):
    """
    Empty
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class EncodingType(Enum):
    binary = "binary"
    json = "json"


@dataclasses.dataclass
class ErrorDetail(autoboto.ShapeBase):
    """
    Details about the error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detailed_error_code",
                "DetailedErrorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "detailed_error_message",
                "DetailedErrorMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # A detailed error code.
    detailed_error_code: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A detailed error message.
    detailed_error_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Function(autoboto.ShapeBase):
    """
    Information about a Lambda function.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_arn",
                "FunctionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "function_configuration",
                "FunctionConfiguration",
                autoboto.TypeInfo(FunctionConfiguration),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the Lambda function.
    function_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The configuration of the Lambda function.
    function_configuration: "FunctionConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the Lambda function.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class FunctionConfiguration(autoboto.ShapeBase):
    """
    The configuration of the Lambda function.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encoding_type",
                "EncodingType",
                autoboto.TypeInfo(EncodingType),
            ),
            (
                "environment",
                "Environment",
                autoboto.TypeInfo(FunctionConfigurationEnvironment),
            ),
            (
                "exec_args",
                "ExecArgs",
                autoboto.TypeInfo(str),
            ),
            (
                "executable",
                "Executable",
                autoboto.TypeInfo(str),
            ),
            (
                "memory_size",
                "MemorySize",
                autoboto.TypeInfo(int),
            ),
            (
                "pinned",
                "Pinned",
                autoboto.TypeInfo(bool),
            ),
            (
                "timeout",
                "Timeout",
                autoboto.TypeInfo(int),
            ),
        ]

    # The expected encoding type of the input payload for the function. The
    # default is ''json''.
    encoding_type: "EncodingType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The environment configuration of the function.
    environment: "FunctionConfigurationEnvironment" = dataclasses.field(
        default_factory=dict,
    )

    # The execution arguments.
    exec_args: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the function executable.
    executable: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The memory size, in KB, which the function requires.
    memory_size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # True if the function is pinned. Pinned means the function is long-lived and
    # starts when the core starts.
    pinned: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The allowed function execution time, after which Lambda should terminate
    # the function. This timeout still applies to pinned lambdas for each
    # request.
    timeout: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class FunctionConfigurationEnvironment(autoboto.ShapeBase):
    """
    The environment configuration of the function.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_sysfs",
                "AccessSysfs",
                autoboto.TypeInfo(bool),
            ),
            (
                "resource_access_policies",
                "ResourceAccessPolicies",
                autoboto.TypeInfo(typing.List[ResourceAccessPolicy]),
            ),
            (
                "variables",
                "Variables",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # If true, the Lambda function is allowed to access the host's /sys folder.
    # Use this when the Lambda function needs to read device information from
    # /sys.
    access_sysfs: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of the resources, with their permissions, to which the Lambda
    # function will be granted access. A Lambda function can have at most 10
    # resources.
    resource_access_policies: typing.List["ResourceAccessPolicy"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )

    # Environment variables for the Lambda function's configuration.
    variables: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class FunctionDefinitionVersion(autoboto.ShapeBase):
    """
    Information about a function definition version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "functions",
                "Functions",
                autoboto.TypeInfo(typing.List[Function]),
            ),
        ]

    # A list of Lambda functions in this function definition version.
    functions: typing.List["Function"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GeneralError(autoboto.ShapeBase):
    """
    General error information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_details",
                "ErrorDetails",
                autoboto.TypeInfo(typing.List[ErrorDetail]),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # Details about the error.
    error_details: typing.List["ErrorDetail"] = dataclasses.field(
        default_factory=list,
    )

    # A message containing information about the error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetAssociatedRoleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetAssociatedRoleResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "associated_at",
                "AssociatedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The time when the role was associated with the group.
    associated_at: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the role that is associated with the group.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetConnectivityInfoRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "ThingName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The thing name.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetConnectivityInfoResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connectivity_info",
                "ConnectivityInfo",
                autoboto.TypeInfo(typing.List[ConnectivityInfo]),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # Connectivity info list.
    connectivity_info: typing.List["ConnectivityInfo"] = dataclasses.field(
        default_factory=list,
    )

    # A message about the connectivity info request.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCoreDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "core_definition_id",
                "CoreDefinitionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the core definition.
    core_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetCoreDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the definition.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the definition.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCoreDefinitionVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "core_definition_id",
                "CoreDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "core_definition_version_id",
                "CoreDefinitionVersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the core definition.
    core_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the core definition version.
    core_definition_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetCoreDefinitionVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                autoboto.TypeInfo(CoreDefinitionVersion),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the core definition version.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the core definition version
    # was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the core definition version.
    definition: "CoreDefinitionVersion" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the core definition version.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the core definition version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDeploymentStatusRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_id",
                "DeploymentId",
                autoboto.TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the deployment.
    deployment_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDeploymentStatusResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_status",
                "DeploymentStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "deployment_type",
                "DeploymentType",
                autoboto.TypeInfo(DeploymentType),
            ),
            (
                "error_details",
                "ErrorDetails",
                autoboto.TypeInfo(typing.List[ErrorDetail]),
            ),
            (
                "error_message",
                "ErrorMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "updated_at",
                "UpdatedAt",
                autoboto.TypeInfo(str),
            ),
        ]

    # The status of the deployment.
    deployment_status: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of the deployment.
    deployment_type: "DeploymentType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Error details
    error_details: typing.List["ErrorDetail"] = dataclasses.field(
        default_factory=list,
    )

    # Error message
    error_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time, in milliseconds since the epoch, when the deployment status was
    # updated.
    updated_at: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDeviceDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_definition_id",
                "DeviceDefinitionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the device definition.
    device_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetDeviceDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the definition.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the definition.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDeviceDefinitionVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_definition_id",
                "DeviceDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "device_definition_version_id",
                "DeviceDefinitionVersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the device definition.
    device_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the device definition version.
    device_definition_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetDeviceDefinitionVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                autoboto.TypeInfo(DeviceDefinitionVersion),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the device definition version.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the device definition
    # version was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the device definition version.
    definition: "DeviceDefinitionVersion" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the device definition version.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the device definition version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetFunctionDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_definition_id",
                "FunctionDefinitionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Lambda function definition.
    function_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetFunctionDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the definition.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the definition.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetFunctionDefinitionVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_definition_id",
                "FunctionDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "function_definition_version_id",
                "FunctionDefinitionVersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Lambda function definition.
    function_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the function definition version.
    function_definition_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetFunctionDefinitionVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                autoboto.TypeInfo(FunctionDefinitionVersion),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the function definition version.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the function definition
    # version was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information on the definition.
    definition: "FunctionDefinitionVersion" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the function definition version.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the function definition version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetGroupCertificateAuthorityRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_id",
                "CertificateAuthorityId",
                autoboto.TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the certificate authority.
    certificate_authority_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetGroupCertificateAuthorityResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_certificate_authority_arn",
                "GroupCertificateAuthorityArn",
                autoboto.TypeInfo(str),
            ),
            (
                "group_certificate_authority_id",
                "GroupCertificateAuthorityId",
                autoboto.TypeInfo(str),
            ),
            (
                "pem_encoded_certificate",
                "PemEncodedCertificate",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the certificate authority for the group.
    group_certificate_authority_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the certificate authority for the group.
    group_certificate_authority_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The PEM encoded certificate for the group.
    pem_encoded_certificate: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetGroupCertificateConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetGroupCertificateConfigurationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_expiry_in_milliseconds",
                "CertificateAuthorityExpiryInMilliseconds",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_expiry_in_milliseconds",
                "CertificateExpiryInMilliseconds",
                autoboto.TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The amount of time remaining before the certificate authority expires, in
    # milliseconds.
    certificate_authority_expiry_in_milliseconds: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The amount of time remaining before the certificate expires, in
    # milliseconds.
    certificate_expiry_in_milliseconds: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the group certificate configuration.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the definition.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the definition.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetGroupVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "group_version_id",
                "GroupVersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the group version.
    group_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetGroupVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                autoboto.TypeInfo(GroupVersion),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the group version.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the group version was
    # created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the group version definition.
    definition: "GroupVersion" = dataclasses.field(default_factory=dict, )

    # The ID of the group version.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID for the version of the group.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetLoggerDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logger_definition_id",
                "LoggerDefinitionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the logger definition.
    logger_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetLoggerDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the definition.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the definition.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetLoggerDefinitionVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logger_definition_id",
                "LoggerDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "logger_definition_version_id",
                "LoggerDefinitionVersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the logger definition.
    logger_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the logger definition version.
    logger_definition_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetLoggerDefinitionVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                autoboto.TypeInfo(LoggerDefinitionVersion),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the logger definition version.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the logger definition
    # version was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the logger definition version.
    definition: "LoggerDefinitionVersion" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the logger definition version.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the logger definition version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetResourceDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_definition_id",
                "ResourceDefinitionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the resource definition.
    resource_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetResourceDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the definition.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the definition.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetResourceDefinitionVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_definition_id",
                "ResourceDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_definition_version_id",
                "ResourceDefinitionVersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the resource definition.
    resource_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the resource definition version.
    resource_definition_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetResourceDefinitionVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                autoboto.TypeInfo(ResourceDefinitionVersion),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # Arn of the resource definition version.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the resource definition
    # version was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the definition.
    definition: "ResourceDefinitionVersion" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the resource definition version.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the resource definition version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetServiceRoleForAccountRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetServiceRoleForAccountResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "associated_at",
                "AssociatedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The time when the service role was associated with the account.
    associated_at: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the role which is associated with the account.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetSubscriptionDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_definition_id",
                "SubscriptionDefinitionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the subscription definition.
    subscription_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetSubscriptionDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the definition.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the definition.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetSubscriptionDefinitionVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_definition_id",
                "SubscriptionDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "subscription_definition_version_id",
                "SubscriptionDefinitionVersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the subscription definition.
    subscription_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the subscription definition version.
    subscription_definition_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetSubscriptionDefinitionVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                autoboto.TypeInfo(SubscriptionDefinitionVersion),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the subscription definition version.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the subscription definition
    # version was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the subscription definition version.
    definition: "SubscriptionDefinitionVersion" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the subscription definition version.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the subscription definition version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GroupCertificateAuthorityProperties(autoboto.ShapeBase):
    """
    Information about a certificate authority for a group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_certificate_authority_arn",
                "GroupCertificateAuthorityArn",
                autoboto.TypeInfo(str),
            ),
            (
                "group_certificate_authority_id",
                "GroupCertificateAuthorityId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the certificate authority for the group.
    group_certificate_authority_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the certificate authority for the group.
    group_certificate_authority_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GroupCertificateConfiguration(autoboto.ShapeBase):
    """
    Information about a group certificate configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_expiry_in_milliseconds",
                "CertificateAuthorityExpiryInMilliseconds",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_expiry_in_milliseconds",
                "CertificateExpiryInMilliseconds",
                autoboto.TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The amount of time remaining before the certificate authority expires, in
    # milliseconds.
    certificate_authority_expiry_in_milliseconds: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The amount of time remaining before the certificate expires, in
    # milliseconds.
    certificate_expiry_in_milliseconds: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the group certificate configuration.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GroupInformation(autoboto.ShapeBase):
    """
    Information about a group.
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
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the group.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the group was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the group.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the group was last updated.
    last_updated_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest version of the group.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the latest version of the group.
    latest_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the group.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GroupOwnerSetting(autoboto.ShapeBase):
    """
    Group owner related settings for local resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_add_group_owner",
                "AutoAddGroupOwner",
                autoboto.TypeInfo(bool),
            ),
            (
                "group_owner",
                "GroupOwner",
                autoboto.TypeInfo(str),
            ),
        ]

    # If true, GreenGrass automatically adds the specified Linux OS group owner
    # of the resource to the Lambda process privileges. Thus the Lambda process
    # will have the file access permissions of the added Linux group.
    auto_add_group_owner: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the Linux OS group whose privileges will be added to the Lambda
    # process. This field is optional.
    group_owner: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GroupVersion(autoboto.ShapeBase):
    """
    Information about a group version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "core_definition_version_arn",
                "CoreDefinitionVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "device_definition_version_arn",
                "DeviceDefinitionVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "function_definition_version_arn",
                "FunctionDefinitionVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "logger_definition_version_arn",
                "LoggerDefinitionVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_definition_version_arn",
                "ResourceDefinitionVersionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "subscription_definition_version_arn",
                "SubscriptionDefinitionVersionArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the core definition version for this group.
    core_definition_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the device definition version for this group.
    device_definition_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the function definition version for this group.
    function_definition_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the logger definition version for this group.
    logger_definition_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The resource definition version ARN for this group.
    resource_definition_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the subscription definition version for this group.
    subscription_definition_version_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class InternalServerErrorException(autoboto.ShapeBase):
    """
    General error information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_details",
                "ErrorDetails",
                autoboto.TypeInfo(typing.List[ErrorDetail]),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # Details about the error.
    error_details: typing.List["ErrorDetail"] = dataclasses.field(
        default_factory=list,
    )

    # A message containing information about the error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListCoreDefinitionVersionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "core_definition_id",
                "CoreDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the core definition.
    core_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListCoreDefinitionVersionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "versions",
                "Versions",
                autoboto.TypeInfo(typing.List[VersionInformation]),
            ),
        ]

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information about a version.
    versions: typing.List["VersionInformation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListCoreDefinitionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListCoreDefinitionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "definitions",
                "Definitions",
                autoboto.TypeInfo(typing.List[DefinitionInformation]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about a definition.
    definitions: typing.List["DefinitionInformation"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListDefinitionsResponse(autoboto.ShapeBase):
    """
    A list of definitions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "definitions",
                "Definitions",
                autoboto.TypeInfo(typing.List[DefinitionInformation]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about a definition.
    definitions: typing.List["DefinitionInformation"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListDeploymentsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListDeploymentsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployments",
                "Deployments",
                autoboto.TypeInfo(typing.List[Deployment]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of deployments for the requested groups.
    deployments: typing.List["Deployment"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListDeviceDefinitionVersionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_definition_id",
                "DeviceDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the device definition.
    device_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListDeviceDefinitionVersionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "versions",
                "Versions",
                autoboto.TypeInfo(typing.List[VersionInformation]),
            ),
        ]

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information about a version.
    versions: typing.List["VersionInformation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListDeviceDefinitionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListDeviceDefinitionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "definitions",
                "Definitions",
                autoboto.TypeInfo(typing.List[DefinitionInformation]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about a definition.
    definitions: typing.List["DefinitionInformation"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListFunctionDefinitionVersionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_definition_id",
                "FunctionDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Lambda function definition.
    function_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListFunctionDefinitionVersionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "versions",
                "Versions",
                autoboto.TypeInfo(typing.List[VersionInformation]),
            ),
        ]

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information about a version.
    versions: typing.List["VersionInformation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListFunctionDefinitionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListFunctionDefinitionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "definitions",
                "Definitions",
                autoboto.TypeInfo(typing.List[DefinitionInformation]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about a definition.
    definitions: typing.List["DefinitionInformation"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListGroupCertificateAuthoritiesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListGroupCertificateAuthoritiesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_certificate_authorities",
                "GroupCertificateAuthorities",
                autoboto.TypeInfo(
                    typing.List[GroupCertificateAuthorityProperties]
                ),
            ),
        ]

    # A list of certificate authorities associated with the group.
    group_certificate_authorities: typing.List[
        "GroupCertificateAuthorityProperties"
    ] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListGroupVersionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListGroupVersionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "versions",
                "Versions",
                autoboto.TypeInfo(typing.List[VersionInformation]),
            ),
        ]

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information about a version.
    versions: typing.List["VersionInformation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListGroupsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListGroupsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "groups",
                "Groups",
                autoboto.TypeInfo(typing.List[GroupInformation]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about a group.
    groups: typing.List["GroupInformation"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListLoggerDefinitionVersionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logger_definition_id",
                "LoggerDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the logger definition.
    logger_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListLoggerDefinitionVersionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "versions",
                "Versions",
                autoboto.TypeInfo(typing.List[VersionInformation]),
            ),
        ]

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information about a version.
    versions: typing.List["VersionInformation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListLoggerDefinitionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListLoggerDefinitionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "definitions",
                "Definitions",
                autoboto.TypeInfo(typing.List[DefinitionInformation]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about a definition.
    definitions: typing.List["DefinitionInformation"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListResourceDefinitionVersionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_definition_id",
                "ResourceDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the resource definition.
    resource_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListResourceDefinitionVersionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "versions",
                "Versions",
                autoboto.TypeInfo(typing.List[VersionInformation]),
            ),
        ]

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information about a version.
    versions: typing.List["VersionInformation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListResourceDefinitionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListResourceDefinitionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "definitions",
                "Definitions",
                autoboto.TypeInfo(typing.List[DefinitionInformation]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about a definition.
    definitions: typing.List["DefinitionInformation"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListSubscriptionDefinitionVersionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_definition_id",
                "SubscriptionDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the subscription definition.
    subscription_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListSubscriptionDefinitionVersionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "versions",
                "Versions",
                autoboto.TypeInfo(typing.List[VersionInformation]),
            ),
        ]

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information about a version.
    versions: typing.List["VersionInformation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListSubscriptionDefinitionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListSubscriptionDefinitionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "definitions",
                "Definitions",
                autoboto.TypeInfo(typing.List[DefinitionInformation]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about a definition.
    definitions: typing.List["DefinitionInformation"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListVersionsResponse(autoboto.ShapeBase):
    """
    A list of versions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "versions",
                "Versions",
                autoboto.TypeInfo(typing.List[VersionInformation]),
            ),
        ]

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information about a version.
    versions: typing.List["VersionInformation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class LocalDeviceResourceData(autoboto.ShapeBase):
    """
    Attributes that define a local device resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_owner_setting",
                "GroupOwnerSetting",
                autoboto.TypeInfo(GroupOwnerSetting),
            ),
            (
                "source_path",
                "SourcePath",
                autoboto.TypeInfo(str),
            ),
        ]

    # Group/owner related settings for local resources.
    group_owner_setting: "GroupOwnerSetting" = dataclasses.field(
        default_factory=dict,
    )

    # The local absolute path of the device resource. The source path for a
    # device resource can refer only to a character device or block device under
    # ''/dev''.
    source_path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LocalVolumeResourceData(autoboto.ShapeBase):
    """
    Attributes that define a local volume resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_path",
                "DestinationPath",
                autoboto.TypeInfo(str),
            ),
            (
                "group_owner_setting",
                "GroupOwnerSetting",
                autoboto.TypeInfo(GroupOwnerSetting),
            ),
            (
                "source_path",
                "SourcePath",
                autoboto.TypeInfo(str),
            ),
        ]

    # The absolute local path of the resource inside the lambda environment.
    destination_path: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Allows you to configure additional group privileges for the Lambda process.
    # This field is optional.
    group_owner_setting: "GroupOwnerSetting" = dataclasses.field(
        default_factory=dict,
    )

    # The local absolute path of the volume resource on the host. The source path
    # for a volume resource type cannot start with ''/sys''.
    source_path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Logger(autoboto.ShapeBase):
    """
    Information about a logger
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "component",
                "Component",
                autoboto.TypeInfo(LoggerComponent),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "level",
                "Level",
                autoboto.TypeInfo(LoggerLevel),
            ),
            (
                "space",
                "Space",
                autoboto.TypeInfo(int),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(LoggerType),
            ),
        ]

    # The component that will be subject to logging.
    component: "LoggerComponent" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The id of the logger.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The level of the logs.
    level: "LoggerLevel" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The amount of file space, in KB, to use if the local file system is used
    # for logging purposes.
    space: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of log output which will be used.
    type: "LoggerType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class LoggerComponent(Enum):
    GreengrassSystem = "GreengrassSystem"
    Lambda = "Lambda"


@dataclasses.dataclass
class LoggerDefinitionVersion(autoboto.ShapeBase):
    """
    Information about a logger definition version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "loggers",
                "Loggers",
                autoboto.TypeInfo(typing.List[Logger]),
            ),
        ]

    # A list of loggers.
    loggers: typing.List["Logger"] = dataclasses.field(default_factory=list, )


class LoggerLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"


class LoggerType(Enum):
    FileSystem = "FileSystem"
    AWSCloudWatch = "AWSCloudWatch"


class Permission(Enum):
    """
    The type of permission a function has to access a resource.
    """
    ro = "ro"
    rw = "rw"


@dataclasses.dataclass
class ResetDeploymentsRequest(autoboto.ShapeBase):
    """
    Information needed to reset deployments.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "force",
                "Force",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If true, performs a best-effort only core reset.
    force: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ResetDeploymentsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_arn",
                "DeploymentArn",
                autoboto.TypeInfo(str),
            ),
            (
                "deployment_id",
                "DeploymentId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the deployment.
    deployment_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the deployment.
    deployment_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Resource(autoboto.ShapeBase):
    """
    Information about a resource.
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
                "resource_data_container",
                "ResourceDataContainer",
                autoboto.TypeInfo(ResourceDataContainer),
            ),
        ]

    # The resource ID, used to refer to a resource in the Lambda function
    # configuration. Max length is 128 characters with pattern
    # ''[a-zA-Z0-9:_-]+''. This must be unique within a Greengrass group.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The descriptive resource name, which is displayed on the Greengrass
    # console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''. This
    # must be unique within a Greengrass group.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A container of data for all resource types.
    resource_data_container: "ResourceDataContainer" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ResourceAccessPolicy(autoboto.ShapeBase):
    """
    A policy used by the function to access a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "permission",
                "Permission",
                autoboto.TypeInfo(Permission),
            ),
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The permissions that the Lambda function has to the resource. Can be one of
    # ''rw'' (read/write) or ''ro'' (read-only).
    permission: "Permission" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the resource. (This ID is assigned to the resource when you
    # create the resource definiton.)
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ResourceDataContainer(autoboto.ShapeBase):
    """
    A container for resource data. The container takes only one of the following
    supported resource data types: ''LocalDeviceResourceData'',
    ''LocalVolumeResourceData'', ''SageMakerMachineLearningModelResourceData'',
    ''S3MachineLearningModelResourceData''.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "local_device_resource_data",
                "LocalDeviceResourceData",
                autoboto.TypeInfo(LocalDeviceResourceData),
            ),
            (
                "local_volume_resource_data",
                "LocalVolumeResourceData",
                autoboto.TypeInfo(LocalVolumeResourceData),
            ),
            (
                "s3_machine_learning_model_resource_data",
                "S3MachineLearningModelResourceData",
                autoboto.TypeInfo(S3MachineLearningModelResourceData),
            ),
            (
                "sage_maker_machine_learning_model_resource_data",
                "SageMakerMachineLearningModelResourceData",
                autoboto.TypeInfo(SageMakerMachineLearningModelResourceData),
            ),
        ]

    # Attributes that define the local device resource.
    local_device_resource_data: "LocalDeviceResourceData" = dataclasses.field(
        default_factory=dict,
    )

    # Attributes that define the local volume resource.
    local_volume_resource_data: "LocalVolumeResourceData" = dataclasses.field(
        default_factory=dict,
    )

    # Attributes that define an S3 machine learning resource.
    s3_machine_learning_model_resource_data: "S3MachineLearningModelResourceData" = dataclasses.field(
        default_factory=dict,
    )

    # Attributes that define an SageMaker machine learning resource.
    sage_maker_machine_learning_model_resource_data: "SageMakerMachineLearningModelResourceData" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ResourceDefinitionVersion(autoboto.ShapeBase):
    """
    Information about a resource definition version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resources",
                "Resources",
                autoboto.TypeInfo(typing.List[Resource]),
            ),
        ]

    # A list of resources.
    resources: typing.List["Resource"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class S3MachineLearningModelResourceData(autoboto.ShapeBase):
    """
    Attributes that define an S3 machine learning resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_path",
                "DestinationPath",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_uri",
                "S3Uri",
                autoboto.TypeInfo(str),
            ),
        ]

    # The absolute local path of the resource inside the Lambda environment.
    destination_path: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URI of the source model in an S3 bucket. The model package must be in
    # tar.gz or .zip format.
    s3_uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SageMakerMachineLearningModelResourceData(autoboto.ShapeBase):
    """
    Attributes that define an SageMaker machine learning resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_path",
                "DestinationPath",
                autoboto.TypeInfo(str),
            ),
            (
                "sage_maker_job_arn",
                "SageMakerJobArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The absolute local path of the resource inside the Lambda environment.
    destination_path: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the SageMaker training job that represents the source model.
    sage_maker_job_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class SoftwareToUpdate(Enum):
    """
    The piece of software on the Greengrass core that will be updated.
    """
    core = "core"
    ota_agent = "ota_agent"


@dataclasses.dataclass
class Subscription(autoboto.ShapeBase):
    """
    Information about a subscription.
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
                "source",
                "Source",
                autoboto.TypeInfo(str),
            ),
            (
                "subject",
                "Subject",
                autoboto.TypeInfo(str),
            ),
            (
                "target",
                "Target",
                autoboto.TypeInfo(str),
            ),
        ]

    # The id of the subscription.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The source of the subscription. Can be a thing ARN, a Lambda function ARN,
    # 'cloud' (which represents the IoT cloud), or 'GGShadowService'.
    source: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The subject of the message.
    subject: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Where the message is sent to. Can be a thing ARN, a Lambda function ARN,
    # 'cloud' (which represents the IoT cloud), or 'GGShadowService'.
    target: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SubscriptionDefinitionVersion(autoboto.ShapeBase):
    """
    Information about a subscription definition version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscriptions",
                "Subscriptions",
                autoboto.TypeInfo(typing.List[Subscription]),
            ),
        ]

    # A list of subscriptions.
    subscriptions: typing.List["Subscription"] = dataclasses.field(
        default_factory=list,
    )


class UpdateAgentLogLevel(Enum):
    """
    The minimum level of log statements that should be logged by the OTA Agent
    during an update.
    """
    NONE = "NONE"
    TRACE = "TRACE"
    DEBUG = "DEBUG"
    VERBOSE = "VERBOSE"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"


@dataclasses.dataclass
class UpdateConnectivityInfoRequest(autoboto.ShapeBase):
    """
    Connectivity information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "ThingName",
                autoboto.TypeInfo(str),
            ),
            (
                "connectivity_info",
                "ConnectivityInfo",
                autoboto.TypeInfo(typing.List[ConnectivityInfo]),
            ),
        ]

    # The thing name.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of connectivity info.
    connectivity_info: typing.List["ConnectivityInfo"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateConnectivityInfoResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # A message about the connectivity info update request.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new version of the connectivity info.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateCoreDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "core_definition_id",
                "CoreDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the core definition.
    core_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateCoreDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateDeviceDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_definition_id",
                "DeviceDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the device definition.
    device_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateDeviceDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateFunctionDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_definition_id",
                "FunctionDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Lambda function definition.
    function_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateFunctionDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateGroupCertificateConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_expiry_in_milliseconds",
                "CertificateExpiryInMilliseconds",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The amount of time remaining before the certificate expires, in
    # milliseconds.
    certificate_expiry_in_milliseconds: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateGroupCertificateConfigurationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_expiry_in_milliseconds",
                "CertificateAuthorityExpiryInMilliseconds",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_expiry_in_milliseconds",
                "CertificateExpiryInMilliseconds",
                autoboto.TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The amount of time remaining before the certificate authority expires, in
    # milliseconds.
    certificate_authority_expiry_in_milliseconds: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The amount of time remaining before the certificate expires, in
    # milliseconds.
    certificate_expiry_in_milliseconds: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the group certificate configuration.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateLoggerDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logger_definition_id",
                "LoggerDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the logger definition.
    logger_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateLoggerDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateResourceDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_definition_id",
                "ResourceDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the resource definition.
    resource_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateResourceDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateSubscriptionDefinitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_definition_id",
                "SubscriptionDefinitionId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the subscription definition.
    subscription_definition_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateSubscriptionDefinitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


class UpdateTargetsArchitecture(Enum):
    """
    The architecture of the cores which are the targets of an update.
    """
    armv7l = "armv7l"
    x86_64 = "x86_64"
    aarch64 = "aarch64"


class UpdateTargetsOperatingSystem(Enum):
    """
    The operating system of the cores which are the targets of an update.
    """
    ubuntu = "ubuntu"
    raspbian = "raspbian"
    amazon_linux = "amazon_linux"


@dataclasses.dataclass
class VersionInformation(autoboto.ShapeBase):
    """
    Information about a version.
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
                "creation_timestamp",
                "CreationTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the version.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the version was created.
    creation_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the version.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID of the version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
