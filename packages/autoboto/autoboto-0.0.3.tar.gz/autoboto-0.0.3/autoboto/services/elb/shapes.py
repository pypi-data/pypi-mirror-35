import datetime
import typing
import autoboto
import dataclasses


@dataclasses.dataclass
class AccessLog(autoboto.ShapeBase):
    """
    Information about the `AccessLog` attribute.
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
                "s3_bucket_name",
                "S3BucketName",
                autoboto.TypeInfo(str),
            ),
            (
                "emit_interval",
                "EmitInterval",
                autoboto.TypeInfo(int),
            ),
            (
                "s3_bucket_prefix",
                "S3BucketPrefix",
                autoboto.TypeInfo(str),
            ),
        ]

    # Specifies whether access logs are enabled for the load balancer.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the Amazon S3 bucket where the access logs are stored.
    s3_bucket_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The interval for publishing the access logs. You can specify an interval of
    # either 5 minutes or 60 minutes.

    # Default: 60 minutes
    emit_interval: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The logical hierarchy you created for your Amazon S3 bucket, for example
    # `my-bucket-prefix/prod`. If the prefix is not provided, the log is placed
    # at the root level of the bucket.
    s3_bucket_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AccessPointNotFoundException(autoboto.ShapeBase):
    """
    The specified load balancer does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AddAvailabilityZonesInput(autoboto.ShapeBase):
    """
    Contains the parameters for EnableAvailabilityZonesForLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Availability Zones. These must be in the same region as the load
    # balancer.
    availability_zones: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AddAvailabilityZonesOutput(autoboto.ShapeBase):
    """
    Contains the output of EnableAvailabilityZonesForLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "availability_zones",
                "AvailabilityZones",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The updated list of Availability Zones for the load balancer.
    availability_zones: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AddTagsInput(autoboto.ShapeBase):
    """
    Contains the parameters for AddTags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_names",
                "LoadBalancerNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the load balancer. You can specify one load balancer only.
    load_balancer_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The tags.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class AddTagsOutput(autoboto.ShapeBase):
    """
    Contains the output of AddTags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AdditionalAttribute(autoboto.ShapeBase):
    """
    This data type is reserved.
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

    # This parameter is reserved.
    key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # This parameter is reserved.
    value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AppCookieStickinessPolicy(autoboto.ShapeBase):
    """
    Information about a policy for application-controlled session stickiness.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "PolicyName",
                autoboto.TypeInfo(str),
            ),
            (
                "cookie_name",
                "CookieName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The mnemonic name for the policy being created. The name must be unique
    # within a set of policies for this load balancer.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the application cookie used for stickiness.
    cookie_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ApplySecurityGroupsToLoadBalancerInput(autoboto.ShapeBase):
    """
    Contains the parameters for ApplySecurityGroupsToLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "security_groups",
                "SecurityGroups",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IDs of the security groups to associate with the load balancer. Note
    # that you cannot specify the name of the security group.
    security_groups: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ApplySecurityGroupsToLoadBalancerOutput(autoboto.ShapeBase):
    """
    Contains the output of ApplySecurityGroupsToLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_groups",
                "SecurityGroups",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The IDs of the security groups associated with the load balancer.
    security_groups: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AttachLoadBalancerToSubnetsInput(autoboto.ShapeBase):
    """
    Contains the parameters for AttachLoaBalancerToSubnets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "subnets",
                "Subnets",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IDs of the subnets to add. You can add only one subnet per Availability
    # Zone.
    subnets: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class AttachLoadBalancerToSubnetsOutput(autoboto.ShapeBase):
    """
    Contains the output of AttachLoadBalancerToSubnets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnets",
                "Subnets",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The IDs of the subnets attached to the load balancer.
    subnets: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class BackendServerDescription(autoboto.ShapeBase):
    """
    Information about the configuration of an EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_port",
                "InstancePort",
                autoboto.TypeInfo(int),
            ),
            (
                "policy_names",
                "PolicyNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The port on which the EC2 instance is listening.
    instance_port: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The names of the policies enabled for the EC2 instance.
    policy_names: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CertificateNotFoundException(autoboto.ShapeBase):
    """
    The specified ARN does not refer to a valid SSL certificate in AWS Identity and
    Access Management (IAM) or AWS Certificate Manager (ACM). Note that if you
    recently uploaded the certificate to IAM, this error might indicate that the
    certificate is not fully available yet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ConfigureHealthCheckInput(autoboto.ShapeBase):
    """
    Contains the parameters for ConfigureHealthCheck.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "health_check",
                "HealthCheck",
                autoboto.TypeInfo(HealthCheck),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The configuration information.
    health_check: "HealthCheck" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ConfigureHealthCheckOutput(autoboto.ShapeBase):
    """
    Contains the output of ConfigureHealthCheck.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "health_check",
                "HealthCheck",
                autoboto.TypeInfo(HealthCheck),
            ),
        ]

    # The updated health check.
    health_check: "HealthCheck" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ConnectionDraining(autoboto.ShapeBase):
    """
    Information about the `ConnectionDraining` attribute.
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
                "timeout",
                "Timeout",
                autoboto.TypeInfo(int),
            ),
        ]

    # Specifies whether connection draining is enabled for the load balancer.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum time, in seconds, to keep the existing connections open before
    # deregistering the instances.
    timeout: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ConnectionSettings(autoboto.ShapeBase):
    """
    Information about the `ConnectionSettings` attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "idle_timeout",
                "IdleTimeout",
                autoboto.TypeInfo(int),
            ),
        ]

    # The time, in seconds, that the connection is allowed to be idle (no data
    # has been sent over the connection) before it is closed by the load
    # balancer.
    idle_timeout: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateAccessPointInput(autoboto.ShapeBase):
    """
    Contains the parameters for CreateLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "listeners",
                "Listeners",
                autoboto.TypeInfo(typing.List[Listener]),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "subnets",
                "Subnets",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "security_groups",
                "SecurityGroups",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "scheme",
                "Scheme",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the load balancer.

    # This name must be unique within your set of load balancers for the region,
    # must have a maximum of 32 characters, must contain only alphanumeric
    # characters or hyphens, and cannot begin or end with a hyphen.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The listeners.

    # For more information, see [Listeners for Your Classic Load
    # Balancer](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
    # listener-config.html) in the _Classic Load Balancer Guide_.
    listeners: typing.List["Listener"] = dataclasses.field(
        default_factory=list,
    )

    # One or more Availability Zones from the same region as the load balancer.

    # You must specify at least one Availability Zone.

    # You can add more Availability Zones after you create the load balancer
    # using EnableAvailabilityZonesForLoadBalancer.
    availability_zones: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The IDs of the subnets in your VPC to attach to the load balancer. Specify
    # one subnet per Availability Zone specified in `AvailabilityZones`.
    subnets: typing.List[str] = dataclasses.field(default_factory=list, )

    # The IDs of the security groups to assign to the load balancer.
    security_groups: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The type of a load balancer. Valid only for load balancers in a VPC.

    # By default, Elastic Load Balancing creates an Internet-facing load balancer
    # with a DNS name that resolves to public IP addresses. For more information
    # about Internet-facing and Internal load balancers, see [Load Balancer
    # Scheme](http://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-
    # elastic-load-balancing-works.html#load-balancer-scheme) in the _Elastic
    # Load Balancing User Guide_.

    # Specify `internal` to create a load balancer with a DNS name that resolves
    # to private IP addresses.
    scheme: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of tags to assign to the load balancer.

    # For more information about tagging your load balancer, see [Tag Your
    # Classic Load
    # Balancer](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/add-
    # remove-tags.html) in the _Classic Load Balancer Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateAccessPointOutput(autoboto.ShapeBase):
    """
    Contains the output for CreateLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dns_name",
                "DNSName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The DNS name of the load balancer.
    dns_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateAppCookieStickinessPolicyInput(autoboto.ShapeBase):
    """
    Contains the parameters for CreateAppCookieStickinessPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                autoboto.TypeInfo(str),
            ),
            (
                "cookie_name",
                "CookieName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the policy being created. Policy names must consist of
    # alphanumeric characters and dashes (-). This name must be unique within the
    # set of policies for this load balancer.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the application cookie used for stickiness.
    cookie_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateAppCookieStickinessPolicyOutput(autoboto.ShapeBase):
    """
    Contains the output for CreateAppCookieStickinessPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateLBCookieStickinessPolicyInput(autoboto.ShapeBase):
    """
    Contains the parameters for CreateLBCookieStickinessPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                autoboto.TypeInfo(str),
            ),
            (
                "cookie_expiration_period",
                "CookieExpirationPeriod",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the policy being created. Policy names must consist of
    # alphanumeric characters and dashes (-). This name must be unique within the
    # set of policies for this load balancer.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time period, in seconds, after which the cookie should be considered
    # stale. If you do not specify this parameter, the default value is 0, which
    # indicates that the sticky session should last for the duration of the
    # browser session.
    cookie_expiration_period: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateLBCookieStickinessPolicyOutput(autoboto.ShapeBase):
    """
    Contains the output for CreateLBCookieStickinessPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateLoadBalancerListenerInput(autoboto.ShapeBase):
    """
    Contains the parameters for CreateLoadBalancerListeners.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "listeners",
                "Listeners",
                autoboto.TypeInfo(typing.List[Listener]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The listeners.
    listeners: typing.List["Listener"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateLoadBalancerListenerOutput(autoboto.ShapeBase):
    """
    Contains the parameters for CreateLoadBalancerListener.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateLoadBalancerPolicyInput(autoboto.ShapeBase):
    """
    Contains the parameters for CreateLoadBalancerPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_type_name",
                "PolicyTypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_attributes",
                "PolicyAttributes",
                autoboto.TypeInfo(typing.List[PolicyAttribute]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the load balancer policy to be created. This name must be
    # unique within the set of policies for this load balancer.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the base policy type. To get the list of policy types, use
    # DescribeLoadBalancerPolicyTypes.
    policy_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The policy attributes.
    policy_attributes: typing.List["PolicyAttribute"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateLoadBalancerPolicyOutput(autoboto.ShapeBase):
    """
    Contains the output of CreateLoadBalancerPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CrossZoneLoadBalancing(autoboto.ShapeBase):
    """
    Information about the `CrossZoneLoadBalancing` attribute.
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

    # Specifies whether cross-zone load balancing is enabled for the load
    # balancer.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteAccessPointInput(autoboto.ShapeBase):
    """
    Contains the parameters for DeleteLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteAccessPointOutput(autoboto.ShapeBase):
    """
    Contains the output of DeleteLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteLoadBalancerListenerInput(autoboto.ShapeBase):
    """
    Contains the parameters for DeleteLoadBalancerListeners.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "load_balancer_ports",
                "LoadBalancerPorts",
                autoboto.TypeInfo(typing.List[int]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The client port numbers of the listeners.
    load_balancer_ports: typing.List[int] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DeleteLoadBalancerListenerOutput(autoboto.ShapeBase):
    """
    Contains the output of DeleteLoadBalancerListeners.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteLoadBalancerPolicyInput(autoboto.ShapeBase):
    """
    Contains the parameters for DeleteLoadBalancerPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the policy.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteLoadBalancerPolicyOutput(autoboto.ShapeBase):
    """
    Contains the output of DeleteLoadBalancerPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DependencyThrottleException(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeregisterEndPointsInput(autoboto.ShapeBase):
    """
    Contains the parameters for DeregisterInstancesFromLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "instances",
                "Instances",
                autoboto.TypeInfo(typing.List[Instance]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IDs of the instances.
    instances: typing.List["Instance"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DeregisterEndPointsOutput(autoboto.ShapeBase):
    """
    Contains the output of DeregisterInstancesFromLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instances",
                "Instances",
                autoboto.TypeInfo(typing.List[Instance]),
            ),
        ]

    # The remaining instances registered with the load balancer.
    instances: typing.List["Instance"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeAccessPointsInput(autoboto.ShapeBase):
    """
    Contains the parameters for DescribeLoadBalancers.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_names",
                "LoadBalancerNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
        ]

    # The names of the load balancers.
    load_balancer_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return with this call (a number from 1 to
    # 400). The default is 400.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeAccessPointsOutput(autoboto.ShapeBase):
    """
    Contains the parameters for DescribeLoadBalancers.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_descriptions",
                "LoadBalancerDescriptions",
                autoboto.TypeInfo(typing.List[LoadBalancerDescription]),
            ),
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the load balancers.
    load_balancer_descriptions: typing.List["LoadBalancerDescription"
                                           ] = dataclasses.field(
                                               default_factory=list,
                                           )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeAccountLimitsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
        ]

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeAccountLimitsOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "limits",
                "Limits",
                autoboto.TypeInfo(typing.List[Limit]),
            ),
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the limits.
    limits: typing.List["Limit"] = dataclasses.field(default_factory=list, )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeEndPointStateInput(autoboto.ShapeBase):
    """
    Contains the parameters for DescribeInstanceHealth.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "instances",
                "Instances",
                autoboto.TypeInfo(typing.List[Instance]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IDs of the instances.
    instances: typing.List["Instance"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeEndPointStateOutput(autoboto.ShapeBase):
    """
    Contains the output for DescribeInstanceHealth.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_states",
                "InstanceStates",
                autoboto.TypeInfo(typing.List[InstanceState]),
            ),
        ]

    # Information about the health of the instances.
    instance_states: typing.List["InstanceState"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeLoadBalancerAttributesInput(autoboto.ShapeBase):
    """
    Contains the parameters for DescribeLoadBalancerAttributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeLoadBalancerAttributesOutput(autoboto.ShapeBase):
    """
    Contains the output of DescribeLoadBalancerAttributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_attributes",
                "LoadBalancerAttributes",
                autoboto.TypeInfo(LoadBalancerAttributes),
            ),
        ]

    # Information about the load balancer attributes.
    load_balancer_attributes: "LoadBalancerAttributes" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeLoadBalancerPoliciesInput(autoboto.ShapeBase):
    """
    Contains the parameters for DescribeLoadBalancerPolicies.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_names",
                "PolicyNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The names of the policies.
    policy_names: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeLoadBalancerPoliciesOutput(autoboto.ShapeBase):
    """
    Contains the output of DescribeLoadBalancerPolicies.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_descriptions",
                "PolicyDescriptions",
                autoboto.TypeInfo(typing.List[PolicyDescription]),
            ),
        ]

    # Information about the policies.
    policy_descriptions: typing.List["PolicyDescription"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeLoadBalancerPolicyTypesInput(autoboto.ShapeBase):
    """
    Contains the parameters for DescribeLoadBalancerPolicyTypes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_type_names",
                "PolicyTypeNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The names of the policy types. If no names are specified, describes all
    # policy types defined by Elastic Load Balancing.
    policy_type_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeLoadBalancerPolicyTypesOutput(autoboto.ShapeBase):
    """
    Contains the output of DescribeLoadBalancerPolicyTypes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_type_descriptions",
                "PolicyTypeDescriptions",
                autoboto.TypeInfo(typing.List[PolicyTypeDescription]),
            ),
        ]

    # Information about the policy types.
    policy_type_descriptions: typing.List["PolicyTypeDescription"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )


@dataclasses.dataclass
class DescribeTagsInput(autoboto.ShapeBase):
    """
    Contains the parameters for DescribeTags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_names",
                "LoadBalancerNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The names of the load balancers.
    load_balancer_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeTagsOutput(autoboto.ShapeBase):
    """
    Contains the output for DescribeTags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_descriptions",
                "TagDescriptions",
                autoboto.TypeInfo(typing.List[TagDescription]),
            ),
        ]

    # Information about the tags.
    tag_descriptions: typing.List["TagDescription"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DetachLoadBalancerFromSubnetsInput(autoboto.ShapeBase):
    """
    Contains the parameters for DetachLoadBalancerFromSubnets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "subnets",
                "Subnets",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IDs of the subnets.
    subnets: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DetachLoadBalancerFromSubnetsOutput(autoboto.ShapeBase):
    """
    Contains the output of DetachLoadBalancerFromSubnets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnets",
                "Subnets",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The IDs of the remaining subnets for the load balancer.
    subnets: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DuplicateAccessPointNameException(autoboto.ShapeBase):
    """
    The specified load balancer name already exists for this account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DuplicateListenerException(autoboto.ShapeBase):
    """
    A listener already exists for the specified load balancer name and port, but
    with a different instance port, protocol, or SSL certificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DuplicatePolicyNameException(autoboto.ShapeBase):
    """
    A policy with the specified name already exists for this load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DuplicateTagKeysException(autoboto.ShapeBase):
    """
    A tag key was specified more than once.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class HealthCheck(autoboto.ShapeBase):
    """
    Information about a health check.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target",
                "Target",
                autoboto.TypeInfo(str),
            ),
            (
                "interval",
                "Interval",
                autoboto.TypeInfo(int),
            ),
            (
                "timeout",
                "Timeout",
                autoboto.TypeInfo(int),
            ),
            (
                "unhealthy_threshold",
                "UnhealthyThreshold",
                autoboto.TypeInfo(int),
            ),
            (
                "healthy_threshold",
                "HealthyThreshold",
                autoboto.TypeInfo(int),
            ),
        ]

    # The instance being checked. The protocol is either TCP, HTTP, HTTPS, or
    # SSL. The range of valid ports is one (1) through 65535.

    # TCP is the default, specified as a TCP: port pair, for example "TCP:5000".
    # In this case, a health check simply attempts to open a TCP connection to
    # the instance on the specified port. Failure to connect within the
    # configured timeout is considered unhealthy.

    # SSL is also specified as SSL: port pair, for example, SSL:5000.

    # For HTTP/HTTPS, you must include a ping path in the string. HTTP is
    # specified as a HTTP:port;/;PathToPing; grouping, for example
    # "HTTP:80/weather/us/wa/seattle". In this case, a HTTP GET request is issued
    # to the instance on the given port and path. Any answer other than "200 OK"
    # within the timeout period is considered unhealthy.

    # The total length of the HTTP ping target must be 1024 16-bit Unicode
    # characters or less.
    target: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The approximate interval, in seconds, between health checks of an
    # individual instance.
    interval: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The amount of time, in seconds, during which no response means a failed
    # health check.

    # This value must be less than the `Interval` value.
    timeout: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of consecutive health check failures required before moving the
    # instance to the `Unhealthy` state.
    unhealthy_threshold: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of consecutive health checks successes required before moving
    # the instance to the `Healthy` state.
    healthy_threshold: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Instance(autoboto.ShapeBase):
    """
    The ID of an EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InstanceState(autoboto.ShapeBase):
    """
    Information about the state of an EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(str),
            ),
            (
                "reason_code",
                "ReasonCode",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The current state of the instance.

    # Valid values: `InService` | `OutOfService` | `Unknown`
    state: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information about the cause of `OutOfService` instances. Specifically,
    # whether the cause is Elastic Load Balancing or the instance.

    # Valid values: `ELB` | `Instance` | `N/A`
    reason_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A description of the instance state. This string can contain one or more of
    # the following messages.

    #   * `N/A`

    #   * `A transient error occurred. Please try again later.`

    #   * `Instance has failed at least the UnhealthyThreshold number of health checks consecutively.`

    #   * `Instance has not passed the configured HealthyThreshold number of health checks consecutively.`

    #   * `Instance registration is still in progress.`

    #   * `Instance is in the EC2 Availability Zone for which LoadBalancer is not configured to route traffic to.`

    #   * `Instance is not currently registered with the LoadBalancer.`

    #   * `Instance deregistration currently in progress.`

    #   * `Disable Availability Zone is currently in progress.`

    #   * `Instance is in pending state.`

    #   * `Instance is in stopped state.`

    #   * `Instance is in terminated state.`
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidConfigurationRequestException(autoboto.ShapeBase):
    """
    The requested configuration change is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidEndPointException(autoboto.ShapeBase):
    """
    The specified endpoint is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSchemeException(autoboto.ShapeBase):
    """
    The specified value for the schema is not valid. You can only specify a scheme
    for load balancers in a VPC.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSecurityGroupException(autoboto.ShapeBase):
    """
    One or more of the specified security groups do not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSubnetException(autoboto.ShapeBase):
    """
    The specified VPC has no associated Internet gateway.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LBCookieStickinessPolicy(autoboto.ShapeBase):
    """
    Information about a policy for duration-based session stickiness.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "PolicyName",
                autoboto.TypeInfo(str),
            ),
            (
                "cookie_expiration_period",
                "CookieExpirationPeriod",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the policy. This name must be unique within the set of policies
    # for this load balancer.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time period, in seconds, after which the cookie should be considered
    # stale. If this parameter is not specified, the stickiness session lasts for
    # the duration of the browser session.
    cookie_expiration_period: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Limit(autoboto.ShapeBase):
    """
    Information about an Elastic Load Balancing resource limit for your AWS account.
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
                "max",
                "Max",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the limit. The possible values are:

    #   * classic-listeners

    #   * classic-load-balancers
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum value of the limit.
    max: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Listener(autoboto.ShapeBase):
    """
    Information about a listener.

    For information about the protocols and the ports supported by Elastic Load
    Balancing, see [Listeners for Your Classic Load
    Balancer](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
    listener-config.html) in the _Classic Load Balancer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "protocol",
                "Protocol",
                autoboto.TypeInfo(str),
            ),
            (
                "load_balancer_port",
                "LoadBalancerPort",
                autoboto.TypeInfo(int),
            ),
            (
                "instance_port",
                "InstancePort",
                autoboto.TypeInfo(int),
            ),
            (
                "instance_protocol",
                "InstanceProtocol",
                autoboto.TypeInfo(str),
            ),
            (
                "ssl_certificate_id",
                "SSLCertificateId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP,
    # or SSL.
    protocol: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The port on which the load balancer is listening. On EC2-VPC, you can
    # specify any port from the range 1-65535. On EC2-Classic, you can specify
    # any port from the following list: 25, 80, 443, 465, 587, 1024-65535.
    load_balancer_port: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The port on which the instance is listening.
    instance_port: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or
    # SSL.

    # If the front-end protocol is HTTP, HTTPS, TCP, or SSL, `InstanceProtocol`
    # must be at the same protocol.

    # If there is another listener with the same `InstancePort` whose
    # `InstanceProtocol` is secure, (HTTPS or SSL), the listener's
    # `InstanceProtocol` must also be secure.

    # If there is another listener with the same `InstancePort` whose
    # `InstanceProtocol` is HTTP or TCP, the listener's `InstanceProtocol` must
    # be HTTP or TCP.
    instance_protocol: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the server certificate.
    ssl_certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListenerDescription(autoboto.ShapeBase):
    """
    The policies enabled for a listener.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "listener",
                "Listener",
                autoboto.TypeInfo(Listener),
            ),
            (
                "policy_names",
                "PolicyNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The listener.
    listener: "Listener" = dataclasses.field(default_factory=dict, )

    # The policies. If there are no policies enabled, the list is empty.
    policy_names: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class ListenerNotFoundException(autoboto.ShapeBase):
    """
    The load balancer does not have a listener configured at the specified port.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LoadBalancerAttributeNotFoundException(autoboto.ShapeBase):
    """
    The specified load balancer attribute does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LoadBalancerAttributes(autoboto.ShapeBase):
    """
    The attributes for a load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cross_zone_load_balancing",
                "CrossZoneLoadBalancing",
                autoboto.TypeInfo(CrossZoneLoadBalancing),
            ),
            (
                "access_log",
                "AccessLog",
                autoboto.TypeInfo(AccessLog),
            ),
            (
                "connection_draining",
                "ConnectionDraining",
                autoboto.TypeInfo(ConnectionDraining),
            ),
            (
                "connection_settings",
                "ConnectionSettings",
                autoboto.TypeInfo(ConnectionSettings),
            ),
            (
                "additional_attributes",
                "AdditionalAttributes",
                autoboto.TypeInfo(typing.List[AdditionalAttribute]),
            ),
        ]

    # If enabled, the load balancer routes the request traffic evenly across all
    # instances regardless of the Availability Zones.

    # For more information, see [Configure Cross-Zone Load
    # Balancing](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-
    # disable-crosszone-lb.html) in the _Classic Load Balancer Guide_.
    cross_zone_load_balancing: "CrossZoneLoadBalancing" = dataclasses.field(
        default_factory=dict,
    )

    # If enabled, the load balancer captures detailed information of all requests
    # and delivers the information to the Amazon S3 bucket that you specify.

    # For more information, see [Enable Access
    # Logs](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-
    # access-logs.html) in the _Classic Load Balancer Guide_.
    access_log: "AccessLog" = dataclasses.field(default_factory=dict, )

    # If enabled, the load balancer allows existing requests to complete before
    # the load balancer shifts traffic away from a deregistered or unhealthy
    # instance.

    # For more information, see [Configure Connection
    # Draining](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-
    # conn-drain.html) in the _Classic Load Balancer Guide_.
    connection_draining: "ConnectionDraining" = dataclasses.field(
        default_factory=dict,
    )

    # If enabled, the load balancer allows the connections to remain idle (no
    # data is sent over the connection) for the specified duration.

    # By default, Elastic Load Balancing maintains a 60-second idle connection
    # timeout for both front-end and back-end connections of your load balancer.
    # For more information, see [Configure Idle Connection
    # Timeout](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-
    # idle-timeout.html) in the _Classic Load Balancer Guide_.
    connection_settings: "ConnectionSettings" = dataclasses.field(
        default_factory=dict,
    )

    # This parameter is reserved.
    additional_attributes: typing.List["AdditionalAttribute"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )


@dataclasses.dataclass
class LoadBalancerDescription(autoboto.ShapeBase):
    """
    Information about a load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "dns_name",
                "DNSName",
                autoboto.TypeInfo(str),
            ),
            (
                "canonical_hosted_zone_name",
                "CanonicalHostedZoneName",
                autoboto.TypeInfo(str),
            ),
            (
                "canonical_hosted_zone_name_id",
                "CanonicalHostedZoneNameID",
                autoboto.TypeInfo(str),
            ),
            (
                "listener_descriptions",
                "ListenerDescriptions",
                autoboto.TypeInfo(typing.List[ListenerDescription]),
            ),
            (
                "policies",
                "Policies",
                autoboto.TypeInfo(Policies),
            ),
            (
                "backend_server_descriptions",
                "BackendServerDescriptions",
                autoboto.TypeInfo(typing.List[BackendServerDescription]),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "subnets",
                "Subnets",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "vpc_id",
                "VPCId",
                autoboto.TypeInfo(str),
            ),
            (
                "instances",
                "Instances",
                autoboto.TypeInfo(typing.List[Instance]),
            ),
            (
                "health_check",
                "HealthCheck",
                autoboto.TypeInfo(HealthCheck),
            ),
            (
                "source_security_group",
                "SourceSecurityGroup",
                autoboto.TypeInfo(SourceSecurityGroup),
            ),
            (
                "security_groups",
                "SecurityGroups",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "scheme",
                "Scheme",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The DNS name of the load balancer.
    dns_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The DNS name of the load balancer.

    # For more information, see [Configure a Custom Domain
    # Name](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/using-
    # domain-names-with-elb.html) in the _Classic Load Balancer Guide_.
    canonical_hosted_zone_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the Amazon Route 53 hosted zone for the load balancer.
    canonical_hosted_zone_name_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The listeners for the load balancer.
    listener_descriptions: typing.List["ListenerDescription"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )

    # The policies defined for the load balancer.
    policies: "Policies" = dataclasses.field(default_factory=dict, )

    # Information about your EC2 instances.
    backend_server_descriptions: typing.List["BackendServerDescription"
                                            ] = dataclasses.field(
                                                default_factory=list,
                                            )

    # The Availability Zones for the load balancer.
    availability_zones: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The IDs of the subnets for the load balancer.
    subnets: typing.List[str] = dataclasses.field(default_factory=list, )

    # The ID of the VPC for the load balancer.
    vpc_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The IDs of the instances for the load balancer.
    instances: typing.List["Instance"] = dataclasses.field(
        default_factory=list,
    )

    # Information about the health checks conducted on the load balancer.
    health_check: "HealthCheck" = dataclasses.field(default_factory=dict, )

    # The security group for the load balancer, which you can use as part of your
    # inbound rules for your registered instances. To only allow traffic from
    # load balancers, add a security group rule that specifies this source
    # security group as the inbound source.
    source_security_group: "SourceSecurityGroup" = dataclasses.field(
        default_factory=dict,
    )

    # The security groups for the load balancer. Valid only for load balancers in
    # a VPC.
    security_groups: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The date and time the load balancer was created.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of load balancer. Valid only for load balancers in a VPC.

    # If `Scheme` is `internet-facing`, the load balancer has a public DNS name
    # that resolves to a public IP address.

    # If `Scheme` is `internal`, the load balancer has a public DNS name that
    # resolves to a private IP address.
    scheme: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ModifyLoadBalancerAttributesInput(autoboto.ShapeBase):
    """
    Contains the parameters for ModifyLoadBalancerAttributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "load_balancer_attributes",
                "LoadBalancerAttributes",
                autoboto.TypeInfo(LoadBalancerAttributes),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The attributes for the load balancer.
    load_balancer_attributes: "LoadBalancerAttributes" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ModifyLoadBalancerAttributesOutput(autoboto.ShapeBase):
    """
    Contains the output of ModifyLoadBalancerAttributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "load_balancer_attributes",
                "LoadBalancerAttributes",
                autoboto.TypeInfo(LoadBalancerAttributes),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the load balancer attributes.
    load_balancer_attributes: "LoadBalancerAttributes" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class OperationNotPermittedException(autoboto.ShapeBase):
    """
    This operation is not allowed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Policies(autoboto.ShapeBase):
    """
    The policies for a load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "app_cookie_stickiness_policies",
                "AppCookieStickinessPolicies",
                autoboto.TypeInfo(typing.List[AppCookieStickinessPolicy]),
            ),
            (
                "lb_cookie_stickiness_policies",
                "LBCookieStickinessPolicies",
                autoboto.TypeInfo(typing.List[LBCookieStickinessPolicy]),
            ),
            (
                "other_policies",
                "OtherPolicies",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The stickiness policies created using CreateAppCookieStickinessPolicy.
    app_cookie_stickiness_policies: typing.List["AppCookieStickinessPolicy"
                                               ] = dataclasses.field(
                                                   default_factory=list,
                                               )

    # The stickiness policies created using CreateLBCookieStickinessPolicy.
    lb_cookie_stickiness_policies: typing.List["LBCookieStickinessPolicy"
                                              ] = dataclasses.field(
                                                  default_factory=list,
                                              )

    # The policies other than the stickiness policies.
    other_policies: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class PolicyAttribute(autoboto.ShapeBase):
    """
    Information about a policy attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_name",
                "AttributeName",
                autoboto.TypeInfo(str),
            ),
            (
                "attribute_value",
                "AttributeValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the attribute.
    attribute_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value of the attribute.
    attribute_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PolicyAttributeDescription(autoboto.ShapeBase):
    """
    Information about a policy attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_name",
                "AttributeName",
                autoboto.TypeInfo(str),
            ),
            (
                "attribute_value",
                "AttributeValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the attribute.
    attribute_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value of the attribute.
    attribute_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PolicyAttributeTypeDescription(autoboto.ShapeBase):
    """
    Information about a policy attribute type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_name",
                "AttributeName",
                autoboto.TypeInfo(str),
            ),
            (
                "attribute_type",
                "AttributeType",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "default_value",
                "DefaultValue",
                autoboto.TypeInfo(str),
            ),
            (
                "cardinality",
                "Cardinality",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the attribute.
    attribute_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of the attribute. For example, `Boolean` or `Integer`.
    attribute_type: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the attribute.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The default value of the attribute, if applicable.
    default_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The cardinality of the attribute.

    # Valid values:

    #   * ONE(1) : Single value required

    #   * ZERO_OR_ONE(0..1) : Up to one value is allowed

    #   * ZERO_OR_MORE(0..*) : Optional. Multiple values are allowed

    #   * ONE_OR_MORE(1..*0) : Required. Multiple values are allowed
    cardinality: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PolicyDescription(autoboto.ShapeBase):
    """
    Information about a policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "PolicyName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_type_name",
                "PolicyTypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_attribute_descriptions",
                "PolicyAttributeDescriptions",
                autoboto.TypeInfo(typing.List[PolicyAttributeDescription]),
            ),
        ]

    # The name of the policy.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the policy type.
    policy_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The policy attributes.
    policy_attribute_descriptions: typing.List["PolicyAttributeDescription"
                                              ] = dataclasses.field(
                                                  default_factory=list,
                                              )


@dataclasses.dataclass
class PolicyNotFoundException(autoboto.ShapeBase):
    """
    One or more of the specified policies do not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PolicyTypeDescription(autoboto.ShapeBase):
    """
    Information about a policy type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_type_name",
                "PolicyTypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_attribute_type_descriptions",
                "PolicyAttributeTypeDescriptions",
                autoboto.TypeInfo(typing.List[PolicyAttributeTypeDescription]),
            ),
        ]

    # The name of the policy type.
    policy_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the policy type.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The description of the policy attributes associated with the policies
    # defined by Elastic Load Balancing.
    policy_attribute_type_descriptions: typing.List[
        "PolicyAttributeTypeDescription"
    ] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class PolicyTypeNotFoundException(autoboto.ShapeBase):
    """
    One or more of the specified policy types do not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RegisterEndPointsInput(autoboto.ShapeBase):
    """
    Contains the parameters for RegisterInstancesWithLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "instances",
                "Instances",
                autoboto.TypeInfo(typing.List[Instance]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IDs of the instances.
    instances: typing.List["Instance"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class RegisterEndPointsOutput(autoboto.ShapeBase):
    """
    Contains the output of RegisterInstancesWithLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instances",
                "Instances",
                autoboto.TypeInfo(typing.List[Instance]),
            ),
        ]

    # The updated list of instances for the load balancer.
    instances: typing.List["Instance"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class RemoveAvailabilityZonesInput(autoboto.ShapeBase):
    """
    Contains the parameters for DisableAvailabilityZonesForLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Availability Zones.
    availability_zones: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class RemoveAvailabilityZonesOutput(autoboto.ShapeBase):
    """
    Contains the output for DisableAvailabilityZonesForLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "availability_zones",
                "AvailabilityZones",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The remaining Availability Zones for the load balancer.
    availability_zones: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class RemoveTagsInput(autoboto.ShapeBase):
    """
    Contains the parameters for RemoveTags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_names",
                "LoadBalancerNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[TagKeyOnly]),
            ),
        ]

    # The name of the load balancer. You can specify a maximum of one load
    # balancer name.
    load_balancer_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The list of tag keys to remove.
    tags: typing.List["TagKeyOnly"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class RemoveTagsOutput(autoboto.ShapeBase):
    """
    Contains the output of RemoveTags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SetLoadBalancerListenerSSLCertificateInput(autoboto.ShapeBase):
    """
    Contains the parameters for SetLoadBalancerListenerSSLCertificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "load_balancer_port",
                "LoadBalancerPort",
                autoboto.TypeInfo(int),
            ),
            (
                "ssl_certificate_id",
                "SSLCertificateId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The port that uses the specified SSL certificate.
    load_balancer_port: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the SSL certificate.
    ssl_certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SetLoadBalancerListenerSSLCertificateOutput(autoboto.ShapeBase):
    """
    Contains the output of SetLoadBalancerListenerSSLCertificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SetLoadBalancerPoliciesForBackendServerInput(autoboto.ShapeBase):
    """
    Contains the parameters for SetLoadBalancerPoliciesForBackendServer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_port",
                "InstancePort",
                autoboto.TypeInfo(int),
            ),
            (
                "policy_names",
                "PolicyNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The port number associated with the EC2 instance.
    instance_port: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The names of the policies. If the list is empty, then all current polices
    # are removed from the EC2 instance.
    policy_names: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class SetLoadBalancerPoliciesForBackendServerOutput(autoboto.ShapeBase):
    """
    Contains the output of SetLoadBalancerPoliciesForBackendServer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SetLoadBalancerPoliciesOfListenerInput(autoboto.ShapeBase):
    """
    Contains the parameters for SetLoadBalancePoliciesOfListener.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "load_balancer_port",
                "LoadBalancerPort",
                autoboto.TypeInfo(int),
            ),
            (
                "policy_names",
                "PolicyNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The external port of the load balancer.
    load_balancer_port: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The names of the policies. This list must include all policies to be
    # enabled. If you omit a policy that is currently enabled, it is disabled. If
    # the list is empty, all current policies are disabled.
    policy_names: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class SetLoadBalancerPoliciesOfListenerOutput(autoboto.ShapeBase):
    """
    Contains the output of SetLoadBalancePoliciesOfListener.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SourceSecurityGroup(autoboto.ShapeBase):
    """
    Information about a source security group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "owner_alias",
                "OwnerAlias",
                autoboto.TypeInfo(str),
            ),
            (
                "group_name",
                "GroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The owner of the security group.
    owner_alias: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the security group.
    group_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SubnetNotFoundException(autoboto.ShapeBase):
    """
    One or more of the specified subnets do not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    """
    Information about a tag.
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
class TagDescription(autoboto.ShapeBase):
    """
    The tags associated with a load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The tags.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class TagKeyOnly(autoboto.ShapeBase):
    """
    The key of a tag.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the key.
    key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TooManyAccessPointsException(autoboto.ShapeBase):
    """
    The quota for the number of load balancers has been reached.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TooManyPoliciesException(autoboto.ShapeBase):
    """
    The quota for the number of policies for this load balancer has been reached.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TooManyTagsException(autoboto.ShapeBase):
    """
    The quota for the number of tags that can be assigned to a load balancer has
    been reached.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UnsupportedProtocolException(autoboto.ShapeBase):
    """
    The specified protocol or signature version is not supported.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []
