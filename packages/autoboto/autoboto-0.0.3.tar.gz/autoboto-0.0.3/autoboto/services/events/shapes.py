import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class BatchArrayProperties(autoboto.ShapeBase):
    """
    The array properties for the submitted job, such as the size of the array. The
    array size can be between 2 and 10,000. If you specify array properties for a
    job, it becomes an array job. This parameter is used only if the target is an
    AWS Batch job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "size",
                "Size",
                autoboto.TypeInfo(int),
            ),
        ]

    # The size of the array, if this is an array batch job. Valid values are
    # integers between 2 and 10,000.
    size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BatchParameters(autoboto.ShapeBase):
    """
    The custom parameters to be used when the target is an AWS Batch job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_definition",
                "JobDefinition",
                autoboto.TypeInfo(str),
            ),
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
            (
                "array_properties",
                "ArrayProperties",
                autoboto.TypeInfo(BatchArrayProperties),
            ),
            (
                "retry_strategy",
                "RetryStrategy",
                autoboto.TypeInfo(BatchRetryStrategy),
            ),
        ]

    # The ARN or name of the job definition to use if the event target is an AWS
    # Batch job. This job definition must already exist.
    job_definition: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name to use for this execution of the job, if the target is an AWS
    # Batch job.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The array properties for the submitted job, such as the size of the array.
    # The array size can be between 2 and 10,000. If you specify array properties
    # for a job, it becomes an array job. This parameter is used only if the
    # target is an AWS Batch job.
    array_properties: "BatchArrayProperties" = dataclasses.field(
        default_factory=dict,
    )

    # The retry strategy to use for failed jobs, if the target is an AWS Batch
    # job. The retry strategy is the number of times to retry the failed job
    # execution. Valid values are 1 to 10. When you specify a retry strategy
    # here, it overrides the retry strategy defined in the job definition.
    retry_strategy: "BatchRetryStrategy" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class BatchRetryStrategy(autoboto.ShapeBase):
    """
    The retry strategy to use for failed jobs, if the target is an AWS Batch job. If
    you specify a retry strategy here, it overrides the retry strategy defined in
    the job definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attempts",
                "Attempts",
                autoboto.TypeInfo(int),
            ),
        ]

    # The number of times to attempt to retry, if the job fails. Valid values are
    # 1 to 10.
    attempts: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ConcurrentModificationException(autoboto.ShapeBase):
    """
    There is concurrent modification on a rule or target.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteRuleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the rule.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeEventBusRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeEventBusResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "policy",
                "Policy",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the event bus. Currently, this is always `default`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Resource Name (ARN) of the account permitted to write events to
    # the current account.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The policy that enables the external account to send events to your
    # account.
    policy: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeRuleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the rule.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeRuleResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "event_pattern",
                "EventPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(RuleState),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the rule.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Resource Name (ARN) of the rule.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The event pattern. For more information, see [Events and Event
    # Patterns](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html)
    # in the _Amazon CloudWatch Events User Guide_.
    event_pattern: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The scheduling expression. For example, "cron(0 20 * * ? *)", "rate(5
    # minutes)".
    schedule_expression: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether the rule is enabled or disabled.
    state: "RuleState" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The description of the rule.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role associated with the rule.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DisableRuleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the rule.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EcsParameters(autoboto.ShapeBase):
    """
    The custom parameters to be used when the target is an Amazon ECS cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_definition_arn",
                "TaskDefinitionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "task_count",
                "TaskCount",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ARN of the task definition to use if the event target is an Amazon ECS
    # cluster.
    task_definition_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of tasks to create based on the `TaskDefinition`. The default is
    # one.
    task_count: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EnableRuleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the rule.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InputTransformer(autoboto.ShapeBase):
    """
    Contains the parameters needed for you to provide custom input to a target based
    on one or more pieces of data extracted from the event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_template",
                "InputTemplate",
                autoboto.TypeInfo(str),
            ),
            (
                "input_paths_map",
                "InputPathsMap",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Input template where you can use the values of the keys from
    # `InputPathsMap` to customize the data sent to the target.
    input_template: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Map of JSON paths to be extracted from the event. These are key-value
    # pairs, where each value is a JSON path. You must use JSON dot notation, not
    # bracket notation.
    input_paths_map: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class InternalException(autoboto.ShapeBase):
    """
    This exception occurs due to unexpected causes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidEventPatternException(autoboto.ShapeBase):
    """
    The event pattern is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class KinesisParameters(autoboto.ShapeBase):
    """
    This object enables you to specify a JSON path to extract from the event and use
    as the partition key for the Amazon Kinesis stream, so that you can control the
    shard to which the event goes. If you do not include this parameter, the default
    is to use the `eventId` as the partition key.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "partition_key_path",
                "PartitionKeyPath",
                autoboto.TypeInfo(str),
            ),
        ]

    # The JSON path to be extracted from the event and used as the partition key.
    # For more information, see [Amazon Kinesis Streams Key
    # Concepts](http://docs.aws.amazon.com/streams/latest/dev/key-
    # concepts.html#partition-key) in the _Amazon Kinesis Streams Developer
    # Guide_.
    partition_key_path: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    You tried to create more rules or add more targets to a rule than is allowed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListRuleNamesByTargetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_arn",
                "TargetArn",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the target resource.
    target_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token returned by a previous call to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListRuleNamesByTargetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_names",
                "RuleNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The names of the rules that can invoke the given target.
    rule_names: typing.List[str] = dataclasses.field(default_factory=list, )

    # Indicates whether there are additional results to retrieve. If there are no
    # more results, the value is null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListRulesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name_prefix",
                "NamePrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # The prefix matching the rule name.
    name_prefix: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token returned by a previous call to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListRulesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rules",
                "Rules",
                autoboto.TypeInfo(typing.List[Rule]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The rules that match the specified criteria.
    rules: typing.List["Rule"] = dataclasses.field(default_factory=list, )

    # Indicates whether there are additional results to retrieve. If there are no
    # more results, the value is null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListTargetsByRuleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule",
                "Rule",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the rule.
    rule: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token returned by a previous call to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListTargetsByRuleResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The targets assigned to the rule.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # Indicates whether there are additional results to retrieve. If there are no
    # more results, the value is null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PolicyLengthExceededException(autoboto.ShapeBase):
    """
    The event bus policy is too long. For more information, see the limits.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PutEventsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "entries",
                "Entries",
                autoboto.TypeInfo(typing.List[PutEventsRequestEntry]),
            ),
        ]

    # The entry that defines an event in your system. You can specify several
    # parameters for the entry such as the source and type of the event,
    # resources associated with the event, and so on.
    entries: typing.List["PutEventsRequestEntry"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class PutEventsRequestEntry(autoboto.ShapeBase):
    """
    Represents an event to be submitted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "time",
                "Time",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "source",
                "Source",
                autoboto.TypeInfo(str),
            ),
            (
                "resources",
                "Resources",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "detail_type",
                "DetailType",
                autoboto.TypeInfo(str),
            ),
            (
                "detail",
                "Detail",
                autoboto.TypeInfo(str),
            ),
        ]

    # The timestamp of the event, per [RFC3339](https://www.rfc-
    # editor.org/rfc/rfc3339.txt). If no timestamp is provided, the timestamp of
    # the PutEvents call is used.
    time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The source of the event.
    source: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # AWS resources, identified by Amazon Resource Name (ARN), which the event
    # primarily concerns. Any number, including zero, may be present.
    resources: typing.List[str] = dataclasses.field(default_factory=list, )

    # Free-form string used to decide what fields to expect in the event detail.
    detail_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A valid JSON string. There is no other schema imposed. The JSON string may
    # contain fields and nested subobjects.
    detail: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PutEventsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failed_entry_count",
                "FailedEntryCount",
                autoboto.TypeInfo(int),
            ),
            (
                "entries",
                "Entries",
                autoboto.TypeInfo(typing.List[PutEventsResultEntry]),
            ),
        ]

    # The number of failed entries.
    failed_entry_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The successfully and unsuccessfully ingested events results. If the
    # ingestion was successful, the entry has the event ID in it. Otherwise, you
    # can use the error code and error message to identify the problem with the
    # entry.
    entries: typing.List["PutEventsResultEntry"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class PutEventsResultEntry(autoboto.ShapeBase):
    """
    Represents an event that failed to be submitted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_id",
                "EventId",
                autoboto.TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the event.
    event_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The error code that indicates why the event submission failed.
    error_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The error message that explains why the event submission failed.
    error_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PutPermissionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(str),
            ),
            (
                "principal",
                "Principal",
                autoboto.TypeInfo(str),
            ),
            (
                "statement_id",
                "StatementId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The action that you are enabling the other account to perform. Currently,
    # this must be `events:PutEvents`.
    action: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The 12-digit AWS account ID that you are permitting to put events to your
    # default event bus. Specify "*" to permit any account to put events to your
    # default event bus.

    # If you specify "*", avoid creating rules that may match undesirable events.
    # To create more secure rules, make sure that the event pattern for each rule
    # contains an `account` field with a specific account ID from which to
    # receive events. Rules with an account field do not match any events sent
    # from other accounts.
    principal: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An identifier string for the external account that you are granting
    # permissions to. If you later want to revoke the permission for this
    # external account, specify this `StatementId` when you run RemovePermission.
    statement_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PutRuleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                autoboto.TypeInfo(str),
            ),
            (
                "event_pattern",
                "EventPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(RuleState),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the rule that you are creating or updating.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The scheduling expression. For example, "cron(0 20 * * ? *)" or "rate(5
    # minutes)".
    schedule_expression: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The event pattern. For more information, see [Events and Event
    # Patterns](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html)
    # in the _Amazon CloudWatch Events User Guide_.
    event_pattern: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates whether the rule is enabled or disabled.
    state: "RuleState" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the rule.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role associated with the rule.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PutRuleResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_arn",
                "RuleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the rule.
    rule_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PutTargetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule",
                "Rule",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
        ]

    # The name of the rule.
    rule: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The targets to update or add to the rule.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class PutTargetsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failed_entry_count",
                "FailedEntryCount",
                autoboto.TypeInfo(int),
            ),
            (
                "failed_entries",
                "FailedEntries",
                autoboto.TypeInfo(typing.List[PutTargetsResultEntry]),
            ),
        ]

    # The number of failed entries.
    failed_entry_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The failed target entries.
    failed_entries: typing.List["PutTargetsResultEntry"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class PutTargetsResultEntry(autoboto.ShapeBase):
    """
    Represents a target that failed to be added to a rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_id",
                "TargetId",
                autoboto.TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the target.
    target_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The error code that indicates why the target addition failed. If the value
    # is `ConcurrentModificationException`, too many requests were made at the
    # same time.
    error_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The error message that explains why the target addition failed.
    error_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RemovePermissionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "statement_id",
                "StatementId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The statement ID corresponding to the account that is no longer allowed to
    # put events to the default event bus.
    statement_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RemoveTargetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule",
                "Rule",
                autoboto.TypeInfo(str),
            ),
            (
                "ids",
                "Ids",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the rule.
    rule: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The IDs of the targets to remove from the rule.
    ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class RemoveTargetsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failed_entry_count",
                "FailedEntryCount",
                autoboto.TypeInfo(int),
            ),
            (
                "failed_entries",
                "FailedEntries",
                autoboto.TypeInfo(typing.List[RemoveTargetsResultEntry]),
            ),
        ]

    # The number of failed entries.
    failed_entry_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The failed target entries.
    failed_entries: typing.List["RemoveTargetsResultEntry"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class RemoveTargetsResultEntry(autoboto.ShapeBase):
    """
    Represents a target that failed to be removed from a rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_id",
                "TargetId",
                autoboto.TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the target.
    target_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The error code that indicates why the target removal failed. If the value
    # is `ConcurrentModificationException`, too many requests were made at the
    # same time.
    error_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The error message that explains why the target removal failed.
    error_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    An entity that you specified does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Rule(autoboto.ShapeBase):
    """
    Contains information about a rule in Amazon CloudWatch Events.
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
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "event_pattern",
                "EventPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(RuleState),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the rule.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Resource Name (ARN) of the rule.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The event pattern of the rule. For more information, see [Events and Event
    # Patterns](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html)
    # in the _Amazon CloudWatch Events User Guide_.
    event_pattern: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The state of the rule.
    state: "RuleState" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The description of the rule.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The scheduling expression. For example, "cron(0 20 * * ? *)", "rate(5
    # minutes)".
    schedule_expression: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the role that is used for target
    # invocation.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class RuleState(Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class RunCommandParameters(autoboto.ShapeBase):
    """
    This parameter contains the criteria (either InstanceIds or a tag) used to
    specify which EC2 instances are to be sent the command.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "run_command_targets",
                "RunCommandTargets",
                autoboto.TypeInfo(typing.List[RunCommandTarget]),
            ),
        ]

    # Currently, we support including only one RunCommandTarget block, which
    # specifies either an array of InstanceIds or a tag.
    run_command_targets: typing.List["RunCommandTarget"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class RunCommandTarget(autoboto.ShapeBase):
    """
    Information about the EC2 instances that are to be sent the command, specified
    as key-value pairs. Each `RunCommandTarget` block can include only one key, but
    this key may specify multiple values.
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
                "values",
                "Values",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # Can be either `tag:` _tag-key_ or `InstanceIds`.
    key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If `Key` is `tag:` _tag-key_ , `Values` is a list of tag values. If `Key`
    # is `InstanceIds`, `Values` is a list of Amazon EC2 instance IDs.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class SqsParameters(autoboto.ShapeBase):
    """
    This structure includes the custom parameter to be used when the target is an
    SQS FIFO queue.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message_group_id",
                "MessageGroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The FIFO message group ID to use as the target.
    message_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Target(autoboto.ShapeBase):
    """
    Targets are the resources to be invoked when a rule is triggered. Target types
    include EC2 instances, AWS Lambda functions, Amazon Kinesis streams, Amazon ECS
    tasks, AWS Step Functions state machines, Run Command, and built-in targets.
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
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "input",
                "Input",
                autoboto.TypeInfo(str),
            ),
            (
                "input_path",
                "InputPath",
                autoboto.TypeInfo(str),
            ),
            (
                "input_transformer",
                "InputTransformer",
                autoboto.TypeInfo(InputTransformer),
            ),
            (
                "kinesis_parameters",
                "KinesisParameters",
                autoboto.TypeInfo(KinesisParameters),
            ),
            (
                "run_command_parameters",
                "RunCommandParameters",
                autoboto.TypeInfo(RunCommandParameters),
            ),
            (
                "ecs_parameters",
                "EcsParameters",
                autoboto.TypeInfo(EcsParameters),
            ),
            (
                "batch_parameters",
                "BatchParameters",
                autoboto.TypeInfo(BatchParameters),
            ),
            (
                "sqs_parameters",
                "SqsParameters",
                autoboto.TypeInfo(SqsParameters),
            ),
        ]

    # The ID of the target.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Resource Name (ARN) of the target.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role to be used for this target
    # when the rule is triggered. If one rule triggers multiple targets, you can
    # use a different IAM role for each target.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Valid JSON text passed to the target. In this case, nothing from the event
    # itself is passed to the target. For more information, see [The JavaScript
    # Object Notation (JSON) Data Interchange Format](http://www.rfc-
    # editor.org/rfc/rfc7159.txt).
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value of the JSONPath that is used for extracting part of the matched
    # event when passing it to the target. You must use JSON dot notation, not
    # bracket notation. For more information about JSON paths, see
    # [JSONPath](http://goessner.net/articles/JsonPath/).
    input_path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Settings to enable you to provide custom input to a target based on certain
    # event data. You can extract one or more key-value pairs from the event and
    # then use that data to send customized input to the target.
    input_transformer: "InputTransformer" = dataclasses.field(
        default_factory=dict,
    )

    # The custom parameter you can use to control shard assignment, when the
    # target is an Amazon Kinesis stream. If you do not include this parameter,
    # the default is to use the `eventId` as the partition key.
    kinesis_parameters: "KinesisParameters" = dataclasses.field(
        default_factory=dict,
    )

    # Parameters used when you are using the rule to invoke Amazon EC2 Run
    # Command.
    run_command_parameters: "RunCommandParameters" = dataclasses.field(
        default_factory=dict,
    )

    # Contains the Amazon ECS task definition and task count to be used, if the
    # event target is an Amazon ECS task. For more information about Amazon ECS
    # tasks, see [Task Definitions
    # ](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html)
    # in the _Amazon EC2 Container Service Developer Guide_.
    ecs_parameters: "EcsParameters" = dataclasses.field(default_factory=dict, )

    # Contains the job definition, job name, and other parameters if the event
    # target is an AWS Batch job. For more information about AWS Batch, see
    # [Jobs](http://docs.aws.amazon.com/batch/latest/userguide/jobs.html) in the
    # _AWS Batch User Guide_.
    batch_parameters: "BatchParameters" = dataclasses.field(
        default_factory=dict,
    )

    # Contains the message group ID to use when the target is a FIFO queue.
    sqs_parameters: "SqsParameters" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class TestEventPatternRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_pattern",
                "EventPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "event",
                "Event",
                autoboto.TypeInfo(str),
            ),
        ]

    # The event pattern. For more information, see [Events and Event
    # Patterns](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html)
    # in the _Amazon CloudWatch Events User Guide_.
    event_pattern: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The event, in JSON format, to test against the event pattern.
    event: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TestEventPatternResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "result",
                "Result",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Indicates whether the event matches the event pattern.
    result: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
