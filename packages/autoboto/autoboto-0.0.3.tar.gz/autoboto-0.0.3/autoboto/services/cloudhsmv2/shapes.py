import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class Backup(autoboto.ShapeBase):
    """
    Contains information about a backup of an AWS CloudHSM cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "backup_id",
                "BackupId",
                autoboto.TypeInfo(str),
            ),
            (
                "backup_state",
                "BackupState",
                autoboto.TypeInfo(BackupState),
            ),
            (
                "cluster_id",
                "ClusterId",
                autoboto.TypeInfo(str),
            ),
            (
                "create_timestamp",
                "CreateTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "copy_timestamp",
                "CopyTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "source_region",
                "SourceRegion",
                autoboto.TypeInfo(str),
            ),
            (
                "source_backup",
                "SourceBackup",
                autoboto.TypeInfo(str),
            ),
            (
                "source_cluster",
                "SourceCluster",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier (ID) of the backup.
    backup_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The state of the backup.
    backup_state: "BackupState" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The identifier (ID) of the cluster that was backed up.
    cluster_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date and time when the backup was created.
    create_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
    copy_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
    source_region: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
    source_backup: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
    source_cluster: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class BackupPolicy(Enum):
    DEFAULT = "DEFAULT"


class BackupState(Enum):
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    READY = "READY"
    DELETED = "DELETED"


@dataclasses.dataclass
class Certificates(autoboto.ShapeBase):
    """
    Contains one or more certificates or a certificate signing request (CSR).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_csr",
                "ClusterCsr",
                autoboto.TypeInfo(str),
            ),
            (
                "hsm_certificate",
                "HsmCertificate",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_hardware_certificate",
                "AwsHardwareCertificate",
                autoboto.TypeInfo(str),
            ),
            (
                "manufacturer_hardware_certificate",
                "ManufacturerHardwareCertificate",
                autoboto.TypeInfo(str),
            ),
            (
                "cluster_certificate",
                "ClusterCertificate",
                autoboto.TypeInfo(str),
            ),
        ]

    # The cluster's certificate signing request (CSR). The CSR exists only when
    # the cluster's state is `UNINITIALIZED`.
    cluster_csr: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The HSM certificate issued (signed) by the HSM hardware.
    hsm_certificate: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The HSM hardware certificate issued (signed) by AWS CloudHSM.
    aws_hardware_certificate: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The HSM hardware certificate issued (signed) by the hardware manufacturer.
    manufacturer_hardware_certificate: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The cluster certificate issued (signed) by the issuing certificate
    # authority (CA) of the cluster's owner.
    cluster_certificate: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CloudHsmAccessDeniedException(autoboto.ShapeBase):
    """
    The request was rejected because the requester does not have permission to
    perform the requested operation.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CloudHsmInternalFailureException(autoboto.ShapeBase):
    """
    The request was rejected because of an AWS CloudHSM internal failure. The
    request can be retried.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CloudHsmInvalidRequestException(autoboto.ShapeBase):
    """
    The request was rejected because it is not a valid request.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CloudHsmResourceNotFoundException(autoboto.ShapeBase):
    """
    The request was rejected because it refers to a resource that cannot be found.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CloudHsmServiceException(autoboto.ShapeBase):
    """
    The request was rejected because an error occurred.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Cluster(autoboto.ShapeBase):
    """
    Contains information about an AWS CloudHSM cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "backup_policy",
                "BackupPolicy",
                autoboto.TypeInfo(BackupPolicy),
            ),
            (
                "cluster_id",
                "ClusterId",
                autoboto.TypeInfo(str),
            ),
            (
                "create_timestamp",
                "CreateTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "hsms",
                "Hsms",
                autoboto.TypeInfo(typing.List[Hsm]),
            ),
            (
                "hsm_type",
                "HsmType",
                autoboto.TypeInfo(str),
            ),
            (
                "pre_co_password",
                "PreCoPassword",
                autoboto.TypeInfo(str),
            ),
            (
                "security_group",
                "SecurityGroup",
                autoboto.TypeInfo(str),
            ),
            (
                "source_backup_id",
                "SourceBackupId",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(ClusterState),
            ),
            (
                "state_message",
                "StateMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_mapping",
                "SubnetMapping",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "vpc_id",
                "VpcId",
                autoboto.TypeInfo(str),
            ),
            (
                "certificates",
                "Certificates",
                autoboto.TypeInfo(Certificates),
            ),
        ]

    # The cluster's backup policy.
    backup_policy: "BackupPolicy" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The cluster's identifier (ID).
    cluster_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date and time when the cluster was created.
    create_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Contains information about the HSMs in the cluster.
    hsms: typing.List["Hsm"] = dataclasses.field(default_factory=list, )

    # The type of HSM that the cluster contains.
    hsm_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The default password for the cluster's Pre-Crypto Officer (PRECO) user.
    pre_co_password: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The identifier (ID) of the cluster's security group.
    security_group: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The identifier (ID) of the backup used to create the cluster. This value
    # exists only when the cluster was created from a backup.
    source_backup_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The cluster's state.
    state: "ClusterState" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the cluster's state.
    state_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A map of the cluster's subnets and their corresponding Availability Zones.
    subnet_mapping: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The identifier (ID) of the virtual private cloud (VPC) that contains the
    # cluster.
    vpc_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Contains one or more certificates or a certificate signing request (CSR).
    certificates: "Certificates" = dataclasses.field(default_factory=dict, )


