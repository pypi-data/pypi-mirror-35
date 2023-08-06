import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class CreateLifecyclePolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution_role_arn",
                "ExecutionRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(SettablePolicyStateValues),
            ),
            (
                "policy_details",
                "PolicyDetails",
                autoboto.TypeInfo(PolicyDetails),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM role used to run the operations
    # specified by the lifecycle policy.
    execution_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A description of the lifecycle policy. The characters ^[0-9A-Za-z _-]+$ are
    # supported.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The desired activation state of the lifecycle policy after creation.
    state: "SettablePolicyStateValues" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The configuration details of the lifecycle policy.

    # Target tags cannot be re-used across lifecycle policies.
    policy_details: "PolicyDetails" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateLifecyclePolicyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier of the lifecycle policy.
    policy_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateRule(autoboto.ShapeBase):
    """
    Specifies when to create snapshots of EBS volumes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "interval",
                "Interval",
                autoboto.TypeInfo(int),
            ),
            (
                "interval_unit",
                "IntervalUnit",
                autoboto.TypeInfo(IntervalUnitValues),
            ),
            (
                "times",
                "Times",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The interval. The supported values are 12 and 24.
    interval: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The interval unit.
    interval_unit: "IntervalUnitValues" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time, in UTC, to start the operation.

    # The operation occurs within a one-hour window following the specified time.
    times: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DeleteLifecyclePolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier of the lifecycle policy.
    policy_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLifecyclePolicyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetLifecyclePoliciesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_ids",
                "PolicyIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(GettablePolicyStateValues),
            ),
            (
                "resource_types",
                "ResourceTypes",
                autoboto.TypeInfo(typing.List[ResourceTypeValues]),
            ),
            (
                "target_tags",
                "TargetTags",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "tags_to_add",
                "TagsToAdd",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The identifiers of the data lifecycle policies.
    policy_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The activation state.
    state: "GettablePolicyStateValues" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The resource type.
    resource_types: typing.List["ResourceTypeValues"] = dataclasses.field(
        default_factory=list,
    )

    # The target tag for a policy.

    # Tags are strings in the format `key=value`.
    target_tags: typing.List[str] = dataclasses.field(default_factory=list, )

    # The tags to add to objects created by the policy.

    # Tags are strings in the format `key=value`.

    # These user-defined tags are added in addition to the AWS-added lifecycle
    # tags.
    tags_to_add: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class GetLifecyclePoliciesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policies",
                "Policies",
                autoboto.TypeInfo(typing.List[LifecyclePolicySummary]),
            ),
        ]

    # Summary information about the lifecycle policies.
    policies: typing.List["LifecyclePolicySummary"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetLifecyclePolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier of the lifecycle policy.
    policy_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLifecyclePolicyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy",
                "Policy",
                autoboto.TypeInfo(LifecyclePolicy),
            ),
        ]

    # Detailed information about the lifecycle policy.
    policy: "LifecyclePolicy" = dataclasses.field(default_factory=dict, )


class GettablePolicyStateValues(Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    ERROR = "ERROR"


@dataclasses.dataclass
class InternalServerException(autoboto.ShapeBase):
    """
    The service failed in an unexpected way.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "code",
                "Code",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class IntervalUnitValues(Enum):
    HOURS = "HOURS"


@dataclasses.dataclass
class InvalidRequestException(autoboto.ShapeBase):
    """
    Bad request. The request is missing required parameters or has invalid
    parameters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "code",
                "Code",
                autoboto.TypeInfo(str),
            ),
            (
                "required_parameters",
                "RequiredParameters",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "mutually_exclusive_parameters",
                "MutuallyExclusiveParameters",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The request omitted one or more required parameters.
    required_parameters: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The request included parameters that cannot be provided together.
    mutually_exclusive_parameters: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class LifecyclePolicy(autoboto.ShapeBase):
    """
    Detailed information about a lifecycle policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(GettablePolicyStateValues),
            ),
            (
                "execution_role_arn",
                "ExecutionRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "date_created",
                "DateCreated",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "date_modified",
                "DateModified",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "policy_details",
                "PolicyDetails",
                autoboto.TypeInfo(PolicyDetails),
            ),
        ]

    # The identifier of the lifecycle policy.
    policy_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the lifecycle policy.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The activation state of the lifecycle policy.
    state: "GettablePolicyStateValues" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the IAM role used to run the operations
    # specified by the lifecycle policy.
    execution_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The local date and time when the lifecycle policy was created.
    date_created: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The local date and time when the lifecycle policy was last modified.
    date_modified: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The configuration of the lifecycle policy
    policy_details: "PolicyDetails" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class LifecyclePolicySummary(autoboto.ShapeBase):
    """
    Summary information about a lifecycle policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(GettablePolicyStateValues),
            ),
        ]

    # The identifier of the lifecycle policy.
    policy_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the lifecycle policy.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The activation state of the lifecycle policy.
    state: "GettablePolicyStateValues" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    The request failed because a limit was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "code",
                "Code",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Value is the type of resource for which a limit was exceeded.
    resource_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PolicyDetails(autoboto.ShapeBase):
    """
    Specifies the configuration of a lifecycle policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_types",
                "ResourceTypes",
                autoboto.TypeInfo(typing.List[ResourceTypeValues]),
            ),
            (
                "target_tags",
                "TargetTags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "schedules",
                "Schedules",
                autoboto.TypeInfo(typing.List[Schedule]),
            ),
        ]

    # The resource type.
    resource_types: typing.List["ResourceTypeValues"] = dataclasses.field(
        default_factory=list,
    )

    # The single tag that identifies targeted resources for this policy.
    target_tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # The schedule of policy-defined actions.
    schedules: typing.List["Schedule"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    A requested resource was not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "code",
                "Code",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_ids",
                "ResourceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Value is the type of resource that was not found.
    resource_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Value is a list of resource IDs that were not found.
    resource_ids: typing.List[str] = dataclasses.field(default_factory=list, )


class ResourceTypeValues(Enum):
    VOLUME = "VOLUME"


@dataclasses.dataclass
class RetainRule(autoboto.ShapeBase):
    """
    Specifies the number of snapshots to keep for each EBS volume.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "count",
                "Count",
                autoboto.TypeInfo(int),
            ),
        ]

    # The number of snapshots to keep for each volume, up to a maximum of 1000.
    count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Schedule(autoboto.ShapeBase):
    """
    Specifies a schedule.
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
                "tags_to_add",
                "TagsToAdd",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "create_rule",
                "CreateRule",
                autoboto.TypeInfo(CreateRule),
            ),
            (
                "retain_rule",
                "RetainRule",
                autoboto.TypeInfo(RetainRule),
            ),
        ]

    # The name of the schedule.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tags to apply to policy-created resources. These user-defined tags are
    # in addition to the AWS-added lifecycle tags.
    tags_to_add: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # The create rule.
    create_rule: "CreateRule" = dataclasses.field(default_factory=dict, )

    # The retain rule.
    retain_rule: "RetainRule" = dataclasses.field(default_factory=dict, )


class SettablePolicyStateValues(Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    """
    Specifies a tag for a resource.
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

    # The tag key.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tag value.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateLifecyclePolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_role_arn",
                "ExecutionRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(SettablePolicyStateValues),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_details",
                "PolicyDetails",
                autoboto.TypeInfo(PolicyDetails),
            ),
        ]

    # The identifier of the lifecycle policy.
    policy_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role used to run the operations
    # specified by the lifecycle policy.
    execution_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The desired activation state of the lifecycle policy after creation.
    state: "SettablePolicyStateValues" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A description of the lifecycle policy.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The configuration of the lifecycle policy.

    # Target tags cannot be re-used across policies.
    policy_details: "PolicyDetails" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateLifecyclePolicyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []
