import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


class ChangeType(Enum):
    IMMEDIATE = "IMMEDIATE"
    REQUIRES_REBOOT = "REQUIRES_REBOOT"


@dataclasses.dataclass
class Cluster(autoboto.ShapeBase):
    """
    Contains all of the attributes of a specific DAX cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_name",
                "ClusterName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "cluster_arn",
                "ClusterArn",
                autoboto.TypeInfo(str),
            ),
            (
                "total_nodes",
                "TotalNodes",
                autoboto.TypeInfo(int),
            ),
            (
                "active_nodes",
                "ActiveNodes",
                autoboto.TypeInfo(int),
            ),
            (
                "node_type",
                "NodeType",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
            (
                "cluster_discovery_endpoint",
                "ClusterDiscoveryEndpoint",
                autoboto.TypeInfo(Endpoint),
            ),
            (
                "node_ids_to_remove",
                "NodeIdsToRemove",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "nodes",
                "Nodes",
                autoboto.TypeInfo(typing.List[Node]),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                autoboto.TypeInfo(str),
            ),
            (
                "notification_configuration",
                "NotificationConfiguration",
                autoboto.TypeInfo(NotificationConfiguration),
            ),
            (
                "subnet_group",
                "SubnetGroup",
                autoboto.TypeInfo(str),
            ),
            (
                "security_groups",
                "SecurityGroups",
                autoboto.TypeInfo(typing.List[SecurityGroupMembership]),
            ),
            (
                "iam_role_arn",
                "IamRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_group",
                "ParameterGroup",
                autoboto.TypeInfo(ParameterGroupStatus),
            ),
            (
                "sse_description",
                "SSEDescription",
                autoboto.TypeInfo(SSEDescription),
            ),
        ]

    # The name of the DAX cluster.
    cluster_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The description of the cluster.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Resource Name (ARN) that uniquely identifies the cluster.
    cluster_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The total number of nodes in the cluster.
    total_nodes: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of nodes in the cluster that are active (i.e., capable of
    # serving requests).
    active_nodes: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The node type for the nodes in the cluster. (All nodes in a DAX cluster are
    # of the same type.)
    node_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The current status of the cluster.
    status: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The configuration endpoint for this DAX cluster, consisting of a DNS name
    # and a port number. Client applications can specify this endpoint, rather
    # than an individual node endpoint, and allow the DAX client software to
    # intelligently route requests and responses to nodes in the DAX cluster.
    cluster_discovery_endpoint: "Endpoint" = dataclasses.field(
        default_factory=dict,
    )

    # A list of nodes to be removed from the cluster.
    node_ids_to_remove: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list of nodes that are currently in the cluster.
    nodes: typing.List["Node"] = dataclasses.field(default_factory=list, )

    # A range of time when maintenance of DAX cluster software will be performed.
    # For example: `sun:01:00-sun:09:00`. Cluster maintenance normally takes less
    # than 30 minutes, and is performed automatically within the maintenance
    # window.
    preferred_maintenance_window: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Describes a notification topic and its status. Notification topics are used
    # for publishing DAX events to subscribers using Amazon Simple Notification
    # Service (SNS).
    notification_configuration: "NotificationConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The subnet group where the DAX cluster is running.
    subnet_group: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of security groups, and the status of each, for the nodes in the
    # cluster.
    security_groups: typing.List["SecurityGroupMembership"] = dataclasses.field(
        default_factory=list,
    )

    # A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime,
    # DAX will assume this role and use the role's permissions to access DynamoDB
    # on your behalf.
    iam_role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The parameter group being used by nodes in the cluster.
    parameter_group: "ParameterGroupStatus" = dataclasses.field(
        default_factory=dict,
    )

    # The description of the server-side encryption status on the specified DAX
    # cluster.
    sse_description: "SSEDescription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ClusterAlreadyExistsFault(autoboto.ShapeBase):
    """
    You already have a DAX cluster with the given identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterNotFoundFault(autoboto.ShapeBase):
    """
    The requested cluster ID does not refer to an existing DAX cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterQuotaForCustomerExceededFault(autoboto.ShapeBase):
    """
    You have attempted to exceed the maximum number of DAX clusters for your AWS
    account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateClusterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_name",
                "ClusterName",
                autoboto.TypeInfo(str),
            ),
            (
                "node_type",
                "NodeType",
                autoboto.TypeInfo(str),
            ),
            (
                "replication_factor",
                "ReplicationFactor",
                autoboto.TypeInfo(int),
            ),
            (
                "iam_role_arn",
                "IamRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "subnet_group_name",
                "SubnetGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                autoboto.TypeInfo(str),
            ),
            (
                "notification_topic_arn",
                "NotificationTopicArn",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_group_name",
                "ParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "sse_specification",
                "SSESpecification",
                autoboto.TypeInfo(SSESpecification),
            ),
        ]

    # The cluster identifier. This parameter is stored as a lowercase string.

    # **Constraints:**

    #   * A name must contain from 1 to 20 alphanumeric characters or hyphens.

    #   * The first character must be a letter.

    #   * A name cannot end with a hyphen or contain two consecutive hyphens.
    cluster_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The compute and memory capacity of the nodes in the cluster.
    node_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of nodes in the DAX cluster. A replication factor of 1 will
    # create a single-node cluster, without any read replicas. For additional
    # fault tolerance, you can create a multiple node cluster with one or more
    # read replicas. To do this, set _ReplicationFactor_ to 2 or more.

    # AWS recommends that you have at least two read replicas per cluster.
    replication_factor: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime,
    # DAX will assume this role and use the role's permissions to access DynamoDB
    # on your behalf.
    iam_role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A description of the cluster.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Availability Zones (AZs) in which the cluster nodes will be created.
    # All nodes belonging to the cluster are placed in these Availability Zones.
    # Use this parameter if you want to distribute the nodes across multiple AZs.
    availability_zones: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The name of the subnet group to be used for the replication group.

    # DAX clusters can only run in an Amazon VPC environment. All of the subnets
    # that you specify in a subnet group must exist in the same VPC.
    subnet_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of security group IDs to be assigned to each node in the DAX
    # cluster. (Each of the security group ID is system-generated.)

    # If this parameter is not specified, DAX assigns the default VPC security
    # group to each node.
    security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Specifies the weekly time range during which maintenance on the DAX cluster
    # is performed. It is specified as a range in the format ddd:hh24:mi-
    # ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute
    # period. Valid values for `ddd` are:

    #   * `sun`

    #   * `mon`

    #   * `tue`

    #   * `wed`

    #   * `thu`

    #   * `fri`

    #   * `sat`

    # Example: `sun:05:00-sun:09:00`

    # If you don't specify a preferred maintenance window when you create or
    # modify a cache cluster, DAX assigns a 60-minute maintenance window on a
    # randomly selected day of the week.
    preferred_maintenance_window: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the Amazon SNS topic to which
    # notifications will be sent.

    # The Amazon SNS topic owner must be same as the DAX cluster owner.
    notification_topic_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The parameter group to be associated with the DAX cluster.
    parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A set of tags to associate with the DAX cluster.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # Represents the settings used to enable server-side encryption on the
    # cluster.
    sse_specification: "SSESpecification" = dataclasses.field(
        default_factory=dict,
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

    # A description of the DAX cluster that you have created.
    cluster: "Cluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateParameterGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_name",
                "ParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the parameter group to apply to all of the clusters in this
    # replication group.
    parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the parameter group.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateParameterGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group",
                "ParameterGroup",
                autoboto.TypeInfo(ParameterGroup),
            ),
        ]

    # Represents the output of a _CreateParameterGroup_ action.
    parameter_group: "ParameterGroup" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateSubnetGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_group_name",
                "SubnetGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # A name for the subnet group. This value is stored as a lowercase string.
    subnet_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of VPC subnet IDs for the subnet group.
    subnet_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # A description for the subnet group
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateSubnetGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_group",
                "SubnetGroup",
                autoboto.TypeInfo(SubnetGroup),
            ),
        ]

    # Represents the output of a _CreateSubnetGroup_ operation.
    subnet_group: "SubnetGroup" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DecreaseReplicationFactorRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_name",
                "ClusterName",
                autoboto.TypeInfo(str),
            ),
            (
                "new_replication_factor",
                "NewReplicationFactor",
                autoboto.TypeInfo(int),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "node_ids_to_remove",
                "NodeIdsToRemove",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the DAX cluster from which you want to remove nodes.
    cluster_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new number of nodes for the DAX cluster.
    new_replication_factor: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Availability Zone(s) from which to remove nodes.
    availability_zones: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The unique identifiers of the nodes to be removed from the cluster.
    node_ids_to_remove: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DecreaseReplicationFactorResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster",
                "Cluster",
                autoboto.TypeInfo(Cluster),
            ),
        ]

    # A description of the DAX cluster, after you have decreased its replication
    # factor.
    cluster: "Cluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteClusterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_name",
                "ClusterName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the cluster to be deleted.
    cluster_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


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

    # A description of the DAX cluster that is being deleted.
    cluster: "Cluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteParameterGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_name",
                "ParameterGroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the parameter group to delete.
    parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteParameterGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deletion_message",
                "DeletionMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-specified message for this action (i.e., a reason for deleting the
    # parameter group).
    deletion_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteSubnetGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_group_name",
                "SubnetGroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the subnet group to delete.
    subnet_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteSubnetGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deletion_message",
                "DeletionMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-specified message for this action (i.e., a reason for deleting the
    # subnet group).
    deletion_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeClustersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_names",
                "ClusterNames",
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

    # The names of the DAX clusters being described.
    cluster_names: typing.List[str] = dataclasses.field(default_factory=list, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved.

    # The value for `MaxResults` must be between 20 and 100.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeClustersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "clusters",
                "Clusters",
                autoboto.TypeInfo(typing.List[Cluster]),
            ),
        ]

    # Provides an identifier to allow retrieval of paginated results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The descriptions of your DAX clusters, in response to a _DescribeClusters_
    # request.
    clusters: typing.List["Cluster"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeDefaultParametersRequest(autoboto.ShapeBase):
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

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved.

    # The value for `MaxResults` must be between 20 and 100.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeDefaultParametersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.List[Parameter]),
            ),
        ]

    # Provides an identifier to allow retrieval of paginated results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of parameters. Each element in the list represents one parameter.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeEventsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_name",
                "SourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "source_type",
                "SourceType",
                autoboto.TypeInfo(SourceType),
            ),
            (
                "start_time",
                "StartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(int),
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

    # The identifier of the event source for which events will be returned. If
    # not specified, then all sources are included in the response.
    source_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The event source to retrieve events for. If no value is specified, all
    # events are returned.
    source_type: "SourceType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The beginning of the time interval to retrieve events for, specified in ISO
    # 8601 format.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The end of the time interval for which to retrieve events, specified in ISO
    # 8601 format.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of minutes' worth of events to retrieve.
    duration: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved.

    # The value for `MaxResults` must be between 20 and 100.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeEventsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "events",
                "Events",
                autoboto.TypeInfo(typing.List[Event]),
            ),
        ]

    # Provides an identifier to allow retrieval of paginated results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of events. Each element in the array represents one event.
    events: typing.List["Event"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeParameterGroupsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_names",
                "ParameterGroupNames",
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

    # The names of the parameter groups.
    parameter_group_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved.

    # The value for `MaxResults` must be between 20 and 100.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeParameterGroupsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_groups",
                "ParameterGroups",
                autoboto.TypeInfo(typing.List[ParameterGroup]),
            ),
        ]

    # Provides an identifier to allow retrieval of paginated results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of parameter groups. Each element in the array represents one
    # parameter group.
    parameter_groups: typing.List["ParameterGroup"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeParametersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_name",
                "ParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "source",
                "Source",
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

    # The name of the parameter group.
    parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # How the parameter is defined. For example, `system` denotes a system-
    # defined parameter.
    source: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved.

    # The value for `MaxResults` must be between 20 and 100.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeParametersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.List[Parameter]),
            ),
        ]

    # Provides an identifier to allow retrieval of paginated results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of parameters within a parameter group. Each element in the list
    # represents one parameter.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeSubnetGroupsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_group_names",
                "SubnetGroupNames",
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

    # The name of the subnet group.
    subnet_group_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of results to include in the response. If more results
    # exist than the specified `MaxResults` value, a token is included in the
    # response so that the remaining results can be retrieved.

    # The value for `MaxResults` must be between 20 and 100.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token, up to the value specified
    # by `MaxResults`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeSubnetGroupsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_groups",
                "SubnetGroups",
                autoboto.TypeInfo(typing.List[SubnetGroup]),
            ),
        ]

    # Provides an identifier to allow retrieval of paginated results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of subnet groups. Each element in the array represents a single
    # subnet group.
    subnet_groups: typing.List["SubnetGroup"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Endpoint(autoboto.ShapeBase):
    """
    Represents the information required for client programs to connect to the
    configuration endpoint for a DAX cluster, or to an individual node within the
    cluster.
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
                "port",
                "Port",
                autoboto.TypeInfo(int),
            ),
        ]

    # The DNS hostname of the endpoint.
    address: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The port number that applications should use to connect to the endpoint.
    port: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Event(autoboto.ShapeBase):
    """
    Represents a single occurrence of something interesting within the system. Some
    examples of events are creating a DAX cluster, adding or removing a node, or
    rebooting a node.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_name",
                "SourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "source_type",
                "SourceType",
                autoboto.TypeInfo(SourceType),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "date",
                "Date",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The source of the event. For example, if the event occurred at the node
    # level, the source would be the node ID.
    source_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the origin of this event - a cluster, a parameter group, a node
    # ID, etc.
    source_type: "SourceType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A user-defined message associated with the event.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date and time when the event occurred.
    date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class IncreaseReplicationFactorRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_name",
                "ClusterName",
                autoboto.TypeInfo(str),
            ),
            (
                "new_replication_factor",
                "NewReplicationFactor",
                autoboto.TypeInfo(int),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the DAX cluster that will receive additional nodes.
    cluster_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new number of nodes for the DAX cluster.
    new_replication_factor: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Availability Zones (AZs) in which the cluster nodes will be created.
    # All nodes belonging to the cluster are placed in these Availability Zones.
    # Use this parameter if you want to distribute the nodes across multiple AZs.
    availability_zones: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class IncreaseReplicationFactorResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster",
                "Cluster",
                autoboto.TypeInfo(Cluster),
            ),
        ]

    # A description of the DAX cluster. with its new replication factor.
    cluster: "Cluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class InsufficientClusterCapacityFault(autoboto.ShapeBase):
    """
    There are not enough system resources to create the cluster you requested (or to
    resize an already-existing cluster).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidARNFault(autoboto.ShapeBase):
    """
    The Amazon Resource Name (ARN) supplied in the request is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidClusterStateFault(autoboto.ShapeBase):
    """
    The requested DAX cluster is not in the _available_ state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidParameterCombinationException(autoboto.ShapeBase):
    """
    Two or more incompatible parameters were specified.
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
class InvalidParameterGroupStateFault(autoboto.ShapeBase):
    """
    One or more parameters in a parameter group are in an invalid state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidParameterValueException(autoboto.ShapeBase):
    """
    The value for a parameter is invalid.
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
class InvalidSubnet(autoboto.ShapeBase):
    """
    An invalid subnet identifier was specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidVPCNetworkStateFault(autoboto.ShapeBase):
    """
    The VPC network is in an invalid state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class IsModifiable(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
    CONDITIONAL = "CONDITIONAL"


@dataclasses.dataclass
class ListTagsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_name",
                "ResourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the DAX resource to which the tags belong.
    resource_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An optional token returned from a prior request. Use this token for
    # pagination of results from this action. If this parameter is specified, the
    # response includes only results beyond the token.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListTagsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # A list of tags currently associated with the DAX cluster.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # If this value is present, there are additional results to be displayed. To
    # retrieve them, call `ListTags` again, with `NextToken` set to this value.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Node(autoboto.ShapeBase):
    """
    Represents an individual node within a DAX cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "node_id",
                "NodeId",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint",
                "Endpoint",
                autoboto.TypeInfo(Endpoint),
            ),
            (
                "node_create_time",
                "NodeCreateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "node_status",
                "NodeStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_group_status",
                "ParameterGroupStatus",
                autoboto.TypeInfo(str),
            ),
        ]

    # A system-generated identifier for the node.
    node_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The endpoint for the node, consisting of a DNS name and a port number.
    # Client applications can connect directly to a node endpoint, if desired (as
    # an alternative to allowing DAX client software to intelligently route
    # requests and responses to nodes in the DAX cluster.
    endpoint: "Endpoint" = dataclasses.field(default_factory=dict, )

    # The date and time (in UNIX epoch format) when the node was launched.
    node_create_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Availability Zone (AZ) in which the node has been deployed.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The current status of the node. For example: `available`.
    node_status: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the parameter group associated with this node. For example,
    # `in-sync`.
    parameter_group_status: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class NodeNotFoundFault(autoboto.ShapeBase):
    """
    None of the nodes in the cluster have the given node ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NodeQuotaForClusterExceededFault(autoboto.ShapeBase):
    """
    You have attempted to exceed the maximum number of nodes for a DAX cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NodeQuotaForCustomerExceededFault(autoboto.ShapeBase):
    """
    You have attempted to exceed the maximum number of nodes for your AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NodeTypeSpecificValue(autoboto.ShapeBase):
    """
    Represents a parameter value that is applicable to a particular node type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "node_type",
                "NodeType",
                autoboto.TypeInfo(str),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
        ]

    # A node type to which the parameter value applies.
    node_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The parameter value for this node type.
    value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class NotificationConfiguration(autoboto.ShapeBase):
    """
    Describes a notification topic and its status. Notification topics are used for
    publishing DAX events to subscribers using Amazon Simple Notification Service
    (SNS).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "topic_arn",
                "TopicArn",
                autoboto.TypeInfo(str),
            ),
            (
                "topic_status",
                "TopicStatus",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) that identifies the topic.
    topic_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The current state of the topic.
    topic_status: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Parameter(autoboto.ShapeBase):
    """
    Describes an individual setting that controls some aspect of DAX behavior.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_name",
                "ParameterName",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_type",
                "ParameterType",
                autoboto.TypeInfo(ParameterType),
            ),
            (
                "parameter_value",
                "ParameterValue",
                autoboto.TypeInfo(str),
            ),
            (
                "node_type_specific_values",
                "NodeTypeSpecificValues",
                autoboto.TypeInfo(typing.List[NodeTypeSpecificValue]),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "source",
                "Source",
                autoboto.TypeInfo(str),
            ),
            (
                "data_type",
                "DataType",
                autoboto.TypeInfo(str),
            ),
            (
                "allowed_values",
                "AllowedValues",
                autoboto.TypeInfo(str),
            ),
            (
                "is_modifiable",
                "IsModifiable",
                autoboto.TypeInfo(IsModifiable),
            ),
            (
                "change_type",
                "ChangeType",
                autoboto.TypeInfo(ChangeType),
            ),
        ]

    # The name of the parameter.
    parameter_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Determines whether the parameter can be applied to any nodes, or only nodes
    # of a particular type.
    parameter_type: "ParameterType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value for the parameter.
    parameter_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of node types, and specific parameter values for each node.
    node_type_specific_values: typing.List["NodeTypeSpecificValue"
                                          ] = dataclasses.field(
                                              default_factory=list,
                                          )

    # A description of the parameter
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # How the parameter is defined. For example, `system` denotes a system-
    # defined parameter.
    source: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The data type of the parameter. For example, `integer`:
    data_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A range of values within which the parameter can be set.
    allowed_values: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the customer is allowed to modify the parameter.
    is_modifiable: "IsModifiable" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The conditions under which changes to this parameter can be applied. For
    # example, `requires-reboot` indicates that a new value for this parameter
    # will only take effect if a node is rebooted.
    change_type: "ChangeType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ParameterGroup(autoboto.ShapeBase):
    """
    A named set of parameters that are applied to all of the nodes in a DAX cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_name",
                "ParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the parameter group.
    parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the parameter group.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ParameterGroupAlreadyExistsFault(autoboto.ShapeBase):
    """
    The specified parameter group already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ParameterGroupNotFoundFault(autoboto.ShapeBase):
    """
    The specified parameter group does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ParameterGroupQuotaExceededFault(autoboto.ShapeBase):
    """
    You have attempted to exceed the maximum number of parameter groups.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ParameterGroupStatus(autoboto.ShapeBase):
    """
    The status of a parameter group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_name",
                "ParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_apply_status",
                "ParameterApplyStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "node_ids_to_reboot",
                "NodeIdsToReboot",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the parameter group.
    parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of parameter updates.
    parameter_apply_status: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The node IDs of one or more nodes to be rebooted.
    node_ids_to_reboot: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ParameterNameValue(autoboto.ShapeBase):
    """
    An individual DAX parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_name",
                "ParameterName",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_value",
                "ParameterValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the parameter.
    parameter_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value of the parameter.
    parameter_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class ParameterType(Enum):
    DEFAULT = "DEFAULT"
    NODE_TYPE_SPECIFIC = "NODE_TYPE_SPECIFIC"


@dataclasses.dataclass
class RebootNodeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_name",
                "ClusterName",
                autoboto.TypeInfo(str),
            ),
            (
                "node_id",
                "NodeId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the DAX cluster containing the node to be rebooted.
    cluster_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The system-assigned ID of the node to be rebooted.
    node_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RebootNodeResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster",
                "Cluster",
                autoboto.TypeInfo(Cluster),
            ),
        ]

    # A description of the DAX cluster after a node has been rebooted.
    cluster: "Cluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class SSEDescription(autoboto.ShapeBase):
    """
    The description of the server-side encryption status on the specified DAX
    cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                autoboto.TypeInfo(SSEStatus),
            ),
        ]

    # The current state of server-side encryption:

    #   * `ENABLING` \- Server-side encryption is being enabled.

    #   * `ENABLED` \- Server-side encryption is enabled.

    #   * `DISABLING` \- Server-side encryption is being disabled.

    #   * `DISABLED` \- Server-side encryption is disabled.
    status: "SSEStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SSESpecification(autoboto.ShapeBase):
    """
    Represents the settings used to enable server-side encryption.
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

    # Indicates whether server-side encryption is enabled (true) or disabled
    # (false) on the cluster.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class SSEStatus(Enum):
    ENABLING = "ENABLING"
    ENABLED = "ENABLED"
    DISABLING = "DISABLING"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class SecurityGroupMembership(autoboto.ShapeBase):
    """
    An individual VPC security group and its status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_group_identifier",
                "SecurityGroupIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID for this security group.
    security_group_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of this security group.
    status: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ServiceLinkedRoleNotFoundFault(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


class SourceType(Enum):
    CLUSTER = "CLUSTER"
    PARAMETER_GROUP = "PARAMETER_GROUP"
    SUBNET_GROUP = "SUBNET_GROUP"


@dataclasses.dataclass
class Subnet(autoboto.ShapeBase):
    """
    Represents the subnet associated with a DAX cluster. This parameter refers to
    subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_identifier",
                "SubnetIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_availability_zone",
                "SubnetAvailabilityZone",
                autoboto.TypeInfo(str),
            ),
        ]

    # The system-assigned identifier for the subnet.
    subnet_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Availability Zone (AZ) for subnet subnet.
    subnet_availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SubnetGroup(autoboto.ShapeBase):
    """
    Represents the output of one of the following actions:

      * _CreateSubnetGroup_

      * _ModifySubnetGroup_
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_group_name",
                "SubnetGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                autoboto.TypeInfo(str),
            ),
            (
                "subnets",
                "Subnets",
                autoboto.TypeInfo(typing.List[Subnet]),
            ),
        ]

    # The name of the subnet group.
    subnet_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The description of the subnet group.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.
    vpc_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of subnets associated with the subnet group.
    subnets: typing.List["Subnet"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class SubnetGroupAlreadyExistsFault(autoboto.ShapeBase):
    """
    The specified subnet group already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubnetGroupInUseFault(autoboto.ShapeBase):
    """
    The specified subnet group is currently in use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubnetGroupNotFoundFault(autoboto.ShapeBase):
    """
    The requested subnet group name does not refer to an existing subnet group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubnetGroupQuotaExceededFault(autoboto.ShapeBase):
    """
    The request cannot be processed because it would exceed the allowed number of
    subnets in a subnet group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubnetInUse(autoboto.ShapeBase):
    """
    The requested subnet is being used by another subnet group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubnetQuotaExceededFault(autoboto.ShapeBase):
    """
    The request cannot be processed because it would exceed the allowed number of
    subnets in a subnet group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    """
    A description of a tag. Every tag is a key-value pair. You can add up to 50 tags
    to a single DAX cluster.

    AWS-assigned tag names and values are automatically assigned the `aws:` prefix,
    which the user cannot assign. AWS-assigned tag names do not count towards the
    tag limit of 50. User-assigned tag names have the prefix `user:`.

    You cannot backdate the application of a tag.
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

    # The key for the tag. Tag keys are case sensitive. Every DAX cluster can
    # only have one tag with the same key. If you try to add an existing tag
    # (same key), the existing tag value will be updated to the new value.
    key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value of the tag. Tag values are case-sensitive and can be null.
    value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TagNotFoundFault(autoboto.ShapeBase):
    """
    The tag does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TagQuotaPerResourceExceeded(autoboto.ShapeBase):
    """
    You have exceeded the maximum number of tags for this DAX cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TagResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_name",
                "ResourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the DAX resource to which tags should be added.
    resource_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The tags to be assigned to the DAX resource.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class TagResourceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The list of tags that are associated with the DAX resource.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UntagResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_name",
                "ResourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the DAX resource from which the tags should be removed.
    resource_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of tag keys. If the DAX cluster has any tags with these keys, then
    # the tags are removed from the cluster.
    tag_keys: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UntagResourceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The tag keys that have been removed from the cluster.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UpdateClusterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_name",
                "ClusterName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                autoboto.TypeInfo(str),
            ),
            (
                "notification_topic_arn",
                "NotificationTopicArn",
                autoboto.TypeInfo(str),
            ),
            (
                "notification_topic_status",
                "NotificationTopicStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_group_name",
                "ParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the DAX cluster to be modified.
    cluster_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A description of the changes being made to the cluster.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A range of time when maintenance of DAX cluster software will be performed.
    # For example: `sun:01:00-sun:09:00`. Cluster maintenance normally takes less
    # than 30 minutes, and is performed automatically within the maintenance
    # window.
    preferred_maintenance_window: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) that identifies the topic.
    notification_topic_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The current state of the topic.
    notification_topic_status: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of a parameter group for this cluster.
    parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of user-specified security group IDs to be assigned to each node in
    # the DAX cluster. If this parameter is not specified, DAX assigns the
    # default VPC security group to each node.
    security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateClusterResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster",
                "Cluster",
                autoboto.TypeInfo(Cluster),
            ),
        ]

    # A description of the DAX cluster, after it has been modified.
    cluster: "Cluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateParameterGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_name",
                "ParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_name_values",
                "ParameterNameValues",
                autoboto.TypeInfo(typing.List[ParameterNameValue]),
            ),
        ]

    # The name of the parameter group.
    parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An array of name-value pairs for the parameters in the group. Each element
    # in the array represents a single parameter.
    parameter_name_values: typing.List["ParameterNameValue"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )


@dataclasses.dataclass
class UpdateParameterGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group",
                "ParameterGroup",
                autoboto.TypeInfo(ParameterGroup),
            ),
        ]

    # The parameter group that has been modified.
    parameter_group: "ParameterGroup" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateSubnetGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_group_name",
                "SubnetGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the subnet group.
    subnet_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the subnet group.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of subnet IDs in the subnet group.
    subnet_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UpdateSubnetGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_group",
                "SubnetGroup",
                autoboto.TypeInfo(SubnetGroup),
            ),
        ]

    # The subnet group that has been modified.
    subnet_group: "SubnetGroup" = dataclasses.field(default_factory=dict, )
