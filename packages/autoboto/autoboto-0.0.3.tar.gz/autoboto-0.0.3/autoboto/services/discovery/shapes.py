import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AgentConfigurationStatus(autoboto.ShapeBase):
    """
    Information about agents or connectors that were instructed to start collecting
    data. Information includes the agent/connector ID, a description of the
    operation, and whether the agent/connector configuration was updated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_id",
                "agentId",
                autoboto.TypeInfo(str),
            ),
            (
                "operation_succeeded",
                "operationSucceeded",
                autoboto.TypeInfo(bool),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The agent/connector ID.
    agent_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information about the status of the `StartDataCollection` and
    # `StopDataCollection` operations. The system has recorded the data
    # collection operation. The agent/connector receives this command the next
    # time it polls for a new command.
    operation_succeeded: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the operation performed.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AgentInfo(autoboto.ShapeBase):
    """
    Information about agents or connectors associated with the user’s AWS account.
    Information includes agent or connector IDs, IP addresses, media access control
    (MAC) addresses, agent or connector health, hostname where the agent or
    connector resides, and agent version for each agent.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_id",
                "agentId",
                autoboto.TypeInfo(str),
            ),
            (
                "host_name",
                "hostName",
                autoboto.TypeInfo(str),
            ),
            (
                "agent_network_info_list",
                "agentNetworkInfoList",
                autoboto.TypeInfo(typing.List[AgentNetworkInfo]),
            ),
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
                "health",
                "health",
                autoboto.TypeInfo(AgentStatus),
            ),
            (
                "last_health_ping_time",
                "lastHealthPingTime",
                autoboto.TypeInfo(str),
            ),
            (
                "collection_status",
                "collectionStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "agent_type",
                "agentType",
                autoboto.TypeInfo(str),
            ),
            (
                "registered_time",
                "registeredTime",
                autoboto.TypeInfo(str),
            ),
        ]

    # The agent or connector ID.
    agent_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the host where the agent or connector resides. The host can be
    # a server or virtual machine.
    host_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Network details about the host where the agent or connector resides.
    agent_network_info_list: typing.List["AgentNetworkInfo"
                                        ] = dataclasses.field(
                                            default_factory=list,
                                        )

    # The ID of the connector.
    connector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The agent or connector version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The health of the agent or connector.
    health: "AgentStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Time since agent or connector health was reported.
    last_health_ping_time: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Status of the collection process for an agent or connector.
    collection_status: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Type of agent.
    agent_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Agent's first registration timestamp in UTC.
    registered_time: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AgentNetworkInfo(autoboto.ShapeBase):
    """
    Network details about the host where the agent/connector resides.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
        ]

    # The IP address for the host where the agent/connector resides.
    ip_address: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The MAC address for the host where the agent/connector resides.
    mac_address: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class AgentStatus(Enum):
    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"
    RUNNING = "RUNNING"
    UNKNOWN = "UNKNOWN"
    BLACKLISTED = "BLACKLISTED"
    SHUTDOWN = "SHUTDOWN"


@dataclasses.dataclass
class AssociateConfigurationItemsToApplicationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_configuration_id",
                "applicationConfigurationId",
                autoboto.TypeInfo(str),
            ),
            (
                "configuration_ids",
                "configurationIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The configuration ID of an application with which items are to be
    # associated.
    application_configuration_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of each configuration item to be associated with an application.
    configuration_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AssociateConfigurationItemsToApplicationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AuthorizationErrorException(autoboto.ShapeBase):
    """
    The AWS user account does not have permission to perform the action. Check the
    IAM policy associated with this account.
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


class ConfigurationItemType(Enum):
    SERVER = "SERVER"
    PROCESS = "PROCESS"
    CONNECTION = "CONNECTION"
    APPLICATION = "APPLICATION"


@dataclasses.dataclass
class ConfigurationTag(autoboto.ShapeBase):
    """
    Tags for a configuration item. Tags are metadata that help you categorize IT
    assets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_type",
                "configurationType",
                autoboto.TypeInfo(ConfigurationItemType),
            ),
            (
                "configuration_id",
                "configurationId",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "key",
                autoboto.TypeInfo(str),
            ),
            (
                "value",
                "value",
                autoboto.TypeInfo(str),
            ),
            (
                "time_of_creation",
                "timeOfCreation",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # A type of IT asset to tag.
    configuration_type: "ConfigurationItemType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The configuration ID for the item to tag. You can specify a list of keys
    # and values.
    configuration_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A type of tag on which to filter. For example, _serverType_.
    key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A value on which to filter. For example _key = serverType_ and _value = web
    # server_.
    value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time the configuration tag was created in Coordinated Universal Time
    # (UTC).
    time_of_creation: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ConflictErrorException(autoboto.ShapeBase):
    """

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
class ContinuousExportDescription(autoboto.ShapeBase):
    """
    A list of continuous export descriptions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_id",
                "exportId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(ContinuousExportStatus),
            ),
            (
                "status_detail",
                "statusDetail",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_bucket",
                "s3Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "start_time",
                "startTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "stop_time",
                "stopTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "data_source",
                "dataSource",
                autoboto.TypeInfo(DataSource),
            ),
            (
                "schema_storage_config",
                "schemaStorageConfig",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The unique ID assigned to this export.
    export_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Describes the status of the export. Can be one of the following values:

    #   * START_IN_PROGRESS - setting up resources to start continuous export.

    #   * START_FAILED - an error occurred setting up continuous export. To recover, call start-continuous-export again.

    #   * ACTIVE - data is being exported to the customer bucket.

    #   * ERROR - an error occurred during export. To fix the issue, call stop-continuous-export and start-continuous-export.

    #   * STOP_IN_PROGRESS - stopping the export.

    #   * STOP_FAILED - an error occurred stopping the export. To recover, call stop-continuous-export again.

    #   * INACTIVE - the continuous export has been stopped. Data is no longer being exported to the customer bucket.
    status: "ContinuousExportStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Contains information about any errors that may have occurred.
    status_detail: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the s3 bucket where the export data parquet files are stored.
    s3_bucket: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The timestamp representing when the continuous export was started.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The timestamp that represents when this continuous export was stopped.
    stop_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of data collector used to gather this data (currently only offered
    # for AGENT).
    data_source: "DataSource" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An object which describes how the data is stored.

    #   * `databaseName` \- the name of the Glue database used to store the schema.
    schema_storage_config: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class ContinuousExportStatus(Enum):
    START_IN_PROGRESS = "START_IN_PROGRESS"
    START_FAILED = "START_FAILED"
    ACTIVE = "ACTIVE"
    ERROR = "ERROR"
    STOP_IN_PROGRESS = "STOP_IN_PROGRESS"
    STOP_FAILED = "STOP_FAILED"
    INACTIVE = "INACTIVE"


@dataclasses.dataclass
class CreateApplicationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the application to be created.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Description of the application to be created.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateApplicationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_id",
                "configurationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Configuration ID of an application to be created.
    configuration_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateTagsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_ids",
                "configurationIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # A list of configuration items that you want to tag.
    configuration_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Tags that you want to associate with one or more configuration items.
    # Specify the tags that you want to create in a _key_ - _value_ format. For
    # example:

    # `{"key": "serverType", "value": "webServer"}`
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateTagsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CustomerAgentInfo(autoboto.ShapeBase):
    """
    Inventory data for installed discovery agents.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "active_agents",
                "activeAgents",
                autoboto.TypeInfo(int),
            ),
            (
                "healthy_agents",
                "healthyAgents",
                autoboto.TypeInfo(int),
            ),
            (
                "black_listed_agents",
                "blackListedAgents",
                autoboto.TypeInfo(int),
            ),
            (
                "shutdown_agents",
                "shutdownAgents",
                autoboto.TypeInfo(int),
            ),
            (
                "unhealthy_agents",
                "unhealthyAgents",
                autoboto.TypeInfo(int),
            ),
            (
                "total_agents",
                "totalAgents",
                autoboto.TypeInfo(int),
            ),
            (
                "unknown_agents",
                "unknownAgents",
                autoboto.TypeInfo(int),
            ),
        ]

    # Number of active discovery agents.
    active_agents: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Number of healthy discovery agents
    healthy_agents: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Number of blacklisted discovery agents.
    black_listed_agents: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Number of discovery agents with status SHUTDOWN.
    shutdown_agents: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Number of unhealthy discovery agents.
    unhealthy_agents: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Total number of discovery agents.
    total_agents: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Number of unknown discovery agents.
    unknown_agents: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CustomerConnectorInfo(autoboto.ShapeBase):
    """
    Inventory data for installed discovery connectors.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "active_connectors",
                "activeConnectors",
                autoboto.TypeInfo(int),
            ),
            (
                "healthy_connectors",
                "healthyConnectors",
                autoboto.TypeInfo(int),
            ),
            (
                "black_listed_connectors",
                "blackListedConnectors",
                autoboto.TypeInfo(int),
            ),
            (
                "shutdown_connectors",
                "shutdownConnectors",
                autoboto.TypeInfo(int),
            ),
            (
                "unhealthy_connectors",
                "unhealthyConnectors",
                autoboto.TypeInfo(int),
            ),
            (
                "total_connectors",
                "totalConnectors",
                autoboto.TypeInfo(int),
            ),
            (
                "unknown_connectors",
                "unknownConnectors",
                autoboto.TypeInfo(int),
            ),
        ]

    # Number of active discovery connectors.
    active_connectors: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Number of healthy discovery connectors.
    healthy_connectors: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Number of blacklisted discovery connectors.
    black_listed_connectors: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Number of discovery connectors with status SHUTDOWN,
    shutdown_connectors: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Number of unhealthy discovery connectors.
    unhealthy_connectors: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Total number of discovery connectors.
    total_connectors: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Number of unknown discovery connectors.
    unknown_connectors: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class DataSource(Enum):
    AGENT = "AGENT"


@dataclasses.dataclass
class DeleteApplicationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_ids",
                "configurationIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # Configuration ID of an application to be deleted.
    configuration_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DeleteApplicationsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteTagsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_ids",
                "configurationIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # A list of configuration items with tags that you want to delete.
    configuration_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Tags that you want to delete from one or more configuration items. Specify
    # the tags that you want to delete in a _key_ - _value_ format. For example:

    # `{"key": "serverType", "value": "webServer"}`
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DeleteTagsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeAgentsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_ids",
                "agentIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "filters",
                "filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The agent or the Connector IDs for which you want information. If you
    # specify no IDs, the system returns information about all agents/Connectors
    # associated with your AWS user account.
    agent_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # You can filter the request using various logical operators and a _key_ -
    # _value_ format. For example:

    # `{"key": "collectionStatus", "value": "STARTED"}`
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The total number of agents/Connectors to return in a single page of output.
    # The maximum value is 100.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Token to retrieve the next set of results. For example, if you previously
    # specified 100 IDs for `DescribeAgentsRequest$agentIds` but set
    # `DescribeAgentsRequest$maxResults` to 10, you received a set of 10 results
    # along with a token. Use that token in this query to get the next set of 10.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeAgentsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agents_info",
                "agentsInfo",
                autoboto.TypeInfo(typing.List[AgentInfo]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Lists agents or the Connector by ID or lists all agents/Connectors
    # associated with your user account if you did not specify an agent/Connector
    # ID. The output includes agent/Connector IDs, IP addresses, media access
    # control (MAC) addresses, agent/Connector health, host name where the
    # agent/Connector resides, and the version number of each agent/Connector.
    agents_info: typing.List["AgentInfo"] = dataclasses.field(
        default_factory=list,
    )

    # Token to retrieve the next set of results. For example, if you specified
    # 100 IDs for `DescribeAgentsRequest$agentIds` but set
    # `DescribeAgentsRequest$maxResults` to 10, you received a set of 10 results
    # along with this token. Use this token in the next query to retrieve the
    # next set of 10.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeConfigurationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_ids",
                "configurationIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # One or more configuration IDs.
    configuration_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeConfigurationsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configurations",
                "configurations",
                autoboto.TypeInfo(typing.List[typing.Dict[str, str]]),
            ),
        ]

    # A key in the response map. The value is an array of data.
    configurations: typing.List[typing.Dict[str, str]] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeContinuousExportsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_ids",
                "exportIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique IDs assigned to the exports.
    export_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # A number between 1 and 100 specifying the maximum number of continuous
    # export descriptions returned.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token from the previous call to `DescribeExportTasks`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeContinuousExportsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "descriptions",
                "descriptions",
                autoboto.TypeInfo(typing.List[ContinuousExportDescription]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of continuous export descriptions.
    descriptions: typing.List["ContinuousExportDescription"
                             ] = dataclasses.field(
                                 default_factory=list,
                             )

    # The token from the previous call to `DescribeExportTasks`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeExportConfigurationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_ids",
                "exportIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of continuous export ids to search for.
    export_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # A number between 1 and 100 specifying the maximum number of continuous
    # export descriptions returned.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token from the previous call to describe-export-tasks.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeExportConfigurationsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "exports_info",
                "exportsInfo",
                autoboto.TypeInfo(typing.List[ExportInfo]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    exports_info: typing.List["ExportInfo"] = dataclasses.field(
        default_factory=list,
    )

    # The token from the previous call to describe-export-tasks.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeExportTasksRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_ids",
                "exportIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "filters",
                "filters",
                autoboto.TypeInfo(typing.List[ExportFilter]),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # One or more unique identifiers used to query the status of an export
    # request.
    export_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # One or more filters.

    #   * `AgentId` \- ID of the agent whose collected data will be exported
    filters: typing.List["ExportFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of volume results returned by `DescribeExportTasks` in
    # paginated output. When this parameter is used, `DescribeExportTasks` only
    # returns `maxResults` results in a single page along with a `nextToken`
    # response element.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The `nextToken` value returned from a previous paginated
    # `DescribeExportTasks` request where `maxResults` was used and the results
    # exceeded the value of that parameter. Pagination continues from the end of
    # the previous results that returned the `nextToken` value. This value is
    # null when there are no more results to return.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeExportTasksResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "exports_info",
                "exportsInfo",
                autoboto.TypeInfo(typing.List[ExportInfo]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Contains one or more sets of export request details. When the status of a
    # request is `SUCCEEDED`, the response includes a URL for an Amazon S3 bucket
    # where you can view the data in a CSV file.
    exports_info: typing.List["ExportInfo"] = dataclasses.field(
        default_factory=list,
    )

    # The `nextToken` value to include in a future `DescribeExportTasks` request.
    # When the results of a `DescribeExportTasks` request exceed `maxResults`,
    # this value can be used to retrieve the next page of results. This value is
    # null when there are no more results to return.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeTagsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "filters",
                autoboto.TypeInfo(typing.List[TagFilter]),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # You can filter the list using a _key_ - _value_ format. You can separate
    # these items by using logical operators. Allowed filters include `tagKey`,
    # `tagValue`, and `configurationId`.
    filters: typing.List["TagFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The total number of items to return in a single page of output. The maximum
    # value is 100.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeTagsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[ConfigurationTag]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Depending on the input, this is a list of configuration items tagged with a
    # specific tag, or a list of tags for a specific configuration item.
    tags: typing.List["ConfigurationTag"] = dataclasses.field(
        default_factory=list,
    )

    # The call returns a token. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DisassociateConfigurationItemsFromApplicationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_configuration_id",
                "applicationConfigurationId",
                autoboto.TypeInfo(str),
            ),
            (
                "configuration_ids",
                "configurationIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # Configuration ID of an application from which each item is disassociated.
    application_configuration_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Configuration ID of each item to be disassociated from an application.
    configuration_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DisassociateConfigurationItemsFromApplicationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ExportConfigurationsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_id",
                "exportId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier that you can use to query the export status.
    export_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class ExportDataFormat(Enum):
    CSV = "CSV"
    GRAPHML = "GRAPHML"


@dataclasses.dataclass
class ExportFilter(autoboto.ShapeBase):
    """
    Used to select which agent's data is to be exported. A single agent ID may be
    selected for export using the
    [StartExportTask](http://docs.aws.amazon.com/application-
    discovery/latest/APIReference/API_StartExportTask.html) action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "values",
                "values",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "condition",
                "condition",
                autoboto.TypeInfo(str),
            ),
        ]

    # A single `ExportFilter` name. Supported filters: `agentId`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A single `agentId` for a Discovery Agent. An `agentId` can be found using
    # the [DescribeAgents](http://docs.aws.amazon.com/application-
    # discovery/latest/APIReference/API_DescribeExportTasks.html) action.
    # Typically an ADS `agentId` is in the form `o-0123456789abcdef0`.
    values: typing.List[str] = dataclasses.field(default_factory=list, )

    # Supported condition: `EQUALS`
    condition: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ExportInfo(autoboto.ShapeBase):
    """
    Information regarding the export status of discovered data. The value is an
    array of objects.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_id",
                "exportId",
                autoboto.TypeInfo(str),
            ),
            (
                "export_status",
                "exportStatus",
                autoboto.TypeInfo(ExportStatus),
            ),
            (
                "status_message",
                "statusMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "export_request_time",
                "exportRequestTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "configurations_download_url",
                "configurationsDownloadUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "is_truncated",
                "isTruncated",
                autoboto.TypeInfo(bool),
            ),
            (
                "requested_start_time",
                "requestedStartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "requested_end_time",
                "requestedEndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # A unique identifier used to query an export.
    export_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the data export job.
    export_status: "ExportStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A status message provided for API callers.
    status_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time that the data export was initiated.
    export_request_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A URL for an Amazon S3 bucket where you can review the exported data. The
    # URL is displayed only if the export succeeded.
    configurations_download_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If true, the export of agent information exceeded the size limit for a
    # single export and the exported data is incomplete for the requested time
    # range. To address this, select a smaller time range for the export by using
    # `startDate` and `endDate`.
    is_truncated: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value of `startTime` parameter in the `StartExportTask` request. If no
    # `startTime` was requested, this result does not appear in `ExportInfo`.
    requested_start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The `endTime` used in the `StartExportTask` request. If no `endTime` was
    # requested, this result does not appear in `ExportInfo`.
    requested_end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class ExportStatus(Enum):
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    IN_PROGRESS = "IN_PROGRESS"


@dataclasses.dataclass
class Filter(autoboto.ShapeBase):
    """
    A filter that can use conditional operators.

    For more information about filters, see [Querying Discovered Configuration
    Items](http://docs.aws.amazon.com/application-
    discovery/latest/APIReference/discovery-api-queries.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "values",
                "values",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "condition",
                "condition",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the filter.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A string value on which to filter. For example, if you choose the
    # `destinationServer.osVersion` filter name, you could specify `Ubuntu` for
    # the value.
    values: typing.List[str] = dataclasses.field(default_factory=list, )

    # A conditional operator. The following operators are valid: EQUALS,
    # NOT_EQUALS, CONTAINS, NOT_CONTAINS. If you specify multiple filters, the
    # system utilizes all filters as though concatenated by _AND_. If you specify
    # multiple values for a particular filter, the system differentiates the
    # values using _OR_. Calling either _DescribeConfigurations_ or
    # _ListConfigurations_ returns attributes of matching configuration items.
    condition: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDiscoverySummaryRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetDiscoverySummaryResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "servers",
                "servers",
                autoboto.TypeInfo(int),
            ),
            (
                "applications",
                "applications",
                autoboto.TypeInfo(int),
            ),
            (
                "servers_mapped_to_applications",
                "serversMappedToApplications",
                autoboto.TypeInfo(int),
            ),
            (
                "servers_mappedto_tags",
                "serversMappedtoTags",
                autoboto.TypeInfo(int),
            ),
            (
                "agent_summary",
                "agentSummary",
                autoboto.TypeInfo(CustomerAgentInfo),
            ),
            (
                "connector_summary",
                "connectorSummary",
                autoboto.TypeInfo(CustomerConnectorInfo),
            ),
        ]

    # The number of servers discovered.
    servers: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of applications discovered.
    applications: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of servers mapped to applications.
    servers_mapped_to_applications: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of servers mapped to tags.
    servers_mappedto_tags: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Details about discovered agents, including agent status and health.
    agent_summary: "CustomerAgentInfo" = dataclasses.field(
        default_factory=dict,
    )

    # Details about discovered connectors, including connector status and health.
    connector_summary: "CustomerConnectorInfo" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class InvalidParameterException(autoboto.ShapeBase):
    """
    One or more parameters are not valid. Verify the parameters and try again.
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
class InvalidParameterValueException(autoboto.ShapeBase):
    """
    The value of one or more parameters are either invalid or out of range. Verify
    the parameter values and try again.
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
class ListConfigurationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_type",
                "configurationType",
                autoboto.TypeInfo(ConfigurationItemType),
            ),
            (
                "filters",
                "filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "order_by",
                "orderBy",
                autoboto.TypeInfo(typing.List[OrderByElement]),
            ),
        ]

    # A valid configuration identified by Application Discovery Service.
    configuration_type: "ConfigurationItemType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # You can filter the request using various logical operators and a _key_ -
    # _value_ format. For example:

    # `{"key": "serverType", "value": "webServer"}`

    # For a complete list of filter options and guidance about using them with
    # this action, see [Querying Discovered Configuration
    # Items](http://docs.aws.amazon.com/application-
    # discovery/latest/APIReference/discovery-api-
    # queries.html#ListConfigurations).
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The total number of items to return. The maximum value is 100.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Token to retrieve the next set of results. For example, if a previous call
    # to ListConfigurations returned 100 items, but you set
    # `ListConfigurationsRequest$maxResults` to 10, you received a set of 10
    # results along with a token. Use that token in this query to get the next
    # set of 10.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Certain filter criteria return output that can be sorted in ascending or
    # descending order. For a list of output characteristics for each filter, see
    # [Using the ListConfigurations
    # Action](http://docs.aws.amazon.com/application-
    # discovery/latest/APIReference/discovery-api-
    # queries.html#ListConfigurations).
    order_by: typing.List["OrderByElement"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListConfigurationsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configurations",
                "configurations",
                autoboto.TypeInfo(typing.List[typing.Dict[str, str]]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Returns configuration details, including the configuration ID, attribute
    # names, and attribute values.
    configurations: typing.List[typing.Dict[str, str]] = dataclasses.field(
        default_factory=list,
    )

    # Token to retrieve the next set of results. For example, if your call to
    # ListConfigurations returned 100 items, but you set
    # `ListConfigurationsRequest$maxResults` to 10, you received a set of 10
    # results along with this token. Use this token in the next query to retrieve
    # the next set of 10.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListServerNeighborsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_id",
                "configurationId",
                autoboto.TypeInfo(str),
            ),
            (
                "port_information_needed",
                "portInformationNeeded",
                autoboto.TypeInfo(bool),
            ),
            (
                "neighbor_configuration_ids",
                "neighborConfigurationIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Configuration ID of the server for which neighbors are being listed.
    configuration_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Flag to indicate if port and protocol information is needed as part of the
    # response.
    port_information_needed: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # List of configuration IDs to test for one-hop-away.
    neighbor_configuration_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Maximum number of results to return in a single page of output.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Token to retrieve the next set of results. For example, if you previously
    # specified 100 IDs for `ListServerNeighborsRequest$neighborConfigurationIds`
    # but set `ListServerNeighborsRequest$maxResults` to 10, you received a set
    # of 10 results along with a token. Use that token in this query to get the
    # next set of 10.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListServerNeighborsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "neighbors",
                "neighbors",
                autoboto.TypeInfo(typing.List[NeighborConnectionDetail]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "known_dependency_count",
                "knownDependencyCount",
                autoboto.TypeInfo(int),
            ),
        ]

    # List of distinct servers that are one hop away from the given server.
    neighbors: typing.List["NeighborConnectionDetail"] = dataclasses.field(
        default_factory=list,
    )

    # Token to retrieve the next set of results. For example, if you specified
    # 100 IDs for `ListServerNeighborsRequest$neighborConfigurationIds` but set
    # `ListServerNeighborsRequest$maxResults` to 10, you received a set of 10
    # results along with this token. Use this token in the next query to retrieve
    # the next set of 10.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Count of distinct servers that are one hop away from the given server.
    known_dependency_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class NeighborConnectionDetail(autoboto.ShapeBase):
    """
    Details about neighboring servers.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_server_id",
                "sourceServerId",
                autoboto.TypeInfo(str),
            ),
            (
                "destination_server_id",
                "destinationServerId",
                autoboto.TypeInfo(str),
            ),
            (
                "connections_count",
                "connectionsCount",
                autoboto.TypeInfo(int),
            ),
            (
                "destination_port",
                "destinationPort",
                autoboto.TypeInfo(int),
            ),
            (
                "transport_protocol",
                "transportProtocol",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the server that opened the network connection.
    source_server_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the server that accepted the network connection.
    destination_server_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of open network connections with the neighboring server.
    connections_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The destination network port for the connection.
    destination_port: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The network protocol used for the connection.
    transport_protocol: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class OperationNotPermittedException(autoboto.ShapeBase):
    """
    This operation is not permitted.
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
class OrderByElement(autoboto.ShapeBase):
    """
    A field and direction for ordered output.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_name",
                "fieldName",
                autoboto.TypeInfo(str),
            ),
            (
                "sort_order",
                "sortOrder",
                autoboto.TypeInfo(orderString),
            ),
        ]

    # The field on which to order.
    field_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Ordering direction.
    sort_order: "orderString" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ResourceInUseException(autoboto.ShapeBase):
    """

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
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    The specified configuration ID was not located. Verify the configuration ID and
    try again.
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
class ServerInternalErrorException(autoboto.ShapeBase):
    """
    The server experienced an internal error. Try again.
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
class StartContinuousExportRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StartContinuousExportResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_id",
                "exportId",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_bucket",
                "s3Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "start_time",
                "startTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "data_source",
                "dataSource",
                autoboto.TypeInfo(DataSource),
            ),
            (
                "schema_storage_config",
                "schemaStorageConfig",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The unique ID assigned to this export.
    export_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the s3 bucket where the export data parquet files are stored.
    s3_bucket: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The timestamp representing when the continuous export was started.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of data collector used to gather this data (currently only offered
    # for AGENT).
    data_source: "DataSource" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A dictionary which describes how the data is stored.

    #   * `databaseName` \- the name of the Glue database used to store the schema.
    schema_storage_config: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class StartDataCollectionByAgentIdsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_ids",
                "agentIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The IDs of the agents or connectors from which to start collecting data. If
    # you send a request to an agent/connector ID that you do not have permission
    # to contact, according to your AWS account, the service does not throw an
    # exception. Instead, it returns the error in the _Description_ field. If you
    # send a request to multiple agents/connectors and you do not have permission
    # to contact some of those agents/connectors, the system does not throw an
    # exception. Instead, the system shows `Failed` in the _Description_ field.
    agent_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class StartDataCollectionByAgentIdsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agents_configuration_status",
                "agentsConfigurationStatus",
                autoboto.TypeInfo(typing.List[AgentConfigurationStatus]),
            ),
        ]

    # Information about agents or the connector that were instructed to start
    # collecting data. Information includes the agent/connector ID, a description
    # of the operation performed, and whether the agent/connector configuration
    # was updated.
    agents_configuration_status: typing.List["AgentConfigurationStatus"
                                            ] = dataclasses.field(
                                                default_factory=list,
                                            )


@dataclasses.dataclass
class StartExportTaskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_data_format",
                "exportDataFormat",
                autoboto.TypeInfo(typing.List[ExportDataFormat]),
            ),
            (
                "filters",
                "filters",
                autoboto.TypeInfo(typing.List[ExportFilter]),
            ),
            (
                "start_time",
                "startTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "endTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The file format for the returned export data. Default value is `CSV`.
    # **Note:** _The_ `GRAPHML` _option has been deprecated._
    export_data_format: typing.List["ExportDataFormat"] = dataclasses.field(
        default_factory=list,
    )

    # If a filter is present, it selects the single `agentId` of the Application
    # Discovery Agent for which data is exported. The `agentId` can be found in
    # the results of the `DescribeAgents` API or CLI. If no filter is present,
    # `startTime` and `endTime` are ignored and exported data includes both
    # Agentless Discovery Connector data and summary data from Application
    # Discovery agents.
    filters: typing.List["ExportFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The start timestamp for exported data from the single Application Discovery
    # Agent selected in the filters. If no value is specified, data is exported
    # starting from the first data collected by the agent.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The end timestamp for exported data from the single Application Discovery
    # Agent selected in the filters. If no value is specified, exported data
    # includes the most recent data collected by the agent.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class StartExportTaskResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_id",
                "exportId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier used to query the status of an export request.
    export_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StopContinuousExportRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "export_id",
                "exportId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID assigned to this export.
    export_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StopContinuousExportResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start_time",
                "startTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "stop_time",
                "stopTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # Timestamp that represents when this continuous export started collecting
    # data.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Timestamp that represents when this continuous export was stopped.
    stop_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class StopDataCollectionByAgentIdsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_ids",
                "agentIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The IDs of the agents or connectors from which to stop collecting data.
    agent_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class StopDataCollectionByAgentIdsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agents_configuration_status",
                "agentsConfigurationStatus",
                autoboto.TypeInfo(typing.List[AgentConfigurationStatus]),
            ),
        ]

    # Information about the agents or connector that were instructed to stop
    # collecting data. Information includes the agent/connector ID, a description
    # of the operation performed, and whether the agent/connector configuration
    # was updated.
    agents_configuration_status: typing.List["AgentConfigurationStatus"
                                            ] = dataclasses.field(
                                                default_factory=list,
                                            )


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    """
    Metadata that help you categorize IT assets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                autoboto.TypeInfo(str),
            ),
            (
                "value",
                "value",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of tag on which to filter.
    key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A value for a tag key on which to filter.
    value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TagFilter(autoboto.ShapeBase):
    """
    The tag filter. Valid names are: `tagKey`, `tagValue`, `configurationId`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "values",
                "values",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A name of the tag filter.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Values for the tag filter.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UpdateApplicationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_id",
                "configurationId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # Configuration ID of the application to be updated.
    configuration_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # New name of the application to be updated.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # New description of the application to be updated.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateApplicationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


class orderString(Enum):
    ASC = "ASC"
    DESC = "DESC"
