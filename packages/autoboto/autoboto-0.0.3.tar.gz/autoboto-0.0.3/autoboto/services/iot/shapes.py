import datetime
import typing
import autoboto
from enum import Enum
import botocore.response
import dataclasses


@dataclasses.dataclass
class AcceptCertificateTransferRequest(autoboto.ShapeBase):
    """
    The input for the AcceptCertificateTransfer operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "set_as_active",
                "setAsActive",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the certificate. (The last part of the certificate ARN contains
    # the certificate ID.)
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether the certificate is active.
    set_as_active: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Action(autoboto.ShapeBase):
    """
    Describes the actions associated with a rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dynamo_db",
                "dynamoDB",
                autoboto.TypeInfo(DynamoDBAction),
            ),
            (
                "dynamo_d_bv2",
                "dynamoDBv2",
                autoboto.TypeInfo(DynamoDBv2Action),
            ),
            (
                "lambda_",
                "lambda",
                autoboto.TypeInfo(LambdaAction),
            ),
            (
                "sns",
                "sns",
                autoboto.TypeInfo(SnsAction),
            ),
            (
                "sqs",
                "sqs",
                autoboto.TypeInfo(SqsAction),
            ),
            (
                "kinesis",
                "kinesis",
                autoboto.TypeInfo(KinesisAction),
            ),
            (
                "republish",
                "republish",
                autoboto.TypeInfo(RepublishAction),
            ),
            (
                "s3",
                "s3",
                autoboto.TypeInfo(S3Action),
            ),
            (
                "firehose",
                "firehose",
                autoboto.TypeInfo(FirehoseAction),
            ),
            (
                "cloudwatch_metric",
                "cloudwatchMetric",
                autoboto.TypeInfo(CloudwatchMetricAction),
            ),
            (
                "cloudwatch_alarm",
                "cloudwatchAlarm",
                autoboto.TypeInfo(CloudwatchAlarmAction),
            ),
            (
                "elasticsearch",
                "elasticsearch",
                autoboto.TypeInfo(ElasticsearchAction),
            ),
            (
                "salesforce",
                "salesforce",
                autoboto.TypeInfo(SalesforceAction),
            ),
            (
                "iot_analytics",
                "iotAnalytics",
                autoboto.TypeInfo(IotAnalyticsAction),
            ),
            (
                "step_functions",
                "stepFunctions",
                autoboto.TypeInfo(StepFunctionsAction),
            ),
        ]

    # Write to a DynamoDB table.
    dynamo_db: "DynamoDBAction" = dataclasses.field(default_factory=dict, )

    # Write to a DynamoDB table. This is a new version of the DynamoDB action. It
    # allows you to write each attribute in an MQTT message payload into a
    # separate DynamoDB column.
    dynamo_d_bv2: "DynamoDBv2Action" = dataclasses.field(default_factory=dict, )

    # Invoke a Lambda function.
    lambda_: "LambdaAction" = dataclasses.field(default_factory=dict, )

    # Publish to an Amazon SNS topic.
    sns: "SnsAction" = dataclasses.field(default_factory=dict, )

    # Publish to an Amazon SQS queue.
    sqs: "SqsAction" = dataclasses.field(default_factory=dict, )

    # Write data to an Amazon Kinesis stream.
    kinesis: "KinesisAction" = dataclasses.field(default_factory=dict, )

    # Publish to another MQTT topic.
    republish: "RepublishAction" = dataclasses.field(default_factory=dict, )

    # Write to an Amazon S3 bucket.
    s3: "S3Action" = dataclasses.field(default_factory=dict, )

    # Write to an Amazon Kinesis Firehose stream.
    firehose: "FirehoseAction" = dataclasses.field(default_factory=dict, )

    # Capture a CloudWatch metric.
    cloudwatch_metric: "CloudwatchMetricAction" = dataclasses.field(
        default_factory=dict,
    )

    # Change the state of a CloudWatch alarm.
    cloudwatch_alarm: "CloudwatchAlarmAction" = dataclasses.field(
        default_factory=dict,
    )

    # Write data to an Amazon Elasticsearch Service domain.
    elasticsearch: "ElasticsearchAction" = dataclasses.field(
        default_factory=dict,
    )

    # Send a message to a Salesforce IoT Cloud Input Stream.
    salesforce: "SalesforceAction" = dataclasses.field(default_factory=dict, )

    # Sends message data to an AWS IoT Analytics channel.
    iot_analytics: "IotAnalyticsAction" = dataclasses.field(
        default_factory=dict,
    )

    # Starts execution of a Step Functions state machine.
    step_functions: "StepFunctionsAction" = dataclasses.field(
        default_factory=dict,
    )


class ActionType(Enum):
    PUBLISH = "PUBLISH"
    SUBSCRIBE = "SUBSCRIBE"
    RECEIVE = "RECEIVE"
    CONNECT = "CONNECT"


@dataclasses.dataclass
class ActiveViolation(autoboto.ShapeBase):
    """
    Information about an active Device Defender security profile behavior violation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "violation_id",
                "violationId",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "security_profile_name",
                "securityProfileName",
                autoboto.TypeInfo(str),
            ),
            (
                "behavior",
                "behavior",
                autoboto.TypeInfo(Behavior),
            ),
            (
                "last_violation_value",
                "lastViolationValue",
                autoboto.TypeInfo(MetricValue),
            ),
            (
                "last_violation_time",
                "lastViolationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "violation_start_time",
                "violationStartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ID of the active violation.
    violation_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the thing responsible for the active violation.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The security profile whose behavior is in violation.
    security_profile_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The behavior which is being violated.
    behavior: "Behavior" = dataclasses.field(default_factory=dict, )

    # The value of the metric (the measurement) which caused the most recent
    # violation.
    last_violation_value: "MetricValue" = dataclasses.field(
        default_factory=dict,
    )

    # The time the most recent violation occurred.
    last_violation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time the violation started.
    violation_start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AddThingToThingGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_group_name",
                "thingGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_group_arn",
                "thingGroupArn",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_arn",
                "thingArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the group to which you are adding a thing.
    thing_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the group to which you are adding a thing.
    thing_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the thing to add to a group.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the thing to add to a group.
    thing_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AddThingToThingGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AlertTarget(autoboto.ShapeBase):
    """
    A structure containing the alert target ARN and the role ARN.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alert_target_arn",
                "alertTargetArn",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the notification target to which alerts are sent.
    alert_target_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the role that grants permission to send alerts to the
    # notification target.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class AlertTargetType(Enum):
    """
    The type of alert target: one of "SNS".
    """
    SNS = "SNS"


@dataclasses.dataclass
class Allowed(autoboto.ShapeBase):
    """
    Contains information that allowed the authorization.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policies",
                "policies",
                autoboto.TypeInfo(typing.List[Policy]),
            ),
        ]

    # A list of policies that allowed the authentication.
    policies: typing.List["Policy"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class AssociateTargetsWithJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "targets",
                "targets",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "comment",
                "comment",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of thing group ARNs that define the targets of the job.
    targets: typing.List[str] = dataclasses.field(default_factory=list, )

    # The unique identifier you assigned to this job when it was created.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An optional comment string describing why the job was associated with the
    # targets.
    comment: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AssociateTargetsWithJobResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_arn",
                "jobArn",
                autoboto.TypeInfo(str),
            ),
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # An ARN identifying the job.
    job_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique identifier you assigned to this job when it was created.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A short text description of the job.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AttachPolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "target",
                "target",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the policy to attach.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identity to which the policy is attached.
    target: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AttachPrincipalPolicyRequest(autoboto.ShapeBase):
    """
    The input for the AttachPrincipalPolicy operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "principal",
                "principal",
                autoboto.TypeInfo(str),
            ),
        ]

    # The policy name.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The principal, which can be a certificate ARN (as returned from the
    # CreateCertificate operation) or an Amazon Cognito ID.
    principal: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AttachSecurityProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_profile_name",
                "securityProfileName",
                autoboto.TypeInfo(str),
            ),
            (
                "security_profile_target_arn",
                "securityProfileTargetArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The security profile that is attached.
    security_profile_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the target (thing group) to which the security profile is
    # attached.
    security_profile_target_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AttachSecurityProfileResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AttachThingPrincipalRequest(autoboto.ShapeBase):
    """
    The input for the AttachThingPrincipal operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "principal",
                "principal",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the thing.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The principal, such as a certificate or other credential.
    principal: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AttachThingPrincipalResponse(autoboto.ShapeBase):
    """
    The output from the AttachThingPrincipal operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AttributePayload(autoboto.ShapeBase):
    """
    The attribute payload.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "merge",
                "merge",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A JSON string containing up to three key-value pair in JSON format. For
    # example:

    # `{\"attributes\":{\"string1\":\"string2\"}}`
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether the list of attributes provided in the `AttributePayload`
    # is merged with the attributes stored in the registry, instead of
    # overwriting them.

    # To remove an attribute, call `UpdateThing` with an empty attribute value.

    # The `merge` attribute is only valid when calling `UpdateThing`.
    merge: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AuditCheckConfiguration(autoboto.ShapeBase):
    """
    Which audit checks are enabled and disabled for this account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "enabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # True if this audit check is enabled for this account.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AuditCheckDetails(autoboto.ShapeBase):
    """
    Information about the audit check.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "check_run_status",
                "checkRunStatus",
                autoboto.TypeInfo(AuditCheckRunStatus),
            ),
            (
                "check_compliant",
                "checkCompliant",
                autoboto.TypeInfo(bool),
            ),
            (
                "total_resources_count",
                "totalResourcesCount",
                autoboto.TypeInfo(int),
            ),
            (
                "non_compliant_resources_count",
                "nonCompliantResourcesCount",
                autoboto.TypeInfo(int),
            ),
            (
                "error_code",
                "errorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The completion status of this check, one of "IN_PROGRESS",
    # "WAITING_FOR_DATA_COLLECTION", "CANCELED", "COMPLETED_COMPLIANT",
    # "COMPLETED_NON_COMPLIANT", or "FAILED".
    check_run_status: "AuditCheckRunStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # True if the check completed and found all resources compliant.
    check_compliant: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of resources on which the check was performed.
    total_resources_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of resources that the check found non-compliant.
    non_compliant_resources_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The code of any error encountered when performing this check during this
    # audit. One of "INSUFFICIENT_PERMISSIONS", or "AUDIT_CHECK_DISABLED".
    error_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message associated with any error encountered when performing this
    # check during this audit.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class AuditCheckRunStatus(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    WAITING_FOR_DATA_COLLECTION = "WAITING_FOR_DATA_COLLECTION"
    CANCELED = "CANCELED"
    COMPLETED_COMPLIANT = "COMPLETED_COMPLIANT"
    COMPLETED_NON_COMPLIANT = "COMPLETED_NON_COMPLIANT"
    FAILED = "FAILED"


@dataclasses.dataclass
class AuditFinding(autoboto.ShapeBase):
    """
    The findings (results) of the audit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                autoboto.TypeInfo(str),
            ),
            (
                "check_name",
                "checkName",
                autoboto.TypeInfo(str),
            ),
            (
                "task_start_time",
                "taskStartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "finding_time",
                "findingTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "severity",
                "severity",
                autoboto.TypeInfo(AuditFindingSeverity),
            ),
            (
                "non_compliant_resource",
                "nonCompliantResource",
                autoboto.TypeInfo(NonCompliantResource),
            ),
            (
                "related_resources",
                "relatedResources",
                autoboto.TypeInfo(typing.List[RelatedResource]),
            ),
            (
                "reason_for_non_compliance",
                "reasonForNonCompliance",
                autoboto.TypeInfo(str),
            ),
            (
                "reason_for_non_compliance_code",
                "reasonForNonComplianceCode",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the audit that generated this result (finding)
    task_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The audit check that generated this result.
    check_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time the audit started.
    task_start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time the result (finding) was discovered.
    finding_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The severity of the result (finding).
    severity: "AuditFindingSeverity" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The resource that was found to be non-compliant with the audit check.
    non_compliant_resource: "NonCompliantResource" = dataclasses.field(
        default_factory=dict,
    )

    # The list of related resources.
    related_resources: typing.List["RelatedResource"] = dataclasses.field(
        default_factory=list,
    )

    # The reason the resource was non-compliant.
    reason_for_non_compliance: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A code which indicates the reason that the resource was non-compliant.
    reason_for_non_compliance_code: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class AuditFindingSeverity(Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class AuditFrequency(Enum):
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    BIWEEKLY = "BIWEEKLY"
    MONTHLY = "MONTHLY"


@dataclasses.dataclass
class AuditNotificationTarget(autoboto.ShapeBase):
    """
    Information about the targets to which audit notifications are sent.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_arn",
                "targetArn",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "enabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ARN of the target (SNS topic) to which audit notifications are sent.
    target_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the role that grants permission to send notifications to the
    # target.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # True if notifications to the target are enabled.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class AuditNotificationType(Enum):
    SNS = "SNS"


@dataclasses.dataclass
class AuditTaskMetadata(autoboto.ShapeBase):
    """
    The audits that were performed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_status",
                "taskStatus",
                autoboto.TypeInfo(AuditTaskStatus),
            ),
            (
                "task_type",
                "taskType",
                autoboto.TypeInfo(AuditTaskType),
            ),
        ]

    # The ID of this audit.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of this audit: one of "IN_PROGRESS", "COMPLETED", "FAILED" or
    # "CANCELED".
    task_status: "AuditTaskStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of this audit: one of "ON_DEMAND_AUDIT_TASK" or
    # "SCHEDULED_AUDIT_TASK".
    task_type: "AuditTaskType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class AuditTaskStatus(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELED = "CANCELED"


class AuditTaskType(Enum):
    ON_DEMAND_AUDIT_TASK = "ON_DEMAND_AUDIT_TASK"
    SCHEDULED_AUDIT_TASK = "SCHEDULED_AUDIT_TASK"


class AuthDecision(Enum):
    ALLOWED = "ALLOWED"
    EXPLICIT_DENY = "EXPLICIT_DENY"
    IMPLICIT_DENY = "IMPLICIT_DENY"


@dataclasses.dataclass
class AuthInfo(autoboto.ShapeBase):
    """
    A collection of authorization information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_type",
                "actionType",
                autoboto.TypeInfo(ActionType),
            ),
            (
                "resources",
                "resources",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The type of action for which the principal is being authorized.
    action_type: "ActionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The resources for which the principal is being authorized to perform the
    # specified action.
    resources: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class AuthResult(autoboto.ShapeBase):
    """
    The authorizer result.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auth_info",
                "authInfo",
                autoboto.TypeInfo(AuthInfo),
            ),
            (
                "allowed",
                "allowed",
                autoboto.TypeInfo(Allowed),
            ),
            (
                "denied",
                "denied",
                autoboto.TypeInfo(Denied),
            ),
            (
                "auth_decision",
                "authDecision",
                autoboto.TypeInfo(AuthDecision),
            ),
            (
                "missing_context_values",
                "missingContextValues",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # Authorization information.
    auth_info: "AuthInfo" = dataclasses.field(default_factory=dict, )

    # The policies and statements that allowed the specified action.
    allowed: "Allowed" = dataclasses.field(default_factory=dict, )

    # The policies and statements that denied the specified action.
    denied: "Denied" = dataclasses.field(default_factory=dict, )

    # The final authorization decision of this scenario. Multiple statements are
    # taken into account when determining the authorization decision. An explicit
    # deny statement can override multiple allow statements.
    auth_decision: "AuthDecision" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Contains any missing context values found while evaluating policy.
    missing_context_values: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AuthorizerDescription(autoboto.ShapeBase):
    """
    The authorizer description.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorizer_name",
                "authorizerName",
                autoboto.TypeInfo(str),
            ),
            (
                "authorizer_arn",
                "authorizerArn",
                autoboto.TypeInfo(str),
            ),
            (
                "authorizer_function_arn",
                "authorizerFunctionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "token_key_name",
                "tokenKeyName",
                autoboto.TypeInfo(str),
            ),
            (
                "token_signing_public_keys",
                "tokenSigningPublicKeys",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(AuthorizerStatus),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_date",
                "lastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The authorizer name.
    authorizer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The authorizer ARN.
    authorizer_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The authorizer's Lambda function ARN.
    authorizer_function_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The key used to extract the token from the HTTP headers.
    token_key_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The public keys used to validate the token signature returned by your
    # custom authentication service.
    token_signing_public_keys: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the authorizer.
    status: "AuthorizerStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The UNIX timestamp of when the authorizer was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The UNIX timestamp of when the authorizer was last updated.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class AuthorizerStatus(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


@dataclasses.dataclass
class AuthorizerSummary(autoboto.ShapeBase):
    """
    The authorizer summary.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorizer_name",
                "authorizerName",
                autoboto.TypeInfo(str),
            ),
            (
                "authorizer_arn",
                "authorizerArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The authorizer name.
    authorizer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The authorizer ARN.
    authorizer_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class AutoRegistrationStatus(Enum):
    ENABLE = "ENABLE"
    DISABLE = "DISABLE"


@dataclasses.dataclass
class Behavior(autoboto.ShapeBase):
    """
    A Device Defender security profile behavior.
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
                "metric",
                "metric",
                autoboto.TypeInfo(str),
            ),
            (
                "criteria",
                "criteria",
                autoboto.TypeInfo(BehaviorCriteria),
            ),
        ]

    # The name you have given to the behavior.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # What is measured by the behavior.
    metric: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The criteria that determine if a device is behaving normally in regard to
    # the `metric`.
    criteria: "BehaviorCriteria" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class BehaviorCriteria(autoboto.ShapeBase):
    """
    The criteria by which the behavior is determined to be normal.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comparison_operator",
                "comparisonOperator",
                autoboto.TypeInfo(ComparisonOperator),
            ),
            (
                "value",
                "value",
                autoboto.TypeInfo(MetricValue),
            ),
            (
                "duration_seconds",
                "durationSeconds",
                autoboto.TypeInfo(int),
            ),
        ]

    # The operator that relates the thing measured (`metric`) to the criteria
    # (`value`).
    comparison_operator: "ComparisonOperator" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value to be compared with the `metric`.
    value: "MetricValue" = dataclasses.field(default_factory=dict, )

    # Use this to specify the period of time over which the behavior is
    # evaluated, for those criteria which have a time dimension (for example,
    # `NUM_MESSAGES_SENT`).
    duration_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CACertificate(autoboto.ShapeBase):
    """
    A CA certificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "certificateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(CACertificateStatus),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ARN of the CA certificate.
    certificate_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the CA certificate.
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the CA certificate.

    # The status value REGISTER_INACTIVE is deprecated and should not be used.
    status: "CACertificateStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the CA certificate was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CACertificateDescription(autoboto.ShapeBase):
    """
    Describes a CA certificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "certificateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(CACertificateStatus),
            ),
            (
                "certificate_pem",
                "certificatePem",
                autoboto.TypeInfo(str),
            ),
            (
                "owned_by",
                "ownedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "auto_registration_status",
                "autoRegistrationStatus",
                autoboto.TypeInfo(AutoRegistrationStatus),
            ),
            (
                "last_modified_date",
                "lastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "customer_version",
                "customerVersion",
                autoboto.TypeInfo(int),
            ),
            (
                "generation_id",
                "generationId",
                autoboto.TypeInfo(str),
            ),
            (
                "validity",
                "validity",
                autoboto.TypeInfo(CertificateValidity),
            ),
        ]

    # The CA certificate ARN.
    certificate_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The CA certificate ID.
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of a CA certificate.
    status: "CACertificateStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The CA certificate data, in PEM format.
    certificate_pem: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The owner of the CA certificate.
    owned_by: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date the CA certificate was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the CA certificate configured for auto registration of device
    # certificates. Valid values are "ENABLE" and "DISABLE"
    auto_registration_status: "AutoRegistrationStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the CA certificate was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The customer version of the CA certificate.
    customer_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The generation ID of the CA certificate.
    generation_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When the CA certificate is valid.
    validity: "CertificateValidity" = dataclasses.field(default_factory=dict, )


class CACertificateStatus(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


@dataclasses.dataclass
class CancelAuditTaskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the audit you want to cancel. You can only cancel an audit that
    # is "IN_PROGRESS".
    task_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CancelAuditTaskResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CancelCertificateTransferRequest(autoboto.ShapeBase):
    """
    The input for the CancelCertificateTransfer operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the certificate. (The last part of the certificate ARN contains
    # the certificate ID.)
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CancelJobExecutionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "force",
                "force",
                autoboto.TypeInfo(bool),
            ),
            (
                "expected_version",
                "expectedVersion",
                autoboto.TypeInfo(int),
            ),
            (
                "status_details",
                "statusDetails",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The ID of the job to be canceled.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the thing whose execution of the job will be canceled.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # (Optional) If `true` the job execution will be canceled if it has status
    # IN_PROGRESS or QUEUED, otherwise the job execution will be canceled only if
    # it has status QUEUED. If you attempt to cancel a job execution that is
    # IN_PROGRESS, and you do not set `force` to `true`, then an
    # `InvalidStateTransitionException` will be thrown. The default is `false`.

    # Canceling a job execution which is "IN_PROGRESS", will cause the device to
    # be unable to update the job execution status. Use caution and ensure that
    # the device is able to recover to a valid state.
    force: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # (Optional) The expected current version of the job execution. Each time you
    # update the job execution, its version is incremented. If the version of the
    # job execution stored in Jobs does not match, the update is rejected with a
    # VersionMismatch error, and an ErrorResponse that contains the current job
    # execution status data is returned. (This makes it unnecessary to perform a
    # separate DescribeJobExecution request in order to obtain the job execution
    # status data.)
    expected_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A collection of name/value pairs that describe the status of the job
    # execution. If not specified, the statusDetails are unchanged. You can
    # specify at most 10 name/value pairs.
    status_details: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CancelJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "comment",
                "comment",
                autoboto.TypeInfo(str),
            ),
            (
                "force",
                "force",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The unique identifier you assigned to this job when it was created.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An optional comment string describing why the job was canceled.
    comment: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # (Optional) If `true` job executions with status "IN_PROGRESS" and "QUEUED"
    # are canceled, otherwise only job executions with status "QUEUED" are
    # canceled. The default is `false`.

    # Canceling a job which is "IN_PROGRESS", will cause a device which is
    # executing the job to be unable to update the job execution status. Use
    # caution and ensure that each device executing a job which is canceled is
    # able to recover to a valid state.
    force: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CancelJobResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_arn",
                "jobArn",
                autoboto.TypeInfo(str),
            ),
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The job ARN.
    job_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique identifier you assigned to this job when it was created.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A short text description of the job.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class CannedAccessControlList(Enum):
    private = "private"
    public_read = "public-read"
    public_read_write = "public-read-write"
    aws_exec_read = "aws-exec-read"
    authenticated_read = "authenticated-read"
    bucket_owner_read = "bucket-owner-read"
    bucket_owner_full_control = "bucket-owner-full-control"
    log_delivery_write = "log-delivery-write"


@dataclasses.dataclass
class Certificate(autoboto.ShapeBase):
    """
    Information about a certificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "certificateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(CertificateStatus),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ARN of the certificate.
    certificate_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the certificate. (The last part of the certificate ARN contains
    # the certificate ID.)
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the certificate.

    # The status value REGISTER_INACTIVE is deprecated and should not be used.
    status: "CertificateStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time the certificate was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CertificateConflictException(autoboto.ShapeBase):
    """
    Unable to verify the CA certificate used to sign the device certificate you are
    attempting to register. This is happens when you have registered more than one
    CA certificate that has the same subject field and public key.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CertificateDescription(autoboto.ShapeBase):
    """
    Describes a certificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "certificateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "ca_certificate_id",
                "caCertificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(CertificateStatus),
            ),
            (
                "certificate_pem",
                "certificatePem",
                autoboto.TypeInfo(str),
            ),
            (
                "owned_by",
                "ownedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "previous_owned_by",
                "previousOwnedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_date",
                "lastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "customer_version",
                "customerVersion",
                autoboto.TypeInfo(int),
            ),
            (
                "transfer_data",
                "transferData",
                autoboto.TypeInfo(TransferData),
            ),
            (
                "generation_id",
                "generationId",
                autoboto.TypeInfo(str),
            ),
            (
                "validity",
                "validity",
                autoboto.TypeInfo(CertificateValidity),
            ),
        ]

    # The ARN of the certificate.
    certificate_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the certificate.
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The certificate ID of the CA certificate used to sign this certificate.
    ca_certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the certificate.
    status: "CertificateStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The certificate data, in PEM format.
    certificate_pem: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the AWS account that owns the certificate.
    owned_by: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the AWS account of the previous owner of the certificate.
    previous_owned_by: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time the certificate was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time the certificate was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The customer version of the certificate.
    customer_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The transfer data.
    transfer_data: "TransferData" = dataclasses.field(default_factory=dict, )

    # The generation ID of the certificate.
    generation_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When the certificate is valid.
    validity: "CertificateValidity" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CertificateStateException(autoboto.ShapeBase):
    """
    The certificate operation is not allowed.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class CertificateStatus(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    REVOKED = "REVOKED"
    PENDING_TRANSFER = "PENDING_TRANSFER"
    REGISTER_INACTIVE = "REGISTER_INACTIVE"
    PENDING_ACTIVATION = "PENDING_ACTIVATION"


@dataclasses.dataclass
class CertificateValidationException(autoboto.ShapeBase):
    """
    The certificate is invalid.
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

    # Additional information about the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CertificateValidity(autoboto.ShapeBase):
    """
    When the certificate is valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "not_before",
                "notBefore",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "not_after",
                "notAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The certificate is not valid before this date.
    not_before: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The certificate is not valid after this date.
    not_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ClearDefaultAuthorizerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClearDefaultAuthorizerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CloudwatchAlarmAction(autoboto.ShapeBase):
    """
    Describes an action that updates a CloudWatch alarm.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "alarm_name",
                "alarmName",
                autoboto.TypeInfo(str),
            ),
            (
                "state_reason",
                "stateReason",
                autoboto.TypeInfo(str),
            ),
            (
                "state_value",
                "stateValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The IAM role that allows access to the CloudWatch alarm.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The CloudWatch alarm name.
    alarm_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The reason for the alarm change.
    state_reason: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value of the alarm state. Acceptable values are: OK, ALARM,
    # INSUFFICIENT_DATA.
    state_value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CloudwatchMetricAction(autoboto.ShapeBase):
    """
    Describes an action that captures a CloudWatch metric.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_namespace",
                "metricNamespace",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_name",
                "metricName",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_value",
                "metricValue",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_unit",
                "metricUnit",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_timestamp",
                "metricTimestamp",
                autoboto.TypeInfo(str),
            ),
        ]

    # The IAM role that allows access to the CloudWatch metric.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The CloudWatch metric namespace name.
    metric_namespace: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The CloudWatch metric name.
    metric_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The CloudWatch metric value.
    metric_value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The [metric
    # unit](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit)
    # supported by CloudWatch.
    metric_unit: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An optional [Unix
    # timestamp](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp).
    metric_timestamp: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CodeSigning(autoboto.ShapeBase):
    """
    Describes the method to use when code signing a file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "aws_signer_job_id",
                "awsSignerJobId",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_code_signing",
                "customCodeSigning",
                autoboto.TypeInfo(CustomCodeSigning),
            ),
        ]

    # The ID of the AWSSignerJob which was created to sign the file.
    aws_signer_job_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A custom method for code signing a file.
    custom_code_signing: "CustomCodeSigning" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CodeSigningCertificateChain(autoboto.ShapeBase):
    """
    Describes the certificate chain being used when code signing a file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream",
                "stream",
                autoboto.TypeInfo(Stream),
            ),
            (
                "certificate_name",
                "certificateName",
                autoboto.TypeInfo(str),
            ),
            (
                "inline_document",
                "inlineDocument",
                autoboto.TypeInfo(str),
            ),
        ]

    # A stream of the certificate chain files.
    stream: "Stream" = dataclasses.field(default_factory=dict, )

    # The name of the certificate.
    certificate_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A base64 encoded binary representation of the code signing certificate
    # chain.
    inline_document: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CodeSigningSignature(autoboto.ShapeBase):
    """
    Describes the signature for a file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream",
                "stream",
                autoboto.TypeInfo(Stream),
            ),
            (
                "inline_document",
                "inlineDocument",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # A stream of the code signing signature.
    stream: "Stream" = dataclasses.field(default_factory=dict, )

    # A base64 encoded binary representation of the code signing signature.
    inline_document: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class ComparisonOperator(Enum):
    less_than = "less-than"
    less_than_equals = "less-than-equals"
    greater_than = "greater-than"
    greater_than_equals = "greater-than-equals"
    in_cidr_set = "in-cidr-set"
    not_in_cidr_set = "not-in-cidr-set"
    in_port_set = "in-port-set"
    not_in_port_set = "not-in-port-set"


@dataclasses.dataclass
class Configuration(autoboto.ShapeBase):
    """
    Configuration.
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

    # True to enable the configuration.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ConflictingResourceUpdateException(autoboto.ShapeBase):
    """
    A conflicting resource update exception. This exception is thrown when two
    pending updates cause a conflict.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateAuthorizerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorizer_name",
                "authorizerName",
                autoboto.TypeInfo(str),
            ),
            (
                "authorizer_function_arn",
                "authorizerFunctionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "token_key_name",
                "tokenKeyName",
                autoboto.TypeInfo(str),
            ),
            (
                "token_signing_public_keys",
                "tokenSigningPublicKeys",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(AuthorizerStatus),
            ),
        ]

    # The authorizer name.
    authorizer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the authorizer's Lambda function.
    authorizer_function_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the token key used to extract the token from the HTTP headers.
    token_key_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The public keys used to verify the digital signature returned by your
    # custom authentication service.
    token_signing_public_keys: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the create authorizer request.
    status: "AuthorizerStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateAuthorizerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorizer_name",
                "authorizerName",
                autoboto.TypeInfo(str),
            ),
            (
                "authorizer_arn",
                "authorizerArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The authorizer's name.
    authorizer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The authorizer ARN.
    authorizer_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateCertificateFromCsrRequest(autoboto.ShapeBase):
    """
    The input for the CreateCertificateFromCsr operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_signing_request",
                "certificateSigningRequest",
                autoboto.TypeInfo(str),
            ),
            (
                "set_as_active",
                "setAsActive",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The certificate signing request (CSR).
    certificate_signing_request: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether the certificate is active.
    set_as_active: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateCertificateFromCsrResponse(autoboto.ShapeBase):
    """
    The output from the CreateCertificateFromCsr operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "certificateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_pem",
                "certificatePem",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the certificate. You can use the ARN as a
    # principal for policy operations.
    certificate_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the certificate. Certificate management operations only take a
    # certificateId.
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The certificate data, in PEM format.
    certificate_pem: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "targets",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "document_source",
                "documentSource",
                autoboto.TypeInfo(str),
            ),
            (
                "document",
                "document",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "presigned_url_config",
                "presignedUrlConfig",
                autoboto.TypeInfo(PresignedUrlConfig),
            ),
            (
                "target_selection",
                "targetSelection",
                autoboto.TypeInfo(TargetSelection),
            ),
            (
                "job_executions_rollout_config",
                "jobExecutionsRolloutConfig",
                autoboto.TypeInfo(JobExecutionsRolloutConfig),
            ),
        ]

    # A job identifier which must be unique for your AWS account. We recommend
    # using a UUID. Alpha-numeric characters, "-" and "_" are valid for use here.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of things and thing groups to which the job should be sent.
    targets: typing.List[str] = dataclasses.field(default_factory=list, )

    # An S3 link to the job document.
    document_source: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The job document.
    document: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A short text description of the job.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Configuration information for pre-signed S3 URLs.
    presigned_url_config: "PresignedUrlConfig" = dataclasses.field(
        default_factory=dict,
    )

    # Specifies whether the job will continue to run (CONTINUOUS), or will be
    # complete after all those things specified as targets have completed the job
    # (SNAPSHOT). If continuous, the job may also be run on a thing when a change
    # is detected in a target. For example, a job will run on a thing when the
    # thing is added to a target group, even after the job was completed by all
    # things originally in the group.
    target_selection: "TargetSelection" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Allows you to create a staged rollout of the job.
    job_executions_rollout_config: "JobExecutionsRolloutConfig" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateJobResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_arn",
                "jobArn",
                autoboto.TypeInfo(str),
            ),
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The job ARN.
    job_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique identifier you assigned to this job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The job description.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateKeysAndCertificateRequest(autoboto.ShapeBase):
    """
    The input for the CreateKeysAndCertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "set_as_active",
                "setAsActive",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Specifies whether the certificate is active.
    set_as_active: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateKeysAndCertificateResponse(autoboto.ShapeBase):
    """
    The output of the CreateKeysAndCertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "certificateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_pem",
                "certificatePem",
                autoboto.TypeInfo(str),
            ),
            (
                "key_pair",
                "keyPair",
                autoboto.TypeInfo(KeyPair),
            ),
        ]

    # The ARN of the certificate.
    certificate_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the certificate. AWS IoT issues a default subject name for the
    # certificate (for example, AWS IoT Certificate).
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The certificate data, in PEM format.
    certificate_pem: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The generated key pair.
    key_pair: "KeyPair" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateOTAUpdateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ota_update_id",
                "otaUpdateId",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "targets",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "files",
                "files",
                autoboto.TypeInfo(typing.List[OTAUpdateFile]),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "target_selection",
                "targetSelection",
                autoboto.TypeInfo(TargetSelection),
            ),
            (
                "additional_parameters",
                "additionalParameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The ID of the OTA update to be created.
    ota_update_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The targeted devices to receive OTA updates.
    targets: typing.List[str] = dataclasses.field(default_factory=list, )

    # The files to be streamed by the OTA update.
    files: typing.List["OTAUpdateFile"] = dataclasses.field(
        default_factory=list,
    )

    # The IAM role that allows access to the AWS IoT Jobs service.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The description of the OTA update.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies whether the update will continue to run (CONTINUOUS), or will be
    # complete after all the things specified as targets have completed the
    # update (SNAPSHOT). If continuous, the update may also be run on a thing
    # when a change is detected in a target. For example, an update will run on a
    # thing when the thing is added to a target group, even after the update was
    # completed by all things originally in the group. Valid values: CONTINUOUS |
    # SNAPSHOT.
    target_selection: "TargetSelection" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of additional OTA update parameters which are name-value pairs.
    additional_parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateOTAUpdateResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ota_update_id",
                "otaUpdateId",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_iot_job_id",
                "awsIotJobId",
                autoboto.TypeInfo(str),
            ),
            (
                "ota_update_arn",
                "otaUpdateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_iot_job_arn",
                "awsIotJobArn",
                autoboto.TypeInfo(str),
            ),
            (
                "ota_update_status",
                "otaUpdateStatus",
                autoboto.TypeInfo(OTAUpdateStatus),
            ),
        ]

    # The OTA update ID.
    ota_update_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS IoT job ID associated with the OTA update.
    aws_iot_job_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The OTA update ARN.
    ota_update_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS IoT job ARN associated with the OTA update.
    aws_iot_job_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The OTA update status.
    ota_update_status: "OTAUpdateStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreatePolicyRequest(autoboto.ShapeBase):
    """
    The input for the CreatePolicy operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_document",
                "policyDocument",
                autoboto.TypeInfo(str),
            ),
        ]

    # The policy name.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The JSON document that describes the policy. **policyDocument** must have a
    # minimum length of 1, with a maximum length of 2048, excluding whitespace.
    policy_document: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreatePolicyResponse(autoboto.ShapeBase):
    """
    The output from the CreatePolicy operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_arn",
                "policyArn",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_document",
                "policyDocument",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_version_id",
                "policyVersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The policy name.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The policy ARN.
    policy_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The JSON document that describes the policy.
    policy_document: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The policy version ID.
    policy_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreatePolicyVersionRequest(autoboto.ShapeBase):
    """
    The input for the CreatePolicyVersion operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_document",
                "policyDocument",
                autoboto.TypeInfo(str),
            ),
            (
                "set_as_default",
                "setAsDefault",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The policy name.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The JSON document that describes the policy. Minimum length of 1. Maximum
    # length of 2048, excluding whitespace.
    policy_document: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether the policy version is set as the default. When this
    # parameter is true, the new policy version becomes the operative version
    # (that is, the version that is in effect for the certificates to which the
    # policy is attached).
    set_as_default: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreatePolicyVersionResponse(autoboto.ShapeBase):
    """
    The output of the CreatePolicyVersion operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_arn",
                "policyArn",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_document",
                "policyDocument",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_version_id",
                "policyVersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "is_default_version",
                "isDefaultVersion",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The policy ARN.
    policy_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The JSON document that describes the policy.
    policy_document: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The policy version ID.
    policy_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether the policy version is the default.
    is_default_version: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateRoleAliasRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_alias",
                "roleAlias",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "credential_duration_seconds",
                "credentialDurationSeconds",
                autoboto.TypeInfo(int),
            ),
        ]

    # The role alias that points to a role ARN. This allows you to change the
    # role without having to update the device.
    role_alias: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The role ARN.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # How long (in seconds) the credentials will be valid.
    credential_duration_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateRoleAliasResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_alias",
                "roleAlias",
                autoboto.TypeInfo(str),
            ),
            (
                "role_alias_arn",
                "roleAliasArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The role alias.
    role_alias: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The role alias ARN.
    role_alias_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateScheduledAuditRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "frequency",
                "frequency",
                autoboto.TypeInfo(AuditFrequency),
            ),
            (
                "target_check_names",
                "targetCheckNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "scheduled_audit_name",
                "scheduledAuditName",
                autoboto.TypeInfo(str),
            ),
            (
                "day_of_month",
                "dayOfMonth",
                autoboto.TypeInfo(str),
            ),
            (
                "day_of_week",
                "dayOfWeek",
                autoboto.TypeInfo(DayOfWeek),
            ),
        ]

    # How often the scheduled audit takes place. Can be one of "DAILY", "WEEKLY",
    # "BIWEEKLY" or "MONTHLY". The actual start time of each audit is determined
    # by the system.
    frequency: "AuditFrequency" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Which checks are performed during the scheduled audit. Checks must be
    # enabled for your account. (Use `DescribeAccountAuditConfiguration` to see
    # the list of all checks including those that are enabled or
    # `UpdateAccountAuditConfiguration` to select which checks are enabled.)
    target_check_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The name you want to give to the scheduled audit. (Max. 128 chars)
    scheduled_audit_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The day of the month on which the scheduled audit takes place. Can be "1"
    # through "31" or "LAST". This field is required if the "frequency" parameter
    # is set to "MONTHLY". If days 29-31 are specified, and the month does not
    # have that many days, the audit takes place on the "LAST" day of the month.
    day_of_month: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The day of the week on which the scheduled audit takes place. Can be one of
    # "SUN", "MON", "TUE", "WED", "THU", "FRI" or "SAT". This field is required
    # if the "frequency" parameter is set to "WEEKLY" or "BIWEEKLY".
    day_of_week: "DayOfWeek" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateScheduledAuditResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_audit_arn",
                "scheduledAuditArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the scheduled audit.
    scheduled_audit_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateSecurityProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_profile_name",
                "securityProfileName",
                autoboto.TypeInfo(str),
            ),
            (
                "behaviors",
                "behaviors",
                autoboto.TypeInfo(typing.List[Behavior]),
            ),
            (
                "security_profile_description",
                "securityProfileDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "alert_targets",
                "alertTargets",
                autoboto.TypeInfo(typing.Dict[AlertTargetType, AlertTarget]),
            ),
        ]

    # The name you are giving to the security profile.
    security_profile_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the behaviors that, when violated by a device (thing), cause an
    # alert.
    behaviors: typing.List["Behavior"] = dataclasses.field(
        default_factory=list,
    )

    # A description of the security profile.
    security_profile_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the destinations to which alerts are sent. (Alerts are always
    # sent to the console.) Alerts are generated when a device (thing) violates a
    # behavior.
    alert_targets: typing.Dict["AlertTargetType", "AlertTarget"
                              ] = dataclasses.field(
                                  default=autoboto.ShapeBase._NOT_SET,
                              )


@dataclasses.dataclass
class CreateSecurityProfileResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_profile_name",
                "securityProfileName",
                autoboto.TypeInfo(str),
            ),
            (
                "security_profile_arn",
                "securityProfileArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name you gave to the security profile.
    security_profile_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the security profile.
    security_profile_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateStreamRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_id",
                "streamId",
                autoboto.TypeInfo(str),
            ),
            (
                "files",
                "files",
                autoboto.TypeInfo(typing.List[StreamFile]),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stream ID.
    stream_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The files to stream.
    files: typing.List["StreamFile"] = dataclasses.field(default_factory=list, )

    # An IAM role that allows the IoT service principal assumes to access your S3
    # files.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A description of the stream.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateStreamResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_id",
                "streamId",
                autoboto.TypeInfo(str),
            ),
            (
                "stream_arn",
                "streamArn",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "stream_version",
                "streamVersion",
                autoboto.TypeInfo(int),
            ),
        ]

    # The stream ID.
    stream_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The stream ARN.
    stream_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A description of the stream.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the stream.
    stream_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateThingGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_group_name",
                "thingGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "parent_group_name",
                "parentGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_group_properties",
                "thingGroupProperties",
                autoboto.TypeInfo(ThingGroupProperties),
            ),
        ]

    # The thing group name to create.
    thing_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the parent thing group.
    parent_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing group properties.
    thing_group_properties: "ThingGroupProperties" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateThingGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_group_name",
                "thingGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_group_arn",
                "thingGroupArn",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_group_id",
                "thingGroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The thing group name.
    thing_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing group ARN.
    thing_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing group ID.
    thing_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateThingRequest(autoboto.ShapeBase):
    """
    The input for the CreateThing operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_type_name",
                "thingTypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "attribute_payload",
                "attributePayload",
                autoboto.TypeInfo(AttributePayload),
            ),
        ]

    # The name of the thing to create.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the thing type associated with the new thing.
    thing_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The attribute payload, which consists of up to three name/value pairs in a
    # JSON document. For example:

    # `{\"attributes\":{\"string1\":\"string2\"}}`
    attribute_payload: "AttributePayload" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateThingResponse(autoboto.ShapeBase):
    """
    The output of the CreateThing operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_arn",
                "thingArn",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_id",
                "thingId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the new thing.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the new thing.
    thing_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The thing ID.
    thing_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateThingTypeRequest(autoboto.ShapeBase):
    """
    The input for the CreateThingType operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_type_name",
                "thingTypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_type_properties",
                "thingTypeProperties",
                autoboto.TypeInfo(ThingTypeProperties),
            ),
        ]

    # The name of the thing type.
    thing_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ThingTypeProperties for the thing type to create. It contains
    # information about the new thing type including a description, and a list of
    # searchable thing attribute names.
    thing_type_properties: "ThingTypeProperties" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateThingTypeResponse(autoboto.ShapeBase):
    """
    The output of the CreateThingType operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_type_name",
                "thingTypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_type_arn",
                "thingTypeArn",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_type_id",
                "thingTypeId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the thing type.
    thing_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the thing type.
    thing_type_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing type ID.
    thing_type_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateTopicRuleRequest(autoboto.ShapeBase):
    """
    The input for the CreateTopicRule operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_name",
                "ruleName",
                autoboto.TypeInfo(str),
            ),
            (
                "topic_rule_payload",
                "topicRulePayload",
                autoboto.TypeInfo(TopicRulePayload),
            ),
        ]

    # The name of the rule.
    rule_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The rule payload.
    topic_rule_payload: "TopicRulePayload" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CustomCodeSigning(autoboto.ShapeBase):
    """
    Describes a custom method used to code sign a file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "signature",
                "signature",
                autoboto.TypeInfo(CodeSigningSignature),
            ),
            (
                "certificate_chain",
                "certificateChain",
                autoboto.TypeInfo(CodeSigningCertificateChain),
            ),
            (
                "hash_algorithm",
                "hashAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "signature_algorithm",
                "signatureAlgorithm",
                autoboto.TypeInfo(str),
            ),
        ]

    # The signature for the file.
    signature: "CodeSigningSignature" = dataclasses.field(
        default_factory=dict,
    )

    # The certificate chain.
    certificate_chain: "CodeSigningCertificateChain" = dataclasses.field(
        default_factory=dict,
    )

    # The hash algorithm used to code sign the file.
    hash_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The signature algorithm used to code sign the file.
    signature_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class DayOfWeek(Enum):
    SUN = "SUN"
    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"


