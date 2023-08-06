import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class Certificate(autoboto.ShapeBase):
    """
    An object representing the `certificate-authority-data` for your cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data",
                "data",
                autoboto.TypeInfo(str),
            ),
        ]

    # The base64 encoded certificate data required to communicate with your
    # cluster. Add this to the `certificate-authority-data` section of the
    # `kubeconfig` file for your cluster.
    data: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ClientException(autoboto.ShapeBase):
    """
    These errors are usually caused by a client action, such as using an action or
    resource on behalf of a user that doesn't have permissions to use the action or
    resource, or specifying an identifier that is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_name",
                "clusterName",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon EKS cluster associated with the exception.
    cluster_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Cluster(autoboto.ShapeBase):
    """
    An object representing an Amazon EKS cluster.
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
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint",
                "endpoint",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "resources_vpc_config",
                "resourcesVpcConfig",
                autoboto.TypeInfo(VpcConfigResponse),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(ClusterStatus),
            ),
            (
                "certificate_authority",
                "certificateAuthority",
                autoboto.TypeInfo(Certificate),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the cluster.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the cluster.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Unix epoch time stamp in seconds for when the cluster was created.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Kubernetes server version for the cluster.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The endpoint for your Kubernetes API server.
    endpoint: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role that provides permissions
    # for the Kubernetes control plane to make calls to AWS API operations on
    # your behalf.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The VPC subnets and security groups used by the cluster control plane.
    # Amazon EKS VPC resources have specific requirements to work properly with
    # Kubernetes. For more information, see [Cluster VPC
    # Considerations](http://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html)
    # and [Cluster Security Group
    # Considerations](http://docs.aws.amazon.com/eks/latest/userguide/sec-group-
    # reqs.html) in the _Amazon EKS User Guide_.
    resources_vpc_config: "VpcConfigResponse" = dataclasses.field(
        default_factory=dict,
    )

    # The current status of the cluster.
    status: "ClusterStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The `certificate-authority-data` for your cluster.
    certificate_authority: "Certificate" = dataclasses.field(
        default_factory=dict,
    )

    # Unique, case-sensitive identifier you provide to ensure the idempotency of
    # the request.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ClusterStatus(Enum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    FAILED = "FAILED"


@dataclasses.dataclass
class CreateClusterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "resources_vpc_config",
                "resourcesVpcConfig",
                autoboto.TypeInfo(VpcConfigRequest),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(str),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique name to give to your cluster.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role that provides permissions
    # for Amazon EKS to make calls to other AWS API operations on your behalf.
    # For more information, see [Amazon EKS Service IAM
    # Role](http://docs.aws.amazon.com/eks/latest/userguide/service_IAM_role.html)
    # in the __Amazon EKS User Guide_ _
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The VPC subnets and security groups used by the cluster control plane.
    # Amazon EKS VPC resources have specific requirements to work properly with
    # Kubernetes. For more information, see [Cluster VPC
    # Considerations](http://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html)
    # and [Cluster Security Group
    # Considerations](http://docs.aws.amazon.com/eks/latest/userguide/sec-group-
    # reqs.html) in the _Amazon EKS User Guide_.
    resources_vpc_config: "VpcConfigRequest" = dataclasses.field(
        default_factory=dict,
    )

    # The desired Kubernetes version for your cluster. If you do not specify a
    # value here, the latest version available in Amazon EKS is used.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Unique, case-sensitive identifier you provide to ensure the idempotency of
    # the request.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateClusterResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster",
                "cluster",
                autoboto.TypeInfo(Cluster),
            ),
        ]

    # The full description of your new cluster.
    cluster: "Cluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteClusterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the cluster to delete.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteClusterResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster",
                "cluster",
                autoboto.TypeInfo(Cluster),
            ),
        ]

    # The full description of the cluster to delete.
    cluster: "Cluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeClusterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the cluster to describe.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeClusterResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster",
                "cluster",
                autoboto.TypeInfo(Cluster),
            ),
        ]

    # The full description of your specified cluster.
    cluster: "Cluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class InvalidParameterException(autoboto.ShapeBase):
    """
    The specified parameter is invalid. Review the available parameters for the API
    request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_name",
                "clusterName",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon EKS cluster associated with the exception.
    cluster_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListClustersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # The maximum number of cluster results returned by `ListClusters` in
    # paginated output. When this parameter is used, `ListClusters` only returns
    # `maxResults` results in a single page along with a `nextToken` response
    # element. The remaining results of the initial request can be seen by
    # sending another `ListClusters` request with the returned `nextToken` value.
    # This value can be between 1 and 100. If this parameter is not used, then
    # `ListClusters` returns up to 100 results and a `nextToken` value if
    # applicable.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The `nextToken` value returned from a previous paginated `ListClusters`
    # request where `maxResults` was used and the results exceeded the value of
    # that parameter. Pagination continues from the end of the previous results
    # that returned the `nextToken` value.

    # This token should be treated as an opaque identifier that is only used to
    # retrieve the next items in a list and not for other programmatic purposes.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListClustersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "clusters",
                "clusters",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of all of the clusters for your account in the specified region.
    clusters: typing.List[str] = dataclasses.field(default_factory=list, )

    # The `nextToken` value to include in a future `ListClusters` request. When
    # the results of a `ListClusters` request exceed `maxResults`, this value can
    # be used to retrieve the next page of results. This value is `null` when
    # there are no more results to return.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceInUseException(autoboto.ShapeBase):
    """
    The specified resource is in use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_name",
                "clusterName",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon EKS cluster associated with the exception.
    cluster_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceLimitExceededException(autoboto.ShapeBase):
    """
    You have encountered a service limit on the specified resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_name",
                "clusterName",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon EKS cluster associated with the exception.
    cluster_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    The specified resource could not be found. You can view your available clusters
    with ListClusters. Amazon EKS clusters are region-specific.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_name",
                "clusterName",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon EKS cluster associated with the exception.
    cluster_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServerException(autoboto.ShapeBase):
    """
    These errors are usually caused by a server-side issue.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_name",
                "clusterName",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon EKS cluster associated with the exception.
    cluster_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceUnavailableException(autoboto.ShapeBase):
    """
    The service is unavailable, back off and retry the operation.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsupportedAvailabilityZoneException(autoboto.ShapeBase):
    """
    At least one of your specified cluster subnets is in an Availability Zone that
    does not support Amazon EKS. The exception output will specify the supported
    Availability Zones for your account, from which you can choose subnets for your
    cluster.
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
                "cluster_name",
                "clusterName",
                autoboto.TypeInfo(str),
            ),
            (
                "valid_zones",
                "validZones",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon EKS cluster associated with the exception.
    cluster_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The supported Availability Zones for your account. Choose subnets in these
    # Availability Zones for your cluster.
    valid_zones: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class VpcConfigRequest(autoboto.ShapeBase):
    """
    An object representing an Amazon EKS cluster VPC configuration request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_ids",
                "subnetIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "security_group_ids",
                "securityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # Specify subnets for your Amazon EKS worker nodes. Amazon EKS creates cross-
    # account elastic network interfaces in these subnets to allow communication
    # between your worker nodes and the Kubernetes control plane.
    subnet_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # Specify one or more security groups for the cross-account elastic network
    # interfaces that Amazon EKS creates to use to allow communication between
    # your worker nodes and the Kubernetes control plane.
    security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class VpcConfigResponse(autoboto.ShapeBase):
    """
    An object representing an Amazon EKS cluster VPC configuration response.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_ids",
                "subnetIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "security_group_ids",
                "securityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "vpc_id",
                "vpcId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The subnets associated with your cluster.
    subnet_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The security groups associated with the cross-account elastic network
    # interfaces that are used to allow communication between your worker nodes
    # and the Kubernetes control plane.
    security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The VPC associated with your cluster.
    vpc_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