class ClusterState(Enum):
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    UNINITIALIZED = "UNINITIALIZED"
    INITIALIZE_IN_PROGRESS = "INITIALIZE_IN_PROGRESS"
    INITIALIZED = "INITIALIZED"
    ACTIVE = "ACTIVE"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETED = "DELETED"
    DEGRADED = "DEGRADED"


@dataclasses.dataclass
class CopyBackupToRegionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_region",
                "DestinationRegion",
                autoboto.TypeInfo(str),
            ),
            (
                "backup_id",
                "BackupId",
                autoboto.TypeInfo(str),
            ),
        ]

    destination_region: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
    backup_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CopyBackupToRegionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_backup",
                "DestinationBackup",
                autoboto.TypeInfo(DestinationBackup),
            ),
        ]

    destination_backup: "DestinationBackup" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateClusterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_ids",
                "SubnetIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "hsm_type",
                "HsmType",
                autoboto.TypeInfo(str),
            ),
            (
                "source_backup_id",
                "SourceBackupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifiers (IDs) of the subnets where you are creating the cluster.
    # You must specify at least one subnet. If you specify multiple subnets, they
    # must meet the following criteria:

    #   * All subnets must be in the same virtual private cloud (VPC).

    #   * You can specify only one subnet per Availability Zone.
    subnet_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The type of HSM to use in the cluster. Currently the only allowed value is
    # `hsm1.medium`.
    hsm_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identifier (ID) of the cluster backup to restore. Use this value to
    # restore the cluster from a backup instead of creating a new cluster. To
    # find the backup ID, use DescribeBackups.
    source_backup_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateClusterResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster",
                "Cluster",
                autoboto.TypeInfo(Cluster),
            ),
        ]

    # Information about the cluster that was created.
    cluster: "Cluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateHsmRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "ip_address",
                "IpAddress",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier (ID) of the HSM's cluster. To find the cluster ID, use
    # DescribeClusters.
    cluster_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Availability Zone where you are creating the HSM. To find the cluster's
    # Availability Zones, use DescribeClusters.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The HSM's IP address. If you specify an IP address, use an available
    # address from the subnet that maps to the Availability Zone where you are
    # creating the HSM. If you don't specify an IP address, one is chosen for you
    # from that subnet.
    ip_address: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateHsmResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm",
                "Hsm",
                autoboto.TypeInfo(Hsm),
            ),
        ]

    # Information about the HSM that was created.
    hsm: "Hsm" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteClusterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier (ID) of the cluster that you are deleting. To find the
    # cluster ID, use DescribeClusters.
    cluster_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteClusterResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster",
                "Cluster",
                autoboto.TypeInfo(Cluster),
            ),
        ]

    # Information about the cluster that was deleted.
    cluster: "Cluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteHsmRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                autoboto.TypeInfo(str),
            ),
            (
                "hsm_id",
                "HsmId",
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
        ]

    # The identifier (ID) of the cluster that contains the HSM that you are
    # deleting.
    cluster_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identifier (ID) of the HSM that you are deleting.
    hsm_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identifier (ID) of the elastic network interface (ENI) of the HSM that
    # you are deleting.
    eni_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The IP address of the elastic network interface (ENI) of the HSM that you
    # are deleting.
    eni_ip: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteHsmResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_id",
                "HsmId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier (ID) of the HSM that was deleted.
    hsm_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeBackupsRequest(autoboto.ShapeBase):
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
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "sort_ascending",
                "SortAscending",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The `NextToken` value that you received in the previous response. Use this
    # value to get more backups.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of backups to return in the response. When there are
    # more backups than the number you specify, the response contains a
    # `NextToken` value.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # One or more filters to limit the items returned in the response.

    # Use the `backupIds` filter to return only the specified backups. Specify
    # backups by their backup identifier (ID).

    # Use the `clusterIds` filter to return only the backups for the specified
    # clusters. Specify clusters by their cluster identifier (ID).

    # Use the `states` filter to return only backups that match the specified
    # state.
    filters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
    sort_ascending: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeBackupsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "backups",
                "Backups",
                autoboto.TypeInfo(typing.List[Backup]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of backups.
    backups: typing.List["Backup"] = dataclasses.field(default_factory=list, )

    # An opaque string that indicates that the response contains only a subset of
    # backups. Use this value in a subsequent `DescribeBackups` request to get
    # more backups.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeClustersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
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

    # One or more filters to limit the items returned in the response.

    # Use the `clusterIds` filter to return only the specified clusters. Specify
    # clusters by their cluster identifier (ID).

    # Use the `vpcIds` filter to return only the clusters in the specified
    # virtual private clouds (VPCs). Specify VPCs by their VPC identifier (ID).

    # Use the `states` filter to return only clusters that match the specified
    # state.
    filters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The `NextToken` value that you received in the previous response. Use this
    # value to get more clusters.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of clusters to return in the response. When there are
    # more clusters than the number you specify, the response contains a
    # `NextToken` value.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeClustersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "clusters",
                "Clusters",
                autoboto.TypeInfo(typing.List[Cluster]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of clusters.
    clusters: typing.List["Cluster"] = dataclasses.field(default_factory=list, )

    # An opaque string that indicates that the response contains only a subset of
    # clusters. Use this value in a subsequent `DescribeClusters` request to get
    # more clusters.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DestinationBackup(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "create_timestamp",
                "CreateTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "source_region",
                "SourceRegion",
                autoboto.TypeInfo(str),
            ),
            (
                "source_backup",
                "SourceBackup",
                autoboto.TypeInfo(str),
            ),
            (
                "source_cluster",
                "SourceCluster",
                autoboto.TypeInfo(str),
            ),
        ]

    create_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
    source_region: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
    source_backup: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
    source_cluster: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Hsm(autoboto.ShapeBase):
    """
    Contains information about a hardware security module (HSM) in an AWS CloudHSM
    cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_id",
                "HsmId",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "cluster_id",
                "ClusterId",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_id",
                "SubnetId",
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
                "state",
                "State",
                autoboto.TypeInfo(HsmState),
            ),
            (
                "state_message",
                "StateMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The HSM's identifier (ID).
    hsm_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Availability Zone that contains the HSM.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The identifier (ID) of the cluster that contains the HSM.
    cluster_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The subnet that contains the HSM's elastic network interface (ENI).
    subnet_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identifier (ID) of the HSM's elastic network interface (ENI).
    eni_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The IP address of the HSM's elastic network interface (ENI).
    eni_ip: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The HSM's state.
    state: "HsmState" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A description of the HSM's state.
    state_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class HsmState(Enum):
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    ACTIVE = "ACTIVE"
    DEGRADED = "DEGRADED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETED = "DELETED"


@dataclasses.dataclass
class InitializeClusterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                autoboto.TypeInfo(str),
            ),
            (
                "signed_cert",
                "SignedCert",
                autoboto.TypeInfo(str),
            ),
            (
                "trust_anchor",
                "TrustAnchor",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier (ID) of the cluster that you are claiming. To find the
    # cluster ID, use DescribeClusters.
    cluster_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The cluster certificate issued (signed) by your issuing certificate
    # authority (CA). The certificate must be in PEM format and can contain a
    # maximum of 5000 characters.
    signed_cert: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The issuing certificate of the issuing certificate authority (CA) that
    # issued (signed) the cluster certificate. This can be a root (self-signed)
    # certificate or a certificate chain that begins with the certificate that
    # issued the cluster certificate and ends with a root certificate. The
    # certificate or certificate chain must be in PEM format and can contain a
    # maximum of 5000 characters.
    trust_anchor: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InitializeClusterResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "State",
                autoboto.TypeInfo(ClusterState),
            ),
            (
                "state_message",
                "StateMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The cluster's state.
    state: "ClusterState" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the cluster's state.
    state_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListTagsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
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

    # The cluster identifier (ID) for the cluster whose tags you are getting. To
    # find the cluster ID, use DescribeClusters.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The `NextToken` value that you received in the previous response. Use this
    # value to get more tags.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of tags to return in the response. When there are more
    # tags than the number you specify, the response contains a `NextToken`
    # value.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListTagsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_list",
                "TagList",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of tags.
    tag_list: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # An opaque string that indicates that the response contains only a subset of
    # tags. Use this value in a subsequent `ListTags` request to get more tags.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    """
    Contains a tag. A tag is a key-value pair.
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


@dataclasses.dataclass
class TagResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_list",
                "TagList",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The cluster identifier (ID) for the cluster that you are tagging. To find
    # the cluster ID, use DescribeClusters.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of one or more tags.
    tag_list: typing.List["Tag"] = dataclasses.field(default_factory=list, )


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
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_key_list",
                "TagKeyList",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The cluster identifier (ID) for the cluster whose tags you are removing. To
    # find the cluster ID, use DescribeClusters.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of one or more tag keys for the tags that you are removing. Specify
    # only the tag keys, not the tag values.
    tag_key_list: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UntagResourceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []
