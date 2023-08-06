import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


class AccessDeniedErrorCode(Enum):
    ACCESS_DENIED_TO_ASSESSMENT_TARGET = "ACCESS_DENIED_TO_ASSESSMENT_TARGET"
    ACCESS_DENIED_TO_ASSESSMENT_TEMPLATE = "ACCESS_DENIED_TO_ASSESSMENT_TEMPLATE"
    ACCESS_DENIED_TO_ASSESSMENT_RUN = "ACCESS_DENIED_TO_ASSESSMENT_RUN"
    ACCESS_DENIED_TO_FINDING = "ACCESS_DENIED_TO_FINDING"
    ACCESS_DENIED_TO_RESOURCE_GROUP = "ACCESS_DENIED_TO_RESOURCE_GROUP"
    ACCESS_DENIED_TO_RULES_PACKAGE = "ACCESS_DENIED_TO_RULES_PACKAGE"
    ACCESS_DENIED_TO_SNS_TOPIC = "ACCESS_DENIED_TO_SNS_TOPIC"
    ACCESS_DENIED_TO_IAM_ROLE = "ACCESS_DENIED_TO_IAM_ROLE"


@dataclasses.dataclass
class AccessDeniedException(autoboto.ShapeBase):
    """
    You do not have required permissions to access the requested resource.
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
                "error_code",
                "errorCode",
                autoboto.TypeInfo(AccessDeniedErrorCode),
            ),
            (
                "can_retry",
                "canRetry",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Code that indicates the type of error that is generated.
    error_code: "AccessDeniedErrorCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # You can immediately retry your request.
    can_retry: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddAttributesToFindingsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "finding_arns",
                "findingArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.List[Attribute]),
            ),
        ]

    # The ARNs that specify the findings that you want to assign attributes to.
    finding_arns: typing.List[str] = dataclasses.field(default_factory=list, )

    # The array of attributes that you want to assign to specified findings.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AddAttributesToFindingsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_items",
                "failedItems",
                autoboto.TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Attribute details that cannot be described. An error code is provided for
    # each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AgentAlreadyRunningAssessment(autoboto.ShapeBase):
    """
    Used in the exception error that is thrown if you start an assessment run for an
    assessment target that includes an EC2 instance that is already participating in
    another started assessment run.
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
                "assessment_run_arn",
                "assessmentRunArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # ID of the agent that is running on an EC2 instance that is already
    # participating in another started assessment run.
    agent_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the assessment run that has already been started.
    assessment_run_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AgentFilter(autoboto.ShapeBase):
    """
    Contains information about an Amazon Inspector agent. This data type is used as
    a request parameter in the ListAssessmentRunAgents action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_healths",
                "agentHealths",
                autoboto.TypeInfo(typing.List[AgentHealth]),
            ),
            (
                "agent_health_codes",
                "agentHealthCodes",
                autoboto.TypeInfo(typing.List[AgentHealthCode]),
            ),
        ]

    # The current health state of the agent. Values can be set to **HEALTHY** or
    # **UNHEALTHY**.
    agent_healths: typing.List["AgentHealth"] = dataclasses.field(
        default_factory=list,
    )

    # The detailed health state of the agent. Values can be set to **IDLE** ,
    # **RUNNING** , **SHUTDOWN** , **UNHEALTHY** , **THROTTLED** , and
    # **UNKNOWN**.
    agent_health_codes: typing.List["AgentHealthCode"] = dataclasses.field(
        default_factory=list,
    )


class AgentHealth(Enum):
    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"
    UNKNOWN = "UNKNOWN"


class AgentHealthCode(Enum):
    IDLE = "IDLE"
    RUNNING = "RUNNING"
    SHUTDOWN = "SHUTDOWN"
    UNHEALTHY = "UNHEALTHY"
    THROTTLED = "THROTTLED"
    UNKNOWN = "UNKNOWN"


@dataclasses.dataclass
class AgentPreview(autoboto.ShapeBase):
    """
    Used as a response element in the PreviewAgents action.
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
                "hostname",
                "hostname",
                autoboto.TypeInfo(str),
            ),
            (
                "auto_scaling_group",
                "autoScalingGroup",
                autoboto.TypeInfo(str),
            ),
            (
                "agent_health",
                "agentHealth",
                autoboto.TypeInfo(AgentHealth),
            ),
            (
                "agent_version",
                "agentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "operating_system",
                "operatingSystem",
                autoboto.TypeInfo(str),
            ),
            (
                "kernel_version",
                "kernelVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "ipv4_address",
                "ipv4Address",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the EC2 instance where the agent is installed.
    agent_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The hostname of the EC2 instance on which the Amazon Inspector Agent is
    # installed.
    hostname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Auto Scaling group for the EC2 instance where the agent is installed.
    auto_scaling_group: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The health status of the Amazon Inspector Agent.
    agent_health: "AgentHealth" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The version of the Amazon Inspector Agent.
    agent_version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The operating system running on the EC2 instance on which the Amazon
    # Inspector Agent is installed.
    operating_system: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The kernel version of the operating system running on the EC2 instance on
    # which the Amazon Inspector Agent is installed.
    kernel_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The IP address of the EC2 instance on which the Amazon Inspector Agent is
    # installed.
    ipv4_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AgentsAlreadyRunningAssessmentException(autoboto.ShapeBase):
    """
    You started an assessment run, but one of the instances is already participating
    in another assessment run.
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
                "agents",
                "agents",
                autoboto.TypeInfo(typing.List[AgentAlreadyRunningAssessment]),
            ),
            (
                "agents_truncated",
                "agentsTruncated",
                autoboto.TypeInfo(bool),
            ),
            (
                "can_retry",
                "canRetry",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    agents: typing.List["AgentAlreadyRunningAssessment"] = dataclasses.field(
        default_factory=list,
    )

    agents_truncated: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # You can immediately retry your request.
    can_retry: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssessmentRun(autoboto.ShapeBase):
    """
    A snapshot of an Amazon Inspector assessment run that contains the findings of
    the assessment run .

    Used as the response element in the DescribeAssessmentRuns action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "assessment_template_arn",
                "assessmentTemplateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "state",
                autoboto.TypeInfo(AssessmentRunState),
            ),
            (
                "duration_in_seconds",
                "durationInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "rules_package_arns",
                "rulesPackageArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "user_attributes_for_findings",
                "userAttributesForFindings",
                autoboto.TypeInfo(typing.List[Attribute]),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "state_changed_at",
                "stateChangedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "data_collected",
                "dataCollected",
                autoboto.TypeInfo(bool),
            ),
            (
                "state_changes",
                "stateChanges",
                autoboto.TypeInfo(typing.List[AssessmentRunStateChange]),
            ),
            (
                "notifications",
                "notifications",
                autoboto.TypeInfo(typing.List[AssessmentRunNotification]),
            ),
            (
                "finding_counts",
                "findingCounts",
                autoboto.TypeInfo(typing.Dict[Severity, int]),
            ),
            (
                "started_at",
                "startedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "completed_at",
                "completedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ARN of the assessment run.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The auto-generated name for the assessment run.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the assessment template that is associated with the assessment
    # run.
    assessment_template_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The state of the assessment run.
    state: "AssessmentRunState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The duration of the assessment run.
    duration_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The rules packages selected for the assessment run.
    rules_package_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The user-defined attributes that are assigned to every generated finding.
    user_attributes_for_findings: typing.List["Attribute"] = dataclasses.field(
        default_factory=list,
    )

    # The time when StartAssessmentRun was called.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The last time when the assessment run's state changed.
    state_changed_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A Boolean value (true or false) that specifies whether the process of
    # collecting data from the agents is completed.
    data_collected: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of the assessment run state changes.
    state_changes: typing.List["AssessmentRunStateChange"] = dataclasses.field(
        default_factory=list,
    )

    # A list of notifications for the event subscriptions. A notification about a
    # particular generated finding is added to this list only once.
    notifications: typing.List["AssessmentRunNotification"] = dataclasses.field(
        default_factory=list,
    )

    # Provides a total count of generated findings per severity.
    finding_counts: typing.Dict["Severity", int] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time when StartAssessmentRun was called.
    started_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The assessment run completion time that corresponds to the rules packages
    # evaluation completion time or failure.
    completed_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssessmentRunAgent(autoboto.ShapeBase):
    """
    Contains information about an Amazon Inspector agent. This data type is used as
    a response element in the ListAssessmentRunAgents action.
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
                "assessment_run_arn",
                "assessmentRunArn",
                autoboto.TypeInfo(str),
            ),
            (
                "agent_health",
                "agentHealth",
                autoboto.TypeInfo(AgentHealth),
            ),
            (
                "agent_health_code",
                "agentHealthCode",
                autoboto.TypeInfo(AgentHealthCode),
            ),
            (
                "telemetry_metadata",
                "telemetryMetadata",
                autoboto.TypeInfo(typing.List[TelemetryMetadata]),
            ),
            (
                "agent_health_details",
                "agentHealthDetails",
                autoboto.TypeInfo(str),
            ),
            (
                "auto_scaling_group",
                "autoScalingGroup",
                autoboto.TypeInfo(str),
            ),
        ]

    # The AWS account of the EC2 instance where the agent is installed.
    agent_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the assessment run that is associated with the agent.
    assessment_run_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The current health state of the agent.
    agent_health: "AgentHealth" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The detailed health state of the agent.
    agent_health_code: "AgentHealthCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Inspector application data metrics that are collected by the
    # agent.
    telemetry_metadata: typing.List["TelemetryMetadata"] = dataclasses.field(
        default_factory=list,
    )

    # The description for the agent health code.
    agent_health_details: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Auto Scaling group of the EC2 instance that is specified by the agent
    # ID.
    auto_scaling_group: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssessmentRunFilter(autoboto.ShapeBase):
    """
    Used as the request parameter in the ListAssessmentRuns action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name_pattern",
                "namePattern",
                autoboto.TypeInfo(str),
            ),
            (
                "states",
                "states",
                autoboto.TypeInfo(typing.List[AssessmentRunState]),
            ),
            (
                "duration_range",
                "durationRange",
                autoboto.TypeInfo(DurationRange),
            ),
            (
                "rules_package_arns",
                "rulesPackageArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "start_time_range",
                "startTimeRange",
                autoboto.TypeInfo(TimestampRange),
            ),
            (
                "completion_time_range",
                "completionTimeRange",
                autoboto.TypeInfo(TimestampRange),
            ),
            (
                "state_change_time_range",
                "stateChangeTimeRange",
                autoboto.TypeInfo(TimestampRange),
            ),
        ]

    # For a record to match a filter, an explicit value or a string containing a
    # wildcard that is specified for this data type property must match the value
    # of the **assessmentRunName** property of the AssessmentRun data type.
    name_pattern: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # For a record to match a filter, one of the values specified for this data
    # type property must be the exact match of the value of the
    # **assessmentRunState** property of the AssessmentRun data type.
    states: typing.List["AssessmentRunState"] = dataclasses.field(
        default_factory=list,
    )

    # For a record to match a filter, the value that is specified for this data
    # type property must inclusively match any value between the specified
    # minimum and maximum values of the **durationInSeconds** property of the
    # AssessmentRun data type.
    duration_range: "DurationRange" = dataclasses.field(default_factory=dict, )

    # For a record to match a filter, the value that is specified for this data
    # type property must be contained in the list of values of the
    # **rulesPackages** property of the AssessmentRun data type.
    rules_package_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # For a record to match a filter, the value that is specified for this data
    # type property must inclusively match any value between the specified
    # minimum and maximum values of the **startTime** property of the
    # AssessmentRun data type.
    start_time_range: "TimestampRange" = dataclasses.field(
        default_factory=dict,
    )

    # For a record to match a filter, the value that is specified for this data
    # type property must inclusively match any value between the specified
    # minimum and maximum values of the **completedAt** property of the
    # AssessmentRun data type.
    completion_time_range: "TimestampRange" = dataclasses.field(
        default_factory=dict,
    )

    # For a record to match a filter, the value that is specified for this data
    # type property must match the **stateChangedAt** property of the
    # AssessmentRun data type.
    state_change_time_range: "TimestampRange" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class AssessmentRunInProgressException(autoboto.ShapeBase):
    """
    You cannot perform a specified action if an assessment run is currently in
    progress.
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
                "assessment_run_arns",
                "assessmentRunArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "assessment_run_arns_truncated",
                "assessmentRunArnsTruncated",
                autoboto.TypeInfo(bool),
            ),
            (
                "can_retry",
                "canRetry",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARNs of the assessment runs that are currently in progress.
    assessment_run_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Boolean value that indicates whether the ARN list of the assessment runs is
    # truncated.
    assessment_run_arns_truncated: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # You can immediately retry your request.
    can_retry: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssessmentRunNotification(autoboto.ShapeBase):
    """
    Used as one of the elements of the AssessmentRun data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "date",
                "date",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "event",
                "event",
                autoboto.TypeInfo(InspectorEvent),
            ),
            (
                "error",
                "error",
                autoboto.TypeInfo(bool),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "sns_topic_arn",
                "snsTopicArn",
                autoboto.TypeInfo(str),
            ),
            (
                "sns_publish_status_code",
                "snsPublishStatusCode",
                autoboto.TypeInfo(AssessmentRunNotificationSnsStatusCode),
            ),
        ]

    # The date of the notification.
    date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The event for which a notification is sent.
    event: "InspectorEvent" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Boolean value that specifies whether the notification represents an
    # error.
    error: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The message included in the notification.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The SNS topic to which the SNS notification is sent.
    sns_topic_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status code of the SNS notification.
    sns_publish_status_code: "AssessmentRunNotificationSnsStatusCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class AssessmentRunNotificationSnsStatusCode(Enum):
    SUCCESS = "SUCCESS"
    TOPIC_DOES_NOT_EXIST = "TOPIC_DOES_NOT_EXIST"
    ACCESS_DENIED = "ACCESS_DENIED"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class AssessmentRunState(Enum):
    CREATED = "CREATED"
    START_DATA_COLLECTION_PENDING = "START_DATA_COLLECTION_PENDING"
    START_DATA_COLLECTION_IN_PROGRESS = "START_DATA_COLLECTION_IN_PROGRESS"
    COLLECTING_DATA = "COLLECTING_DATA"
    STOP_DATA_COLLECTION_PENDING = "STOP_DATA_COLLECTION_PENDING"
    DATA_COLLECTED = "DATA_COLLECTED"
    START_EVALUATING_RULES_PENDING = "START_EVALUATING_RULES_PENDING"
    EVALUATING_RULES = "EVALUATING_RULES"
    FAILED = "FAILED"
    ERROR = "ERROR"
    COMPLETED = "COMPLETED"
    COMPLETED_WITH_ERRORS = "COMPLETED_WITH_ERRORS"
    CANCELED = "CANCELED"


