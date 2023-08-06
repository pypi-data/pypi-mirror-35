import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AccessDeniedForDependencyException(autoboto.ShapeBase):
    """
    In order to grant the necessary access to the DDoS Response Team, the user
    submitting `AssociateDRTRole` must have the `iam:PassRole` permission. This
    error indicates the user did not have the appropriate permissions. For more
    information, see [Granting a User Permissions to Pass a Role to an AWS
    Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html).
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
class AssociateDRTLogBucketRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_bucket",
                "LogBucket",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon S3 bucket that contains your flow logs.
    log_bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateDRTLogBucketResponse(autoboto.OutputShapeBase):
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
class AssociateDRTRoleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the role the DRT will use to access your
    # AWS account.

    # Prior to making the `AssociateDRTRole` request, you must attach the
    # [AWSShieldDRTAccessPolicy](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-
    # role/AWSShieldDRTAccessPolicy) managed policy to this role. For more
    # information see [Attaching and Detaching IAM Policies](
    # https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-
    # attach-detach.html).
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateDRTRoleResponse(autoboto.OutputShapeBase):
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
class AttackDetail(autoboto.ShapeBase):
    """
    The details of a DDoS attack.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attack_id",
                "AttackId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_arn",
                "ResourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "sub_resources",
                "SubResources",
                autoboto.TypeInfo(typing.List[SubResourceSummary]),
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
                "attack_counters",
                "AttackCounters",
                autoboto.TypeInfo(typing.List[SummarizedCounter]),
            ),
            (
                "attack_properties",
                "AttackProperties",
                autoboto.TypeInfo(typing.List[AttackProperty]),
            ),
            (
                "mitigations",
                "Mitigations",
                autoboto.TypeInfo(typing.List[Mitigation]),
            ),
        ]

    # The unique identifier (ID) of the attack.
    attack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN (Amazon Resource Name) of the resource that was attacked.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If applicable, additional detail about the resource being attacked, for
    # example, IP address or URL.
    sub_resources: typing.List["SubResourceSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The time the attack started, in Unix time in seconds. For more information
    # see [timestamp](http://docs.aws.amazon.com/cli/latest/userguide/cli-using-
    # param.html#parameter-types).
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the attack ended, in Unix time in seconds. For more information
    # see [timestamp](http://docs.aws.amazon.com/cli/latest/userguide/cli-using-
    # param.html#parameter-types).
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # List of counters that describe the attack for the specified time period.
    attack_counters: typing.List["SummarizedCounter"] = dataclasses.field(
        default_factory=list,
    )

    # The array of AttackProperty objects.
    attack_properties: typing.List["AttackProperty"] = dataclasses.field(
        default_factory=list,
    )

    # List of mitigation actions taken for the attack.
    mitigations: typing.List["Mitigation"] = dataclasses.field(
        default_factory=list,
    )


class AttackLayer(Enum):
    NETWORK = "NETWORK"
    APPLICATION = "APPLICATION"


@dataclasses.dataclass
class AttackProperty(autoboto.ShapeBase):
    """
    Details of the described attack.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attack_layer",
                "AttackLayer",
                autoboto.TypeInfo(AttackLayer),
            ),
            (
                "attack_property_identifier",
                "AttackPropertyIdentifier",
                autoboto.TypeInfo(AttackPropertyIdentifier),
            ),
            (
                "top_contributors",
                "TopContributors",
                autoboto.TypeInfo(typing.List[Contributor]),
            ),
            (
                "unit",
                "Unit",
                autoboto.TypeInfo(Unit),
            ),
            (
                "total",
                "Total",
                autoboto.TypeInfo(int),
            ),
        ]

    # The type of DDoS event that was observed. `NETWORK` indicates layer 3 and
    # layer 4 events and `APPLICATION` indicates layer 7 events.
    attack_layer: "AttackLayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Defines the DDoS attack property information that is provided.
    attack_property_identifier: "AttackPropertyIdentifier" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The array of Contributor objects that includes the top five contributors to
    # an attack.
    top_contributors: typing.List["Contributor"] = dataclasses.field(
        default_factory=list,
    )

    # The unit of the `Value` of the contributions.
    unit: "Unit" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total contributions made to this attack by all contributors, not just
    # the five listed in the `TopContributors` list.
    total: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class AttackPropertyIdentifier(Enum):
    DESTINATION_URL = "DESTINATION_URL"
    REFERRER = "REFERRER"
    SOURCE_ASN = "SOURCE_ASN"
    SOURCE_COUNTRY = "SOURCE_COUNTRY"
    SOURCE_IP_ADDRESS = "SOURCE_IP_ADDRESS"
    SOURCE_USER_AGENT = "SOURCE_USER_AGENT"


@dataclasses.dataclass
class AttackSummary(autoboto.ShapeBase):
    """
    Summarizes all DDoS attacks for a specified time period.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attack_id",
                "AttackId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_arn",
                "ResourceArn",
                autoboto.TypeInfo(str),
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
                "attack_vectors",
                "AttackVectors",
                autoboto.TypeInfo(typing.List[AttackVectorDescription]),
            ),
        ]

    # The unique identifier (ID) of the attack.
    attack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN (Amazon Resource Name) of the resource that was attacked.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The start time of the attack, in Unix time in seconds. For more information
    # see [timestamp](http://docs.aws.amazon.com/cli/latest/userguide/cli-using-
    # param.html#parameter-types).
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The end time of the attack, in Unix time in seconds. For more information
    # see [timestamp](http://docs.aws.amazon.com/cli/latest/userguide/cli-using-
    # param.html#parameter-types).
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The list of attacks for a specified time period.
    attack_vectors: typing.List["AttackVectorDescription"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AttackVectorDescription(autoboto.ShapeBase):
    """
    Describes the attack.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vector_type",
                "VectorType",
                autoboto.TypeInfo(str),
            ),
        ]

    # The attack type. Valid values:

    #   * UDP_TRAFFIC

    #   * UDP_FRAGMENT

    #   * GENERIC_UDP_REFLECTION

    #   * DNS_REFLECTION

    #   * NTP_REFLECTION

    #   * CHARGEN_REFLECTION

    #   * SSDP_REFLECTION

    #   * PORT_MAPPER

    #   * RIP_REFLECTION

    #   * SNMP_REFLECTION

    #   * MSSQL_REFLECTION

    #   * NET_BIOS_REFLECTION

    #   * SYN_FLOOD

    #   * ACK_FLOOD

    #   * REQUEST_FLOOD
    vector_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class AutoRenew(Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class Contributor(autoboto.ShapeBase):
    """
    A contributor to the attack and their contribution.
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
                "value",
                "Value",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the contributor. This is dependent on the
    # `AttackPropertyIdentifier`. For example, if the `AttackPropertyIdentifier`
    # is `SOURCE_COUNTRY`, the `Name` could be `United States`.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The contribution of this contributor expressed in Protection units. For
    # example `10,000`.
    value: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateProtectionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_arn",
                "ResourceArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # Friendly name for the `Protection` you are creating.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN (Amazon Resource Name) of the resource to be protected.

    # The ARN should be in one of the following formats:

    #   * For an Application Load Balancer: `arn:aws:elasticloadbalancing: _region_ : _account-id_ :loadbalancer/app/ _load-balancer-name_ / _load-balancer-id_ `

    #   * For an Elastic Load Balancer (Classic Load Balancer): `arn:aws:elasticloadbalancing: _region_ : _account-id_ :loadbalancer/ _load-balancer-name_ `

    #   * For AWS CloudFront distribution: `arn:aws:cloudfront:: _account-id_ :distribution/ _distribution-id_ `

    #   * For Amazon Route 53: `arn:aws:route53:: _account-id_ :hostedzone/ _hosted-zone-id_ `

    #   * For an Elastic IP address: `arn:aws:ec2: _region_ : _account-id_ :eip-allocation/ _allocation-id_ `
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateProtectionResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "protection_id",
                "ProtectionId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The unique identifier (ID) for the Protection object that is created.
    protection_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSubscriptionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateSubscriptionResponse(autoboto.OutputShapeBase):
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
class DeleteProtectionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "protection_id",
                "ProtectionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) for the Protection object to be deleted.
    protection_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProtectionResponse(autoboto.OutputShapeBase):
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
class DeleteSubscriptionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteSubscriptionResponse(autoboto.OutputShapeBase):
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
class DescribeAttackRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attack_id",
                "AttackId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) for the attack that to be described.
    attack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAttackResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attack",
                "Attack",
                autoboto.TypeInfo(AttackDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The attack that is described.
    attack: "AttackDetail" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeDRTAccessRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeDRTAccessResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "log_bucket_list",
                "LogBucketList",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the role the DRT used to access your AWS
    # account.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of Amazon S3 buckets accessed by the DRT.
    log_bucket_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeEmergencyContactSettingsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeEmergencyContactSettingsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "emergency_contact_list",
                "EmergencyContactList",
                autoboto.TypeInfo(typing.List[EmergencyContact]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of email addresses that the DRT can use to contact you during a
    # suspected attack.
    emergency_contact_list: typing.List["EmergencyContact"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeProtectionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "protection_id",
                "ProtectionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) for the Protection object that is described.
    protection_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProtectionResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "protection",
                "Protection",
                autoboto.TypeInfo(Protection),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Protection object that is described.
    protection: "Protection" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeSubscriptionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeSubscriptionResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "subscription",
                "Subscription",
                autoboto.TypeInfo(Subscription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS Shield Advanced subscription details for an account.
    subscription: "Subscription" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DisassociateDRTLogBucketRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_bucket",
                "LogBucket",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon S3 bucket that contains your flow logs.
    log_bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateDRTLogBucketResponse(autoboto.OutputShapeBase):
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
class DisassociateDRTRoleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DisassociateDRTRoleResponse(autoboto.OutputShapeBase):
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
class EmergencyContact(autoboto.ShapeBase):
    """
    Contact information that the DRT can use to contact you during a suspected
    attack.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "email_address",
                "EmailAddress",
                autoboto.TypeInfo(str),
            ),
        ]

    # An email address that the DRT can use to contact you during a suspected
    # attack.
    email_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSubscriptionStateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetSubscriptionStateResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "subscription_state",
                "SubscriptionState",
                autoboto.TypeInfo(SubscriptionState),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the subscription.
    subscription_state: "SubscriptionState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalErrorException(autoboto.ShapeBase):
    """
    Exception that indicates that a problem occurred with the service
    infrastructure. You can retry the request.
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
class InvalidOperationException(autoboto.ShapeBase):
    """
    Exception that indicates that the operation would not cause any change to occur.
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
class InvalidPaginationTokenException(autoboto.ShapeBase):
    """
    Exception that indicates that the NextToken specified in the request is invalid.
    Submit the request using the NextToken value that was returned in the response.
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
class InvalidParameterException(autoboto.ShapeBase):
    """
    Exception that indicates that the parameters passed to the API are invalid.
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
class InvalidResourceException(autoboto.ShapeBase):
    """
    Exception that indicates that the resource is invalid. You might not have access
    to the resource, or the resource might not exist.
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
class Limit(autoboto.ShapeBase):
    """
    Specifies how many protections of a given type you can create.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
            (
                "max",
                "Max",
                autoboto.TypeInfo(int),
            ),
        ]

    # The type of protection.
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of protections that can be created for the specified
    # `Type`.
    max: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitsExceededException(autoboto.ShapeBase):
    """
    Exception that indicates that the operation would exceed a limit.

    `Type` is the type of limit that would be exceeded.

    `Limit` is the threshold that would be exceeded.
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
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAttacksRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arns",
                "ResourceArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "start_time",
                "StartTime",
                autoboto.TypeInfo(TimeRange),
            ),
            (
                "end_time",
                "EndTime",
                autoboto.TypeInfo(TimeRange),
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

    # The ARN (Amazon Resource Name) of the resource that was attacked. If this
    # is left blank, all applicable resources for this account will be included.
    resource_arns: typing.List[str] = dataclasses.field(default_factory=list, )

    # The start of the time period for the attacks. This is a `timestamp` type.
    # The sample request above indicates a `number` type because the default used
    # by WAF is Unix time in seconds. However any valid [timestamp
    # format](http://docs.aws.amazon.com/cli/latest/userguide/cli-using-
    # param.html#parameter-types) is allowed.
    start_time: "TimeRange" = dataclasses.field(default_factory=dict, )

    # The end of the time period for the attacks. This is a `timestamp` type. The
    # sample request above indicates a `number` type because the default used by
    # WAF is Unix time in seconds. However any valid [timestamp
    # format](http://docs.aws.amazon.com/cli/latest/userguide/cli-using-
    # param.html#parameter-types) is allowed.
    end_time: "TimeRange" = dataclasses.field(default_factory=dict, )

    # The `ListAttacksRequest.NextMarker` value from a previous call to
    # `ListAttacksRequest`. Pass null if this is the first call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of AttackSummary objects to be returned. If this is left
    # blank, the first 20 results will be returned.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAttacksResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attack_summaries",
                "AttackSummaries",
                autoboto.TypeInfo(typing.List[AttackSummary]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The attack information for the specified time range.
    attack_summaries: typing.List["AttackSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The token returned by a previous call to indicate that there is more data
    # available. If not null, more results are available. Pass this value for the
    # `NextMarker` parameter in a subsequent call to `ListAttacks` to retrieve
    # the next set of items.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListProtectionsRequest(autoboto.ShapeBase):
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
        ]

    # The `ListProtectionsRequest.NextToken` value from a previous call to
    # `ListProtections`. Pass null if this is the first call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of Protection objects to be returned. If this is left
    # blank the first 20 results will be returned.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListProtectionsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "protections",
                "Protections",
                autoboto.TypeInfo(typing.List[Protection]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The array of enabled Protection objects.
    protections: typing.List["Protection"] = dataclasses.field(
        default_factory=list,
    )

    # If you specify a value for `MaxResults` and you have more Protections than
    # the value of MaxResults, AWS Shield Advanced returns a NextToken value in
    # the response that allows you to list another group of Protections. For the
    # second and subsequent ListProtections requests, specify the value of
    # NextToken from the previous response to get information about another batch
    # of Protections.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LockedSubscriptionException(autoboto.ShapeBase):
    """
    You are trying to update a subscription that has not yet completed the 1-year
    commitment. You can change the `AutoRenew` parameter during the last 30 days of
    your subscription. This exception indicates that you are attempting to change
    `AutoRenew` prior to that period.
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
class Mitigation(autoboto.ShapeBase):
    """
    The mitigation applied to a DDoS attack.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "mitigation_name",
                "MitigationName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the mitigation taken for this attack.
    mitigation_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NoAssociatedRoleException(autoboto.ShapeBase):
    """
    The ARN of the role that you specifed does not exist.
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
class OptimisticLockException(autoboto.ShapeBase):
    """
    Exception that indicates that the protection state has been modified by another
    client. You can retry the request.
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
class Protection(autoboto.ShapeBase):
    """
    An object that represents a resource that is under DDoS protection.
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
                "resource_arn",
                "ResourceArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier (ID) of the protection.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The friendly name of the protection. For example, `My CloudFront
    # distributions`.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN (Amazon Resource Name) of the AWS resource that is protected.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceAlreadyExistsException(autoboto.ShapeBase):
    """
    Exception indicating the specified resource already exists.
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
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    Exception indicating the specified resource does not exist.
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
class SubResourceSummary(autoboto.ShapeBase):
    """
    The attack information for the specified SubResource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(SubResourceType),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "attack_vectors",
                "AttackVectors",
                autoboto.TypeInfo(typing.List[SummarizedAttackVector]),
            ),
            (
                "counters",
                "Counters",
                autoboto.TypeInfo(typing.List[SummarizedCounter]),
            ),
        ]

    # The `SubResource` type.
    type: "SubResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The unique identifier (ID) of the `SubResource`.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of attack types and associated counters.
    attack_vectors: typing.List["SummarizedAttackVector"] = dataclasses.field(
        default_factory=list,
    )

    # The counters that describe the details of the attack.
    counters: typing.List["SummarizedCounter"] = dataclasses.field(
        default_factory=list,
    )


class SubResourceType(Enum):
    IP = "IP"
    URL = "URL"


@dataclasses.dataclass
class Subscription(autoboto.ShapeBase):
    """
    Information about the AWS Shield Advanced subscription for an account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "time_commitment_in_seconds",
                "TimeCommitmentInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "auto_renew",
                "AutoRenew",
                autoboto.TypeInfo(AutoRenew),
            ),
            (
                "limits",
                "Limits",
                autoboto.TypeInfo(typing.List[Limit]),
            ),
        ]

    # The start time of the subscription, in Unix time in seconds. For more
    # information see
    # [timestamp](http://docs.aws.amazon.com/cli/latest/userguide/cli-using-
    # param.html#parameter-types).
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time your subscription will end.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The length, in seconds, of the AWS Shield Advanced subscription for the
    # account.
    time_commitment_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If `ENABLED`, the subscription will be automatically renewed at the end of
    # the existing subscription period.

    # When you initally create a subscription, `AutoRenew` is set to `ENABLED`.
    # You can change this by submitting an `UpdateSubscription` request. If the
    # `UpdateSubscription` request does not included a value for `AutoRenew`, the
    # existing value for `AutoRenew` remains unchanged.
    auto_renew: "AutoRenew" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies how many protections of a given type you can create.
    limits: typing.List["Limit"] = dataclasses.field(default_factory=list, )


class SubscriptionState(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


@dataclasses.dataclass
class SummarizedAttackVector(autoboto.ShapeBase):
    """
    A summary of information about the attack.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vector_type",
                "VectorType",
                autoboto.TypeInfo(str),
            ),
            (
                "vector_counters",
                "VectorCounters",
                autoboto.TypeInfo(typing.List[SummarizedCounter]),
            ),
        ]

    # The attack type, for example, SNMP reflection or SYN flood.
    vector_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of counters that describe the details of the attack.
    vector_counters: typing.List["SummarizedCounter"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class SummarizedCounter(autoboto.ShapeBase):
    """
    The counter that describes a DDoS attack.
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
                autoboto.TypeInfo(float),
            ),
            (
                "average",
                "Average",
                autoboto.TypeInfo(float),
            ),
            (
                "sum",
                "Sum",
                autoboto.TypeInfo(float),
            ),
            (
                "n",
                "N",
                autoboto.TypeInfo(int),
            ),
            (
                "unit",
                "Unit",
                autoboto.TypeInfo(str),
            ),
        ]

    # The counter name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum value of the counter for a specified time period.
    max: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The average value of the counter for a specified time period.
    average: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total of counter values for a specified time period.
    sum: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of counters for a specified time period.
    n: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The unit of the counters.
    unit: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TimeRange(autoboto.ShapeBase):
    """
    The time range.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "from_inclusive",
                "FromInclusive",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "to_exclusive",
                "ToExclusive",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The start time, in Unix time in seconds. For more information see
    # [timestamp](http://docs.aws.amazon.com/cli/latest/userguide/cli-using-
    # param.html#parameter-types).
    from_inclusive: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The end time, in Unix time in seconds. For more information see
    # [timestamp](http://docs.aws.amazon.com/cli/latest/userguide/cli-using-
    # param.html#parameter-types).
    to_exclusive: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class Unit(Enum):
    BITS = "BITS"
    BYTES = "BYTES"
    PACKETS = "PACKETS"
    REQUESTS = "REQUESTS"


@dataclasses.dataclass
class UpdateEmergencyContactSettingsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "emergency_contact_list",
                "EmergencyContactList",
                autoboto.TypeInfo(typing.List[EmergencyContact]),
            ),
        ]

    # A list of email addresses that the DRT can use to contact you during a
    # suspected attack.
    emergency_contact_list: typing.List["EmergencyContact"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateEmergencyContactSettingsResponse(autoboto.OutputShapeBase):
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
class UpdateSubscriptionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_renew",
                "AutoRenew",
                autoboto.TypeInfo(AutoRenew),
            ),
        ]

    # When you initally create a subscription, `AutoRenew` is set to `ENABLED`.
    # If `ENABLED`, the subscription will be automatically renewed at the end of
    # the existing subscription period. You can change this by submitting an
    # `UpdateSubscription` request. If the `UpdateSubscription` request does not
    # included a value for `AutoRenew`, the existing value for `AutoRenew`
    # remains unchanged.
    auto_renew: "AutoRenew" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateSubscriptionResponse(autoboto.OutputShapeBase):
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
