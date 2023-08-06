import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class Connector(autoboto.ShapeBase):
    """
    Object representing a Connector
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connector_id",
                "connectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(ConnectorStatus),
            ),
            (
                "capability_list",
                "capabilityList",
                autoboto.TypeInfo(typing.List[ConnectorCapability]),
            ),
            (
                "vm_manager_name",
                "vmManagerName",
                autoboto.TypeInfo(str),
            ),
            (
                "vm_manager_type",
                "vmManagerType",
                autoboto.TypeInfo(VmManagerType),
            ),
            (
                "vm_manager_id",
                "vmManagerId",
                autoboto.TypeInfo(str),
            ),
            (
                "ip_address",
                "ipAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "mac_address",
                "macAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "associated_on",
                "associatedOn",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # Unique Identifier for Connector
    connector_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Connector version string
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Status of on-premise Connector
    status: "ConnectorStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # List of Connector Capabilities
    capability_list: typing.List["ConnectorCapability"] = dataclasses.field(
        default_factory=list,
    )

    # VM Manager Name
    vm_manager_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # VM Management Product
    vm_manager_type: "VmManagerType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique Identifier for VM Manager
    vm_manager_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Internet Protocol (IP) Address
    ip_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Hardware (MAC) address
    mac_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Timestamp of an operation
    associated_on: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ConnectorCapability(Enum):
    """
    Capabilities for a Connector
    """
    VSPHERE = "VSPHERE"


class ConnectorStatus(Enum):
    """
    Status of on-premise Connector
    """
    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"


@dataclasses.dataclass
class CreateReplicationJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_id",
                "serverId",
                autoboto.TypeInfo(str),
            ),
            (
                "seed_replication_time",
                "seedReplicationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "frequency",
                "frequency",
                autoboto.TypeInfo(int),
            ),
            (
                "license_type",
                "licenseType",
                autoboto.TypeInfo(LicenseType),
            ),
            (
                "role_name",
                "roleName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # Unique Identifier for a server
    server_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Timestamp of an operation
    seed_replication_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Interval between Replication Runs. This value is specified in hours, and
    # represents the time between consecutive Replication Runs.
    frequency: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The license type to be used for the Amazon Machine Image (AMI) created
    # after a successful ReplicationRun.
    license_type: "LicenseType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Name of service role in customer's account to be used by SMS service.
    role_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description for a Replication Job/Run.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateReplicationJobResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_job_id",
                "replicationJobId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The unique identifier for a Replication Job.
    replication_job_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteReplicationJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_job_id",
                "replicationJobId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier for a Replication Job.
    replication_job_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteReplicationJobResponse(autoboto.OutputShapeBase):
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
class DeleteServerCatalogRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteServerCatalogResponse(autoboto.OutputShapeBase):
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
class DisassociateConnectorRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connector_id",
                "connectorId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Unique Identifier for Connector
    connector_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateConnectorResponse(autoboto.OutputShapeBase):
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
class GetConnectorsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # Pagination token to pass as input to API call
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to return in one API call. If left empty,
    # this will default to 50.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetConnectorsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "connector_list",
                "connectorList",
                autoboto.TypeInfo(typing.List[Connector]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # List of connectors
    connector_list: typing.List["Connector"] = dataclasses.field(
        default_factory=list,
    )

    # Pagination token to pass as input to API call
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetReplicationJobsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_job_id",
                "replicationJobId",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique identifier for a Replication Job.
    replication_job_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Pagination token to pass as input to API call
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to return in one API call. If left empty,
    # this will default to 50.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetReplicationJobsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_job_list",
                "replicationJobList",
                autoboto.TypeInfo(typing.List[ReplicationJob]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # List of Replication Jobs
    replication_job_list: typing.List["ReplicationJob"] = dataclasses.field(
        default_factory=list,
    )

    # Pagination token to pass as input to API call
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetReplicationRunsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_job_id",
                "replicationJobId",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique identifier for a Replication Job.
    replication_job_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Pagination token to pass as input to API call
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to return in one API call. If left empty,
    # this will default to 50.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetReplicationRunsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_job",
                "replicationJob",
                autoboto.TypeInfo(ReplicationJob),
            ),
            (
                "replication_run_list",
                "replicationRunList",
                autoboto.TypeInfo(typing.List[ReplicationRun]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Object representing a Replication Job
    replication_job: "ReplicationJob" = dataclasses.field(
        default_factory=dict,
    )

    # List of Replication Runs
    replication_run_list: typing.List["ReplicationRun"] = dataclasses.field(
        default_factory=list,
    )

    # Pagination token to pass as input to API call
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetServersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # Pagination token to pass as input to API call
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to return in one API call. If left empty,
    # this will default to 50.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetServersResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "last_modified_on",
                "lastModifiedOn",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "server_catalog_status",
                "serverCatalogStatus",
                autoboto.TypeInfo(ServerCatalogStatus),
            ),
            (
                "server_list",
                "serverList",
                autoboto.TypeInfo(typing.List[Server]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Timestamp of an operation
    last_modified_on: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Status of Server catalog
    server_catalog_status: "ServerCatalogStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # List of servers from catalog
    server_list: typing.List["Server"] = dataclasses.field(
        default_factory=list,
    )

    # Pagination token to pass as input to API call
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImportServerCatalogRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ImportServerCatalogResponse(autoboto.OutputShapeBase):
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
class InternalError(autoboto.ShapeBase):
    """
    An internal error has occured.
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

    # Error Message string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterException(autoboto.ShapeBase):
    """
    A parameter specified in the request is not valid, is unsupported, or cannot be
    used.
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

    # Error Message string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class LicenseType(Enum):
    """
    The license type to be used for the Amazon Machine Image (AMI) created after a
    successful ReplicationRun.
    """
    AWS = "AWS"
    BYOL = "BYOL"


@dataclasses.dataclass
class MissingRequiredParameterException(autoboto.ShapeBase):
    """
    The request is missing a required parameter. Ensure that you have supplied all
    the required parameters for the request.
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

    # Error Message string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoConnectorsAvailableException(autoboto.ShapeBase):
    """
    No connectors are available to handle this request. Please associate
    connector(s) and verify any existing connectors are healthy and can respond to
    requests.
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

    # Error Message string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OperationNotPermittedException(autoboto.ShapeBase):
    """
    The specified operation is not allowed. This error can occur for a number of
    reasons; for example, you might be trying to start a Replication Run before seed
    Replication Run.
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

    # Error Message string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReplicationJob(autoboto.ShapeBase):
    """
    Object representing a Replication Job
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_job_id",
                "replicationJobId",
                autoboto.TypeInfo(str),
            ),
            (
                "server_id",
                "serverId",
                autoboto.TypeInfo(str),
            ),
            (
                "server_type",
                "serverType",
                autoboto.TypeInfo(ServerType),
            ),
            (
                "vm_server",
                "vmServer",
                autoboto.TypeInfo(VmServer),
            ),
            (
                "seed_replication_time",
                "seedReplicationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "frequency",
                "frequency",
                autoboto.TypeInfo(int),
            ),
            (
                "next_replication_run_start_time",
                "nextReplicationRunStartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "license_type",
                "licenseType",
                autoboto.TypeInfo(LicenseType),
            ),
            (
                "role_name",
                "roleName",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_ami_id",
                "latestAmiId",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "state",
                autoboto.TypeInfo(ReplicationJobState),
            ),
            (
                "status_message",
                "statusMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "replication_run_list",
                "replicationRunList",
                autoboto.TypeInfo(typing.List[ReplicationRun]),
            ),
        ]

    # The unique identifier for a Replication Job.
    replication_job_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique Identifier for a server
    server_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Type of server.
    server_type: "ServerType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Object representing a VM server
    vm_server: "VmServer" = dataclasses.field(default_factory=dict, )

    # Timestamp of an operation
    seed_replication_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Interval between Replication Runs. This value is specified in hours, and
    # represents the time between consecutive Replication Runs.
    frequency: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Timestamp of an operation
    next_replication_run_start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The license type to be used for the Amazon Machine Image (AMI) created
    # after a successful ReplicationRun.
    license_type: "LicenseType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Name of service role in customer's account to be used by SMS service.
    role_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The AMI id for the image resulting from a Replication Run.
    latest_ami_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Current state of Replication Job
    state: "ReplicationJobState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # String describing current status of Replication Job
    status_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description for a Replication Job/Run.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # List of Replication Runs
    replication_run_list: typing.List["ReplicationRun"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ReplicationJobAlreadyExistsException(autoboto.ShapeBase):
    """
    An active Replication Job already exists for the specified server.
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

    # Error Message string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReplicationJobNotFoundException(autoboto.ShapeBase):
    """
    The specified Replication Job cannot be found.
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

    # Error Message string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ReplicationJobState(Enum):
    """
    Current state of Replication Job
    """
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"
    DELETING = "DELETING"
    DELETED = "DELETED"


@dataclasses.dataclass
class ReplicationRun(autoboto.ShapeBase):
    """
    Object representing a Replication Run
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_run_id",
                "replicationRunId",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "state",
                autoboto.TypeInfo(ReplicationRunState),
            ),
            (
                "type",
                "type",
                autoboto.TypeInfo(ReplicationRunType),
            ),
            (
                "status_message",
                "statusMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "ami_id",
                "amiId",
                autoboto.TypeInfo(str),
            ),
            (
                "scheduled_start_time",
                "scheduledStartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "completed_time",
                "completedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier for a Replication Run.
    replication_run_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Current state of Replication Run
    state: "ReplicationRunState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Type of Replication Run
    type: "ReplicationRunType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # String describing current status of Replication Run
    status_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AMI id for the image resulting from a Replication Run.
    ami_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Timestamp of an operation
    scheduled_start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Timestamp of an operation
    completed_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description for a Replication Job/Run.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReplicationRunLimitExceededException(autoboto.ShapeBase):
    """
    This user has exceeded the maximum allowed Replication Run limit.
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

    # Error Message string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ReplicationRunState(Enum):
    """
    Current state of Replication Run
    """
    PENDING = "PENDING"
    MISSED = "MISSED"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    DELETING = "DELETING"
    DELETED = "DELETED"


class ReplicationRunType(Enum):
    """
    Type of Replication Run
    """
    ON_DEMAND = "ON_DEMAND"
    AUTOMATIC = "AUTOMATIC"


@dataclasses.dataclass
class Server(autoboto.ShapeBase):
    """
    Object representing a server
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_id",
                "serverId",
                autoboto.TypeInfo(str),
            ),
            (
                "server_type",
                "serverType",
                autoboto.TypeInfo(ServerType),
            ),
            (
                "vm_server",
                "vmServer",
                autoboto.TypeInfo(VmServer),
            ),
            (
                "replication_job_id",
                "replicationJobId",
                autoboto.TypeInfo(str),
            ),
            (
                "replication_job_terminated",
                "replicationJobTerminated",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Unique Identifier for a server
    server_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Type of server.
    server_type: "ServerType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Object representing a VM server
    vm_server: "VmServer" = dataclasses.field(default_factory=dict, )

    # The unique identifier for a Replication Job.
    replication_job_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An indicator of the Replication Job being deleted or failed.
    replication_job_terminated: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServerCannotBeReplicatedException(autoboto.ShapeBase):
    """
    The provided server cannot be replicated.
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

    # Error Message string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ServerCatalogStatus(Enum):
    """
    Status of Server catalog
    """
    NOT_IMPORTED = "NOT_IMPORTED"
    IMPORTING = "IMPORTING"
    AVAILABLE = "AVAILABLE"
    DELETED = "DELETED"
    EXPIRED = "EXPIRED"


class ServerType(Enum):
    """
    Type of server.
    """
    VIRTUAL_MACHINE = "VIRTUAL_MACHINE"


@dataclasses.dataclass
class StartOnDemandReplicationRunRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_job_id",
                "replicationJobId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier for a Replication Job.
    replication_job_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description for a Replication Job/Run.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartOnDemandReplicationRunResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_run_id",
                "replicationRunId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The unique identifier for a Replication Run.
    replication_run_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UnauthorizedOperationException(autoboto.ShapeBase):
    """
    This user does not have permissions to perform this operation.
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

    # Error Message string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateReplicationJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_job_id",
                "replicationJobId",
                autoboto.TypeInfo(str),
            ),
            (
                "frequency",
                "frequency",
                autoboto.TypeInfo(int),
            ),
            (
                "next_replication_run_start_time",
                "nextReplicationRunStartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "license_type",
                "licenseType",
                autoboto.TypeInfo(LicenseType),
            ),
            (
                "role_name",
                "roleName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier for a Replication Job.
    replication_job_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Interval between Replication Runs. This value is specified in hours, and
    # represents the time between consecutive Replication Runs.
    frequency: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Timestamp of an operation
    next_replication_run_start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The license type to be used for the Amazon Machine Image (AMI) created
    # after a successful ReplicationRun.
    license_type: "LicenseType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Name of service role in customer's account to be used by SMS service.
    role_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description for a Replication Job/Run.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateReplicationJobResponse(autoboto.OutputShapeBase):
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


class VmManagerType(Enum):
    """
    VM Management Product
    """
    VSPHERE = "VSPHERE"


@dataclasses.dataclass
class VmServer(autoboto.ShapeBase):
    """
    Object representing a VM server
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vm_server_address",
                "vmServerAddress",
                autoboto.TypeInfo(VmServerAddress),
            ),
            (
                "vm_name",
                "vmName",
                autoboto.TypeInfo(str),
            ),
            (
                "vm_manager_name",
                "vmManagerName",
                autoboto.TypeInfo(str),
            ),
            (
                "vm_manager_type",
                "vmManagerType",
                autoboto.TypeInfo(VmManagerType),
            ),
            (
                "vm_path",
                "vmPath",
                autoboto.TypeInfo(str),
            ),
        ]

    # Object representing a server's location
    vm_server_address: "VmServerAddress" = dataclasses.field(
        default_factory=dict,
    )

    # Name of Virtual Machine
    vm_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # VM Manager Name
    vm_manager_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # VM Management Product
    vm_manager_type: "VmManagerType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Path to VM
    vm_path: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VmServerAddress(autoboto.ShapeBase):
    """
    Object representing a server's location
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vm_manager_id",
                "vmManagerId",
                autoboto.TypeInfo(str),
            ),
            (
                "vm_id",
                "vmId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Unique Identifier for VM Manager
    vm_manager_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Unique Identifier for a VM
    vm_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