@dataclasses.dataclass
class AssessmentRunStateChange(autoboto.ShapeBase):
    """
    Used as one of the elements of the AssessmentRun data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state_changed_at",
                "stateChangedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "state",
                "state",
                autoboto.TypeInfo(AssessmentRunState),
            ),
        ]

    # The last time the assessment run state changed.
    state_changed_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The assessment run state.
    state: "AssessmentRunState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssessmentTarget(autoboto.ShapeBase):
    """
    Contains information about an Amazon Inspector application. This data type is
    used as the response element in the DescribeAssessmentTargets action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "updated_at",
                "updatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "resource_group_arn",
                "resourceGroupArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN that specifies the Amazon Inspector assessment target.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the Amazon Inspector assessment target.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time at which the assessment target is created.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time at which UpdateAssessmentTarget is called.
    updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN that specifies the resource group that is associated with the
    # assessment target.
    resource_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssessmentTargetFilter(autoboto.ShapeBase):
    """
    Used as the request parameter in the ListAssessmentTargets action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_target_name_pattern",
                "assessmentTargetNamePattern",
                autoboto.TypeInfo(str),
            ),
        ]

    # For a record to match a filter, an explicit value or a string that contains
    # a wildcard that is specified for this data type property must match the
    # value of the **assessmentTargetName** property of the AssessmentTarget data
    # type.
    assessment_target_name_pattern: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssessmentTemplate(autoboto.ShapeBase):
    """
    Contains information about an Amazon Inspector assessment template. This data
    type is used as the response element in the DescribeAssessmentTemplates action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "assessment_target_arn",
                "assessmentTargetArn",
                autoboto.TypeInfo(str),
            ),
            (
                "duration_in_seconds",
                "durationInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "rules_package_arns",
                "rulesPackageArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "user_attributes_for_findings",
                "userAttributesForFindings",
                autoboto.TypeInfo(typing.List[Attribute]),
            ),
            (
                "assessment_run_count",
                "assessmentRunCount",
                autoboto.TypeInfo(int),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_assessment_run_arn",
                "lastAssessmentRunArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the assessment template.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the assessment template.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the assessment target that corresponds to this assessment
    # template.
    assessment_target_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The duration in seconds specified for this assessment template. The default
    # value is 3600 seconds (one hour). The maximum value is 86400 seconds (one
    # day).
    duration_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The rules packages that are specified for this assessment template.
    rules_package_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The user-defined attributes that are assigned to every generated finding
    # from the assessment run that uses this assessment template.
    user_attributes_for_findings: typing.List["Attribute"] = dataclasses.field(
        default_factory=list,
    )

    # The number of existing assessment runs associated with this assessment
    # template. This value can be zero or a positive integer.
    assessment_run_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time at which the assessment template is created.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the most recent assessment run associated
    # with this assessment template. This value exists only when the value of
    # assessmentRunCount is greaterpa than zero.
    last_assessment_run_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssessmentTemplateFilter(autoboto.ShapeBase):
    """
    Used as the request parameter in the ListAssessmentTemplates action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name_pattern",
                "namePattern",
                autoboto.TypeInfo(str),
            ),
            (
                "duration_range",
                "durationRange",
                autoboto.TypeInfo(DurationRange),
            ),
            (
                "rules_package_arns",
                "rulesPackageArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # For a record to match a filter, an explicit value or a string that contains
    # a wildcard that is specified for this data type property must match the
    # value of the **assessmentTemplateName** property of the AssessmentTemplate
    # data type.
    name_pattern: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # For a record to match a filter, the value specified for this data type
    # property must inclusively match any value between the specified minimum and
    # maximum values of the **durationInSeconds** property of the
    # AssessmentTemplate data type.
    duration_range: "DurationRange" = dataclasses.field(default_factory=dict, )

    # For a record to match a filter, the values that are specified for this data
    # type property must be contained in the list of values of the
    # **rulesPackageArns** property of the AssessmentTemplate data type.
    rules_package_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AssetAttributes(autoboto.ShapeBase):
    """
    A collection of attributes of the host from which the finding is generated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_version",
                "schemaVersion",
                autoboto.TypeInfo(int),
            ),
            (
                "agent_id",
                "agentId",
                autoboto.TypeInfo(str),
            ),
            (
                "auto_scaling_group",
                "autoScalingGroup",
                autoboto.TypeInfo(str),
            ),
            (
                "ami_id",
                "amiId",
                autoboto.TypeInfo(str),
            ),
            (
                "hostname",
                "hostname",
                autoboto.TypeInfo(str),
            ),
            (
                "ipv4_addresses",
                "ipv4Addresses",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The schema version of this data type.
    schema_version: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the agent that is installed on the EC2 instance where the finding
    # is generated.
    agent_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Auto Scaling group of the EC2 instance where the finding is generated.
    auto_scaling_group: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the Amazon Machine Image (AMI) that is installed on the EC2
    # instance where the finding is generated.
    ami_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The hostname of the EC2 instance where the finding is generated.
    hostname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of IP v4 addresses of the EC2 instance where the finding is
    # generated.
    ipv4_addresses: typing.List[str] = dataclasses.field(default_factory=list, )


class AssetType(Enum):
    ec2_instance = "ec2-instance"


@dataclasses.dataclass
class Attribute(autoboto.ShapeBase):
    """
    This data type is used as a request parameter in the AddAttributesToFindings and
    CreateAssessmentTemplate actions.
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

    # The attribute key.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value assigned to the attribute key.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAssessmentTargetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_target_name",
                "assessmentTargetName",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_group_arn",
                "resourceGroupArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user-defined name that identifies the assessment target that you want
    # to create. The name must be unique within the AWS account.
    assessment_target_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN that specifies the resource group that is used to create the
    # assessment target. If resourceGroupArn is not specified, all EC2 instances
    # in the current AWS account and region are included in the assessment
    # target.
    resource_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateAssessmentTargetResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_target_arn",
                "assessmentTargetArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN that specifies the assessment target that is created.
    assessment_target_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateAssessmentTemplateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_target_arn",
                "assessmentTargetArn",
                autoboto.TypeInfo(str),
            ),
            (
                "assessment_template_name",
                "assessmentTemplateName",
                autoboto.TypeInfo(str),
            ),
            (
                "duration_in_seconds",
                "durationInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "rules_package_arns",
                "rulesPackageArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "user_attributes_for_findings",
                "userAttributesForFindings",
                autoboto.TypeInfo(typing.List[Attribute]),
            ),
        ]

    # The ARN that specifies the assessment target for which you want to create
    # the assessment template.
    assessment_target_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The user-defined name that identifies the assessment template that you want
    # to create. You can create several assessment templates for an assessment
    # target. The names of the assessment templates that correspond to a
    # particular assessment target must be unique.
    assessment_template_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The duration of the assessment run in seconds.
    duration_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARNs that specify the rules packages that you want to attach to the
    # assessment template.
    rules_package_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The user-defined attributes that are assigned to every finding that is
    # generated by the assessment run that uses this assessment template. An
    # attribute is a key and value pair (an Attribute object). Within an
    # assessment template, each key must be unique.
    user_attributes_for_findings: typing.List["Attribute"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateAssessmentTemplateResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_template_arn",
                "assessmentTemplateArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN that specifies the assessment template that is created.
    assessment_template_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateExclusionsPreviewRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_template_arn",
                "assessmentTemplateArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN that specifies the assessment template for which you want to create
    # an exclusions preview.
    assessment_template_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateExclusionsPreviewResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "preview_token",
                "previewToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the unique identifier of the requested exclusions preview. You
    # can use the unique identifier to retrieve the exclusions preview when
    # running the GetExclusionsPreview API.
    preview_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateResourceGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_group_tags",
                "resourceGroupTags",
                autoboto.TypeInfo(typing.List[ResourceGroupTag]),
            ),
        ]

    # A collection of keys and an array of possible values,
    # '[{"key":"key1","values":["Value1","Value2"]},{"key":"Key2","values":["Value3"]}]'.

    # For example,'[{"key":"Name","values":["TestEC2Instance"]}]'.
    resource_group_tags: typing.List["ResourceGroupTag"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateResourceGroupResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_group_arn",
                "resourceGroupArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN that specifies the resource group that is created.
    resource_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteAssessmentRunRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_run_arn",
                "assessmentRunArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN that specifies the assessment run that you want to delete.
    assessment_run_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteAssessmentTargetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_target_arn",
                "assessmentTargetArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN that specifies the assessment target that you want to delete.
    assessment_target_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteAssessmentTemplateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_template_arn",
                "assessmentTemplateArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN that specifies the assessment template that you want to delete.
    assessment_template_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAssessmentRunsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_run_arns",
                "assessmentRunArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN that specifies the assessment run that you want to describe.
    assessment_run_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeAssessmentRunsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_runs",
                "assessmentRuns",
                autoboto.TypeInfo(typing.List[AssessmentRun]),
            ),
            (
                "failed_items",
                "failedItems",
                autoboto.TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the assessment run.
    assessment_runs: typing.List["AssessmentRun"] = dataclasses.field(
        default_factory=list,
    )

    # Assessment run details that cannot be described. An error code is provided
    # for each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAssessmentTargetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_target_arns",
                "assessmentTargetArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ARNs that specifies the assessment targets that you want to describe.
    assessment_target_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeAssessmentTargetsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_targets",
                "assessmentTargets",
                autoboto.TypeInfo(typing.List[AssessmentTarget]),
            ),
            (
                "failed_items",
                "failedItems",
                autoboto.TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the assessment targets.
    assessment_targets: typing.List["AssessmentTarget"] = dataclasses.field(
        default_factory=list,
    )

    # Assessment target details that cannot be described. An error code is
    # provided for each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAssessmentTemplatesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_template_arns",
                "assessmentTemplateArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    assessment_template_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeAssessmentTemplatesResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_templates",
                "assessmentTemplates",
                autoboto.TypeInfo(typing.List[AssessmentTemplate]),
            ),
            (
                "failed_items",
                "failedItems",
                autoboto.TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the assessment templates.
    assessment_templates: typing.List["AssessmentTemplate"] = dataclasses.field(
        default_factory=list,
    )

    # Assessment template details that cannot be described. An error code is
    # provided for each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeCrossAccountAccessRoleResponse(autoboto.OutputShapeBase):
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
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "valid",
                "valid",
                autoboto.TypeInfo(bool),
            ),
            (
                "registered_at",
                "registeredAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN that specifies the IAM role that Amazon Inspector uses to access
    # your AWS account.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Boolean value that specifies whether the IAM role has the necessary
    # policies attached to enable Amazon Inspector to access your AWS account.
    valid: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date when the cross-account access role was registered.
    registered_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeExclusionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "exclusion_arns",
                "exclusionArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "locale",
                "locale",
                autoboto.TypeInfo(Locale),
            ),
        ]

    # The list of ARNs that specify the exclusions that you want to describe.
    exclusion_arns: typing.List[str] = dataclasses.field(default_factory=list, )

    # The locale into which you want to translate the exclusion's title,
    # description, and recommendation.
    locale: "Locale" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeExclusionsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "exclusions",
                "exclusions",
                autoboto.TypeInfo(typing.Dict[str, Exclusion]),
            ),
            (
                "failed_items",
                "failedItems",
                autoboto.TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the exclusions.
    exclusions: typing.Dict[str, "Exclusion"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Exclusion details that cannot be described. An error code is provided for
    # each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeFindingsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "finding_arns",
                "findingArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "locale",
                "locale",
                autoboto.TypeInfo(Locale),
            ),
        ]

    # The ARN that specifies the finding that you want to describe.
    finding_arns: typing.List[str] = dataclasses.field(default_factory=list, )

    # The locale into which you want to translate a finding description,
    # recommendation, and the short description that identifies the finding.
    locale: "Locale" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFindingsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "findings",
                "findings",
                autoboto.TypeInfo(typing.List[Finding]),
            ),
            (
                "failed_items",
                "failedItems",
                autoboto.TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the finding.
    findings: typing.List["Finding"] = dataclasses.field(default_factory=list, )

    # Finding details that cannot be described. An error code is provided for
    # each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeResourceGroupsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_group_arns",
                "resourceGroupArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN that specifies the resource group that you want to describe.
    resource_group_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeResourceGroupsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_groups",
                "resourceGroups",
                autoboto.TypeInfo(typing.List[ResourceGroup]),
            ),
            (
                "failed_items",
                "failedItems",
                autoboto.TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about a resource group.
    resource_groups: typing.List["ResourceGroup"] = dataclasses.field(
        default_factory=list,
    )

    # Resource group details that cannot be described. An error code is provided
    # for each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeRulesPackagesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rules_package_arns",
                "rulesPackageArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "locale",
                "locale",
                autoboto.TypeInfo(Locale),
            ),
        ]

    # The ARN that specifies the rules package that you want to describe.
    rules_package_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The locale that you want to translate a rules package description into.
    locale: "Locale" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRulesPackagesResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rules_packages",
                "rulesPackages",
                autoboto.TypeInfo(typing.List[RulesPackage]),
            ),
            (
                "failed_items",
                "failedItems",
                autoboto.TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the rules package.
    rules_packages: typing.List["RulesPackage"] = dataclasses.field(
        default_factory=list,
    )

    # Rules package details that cannot be described. An error code is provided
    # for each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DurationRange(autoboto.ShapeBase):
    """
    This data type is used in the AssessmentTemplateFilter data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "min_seconds",
                "minSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "max_seconds",
                "maxSeconds",
                autoboto.TypeInfo(int),
            ),
        ]

    # The minimum value of the duration range. Must be greater than zero.
    min_seconds: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum value of the duration range. Must be less than or equal to
    # 604800 seconds (1 week).
    max_seconds: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventSubscription(autoboto.ShapeBase):
    """
    This data type is used in the Subscription data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event",
                "event",
                autoboto.TypeInfo(InspectorEvent),
            ),
            (
                "subscribed_at",
                "subscribedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The event for which Amazon Simple Notification Service (SNS) notifications
    # are sent.
    event: "InspectorEvent" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time at which SubscribeToEvent is called.
    subscribed_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Exclusion(autoboto.ShapeBase):
    """
    Contains information about what was excluded from an assessment run.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "title",
                "title",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "recommendation",
                "recommendation",
                autoboto.TypeInfo(str),
            ),
            (
                "scopes",
                "scopes",
                autoboto.TypeInfo(typing.List[Scope]),
            ),
            (
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.List[Attribute]),
            ),
        ]

    # The ARN that specifies the exclusion.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the exclusion.
    title: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the exclusion.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The recommendation for the exclusion.
    recommendation: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS resources for which the exclusion pertains.
    scopes: typing.List["Scope"] = dataclasses.field(default_factory=list, )

    # The system-defined attributes for the exclusion.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ExclusionPreview(autoboto.ShapeBase):
    """
    Contains information about what is excluded from an assessment run given the
    current state of the assessment template.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "title",
                "title",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "recommendation",
                "recommendation",
                autoboto.TypeInfo(str),
            ),
            (
                "scopes",
                "scopes",
                autoboto.TypeInfo(typing.List[Scope]),
            ),
            (
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.List[Attribute]),
            ),
        ]

    # The name of the exclusion preview.
    title: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the exclusion preview.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The recommendation for the exclusion preview.
    recommendation: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS resources for which the exclusion preview pertains.
    scopes: typing.List["Scope"] = dataclasses.field(default_factory=list, )

    # The system-defined attributes for the exclusion preview.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class FailedItemDetails(autoboto.ShapeBase):
    """
    Includes details about the failed items.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failure_code",
                "failureCode",
                autoboto.TypeInfo(FailedItemErrorCode),
            ),
            (
                "retryable",
                "retryable",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The status code of a failed item.
    failure_code: "FailedItemErrorCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether you can immediately retry a request for this item for a
    # specified resource.
    retryable: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class FailedItemErrorCode(Enum):
    INVALID_ARN = "INVALID_ARN"
    DUPLICATE_ARN = "DUPLICATE_ARN"
    ITEM_DOES_NOT_EXIST = "ITEM_DOES_NOT_EXIST"
    ACCESS_DENIED = "ACCESS_DENIED"
    LIMIT_EXCEEDED = "LIMIT_EXCEEDED"
    INTERNAL_ERROR = "INTERNAL_ERROR"


@dataclasses.dataclass
class Finding(autoboto.ShapeBase):
    """
    Contains information about an Amazon Inspector finding. This data type is used
    as the response element in the DescribeFindings action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.List[Attribute]),
            ),
            (
                "user_attributes",
                "userAttributes",
                autoboto.TypeInfo(typing.List[Attribute]),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "updated_at",
                "updatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "schema_version",
                "schemaVersion",
                autoboto.TypeInfo(int),
            ),
            (
                "service",
                "service",
                autoboto.TypeInfo(str),
            ),
            (
                "service_attributes",
                "serviceAttributes",
                autoboto.TypeInfo(InspectorServiceAttributes),
            ),
            (
                "asset_type",
                "assetType",
                autoboto.TypeInfo(AssetType),
            ),
            (
                "asset_attributes",
                "assetAttributes",
                autoboto.TypeInfo(AssetAttributes),
            ),
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "title",
                "title",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "recommendation",
                "recommendation",
                autoboto.TypeInfo(str),
            ),
            (
                "severity",
                "severity",
                autoboto.TypeInfo(Severity),
            ),
            (
                "numeric_severity",
                "numericSeverity",
                autoboto.TypeInfo(float),
            ),
            (
                "confidence",
                "confidence",
                autoboto.TypeInfo(int),
            ),
            (
                "indicator_of_compromise",
                "indicatorOfCompromise",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ARN that specifies the finding.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The system-defined attributes for the finding.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default_factory=list,
    )

    # The user-defined attributes that are assigned to the finding.
    user_attributes: typing.List["Attribute"] = dataclasses.field(
        default_factory=list,
    )

    # The time when the finding was generated.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time when AddAttributesToFindings is called.
    updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The schema version of this data type.
    schema_version: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The data element is set to "Inspector".
    service: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This data type is used in the Finding data type.
    service_attributes: "InspectorServiceAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # The type of the host from which the finding is generated.
    asset_type: "AssetType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A collection of attributes of the host from which the finding is generated.
    asset_attributes: "AssetAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the finding.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the finding.
    title: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the finding.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The recommendation for the finding.
    recommendation: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The finding severity. Values can be set to High, Medium, Low, and
    # Informational.
    severity: "Severity" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The numeric value of the finding severity.
    numeric_severity: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This data element is currently not used.
    confidence: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This data element is currently not used.
    indicator_of_compromise: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FindingFilter(autoboto.ShapeBase):
    """
    This data type is used as a request parameter in the ListFindings action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_ids",
                "agentIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "auto_scaling_groups",
                "autoScalingGroups",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "rule_names",
                "ruleNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "severities",
                "severities",
                autoboto.TypeInfo(typing.List[Severity]),
            ),
            (
                "rules_package_arns",
                "rulesPackageArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.List[Attribute]),
            ),
            (
                "user_attributes",
                "userAttributes",
                autoboto.TypeInfo(typing.List[Attribute]),
            ),
            (
                "creation_time_range",
                "creationTimeRange",
                autoboto.TypeInfo(TimestampRange),
            ),
        ]

    # For a record to match a filter, one of the values that is specified for
    # this data type property must be the exact match of the value of the
    # **agentId** property of the Finding data type.
    agent_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # For a record to match a filter, one of the values that is specified for
    # this data type property must be the exact match of the value of the
    # **autoScalingGroup** property of the Finding data type.
    auto_scaling_groups: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # For a record to match a filter, one of the values that is specified for
    # this data type property must be the exact match of the value of the
    # **ruleName** property of the Finding data type.
    rule_names: typing.List[str] = dataclasses.field(default_factory=list, )

    # For a record to match a filter, one of the values that is specified for
    # this data type property must be the exact match of the value of the
    # **severity** property of the Finding data type.
    severities: typing.List["Severity"] = dataclasses.field(
        default_factory=list,
    )

    # For a record to match a filter, one of the values that is specified for
    # this data type property must be the exact match of the value of the
    # **rulesPackageArn** property of the Finding data type.
    rules_package_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # For a record to match a filter, the list of values that are specified for
    # this data type property must be contained in the list of values of the
    # **attributes** property of the Finding data type.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default_factory=list,
    )

    # For a record to match a filter, the value that is specified for this data
    # type property must be contained in the list of values of the
    # **userAttributes** property of the Finding data type.
    user_attributes: typing.List["Attribute"] = dataclasses.field(
        default_factory=list,
    )

    # The time range during which the finding is generated.
    creation_time_range: "TimestampRange" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetAssessmentReportRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_run_arn",
                "assessmentRunArn",
                autoboto.TypeInfo(str),
            ),
            (
                "report_file_format",
                "reportFileFormat",
                autoboto.TypeInfo(ReportFileFormat),
            ),
            (
                "report_type",
                "reportType",
                autoboto.TypeInfo(ReportType),
            ),
        ]

    # The ARN that specifies the assessment run for which you want to generate a
    # report.
    assessment_run_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the file format (html or pdf) of the assessment report that you
    # want to generate.
    report_file_format: "ReportFileFormat" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the type of the assessment report that you want to generate.
    # There are two types of assessment reports: a finding report and a full
    # report. For more information, see [Assessment
    # Reports](http://docs.aws.amazon.com/inspector/latest/userguide/inspector_reports.html).
    report_type: "ReportType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetAssessmentReportResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(ReportStatus),
            ),
            (
                "url",
                "url",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the status of the request to generate an assessment report.
    status: "ReportStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the URL where you can find the generated assessment report. This
    # parameter is only returned if the report is successfully generated.
    url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetExclusionsPreviewRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_template_arn",
                "assessmentTemplateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "preview_token",
                "previewToken",
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
                "locale",
                "locale",
                autoboto.TypeInfo(Locale),
            ),
        ]

    # The ARN that specifies the assessment template for which the exclusions
    # preview was requested.
    assessment_template_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The unique identifier associated of the exclusions preview.
    preview_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the GetExclusionsPreviewRequest
    # action. Subsequent calls to the action fill nextToken in the request with
    # the value of nextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 100. The maximum value is 500.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The locale into which you want to translate the exclusion's title,
    # description, and recommendation.
    locale: "Locale" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetExclusionsPreviewResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "preview_status",
                "previewStatus",
                autoboto.TypeInfo(PreviewStatus),
            ),
            (
                "exclusion_previews",
                "exclusionPreviews",
                autoboto.TypeInfo(typing.List[ExclusionPreview]),
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

    # Specifies the status of the request to generate an exclusions preview.
    preview_status: "PreviewStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the exclusions included in the preview.
    exclusion_previews: typing.List["ExclusionPreview"] = dataclasses.field(
        default_factory=list,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameters is present in the response and contains the value to use for the
    # nextToken parameter in a subsequent pagination request. If there is no more
    # data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTelemetryMetadataRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_run_arn",
                "assessmentRunArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN that specifies the assessment run that has the telemetry data that
    # you want to obtain.
    assessment_run_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetTelemetryMetadataResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "telemetry_metadata",
                "telemetryMetadata",
                autoboto.TypeInfo(typing.List[TelemetryMetadata]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Telemetry details.
    telemetry_metadata: typing.List["TelemetryMetadata"] = dataclasses.field(
        default_factory=list,
    )


class InspectorEvent(Enum):
    ASSESSMENT_RUN_STARTED = "ASSESSMENT_RUN_STARTED"
    ASSESSMENT_RUN_COMPLETED = "ASSESSMENT_RUN_COMPLETED"
    ASSESSMENT_RUN_STATE_CHANGED = "ASSESSMENT_RUN_STATE_CHANGED"
    FINDING_REPORTED = "FINDING_REPORTED"
    OTHER = "OTHER"


@dataclasses.dataclass
class InspectorServiceAttributes(autoboto.ShapeBase):
    """
    This data type is used in the Finding data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_version",
                "schemaVersion",
                autoboto.TypeInfo(int),
            ),
            (
                "assessment_run_arn",
                "assessmentRunArn",
                autoboto.TypeInfo(str),
            ),
            (
                "rules_package_arn",
                "rulesPackageArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The schema version of this data type.
    schema_version: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the assessment run during which the finding is generated.
    assessment_run_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the rules package that is used to generate the finding.
    rules_package_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalException(autoboto.ShapeBase):
    """
    Internal server error.
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
                "can_retry",
                "canRetry",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # You can immediately retry your request.
    can_retry: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class InvalidCrossAccountRoleErrorCode(Enum):
    ROLE_DOES_NOT_EXIST_OR_INVALID_TRUST_RELATIONSHIP = "ROLE_DOES_NOT_EXIST_OR_INVALID_TRUST_RELATIONSHIP"
    ROLE_DOES_NOT_HAVE_CORRECT_POLICY = "ROLE_DOES_NOT_HAVE_CORRECT_POLICY"


@dataclasses.dataclass
class InvalidCrossAccountRoleException(autoboto.ShapeBase):
    """
    Amazon Inspector cannot assume the cross-account role that it needs to list your
    EC2 instances during the assessment run.
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
                "error_code",
                "errorCode",
                autoboto.TypeInfo(InvalidCrossAccountRoleErrorCode),
            ),
            (
                "can_retry",
                "canRetry",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Code that indicates the type of error that is generated.
    error_code: "InvalidCrossAccountRoleErrorCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # You can immediately retry your request.
    can_retry: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class InvalidInputErrorCode(Enum):
    INVALID_ASSESSMENT_TARGET_ARN = "INVALID_ASSESSMENT_TARGET_ARN"
    INVALID_ASSESSMENT_TEMPLATE_ARN = "INVALID_ASSESSMENT_TEMPLATE_ARN"
    INVALID_ASSESSMENT_RUN_ARN = "INVALID_ASSESSMENT_RUN_ARN"
    INVALID_FINDING_ARN = "INVALID_FINDING_ARN"
    INVALID_RESOURCE_GROUP_ARN = "INVALID_RESOURCE_GROUP_ARN"
    INVALID_RULES_PACKAGE_ARN = "INVALID_RULES_PACKAGE_ARN"
    INVALID_RESOURCE_ARN = "INVALID_RESOURCE_ARN"
    INVALID_SNS_TOPIC_ARN = "INVALID_SNS_TOPIC_ARN"
    INVALID_IAM_ROLE_ARN = "INVALID_IAM_ROLE_ARN"
    INVALID_ASSESSMENT_TARGET_NAME = "INVALID_ASSESSMENT_TARGET_NAME"
    INVALID_ASSESSMENT_TARGET_NAME_PATTERN = "INVALID_ASSESSMENT_TARGET_NAME_PATTERN"
    INVALID_ASSESSMENT_TEMPLATE_NAME = "INVALID_ASSESSMENT_TEMPLATE_NAME"
    INVALID_ASSESSMENT_TEMPLATE_NAME_PATTERN = "INVALID_ASSESSMENT_TEMPLATE_NAME_PATTERN"
    INVALID_ASSESSMENT_TEMPLATE_DURATION = "INVALID_ASSESSMENT_TEMPLATE_DURATION"
    INVALID_ASSESSMENT_TEMPLATE_DURATION_RANGE = "INVALID_ASSESSMENT_TEMPLATE_DURATION_RANGE"
    INVALID_ASSESSMENT_RUN_DURATION_RANGE = "INVALID_ASSESSMENT_RUN_DURATION_RANGE"
    INVALID_ASSESSMENT_RUN_START_TIME_RANGE = "INVALID_ASSESSMENT_RUN_START_TIME_RANGE"
    INVALID_ASSESSMENT_RUN_COMPLETION_TIME_RANGE = "INVALID_ASSESSMENT_RUN_COMPLETION_TIME_RANGE"
    INVALID_ASSESSMENT_RUN_STATE_CHANGE_TIME_RANGE = "INVALID_ASSESSMENT_RUN_STATE_CHANGE_TIME_RANGE"
    INVALID_ASSESSMENT_RUN_STATE = "INVALID_ASSESSMENT_RUN_STATE"
    INVALID_TAG = "INVALID_TAG"
    INVALID_TAG_KEY = "INVALID_TAG_KEY"
    INVALID_TAG_VALUE = "INVALID_TAG_VALUE"
    INVALID_RESOURCE_GROUP_TAG_KEY = "INVALID_RESOURCE_GROUP_TAG_KEY"
    INVALID_RESOURCE_GROUP_TAG_VALUE = "INVALID_RESOURCE_GROUP_TAG_VALUE"
    INVALID_ATTRIBUTE = "INVALID_ATTRIBUTE"
    INVALID_USER_ATTRIBUTE = "INVALID_USER_ATTRIBUTE"
    INVALID_USER_ATTRIBUTE_KEY = "INVALID_USER_ATTRIBUTE_KEY"
    INVALID_USER_ATTRIBUTE_VALUE = "INVALID_USER_ATTRIBUTE_VALUE"
    INVALID_PAGINATION_TOKEN = "INVALID_PAGINATION_TOKEN"
    INVALID_MAX_RESULTS = "INVALID_MAX_RESULTS"
    INVALID_AGENT_ID = "INVALID_AGENT_ID"
    INVALID_AUTO_SCALING_GROUP = "INVALID_AUTO_SCALING_GROUP"
    INVALID_RULE_NAME = "INVALID_RULE_NAME"
    INVALID_SEVERITY = "INVALID_SEVERITY"
    INVALID_LOCALE = "INVALID_LOCALE"
    INVALID_EVENT = "INVALID_EVENT"
    ASSESSMENT_TARGET_NAME_ALREADY_TAKEN = "ASSESSMENT_TARGET_NAME_ALREADY_TAKEN"
    ASSESSMENT_TEMPLATE_NAME_ALREADY_TAKEN = "ASSESSMENT_TEMPLATE_NAME_ALREADY_TAKEN"
    INVALID_NUMBER_OF_ASSESSMENT_TARGET_ARNS = "INVALID_NUMBER_OF_ASSESSMENT_TARGET_ARNS"
    INVALID_NUMBER_OF_ASSESSMENT_TEMPLATE_ARNS = "INVALID_NUMBER_OF_ASSESSMENT_TEMPLATE_ARNS"
    INVALID_NUMBER_OF_ASSESSMENT_RUN_ARNS = "INVALID_NUMBER_OF_ASSESSMENT_RUN_ARNS"
    INVALID_NUMBER_OF_FINDING_ARNS = "INVALID_NUMBER_OF_FINDING_ARNS"
    INVALID_NUMBER_OF_RESOURCE_GROUP_ARNS = "INVALID_NUMBER_OF_RESOURCE_GROUP_ARNS"
    INVALID_NUMBER_OF_RULES_PACKAGE_ARNS = "INVALID_NUMBER_OF_RULES_PACKAGE_ARNS"
    INVALID_NUMBER_OF_ASSESSMENT_RUN_STATES = "INVALID_NUMBER_OF_ASSESSMENT_RUN_STATES"
    INVALID_NUMBER_OF_TAGS = "INVALID_NUMBER_OF_TAGS"
    INVALID_NUMBER_OF_RESOURCE_GROUP_TAGS = "INVALID_NUMBER_OF_RESOURCE_GROUP_TAGS"
    INVALID_NUMBER_OF_ATTRIBUTES = "INVALID_NUMBER_OF_ATTRIBUTES"
    INVALID_NUMBER_OF_USER_ATTRIBUTES = "INVALID_NUMBER_OF_USER_ATTRIBUTES"
    INVALID_NUMBER_OF_AGENT_IDS = "INVALID_NUMBER_OF_AGENT_IDS"
    INVALID_NUMBER_OF_AUTO_SCALING_GROUPS = "INVALID_NUMBER_OF_AUTO_SCALING_GROUPS"
    INVALID_NUMBER_OF_RULE_NAMES = "INVALID_NUMBER_OF_RULE_NAMES"
    INVALID_NUMBER_OF_SEVERITIES = "INVALID_NUMBER_OF_SEVERITIES"


@dataclasses.dataclass
class InvalidInputException(autoboto.ShapeBase):
    """
    The request was rejected because an invalid or out-of-range value was supplied
    for an input parameter.
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
                "error_code",
                "errorCode",
                autoboto.TypeInfo(InvalidInputErrorCode),
            ),
            (
                "can_retry",
                "canRetry",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Code that indicates the type of error that is generated.
    error_code: "InvalidInputErrorCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # You can immediately retry your request.
    can_retry: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class LimitExceededErrorCode(Enum):
    ASSESSMENT_TARGET_LIMIT_EXCEEDED = "ASSESSMENT_TARGET_LIMIT_EXCEEDED"
    ASSESSMENT_TEMPLATE_LIMIT_EXCEEDED = "ASSESSMENT_TEMPLATE_LIMIT_EXCEEDED"
    ASSESSMENT_RUN_LIMIT_EXCEEDED = "ASSESSMENT_RUN_LIMIT_EXCEEDED"
    RESOURCE_GROUP_LIMIT_EXCEEDED = "RESOURCE_GROUP_LIMIT_EXCEEDED"
    EVENT_SUBSCRIPTION_LIMIT_EXCEEDED = "EVENT_SUBSCRIPTION_LIMIT_EXCEEDED"


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    The request was rejected because it attempted to create resources beyond the
    current AWS account limits. The error code describes the limit exceeded.
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
                "error_code",
                "errorCode",
                autoboto.TypeInfo(LimitExceededErrorCode),
            ),
            (
                "can_retry",
                "canRetry",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Code that indicates the type of error that is generated.
    error_code: "LimitExceededErrorCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # You can immediately retry your request.
    can_retry: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssessmentRunAgentsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_run_arn",
                "assessmentRunArn",
                autoboto.TypeInfo(str),
            ),
            (
                "filter",
                "filter",
                autoboto.TypeInfo(AgentFilter),
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

    # The ARN that specifies the assessment run whose agents you want to list.
    assessment_run_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # You can use this parameter to specify a subset of data to be included in
    # the action's response.

    # For a record to match a filter, all specified filter attributes must match.
    # When multiple values are specified for a filter attribute, any of the
    # values can match.
    filter: "AgentFilter" = dataclasses.field(default_factory=dict, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the **ListAssessmentRunAgents**
    # action. Subsequent calls to the action fill **nextToken** in the request
    # with the value of **NextToken** from the previous response to continue
    # listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items that you
    # want in the response. The default value is 10. The maximum value is 500.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssessmentRunAgentsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_run_agents",
                "assessmentRunAgents",
                autoboto.TypeInfo(typing.List[AssessmentRunAgent]),
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

    # A list of ARNs that specifies the agents returned by the action.
    assessment_run_agents: typing.List["AssessmentRunAgent"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # **nextToken** parameter in a subsequent pagination request. If there is no
    # more data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssessmentRunsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_template_arns",
                "assessmentTemplateArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "filter",
                "filter",
                autoboto.TypeInfo(AssessmentRunFilter),
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

    # The ARNs that specify the assessment templates whose assessment runs you
    # want to list.
    assessment_template_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # You can use this parameter to specify a subset of data to be included in
    # the action's response.

    # For a record to match a filter, all specified filter attributes must match.
    # When multiple values are specified for a filter attribute, any of the
    # values can match.
    filter: "AssessmentRunFilter" = dataclasses.field(default_factory=dict, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the **ListAssessmentRuns** action.
    # Subsequent calls to the action fill **nextToken** in the request with the
    # value of **NextToken** from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items that you
    # want in the response. The default value is 10. The maximum value is 500.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssessmentRunsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_run_arns",
                "assessmentRunArns",
                autoboto.TypeInfo(typing.List[str]),
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

    # A list of ARNs that specifies the assessment runs that are returned by the
    # action.
    assessment_run_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # **nextToken** parameter in a subsequent pagination request. If there is no
    # more data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssessmentTargetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "filter",
                autoboto.TypeInfo(AssessmentTargetFilter),
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

    # You can use this parameter to specify a subset of data to be included in
    # the action's response.

    # For a record to match a filter, all specified filter attributes must match.
    # When multiple values are specified for a filter attribute, any of the
    # values can match.
    filter: "AssessmentTargetFilter" = dataclasses.field(default_factory=dict, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the **ListAssessmentTargets**
    # action. Subsequent calls to the action fill **nextToken** in the request
    # with the value of **NextToken** from the previous response to continue
    # listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 10. The maximum value is 500.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssessmentTargetsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_target_arns",
                "assessmentTargetArns",
                autoboto.TypeInfo(typing.List[str]),
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

    # A list of ARNs that specifies the assessment targets that are returned by
    # the action.
    assessment_target_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # **nextToken** parameter in a subsequent pagination request. If there is no
    # more data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssessmentTemplatesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_target_arns",
                "assessmentTargetArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "filter",
                "filter",
                autoboto.TypeInfo(AssessmentTemplateFilter),
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

    # A list of ARNs that specifies the assessment targets whose assessment
    # templates you want to list.
    assessment_target_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # You can use this parameter to specify a subset of data to be included in
    # the action's response.

    # For a record to match a filter, all specified filter attributes must match.
    # When multiple values are specified for a filter attribute, any of the
    # values can match.
    filter: "AssessmentTemplateFilter" = dataclasses.field(
        default_factory=dict,
    )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the **ListAssessmentTemplates**
    # action. Subsequent calls to the action fill **nextToken** in the request
    # with the value of **NextToken** from the previous response to continue
    # listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 10. The maximum value is 500.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssessmentTemplatesResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_template_arns",
                "assessmentTemplateArns",
                autoboto.TypeInfo(typing.List[str]),
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

    # A list of ARNs that specifies the assessment templates returned by the
    # action.
    assessment_template_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # **nextToken** parameter in a subsequent pagination request. If there is no
    # more data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListEventSubscriptionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
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

    # The ARN of the assessment template for which you want to list the existing
    # event subscriptions.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the **ListEventSubscriptions**
    # action. Subsequent calls to the action fill **nextToken** in the request
    # with the value of **NextToken** from the previous response to continue
    # listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 10. The maximum value is 500.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListEventSubscriptionsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "subscriptions",
                "subscriptions",
                autoboto.TypeInfo(typing.List[Subscription]),
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

    # Details of the returned event subscriptions.
    subscriptions: typing.List["Subscription"] = dataclasses.field(
        default_factory=list,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # **nextToken** parameter in a subsequent pagination request. If there is no
    # more data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListExclusionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_run_arn",
                "assessmentRunArn",
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

    # The ARN of the assessment run that generated the exclusions that you want
    # to list.
    assessment_run_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the ListExclusionsRequest action.
    # Subsequent calls to the action fill nextToken in the request with the value
    # of nextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 100. The maximum value is 500.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListExclusionsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "exclusion_arns",
                "exclusionArns",
                autoboto.TypeInfo(typing.List[str]),
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

    # A list of exclusions' ARNs returned by the action.
    exclusion_arns: typing.List[str] = dataclasses.field(default_factory=list, )

    # When a response is generated, if there is more data to be listed, this
    # parameters is present in the response and contains the value to use for the
    # nextToken parameter in a subsequent pagination request. If there is no more
    # data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFindingsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_run_arns",
                "assessmentRunArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "filter",
                "filter",
                autoboto.TypeInfo(FindingFilter),
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

    # The ARNs of the assessment runs that generate the findings that you want to
    # list.
    assessment_run_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # You can use this parameter to specify a subset of data to be included in
    # the action's response.

    # For a record to match a filter, all specified filter attributes must match.
    # When multiple values are specified for a filter attribute, any of the
    # values can match.
    filter: "FindingFilter" = dataclasses.field(default_factory=dict, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the **ListFindings** action.
    # Subsequent calls to the action fill **nextToken** in the request with the
    # value of **NextToken** from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 10. The maximum value is 500.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFindingsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "finding_arns",
                "findingArns",
                autoboto.TypeInfo(typing.List[str]),
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

    # A list of ARNs that specifies the findings returned by the action.
    finding_arns: typing.List[str] = dataclasses.field(default_factory=list, )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # **nextToken** parameter in a subsequent pagination request. If there is no
    # more data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRulesPackagesRequest(autoboto.ShapeBase):
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

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the **ListRulesPackages** action.
    # Subsequent calls to the action fill **nextToken** in the request with the
    # value of **NextToken** from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 10. The maximum value is 500.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRulesPackagesResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rules_package_arns",
                "rulesPackageArns",
                autoboto.TypeInfo(typing.List[str]),
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

    # The list of ARNs that specifies the rules packages returned by the action.
    rules_package_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # **nextToken** parameter in a subsequent pagination request. If there is no
    # more data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN that specifies the assessment template whose tags you want to list.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A collection of key and value pairs.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


class Locale(Enum):
    EN_US = "EN_US"


class NoSuchEntityErrorCode(Enum):
    ASSESSMENT_TARGET_DOES_NOT_EXIST = "ASSESSMENT_TARGET_DOES_NOT_EXIST"
    ASSESSMENT_TEMPLATE_DOES_NOT_EXIST = "ASSESSMENT_TEMPLATE_DOES_NOT_EXIST"
    ASSESSMENT_RUN_DOES_NOT_EXIST = "ASSESSMENT_RUN_DOES_NOT_EXIST"
    FINDING_DOES_NOT_EXIST = "FINDING_DOES_NOT_EXIST"
    RESOURCE_GROUP_DOES_NOT_EXIST = "RESOURCE_GROUP_DOES_NOT_EXIST"
    RULES_PACKAGE_DOES_NOT_EXIST = "RULES_PACKAGE_DOES_NOT_EXIST"
    SNS_TOPIC_DOES_NOT_EXIST = "SNS_TOPIC_DOES_NOT_EXIST"
    IAM_ROLE_DOES_NOT_EXIST = "IAM_ROLE_DOES_NOT_EXIST"


@dataclasses.dataclass
class NoSuchEntityException(autoboto.ShapeBase):
    """
    The request was rejected because it referenced an entity that does not exist.
    The error code describes the entity.
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
                "error_code",
                "errorCode",
                autoboto.TypeInfo(NoSuchEntityErrorCode),
            ),
            (
                "can_retry",
                "canRetry",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Code that indicates the type of error that is generated.
    error_code: "NoSuchEntityErrorCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # You can immediately retry your request.
    can_retry: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PreviewAgentsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "preview_agents_arn",
                "previewAgentsArn",
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

    # The ARN of the assessment target whose agents you want to preview.
    preview_agents_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the **PreviewAgents** action.
    # Subsequent calls to the action fill **nextToken** in the request with the
    # value of **NextToken** from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 10. The maximum value is 500.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PreviewAgentsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "agent_previews",
                "agentPreviews",
                autoboto.TypeInfo(typing.List[AgentPreview]),
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

    # The resulting list of agents.
    agent_previews: typing.List["AgentPreview"] = dataclasses.field(
        default_factory=list,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # **nextToken** parameter in a subsequent pagination request. If there is no
    # more data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PreviewGenerationInProgressException(autoboto.ShapeBase):
    """
    The request is rejected. The specified assessment template is currently
    generating an exclusions preview.
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


class PreviewStatus(Enum):
    WORK_IN_PROGRESS = "WORK_IN_PROGRESS"
    COMPLETED = "COMPLETED"


@dataclasses.dataclass
class RegisterCrossAccountAccessRoleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the IAM role that grants Amazon Inspector access to AWS Services
    # needed to perform security assessments.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveAttributesFromFindingsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "finding_arns",
                "findingArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "attribute_keys",
                "attributeKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ARNs that specify the findings that you want to remove attributes from.
    finding_arns: typing.List[str] = dataclasses.field(default_factory=list, )

    # The array of attribute keys that you want to remove from specified
    # findings.
    attribute_keys: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class RemoveAttributesFromFindingsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_items",
                "failedItems",
                autoboto.TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Attributes details that cannot be described. An error code is provided for
    # each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ReportFileFormat(Enum):
    HTML = "HTML"
    PDF = "PDF"


class ReportStatus(Enum):
    WORK_IN_PROGRESS = "WORK_IN_PROGRESS"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"


class ReportType(Enum):
    FINDING = "FINDING"
    FULL = "FULL"


@dataclasses.dataclass
class ResourceGroup(autoboto.ShapeBase):
    """
    Contains information about a resource group. The resource group defines a set of
    tags that, when queried, identify the AWS resources that make up the assessment
    target. This data type is used as the response element in the
    DescribeResourceGroups action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[ResourceGroupTag]),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ARN of the resource group.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tags (key and value pairs) of the resource group. This data type
    # property is used in the CreateResourceGroup action.
    tags: typing.List["ResourceGroupTag"] = dataclasses.field(
        default_factory=list,
    )

    # The time at which resource group is created.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceGroupTag(autoboto.ShapeBase):
    """
    This data type is used as one of the elements of the ResourceGroup data type.
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

    # A tag key.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value assigned to a tag key.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RulesPackage(autoboto.ShapeBase):
    """
    Contains information about an Amazon Inspector rules package. This data type is
    used as the response element in the DescribeRulesPackages action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(str),
            ),
            (
                "provider",
                "provider",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the rules package.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the rules package.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version ID of the rules package.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The provider of the rules package.
    provider: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the rules package.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Scope(autoboto.ShapeBase):
    """
    This data type contains key-value pairs that identify various Amazon resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                autoboto.TypeInfo(ScopeType),
            ),
            (
                "value",
                "value",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of the scope.
    key: "ScopeType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The resource identifier for the specified scope type.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ScopeType(Enum):
    INSTANCE_ID = "INSTANCE_ID"
    RULES_PACKAGE_ARN = "RULES_PACKAGE_ARN"


@dataclasses.dataclass
class ServiceTemporarilyUnavailableException(autoboto.ShapeBase):
    """
    The serice is temporary unavailable.
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
                "can_retry",
                "canRetry",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # You can wait and then retry your request.
    can_retry: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetTagsForResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The ARN of the assessment template that you want to set tags to.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A collection of key and value pairs that you want to set to the assessment
    # template.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


class Severity(Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"
    Informational = "Informational"
    Undefined = "Undefined"


@dataclasses.dataclass
class StartAssessmentRunRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_template_arn",
                "assessmentTemplateArn",
                autoboto.TypeInfo(str),
            ),
            (
                "assessment_run_name",
                "assessmentRunName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the assessment template of the assessment run that you want to
    # start.
    assessment_template_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # You can specify the name for the assessment run. The name must be unique
    # for the assessment template whose ARN is used to start the assessment run.
    assessment_run_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartAssessmentRunResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_run_arn",
                "assessmentRunArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the assessment run that has been started.
    assessment_run_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class StopAction(Enum):
    START_EVALUATION = "START_EVALUATION"
    SKIP_EVALUATION = "SKIP_EVALUATION"


@dataclasses.dataclass
class StopAssessmentRunRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_run_arn",
                "assessmentRunArn",
                autoboto.TypeInfo(str),
            ),
            (
                "stop_action",
                "stopAction",
                autoboto.TypeInfo(StopAction),
            ),
        ]

    # The ARN of the assessment run that you want to stop.
    assessment_run_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An input option that can be set to either START_EVALUATION or
    # SKIP_EVALUATION. START_EVALUATION (the default value), stops the AWS agent
    # from collecting data and begins the results evaluation and the findings
    # generation process. SKIP_EVALUATION cancels the assessment run immediately,
    # after which no findings are generated.
    stop_action: "StopAction" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SubscribeToEventRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "event",
                "event",
                autoboto.TypeInfo(InspectorEvent),
            ),
            (
                "topic_arn",
                "topicArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the assessment template that is used during the event for which
    # you want to receive SNS notifications.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The event for which you want to receive SNS notifications.
    event: "InspectorEvent" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the SNS topic to which the SNS notifications are sent.
    topic_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Subscription(autoboto.ShapeBase):
    """
    This data type is used as a response element in the ListEventSubscriptions
    action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "topic_arn",
                "topicArn",
                autoboto.TypeInfo(str),
            ),
            (
                "event_subscriptions",
                "eventSubscriptions",
                autoboto.TypeInfo(typing.List[EventSubscription]),
            ),
        ]

    # The ARN of the assessment template that is used during the event for which
    # the SNS notification is sent.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the Amazon Simple Notification Service (SNS) topic to which the
    # SNS notifications are sent.
    topic_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of existing event subscriptions.
    event_subscriptions: typing.List["EventSubscription"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    """
    A key and value pair. This data type is used as a request parameter in the
    SetTagsForResource action and a response element in the ListTagsForResource
    action.
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

    # A tag key.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A value assigned to a tag key.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TelemetryMetadata(autoboto.ShapeBase):
    """
    The metadata about the Amazon Inspector application data metrics collected by
    the agent. This data type is used as the response element in the
    GetTelemetryMetadata action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message_type",
                "messageType",
                autoboto.TypeInfo(str),
            ),
            (
                "count",
                "count",
                autoboto.TypeInfo(int),
            ),
            (
                "data_size",
                "dataSize",
                autoboto.TypeInfo(int),
            ),
        ]

    # A specific type of behavioral data that is collected by the agent.
    message_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The count of messages that the agent sends to the Amazon Inspector service.
    count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The data size of messages that the agent sends to the Amazon Inspector
    # service.
    data_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TimestampRange(autoboto.ShapeBase):
    """
    This data type is used in the AssessmentRunFilter data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "begin_date",
                "beginDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "end_date",
                "endDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The minimum value of the timestamp range.
    begin_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum value of the timestamp range.
    end_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UnsubscribeFromEventRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "event",
                "event",
                autoboto.TypeInfo(InspectorEvent),
            ),
            (
                "topic_arn",
                "topicArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the assessment template that is used during the event for which
    # you want to stop receiving SNS notifications.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The event for which you want to stop receiving SNS notifications.
    event: "InspectorEvent" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the SNS topic to which SNS notifications are sent.
    topic_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsupportedFeatureException(autoboto.ShapeBase):
    """
    Used by the GetAssessmentReport API. The request was rejected because you tried
    to generate a report for an assessment run that existed before reporting was
    supported in Amazon Inspector. You can only generate reports for assessment runs
    that took place or will take place after generating reports in Amazon Inspector
    became available.
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
                "can_retry",
                "canRetry",
                autoboto.TypeInfo(bool),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    can_retry: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateAssessmentTargetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_target_arn",
                "assessmentTargetArn",
                autoboto.TypeInfo(str),
            ),
            (
                "assessment_target_name",
                "assessmentTargetName",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_group_arn",
                "resourceGroupArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN of the assessment target that you want to update.
    assessment_target_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the assessment target that you want to update.
    assessment_target_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the resource group that is used to specify the new resource
    # group to associate with the assessment target.
    resource_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
