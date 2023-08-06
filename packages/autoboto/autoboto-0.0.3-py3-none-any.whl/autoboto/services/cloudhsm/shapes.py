import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AddTagsToResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_list",
                "TagList",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS CloudHSM resource to tag.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # One or more tags.
    tag_list: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class AddTagsToResourceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
        ]

    # The status of the operation.
    status: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class ClientVersion(Enum):
    5_1 = "5.1"
    5_3 = "5.3"


@dataclasses.dataclass
class CloudHsmInternalException(autoboto.ShapeBase):
    """
    Indicates that an internal error occurred.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class CloudHsmObjectState(Enum):
    READY = "READY"
    UPDATING = "UPDATING"
    DEGRADED = "DEGRADED"


@dataclasses.dataclass
class CloudHsmServiceException(autoboto.ShapeBase):
    """
    Indicates that an exception occurred in the AWS CloudHSM service.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "retryable",
                "retryable",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Additional information about the error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Indicates if the action can be retried.
    retryable: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateHapgRequest(autoboto.ShapeBase):
    """
    Contains the inputs for the CreateHapgRequest action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "label",
                "Label",
                autoboto.TypeInfo(str),
            ),
        ]

    # The label of the new high-availability partition group.
    label: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateHapgResponse(autoboto.ShapeBase):
    """
    Contains the output of the CreateHAPartitionGroup action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hapg_arn",
                "HapgArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the high-availability partition group.
    hapg_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateHsmRequest(autoboto.ShapeBase):
    """
    Contains the inputs for the `CreateHsm` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_id",
                "SubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_key",
                "SshKey",
                autoboto.TypeInfo(str),
            ),
            (
                "iam_role_arn",
                "IamRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "subscription_type",
                "SubscriptionType",
                autoboto.TypeInfo(SubscriptionType),
            ),
            (
                "eni_ip",
                "EniIp",
                autoboto.TypeInfo(str),
            ),
            (
                "external_id",
                "ExternalId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_token",
                "ClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "syslog_ip",
                "SyslogIp",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier of the subnet in your VPC in which to place the HSM.
    subnet_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The SSH public key to install on the HSM.
    ssh_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of an IAM role to enable the AWS CloudHSM service to allocate an
    # ENI on your behalf.
    iam_role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the type of subscription for the HSM.

    #   * **PRODUCTION** \- The HSM is being used in a production environment.

    #   * **TRIAL** \- The HSM is being used in a product trial.
    subscription_type: "SubscriptionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IP address to assign to the HSM's ENI.

    # If an IP address is not specified, an IP address will be randomly chosen
    # from the CIDR range of the subnet.
    eni_ip: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The external ID from `IamRoleArn`, if present.
    external_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A user-defined token to ensure idempotence. Subsequent calls to this
    # operation with the same token will be ignored.
    client_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The IP address for the syslog monitoring server. The AWS CloudHSM service
    # only supports one syslog monitoring server.
    syslog_ip: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateHsmResponse(autoboto.ShapeBase):
    """
    Contains the output of the `CreateHsm` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_arn",
                "HsmArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the HSM.
    hsm_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateLunaClientRequest(autoboto.ShapeBase):
    """
    Contains the inputs for the CreateLunaClient action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate",
                "Certificate",
                autoboto.TypeInfo(str),
            ),
            (
                "label",
                "Label",
                autoboto.TypeInfo(str),
            ),
        ]

    # The contents of a Base64-Encoded X.509 v3 certificate to be installed on
    # the HSMs used by this client.
    certificate: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The label for the client.
    label: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateLunaClientResponse(autoboto.ShapeBase):
    """
    Contains the output of the CreateLunaClient action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_arn",
                "ClientArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the client.
    client_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteHapgRequest(autoboto.ShapeBase):
    """
    Contains the inputs for the DeleteHapg action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hapg_arn",
                "HapgArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the high-availability partition group to delete.
    hapg_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteHapgResponse(autoboto.ShapeBase):
    """
    Contains the output of the DeleteHapg action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
        ]

    # The status of the action.
    status: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteHsmRequest(autoboto.ShapeBase):
    """
    Contains the inputs for the DeleteHsm operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_arn",
                "HsmArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the HSM to delete.
    hsm_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteHsmResponse(autoboto.ShapeBase):
    """
    Contains the output of the DeleteHsm operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
        ]

    # The status of the operation.
    status: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteLunaClientRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_arn",
                "ClientArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the client to delete.
    client_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteLunaClientResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
        ]

    # The status of the action.
    status: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeHapgRequest(autoboto.ShapeBase):
    """
    Contains the inputs for the DescribeHapg action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hapg_arn",
                "HapgArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the high-availability partition group to describe.
    hapg_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeHapgResponse(autoboto.ShapeBase):
    """
    Contains the output of the DescribeHapg action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hapg_arn",
                "HapgArn",
                autoboto.TypeInfo(str),
            ),
            (
                "hapg_serial",
                "HapgSerial",
                autoboto.TypeInfo(str),
            ),
            (
                "hsms_last_action_failed",
                "HsmsLastActionFailed",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "hsms_pending_deletion",
                "HsmsPendingDeletion",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "hsms_pending_registration",
                "HsmsPendingRegistration",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "label",
                "Label",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_timestamp",
                "LastModifiedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "partition_serial_list",
                "PartitionSerialList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(CloudHsmObjectState),
            ),
        ]

    # The ARN of the high-availability partition group.
    hapg_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The serial number of the high-availability partition group.
    hapg_serial: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    hsms_last_action_failed: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    hsms_pending_deletion: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    hsms_pending_registration: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The label for the high-availability partition group.
    label: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date and time the high-availability partition group was last modified.
    last_modified_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The list of partition serial numbers that belong to the high-availability
    # partition group.
    partition_serial_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The state of the high-availability partition group.
    state: "CloudHsmObjectState" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeHsmRequest(autoboto.ShapeBase):
    """
    Contains the inputs for the DescribeHsm operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_arn",
                "HsmArn",
                autoboto.TypeInfo(str),
            ),
            (
                "hsm_serial_number",
                "HsmSerialNumber",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the HSM. Either the `HsmArn` or the `SerialNumber` parameter
    # must be specified.
    hsm_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The serial number of the HSM. Either the `HsmArn` or the `HsmSerialNumber`
    # parameter must be specified.
    hsm_serial_number: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeHsmResponse(autoboto.ShapeBase):
    """
    Contains the output of the DescribeHsm operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_arn",
                "HsmArn",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(HsmStatus),
            ),
            (
                "status_details",
                "StatusDetails",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "eni_id",
                "EniId",
                autoboto.TypeInfo(str),
            ),
            (
                "eni_ip",
                "EniIp",
                autoboto.TypeInfo(str),
            ),
            (
                "subscription_type",
                "SubscriptionType",
                autoboto.TypeInfo(SubscriptionType),
            ),
            (
                "subscription_start_date",
                "SubscriptionStartDate",
                autoboto.TypeInfo(str),
            ),
            (
                "subscription_end_date",
                "SubscriptionEndDate",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_id",
                "SubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "iam_role_arn",
                "IamRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "serial_number",
                "SerialNumber",
                autoboto.TypeInfo(str),
            ),
            (
                "vendor_name",
                "VendorName",
                autoboto.TypeInfo(str),
            ),
            (
                "hsm_type",
                "HsmType",
                autoboto.TypeInfo(str),
            ),
            (
                "software_version",
                "SoftwareVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "SshPublicKey",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_key_last_updated",
                "SshKeyLastUpdated",
                autoboto.TypeInfo(str),
            ),
            (
                "server_cert_uri",
                "ServerCertUri",
                autoboto.TypeInfo(str),
            ),
            (
                "server_cert_last_updated",
                "ServerCertLastUpdated",
                autoboto.TypeInfo(str),
            ),
            (
                "partitions",
                "Partitions",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN of the HSM.
    hsm_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the HSM.
    status: "HsmStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Contains additional information about the status of the HSM.
    status_details: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Availability Zone that the HSM is in.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The identifier of the elastic network interface (ENI) attached to the HSM.
    eni_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The IP address assigned to the HSM's ENI.
    eni_ip: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the type of subscription for the HSM.

    #   * **PRODUCTION** \- The HSM is being used in a production environment.

    #   * **TRIAL** \- The HSM is being used in a product trial.
    subscription_type: "SubscriptionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The subscription start date.
    subscription_start_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The subscription end date.
    subscription_end_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The identifier of the VPC that the HSM is in.
    vpc_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identifier of the subnet that the HSM is in.
    subnet_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the IAM role assigned to the HSM.
    iam_role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The serial number of the HSM.
    serial_number: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the HSM vendor.
    vendor_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The HSM model type.
    hsm_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The HSM software version.
    software_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The public SSH key.
    ssh_public_key: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time that the SSH key was last updated.
    ssh_key_last_updated: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URI of the certificate server.
    server_cert_uri: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time that the server certificate was last updated.
    server_cert_last_updated: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The list of partitions on the HSM.
    partitions: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeLunaClientRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_arn",
                "ClientArn",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_fingerprint",
                "CertificateFingerprint",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the client.
    client_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The certificate fingerprint.
    certificate_fingerprint: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeLunaClientResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_arn",
                "ClientArn",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate",
                "Certificate",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_fingerprint",
                "CertificateFingerprint",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_timestamp",
                "LastModifiedTimestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "label",
                "Label",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the client.
    client_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The certificate installed on the HSMs used by this client.
    certificate: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The certificate fingerprint.
    certificate_fingerprint: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time the client was last modified.
    last_modified_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The label of the client.
    label: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetConfigRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_arn",
                "ClientArn",
                autoboto.TypeInfo(str),
            ),
            (
                "client_version",
                "ClientVersion",
                autoboto.TypeInfo(ClientVersion),
            ),
            (
                "hapg_list",
                "HapgList",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN of the client.
    client_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The client version.
    client_version: "ClientVersion" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of ARNs that identify the high-availability partition groups that
    # are associated with the client.
    hapg_list: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class GetConfigResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "config_type",
                "ConfigType",
                autoboto.TypeInfo(str),
            ),
            (
                "config_file",
                "ConfigFile",
                autoboto.TypeInfo(str),
            ),
            (
                "config_cred",
                "ConfigCred",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of credentials.
    config_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The chrystoki.conf configuration file.
    config_file: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The certificate file containing the server.pem files of the HSMs.
    config_cred: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class HsmStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    UPDATING = "UPDATING"
    SUSPENDED = "SUSPENDED"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"
    DEGRADED = "DEGRADED"


@dataclasses.dataclass
class InvalidRequestException(autoboto.ShapeBase):
    """
    Indicates that one or more of the request parameters are not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListAvailableZonesRequest(autoboto.ShapeBase):
    """
    Contains the inputs for the ListAvailableZones action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListAvailableZonesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "az_list",
                "AZList",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The list of Availability Zones that have available AWS CloudHSM capacity.
    az_list: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class ListHapgsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `NextToken` value from a previous call to `ListHapgs`. Pass null if
    # this is the first call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListHapgsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hapg_list",
                "HapgList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of high-availability partition groups.
    hapg_list: typing.List[str] = dataclasses.field(default_factory=list, )

    # If not null, more results are available. Pass this value to `ListHapgs` to
    # retrieve the next set of items.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListHsmsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `NextToken` value from a previous call to `ListHsms`. Pass null if this
    # is the first call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListHsmsResponse(autoboto.ShapeBase):
    """
    Contains the output of the `ListHsms` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_list",
                "HsmList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of ARNs that identify the HSMs.
    hsm_list: typing.List[str] = dataclasses.field(default_factory=list, )

    # If not null, more results are available. Pass this value to `ListHsms` to
    # retrieve the next set of items.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListLunaClientsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `NextToken` value from a previous call to `ListLunaClients`. Pass null
    # if this is the first call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListLunaClientsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_list",
                "ClientList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of clients.
    client_list: typing.List[str] = dataclasses.field(default_factory=list, )

    # If not null, more results are available. Pass this to `ListLunaClients` to
    # retrieve the next set of items.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


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

    # The Amazon Resource Name (ARN) of the AWS CloudHSM resource.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_list",
                "TagList",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # One or more tags.
    tag_list: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class ModifyHapgRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hapg_arn",
                "HapgArn",
                autoboto.TypeInfo(str),
            ),
            (
                "label",
                "Label",
                autoboto.TypeInfo(str),
            ),
            (
                "partition_serial_list",
                "PartitionSerialList",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN of the high-availability partition group to modify.
    hapg_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new label for the high-availability partition group.
    label: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The list of partition serial numbers to make members of the high-
    # availability partition group.
    partition_serial_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ModifyHapgResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hapg_arn",
                "HapgArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the high-availability partition group.
    hapg_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ModifyHsmRequest(autoboto.ShapeBase):
    """
    Contains the inputs for the ModifyHsm operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_arn",
                "HsmArn",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_id",
                "SubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "eni_ip",
                "EniIp",
                autoboto.TypeInfo(str),
            ),
            (
                "iam_role_arn",
                "IamRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "external_id",
                "ExternalId",
                autoboto.TypeInfo(str),
            ),
            (
                "syslog_ip",
                "SyslogIp",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the HSM to modify.
    hsm_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new identifier of the subnet that the HSM is in. The new subnet must be
    # in the same Availability Zone as the current subnet.
    subnet_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new IP address for the elastic network interface (ENI) attached to the
    # HSM.

    # If the HSM is moved to a different subnet, and an IP address is not
    # specified, an IP address will be randomly chosen from the CIDR range of the
    # new subnet.
    eni_ip: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new IAM role ARN.
    iam_role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new external ID.
    external_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new IP address for the syslog monitoring server. The AWS CloudHSM
    # service only supports one syslog monitoring server.
    syslog_ip: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ModifyHsmResponse(autoboto.ShapeBase):
    """
    Contains the output of the ModifyHsm operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_arn",
                "HsmArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the HSM.
    hsm_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ModifyLunaClientRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_arn",
                "ClientArn",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate",
                "Certificate",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the client.
    client_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new certificate for the client.
    certificate: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ModifyLunaClientResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_arn",
                "ClientArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the client.
    client_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RemoveTagsFromResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_key_list",
                "TagKeyList",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS CloudHSM resource.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The tag key or keys to remove.

    # Specify only the tag key to remove (not the value). To overwrite the value
    # for an existing tag, use AddTagsToResource.
    tag_key_list: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class RemoveTagsFromResourceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
        ]

    # The status of the operation.
    status: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class SubscriptionType(Enum):
    """
    Specifies the type of subscription for the HSM.

      * **PRODUCTION** \- The HSM is being used in a production environment.

      * **TRIAL** \- The HSM is being used in a product trial.
    """
    PRODUCTION = "PRODUCTION"


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    """
    A key-value pair that identifies or specifies metadata about an AWS CloudHSM
    resource.
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

    # The key of the tag.
    key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value of the tag.
    value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