@dataclasses.dataclass
class DeleteAccountAuditConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delete_scheduled_audits",
                "deleteScheduledAudits",
                autoboto.TypeInfo(bool),
            ),
        ]

    # If true, all scheduled audits are deleted.
    delete_scheduled_audits: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteAccountAuditConfigurationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteAuthorizerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorizer_name",
                "authorizerName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the authorizer to delete.
    authorizer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteAuthorizerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteCACertificateRequest(autoboto.ShapeBase):
    """
    Input for the DeleteCACertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the certificate to delete. (The last part of the certificate ARN
    # contains the certificate ID.)
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteCACertificateResponse(autoboto.ShapeBase):
    """
    The output for the DeleteCACertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteCertificateRequest(autoboto.ShapeBase):
    """
    The input for the DeleteCertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "force_delete",
                "forceDelete",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the certificate. (The last part of the certificate ARN contains
    # the certificate ID.)
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Forces a certificate request to be deleted.
    force_delete: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteConflictException(autoboto.ShapeBase):
    """
    You can't delete the resource because it is attached to one or more resources.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteJobExecutionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_number",
                "executionNumber",
                autoboto.TypeInfo(int),
            ),
            (
                "force",
                "force",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the job whose execution on a particular device will be deleted.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the thing whose job execution will be deleted.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the job execution to be deleted. The `executionNumber` refers to
    # the execution of a particular job on a particular device.

    # Note that once a job execution is deleted, the `executionNumber` may be
    # reused by IoT, so be sure you get and use the correct value here.
    execution_number: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # (Optional) When true, you can delete a job execution which is
    # "IN_PROGRESS". Otherwise, you can only delete a job execution which is in a
    # terminal state ("SUCCEEDED", "FAILED", "REJECTED", "REMOVED" or "CANCELED")
    # or an exception will occur. The default is false.

    # Deleting a job execution which is "IN_PROGRESS", will cause the device to
    # be unable to access job information or update the job execution status. Use
    # caution and ensure that the device is able to recover to a valid state.
    force: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "force",
                "force",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the job to be deleted.

    # After a job deletion is completed, you may reuse this jobId when you create
    # a new job. However, this is not recommended, and you must ensure that your
    # devices are not using the jobId to refer to the deleted job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # (Optional) When true, you can delete a job which is "IN_PROGRESS".
    # Otherwise, you can only delete a job which is in a terminal state
    # ("COMPLETED" or "CANCELED") or an exception will occur. The default is
    # false.

    # Deleting a job which is "IN_PROGRESS", will cause a device which is
    # executing the job to be unable to access job information or update the job
    # execution status. Use caution and ensure that each device executing a job
    # which is deleted is able to recover to a valid state.
    force: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteOTAUpdateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ota_update_id",
                "otaUpdateId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The OTA update ID to delete.
    ota_update_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteOTAUpdateResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeletePolicyRequest(autoboto.ShapeBase):
    """
    The input for the DeletePolicy operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the policy to delete.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeletePolicyVersionRequest(autoboto.ShapeBase):
    """
    The input for the DeletePolicyVersion operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_version_id",
                "policyVersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the policy.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The policy version ID.
    policy_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteRegistrationCodeRequest(autoboto.ShapeBase):
    """
    The input for the DeleteRegistrationCode operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteRegistrationCodeResponse(autoboto.ShapeBase):
    """
    The output for the DeleteRegistrationCode operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteRoleAliasRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_alias",
                "roleAlias",
                autoboto.TypeInfo(str),
            ),
        ]

    # The role alias to delete.
    role_alias: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteRoleAliasResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteScheduledAuditRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_audit_name",
                "scheduledAuditName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the scheduled audit you want to delete.
    scheduled_audit_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteScheduledAuditResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteSecurityProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_profile_name",
                "securityProfileName",
                autoboto.TypeInfo(str),
            ),
            (
                "expected_version",
                "expectedVersion",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the security profile to be deleted.
    security_profile_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The expected version of the security profile. A new version is generated
    # whenever the security profile is updated. If you specify a value that is
    # different than the actual version, a `VersionConflictException` is thrown.
    expected_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteSecurityProfileResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteStreamRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_id",
                "streamId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stream ID.
    stream_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteStreamResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteThingGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_group_name",
                "thingGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "expected_version",
                "expectedVersion",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the thing group to delete.
    thing_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The expected version of the thing group to delete.
    expected_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteThingGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteThingRequest(autoboto.ShapeBase):
    """
    The input for the DeleteThing operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "expected_version",
                "expectedVersion",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the thing to delete.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The expected version of the thing record in the registry. If the version of
    # the record in the registry does not match the expected version specified in
    # the request, the `DeleteThing` request is rejected with a
    # `VersionConflictException`.
    expected_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteThingResponse(autoboto.ShapeBase):
    """
    The output of the DeleteThing operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteThingTypeRequest(autoboto.ShapeBase):
    """
    The input for the DeleteThingType operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_type_name",
                "thingTypeName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the thing type.
    thing_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteThingTypeResponse(autoboto.ShapeBase):
    """
    The output for the DeleteThingType operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteTopicRuleRequest(autoboto.ShapeBase):
    """
    The input for the DeleteTopicRule operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_name",
                "ruleName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the rule.
    rule_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteV2LoggingLevelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_type",
                "targetType",
                autoboto.TypeInfo(LogTargetType),
            ),
            (
                "target_name",
                "targetName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of resource for which you are configuring logging. Must be
    # `THING_Group`.
    target_type: "LogTargetType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the resource for which you are configuring logging.
    target_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Denied(autoboto.ShapeBase):
    """
    Contains information that denied the authorization.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "implicit_deny",
                "implicitDeny",
                autoboto.TypeInfo(ImplicitDeny),
            ),
            (
                "explicit_deny",
                "explicitDeny",
                autoboto.TypeInfo(ExplicitDeny),
            ),
        ]

    # Information that implicitly denies the authorization. When a policy doesn't
    # explicitly deny or allow an action on a resource it is considered an
    # implicit deny.
    implicit_deny: "ImplicitDeny" = dataclasses.field(default_factory=dict, )

    # Information that explicitly denies the authorization.
    explicit_deny: "ExplicitDeny" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeprecateThingTypeRequest(autoboto.ShapeBase):
    """
    The input for the DeprecateThingType operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_type_name",
                "thingTypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "undo_deprecate",
                "undoDeprecate",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the thing type to deprecate.
    thing_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether to undeprecate a deprecated thing type. If **true** , the thing
    # type will not be deprecated anymore and you can associate it with things.
    undo_deprecate: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeprecateThingTypeResponse(autoboto.ShapeBase):
    """
    The output for the DeprecateThingType operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeAccountAuditConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeAccountAuditConfigurationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "audit_notification_target_configurations",
                "auditNotificationTargetConfigurations",
                autoboto.TypeInfo(
                    typing.Dict[AuditNotificationType, AuditNotificationTarget]
                ),
            ),
            (
                "audit_check_configurations",
                "auditCheckConfigurations",
                autoboto.TypeInfo(typing.Dict[str, AuditCheckConfiguration]),
            ),
        ]

    # The ARN of the role that grants permission to AWS IoT to access information
    # about your devices, policies, certificates and other items as necessary
    # when performing an audit.

    # On the first call to `UpdateAccountAuditConfiguration` this parameter is
    # required.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information about the targets to which audit notifications are sent for
    # this account.
    audit_notification_target_configurations: typing.Dict[
        "AuditNotificationType", "AuditNotificationTarget"
    ] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Which audit checks are enabled and disabled for this account.
    audit_check_configurations: typing.Dict[
        str, "AuditCheckConfiguration"
    ] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeAuditTaskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the audit whose information you want to get.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeAuditTaskResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_status",
                "taskStatus",
                autoboto.TypeInfo(AuditTaskStatus),
            ),
            (
                "task_type",
                "taskType",
                autoboto.TypeInfo(AuditTaskType),
            ),
            (
                "task_start_time",
                "taskStartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "task_statistics",
                "taskStatistics",
                autoboto.TypeInfo(TaskStatistics),
            ),
            (
                "scheduled_audit_name",
                "scheduledAuditName",
                autoboto.TypeInfo(str),
            ),
            (
                "audit_details",
                "auditDetails",
                autoboto.TypeInfo(typing.Dict[str, AuditCheckDetails]),
            ),
        ]

    # The status of the audit: one of "IN_PROGRESS", "COMPLETED", "FAILED", or
    # "CANCELED".
    task_status: "AuditTaskStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of audit: "ON_DEMAND_AUDIT_TASK" or "SCHEDULED_AUDIT_TASK".
    task_type: "AuditTaskType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time the audit started.
    task_start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Statistical information about the audit.
    task_statistics: "TaskStatistics" = dataclasses.field(
        default_factory=dict,
    )

    # The name of the scheduled audit (only if the audit was a scheduled audit).
    scheduled_audit_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Detailed information about each check performed during this audit.
    audit_details: typing.Dict[str, "AuditCheckDetails"] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeAuthorizerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorizer_name",
                "authorizerName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the authorizer to describe.
    authorizer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeAuthorizerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorizer_description",
                "authorizerDescription",
                autoboto.TypeInfo(AuthorizerDescription),
            ),
        ]

    # The authorizer description.
    authorizer_description: "AuthorizerDescription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeCACertificateRequest(autoboto.ShapeBase):
    """
    The input for the DescribeCACertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The CA certificate identifier.
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeCACertificateResponse(autoboto.ShapeBase):
    """
    The output from the DescribeCACertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_description",
                "certificateDescription",
                autoboto.TypeInfo(CACertificateDescription),
            ),
            (
                "registration_config",
                "registrationConfig",
                autoboto.TypeInfo(RegistrationConfig),
            ),
        ]

    # The CA certificate description.
    certificate_description: "CACertificateDescription" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the registration configuration.
    registration_config: "RegistrationConfig" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeCertificateRequest(autoboto.ShapeBase):
    """
    The input for the DescribeCertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the certificate. (The last part of the certificate ARN contains
    # the certificate ID.)
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeCertificateResponse(autoboto.ShapeBase):
    """
    The output of the DescribeCertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_description",
                "certificateDescription",
                autoboto.TypeInfo(CertificateDescription),
            ),
        ]

    # The description of the certificate.
    certificate_description: "CertificateDescription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeDefaultAuthorizerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeDefaultAuthorizerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorizer_description",
                "authorizerDescription",
                autoboto.TypeInfo(AuthorizerDescription),
            ),
        ]

    # The default authorizer's description.
    authorizer_description: "AuthorizerDescription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeEndpointRequest(autoboto.ShapeBase):
    """
    The input for the DescribeEndpoint operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_type",
                "endpointType",
                autoboto.TypeInfo(str),
            ),
        ]

    # The endpoint type (such as `iot:Data`, `iot:CredentialProvider` and
    # `iot:Jobs`).
    endpoint_type: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeEndpointResponse(autoboto.ShapeBase):
    """
    The output from the DescribeEndpoint operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_address",
                "endpointAddress",
                autoboto.TypeInfo(str),
            ),
        ]

    # The endpoint. The format of the endpoint is as follows: _identifier_.iot.
    # _region_.amazonaws.com.
    endpoint_address: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeEventConfigurationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeEventConfigurationsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_configurations",
                "eventConfigurations",
                autoboto.TypeInfo(typing.Dict[EventType, Configuration]),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_date",
                "lastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The event configurations.
    event_configurations: typing.Dict["EventType", "Configuration"
                                     ] = dataclasses.field(
                                         default=autoboto.ShapeBase._NOT_SET,
                                     )

    # The creation date of the event configuration.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the event configurations were last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeIndexRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_name",
                "indexName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The index name.
    index_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeIndexResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_name",
                "indexName",
                autoboto.TypeInfo(str),
            ),
            (
                "index_status",
                "indexStatus",
                autoboto.TypeInfo(IndexStatus),
            ),
            (
                "schema",
                "schema",
                autoboto.TypeInfo(str),
            ),
        ]

    # The index name.
    index_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The index status.
    index_status: "IndexStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Contains a value that specifies the type of indexing performed. Valid
    # values are:

    #   1. REGISTRY – Your thing index will contain only registry data.

    #   2. REGISTRY_AND_SHADOW - Your thing index will contain registry and shadow data.
    schema: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeJobExecutionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_number",
                "executionNumber",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique identifier you assigned to this job when it was created.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the thing on which the job execution is running.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A string (consisting of the digits "0" through "9" which is used to specify
    # a particular job execution on a particular device.
    execution_number: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeJobExecutionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution",
                "execution",
                autoboto.TypeInfo(JobExecution),
            ),
        ]

    # Information about the job execution.
    execution: "JobExecution" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier you assigned to this job when it was created.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeJobResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_source",
                "documentSource",
                autoboto.TypeInfo(str),
            ),
            (
                "job",
                "job",
                autoboto.TypeInfo(Job),
            ),
        ]

    # An S3 link to the job document.
    document_source: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the job.
    job: "Job" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeRoleAliasRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_alias",
                "roleAlias",
                autoboto.TypeInfo(str),
            ),
        ]

    # The role alias to describe.
    role_alias: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeRoleAliasResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_alias_description",
                "roleAliasDescription",
                autoboto.TypeInfo(RoleAliasDescription),
            ),
        ]

    # The role alias description.
    role_alias_description: "RoleAliasDescription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeScheduledAuditRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_audit_name",
                "scheduledAuditName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the scheduled audit whose information you want to get.
    scheduled_audit_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeScheduledAuditResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "frequency",
                "frequency",
                autoboto.TypeInfo(AuditFrequency),
            ),
            (
                "day_of_month",
                "dayOfMonth",
                autoboto.TypeInfo(str),
            ),
            (
                "day_of_week",
                "dayOfWeek",
                autoboto.TypeInfo(DayOfWeek),
            ),
            (
                "target_check_names",
                "targetCheckNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "scheduled_audit_name",
                "scheduledAuditName",
                autoboto.TypeInfo(str),
            ),
            (
                "scheduled_audit_arn",
                "scheduledAuditArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # How often the scheduled audit takes place. One of "DAILY", "WEEKLY",
    # "BIWEEKLY" or "MONTHLY". The actual start time of each audit is determined
    # by the system.
    frequency: "AuditFrequency" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The day of the month on which the scheduled audit takes place. Will be "1"
    # through "31" or "LAST". If days 29-31 are specified, and the month does not
    # have that many days, the audit takes place on the "LAST" day of the month.
    day_of_month: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The day of the week on which the scheduled audit takes place. One of "SUN",
    # "MON", "TUE", "WED", "THU", "FRI" or "SAT".
    day_of_week: "DayOfWeek" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Which checks are performed during the scheduled audit. (Note that checks
    # must be enabled for your account. (Use `DescribeAccountAuditConfiguration`
    # to see the list of all checks including those that are enabled or
    # `UpdateAccountAuditConfiguration` to select which checks are enabled.)
    target_check_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The name of the scheduled audit.
    scheduled_audit_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the scheduled audit.
    scheduled_audit_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeSecurityProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_profile_name",
                "securityProfileName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the security profile whose information you want to get.
    security_profile_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeSecurityProfileResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_profile_name",
                "securityProfileName",
                autoboto.TypeInfo(str),
            ),
            (
                "security_profile_arn",
                "securityProfileArn",
                autoboto.TypeInfo(str),
            ),
            (
                "security_profile_description",
                "securityProfileDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "behaviors",
                "behaviors",
                autoboto.TypeInfo(typing.List[Behavior]),
            ),
            (
                "alert_targets",
                "alertTargets",
                autoboto.TypeInfo(typing.Dict[AlertTargetType, AlertTarget]),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(int),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_date",
                "lastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the security profile.
    security_profile_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the security profile.
    security_profile_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the security profile (associated with the security profile
    # when it was created or updated).
    security_profile_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the behaviors that, when violated by a device (thing), cause an
    # alert.
    behaviors: typing.List["Behavior"] = dataclasses.field(
        default_factory=list,
    )

    # Where the alerts are sent. (Alerts are always sent to the console.)
    alert_targets: typing.Dict["AlertTargetType", "AlertTarget"
                              ] = dataclasses.field(
                                  default=autoboto.ShapeBase._NOT_SET,
                              )

    # The version of the security profile. A new version is generated whenever
    # the security profile is updated.
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time the security profile was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time the security profile was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeStreamRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_id",
                "streamId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stream ID.
    stream_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeStreamResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_info",
                "streamInfo",
                autoboto.TypeInfo(StreamInfo),
            ),
        ]

    # Information about the stream.
    stream_info: "StreamInfo" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeThingGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_group_name",
                "thingGroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the thing group.
    thing_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeThingGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_group_name",
                "thingGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_group_id",
                "thingGroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_group_arn",
                "thingGroupArn",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(int),
            ),
            (
                "thing_group_properties",
                "thingGroupProperties",
                autoboto.TypeInfo(ThingGroupProperties),
            ),
            (
                "thing_group_metadata",
                "thingGroupMetadata",
                autoboto.TypeInfo(ThingGroupMetadata),
            ),
        ]

    # The name of the thing group.
    thing_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing group ID.
    thing_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing group ARN.
    thing_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The version of the thing group.
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The thing group properties.
    thing_group_properties: "ThingGroupProperties" = dataclasses.field(
        default_factory=dict,
    )

    # Thing group metadata.
    thing_group_metadata: "ThingGroupMetadata" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeThingRegistrationTaskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The task ID.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeThingRegistrationTaskResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_date",
                "lastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "template_body",
                "templateBody",
                autoboto.TypeInfo(str),
            ),
            (
                "input_file_bucket",
                "inputFileBucket",
                autoboto.TypeInfo(str),
            ),
            (
                "input_file_key",
                "inputFileKey",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(Status),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "success_count",
                "successCount",
                autoboto.TypeInfo(int),
            ),
            (
                "failure_count",
                "failureCount",
                autoboto.TypeInfo(int),
            ),
            (
                "percentage_progress",
                "percentageProgress",
                autoboto.TypeInfo(int),
            ),
        ]

    # The task ID.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The task creation date.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date when the task was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The task's template.
    template_body: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The S3 bucket that contains the input file.
    input_file_bucket: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The input file key.
    input_file_key: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The role ARN that grants access to the input file bucket.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the bulk thing provisioning task.
    status: "Status" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The message.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of things successfully provisioned.
    success_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of things that failed to be provisioned.
    failure_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The progress of the bulk provisioning task expressed as a percentage.
    percentage_progress: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeThingRequest(autoboto.ShapeBase):
    """
    The input for the DescribeThing operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the thing.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeThingResponse(autoboto.ShapeBase):
    """
    The output from the DescribeThing operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "default_client_id",
                "defaultClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_id",
                "thingId",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_arn",
                "thingArn",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_type_name",
                "thingTypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(int),
            ),
        ]

    # The default client ID.
    default_client_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the thing.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the thing to describe.
    thing_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the thing to describe.
    thing_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The thing type name.
    thing_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing attributes.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The current version of the thing record in the registry.

    # To avoid unintentional changes to the information in the registry, you can
    # pass the version information in the `expectedVersion` parameter of the
    # `UpdateThing` and `DeleteThing` calls.
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeThingTypeRequest(autoboto.ShapeBase):
    """
    The input for the DescribeThingType operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_type_name",
                "thingTypeName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the thing type.
    thing_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeThingTypeResponse(autoboto.ShapeBase):
    """
    The output for the DescribeThingType operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_type_name",
                "thingTypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_type_id",
                "thingTypeId",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_type_arn",
                "thingTypeArn",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_type_properties",
                "thingTypeProperties",
                autoboto.TypeInfo(ThingTypeProperties),
            ),
            (
                "thing_type_metadata",
                "thingTypeMetadata",
                autoboto.TypeInfo(ThingTypeMetadata),
            ),
        ]

    # The name of the thing type.
    thing_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing type ID.
    thing_type_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing type ARN.
    thing_type_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ThingTypeProperties contains information about the thing type including
    # description, and a list of searchable thing attribute names.
    thing_type_properties: "ThingTypeProperties" = dataclasses.field(
        default_factory=dict,
    )

    # The ThingTypeMetadata contains additional information about the thing type
    # including: creation date and time, a value indicating whether the thing
    # type is deprecated, and a date and time when it was deprecated.
    thing_type_metadata: "ThingTypeMetadata" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DetachPolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "target",
                "target",
                autoboto.TypeInfo(str),
            ),
        ]

    # The policy to detach.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The target from which the policy will be detached.
    target: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DetachPrincipalPolicyRequest(autoboto.ShapeBase):
    """
    The input for the DetachPrincipalPolicy operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "principal",
                "principal",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the policy to detach.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The principal.

    # If the principal is a certificate, specify the certificate ARN. If the
    # principal is an Amazon Cognito identity, specify the identity ID.
    principal: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DetachSecurityProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_profile_name",
                "securityProfileName",
                autoboto.TypeInfo(str),
            ),
            (
                "security_profile_target_arn",
                "securityProfileTargetArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The security profile that is detached.
    security_profile_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the thing group from which the security profile is detached.
    security_profile_target_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DetachSecurityProfileResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DetachThingPrincipalRequest(autoboto.ShapeBase):
    """
    The input for the DetachThingPrincipal operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "principal",
                "principal",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the thing.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If the principal is a certificate, this value must be ARN of the
    # certificate. If the principal is an Amazon Cognito identity, this value
    # must be the ID of the Amazon Cognito identity.
    principal: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DetachThingPrincipalResponse(autoboto.ShapeBase):
    """
    The output from the DetachThingPrincipal operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DisableTopicRuleRequest(autoboto.ShapeBase):
    """
    The input for the DisableTopicRuleRequest operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_name",
                "ruleName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the rule to disable.
    rule_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DynamoDBAction(autoboto.ShapeBase):
    """
    Describes an action to write to a DynamoDB table.

    The `tableName`, `hashKeyField`, and `rangeKeyField` values must match the
    values used when you created the table.

    The `hashKeyValue` and `rangeKeyvalue` fields use a substitution template
    syntax. These templates provide data at runtime. The syntax is as follows: ${
    _sql-expression_ }.

    You can specify any valid expression in a WHERE or SELECT clause, including JSON
    properties, comparisons, calculations, and functions. For example, the following
    field uses the third level of the topic:

    `"hashKeyValue": "${topic(3)}"`

    The following field uses the timestamp:

    `"rangeKeyValue": "${timestamp()}"`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "tableName",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "hash_key_field",
                "hashKeyField",
                autoboto.TypeInfo(str),
            ),
            (
                "hash_key_value",
                "hashKeyValue",
                autoboto.TypeInfo(str),
            ),
            (
                "operation",
                "operation",
                autoboto.TypeInfo(str),
            ),
            (
                "hash_key_type",
                "hashKeyType",
                autoboto.TypeInfo(DynamoKeyType),
            ),
            (
                "range_key_field",
                "rangeKeyField",
                autoboto.TypeInfo(str),
            ),
            (
                "range_key_value",
                "rangeKeyValue",
                autoboto.TypeInfo(str),
            ),
            (
                "range_key_type",
                "rangeKeyType",
                autoboto.TypeInfo(DynamoKeyType),
            ),
            (
                "payload_field",
                "payloadField",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the DynamoDB table.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the IAM role that grants access to the DynamoDB table.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The hash key name.
    hash_key_field: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The hash key value.
    hash_key_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of operation to be performed. This follows the substitution
    # template, so it can be `${operation}`, but the substitution must result in
    # one of the following: `INSERT`, `UPDATE`, or `DELETE`.
    operation: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The hash key type. Valid values are "STRING" or "NUMBER"
    hash_key_type: "DynamoKeyType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The range key name.
    range_key_field: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The range key value.
    range_key_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The range key type. Valid values are "STRING" or "NUMBER"
    range_key_type: "DynamoKeyType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The action payload. This name can be customized.
    payload_field: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DynamoDBv2Action(autoboto.ShapeBase):
    """
    Describes an action to write to a DynamoDB table.

    This DynamoDB action writes each attribute in the message payload into it's own
    column in the DynamoDB table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "put_item",
                "putItem",
                autoboto.TypeInfo(PutItemInput),
            ),
        ]

    # The ARN of the IAM role that grants access to the DynamoDB table.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the DynamoDB table to which the message data will be written. For
    # example:

    # `{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": {
    # "tableName": "my-table" } } }`

    # Each attribute in the message payload will be written to a separate column
    # in the DynamoDB database.
    put_item: "PutItemInput" = dataclasses.field(default_factory=dict, )


class DynamoKeyType(Enum):
    STRING = "STRING"
    NUMBER = "NUMBER"


@dataclasses.dataclass
class EffectivePolicy(autoboto.ShapeBase):
    """
    The policy that has the effect on the authorization results.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_arn",
                "policyArn",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_document",
                "policyDocument",
                autoboto.TypeInfo(str),
            ),
        ]

    # The policy name.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The policy ARN.
    policy_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The IAM policy document.
    policy_document: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ElasticsearchAction(autoboto.ShapeBase):
    """
    Describes an action that writes data to an Amazon Elasticsearch Service domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint",
                "endpoint",
                autoboto.TypeInfo(str),
            ),
            (
                "index",
                "index",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "type",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The IAM role ARN that has access to Elasticsearch.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The endpoint of your Elasticsearch domain.
    endpoint: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Elasticsearch index where you want to store your data.
    index: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of document you are storing.
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique identifier for the document you are storing.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EnableTopicRuleRequest(autoboto.ShapeBase):
    """
    The input for the EnableTopicRuleRequest operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_name",
                "ruleName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the topic rule to enable.
    rule_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ErrorInfo(autoboto.ShapeBase):
    """
    Error information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error code.
    code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The error message.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class EventType(Enum):
    THING = "THING"
    THING_GROUP = "THING_GROUP"
    THING_TYPE = "THING_TYPE"
    THING_GROUP_MEMBERSHIP = "THING_GROUP_MEMBERSHIP"
    THING_GROUP_HIERARCHY = "THING_GROUP_HIERARCHY"
    THING_TYPE_ASSOCIATION = "THING_TYPE_ASSOCIATION"
    JOB = "JOB"
    JOB_EXECUTION = "JOB_EXECUTION"
    POLICY = "POLICY"
    CERTIFICATE = "CERTIFICATE"
    CA_CERTIFICATE = "CA_CERTIFICATE"


@dataclasses.dataclass
class ExplicitDeny(autoboto.ShapeBase):
    """
    Information that explicitly denies authorization.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policies",
                "policies",
                autoboto.TypeInfo(typing.List[Policy]),
            ),
        ]

    # The policies that denied the authorization.
    policies: typing.List["Policy"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class FirehoseAction(autoboto.ShapeBase):
    """
    Describes an action that writes data to an Amazon Kinesis Firehose stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "delivery_stream_name",
                "deliveryStreamName",
                autoboto.TypeInfo(str),
            ),
            (
                "separator",
                "separator",
                autoboto.TypeInfo(str),
            ),
        ]

    # The IAM role that grants access to the Amazon Kinesis Firehose stream.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The delivery stream name.
    delivery_stream_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A character separator that will be used to separate records written to the
    # Firehose stream. Valid values are: '\n' (newline), '\t' (tab), '\r\n'
    # (Windows newline), ',' (comma).
    separator: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetEffectivePoliciesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "principal",
                "principal",
                autoboto.TypeInfo(str),
            ),
            (
                "cognito_identity_pool_id",
                "cognitoIdentityPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The principal.
    principal: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Cognito identity pool ID.
    cognito_identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing name.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetEffectivePoliciesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "effective_policies",
                "effectivePolicies",
                autoboto.TypeInfo(typing.List[EffectivePolicy]),
            ),
        ]

    # The effective policies.
    effective_policies: typing.List["EffectivePolicy"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetIndexingConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetIndexingConfigurationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_indexing_configuration",
                "thingIndexingConfiguration",
                autoboto.TypeInfo(ThingIndexingConfiguration),
            ),
            (
                "thing_group_indexing_configuration",
                "thingGroupIndexingConfiguration",
                autoboto.TypeInfo(ThingGroupIndexingConfiguration),
            ),
        ]

    # Thing indexing configuration.
    thing_indexing_configuration: "ThingIndexingConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The index configuration.
    thing_group_indexing_configuration: "ThingGroupIndexingConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetJobDocumentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier you assigned to this job when it was created.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetJobDocumentResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document",
                "document",
                autoboto.TypeInfo(str),
            ),
        ]

    # The job document content.
    document: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetLoggingOptionsRequest(autoboto.ShapeBase):
    """
    The input for the GetLoggingOptions operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetLoggingOptionsResponse(autoboto.ShapeBase):
    """
    The output from the GetLoggingOptions operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "log_level",
                "logLevel",
                autoboto.TypeInfo(LogLevel),
            ),
        ]

    # The ARN of the IAM role that grants access.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The logging level.
    log_level: "LogLevel" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetOTAUpdateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ota_update_id",
                "otaUpdateId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The OTA update ID.
    ota_update_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetOTAUpdateResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ota_update_info",
                "otaUpdateInfo",
                autoboto.TypeInfo(OTAUpdateInfo),
            ),
        ]

    # The OTA update info.
    ota_update_info: "OTAUpdateInfo" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetPolicyRequest(autoboto.ShapeBase):
    """
    The input for the GetPolicy operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the policy.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetPolicyResponse(autoboto.ShapeBase):
    """
    The output from the GetPolicy operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_arn",
                "policyArn",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_document",
                "policyDocument",
                autoboto.TypeInfo(str),
            ),
            (
                "default_version_id",
                "defaultVersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_date",
                "lastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "generation_id",
                "generationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The policy name.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The policy ARN.
    policy_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The JSON document that describes the policy.
    policy_document: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default policy version ID.
    default_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the policy was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the policy was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The generation ID of the policy.
    generation_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetPolicyVersionRequest(autoboto.ShapeBase):
    """
    The input for the GetPolicyVersion operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_version_id",
                "policyVersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the policy.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The policy version ID.
    policy_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetPolicyVersionResponse(autoboto.ShapeBase):
    """
    The output from the GetPolicyVersion operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_arn",
                "policyArn",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_document",
                "policyDocument",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_version_id",
                "policyVersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "is_default_version",
                "isDefaultVersion",
                autoboto.TypeInfo(bool),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_date",
                "lastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "generation_id",
                "generationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The policy ARN.
    policy_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The policy name.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The JSON document that describes the policy.
    policy_document: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The policy version ID.
    policy_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether the policy version is the default.
    is_default_version: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the policy version was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the policy version was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The generation ID of the policy version.
    generation_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetRegistrationCodeRequest(autoboto.ShapeBase):
    """
    The input to the GetRegistrationCode operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetRegistrationCodeResponse(autoboto.ShapeBase):
    """
    The output from the GetRegistrationCode operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registration_code",
                "registrationCode",
                autoboto.TypeInfo(str),
            ),
        ]

    # The CA certificate registration code.
    registration_code: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetTopicRuleRequest(autoboto.ShapeBase):
    """
    The input for the GetTopicRule operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_name",
                "ruleName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the rule.
    rule_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetTopicRuleResponse(autoboto.ShapeBase):
    """
    The output from the GetTopicRule operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_arn",
                "ruleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "rule",
                "rule",
                autoboto.TypeInfo(TopicRule),
            ),
        ]

    # The rule ARN.
    rule_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The rule.
    rule: "TopicRule" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetV2LoggingOptionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetV2LoggingOptionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "default_log_level",
                "defaultLogLevel",
                autoboto.TypeInfo(LogLevel),
            ),
            (
                "disable_all_logs",
                "disableAllLogs",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The IAM role ARN AWS IoT uses to write to your CloudWatch logs.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The default log level.
    default_log_level: "LogLevel" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Disables all logs.
    disable_all_logs: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GroupNameAndArn(autoboto.ShapeBase):
    """
    The name and ARN of a group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "groupName",
                autoboto.TypeInfo(str),
            ),
            (
                "group_arn",
                "groupArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The group name.
    group_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The group ARN.
    group_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ImplicitDeny(autoboto.ShapeBase):
    """
    Information that implicitly denies authorization. When policy doesn't explicitly
    deny or allow an action on a resource it is considered an implicit deny.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policies",
                "policies",
                autoboto.TypeInfo(typing.List[Policy]),
            ),
        ]

    # Policies that don't contain a matching allow or deny statement for the
    # specified action on the specified resource.
    policies: typing.List["Policy"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class IndexNotReadyException(autoboto.ShapeBase):
    """
    The index is not ready.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class IndexStatus(Enum):
    ACTIVE = "ACTIVE"
    BUILDING = "BUILDING"
    REBUILDING = "REBUILDING"


@dataclasses.dataclass
class InternalException(autoboto.ShapeBase):
    """
    An unexpected error has occurred.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InternalFailureException(autoboto.ShapeBase):
    """
    An unexpected error has occurred.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidQueryException(autoboto.ShapeBase):
    """
    The query is invalid.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidRequestException(autoboto.ShapeBase):
    """
    The request is not valid.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidResponseException(autoboto.ShapeBase):
    """
    The response is invalid.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidStateTransitionException(autoboto.ShapeBase):
    """
    An attempt was made to change to an invalid state, for example by deleting a job
    or a job execution which is "IN_PROGRESS" without setting the `force` parameter.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class IotAnalyticsAction(autoboto.ShapeBase):
    """
    Sends messge data to an AWS IoT Analytics channel.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_arn",
                "channelArn",
                autoboto.TypeInfo(str),
            ),
            (
                "channel_name",
                "channelName",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # (deprecated) The ARN of the IoT Analytics channel to which message data
    # will be sent.
    channel_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the IoT Analytics channel to which message data will be sent.
    channel_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the role which has a policy that grants IoT Analytics permission
    # to send message data via IoT Analytics (iotanalytics:BatchPutMessage).
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Job(autoboto.ShapeBase):
    """
    The `Job` object contains details about a job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_arn",
                "jobArn",
                autoboto.TypeInfo(str),
            ),
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "target_selection",
                "targetSelection",
                autoboto.TypeInfo(TargetSelection),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(JobStatus),
            ),
            (
                "force_canceled",
                "forceCanceled",
                autoboto.TypeInfo(bool),
            ),
            (
                "comment",
                "comment",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "targets",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "presigned_url_config",
                "presignedUrlConfig",
                autoboto.TypeInfo(PresignedUrlConfig),
            ),
            (
                "job_executions_rollout_config",
                "jobExecutionsRolloutConfig",
                autoboto.TypeInfo(JobExecutionsRolloutConfig),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_at",
                "lastUpdatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "completed_at",
                "completedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "job_process_details",
                "jobProcessDetails",
                autoboto.TypeInfo(JobProcessDetails),
            ),
        ]

    # An ARN identifying the job with format
    # "arn:aws:iot:region:account:job/jobId".
    job_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique identifier you assigned to this job when it was created.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies whether the job will continue to run (CONTINUOUS), or will be
    # complete after all those things specified as targets have completed the job
    # (SNAPSHOT). If continuous, the job may also be run on a thing when a change
    # is detected in a target. For example, a job will run on a device when the
    # thing representing the device is added to a target group, even after the
    # job was completed by all things originally in the group.
    target_selection: "TargetSelection" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the job, one of `IN_PROGRESS`, `CANCELED`, or `COMPLETED`.
    status: "JobStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Will be `true` if the job was canceled with the optional `force` parameter
    # set to `true`.
    force_canceled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the job was updated, describes the reason for the update.
    comment: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of IoT things and thing groups to which the job should be sent.
    targets: typing.List[str] = dataclasses.field(default_factory=list, )

    # A short text description of the job.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Configuration for pre-signed S3 URLs.
    presigned_url_config: "PresignedUrlConfig" = dataclasses.field(
        default_factory=dict,
    )

    # Allows you to create a staged rollout of a job.
    job_executions_rollout_config: "JobExecutionsRolloutConfig" = dataclasses.field(
        default_factory=dict,
    )

    # The time, in milliseconds since the epoch, when the job was created.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time, in milliseconds since the epoch, when the job was last updated.
    last_updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time, in milliseconds since the epoch, when the job was completed.
    completed_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Details about the job process.
    job_process_details: "JobProcessDetails" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class JobExecution(autoboto.ShapeBase):
    """
    The job execution object represents the execution of a job on a particular
    device.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(JobExecutionStatus),
            ),
            (
                "force_canceled",
                "forceCanceled",
                autoboto.TypeInfo(bool),
            ),
            (
                "status_details",
                "statusDetails",
                autoboto.TypeInfo(JobExecutionStatusDetails),
            ),
            (
                "thing_arn",
                "thingArn",
                autoboto.TypeInfo(str),
            ),
            (
                "queued_at",
                "queuedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "started_at",
                "startedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_at",
                "lastUpdatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "execution_number",
                "executionNumber",
                autoboto.TypeInfo(int),
            ),
            (
                "version_number",
                "versionNumber",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique identifier you assigned to the job when it was created.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the job execution (IN_PROGRESS, QUEUED, FAILED, SUCCESS,
    # CANCELED, or REJECTED).
    status: "JobExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Will be `true` if the job execution was canceled with the optional `force`
    # parameter set to `true`.
    force_canceled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A collection of name/value pairs that describe the status of the job
    # execution.
    status_details: "JobExecutionStatusDetails" = dataclasses.field(
        default_factory=dict,
    )

    # The ARN of the thing on which the job execution is running.
    thing_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time, in milliseconds since the epoch, when the job execution was
    # queued.
    queued_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time, in milliseconds since the epoch, when the job execution started.
    started_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time, in milliseconds since the epoch, when the job execution was last
    # updated.
    last_updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A string (consisting of the digits "0" through "9") which identifies this
    # particular job execution on this particular device. It can be used in
    # commands which return or update job execution information.
    execution_number: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The version of the job execution. Job execution versions are incremented
    # each time they are updated by a device.
    version_number: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class JobExecutionStatus(Enum):
    QUEUED = "QUEUED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    REJECTED = "REJECTED"
    REMOVED = "REMOVED"
    CANCELED = "CANCELED"


@dataclasses.dataclass
class JobExecutionStatusDetails(autoboto.ShapeBase):
    """
    Details of the job execution status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "details_map",
                "detailsMap",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The job execution status.
    details_map: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class JobExecutionSummary(autoboto.ShapeBase):
    """
    The job execution summary.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "status",
                autoboto.TypeInfo(JobExecutionStatus),
            ),
            (
                "queued_at",
                "queuedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "started_at",
                "startedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_at",
                "lastUpdatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "execution_number",
                "executionNumber",
                autoboto.TypeInfo(int),
            ),
        ]

    # The status of the job execution.
    status: "JobExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time, in milliseconds since the epoch, when the job execution was
    # queued.
    queued_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time, in milliseconds since the epoch, when the job execution started.
    started_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time, in milliseconds since the epoch, when the job execution was last
    # updated.
    last_updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A string (consisting of the digits "0" through "9") which identifies this
    # particular job execution on this particular device. It can be used later in
    # commands which return or update job execution information.
    execution_number: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class JobExecutionSummaryForJob(autoboto.ShapeBase):
    """
    Contains a summary of information about job executions for a specific job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_arn",
                "thingArn",
                autoboto.TypeInfo(str),
            ),
            (
                "job_execution_summary",
                "jobExecutionSummary",
                autoboto.TypeInfo(JobExecutionSummary),
            ),
        ]

    # The ARN of the thing on which the job execution is running.
    thing_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Contains a subset of information about a job execution.
    job_execution_summary: "JobExecutionSummary" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class JobExecutionSummaryForThing(autoboto.ShapeBase):
    """
    The job execution summary for a thing.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "job_execution_summary",
                "jobExecutionSummary",
                autoboto.TypeInfo(JobExecutionSummary),
            ),
        ]

    # The unique identifier you assigned to this job when it was created.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Contains a subset of information about a job execution.
    job_execution_summary: "JobExecutionSummary" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class JobExecutionsRolloutConfig(autoboto.ShapeBase):
    """
    Allows you to create a staged rollout of a job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "maximum_per_minute",
                "maximumPerMinute",
                autoboto.TypeInfo(int),
            ),
        ]

    # The maximum number of things that will be notified of a pending job, per
    # minute. This parameter allows you to create a staged rollout.
    maximum_per_minute: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class JobProcessDetails(autoboto.ShapeBase):
    """
    The job process details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "processing_targets",
                "processingTargets",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "number_of_canceled_things",
                "numberOfCanceledThings",
                autoboto.TypeInfo(int),
            ),
            (
                "number_of_succeeded_things",
                "numberOfSucceededThings",
                autoboto.TypeInfo(int),
            ),
            (
                "number_of_failed_things",
                "numberOfFailedThings",
                autoboto.TypeInfo(int),
            ),
            (
                "number_of_rejected_things",
                "numberOfRejectedThings",
                autoboto.TypeInfo(int),
            ),
            (
                "number_of_queued_things",
                "numberOfQueuedThings",
                autoboto.TypeInfo(int),
            ),
            (
                "number_of_in_progress_things",
                "numberOfInProgressThings",
                autoboto.TypeInfo(int),
            ),
            (
                "number_of_removed_things",
                "numberOfRemovedThings",
                autoboto.TypeInfo(int),
            ),
        ]

    # The target devices to which the job execution is being rolled out. This
    # value will be null after the job execution has finished rolling out to all
    # the target devices.
    processing_targets: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The number of things that cancelled the job.
    number_of_canceled_things: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of things which successfully completed the job.
    number_of_succeeded_things: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of things that failed executing the job.
    number_of_failed_things: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of things that rejected the job.
    number_of_rejected_things: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of things that are awaiting execution of the job.
    number_of_queued_things: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of things currently executing the job.
    number_of_in_progress_things: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of things that are no longer scheduled to execute the job
    # because they have been deleted or have been removed from the group that was
    # a target of the job.
    number_of_removed_things: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class JobStatus(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    CANCELED = "CANCELED"
    COMPLETED = "COMPLETED"
    DELETION_IN_PROGRESS = "DELETION_IN_PROGRESS"


@dataclasses.dataclass
class JobSummary(autoboto.ShapeBase):
    """
    The job summary.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_arn",
                "jobArn",
                autoboto.TypeInfo(str),
            ),
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_group_id",
                "thingGroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "target_selection",
                "targetSelection",
                autoboto.TypeInfo(TargetSelection),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(JobStatus),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_at",
                "lastUpdatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "completed_at",
                "completedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The job ARN.
    job_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique identifier you assigned to this job when it was created.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the thing group.
    thing_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether the job will continue to run (CONTINUOUS), or will be
    # complete after all those things specified as targets have completed the job
    # (SNAPSHOT). If continuous, the job may also be run on a thing when a change
    # is detected in a target. For example, a job will run on a thing when the
    # thing is added to a target group, even after the job was completed by all
    # things originally in the group.
    target_selection: "TargetSelection" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The job summary status.
    status: "JobStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time, in milliseconds since the epoch, when the job was created.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time, in milliseconds since the epoch, when the job was last updated.
    last_updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time, in milliseconds since the epoch, when the job completed.
    completed_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class KeyPair(autoboto.ShapeBase):
    """
    Describes a key pair.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "public_key",
                "PublicKey",
                autoboto.TypeInfo(str),
            ),
            (
                "private_key",
                "PrivateKey",
                autoboto.TypeInfo(str),
            ),
        ]

    # The public key.
    public_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The private key.
    private_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class KinesisAction(autoboto.ShapeBase):
    """
    Describes an action to write data to an Amazon Kinesis stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "stream_name",
                "streamName",
                autoboto.TypeInfo(str),
            ),
            (
                "partition_key",
                "partitionKey",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the IAM role that grants access to the Amazon Kinesis stream.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the Amazon Kinesis stream.
    stream_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The partition key.
    partition_key: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class LambdaAction(autoboto.ShapeBase):
    """
    Describes an action to invoke a Lambda function.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_arn",
                "functionArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the Lambda function.
    function_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    A limit has been exceeded.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListActiveViolationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "security_profile_name",
                "securityProfileName",
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

    # The name of the thing whose active violations are listed.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the Device Defender security profile for which violations are
    # listed.
    security_profile_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return at one time.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListActiveViolationsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "active_violations",
                "activeViolations",
                autoboto.TypeInfo(typing.List[ActiveViolation]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of active violations.
    active_violations: typing.List["ActiveViolation"] = dataclasses.field(
        default_factory=list,
    )

    # A token that can be used to retrieve the next set of results, or `null` if
    # there are no additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListAttachedPoliciesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target",
                "target",
                autoboto.TypeInfo(str),
            ),
            (
                "recursive",
                "recursive",
                autoboto.TypeInfo(bool),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "pageSize",
                autoboto.TypeInfo(int),
            ),
        ]

    # The group for which the policies will be listed.
    target: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # When true, recursively list attached policies.
    recursive: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token to retrieve the next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to be returned per request.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListAttachedPoliciesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policies",
                "policies",
                autoboto.TypeInfo(typing.List[Policy]),
            ),
            (
                "next_marker",
                "nextMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The policies.
    policies: typing.List["Policy"] = dataclasses.field(default_factory=list, )

    # The token to retrieve the next set of results, or ``null`` if there are no
    # more results.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListAuditFindingsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                autoboto.TypeInfo(str),
            ),
            (
                "check_name",
                "checkName",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_identifier",
                "resourceIdentifier",
                autoboto.TypeInfo(ResourceIdentifier),
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

    # A filter to limit results to the audit with the specified ID. You must
    # specify either the taskId or the startTime and endTime, but not both.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A filter to limit results to the findings for the specified audit check.
    check_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information identifying the non-compliant resource.
    resource_identifier: "ResourceIdentifier" = dataclasses.field(
        default_factory=dict,
    )

    # The maximum number of results to return at one time. The default is 25.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A filter to limit results to those found after the specified time. You must
    # specify either the startTime and endTime or the taskId, but not both.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A filter to limit results to those found before the specified time. You
    # must specify either the startTime and endTime or the taskId, but not both.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListAuditFindingsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "findings",
                "findings",
                autoboto.TypeInfo(typing.List[AuditFinding]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The findings (results) of the audit.
    findings: typing.List["AuditFinding"] = dataclasses.field(
        default_factory=list,
    )

    # A token that can be used to retrieve the next set of results, or `null` if
    # there are no additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListAuditTasksRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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
            (
                "task_type",
                "taskType",
                autoboto.TypeInfo(AuditTaskType),
            ),
            (
                "task_status",
                "taskStatus",
                autoboto.TypeInfo(AuditTaskStatus),
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

    # The beginning of the time period. Note that audit information is retained
    # for a limited time (180 days). Requesting a start time prior to what is
    # retained results in an "InvalidRequestException".
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The end of the time period.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A filter to limit the output to the specified type of audit: can be one of
    # "ON_DEMAND_AUDIT_TASK" or "SCHEDULED__AUDIT_TASK".
    task_type: "AuditTaskType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A filter to limit the output to audits with the specified completion
    # status: can be one of "IN_PROGRESS", "COMPLETED", "FAILED" or "CANCELED".
    task_status: "AuditTaskStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return at one time. The default is 25.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListAuditTasksResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tasks",
                "tasks",
                autoboto.TypeInfo(typing.List[AuditTaskMetadata]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The audits that were performed during the specified time period.
    tasks: typing.List["AuditTaskMetadata"] = dataclasses.field(
        default_factory=list,
    )

    # A token that can be used to retrieve the next set of results, or `null` if
    # there are no additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListAuthorizersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_size",
                "pageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "ascending_order",
                "ascendingOrder",
                autoboto.TypeInfo(bool),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(AuthorizerStatus),
            ),
        ]

    # The maximum number of results to return at one time.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A marker used to get the next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Return the list of authorizers in ascending alphabetical order.
    ascending_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the list authorizers request.
    status: "AuthorizerStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListAuthorizersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorizers",
                "authorizers",
                autoboto.TypeInfo(typing.List[AuthorizerSummary]),
            ),
            (
                "next_marker",
                "nextMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The authorizers.
    authorizers: typing.List["AuthorizerSummary"] = dataclasses.field(
        default_factory=list,
    )

    # A marker used to get the next set of results.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListCACertificatesRequest(autoboto.ShapeBase):
    """
    Input for the ListCACertificates operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_size",
                "pageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "ascending_order",
                "ascendingOrder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The result page size.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The marker for the next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Determines the order of the results.
    ascending_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListCACertificatesResponse(autoboto.ShapeBase):
    """
    The output from the ListCACertificates operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificates",
                "certificates",
                autoboto.TypeInfo(typing.List[CACertificate]),
            ),
            (
                "next_marker",
                "nextMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The CA certificates registered in your AWS account.
    certificates: typing.List["CACertificate"] = dataclasses.field(
        default_factory=list,
    )

    # The current position within the list of CA certificates.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListCertificatesByCARequest(autoboto.ShapeBase):
    """
    The input to the ListCertificatesByCA operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ca_certificate_id",
                "caCertificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "pageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "ascending_order",
                "ascendingOrder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the CA certificate. This operation will list all registered
    # device certificate that were signed by this CA certificate.
    ca_certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The result page size.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The marker for the next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the order for results. If True, the results are returned in
    # ascending order, based on the creation date.
    ascending_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListCertificatesByCAResponse(autoboto.ShapeBase):
    """
    The output of the ListCertificatesByCA operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificates",
                "certificates",
                autoboto.TypeInfo(typing.List[Certificate]),
            ),
            (
                "next_marker",
                "nextMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The device certificates signed by the specified CA certificate.
    certificates: typing.List["Certificate"] = dataclasses.field(
        default_factory=list,
    )

    # The marker for the next set of results, or null if there are no additional
    # results.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListCertificatesRequest(autoboto.ShapeBase):
    """
    The input for the ListCertificates operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_size",
                "pageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "ascending_order",
                "ascendingOrder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The result page size.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The marker for the next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the order for results. If True, the results are returned in
    # ascending order, based on the creation date.
    ascending_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListCertificatesResponse(autoboto.ShapeBase):
    """
    The output of the ListCertificates operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificates",
                "certificates",
                autoboto.TypeInfo(typing.List[Certificate]),
            ),
            (
                "next_marker",
                "nextMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The descriptions of the certificates.
    certificates: typing.List["Certificate"] = dataclasses.field(
        default_factory=list,
    )

    # The marker for the next set of results, or null if there are no additional
    # results.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListIndicesRequest(autoboto.ShapeBase):
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

    # The token used to get the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return at one time.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListIndicesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_names",
                "indexNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The index names.
    index_names: typing.List[str] = dataclasses.field(default_factory=list, )

    # The token used to get the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListJobExecutionsForJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(JobExecutionStatus),
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

    # The unique identifier you assigned to this job when it was created.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the job.
    status: "JobExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results to be returned per request.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListJobExecutionsForJobResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution_summaries",
                "executionSummaries",
                autoboto.TypeInfo(typing.List[JobExecutionSummaryForJob]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of job execution summaries.
    execution_summaries: typing.List["JobExecutionSummaryForJob"
                                    ] = dataclasses.field(
                                        default_factory=list,
                                    )

    # The token for the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListJobExecutionsForThingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(JobExecutionStatus),
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

    # The thing name.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An optional filter that lets you search for jobs that have the specified
    # status.
    status: "JobExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results to be returned per request.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListJobExecutionsForThingResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution_summaries",
                "executionSummaries",
                autoboto.TypeInfo(typing.List[JobExecutionSummaryForThing]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of job execution summaries.
    execution_summaries: typing.List["JobExecutionSummaryForThing"
                                    ] = dataclasses.field(
                                        default_factory=list,
                                    )

    # The token for the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListJobsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "status",
                autoboto.TypeInfo(JobStatus),
            ),
            (
                "target_selection",
                "targetSelection",
                autoboto.TypeInfo(TargetSelection),
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
                "thing_group_name",
                "thingGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_group_id",
                "thingGroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # An optional filter that lets you search for jobs that have the specified
    # status.
    status: "JobStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether the job will continue to run (CONTINUOUS), or will be
    # complete after all those things specified as targets have completed the job
    # (SNAPSHOT). If continuous, the job may also be run on a thing when a change
    # is detected in a target. For example, a job will run on a thing when the
    # thing is added to a target group, even after the job was completed by all
    # things originally in the group.
    target_selection: "TargetSelection" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results to return per request.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A filter that limits the returned jobs to those for the specified group.
    thing_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A filter that limits the returned jobs to those for the specified group.
    thing_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListJobsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "jobs",
                "jobs",
                autoboto.TypeInfo(typing.List[JobSummary]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of jobs.
    jobs: typing.List["JobSummary"] = dataclasses.field(default_factory=list, )

    # The token for the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListOTAUpdatesRequest(autoboto.ShapeBase):
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
            (
                "ota_update_status",
                "otaUpdateStatus",
                autoboto.TypeInfo(OTAUpdateStatus),
            ),
        ]

    # The maximum number of results to return at one time.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A token used to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The OTA update job status.
    ota_update_status: "OTAUpdateStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListOTAUpdatesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ota_updates",
                "otaUpdates",
                autoboto.TypeInfo(typing.List[OTAUpdateSummary]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of OTA update jobs.
    ota_updates: typing.List["OTAUpdateSummary"] = dataclasses.field(
        default_factory=list,
    )

    # A token to use to get the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListOutgoingCertificatesRequest(autoboto.ShapeBase):
    """
    The input to the ListOutgoingCertificates operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_size",
                "pageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "ascending_order",
                "ascendingOrder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The result page size.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The marker for the next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the order for results. If True, the results are returned in
    # ascending order, based on the creation date.
    ascending_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListOutgoingCertificatesResponse(autoboto.ShapeBase):
    """
    The output from the ListOutgoingCertificates operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "outgoing_certificates",
                "outgoingCertificates",
                autoboto.TypeInfo(typing.List[OutgoingCertificate]),
            ),
            (
                "next_marker",
                "nextMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The certificates that are being transferred but not yet accepted.
    outgoing_certificates: typing.List["OutgoingCertificate"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )

    # The marker for the next set of results.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListPoliciesRequest(autoboto.ShapeBase):
    """
    The input for the ListPolicies operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "pageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "ascending_order",
                "ascendingOrder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The marker for the next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The result page size.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the order for results. If true, the results are returned in
    # ascending creation order.
    ascending_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListPoliciesResponse(autoboto.ShapeBase):
    """
    The output from the ListPolicies operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policies",
                "policies",
                autoboto.TypeInfo(typing.List[Policy]),
            ),
            (
                "next_marker",
                "nextMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The descriptions of the policies.
    policies: typing.List["Policy"] = dataclasses.field(default_factory=list, )

    # The marker for the next set of results, or null if there are no additional
    # results.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListPolicyPrincipalsRequest(autoboto.ShapeBase):
    """
    The input for the ListPolicyPrincipals operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "pageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "ascending_order",
                "ascendingOrder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The policy name.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The marker for the next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The result page size.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the order for results. If true, the results are returned in
    # ascending creation order.
    ascending_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListPolicyPrincipalsResponse(autoboto.ShapeBase):
    """
    The output from the ListPolicyPrincipals operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "principals",
                "principals",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_marker",
                "nextMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The descriptions of the principals.
    principals: typing.List[str] = dataclasses.field(default_factory=list, )

    # The marker for the next set of results, or null if there are no additional
    # results.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListPolicyVersionsRequest(autoboto.ShapeBase):
    """
    The input for the ListPolicyVersions operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The policy name.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListPolicyVersionsResponse(autoboto.ShapeBase):
    """
    The output from the ListPolicyVersions operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_versions",
                "policyVersions",
                autoboto.TypeInfo(typing.List[PolicyVersion]),
            ),
        ]

    # The policy versions.
    policy_versions: typing.List["PolicyVersion"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListPrincipalPoliciesRequest(autoboto.ShapeBase):
    """
    The input for the ListPrincipalPolicies operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "principal",
                "principal",
                autoboto.TypeInfo(str),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "pageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "ascending_order",
                "ascendingOrder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The principal.
    principal: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The marker for the next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The result page size.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the order for results. If true, results are returned in ascending
    # creation order.
    ascending_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListPrincipalPoliciesResponse(autoboto.ShapeBase):
    """
    The output from the ListPrincipalPolicies operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policies",
                "policies",
                autoboto.TypeInfo(typing.List[Policy]),
            ),
            (
                "next_marker",
                "nextMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The policies.
    policies: typing.List["Policy"] = dataclasses.field(default_factory=list, )

    # The marker for the next set of results, or null if there are no additional
    # results.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListPrincipalThingsRequest(autoboto.ShapeBase):
    """
    The input for the ListPrincipalThings operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "principal",
                "principal",
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

    # The principal.
    principal: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return in this operation.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListPrincipalThingsResponse(autoboto.ShapeBase):
    """
    The output from the ListPrincipalThings operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "things",
                "things",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The things.
    things: typing.List[str] = dataclasses.field(default_factory=list, )

    # The token used to get the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListRoleAliasesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_size",
                "pageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "ascending_order",
                "ascendingOrder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The maximum number of results to return at one time.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A marker used to get the next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Return the list of role aliases in ascending alphabetical order.
    ascending_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListRoleAliasesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_aliases",
                "roleAliases",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_marker",
                "nextMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The role aliases.
    role_aliases: typing.List[str] = dataclasses.field(default_factory=list, )

    # A marker used to get the next set of results.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListScheduledAuditsRequest(autoboto.ShapeBase):
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

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return at one time. The default is 25.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListScheduledAuditsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_audits",
                "scheduledAudits",
                autoboto.TypeInfo(typing.List[ScheduledAuditMetadata]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of scheduled audits.
    scheduled_audits: typing.List["ScheduledAuditMetadata"] = dataclasses.field(
        default_factory=list,
    )

    # A token that can be used to retrieve the next set of results, or `null` if
    # there are no additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListSecurityProfilesForTargetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_profile_target_arn",
                "securityProfileTargetArn",
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
            (
                "recursive",
                "recursive",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ARN of the target (thing group) whose attached security profiles you
    # want to get.
    security_profile_target_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return at one time.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If true, return child groups as well.
    recursive: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListSecurityProfilesForTargetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_profile_target_mappings",
                "securityProfileTargetMappings",
                autoboto.TypeInfo(typing.List[SecurityProfileTargetMapping]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of security profiles and their associated targets.
    security_profile_target_mappings: typing.List["SecurityProfileTargetMapping"
                                                 ] = dataclasses.field(
                                                     default_factory=list,
                                                 )

    # A token that can be used to retrieve the next set of results, or `null` if
    # there are no additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListSecurityProfilesRequest(autoboto.ShapeBase):
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

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return at one time.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListSecurityProfilesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_profile_identifiers",
                "securityProfileIdentifiers",
                autoboto.TypeInfo(typing.List[SecurityProfileIdentifier]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of security profile identifiers (names and ARNs).
    security_profile_identifiers: typing.List["SecurityProfileIdentifier"
                                             ] = dataclasses.field(
                                                 default_factory=list,
                                             )

    # A token that can be used to retrieve the next set of results, or `null` if
    # there are no additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListStreamsRequest(autoboto.ShapeBase):
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
            (
                "ascending_order",
                "ascendingOrder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The maximum number of results to return at a time.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A token used to get the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Set to true to return the list of streams in ascending order.
    ascending_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListStreamsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "streams",
                "streams",
                autoboto.TypeInfo(typing.List[StreamSummary]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of streams.
    streams: typing.List["StreamSummary"] = dataclasses.field(
        default_factory=list,
    )

    # A token used to get the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListTargetsForPolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "pageSize",
                autoboto.TypeInfo(int),
            ),
        ]

    # The policy name.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A marker used to get the next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return at one time.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListTargetsForPolicyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "targets",
                "targets",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_marker",
                "nextMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The policy targets.
    targets: typing.List[str] = dataclasses.field(default_factory=list, )

    # A marker used to get the next set of results.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListTargetsForSecurityProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_profile_name",
                "securityProfileName",
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

    # The security profile.
    security_profile_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return at one time.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListTargetsForSecurityProfileResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_profile_targets",
                "securityProfileTargets",
                autoboto.TypeInfo(typing.List[SecurityProfileTarget]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The thing groups to which the security profile is attached.
    security_profile_targets: typing.List["SecurityProfileTarget"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )

    # A token that can be used to retrieve the next set of results, or `null` if
    # there are no additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListThingGroupsForThingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
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

    # The thing name.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return at one time.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListThingGroupsForThingResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_groups",
                "thingGroups",
                autoboto.TypeInfo(typing.List[GroupNameAndArn]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The thing groups.
    thing_groups: typing.List["GroupNameAndArn"] = dataclasses.field(
        default_factory=list,
    )

    # The token used to get the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListThingGroupsRequest(autoboto.ShapeBase):
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
            (
                "parent_group",
                "parentGroup",
                autoboto.TypeInfo(str),
            ),
            (
                "name_prefix_filter",
                "namePrefixFilter",
                autoboto.TypeInfo(str),
            ),
            (
                "recursive",
                "recursive",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return at one time.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A filter that limits the results to those with the specified parent group.
    parent_group: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A filter that limits the results to those with the specified name prefix.
    name_prefix_filter: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If true, return child groups as well.
    recursive: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListThingGroupsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_groups",
                "thingGroups",
                autoboto.TypeInfo(typing.List[GroupNameAndArn]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The thing groups.
    thing_groups: typing.List["GroupNameAndArn"] = dataclasses.field(
        default_factory=list,
    )

    # The token used to get the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListThingPrincipalsRequest(autoboto.ShapeBase):
    """
    The input for the ListThingPrincipal operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the thing.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListThingPrincipalsResponse(autoboto.ShapeBase):
    """
    The output from the ListThingPrincipals operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "principals",
                "principals",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The principals associated with the thing.
    principals: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class ListThingRegistrationTaskReportsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                autoboto.TypeInfo(str),
            ),
            (
                "report_type",
                "reportType",
                autoboto.TypeInfo(ReportType),
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

    # The id of the task.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of task report.
    report_type: "ReportType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return per request.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListThingRegistrationTaskReportsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_links",
                "resourceLinks",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "report_type",
                "reportType",
                autoboto.TypeInfo(ReportType),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Links to the task resources.
    resource_links: typing.List[str] = dataclasses.field(default_factory=list, )

    # The type of task report.
    report_type: "ReportType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The token used to get the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListThingRegistrationTasksRequest(autoboto.ShapeBase):
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
            (
                "status",
                "status",
                autoboto.TypeInfo(Status),
            ),
        ]

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return at one time.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the bulk thing provisioning task.
    status: "Status" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListThingRegistrationTasksResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_ids",
                "taskIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of bulk thing provisioning task IDs.
    task_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The token used to get the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListThingTypesRequest(autoboto.ShapeBase):
    """
    The input for the ListThingTypes operation.
    """

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
            (
                "thing_type_name",
                "thingTypeName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return in this operation.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the thing type.
    thing_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListThingTypesResponse(autoboto.ShapeBase):
    """
    The output for the ListThingTypes operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_types",
                "thingTypes",
                autoboto.TypeInfo(typing.List[ThingTypeDefinition]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The thing types.
    thing_types: typing.List["ThingTypeDefinition"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListThingsInThingGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_group_name",
                "thingGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "recursive",
                "recursive",
                autoboto.TypeInfo(bool),
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

    # The thing group name.
    thing_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When true, list things in this thing group and in all child groups as well.
    recursive: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return at one time.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListThingsInThingGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "things",
                "things",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The things in the specified thing group.
    things: typing.List[str] = dataclasses.field(default_factory=list, )

    # The token used to get the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListThingsRequest(autoboto.ShapeBase):
    """
    The input for the ListThings operation.
    """

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
            (
                "attribute_name",
                "attributeName",
                autoboto.TypeInfo(str),
            ),
            (
                "attribute_value",
                "attributeValue",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_type_name",
                "thingTypeName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return in this operation.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The attribute name used to search for things.
    attribute_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The attribute value used to search for things.
    attribute_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the thing type used to search for things.
    thing_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListThingsResponse(autoboto.ShapeBase):
    """
    The output from the ListThings operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "things",
                "things",
                autoboto.TypeInfo(typing.List[ThingAttribute]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The things.
    things: typing.List["ThingAttribute"] = dataclasses.field(
        default_factory=list,
    )

    # The token used to get the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListTopicRulesRequest(autoboto.ShapeBase):
    """
    The input for the ListTopicRules operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "topic",
                "topic",
                autoboto.TypeInfo(str),
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
                "rule_disabled",
                "ruleDisabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The topic.
    topic: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A token used to retrieve the next value.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies whether the rule is disabled.
    rule_disabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListTopicRulesResponse(autoboto.ShapeBase):
    """
    The output from the ListTopicRules operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rules",
                "rules",
                autoboto.TypeInfo(typing.List[TopicRuleListItem]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The rules.
    rules: typing.List["TopicRuleListItem"] = dataclasses.field(
        default_factory=list,
    )

    # A token used to retrieve the next value.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListV2LoggingLevelsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_type",
                "targetType",
                autoboto.TypeInfo(LogTargetType),
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

    # The type of resource for which you are configuring logging. Must be
    # `THING_Group`.
    target_type: "LogTargetType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The token used to get the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return at one time.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListV2LoggingLevelsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_target_configurations",
                "logTargetConfigurations",
                autoboto.TypeInfo(typing.List[LogTargetConfiguration]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The logging configuration for a target.
    log_target_configurations: typing.List["LogTargetConfiguration"
                                          ] = dataclasses.field(
                                              default_factory=list,
                                          )

    # The token used to get the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListViolationEventsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "security_profile_name",
                "securityProfileName",
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

    # The start time for the alerts to be listed.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The end time for the alerts to be listed.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A filter to limit results to those alerts caused by the specified thing.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A filter to limit results to those alerts generated by the specified
    # security profile.
    security_profile_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return at one time.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListViolationEventsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "violation_events",
                "violationEvents",
                autoboto.TypeInfo(typing.List[ViolationEvent]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The security profile violation alerts issued for this account during the
    # given time frame, potentially filtered by security profile, behavior
    # violated, or thing (device) violating.
    violation_events: typing.List["ViolationEvent"] = dataclasses.field(
        default_factory=list,
    )

    # A token that can be used to retrieve the next set of results, or `null` if
    # there are no additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    ERROR = "ERROR"
    WARN = "WARN"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class LogTarget(autoboto.ShapeBase):
    """
    A log target.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_type",
                "targetType",
                autoboto.TypeInfo(LogTargetType),
            ),
            (
                "target_name",
                "targetName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The target type.
    target_type: "LogTargetType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The target name.
    target_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LogTargetConfiguration(autoboto.ShapeBase):
    """
    The target configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_target",
                "logTarget",
                autoboto.TypeInfo(LogTarget),
            ),
            (
                "log_level",
                "logLevel",
                autoboto.TypeInfo(LogLevel),
            ),
        ]

    # A log target
    log_target: "LogTarget" = dataclasses.field(default_factory=dict, )

    # The logging level.
    log_level: "LogLevel" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class LogTargetType(Enum):
    DEFAULT = "DEFAULT"
    THING_GROUP = "THING_GROUP"


@dataclasses.dataclass
class LoggingOptionsPayload(autoboto.ShapeBase):
    """
    Describes the logging options payload.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "log_level",
                "logLevel",
                autoboto.TypeInfo(LogLevel),
            ),
        ]

    # The ARN of the IAM role that grants access.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The log level.
    log_level: "LogLevel" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class MalformedPolicyException(autoboto.ShapeBase):
    """
    The policy documentation is not valid.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class MessageFormat(Enum):
    RAW = "RAW"
    JSON = "JSON"


@dataclasses.dataclass
class MetricValue(autoboto.ShapeBase):
    """
    The value to be compared with the `metric`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "count",
                "count",
                autoboto.TypeInfo(int),
            ),
            (
                "cidrs",
                "cidrs",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "ports",
                "ports",
                autoboto.TypeInfo(typing.List[int]),
            ),
        ]

    # If the `comparisonOperator` calls for a numeric value, use this to specify
    # that numeric value to be compared with the `metric`.
    count: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If the `comparisonOperator` calls for a set of CIDRs, use this to specify
    # that set to be compared with the `metric`.
    cidrs: typing.List[str] = dataclasses.field(default_factory=list, )

    # If the `comparisonOperator` calls for a set of ports, use this to specify
    # that set to be compared with the `metric`.
    ports: typing.List[int] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class NonCompliantResource(autoboto.ShapeBase):
    """
    Information about the resource that was non-compliant with the audit check.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "resource_identifier",
                "resourceIdentifier",
                autoboto.TypeInfo(ResourceIdentifier),
            ),
            (
                "additional_info",
                "additionalInfo",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The type of the non-compliant resource.
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information identifying the non-compliant resource.
    resource_identifier: "ResourceIdentifier" = dataclasses.field(
        default_factory=dict,
    )

    # Additional information about the non-compliant resource.
    additional_info: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class NotConfiguredException(autoboto.ShapeBase):
    """
    The resource is not configured.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class OTAUpdateFile(autoboto.ShapeBase):
    """
    Describes a file to be associated with an OTA update.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_name",
                "fileName",
                autoboto.TypeInfo(str),
            ),
            (
                "file_version",
                "fileVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "file_source",
                "fileSource",
                autoboto.TypeInfo(Stream),
            ),
            (
                "code_signing",
                "codeSigning",
                autoboto.TypeInfo(CodeSigning),
            ),
            (
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the file.
    file_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The file version.
    file_version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The source of the file.
    file_source: "Stream" = dataclasses.field(default_factory=dict, )

    # The code signing method of the file.
    code_signing: "CodeSigning" = dataclasses.field(default_factory=dict, )

    # A list of name/attribute pairs.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class OTAUpdateInfo(autoboto.ShapeBase):
    """
    Information about an OTA update.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ota_update_id",
                "otaUpdateId",
                autoboto.TypeInfo(str),
            ),
            (
                "ota_update_arn",
                "otaUpdateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_date",
                "lastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "targets",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "target_selection",
                "targetSelection",
                autoboto.TypeInfo(TargetSelection),
            ),
            (
                "ota_update_files",
                "otaUpdateFiles",
                autoboto.TypeInfo(typing.List[OTAUpdateFile]),
            ),
            (
                "ota_update_status",
                "otaUpdateStatus",
                autoboto.TypeInfo(OTAUpdateStatus),
            ),
            (
                "aws_iot_job_id",
                "awsIotJobId",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_iot_job_arn",
                "awsIotJobArn",
                autoboto.TypeInfo(str),
            ),
            (
                "error_info",
                "errorInfo",
                autoboto.TypeInfo(ErrorInfo),
            ),
            (
                "additional_parameters",
                "additionalParameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The OTA update ID.
    ota_update_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The OTA update ARN.
    ota_update_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date when the OTA update was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date when the OTA update was last updated.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the OTA update.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The targets of the OTA update.
    targets: typing.List[str] = dataclasses.field(default_factory=list, )

    # Specifies whether the OTA update will continue to run (CONTINUOUS), or will
    # be complete after all those things specified as targets have completed the
    # OTA update (SNAPSHOT). If continuous, the OTA update may also be run on a
    # thing when a change is detected in a target. For example, an OTA update
    # will run on a thing when the thing is added to a target group, even after
    # the OTA update was completed by all things originally in the group.
    target_selection: "TargetSelection" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of files associated with the OTA update.
    ota_update_files: typing.List["OTAUpdateFile"] = dataclasses.field(
        default_factory=list,
    )

    # The status of the OTA update.
    ota_update_status: "OTAUpdateStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS IoT job ID associated with the OTA update.
    aws_iot_job_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS IoT job ARN associated with the OTA update.
    aws_iot_job_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Error information associated with the OTA update.
    error_info: "ErrorInfo" = dataclasses.field(default_factory=dict, )

    # A collection of name/value pairs
    additional_parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class OTAUpdateStatus(Enum):
    CREATE_PENDING = "CREATE_PENDING"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    CREATE_FAILED = "CREATE_FAILED"


@dataclasses.dataclass
class OTAUpdateSummary(autoboto.ShapeBase):
    """
    An OTA update summary.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ota_update_id",
                "otaUpdateId",
                autoboto.TypeInfo(str),
            ),
            (
                "ota_update_arn",
                "otaUpdateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The OTA update ID.
    ota_update_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The OTA update ARN.
    ota_update_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date when the OTA update was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class OutgoingCertificate(autoboto.ShapeBase):
    """
    A certificate that has been transferred but not yet accepted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "certificateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "transferred_to",
                "transferredTo",
                autoboto.TypeInfo(str),
            ),
            (
                "transfer_date",
                "transferDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "transfer_message",
                "transferMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The certificate ARN.
    certificate_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The certificate ID.
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS account to which the transfer was made.
    transferred_to: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the transfer was initiated.
    transfer_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The transfer message.
    transfer_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The certificate creation date.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Policy(autoboto.ShapeBase):
    """
    Describes an AWS IoT policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_arn",
                "policyArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The policy name.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The policy ARN.
    policy_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PolicyVersion(autoboto.ShapeBase):
    """
    Describes a policy version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "version_id",
                "versionId",
                autoboto.TypeInfo(str),
            ),
            (
                "is_default_version",
                "isDefaultVersion",
                autoboto.TypeInfo(bool),
            ),
            (
                "create_date",
                "createDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The policy version ID.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies whether the policy version is the default.
    is_default_version: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time the policy was created.
    create_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PolicyVersionIdentifier(autoboto.ShapeBase):
    """
    Information about the version of the policy associated with the resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_version_id",
                "policyVersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the policy.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the version of the policy associated with the resource.
    policy_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PresignedUrlConfig(autoboto.ShapeBase):
    """
    Configuration for pre-signed S3 URLs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "expires_in_sec",
                "expiresInSec",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ARN of an IAM role that grants grants permission to download files from
    # the S3 bucket where the job data/updates are stored. The role must also
    # grant permission for IoT to download the files.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # How long (in seconds) pre-signed URLs are valid. Valid values are 60 -
    # 3600, the default value is 3600 seconds. Pre-signed URLs are generated when
    # Jobs receives an MQTT request for the job document.
    expires_in_sec: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PutItemInput(autoboto.ShapeBase):
    """
    The input for the DynamoActionVS action that specifies the DynamoDB table to
    which the message data will be written.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "tableName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The table where the message data will be written
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RegisterCACertificateRequest(autoboto.ShapeBase):
    """
    The input to the RegisterCACertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ca_certificate",
                "caCertificate",
                autoboto.TypeInfo(str),
            ),
            (
                "verification_certificate",
                "verificationCertificate",
                autoboto.TypeInfo(str),
            ),
            (
                "set_as_active",
                "setAsActive",
                autoboto.TypeInfo(bool),
            ),
            (
                "allow_auto_registration",
                "allowAutoRegistration",
                autoboto.TypeInfo(bool),
            ),
            (
                "registration_config",
                "registrationConfig",
                autoboto.TypeInfo(RegistrationConfig),
            ),
        ]

    # The CA certificate.
    ca_certificate: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The private key verification certificate.
    verification_certificate: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A boolean value that specifies if the CA certificate is set to active.
    set_as_active: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Allows this CA certificate to be used for auto registration of device
    # certificates.
    allow_auto_registration: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the registration configuration.
    registration_config: "RegistrationConfig" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class RegisterCACertificateResponse(autoboto.ShapeBase):
    """
    The output from the RegisterCACertificateResponse operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "certificateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The CA certificate ARN.
    certificate_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The CA certificate identifier.
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RegisterCertificateRequest(autoboto.ShapeBase):
    """
    The input to the RegisterCertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_pem",
                "certificatePem",
                autoboto.TypeInfo(str),
            ),
            (
                "ca_certificate_pem",
                "caCertificatePem",
                autoboto.TypeInfo(str),
            ),
            (
                "set_as_active",
                "setAsActive",
                autoboto.TypeInfo(bool),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(CertificateStatus),
            ),
        ]

    # The certificate data, in PEM format.
    certificate_pem: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The CA certificate used to sign the device certificate being registered.
    ca_certificate_pem: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A boolean value that specifies if the CA certificate is set to active.
    set_as_active: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the register certificate request.
    status: "CertificateStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RegisterCertificateResponse(autoboto.ShapeBase):
    """
    The output from the RegisterCertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "certificateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The certificate ARN.
    certificate_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The certificate identifier.
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RegisterThingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_body",
                "templateBody",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "parameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The provisioning template. See [Programmatic
    # Provisioning](http://docs.aws.amazon.com/iot/latest/developerguide/programmatic-
    # provisioning.html) for more information.
    template_body: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The parameters for provisioning a thing. See [Programmatic
    # Provisioning](http://docs.aws.amazon.com/iot/latest/developerguide/programmatic-
    # provisioning.html) for more information.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RegisterThingResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_pem",
                "certificatePem",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_arns",
                "resourceArns",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # .
    certificate_pem: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # ARNs for the generated resources.
    resource_arns: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RegistrationCodeValidationException(autoboto.ShapeBase):
    """
    The registration code is invalid.
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

    # Additional information about the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RegistrationConfig(autoboto.ShapeBase):
    """
    The registration configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_body",
                "templateBody",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The template body.
    template_body: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the role.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RejectCertificateTransferRequest(autoboto.ShapeBase):
    """
    The input for the RejectCertificateTransfer operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "reject_reason",
                "rejectReason",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the certificate. (The last part of the certificate ARN contains
    # the certificate ID.)
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The reason the certificate transfer was rejected.
    reject_reason: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RelatedResource(autoboto.ShapeBase):
    """
    Information about a related resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "resource_identifier",
                "resourceIdentifier",
                autoboto.TypeInfo(ResourceIdentifier),
            ),
            (
                "additional_info",
                "additionalInfo",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The type of resource.
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information identifying the resource.
    resource_identifier: "ResourceIdentifier" = dataclasses.field(
        default_factory=dict,
    )

    # Additional information about the resource.
    additional_info: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RemoveThingFromThingGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_group_name",
                "thingGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_group_arn",
                "thingGroupArn",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_arn",
                "thingArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The group name.
    thing_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The group ARN.
    thing_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the thing to remove from the group.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the thing to remove from the group.
    thing_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RemoveThingFromThingGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReplaceTopicRuleRequest(autoboto.ShapeBase):
    """
    The input for the ReplaceTopicRule operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_name",
                "ruleName",
                autoboto.TypeInfo(str),
            ),
            (
                "topic_rule_payload",
                "topicRulePayload",
                autoboto.TypeInfo(TopicRulePayload),
            ),
        ]

    # The name of the rule.
    rule_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The rule payload.
    topic_rule_payload: "TopicRulePayload" = dataclasses.field(
        default_factory=dict,
    )


class ReportType(Enum):
    ERRORS = "ERRORS"
    RESULTS = "RESULTS"


@dataclasses.dataclass
class RepublishAction(autoboto.ShapeBase):
    """
    Describes an action to republish to another topic.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "topic",
                "topic",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the IAM role that grants access.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the MQTT topic.
    topic: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ResourceAlreadyExistsException(autoboto.ShapeBase):
    """
    The resource already exists.
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
                "resource_id",
                "resourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_arn",
                "resourceArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the resource that caused the exception.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the resource that caused the exception.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ResourceIdentifier(autoboto.ShapeBase):
    """
    Information identifying the non-compliant resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_certificate_id",
                "deviceCertificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "ca_certificate_id",
                "caCertificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "cognito_identity_pool_id",
                "cognitoIdentityPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_id",
                "clientId",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_version_identifier",
                "policyVersionIdentifier",
                autoboto.TypeInfo(PolicyVersionIdentifier),
            ),
            (
                "account",
                "account",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the certificate attached to the resource.
    device_certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the CA certificate used to authorize the certificate.
    ca_certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the Cognito Identity Pool.
    cognito_identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The client ID.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the policy associated with the resource.
    policy_version_identifier: "PolicyVersionIdentifier" = dataclasses.field(
        default_factory=dict,
    )

    # The account with which the resource is associated.
    account: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    The specified resource does not exist.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ResourceRegistrationFailureException(autoboto.ShapeBase):
    """
    The resource registration failed.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class ResourceType(Enum):
    DEVICE_CERTIFICATE = "DEVICE_CERTIFICATE"
    CA_CERTIFICATE = "CA_CERTIFICATE"
    IOT_POLICY = "IOT_POLICY"
    COGNITO_IDENTITY_POOL = "COGNITO_IDENTITY_POOL"
    CLIENT_ID = "CLIENT_ID"
    ACCOUNT_SETTINGS = "ACCOUNT_SETTINGS"


@dataclasses.dataclass
class RoleAliasDescription(autoboto.ShapeBase):
    """
    Role alias description.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_alias",
                "roleAlias",
                autoboto.TypeInfo(str),
            ),
            (
                "role_alias_arn",
                "roleAliasArn",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "owner",
                "owner",
                autoboto.TypeInfo(str),
            ),
            (
                "credential_duration_seconds",
                "credentialDurationSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_date",
                "lastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The role alias.
    role_alias: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the role alias.
    role_alias_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The role ARN.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The role alias owner.
    owner: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of seconds for which the credential is valid.
    credential_duration_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The UNIX timestamp of when the role alias was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The UNIX timestamp of when the role alias was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class S3Action(autoboto.ShapeBase):
    """
    Describes an action to write data to an Amazon S3 bucket.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "bucket_name",
                "bucketName",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "key",
                autoboto.TypeInfo(str),
            ),
            (
                "canned_acl",
                "cannedAcl",
                autoboto.TypeInfo(CannedAccessControlList),
            ),
        ]

    # The ARN of the IAM role that grants access.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon S3 bucket.
    bucket_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The object key.
    key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon S3 canned ACL that controls access to the object identified by
    # the object key. For more information, see [S3 canned
    # ACLs](http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-
    # overview.html#canned-acl).
    canned_acl: "CannedAccessControlList" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class S3Location(autoboto.ShapeBase):
    """
    The location in S3 the contains the files to stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "key",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The S3 bucket that contains the file to stream.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the file within the S3 bucket to stream.
    key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The file version.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SalesforceAction(autoboto.ShapeBase):
    """
    Describes an action to write a message to a Salesforce IoT Cloud Input Stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "token",
                "token",
                autoboto.TypeInfo(str),
            ),
            (
                "url",
                "url",
                autoboto.TypeInfo(str),
            ),
        ]

    # The token used to authenticate access to the Salesforce IoT Cloud Input
    # Stream. The token is available from the Salesforce IoT Cloud platform after
    # creation of the Input Stream.
    token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is
    # available from the Salesforce IoT Cloud platform after creation of the
    # Input Stream.
    url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ScheduledAuditMetadata(autoboto.ShapeBase):
    """
    Information about the scheduled audit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_audit_name",
                "scheduledAuditName",
                autoboto.TypeInfo(str),
            ),
            (
                "scheduled_audit_arn",
                "scheduledAuditArn",
                autoboto.TypeInfo(str),
            ),
            (
                "frequency",
                "frequency",
                autoboto.TypeInfo(AuditFrequency),
            ),
            (
                "day_of_month",
                "dayOfMonth",
                autoboto.TypeInfo(str),
            ),
            (
                "day_of_week",
                "dayOfWeek",
                autoboto.TypeInfo(DayOfWeek),
            ),
        ]

    # The name of the scheduled audit.
    scheduled_audit_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the scheduled audit.
    scheduled_audit_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # How often the scheduled audit takes place.
    frequency: "AuditFrequency" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The day of the month on which the scheduled audit is run (if the
    # `frequency` is "MONTHLY"). If days 29-31 are specified, and the month does
    # not have that many days, the audit takes place on the "LAST" day of the
    # month.
    day_of_month: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The day of the week on which the scheduled audit is run (if the `frequency`
    # is "WEEKLY" or "BIWEEKLY").
    day_of_week: "DayOfWeek" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SearchIndexRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_string",
                "queryString",
                autoboto.TypeInfo(str),
            ),
            (
                "index_name",
                "indexName",
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
            (
                "query_version",
                "queryVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The search query string.
    query_string: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The search index name.
    index_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The token used to get the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results to return at one time.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The query version.
    query_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SearchIndexResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "things",
                "things",
                autoboto.TypeInfo(typing.List[ThingDocument]),
            ),
            (
                "thing_groups",
                "thingGroups",
                autoboto.TypeInfo(typing.List[ThingGroupDocument]),
            ),
        ]

    # The token used to get the next set of results, or **null** if there are no
    # additional results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The things that match the search query.
    things: typing.List["ThingDocument"] = dataclasses.field(
        default_factory=list,
    )

    # The thing groups that match the search query.
    thing_groups: typing.List["ThingGroupDocument"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class SecurityProfileIdentifier(autoboto.ShapeBase):
    """
    Identifying information for a Device Defender security profile.
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
        ]

    # The name you have given to the security profile.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the security profile.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SecurityProfileTarget(autoboto.ShapeBase):
    """
    A target to which an alert is sent when a security profile behavior is violated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the security profile.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SecurityProfileTargetMapping(autoboto.ShapeBase):
    """
    Information about a security profile and the target associated with it.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_profile_identifier",
                "securityProfileIdentifier",
                autoboto.TypeInfo(SecurityProfileIdentifier),
            ),
            (
                "target",
                "target",
                autoboto.TypeInfo(SecurityProfileTarget),
            ),
        ]

    # Information that identifies the security profile.
    security_profile_identifier: "SecurityProfileIdentifier" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the target (thing group) associated with the security
    # profile.
    target: "SecurityProfileTarget" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ServiceUnavailableException(autoboto.ShapeBase):
    """
    The service is temporarily unavailable.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SetDefaultAuthorizerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorizer_name",
                "authorizerName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The authorizer name.
    authorizer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SetDefaultAuthorizerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorizer_name",
                "authorizerName",
                autoboto.TypeInfo(str),
            ),
            (
                "authorizer_arn",
                "authorizerArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The authorizer name.
    authorizer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The authorizer ARN.
    authorizer_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SetDefaultPolicyVersionRequest(autoboto.ShapeBase):
    """
    The input for the SetDefaultPolicyVersion operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_version_id",
                "policyVersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The policy name.
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The policy version ID.
    policy_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SetLoggingOptionsRequest(autoboto.ShapeBase):
    """
    The input for the SetLoggingOptions operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logging_options_payload",
                "loggingOptionsPayload",
                autoboto.TypeInfo(LoggingOptionsPayload),
            ),
        ]

    # The logging options payload.
    logging_options_payload: "LoggingOptionsPayload" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SetV2LoggingLevelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_target",
                "logTarget",
                autoboto.TypeInfo(LogTarget),
            ),
            (
                "log_level",
                "logLevel",
                autoboto.TypeInfo(LogLevel),
            ),
        ]

    # The log target.
    log_target: "LogTarget" = dataclasses.field(default_factory=dict, )

    # The log level.
    log_level: "LogLevel" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SetV2LoggingOptionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "default_log_level",
                "defaultLogLevel",
                autoboto.TypeInfo(LogLevel),
            ),
            (
                "disable_all_logs",
                "disableAllLogs",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ARN of the role that allows IoT to write to Cloudwatch logs.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The default logging level.
    default_log_level: "LogLevel" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If true all logs are disabled. The default is false.
    disable_all_logs: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class Signature(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class SnsAction(autoboto.ShapeBase):
    """
    Describes an action to publish to an Amazon SNS topic.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_arn",
                "targetArn",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "message_format",
                "messageFormat",
                autoboto.TypeInfo(MessageFormat),
            ),
        ]

    # The ARN of the SNS topic.
    target_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the IAM role that grants access.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # (Optional) The message format of the message to publish. Accepted values
    # are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses
    # this setting to determine if the payload should be parsed and relevant
    # platform-specific bits of the payload should be extracted. To read more
    # about SNS message formats, see
    # <http://docs.aws.amazon.com/sns/latest/dg/json-formats.html> refer to their
    # official documentation.
    message_format: "MessageFormat" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SqlParseException(autoboto.ShapeBase):
    """
    The Rule-SQL expression can't be parsed correctly.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SqsAction(autoboto.ShapeBase):
    """
    Describes an action to publish data to an Amazon SQS queue.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "queue_url",
                "queueUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "use_base64",
                "useBase64",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ARN of the IAM role that grants access.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL of the Amazon SQS queue.
    queue_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies whether to use Base64 encoding.
    use_base64: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StartOnDemandAuditTaskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_check_names",
                "targetCheckNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # Which checks are performed during the audit. The checks you specify must be
    # enabled for your account or an exception occurs. Use
    # `DescribeAccountAuditConfiguration` to see the list of all checks including
    # those that are enabled or `UpdateAccountAuditConfiguration` to select which
    # checks are enabled.
    target_check_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class StartOnDemandAuditTaskResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the on-demand audit you started.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StartThingRegistrationTaskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_body",
                "templateBody",
                autoboto.TypeInfo(str),
            ),
            (
                "input_file_bucket",
                "inputFileBucket",
                autoboto.TypeInfo(str),
            ),
            (
                "input_file_key",
                "inputFileKey",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The provisioning template.
    template_body: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The S3 bucket that contains the input file.
    input_file_bucket: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of input file within the S3 bucket. This file contains a newline
    # delimited JSON file. Each line contains the parameter values to provision
    # one device (thing).
    input_file_key: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IAM role ARN that grants permission the input file.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StartThingRegistrationTaskResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The bulk thing provisioning task ID.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class Status(Enum):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Cancelled = "Cancelled"
    Cancelling = "Cancelling"


@dataclasses.dataclass
class StepFunctionsAction(autoboto.ShapeBase):
    """
    Starts execution of a Step Functions state machine.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state_machine_name",
                "stateMachineName",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_name_prefix",
                "executionNamePrefix",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the Step Functions state machine whose execution will be
    # started.
    state_machine_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the role that grants IoT permission to start execution of a
    # state machine ("Action":"states:StartExecution").
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # (Optional) A name will be given to the state machine execution consisting
    # of this prefix followed by a UUID. Step Functions automatically creates a
    # unique name for each state machine execution if one is not provided.
    execution_name_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class StopThingRegistrationTaskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The bulk thing provisioning task ID.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StopThingRegistrationTaskResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Stream(autoboto.ShapeBase):
    """
    Describes a group of files that can be streamed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_id",
                "streamId",
                autoboto.TypeInfo(str),
            ),
            (
                "file_id",
                "fileId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The stream ID.
    stream_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of a file associated with a stream.
    file_id: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StreamFile(autoboto.ShapeBase):
    """
    Represents a file to stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_id",
                "fileId",
                autoboto.TypeInfo(int),
            ),
            (
                "s3_location",
                "s3Location",
                autoboto.TypeInfo(S3Location),
            ),
        ]

    # The file ID.
    file_id: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The location of the file in S3.
    s3_location: "S3Location" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class StreamInfo(autoboto.ShapeBase):
    """
    Information about a stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_id",
                "streamId",
                autoboto.TypeInfo(str),
            ),
            (
                "stream_arn",
                "streamArn",
                autoboto.TypeInfo(str),
            ),
            (
                "stream_version",
                "streamVersion",
                autoboto.TypeInfo(int),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "files",
                "files",
                autoboto.TypeInfo(typing.List[StreamFile]),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_at",
                "lastUpdatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stream ID.
    stream_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The stream ARN.
    stream_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The stream version.
    stream_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The description of the stream.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The files to stream.
    files: typing.List["StreamFile"] = dataclasses.field(default_factory=list, )

    # The date when the stream was created.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date when the stream was last updated.
    last_updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An IAM role AWS IoT assumes to access your S3 files.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StreamSummary(autoboto.ShapeBase):
    """
    A summary of a stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_id",
                "streamId",
                autoboto.TypeInfo(str),
            ),
            (
                "stream_arn",
                "streamArn",
                autoboto.TypeInfo(str),
            ),
            (
                "stream_version",
                "streamVersion",
                autoboto.TypeInfo(int),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stream ID.
    stream_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The stream ARN.
    stream_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The stream version.
    stream_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the stream.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class TargetSelection(Enum):
    CONTINUOUS = "CONTINUOUS"
    SNAPSHOT = "SNAPSHOT"


@dataclasses.dataclass
class TaskStatistics(autoboto.ShapeBase):
    """
    Statistics for the checks performed during the audit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "total_checks",
                "totalChecks",
                autoboto.TypeInfo(int),
            ),
            (
                "in_progress_checks",
                "inProgressChecks",
                autoboto.TypeInfo(int),
            ),
            (
                "waiting_for_data_collection_checks",
                "waitingForDataCollectionChecks",
                autoboto.TypeInfo(int),
            ),
            (
                "compliant_checks",
                "compliantChecks",
                autoboto.TypeInfo(int),
            ),
            (
                "non_compliant_checks",
                "nonCompliantChecks",
                autoboto.TypeInfo(int),
            ),
            (
                "failed_checks",
                "failedChecks",
                autoboto.TypeInfo(int),
            ),
            (
                "canceled_checks",
                "canceledChecks",
                autoboto.TypeInfo(int),
            ),
        ]

    # The number of checks in this audit.
    total_checks: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of checks in progress.
    in_progress_checks: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of checks waiting for data collection.
    waiting_for_data_collection_checks: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of checks that found compliant resources.
    compliant_checks: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of checks that found non-compliant resources.
    non_compliant_checks: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of checks
    failed_checks: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of checks that did not run because the audit was canceled.
    canceled_checks: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class TestAuthorizationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auth_infos",
                "authInfos",
                autoboto.TypeInfo(typing.List[AuthInfo]),
            ),
            (
                "principal",
                "principal",
                autoboto.TypeInfo(str),
            ),
            (
                "cognito_identity_pool_id",
                "cognitoIdentityPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "client_id",
                "clientId",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_names_to_add",
                "policyNamesToAdd",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "policy_names_to_skip",
                "policyNamesToSkip",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A list of authorization info objects. Simulating authorization will create
    # a response for each `authInfo` object in the list.
    auth_infos: typing.List["AuthInfo"] = dataclasses.field(
        default_factory=list,
    )

    # The principal.
    principal: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Cognito identity pool ID.
    cognito_identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The MQTT client ID.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # When testing custom authorization, the policies specified here are treated
    # as if they are attached to the principal being authorized.
    policy_names_to_add: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # When testing custom authorization, the policies specified here are treated
    # as if they are not attached to the principal being authorized.
    policy_names_to_skip: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class TestAuthorizationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auth_results",
                "authResults",
                autoboto.TypeInfo(typing.List[AuthResult]),
            ),
        ]

    # The authentication results.
    auth_results: typing.List["AuthResult"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class TestInvokeAuthorizerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorizer_name",
                "authorizerName",
                autoboto.TypeInfo(str),
            ),
            (
                "token",
                "token",
                autoboto.TypeInfo(str),
            ),
            (
                "token_signature",
                "tokenSignature",
                autoboto.TypeInfo(str),
            ),
        ]

    # The custom authorizer name.
    authorizer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The token returned by your custom authentication service.
    token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The signature made with the token and your custom authentication service's
    # private key.
    token_signature: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class TestInvokeAuthorizerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "is_authenticated",
                "isAuthenticated",
                autoboto.TypeInfo(bool),
            ),
            (
                "principal_id",
                "principalId",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_documents",
                "policyDocuments",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "refresh_after_in_seconds",
                "refreshAfterInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "disconnect_after_in_seconds",
                "disconnectAfterInSeconds",
                autoboto.TypeInfo(int),
            ),
        ]

    # True if the token is authenticated, otherwise false.
    is_authenticated: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The principal ID.
    principal_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # IAM policy documents.
    policy_documents: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The number of seconds after which the temporary credentials are refreshed.
    refresh_after_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of seconds after which the connection is terminated.
    disconnect_after_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ThingAttribute(autoboto.ShapeBase):
    """
    The properties of the thing, including thing name, thing type name, and a list
    of thing attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_type_name",
                "thingTypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_arn",
                "thingArn",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the thing.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the thing type, if the thing has been associated with a type.
    thing_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing ARN.
    thing_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of thing attributes which are name-value pairs.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The version of the thing record in the registry.
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ThingDocument(autoboto.ShapeBase):
    """
    The thing search index document.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_id",
                "thingId",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_type_name",
                "thingTypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_group_names",
                "thingGroupNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "shadow",
                "shadow",
                autoboto.TypeInfo(str),
            ),
        ]

    # The thing name.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The thing ID.
    thing_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The thing type name.
    thing_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Thing group names.
    thing_group_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The attributes.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The shadow.
    shadow: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ThingGroupDocument(autoboto.ShapeBase):
    """
    The thing group search index document.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_group_name",
                "thingGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_group_id",
                "thingGroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_group_description",
                "thingGroupDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "parent_group_names",
                "parentGroupNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The thing group name.
    thing_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing group ID.
    thing_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing group description.
    thing_group_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing group attributes.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Parent group names.
    parent_group_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ThingGroupIndexingConfiguration(autoboto.ShapeBase):
    """
    Thing group indexing configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_group_indexing_mode",
                "thingGroupIndexingMode",
                autoboto.TypeInfo(ThingGroupIndexingMode),
            ),
        ]

    # Thing group indexing mode.
    thing_group_indexing_mode: "ThingGroupIndexingMode" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class ThingGroupIndexingMode(Enum):
    OFF = "OFF"
    ON = "ON"


@dataclasses.dataclass
class ThingGroupMetadata(autoboto.ShapeBase):
    """
    Thing group metadata.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parent_group_name",
                "parentGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "root_to_parent_thing_groups",
                "rootToParentThingGroups",
                autoboto.TypeInfo(typing.List[GroupNameAndArn]),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The parent thing group name.
    parent_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The root parent thing group.
    root_to_parent_thing_groups: typing.List["GroupNameAndArn"
                                            ] = dataclasses.field(
                                                default_factory=list,
                                            )

    # The UNIX timestamp of when the thing group was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ThingGroupProperties(autoboto.ShapeBase):
    """
    Thing group properties.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_group_description",
                "thingGroupDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "attribute_payload",
                "attributePayload",
                autoboto.TypeInfo(AttributePayload),
            ),
        ]

    # The thing group description.
    thing_group_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing group attributes in JSON format.
    attribute_payload: "AttributePayload" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ThingIndexingConfiguration(autoboto.ShapeBase):
    """
    Thing indexing configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_indexing_mode",
                "thingIndexingMode",
                autoboto.TypeInfo(ThingIndexingMode),
            ),
        ]

    # Thing indexing mode. Valid values are:

    #   * REGISTRY – Your thing index will contain only registry data.

    #   * REGISTRY_AND_SHADOW - Your thing index will contain registry and shadow data.

    #   * OFF - Thing indexing is disabled.
    thing_indexing_mode: "ThingIndexingMode" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class ThingIndexingMode(Enum):
    OFF = "OFF"
    REGISTRY = "REGISTRY"
    REGISTRY_AND_SHADOW = "REGISTRY_AND_SHADOW"


@dataclasses.dataclass
class ThingTypeDefinition(autoboto.ShapeBase):
    """
    The definition of the thing type, including thing type name and description.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_type_name",
                "thingTypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_type_arn",
                "thingTypeArn",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_type_properties",
                "thingTypeProperties",
                autoboto.TypeInfo(ThingTypeProperties),
            ),
            (
                "thing_type_metadata",
                "thingTypeMetadata",
                autoboto.TypeInfo(ThingTypeMetadata),
            ),
        ]

    # The name of the thing type.
    thing_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing type ARN.
    thing_type_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ThingTypeProperties for the thing type.
    thing_type_properties: "ThingTypeProperties" = dataclasses.field(
        default_factory=dict,
    )

    # The ThingTypeMetadata contains additional information about the thing type
    # including: creation date and time, a value indicating whether the thing
    # type is deprecated, and a date and time when it was deprecated.
    thing_type_metadata: "ThingTypeMetadata" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ThingTypeMetadata(autoboto.ShapeBase):
    """
    The ThingTypeMetadata contains additional information about the thing type
    including: creation date and time, a value indicating whether the thing type is
    deprecated, and a date and time when time was deprecated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deprecated",
                "deprecated",
                autoboto.TypeInfo(bool),
            ),
            (
                "deprecation_date",
                "deprecationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # Whether the thing type is deprecated. If **true** , no new things could be
    # associated with this type.
    deprecated: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date and time when the thing type was deprecated.
    deprecation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time when the thing type was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ThingTypeProperties(autoboto.ShapeBase):
    """
    The ThingTypeProperties contains information about the thing type including: a
    thing type description, and a list of searchable thing attribute names.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_type_description",
                "thingTypeDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "searchable_attributes",
                "searchableAttributes",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The description of the thing type.
    thing_type_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of searchable thing attribute names.
    searchable_attributes: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ThrottlingException(autoboto.ShapeBase):
    """
    The rate exceeds the limit.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TopicRule(autoboto.ShapeBase):
    """
    Describes a rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_name",
                "ruleName",
                autoboto.TypeInfo(str),
            ),
            (
                "sql",
                "sql",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "actions",
                "actions",
                autoboto.TypeInfo(typing.List[Action]),
            ),
            (
                "rule_disabled",
                "ruleDisabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "aws_iot_sql_version",
                "awsIotSqlVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "error_action",
                "errorAction",
                autoboto.TypeInfo(Action),
            ),
        ]

    # The name of the rule.
    rule_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The SQL statement used to query the topic. When using a SQL query with
    # multiple lines, be sure to escape the newline characters.
    sql: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The description of the rule.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date and time the rule was created.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The actions associated with the rule.
    actions: typing.List["Action"] = dataclasses.field(default_factory=list, )

    # Specifies whether the rule is disabled.
    rule_disabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The version of the SQL rules engine to use when evaluating the rule.
    aws_iot_sql_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The action to perform when an error occurs.
    error_action: "Action" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class TopicRuleListItem(autoboto.ShapeBase):
    """
    Describes a rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_arn",
                "ruleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "rule_name",
                "ruleName",
                autoboto.TypeInfo(str),
            ),
            (
                "topic_pattern",
                "topicPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "rule_disabled",
                "ruleDisabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The rule ARN.
    rule_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the rule.
    rule_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The pattern for the topic names that apply.
    topic_pattern: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time the rule was created.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether the rule is disabled.
    rule_disabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class TopicRulePayload(autoboto.ShapeBase):
    """
    Describes a rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sql",
                "sql",
                autoboto.TypeInfo(str),
            ),
            (
                "actions",
                "actions",
                autoboto.TypeInfo(typing.List[Action]),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "rule_disabled",
                "ruleDisabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "aws_iot_sql_version",
                "awsIotSqlVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "error_action",
                "errorAction",
                autoboto.TypeInfo(Action),
            ),
        ]

    # The SQL statement used to query the topic. For more information, see [AWS
    # IoT SQL
    # Reference](http://docs.aws.amazon.com/iot/latest/developerguide/iot-
    # rules.html#aws-iot-sql-reference) in the _AWS IoT Developer Guide_.
    sql: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The actions associated with the rule.
    actions: typing.List["Action"] = dataclasses.field(default_factory=list, )

    # The description of the rule.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies whether the rule is disabled.
    rule_disabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The version of the SQL rules engine to use when evaluating the rule.
    aws_iot_sql_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The action to take when an error occurs.
    error_action: "Action" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class TransferAlreadyCompletedException(autoboto.ShapeBase):
    """
    You can't revert the certificate transfer because the transfer is already
    complete.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TransferCertificateRequest(autoboto.ShapeBase):
    """
    The input for the TransferCertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "target_aws_account",
                "targetAwsAccount",
                autoboto.TypeInfo(str),
            ),
            (
                "transfer_message",
                "transferMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the certificate. (The last part of the certificate ARN contains
    # the certificate ID.)
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS account.
    target_aws_account: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The transfer message.
    transfer_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class TransferCertificateResponse(autoboto.ShapeBase):
    """
    The output from the TransferCertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "transferred_certificate_arn",
                "transferredCertificateArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the certificate.
    transferred_certificate_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class TransferConflictException(autoboto.ShapeBase):
    """
    You can't transfer the certificate because authorization policies are still
    attached.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TransferData(autoboto.ShapeBase):
    """
    Data used to transfer a certificate to an AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "transfer_message",
                "transferMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "reject_reason",
                "rejectReason",
                autoboto.TypeInfo(str),
            ),
            (
                "transfer_date",
                "transferDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "accept_date",
                "acceptDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "reject_date",
                "rejectDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The transfer message.
    transfer_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The reason why the transfer was rejected.
    reject_reason: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the transfer took place.
    transfer_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the transfer was accepted.
    accept_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the transfer was rejected.
    reject_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UnauthorizedException(autoboto.ShapeBase):
    """
    You are not authorized to perform this operation.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateAccountAuditConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "audit_notification_target_configurations",
                "auditNotificationTargetConfigurations",
                autoboto.TypeInfo(
                    typing.Dict[AuditNotificationType, AuditNotificationTarget]
                ),
            ),
            (
                "audit_check_configurations",
                "auditCheckConfigurations",
                autoboto.TypeInfo(typing.Dict[str, AuditCheckConfiguration]),
            ),
        ]

    # The ARN of the role that grants permission to AWS IoT to access information
    # about your devices, policies, certificates and other items as necessary
    # when performing an audit.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information about the targets to which audit notifications are sent.
    audit_notification_target_configurations: typing.Dict[
        "AuditNotificationType", "AuditNotificationTarget"
    ] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies which audit checks are enabled and disabled for this account. Use
    # `DescribeAccountAuditConfiguration` to see the list of all checks including
    # those that are currently enabled.

    # Note that some data collection may begin immediately when certain checks
    # are enabled. When a check is disabled, any data collected so far in
    # relation to the check is deleted.

    # You cannot disable a check if it is used by any scheduled audit. You must
    # first delete the check from the scheduled audit or delete the scheduled
    # audit itself.

    # On the first call to `UpdateAccountAuditConfiguration` this parameter is
    # required and must specify at least one enabled check.
    audit_check_configurations: typing.Dict[
        str, "AuditCheckConfiguration"
    ] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateAccountAuditConfigurationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateAuthorizerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorizer_name",
                "authorizerName",
                autoboto.TypeInfo(str),
            ),
            (
                "authorizer_function_arn",
                "authorizerFunctionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "token_key_name",
                "tokenKeyName",
                autoboto.TypeInfo(str),
            ),
            (
                "token_signing_public_keys",
                "tokenSigningPublicKeys",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(AuthorizerStatus),
            ),
        ]

    # The authorizer name.
    authorizer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the authorizer's Lambda function.
    authorizer_function_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The key used to extract the token from the HTTP headers.
    token_key_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The public keys used to verify the token signature.
    token_signing_public_keys: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the update authorizer request.
    status: "AuthorizerStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateAuthorizerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorizer_name",
                "authorizerName",
                autoboto.TypeInfo(str),
            ),
            (
                "authorizer_arn",
                "authorizerArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The authorizer name.
    authorizer_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The authorizer ARN.
    authorizer_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateCACertificateRequest(autoboto.ShapeBase):
    """
    The input to the UpdateCACertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "new_status",
                "newStatus",
                autoboto.TypeInfo(CACertificateStatus),
            ),
            (
                "new_auto_registration_status",
                "newAutoRegistrationStatus",
                autoboto.TypeInfo(AutoRegistrationStatus),
            ),
            (
                "registration_config",
                "registrationConfig",
                autoboto.TypeInfo(RegistrationConfig),
            ),
            (
                "remove_auto_registration",
                "removeAutoRegistration",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The CA certificate identifier.
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The updated status of the CA certificate.

    # **Note:** The status value REGISTER_INACTIVE is deprecated and should not
    # be used.
    new_status: "CACertificateStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The new value for the auto registration status. Valid values are: "ENABLE"
    # or "DISABLE".
    new_auto_registration_status: "AutoRegistrationStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the registration configuration.
    registration_config: "RegistrationConfig" = dataclasses.field(
        default_factory=dict,
    )

    # If true, remove auto registration.
    remove_auto_registration: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateCertificateRequest(autoboto.ShapeBase):
    """
    The input for the UpdateCertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_id",
                "certificateId",
                autoboto.TypeInfo(str),
            ),
            (
                "new_status",
                "newStatus",
                autoboto.TypeInfo(CertificateStatus),
            ),
        ]

    # The ID of the certificate. (The last part of the certificate ARN contains
    # the certificate ID.)
    certificate_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The new status.

    # **Note:** Setting the status to PENDING_TRANSFER will result in an
    # exception being thrown. PENDING_TRANSFER is a status used internally by AWS
    # IoT. It is not intended for developer use.

    # **Note:** The status value REGISTER_INACTIVE is deprecated and should not
    # be used.
    new_status: "CertificateStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateEventConfigurationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_configurations",
                "eventConfigurations",
                autoboto.TypeInfo(typing.Dict[EventType, Configuration]),
            ),
        ]

    # The new event configuration values.
    event_configurations: typing.Dict["EventType", "Configuration"
                                     ] = dataclasses.field(
                                         default=autoboto.ShapeBase._NOT_SET,
                                     )


@dataclasses.dataclass
class UpdateEventConfigurationsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateIndexingConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_indexing_configuration",
                "thingIndexingConfiguration",
                autoboto.TypeInfo(ThingIndexingConfiguration),
            ),
            (
                "thing_group_indexing_configuration",
                "thingGroupIndexingConfiguration",
                autoboto.TypeInfo(ThingGroupIndexingConfiguration),
            ),
        ]

    # Thing indexing configuration.
    thing_indexing_configuration: "ThingIndexingConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # Thing group indexing configuration.
    thing_group_indexing_configuration: "ThingGroupIndexingConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateIndexingConfigurationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateRoleAliasRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_alias",
                "roleAlias",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "credential_duration_seconds",
                "credentialDurationSeconds",
                autoboto.TypeInfo(int),
            ),
        ]

    # The role alias to update.
    role_alias: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The role ARN.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of seconds the credential will be valid.
    credential_duration_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateRoleAliasResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_alias",
                "roleAlias",
                autoboto.TypeInfo(str),
            ),
            (
                "role_alias_arn",
                "roleAliasArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The role alias.
    role_alias: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The role alias ARN.
    role_alias_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateScheduledAuditRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_audit_name",
                "scheduledAuditName",
                autoboto.TypeInfo(str),
            ),
            (
                "frequency",
                "frequency",
                autoboto.TypeInfo(AuditFrequency),
            ),
            (
                "day_of_month",
                "dayOfMonth",
                autoboto.TypeInfo(str),
            ),
            (
                "day_of_week",
                "dayOfWeek",
                autoboto.TypeInfo(DayOfWeek),
            ),
            (
                "target_check_names",
                "targetCheckNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the scheduled audit. (Max. 128 chars)
    scheduled_audit_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # How often the scheduled audit takes place. Can be one of "DAILY", "WEEKLY",
    # "BIWEEKLY" or "MONTHLY". The actual start time of each audit is determined
    # by the system.
    frequency: "AuditFrequency" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The day of the month on which the scheduled audit takes place. Can be "1"
    # through "31" or "LAST". This field is required if the "frequency" parameter
    # is set to "MONTHLY". If days 29-31 are specified, and the month does not
    # have that many days, the audit takes place on the "LAST" day of the month.
    day_of_month: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The day of the week on which the scheduled audit takes place. Can be one of
    # "SUN", "MON", "TUE", "WED", "THU", "FRI" or "SAT". This field is required
    # if the "frequency" parameter is set to "WEEKLY" or "BIWEEKLY".
    day_of_week: "DayOfWeek" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Which checks are performed during the scheduled audit. Checks must be
    # enabled for your account. (Use `DescribeAccountAuditConfiguration` to see
    # the list of all checks including those that are enabled or
    # `UpdateAccountAuditConfiguration` to select which checks are enabled.)
    target_check_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateScheduledAuditResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_audit_arn",
                "scheduledAuditArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the scheduled audit.
    scheduled_audit_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateSecurityProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_profile_name",
                "securityProfileName",
                autoboto.TypeInfo(str),
            ),
            (
                "security_profile_description",
                "securityProfileDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "behaviors",
                "behaviors",
                autoboto.TypeInfo(typing.List[Behavior]),
            ),
            (
                "alert_targets",
                "alertTargets",
                autoboto.TypeInfo(typing.Dict[AlertTargetType, AlertTarget]),
            ),
            (
                "expected_version",
                "expectedVersion",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the security profile you want to update.
    security_profile_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the security profile.
    security_profile_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the behaviors that, when violated by a device (thing), cause an
    # alert.
    behaviors: typing.List["Behavior"] = dataclasses.field(
        default_factory=list,
    )

    # Where the alerts are sent. (Alerts are always sent to the console.)
    alert_targets: typing.Dict["AlertTargetType", "AlertTarget"
                              ] = dataclasses.field(
                                  default=autoboto.ShapeBase._NOT_SET,
                              )

    # The expected version of the security profile. A new version is generated
    # whenever the security profile is updated. If you specify a value that is
    # different than the actual version, a `VersionConflictException` is thrown.
    expected_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateSecurityProfileResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_profile_name",
                "securityProfileName",
                autoboto.TypeInfo(str),
            ),
            (
                "security_profile_arn",
                "securityProfileArn",
                autoboto.TypeInfo(str),
            ),
            (
                "security_profile_description",
                "securityProfileDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "behaviors",
                "behaviors",
                autoboto.TypeInfo(typing.List[Behavior]),
            ),
            (
                "alert_targets",
                "alertTargets",
                autoboto.TypeInfo(typing.Dict[AlertTargetType, AlertTarget]),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(int),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_date",
                "lastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the security profile that was updated.
    security_profile_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ARN of the security profile that was updated.
    security_profile_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The description of the security profile.
    security_profile_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the behaviors that, when violated by a device (thing), cause an
    # alert.
    behaviors: typing.List["Behavior"] = dataclasses.field(
        default_factory=list,
    )

    # Where the alerts are sent. (Alerts are always sent to the console.)
    alert_targets: typing.Dict["AlertTargetType", "AlertTarget"
                              ] = dataclasses.field(
                                  default=autoboto.ShapeBase._NOT_SET,
                              )

    # The updated version of the security profile.
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time the security profile was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time the security profile was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateStreamRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_id",
                "streamId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "files",
                "files",
                autoboto.TypeInfo(typing.List[StreamFile]),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stream ID.
    stream_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The description of the stream.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The files associated with the stream.
    files: typing.List["StreamFile"] = dataclasses.field(default_factory=list, )

    # An IAM role that allows the IoT service principal assumes to access your S3
    # files.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateStreamResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_id",
                "streamId",
                autoboto.TypeInfo(str),
            ),
            (
                "stream_arn",
                "streamArn",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "stream_version",
                "streamVersion",
                autoboto.TypeInfo(int),
            ),
        ]

    # The stream ID.
    stream_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The stream ARN.
    stream_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A description of the stream.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The stream version.
    stream_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateThingGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_group_name",
                "thingGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_group_properties",
                "thingGroupProperties",
                autoboto.TypeInfo(ThingGroupProperties),
            ),
            (
                "expected_version",
                "expectedVersion",
                autoboto.TypeInfo(int),
            ),
        ]

    # The thing group to update.
    thing_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The thing group properties.
    thing_group_properties: "ThingGroupProperties" = dataclasses.field(
        default_factory=dict,
    )

    # The expected version of the thing group. If this does not match the version
    # of the thing group being updated, the update will fail.
    expected_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateThingGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "version",
                "version",
                autoboto.TypeInfo(int),
            ),
        ]

    # The version of the updated thing group.
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateThingGroupsForThingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_groups_to_add",
                "thingGroupsToAdd",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "thing_groups_to_remove",
                "thingGroupsToRemove",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The thing whose group memberships will be updated.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The groups to which the thing will be added.
    thing_groups_to_add: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The groups from which the thing will be removed.
    thing_groups_to_remove: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateThingGroupsForThingResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateThingRequest(autoboto.ShapeBase):
    """
    The input for the UpdateThing operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_type_name",
                "thingTypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "attribute_payload",
                "attributePayload",
                autoboto.TypeInfo(AttributePayload),
            ),
            (
                "expected_version",
                "expectedVersion",
                autoboto.TypeInfo(int),
            ),
            (
                "remove_thing_type",
                "removeThingType",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the thing to update.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the thing type.
    thing_type_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of thing attributes, a JSON string containing name-value pairs. For
    # example:

    # `{\"attributes\":{\"name1\":\"value2\"}}`

    # This data is used to add new attributes or update existing attributes.
    attribute_payload: "AttributePayload" = dataclasses.field(
        default_factory=dict,
    )

    # The expected version of the thing record in the registry. If the version of
    # the record in the registry does not match the expected version specified in
    # the request, the `UpdateThing` request is rejected with a
    # `VersionConflictException`.
    expected_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Remove a thing type association. If **true** , the association is removed.
    remove_thing_type: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateThingResponse(autoboto.ShapeBase):
    """
    The output from the UpdateThing operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ValidateSecurityProfileBehaviorsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "behaviors",
                "behaviors",
                autoboto.TypeInfo(typing.List[Behavior]),
            ),
        ]

    # Specifies the behaviors that, when violated by a device (thing), cause an
    # alert.
    behaviors: typing.List["Behavior"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ValidateSecurityProfileBehaviorsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "valid",
                "valid",
                autoboto.TypeInfo(bool),
            ),
            (
                "validation_errors",
                "validationErrors",
                autoboto.TypeInfo(typing.List[ValidationError]),
            ),
        ]

    # True if the behaviors were valid.
    valid: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The list of any errors found in the behaviors.
    validation_errors: typing.List["ValidationError"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ValidationError(autoboto.ShapeBase):
    """
    Information about an error found in a behavior specification.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_message",
                "errorMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The description of an error found in the behaviors.
    error_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class VersionConflictException(autoboto.ShapeBase):
    """
    An exception thrown when the version of an entity specified with the
    `expectedVersion` parameter does not match the latest version in the system.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class VersionsLimitExceededException(autoboto.ShapeBase):
    """
    The number of policy versions exceeds the limit.
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

    # The message for the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ViolationEvent(autoboto.ShapeBase):
    """
    Information about a Device Defender security profile behavior violation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "violation_id",
                "violationId",
                autoboto.TypeInfo(str),
            ),
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "security_profile_name",
                "securityProfileName",
                autoboto.TypeInfo(str),
            ),
            (
                "behavior",
                "behavior",
                autoboto.TypeInfo(Behavior),
            ),
            (
                "metric_value",
                "metricValue",
                autoboto.TypeInfo(MetricValue),
            ),
            (
                "violation_event_type",
                "violationEventType",
                autoboto.TypeInfo(ViolationEventType),
            ),
            (
                "violation_event_time",
                "violationEventTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ID of the violation event.
    violation_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the thing responsible for the violation event.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the security profile whose behavior was violated.
    security_profile_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The behavior which was violated.
    behavior: "Behavior" = dataclasses.field(default_factory=dict, )

    # The value of the metric (the measurement).
    metric_value: "MetricValue" = dataclasses.field(default_factory=dict, )

    # The type of violation event.
    violation_event_type: "ViolationEventType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time the violation event occurred.
    violation_event_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class ViolationEventType(Enum):
    in_alarm = "in-alarm"
    alarm_cleared = "alarm-cleared"
    alarm_invalidated = "alarm-invalidated"
