import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class ActivityTask(autoboto.ShapeBase):
    """
    Unit of work sent to an activity worker.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_token",
                "taskToken",
                autoboto.TypeInfo(str),
            ),
            (
                "activity_id",
                "activityId",
                autoboto.TypeInfo(str),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "workflow_execution",
                "workflowExecution",
                autoboto.TypeInfo(WorkflowExecution),
            ),
            (
                "activity_type",
                "activityType",
                autoboto.TypeInfo(ActivityType),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
        ]

    # The opaque string used as a handle on the task. This token is used by
    # workers to communicate progress and response information back to the system
    # about the task.
    task_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID of the task.
    activity_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the `ActivityTaskStarted` event recorded in the history.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The workflow execution that started this activity task.
    workflow_execution: "WorkflowExecution" = dataclasses.field(
        default_factory=dict,
    )

    # The type of this activity task.
    activity_type: "ActivityType" = dataclasses.field(default_factory=dict, )

    # The inputs provided when the activity task was scheduled. The form of the
    # input is user defined and should be meaningful to the activity
    # implementation.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ActivityTaskCancelRequestedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ActivityTaskCancelRequested` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "activity_id",
                "activityId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `RequestCancelActivityTask` decision for this
    # cancellation request. This information can be useful for diagnosing
    # problems by tracing back the chain of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The unique ID of the task.
    activity_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ActivityTaskCanceledEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ActivityTaskCanceled` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_event_id",
                "scheduledEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_cancel_requested_event_id",
                "latestCancelRequestedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the `ActivityTaskScheduled` event that was recorded when this
    # activity task was scheduled. This information can be useful for diagnosing
    # problems by tracing back the chain of events leading up to this event.
    scheduled_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `ActivityTaskStarted` event recorded when this activity task
    # was started. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Details of the cancellation.
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If set, contains the ID of the last `ActivityTaskCancelRequested` event
    # recorded for this activity task. This information can be useful for
    # diagnosing problems by tracing back the chain of events leading up to this
    # event.
    latest_cancel_requested_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ActivityTaskCompletedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ActivityTaskCompleted` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_event_id",
                "scheduledEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "result",
                "result",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the `ActivityTaskScheduled` event that was recorded when this
    # activity task was scheduled. This information can be useful for diagnosing
    # problems by tracing back the chain of events leading up to this event.
    scheduled_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `ActivityTaskStarted` event recorded when this activity task
    # was started. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The results of the activity task.
    result: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ActivityTaskFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ActivityTaskFailed` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_event_id",
                "scheduledEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "reason",
                "reason",
                autoboto.TypeInfo(str),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the `ActivityTaskScheduled` event that was recorded when this
    # activity task was scheduled. This information can be useful for diagnosing
    # problems by tracing back the chain of events leading up to this event.
    scheduled_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `ActivityTaskStarted` event recorded when this activity task
    # was started. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The reason provided for the failure.
    reason: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The details of the failure.
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ActivityTaskScheduledEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ActivityTaskScheduled` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activity_type",
                "activityType",
                autoboto.TypeInfo(ActivityType),
            ),
            (
                "activity_id",
                "activityId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_list",
                "taskList",
                autoboto.TypeInfo(TaskList),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
            (
                "control",
                "control",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule_to_start_timeout",
                "scheduleToStartTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule_to_close_timeout",
                "scheduleToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "start_to_close_timeout",
                "startToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "task_priority",
                "taskPriority",
                autoboto.TypeInfo(str),
            ),
            (
                "heartbeat_timeout",
                "heartbeatTimeout",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of the activity task.
    activity_type: "ActivityType" = dataclasses.field(default_factory=dict, )

    # The unique ID of the activity task.
    activity_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The task list in which the activity task has been scheduled.
    task_list: "TaskList" = dataclasses.field(default_factory=dict, )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # that resulted in the scheduling of this activity task. This information can
    # be useful for diagnosing problems by tracing back the chain of events
    # leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The input provided to the activity task.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Data attached to the event that can be used by the decider in subsequent
    # workflow tasks. This data isn't sent to the activity.
    control: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum amount of time the activity task can wait to be assigned to a
    # worker.
    schedule_to_start_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum amount of time for this activity task.
    schedule_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum amount of time a worker may take to process the activity task.
    start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The priority to assign to the scheduled activity task. If set, this
    # overrides any default priority value that was assigned when the activity
    # type was registered.

    # Valid values are integers that range from Java's `Integer.MIN_VALUE`
    # (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate
    # higher priority.

    # For more information about setting task priority, see [Setting Task
    # Priority](http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-
    # priority.html) in the _Amazon SWF Developer Guide_.
    task_priority: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum time before which the worker processing this task must report
    # progress by calling RecordActivityTaskHeartbeat. If the timeout is
    # exceeded, the activity task is automatically timed out. If the worker
    # subsequently attempts to record a heartbeat or return a result, it is
    # ignored.
    heartbeat_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ActivityTaskStartedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ActivityTaskStarted` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_event_id",
                "scheduledEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "identity",
                "identity",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the `ActivityTaskScheduled` event that was recorded when this
    # activity task was scheduled. This information can be useful for diagnosing
    # problems by tracing back the chain of events leading up to this event.
    scheduled_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Identity of the worker that was assigned this task. This aids diagnostics
    # when problems arise. The form of this identity is user defined.
    identity: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ActivityTaskStatus(autoboto.ShapeBase):
    """
    Status information about an activity task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cancel_requested",
                "cancelRequested",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Set to `true` if cancellation of the task is requested.
    cancel_requested: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ActivityTaskTimedOutEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ActivityTaskTimedOut` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timeout_type",
                "timeoutType",
                autoboto.TypeInfo(ActivityTaskTimeoutType),
            ),
            (
                "scheduled_event_id",
                "scheduledEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of the timeout that caused this event.
    timeout_type: "ActivityTaskTimeoutType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `ActivityTaskScheduled` event that was recorded when this
    # activity task was scheduled. This information can be useful for diagnosing
    # problems by tracing back the chain of events leading up to this event.
    scheduled_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `ActivityTaskStarted` event recorded when this activity task
    # was started. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Contains the content of the `details` parameter for the last call made by
    # the activity to `RecordActivityTaskHeartbeat`.
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class ActivityTaskTimeoutType(Enum):
    START_TO_CLOSE = "START_TO_CLOSE"
    SCHEDULE_TO_START = "SCHEDULE_TO_START"
    SCHEDULE_TO_CLOSE = "SCHEDULE_TO_CLOSE"
    HEARTBEAT = "HEARTBEAT"


@dataclasses.dataclass
class ActivityType(autoboto.ShapeBase):
    """
    Represents an activity type.
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
                "version",
                "version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of this activity.

    # The combination of activity type name and version must be unique within a
    # domain.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of this activity.

    # The combination of activity type name and version must be unique with in a
    # domain.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ActivityTypeConfiguration(autoboto.ShapeBase):
    """
    Configuration settings registered with the activity type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "default_task_start_to_close_timeout",
                "defaultTaskStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "default_task_heartbeat_timeout",
                "defaultTaskHeartbeatTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "default_task_list",
                "defaultTaskList",
                autoboto.TypeInfo(TaskList),
            ),
            (
                "default_task_priority",
                "defaultTaskPriority",
                autoboto.TypeInfo(str),
            ),
            (
                "default_task_schedule_to_start_timeout",
                "defaultTaskScheduleToStartTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "default_task_schedule_to_close_timeout",
                "defaultTaskScheduleToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
        ]

    # The default maximum duration for tasks of an activity type specified when
    # registering the activity type. You can override this default when
    # scheduling a task through the `ScheduleActivityTask` Decision.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    default_task_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default maximum time, in seconds, before which a worker processing a
    # task must report progress by calling RecordActivityTaskHeartbeat.

    # You can specify this value only when _registering_ an activity type. The
    # registered default value can be overridden when you schedule a task through
    # the `ScheduleActivityTask` Decision. If the activity worker subsequently
    # attempts to record a heartbeat or returns a result, the activity worker
    # receives an `UnknownResource` fault. In this case, Amazon SWF no longer
    # considers the activity task to be valid; the activity worker should clean
    # up the activity task.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    default_task_heartbeat_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default task list specified for this activity type at registration.
    # This default is used if a task list isn't provided when a task is scheduled
    # through the `ScheduleActivityTask` Decision. You can override the default
    # registered task list when scheduling a task through the
    # `ScheduleActivityTask` Decision.
    default_task_list: "TaskList" = dataclasses.field(default_factory=dict, )

    # The default task priority for tasks of this activity type, specified at
    # registration. If not set, then `0` is used as the default priority. This
    # default can be overridden when scheduling an activity task.

    # Valid values are integers that range from Java's `Integer.MIN_VALUE`
    # (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate
    # higher priority.

    # For more information about setting task priority, see [Setting Task
    # Priority](http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-
    # priority.html) in the _Amazon SWF Developer Guide_.
    default_task_priority: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default maximum duration, specified when registering the activity type,
    # that a task of an activity type can wait before being assigned to a worker.
    # You can override this default when scheduling a task through the
    # `ScheduleActivityTask` Decision.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    default_task_schedule_to_start_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default maximum duration, specified when registering the activity type,
    # for tasks of this activity type. You can override this default when
    # scheduling a task through the `ScheduleActivityTask` Decision.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    default_task_schedule_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ActivityTypeDetail(autoboto.ShapeBase):
    """
    Detailed information about an activity type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_info",
                "typeInfo",
                autoboto.TypeInfo(ActivityTypeInfo),
            ),
            (
                "configuration",
                "configuration",
                autoboto.TypeInfo(ActivityTypeConfiguration),
            ),
        ]

    # General information about the activity type.

    # The status of activity type (returned in the ActivityTypeInfo structure)
    # can be one of the following.

    #   * `REGISTERED` – The type is registered and available. Workers supporting this type should be running.

    #   * `DEPRECATED` – The type was deprecated using DeprecateActivityType, but is still in use. You should keep workers supporting this type running. You cannot create new tasks of this type.
    type_info: "ActivityTypeInfo" = dataclasses.field(default_factory=dict, )

    # The configuration settings registered with the activity type.
    configuration: "ActivityTypeConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ActivityTypeInfo(autoboto.ShapeBase):
    """
    Detailed information about an activity type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activity_type",
                "activityType",
                autoboto.TypeInfo(ActivityType),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(RegistrationStatus),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "deprecation_date",
                "deprecationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ActivityType type structure representing the activity type.
    activity_type: "ActivityType" = dataclasses.field(default_factory=dict, )

    # The current status of the activity type.
    status: "RegistrationStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time this activity type was created through
    # RegisterActivityType.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The description of the activity type provided in RegisterActivityType.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If DEPRECATED, the date and time DeprecateActivityType was called.
    deprecation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ActivityTypeInfos(autoboto.ShapeBase):
    """
    Contains a paginated list of activity type information structures.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_infos",
                "typeInfos",
                autoboto.TypeInfo(typing.List[ActivityTypeInfo]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # List of activity type information.
    type_infos: typing.List["ActivityTypeInfo"] = dataclasses.field(
        default_factory=list,
    )

    # If a `NextPageToken` was returned by a previous call, there are more
    # results available. To retrieve the next page of results, make the call
    # again using the returned token in `nextPageToken`. Keep all other arguments
    # unchanged.

    # The configured `maximumPageSize` determines how many results can be
    # returned in a single call.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CancelTimerDecisionAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `CancelTimer` decision.

    **Access Control**

    You can use IAM policies to control this decision's access to Amazon SWF
    resources as follows:

      * Use a `Resource` element with the domain name to limit the action to only specified domains.

      * Use an `Action` element to allow or deny permission to call this action.

      * You cannot use an IAM policy to constrain this action's parameters.

    If the caller doesn't have sufficient permissions to invoke the action, or the
    parameter values fall outside the specified constraints, the action fails. The
    associated event attribute's `cause` parameter is set to
    `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
    to Manage Access to Amazon SWF
    Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
    iam.html) in the _Amazon SWF Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timer_id",
                "timerId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the timer to cancel.
    timer_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class CancelTimerFailedCause(Enum):
    TIMER_ID_UNKNOWN = "TIMER_ID_UNKNOWN"
    OPERATION_NOT_PERMITTED = "OPERATION_NOT_PERMITTED"


@dataclasses.dataclass
class CancelTimerFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `CancelTimerFailed` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timer_id",
                "timerId",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(CancelTimerFailedCause),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The timerId provided in the `CancelTimer` decision that failed.
    timer_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The cause of the failure. This information is generated by the system and
    # can be useful for diagnostic purposes.

    # If `cause` is set to `OPERATION_NOT_PERMITTED`, the decision failed because
    # it lacked sufficient permissions. For details and example IAM policies, see
    # [Using IAM to Manage Access to Amazon SWF
    # Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-
    # dev-iam.html) in the _Amazon SWF Developer Guide_.
    cause: "CancelTimerFailedCause" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `CancelTimer` decision to cancel this timer. This
    # information can be useful for diagnosing problems by tracing back the chain
    # of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CancelWorkflowExecutionDecisionAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `CancelWorkflowExecution` decision.

    **Access Control**

    You can use IAM policies to control this decision's access to Amazon SWF
    resources as follows:

      * Use a `Resource` element with the domain name to limit the action to only specified domains.

      * Use an `Action` element to allow or deny permission to call this action.

      * You cannot use an IAM policy to constrain this action's parameters.

    If the caller doesn't have sufficient permissions to invoke the action, or the
    parameter values fall outside the specified constraints, the action fails. The
    associated event attribute's `cause` parameter is set to
    `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
    to Manage Access to Amazon SWF
    Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
    iam.html) in the _Amazon SWF Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
        ]

    # Details of the cancellation.
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class CancelWorkflowExecutionFailedCause(Enum):
    UNHANDLED_DECISION = "UNHANDLED_DECISION"
    OPERATION_NOT_PERMITTED = "OPERATION_NOT_PERMITTED"


@dataclasses.dataclass
class CancelWorkflowExecutionFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `CancelWorkflowExecutionFailed` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cause",
                "cause",
                autoboto.TypeInfo(CancelWorkflowExecutionFailedCause),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The cause of the failure. This information is generated by the system and
    # can be useful for diagnostic purposes.

    # If `cause` is set to `OPERATION_NOT_PERMITTED`, the decision failed because
    # it lacked sufficient permissions. For details and example IAM policies, see
    # [Using IAM to Manage Access to Amazon SWF
    # Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-
    # dev-iam.html) in the _Amazon SWF Developer Guide_.
    cause: "CancelWorkflowExecutionFailedCause" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `CancelWorkflowExecution` decision for this
    # cancellation request. This information can be useful for diagnosing
    # problems by tracing back the chain of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class ChildPolicy(Enum):
    TERMINATE = "TERMINATE"
    REQUEST_CANCEL = "REQUEST_CANCEL"
    ABANDON = "ABANDON"


@dataclasses.dataclass
class ChildWorkflowExecutionCanceledEventAttributes(autoboto.ShapeBase):
    """
    Provide details of the `ChildWorkflowExecutionCanceled` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_execution",
                "workflowExecution",
                autoboto.TypeInfo(WorkflowExecution),
            ),
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
            (
                "initiated_event_id",
                "initiatedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
        ]

    # The child workflow execution that was canceled.
    workflow_execution: "WorkflowExecution" = dataclasses.field(
        default_factory=dict,
    )

    # The type of the child workflow execution.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )

    # The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to
    # the `StartChildWorkflowExecution` Decision to start this child workflow
    # execution. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    initiated_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `ChildWorkflowExecutionStarted` event recorded when this
    # child workflow execution was started. This information can be useful for
    # diagnosing problems by tracing back the chain of events leading up to this
    # event.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Details of the cancellation (if provided).
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ChildWorkflowExecutionCompletedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ChildWorkflowExecutionCompleted` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_execution",
                "workflowExecution",
                autoboto.TypeInfo(WorkflowExecution),
            ),
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
            (
                "initiated_event_id",
                "initiatedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "result",
                "result",
                autoboto.TypeInfo(str),
            ),
        ]

    # The child workflow execution that was completed.
    workflow_execution: "WorkflowExecution" = dataclasses.field(
        default_factory=dict,
    )

    # The type of the child workflow execution.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )

    # The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to
    # the `StartChildWorkflowExecution` Decision to start this child workflow
    # execution. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    initiated_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `ChildWorkflowExecutionStarted` event recorded when this
    # child workflow execution was started. This information can be useful for
    # diagnosing problems by tracing back the chain of events leading up to this
    # event.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The result of the child workflow execution.
    result: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ChildWorkflowExecutionFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ChildWorkflowExecutionFailed` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_execution",
                "workflowExecution",
                autoboto.TypeInfo(WorkflowExecution),
            ),
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
            (
                "initiated_event_id",
                "initiatedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "reason",
                "reason",
                autoboto.TypeInfo(str),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
        ]

    # The child workflow execution that failed.
    workflow_execution: "WorkflowExecution" = dataclasses.field(
        default_factory=dict,
    )

    # The type of the child workflow execution.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )

    # The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to
    # the `StartChildWorkflowExecution` Decision to start this child workflow
    # execution. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    initiated_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `ChildWorkflowExecutionStarted` event recorded when this
    # child workflow execution was started. This information can be useful for
    # diagnosing problems by tracing back the chain of events leading up to this
    # event.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The reason for the failure (if provided).
    reason: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The details of the failure (if provided).
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ChildWorkflowExecutionStartedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ChildWorkflowExecutionStarted` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_execution",
                "workflowExecution",
                autoboto.TypeInfo(WorkflowExecution),
            ),
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
            (
                "initiated_event_id",
                "initiatedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The child workflow execution that was started.
    workflow_execution: "WorkflowExecution" = dataclasses.field(
        default_factory=dict,
    )

    # The type of the child workflow execution.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )

    # The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to
    # the `StartChildWorkflowExecution` Decision to start this child workflow
    # execution. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    initiated_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ChildWorkflowExecutionTerminatedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ChildWorkflowExecutionTerminated` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_execution",
                "workflowExecution",
                autoboto.TypeInfo(WorkflowExecution),
            ),
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
            (
                "initiated_event_id",
                "initiatedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The child workflow execution that was terminated.
    workflow_execution: "WorkflowExecution" = dataclasses.field(
        default_factory=dict,
    )

    # The type of the child workflow execution.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )

    # The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to
    # the `StartChildWorkflowExecution` Decision to start this child workflow
    # execution. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    initiated_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `ChildWorkflowExecutionStarted` event recorded when this
    # child workflow execution was started. This information can be useful for
    # diagnosing problems by tracing back the chain of events leading up to this
    # event.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ChildWorkflowExecutionTimedOutEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ChildWorkflowExecutionTimedOut` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_execution",
                "workflowExecution",
                autoboto.TypeInfo(WorkflowExecution),
            ),
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
            (
                "timeout_type",
                "timeoutType",
                autoboto.TypeInfo(WorkflowExecutionTimeoutType),
            ),
            (
                "initiated_event_id",
                "initiatedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The child workflow execution that timed out.
    workflow_execution: "WorkflowExecution" = dataclasses.field(
        default_factory=dict,
    )

    # The type of the child workflow execution.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )

    # The type of the timeout that caused the child workflow execution to time
    # out.
    timeout_type: "WorkflowExecutionTimeoutType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to
    # the `StartChildWorkflowExecution` Decision to start this child workflow
    # execution. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    initiated_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `ChildWorkflowExecutionStarted` event recorded when this
    # child workflow execution was started. This information can be useful for
    # diagnosing problems by tracing back the chain of events leading up to this
    # event.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class CloseStatus(Enum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELED = "CANCELED"
    TERMINATED = "TERMINATED"
    CONTINUED_AS_NEW = "CONTINUED_AS_NEW"
    TIMED_OUT = "TIMED_OUT"


@dataclasses.dataclass
class CloseStatusFilter(autoboto.ShapeBase):
    """
    Used to filter the closed workflow executions in visibility APIs by their close
    status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "status",
                autoboto.TypeInfo(CloseStatus),
            ),
        ]

    # The close status that must match the close status of an execution for it to
    # meet the criteria of this filter.
    status: "CloseStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CompleteWorkflowExecutionDecisionAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `CompleteWorkflowExecution` decision.

    **Access Control**

    You can use IAM policies to control this decision's access to Amazon SWF
    resources as follows:

      * Use a `Resource` element with the domain name to limit the action to only specified domains.

      * Use an `Action` element to allow or deny permission to call this action.

      * You cannot use an IAM policy to constrain this action's parameters.

    If the caller doesn't have sufficient permissions to invoke the action, or the
    parameter values fall outside the specified constraints, the action fails. The
    associated event attribute's `cause` parameter is set to
    `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
    to Manage Access to Amazon SWF
    Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
    iam.html) in the _Amazon SWF Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "result",
                "result",
                autoboto.TypeInfo(str),
            ),
        ]

    # The result of the workflow execution. The form of the result is
    # implementation defined.
    result: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class CompleteWorkflowExecutionFailedCause(Enum):
    UNHANDLED_DECISION = "UNHANDLED_DECISION"
    OPERATION_NOT_PERMITTED = "OPERATION_NOT_PERMITTED"


@dataclasses.dataclass
class CompleteWorkflowExecutionFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `CompleteWorkflowExecutionFailed` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cause",
                "cause",
                autoboto.TypeInfo(CompleteWorkflowExecutionFailedCause),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The cause of the failure. This information is generated by the system and
    # can be useful for diagnostic purposes.

    # If `cause` is set to `OPERATION_NOT_PERMITTED`, the decision failed because
    # it lacked sufficient permissions. For details and example IAM policies, see
    # [Using IAM to Manage Access to Amazon SWF
    # Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-
    # dev-iam.html) in the _Amazon SWF Developer Guide_.
    cause: "CompleteWorkflowExecutionFailedCause" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `CompleteWorkflowExecution` decision to complete
    # this execution. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ContinueAsNewWorkflowExecutionDecisionAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ContinueAsNewWorkflowExecution` decision.

    **Access Control**

    You can use IAM policies to control this decision's access to Amazon SWF
    resources as follows:

      * Use a `Resource` element with the domain name to limit the action to only specified domains.

      * Use an `Action` element to allow or deny permission to call this action.

      * Constrain the following parameters by using a `Condition` element with the appropriate keys.

        * `tag` – A tag used to identify the workflow execution

        * `taskList` – String constraint. The key is `swf:taskList.name`.

        * `workflowType.version` – String constraint. The key is `swf:workflowType.version`.

    If the caller doesn't have sufficient permissions to invoke the action, or the
    parameter values fall outside the specified constraints, the action fails. The
    associated event attribute's `cause` parameter is set to
    `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
    to Manage Access to Amazon SWF
    Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
    iam.html) in the _Amazon SWF Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_start_to_close_timeout",
                "executionStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "task_list",
                "taskList",
                autoboto.TypeInfo(TaskList),
            ),
            (
                "task_priority",
                "taskPriority",
                autoboto.TypeInfo(str),
            ),
            (
                "task_start_to_close_timeout",
                "taskStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "child_policy",
                "childPolicy",
                autoboto.TypeInfo(ChildPolicy),
            ),
            (
                "tag_list",
                "tagList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "workflow_type_version",
                "workflowTypeVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "lambda_role",
                "lambdaRole",
                autoboto.TypeInfo(str),
            ),
        ]

    # The input provided to the new workflow execution.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If set, specifies the total duration for this workflow execution. This
    # overrides the `defaultExecutionStartToCloseTimeout` specified when
    # registering the workflow type.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.

    # An execution start-to-close timeout for this workflow execution must be
    # specified either as a default for the workflow type or through this field.
    # If neither this field is set nor a default execution start-to-close timeout
    # was specified at registration time then a fault is returned.
    execution_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The task list to use for the decisions of the new (continued) workflow
    # execution.
    task_list: "TaskList" = dataclasses.field(default_factory=dict, )

    # The task priority that, if set, specifies the priority for the decision
    # tasks for this workflow execution. This overrides the defaultTaskPriority
    # specified when registering the workflow type. Valid values are integers
    # that range from Java's `Integer.MIN_VALUE` (-2147483648) to
    # `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.

    # For more information about setting task priority, see [Setting Task
    # Priority](http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-
    # priority.html) in the _Amazon SWF Developer Guide_.
    task_priority: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the maximum duration of decision tasks for the new workflow
    # execution. This parameter overrides the `defaultTaskStartToCloseTimout`
    # specified when registering the workflow type using RegisterWorkflowType.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.

    # A task start-to-close timeout for the new workflow execution must be
    # specified either as a default for the workflow type or through this
    # parameter. If neither this parameter is set nor a default task start-to-
    # close timeout was specified at registration time then a fault is returned.
    task_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If set, specifies the policy to use for the child workflow executions of
    # the new execution if it is terminated by calling the
    # TerminateWorkflowExecution action explicitly or due to an expired timeout.
    # This policy overrides the default child policy specified when registering
    # the workflow type using RegisterWorkflowType.

    # The supported child policies are:

    #   * `TERMINATE` – The child executions are terminated.

    #   * `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.

    #   * `ABANDON` – No action is taken. The child executions continue to run.

    # A child policy for this workflow execution must be specified either as a
    # default for the workflow type or through this parameter. If neither this
    # parameter is set nor a default child policy was specified at registration
    # time then a fault is returned.
    child_policy: "ChildPolicy" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The list of tags to associate with the new workflow execution. A maximum of
    # 5 tags can be specified. You can list workflow executions with a specific
    # tag by calling ListOpenWorkflowExecutions or ListClosedWorkflowExecutions
    # and specifying a TagFilter.
    tag_list: typing.List[str] = dataclasses.field(default_factory=list, )

    # The version of the workflow to start.
    workflow_type_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IAM role to attach to the new (continued) execution.
    lambda_role: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class ContinueAsNewWorkflowExecutionFailedCause(Enum):
    UNHANDLED_DECISION = "UNHANDLED_DECISION"
    WORKFLOW_TYPE_DEPRECATED = "WORKFLOW_TYPE_DEPRECATED"
    WORKFLOW_TYPE_DOES_NOT_EXIST = "WORKFLOW_TYPE_DOES_NOT_EXIST"
    DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED = "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED"
    DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED = "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED"
    DEFAULT_TASK_LIST_UNDEFINED = "DEFAULT_TASK_LIST_UNDEFINED"
    DEFAULT_CHILD_POLICY_UNDEFINED = "DEFAULT_CHILD_POLICY_UNDEFINED"
    CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED = "CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED"
    OPERATION_NOT_PERMITTED = "OPERATION_NOT_PERMITTED"


@dataclasses.dataclass
class ContinueAsNewWorkflowExecutionFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ContinueAsNewWorkflowExecutionFailed` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cause",
                "cause",
                autoboto.TypeInfo(ContinueAsNewWorkflowExecutionFailedCause),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The cause of the failure. This information is generated by the system and
    # can be useful for diagnostic purposes.

    # If `cause` is set to `OPERATION_NOT_PERMITTED`, the decision failed because
    # it lacked sufficient permissions. For details and example IAM policies, see
    # [Using IAM to Manage Access to Amazon SWF
    # Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-
    # dev-iam.html) in the _Amazon SWF Developer Guide_.
    cause: "ContinueAsNewWorkflowExecutionFailedCause" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `ContinueAsNewWorkflowExecution` decision that
    # started this execution. This information can be useful for diagnosing
    # problems by tracing back the chain of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CountClosedWorkflowExecutionsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "start_time_filter",
                "startTimeFilter",
                autoboto.TypeInfo(ExecutionTimeFilter),
            ),
            (
                "close_time_filter",
                "closeTimeFilter",
                autoboto.TypeInfo(ExecutionTimeFilter),
            ),
            (
                "execution_filter",
                "executionFilter",
                autoboto.TypeInfo(WorkflowExecutionFilter),
            ),
            (
                "type_filter",
                "typeFilter",
                autoboto.TypeInfo(WorkflowTypeFilter),
            ),
            (
                "tag_filter",
                "tagFilter",
                autoboto.TypeInfo(TagFilter),
            ),
            (
                "close_status_filter",
                "closeStatusFilter",
                autoboto.TypeInfo(CloseStatusFilter),
            ),
        ]

    # The name of the domain containing the workflow executions to count.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If specified, only workflow executions that meet the start time criteria of
    # the filter are counted.

    # `startTimeFilter` and `closeTimeFilter` are mutually exclusive. You must
    # specify one of these in a request but not both.
    start_time_filter: "ExecutionTimeFilter" = dataclasses.field(
        default_factory=dict,
    )

    # If specified, only workflow executions that meet the close time criteria of
    # the filter are counted.

    # `startTimeFilter` and `closeTimeFilter` are mutually exclusive. You must
    # specify one of these in a request but not both.
    close_time_filter: "ExecutionTimeFilter" = dataclasses.field(
        default_factory=dict,
    )

    # If specified, only workflow executions matching the `WorkflowId` in the
    # filter are counted.

    # `closeStatusFilter`, `executionFilter`, `typeFilter` and `tagFilter` are
    # mutually exclusive. You can specify at most one of these in a request.
    execution_filter: "WorkflowExecutionFilter" = dataclasses.field(
        default_factory=dict,
    )

    # If specified, indicates the type of the workflow executions to be counted.

    # `closeStatusFilter`, `executionFilter`, `typeFilter` and `tagFilter` are
    # mutually exclusive. You can specify at most one of these in a request.
    type_filter: "WorkflowTypeFilter" = dataclasses.field(
        default_factory=dict,
    )

    # If specified, only executions that have a tag that matches the filter are
    # counted.

    # `closeStatusFilter`, `executionFilter`, `typeFilter` and `tagFilter` are
    # mutually exclusive. You can specify at most one of these in a request.
    tag_filter: "TagFilter" = dataclasses.field(default_factory=dict, )

    # If specified, only workflow executions that match this close status are
    # counted. This filter has an affect only if `executionStatus` is specified
    # as `CLOSED`.

    # `closeStatusFilter`, `executionFilter`, `typeFilter` and `tagFilter` are
    # mutually exclusive. You can specify at most one of these in a request.
    close_status_filter: "CloseStatusFilter" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CountOpenWorkflowExecutionsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "start_time_filter",
                "startTimeFilter",
                autoboto.TypeInfo(ExecutionTimeFilter),
            ),
            (
                "type_filter",
                "typeFilter",
                autoboto.TypeInfo(WorkflowTypeFilter),
            ),
            (
                "tag_filter",
                "tagFilter",
                autoboto.TypeInfo(TagFilter),
            ),
            (
                "execution_filter",
                "executionFilter",
                autoboto.TypeInfo(WorkflowExecutionFilter),
            ),
        ]

    # The name of the domain containing the workflow executions to count.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the start time criteria that workflow executions must meet in
    # order to be counted.
    start_time_filter: "ExecutionTimeFilter" = dataclasses.field(
        default_factory=dict,
    )

    # Specifies the type of the workflow executions to be counted.

    # `executionFilter`, `typeFilter` and `tagFilter` are mutually exclusive. You
    # can specify at most one of these in a request.
    type_filter: "WorkflowTypeFilter" = dataclasses.field(
        default_factory=dict,
    )

    # If specified, only executions that have a tag that matches the filter are
    # counted.

    # `executionFilter`, `typeFilter` and `tagFilter` are mutually exclusive. You
    # can specify at most one of these in a request.
    tag_filter: "TagFilter" = dataclasses.field(default_factory=dict, )

    # If specified, only workflow executions matching the `WorkflowId` in the
    # filter are counted.

    # `executionFilter`, `typeFilter` and `tagFilter` are mutually exclusive. You
    # can specify at most one of these in a request.
    execution_filter: "WorkflowExecutionFilter" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CountPendingActivityTasksInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "task_list",
                "taskList",
                autoboto.TypeInfo(TaskList),
            ),
        ]

    # The name of the domain that contains the task list.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the task list.
    task_list: "TaskList" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CountPendingDecisionTasksInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "task_list",
                "taskList",
                autoboto.TypeInfo(TaskList),
            ),
        ]

    # The name of the domain that contains the task list.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the task list.
    task_list: "TaskList" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class Decision(autoboto.ShapeBase):
    """
    Specifies a decision made by the decider. A decision can be one of these types:

      * `CancelTimer` – Cancels a previously started timer and records a `TimerCanceled` event in the history.

      * `CancelWorkflowExecution` – Closes the workflow execution and records a `WorkflowExecutionCanceled` event in the history.

      * `CompleteWorkflowExecution` – Closes the workflow execution and records a `WorkflowExecutionCompleted` event in the history .

      * `ContinueAsNewWorkflowExecution` – Closes the workflow execution and starts a new workflow execution of the same type using the same workflow ID and a unique run Id. A `WorkflowExecutionContinuedAsNew` event is recorded in the history.

      * `FailWorkflowExecution` – Closes the workflow execution and records a `WorkflowExecutionFailed` event in the history.

      * `RecordMarker` – Records a `MarkerRecorded` event in the history. Markers can be used for adding custom information in the history for instance to let deciders know that they don't need to look at the history beyond the marker event.

      * `RequestCancelActivityTask` – Attempts to cancel a previously scheduled activity task. If the activity task was scheduled but has not been assigned to a worker, then it is canceled. If the activity task was already assigned to a worker, then the worker is informed that cancellation has been requested in the response to RecordActivityTaskHeartbeat.

      * `RequestCancelExternalWorkflowExecution` – Requests that a request be made to cancel the specified external workflow execution and records a `RequestCancelExternalWorkflowExecutionInitiated` event in the history.

      * `ScheduleActivityTask` – Schedules an activity task.

      * `SignalExternalWorkflowExecution` – Requests a signal to be delivered to the specified external workflow execution and records a `SignalExternalWorkflowExecutionInitiated` event in the history.

      * `StartChildWorkflowExecution` – Requests that a child workflow execution be started and records a `StartChildWorkflowExecutionInitiated` event in the history. The child workflow execution is a separate workflow execution with its own history.

      * `StartTimer` – Starts a timer for this workflow execution and records a `TimerStarted` event in the history. This timer fires after the specified delay and record a `TimerFired` event.

    **Access Control**

    If you grant permission to use `RespondDecisionTaskCompleted`, you can use IAM
    policies to express permissions for the list of decisions returned by this
    action as if they were members of the API. Treating decisions as a pseudo API
    maintains a uniform conceptual model and helps keep policies readable. For
    details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF
    Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
    iam.html) in the _Amazon SWF Developer Guide_.

    **Decision Failure**

    Decisions can fail for several reasons

      * The ordering of decisions should follow a logical flow. Some decisions might not make sense in the current context of the workflow execution and therefore fails.

      * A limit on your account was reached.

      * The decision lacks sufficient permissions.

    One of the following events might be added to the history to indicate an error.
    The event attribute's `cause` parameter indicates the cause. If `cause` is set
    to `OPERATION_NOT_PERMITTED`, the decision failed because it lacked sufficient
    permissions. For details and example IAM policies, see [Using IAM to Manage
    Access to Amazon SWF
    Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
    iam.html) in the _Amazon SWF Developer Guide_.

      * `ScheduleActivityTaskFailed` – A `ScheduleActivityTask` decision failed. This could happen if the activity type specified in the decision isn't registered, is in a deprecated state, or the decision isn't properly configured.

      * `RequestCancelActivityTaskFailed` – A `RequestCancelActivityTask` decision failed. This could happen if there is no open activity task with the specified activityId.

      * `StartTimerFailed` – A `StartTimer` decision failed. This could happen if there is another open timer with the same timerId.

      * `CancelTimerFailed` – A `CancelTimer` decision failed. This could happen if there is no open timer with the specified timerId.

      * `StartChildWorkflowExecutionFailed` – A `StartChildWorkflowExecution` decision failed. This could happen if the workflow type specified isn't registered, is deprecated, or the decision isn't properly configured.

      * `SignalExternalWorkflowExecutionFailed` – A `SignalExternalWorkflowExecution` decision failed. This could happen if the `workflowID` specified in the decision was incorrect.

      * `RequestCancelExternalWorkflowExecutionFailed` – A `RequestCancelExternalWorkflowExecution` decision failed. This could happen if the `workflowID` specified in the decision was incorrect.

      * `CancelWorkflowExecutionFailed` – A `CancelWorkflowExecution` decision failed. This could happen if there is an unhandled decision task pending in the workflow execution.

      * `CompleteWorkflowExecutionFailed` – A `CompleteWorkflowExecution` decision failed. This could happen if there is an unhandled decision task pending in the workflow execution.

      * `ContinueAsNewWorkflowExecutionFailed` – A `ContinueAsNewWorkflowExecution` decision failed. This could happen if there is an unhandled decision task pending in the workflow execution or the ContinueAsNewWorkflowExecution decision was not configured correctly.

      * `FailWorkflowExecutionFailed` – A `FailWorkflowExecution` decision failed. This could happen if there is an unhandled decision task pending in the workflow execution.

    The preceding error events might occur due to an error in the decider logic,
    which might put the workflow execution in an unstable state The cause field in
    the event structure for the error event indicates the cause of the error.

    A workflow execution may be closed by the decider by returning one of the
    following decisions when completing a decision task:
    `CompleteWorkflowExecution`, `FailWorkflowExecution`, `CancelWorkflowExecution`
    and `ContinueAsNewWorkflowExecution`. An `UnhandledDecision` fault is returned
    if a workflow closing decision is specified and a signal or activity event had
    been added to the history while the decision task was being performed by the
    decider. Unlike the above situations which are logic issues, this fault is
    always possible because of race conditions in a distributed system. The right
    action here is to call RespondDecisionTaskCompleted without any decisions. This
    would result in another decision task with these new events included in the
    history. The decider should handle the new events and may decide to close the
    workflow execution.

    **How to Code a Decision**

    You code a decision by first setting the decision type field to one of the above
    decision values, and then set the corresponding attributes field shown below:

      * ` ScheduleActivityTaskDecisionAttributes `

      * ` RequestCancelActivityTaskDecisionAttributes `

      * ` CompleteWorkflowExecutionDecisionAttributes `

      * ` FailWorkflowExecutionDecisionAttributes `

      * ` CancelWorkflowExecutionDecisionAttributes `

      * ` ContinueAsNewWorkflowExecutionDecisionAttributes `

      * ` RecordMarkerDecisionAttributes `

      * ` StartTimerDecisionAttributes `

      * ` CancelTimerDecisionAttributes `

      * ` SignalExternalWorkflowExecutionDecisionAttributes `

      * ` RequestCancelExternalWorkflowExecutionDecisionAttributes `

      * ` StartChildWorkflowExecutionDecisionAttributes `
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "decision_type",
                "decisionType",
                autoboto.TypeInfo(DecisionType),
            ),
            (
                "schedule_activity_task_decision_attributes",
                "scheduleActivityTaskDecisionAttributes",
                autoboto.TypeInfo(ScheduleActivityTaskDecisionAttributes),
            ),
            (
                "request_cancel_activity_task_decision_attributes",
                "requestCancelActivityTaskDecisionAttributes",
                autoboto.TypeInfo(RequestCancelActivityTaskDecisionAttributes),
            ),
            (
                "complete_workflow_execution_decision_attributes",
                "completeWorkflowExecutionDecisionAttributes",
                autoboto.TypeInfo(CompleteWorkflowExecutionDecisionAttributes),
            ),
            (
                "fail_workflow_execution_decision_attributes",
                "failWorkflowExecutionDecisionAttributes",
                autoboto.TypeInfo(FailWorkflowExecutionDecisionAttributes),
            ),
            (
                "cancel_workflow_execution_decision_attributes",
                "cancelWorkflowExecutionDecisionAttributes",
                autoboto.TypeInfo(CancelWorkflowExecutionDecisionAttributes),
            ),
            (
                "continue_as_new_workflow_execution_decision_attributes",
                "continueAsNewWorkflowExecutionDecisionAttributes",
                autoboto.
                TypeInfo(ContinueAsNewWorkflowExecutionDecisionAttributes),
            ),
            (
                "record_marker_decision_attributes",
                "recordMarkerDecisionAttributes",
                autoboto.TypeInfo(RecordMarkerDecisionAttributes),
            ),
            (
                "start_timer_decision_attributes",
                "startTimerDecisionAttributes",
                autoboto.TypeInfo(StartTimerDecisionAttributes),
            ),
            (
                "cancel_timer_decision_attributes",
                "cancelTimerDecisionAttributes",
                autoboto.TypeInfo(CancelTimerDecisionAttributes),
            ),
            (
                "signal_external_workflow_execution_decision_attributes",
                "signalExternalWorkflowExecutionDecisionAttributes",
                autoboto.
                TypeInfo(SignalExternalWorkflowExecutionDecisionAttributes),
            ),
            (
                "request_cancel_external_workflow_execution_decision_attributes",
                "requestCancelExternalWorkflowExecutionDecisionAttributes",
                autoboto.TypeInfo(
                    RequestCancelExternalWorkflowExecutionDecisionAttributes
                ),
            ),
            (
                "start_child_workflow_execution_decision_attributes",
                "startChildWorkflowExecutionDecisionAttributes",
                autoboto.
                TypeInfo(StartChildWorkflowExecutionDecisionAttributes),
            ),
            (
                "schedule_lambda_function_decision_attributes",
                "scheduleLambdaFunctionDecisionAttributes",
                autoboto.TypeInfo(ScheduleLambdaFunctionDecisionAttributes),
            ),
        ]

    # Specifies the type of the decision.
    decision_type: "DecisionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Provides the details of the `ScheduleActivityTask` decision. It isn't set
    # for other decision types.
    schedule_activity_task_decision_attributes: "ScheduleActivityTaskDecisionAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `RequestCancelActivityTask` decision. It isn't
    # set for other decision types.
    request_cancel_activity_task_decision_attributes: "RequestCancelActivityTaskDecisionAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `CompleteWorkflowExecution` decision. It isn't
    # set for other decision types.
    complete_workflow_execution_decision_attributes: "CompleteWorkflowExecutionDecisionAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `FailWorkflowExecution` decision. It isn't set
    # for other decision types.
    fail_workflow_execution_decision_attributes: "FailWorkflowExecutionDecisionAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `CancelWorkflowExecution` decision. It isn't
    # set for other decision types.
    cancel_workflow_execution_decision_attributes: "CancelWorkflowExecutionDecisionAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `ContinueAsNewWorkflowExecution` decision. It
    # isn't set for other decision types.
    continue_as_new_workflow_execution_decision_attributes: "ContinueAsNewWorkflowExecutionDecisionAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `RecordMarker` decision. It isn't set for other
    # decision types.
    record_marker_decision_attributes: "RecordMarkerDecisionAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `StartTimer` decision. It isn't set for other
    # decision types.
    start_timer_decision_attributes: "StartTimerDecisionAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `CancelTimer` decision. It isn't set for other
    # decision types.
    cancel_timer_decision_attributes: "CancelTimerDecisionAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `SignalExternalWorkflowExecution` decision. It
    # isn't set for other decision types.
    signal_external_workflow_execution_decision_attributes: "SignalExternalWorkflowExecutionDecisionAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `RequestCancelExternalWorkflowExecution`
    # decision. It isn't set for other decision types.
    request_cancel_external_workflow_execution_decision_attributes: "RequestCancelExternalWorkflowExecutionDecisionAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `StartChildWorkflowExecution` decision. It
    # isn't set for other decision types.
    start_child_workflow_execution_decision_attributes: "StartChildWorkflowExecutionDecisionAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `ScheduleLambdaFunction` decision. It isn't set
    # for other decision types.
    schedule_lambda_function_decision_attributes: "ScheduleLambdaFunctionDecisionAttributes" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DecisionTask(autoboto.ShapeBase):
    """
    A structure that represents a decision task. Decision tasks are sent to deciders
    in order for them to make decisions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_token",
                "taskToken",
                autoboto.TypeInfo(str),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "workflow_execution",
                "workflowExecution",
                autoboto.TypeInfo(WorkflowExecution),
            ),
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
            (
                "events",
                "events",
                autoboto.TypeInfo(typing.List[HistoryEvent]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
            (
                "previous_started_event_id",
                "previousStartedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The opaque string used as a handle on the task. This token is used by
    # workers to communicate progress and response information back to the system
    # about the task.
    task_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the `DecisionTaskStarted` event recorded in the history.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The workflow execution for which this decision task was created.
    workflow_execution: "WorkflowExecution" = dataclasses.field(
        default_factory=dict,
    )

    # The type of the workflow execution for which this decision task was
    # created.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )

    # A paginated list of history events of the workflow execution. The decider
    # uses this during the processing of the decision task.
    events: typing.List["HistoryEvent"] = dataclasses.field(
        default_factory=list,
    )

    # If a `NextPageToken` was returned by a previous call, there are more
    # results available. To retrieve the next page of results, make the call
    # again using the returned token in `nextPageToken`. Keep all other arguments
    # unchanged.

    # The configured `maximumPageSize` determines how many results can be
    # returned in a single call.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the DecisionTaskStarted event of the previous decision task of
    # this workflow execution that was processed by the decider. This can be used
    # to determine the events in the history new since the last decision task
    # received by the decider.
    previous_started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DecisionTaskCompletedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `DecisionTaskCompleted` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_event_id",
                "scheduledEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "execution_context",
                "executionContext",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the `DecisionTaskScheduled` event that was recorded when this
    # decision task was scheduled. This information can be useful for diagnosing
    # problems by tracing back the chain of events leading up to this event.
    scheduled_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskStarted` event recorded when this decision task
    # was started. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # User defined context for the workflow execution.
    execution_context: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DecisionTaskScheduledEventAttributes(autoboto.ShapeBase):
    """
    Provides details about the `DecisionTaskScheduled` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_list",
                "taskList",
                autoboto.TypeInfo(TaskList),
            ),
            (
                "task_priority",
                "taskPriority",
                autoboto.TypeInfo(str),
            ),
            (
                "start_to_close_timeout",
                "startToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the task list in which the decision task was scheduled.
    task_list: "TaskList" = dataclasses.field(default_factory=dict, )

    # A task priority that, if set, specifies the priority for this decision
    # task. Valid values are integers that range from Java's `Integer.MIN_VALUE`
    # (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate
    # higher priority.

    # For more information about setting task priority, see [Setting Task
    # Priority](http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-
    # priority.html) in the _Amazon SWF Developer Guide_.
    task_priority: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum duration for this decision task. The task is considered timed
    # out if it doesn't completed within this duration.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DecisionTaskStartedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `DecisionTaskStarted` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_event_id",
                "scheduledEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "identity",
                "identity",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the `DecisionTaskScheduled` event that was recorded when this
    # decision task was scheduled. This information can be useful for diagnosing
    # problems by tracing back the chain of events leading up to this event.
    scheduled_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Identity of the decider making the request. This enables diagnostic tracing
    # when problems arise. The form of this identity is user defined.
    identity: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DecisionTaskTimedOutEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `DecisionTaskTimedOut` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timeout_type",
                "timeoutType",
                autoboto.TypeInfo(DecisionTaskTimeoutType),
            ),
            (
                "scheduled_event_id",
                "scheduledEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The type of timeout that expired before the decision task could be
    # completed.
    timeout_type: "DecisionTaskTimeoutType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskScheduled` event that was recorded when this
    # decision task was scheduled. This information can be useful for diagnosing
    # problems by tracing back the chain of events leading up to this event.
    scheduled_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskStarted` event recorded when this decision task
    # was started. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class DecisionTaskTimeoutType(Enum):
    START_TO_CLOSE = "START_TO_CLOSE"


class DecisionType(Enum):
    ScheduleActivityTask = "ScheduleActivityTask"
    RequestCancelActivityTask = "RequestCancelActivityTask"
    CompleteWorkflowExecution = "CompleteWorkflowExecution"
    FailWorkflowExecution = "FailWorkflowExecution"
    CancelWorkflowExecution = "CancelWorkflowExecution"
    ContinueAsNewWorkflowExecution = "ContinueAsNewWorkflowExecution"
    RecordMarker = "RecordMarker"
    StartTimer = "StartTimer"
    CancelTimer = "CancelTimer"
    SignalExternalWorkflowExecution = "SignalExternalWorkflowExecution"
    RequestCancelExternalWorkflowExecution = "RequestCancelExternalWorkflowExecution"
    StartChildWorkflowExecution = "StartChildWorkflowExecution"
    ScheduleLambdaFunction = "ScheduleLambdaFunction"


@dataclasses.dataclass
class DefaultUndefinedFault(autoboto.ShapeBase):
    """
    The `StartWorkflowExecution` API action was called without the required
    parameters set.

    Some workflow execution parameters, such as the decision `taskList`, must be set
    to start the execution. However, these parameters might have been set as
    defaults when the workflow type was registered. In this case, you can omit these
    parameters from the `StartWorkflowExecution` call and Amazon SWF uses the values
    defined in the workflow type.

    If these parameters aren't set and no default parameters were defined in the
    workflow type, this error is displayed.
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
class DeprecateActivityTypeInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "activity_type",
                "activityType",
                autoboto.TypeInfo(ActivityType),
            ),
        ]

    # The name of the domain in which the activity type is registered.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The activity type to deprecate.
    activity_type: "ActivityType" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeprecateDomainInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the domain to deprecate.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeprecateWorkflowTypeInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
        ]

    # The name of the domain in which the workflow type is registered.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The workflow type to deprecate.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeActivityTypeInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "activity_type",
                "activityType",
                autoboto.TypeInfo(ActivityType),
            ),
        ]

    # The name of the domain in which the activity type is registered.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The activity type to get information about. Activity types are identified
    # by the `name` and `version` that were supplied when the activity was
    # registered.
    activity_type: "ActivityType" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeDomainInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the domain to describe.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeWorkflowExecutionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "execution",
                "execution",
                autoboto.TypeInfo(WorkflowExecution),
            ),
        ]

    # The name of the domain containing the workflow execution.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The workflow execution to describe.
    execution: "WorkflowExecution" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeWorkflowTypeInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
        ]

    # The name of the domain in which this workflow type is registered.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The workflow type to describe.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DomainAlreadyExistsFault(autoboto.ShapeBase):
    """
    Returned if the specified domain already exists. You get this fault even if the
    existing domain is in deprecated status.
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

    # A description that may help with diagnosing the cause of the fault.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DomainConfiguration(autoboto.ShapeBase):
    """
    Contains the configuration settings of a domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_execution_retention_period_in_days",
                "workflowExecutionRetentionPeriodInDays",
                autoboto.TypeInfo(str),
            ),
        ]

    # The retention period for workflow executions in this domain.
    workflow_execution_retention_period_in_days: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DomainDeprecatedFault(autoboto.ShapeBase):
    """
    Returned when the specified domain has been deprecated.
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

    # A description that may help with diagnosing the cause of the fault.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DomainDetail(autoboto.ShapeBase):
    """
    Contains details of a domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_info",
                "domainInfo",
                autoboto.TypeInfo(DomainInfo),
            ),
            (
                "configuration",
                "configuration",
                autoboto.TypeInfo(DomainConfiguration),
            ),
        ]

    # The basic information about a domain, such as its name, status, and
    # description.
    domain_info: "DomainInfo" = dataclasses.field(default_factory=dict, )

    # The domain configuration. Currently, this includes only the domain's
    # retention period.
    configuration: "DomainConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DomainInfo(autoboto.ShapeBase):
    """
    Contains general information about a domain.
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
                "status",
                "status",
                autoboto.TypeInfo(RegistrationStatus),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the domain. This name is unique within the account.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the domain:

    #   * `REGISTERED` – The domain is properly registered and available. You can use this domain for registering types and creating new workflow executions.

    #   * `DEPRECATED` – The domain was deprecated using DeprecateDomain, but is still in use. You should not create new workflow executions in this domain.
    status: "RegistrationStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The description of the domain provided through RegisterDomain.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DomainInfos(autoboto.ShapeBase):
    """
    Contains a paginated collection of DomainInfo structures.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_infos",
                "domainInfos",
                autoboto.TypeInfo(typing.List[DomainInfo]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of DomainInfo structures.
    domain_infos: typing.List["DomainInfo"] = dataclasses.field(
        default_factory=list,
    )

    # If a `NextPageToken` was returned by a previous call, there are more
    # results available. To retrieve the next page of results, make the call
    # again using the returned token in `nextPageToken`. Keep all other arguments
    # unchanged.

    # The configured `maximumPageSize` determines how many results can be
    # returned in a single call.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class EventType(Enum):
    WorkflowExecutionStarted = "WorkflowExecutionStarted"
    WorkflowExecutionCancelRequested = "WorkflowExecutionCancelRequested"
    WorkflowExecutionCompleted = "WorkflowExecutionCompleted"
    CompleteWorkflowExecutionFailed = "CompleteWorkflowExecutionFailed"
    WorkflowExecutionFailed = "WorkflowExecutionFailed"
    FailWorkflowExecutionFailed = "FailWorkflowExecutionFailed"
    WorkflowExecutionTimedOut = "WorkflowExecutionTimedOut"
    WorkflowExecutionCanceled = "WorkflowExecutionCanceled"
    CancelWorkflowExecutionFailed = "CancelWorkflowExecutionFailed"
    WorkflowExecutionContinuedAsNew = "WorkflowExecutionContinuedAsNew"
    ContinueAsNewWorkflowExecutionFailed = "ContinueAsNewWorkflowExecutionFailed"
    WorkflowExecutionTerminated = "WorkflowExecutionTerminated"
    DecisionTaskScheduled = "DecisionTaskScheduled"
    DecisionTaskStarted = "DecisionTaskStarted"
    DecisionTaskCompleted = "DecisionTaskCompleted"
    DecisionTaskTimedOut = "DecisionTaskTimedOut"
    ActivityTaskScheduled = "ActivityTaskScheduled"
    ScheduleActivityTaskFailed = "ScheduleActivityTaskFailed"
    ActivityTaskStarted = "ActivityTaskStarted"
    ActivityTaskCompleted = "ActivityTaskCompleted"
    ActivityTaskFailed = "ActivityTaskFailed"
    ActivityTaskTimedOut = "ActivityTaskTimedOut"
    ActivityTaskCanceled = "ActivityTaskCanceled"
    ActivityTaskCancelRequested = "ActivityTaskCancelRequested"
    RequestCancelActivityTaskFailed = "RequestCancelActivityTaskFailed"
    WorkflowExecutionSignaled = "WorkflowExecutionSignaled"
    MarkerRecorded = "MarkerRecorded"
    RecordMarkerFailed = "RecordMarkerFailed"
    TimerStarted = "TimerStarted"
    StartTimerFailed = "StartTimerFailed"
    TimerFired = "TimerFired"
    TimerCanceled = "TimerCanceled"
    CancelTimerFailed = "CancelTimerFailed"
    StartChildWorkflowExecutionInitiated = "StartChildWorkflowExecutionInitiated"
    StartChildWorkflowExecutionFailed = "StartChildWorkflowExecutionFailed"
    ChildWorkflowExecutionStarted = "ChildWorkflowExecutionStarted"
    ChildWorkflowExecutionCompleted = "ChildWorkflowExecutionCompleted"
    ChildWorkflowExecutionFailed = "ChildWorkflowExecutionFailed"
    ChildWorkflowExecutionTimedOut = "ChildWorkflowExecutionTimedOut"
    ChildWorkflowExecutionCanceled = "ChildWorkflowExecutionCanceled"
    ChildWorkflowExecutionTerminated = "ChildWorkflowExecutionTerminated"
    SignalExternalWorkflowExecutionInitiated = "SignalExternalWorkflowExecutionInitiated"
    SignalExternalWorkflowExecutionFailed = "SignalExternalWorkflowExecutionFailed"
    ExternalWorkflowExecutionSignaled = "ExternalWorkflowExecutionSignaled"
    RequestCancelExternalWorkflowExecutionInitiated = "RequestCancelExternalWorkflowExecutionInitiated"
    RequestCancelExternalWorkflowExecutionFailed = "RequestCancelExternalWorkflowExecutionFailed"
    ExternalWorkflowExecutionCancelRequested = "ExternalWorkflowExecutionCancelRequested"
    LambdaFunctionScheduled = "LambdaFunctionScheduled"
    LambdaFunctionStarted = "LambdaFunctionStarted"
    LambdaFunctionCompleted = "LambdaFunctionCompleted"
    LambdaFunctionFailed = "LambdaFunctionFailed"
    LambdaFunctionTimedOut = "LambdaFunctionTimedOut"
    ScheduleLambdaFunctionFailed = "ScheduleLambdaFunctionFailed"
    StartLambdaFunctionFailed = "StartLambdaFunctionFailed"


class ExecutionStatus(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"


@dataclasses.dataclass
class ExecutionTimeFilter(autoboto.ShapeBase):
    """
    Used to filter the workflow executions in visibility APIs by various time-based
    rules. Each parameter, if specified, defines a rule that must be satisfied by
    each returned query result. The parameter values are in the [Unix Time
    format](https://en.wikipedia.org/wiki/Unix_time). For example: `"oldestDate":
    1325376070.`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "oldest_date",
                "oldestDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "latest_date",
                "latestDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # Specifies the oldest start or close date and time to return.
    oldest_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the latest start or close date and time to return.
    latest_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ExternalWorkflowExecutionCancelRequestedEventAttributes(
    autoboto.ShapeBase
):
    """
    Provides the details of the `ExternalWorkflowExecutionCancelRequested` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_execution",
                "workflowExecution",
                autoboto.TypeInfo(WorkflowExecution),
            ),
            (
                "initiated_event_id",
                "initiatedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The external workflow execution to which the cancellation request was
    # delivered.
    workflow_execution: "WorkflowExecution" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the `RequestCancelExternalWorkflowExecutionInitiated` event
    # corresponding to the `RequestCancelExternalWorkflowExecution` decision to
    # cancel this external workflow execution. This information can be useful for
    # diagnosing problems by tracing back the chain of events leading up to this
    # event.
    initiated_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ExternalWorkflowExecutionSignaledEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ExternalWorkflowExecutionSignaled` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_execution",
                "workflowExecution",
                autoboto.TypeInfo(WorkflowExecution),
            ),
            (
                "initiated_event_id",
                "initiatedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The external workflow execution that the signal was delivered to.
    workflow_execution: "WorkflowExecution" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the `SignalExternalWorkflowExecutionInitiated` event
    # corresponding to the `SignalExternalWorkflowExecution` decision to request
    # this signal. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    initiated_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class FailWorkflowExecutionDecisionAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `FailWorkflowExecution` decision.

    **Access Control**

    You can use IAM policies to control this decision's access to Amazon SWF
    resources as follows:

      * Use a `Resource` element with the domain name to limit the action to only specified domains.

      * Use an `Action` element to allow or deny permission to call this action.

      * You cannot use an IAM policy to constrain this action's parameters.

    If the caller doesn't have sufficient permissions to invoke the action, or the
    parameter values fall outside the specified constraints, the action fails. The
    associated event attribute's `cause` parameter is set to
    `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
    to Manage Access to Amazon SWF
    Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
    iam.html) in the _Amazon SWF Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reason",
                "reason",
                autoboto.TypeInfo(str),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
        ]

    # A descriptive reason for the failure that may help in diagnostics.
    reason: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Details of the failure.
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class FailWorkflowExecutionFailedCause(Enum):
    UNHANDLED_DECISION = "UNHANDLED_DECISION"
    OPERATION_NOT_PERMITTED = "OPERATION_NOT_PERMITTED"


@dataclasses.dataclass
class FailWorkflowExecutionFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `FailWorkflowExecutionFailed` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cause",
                "cause",
                autoboto.TypeInfo(FailWorkflowExecutionFailedCause),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The cause of the failure. This information is generated by the system and
    # can be useful for diagnostic purposes.

    # If `cause` is set to `OPERATION_NOT_PERMITTED`, the decision failed because
    # it lacked sufficient permissions. For details and example IAM policies, see
    # [Using IAM to Manage Access to Amazon SWF
    # Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-
    # dev-iam.html) in the _Amazon SWF Developer Guide_.
    cause: "FailWorkflowExecutionFailedCause" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `FailWorkflowExecution` decision to fail this
    # execution. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetWorkflowExecutionHistoryInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "execution",
                "execution",
                autoboto.TypeInfo(WorkflowExecution),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
            (
                "maximum_page_size",
                "maximumPageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "reverse_order",
                "reverseOrder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the domain containing the workflow execution.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the workflow execution for which to return the history.
    execution: "WorkflowExecution" = dataclasses.field(default_factory=dict, )

    # If a `NextPageToken` was returned by a previous call, there are more
    # results available. To retrieve the next page of results, make the call
    # again using the returned token in `nextPageToken`. Keep all other arguments
    # unchanged.

    # The configured `maximumPageSize` determines how many results can be
    # returned in a single call.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results that are returned per call. `nextPageToken`
    # can be used to obtain futher pages of results. The default is 1000, which
    # is the maximum allowed page size. You can, however, specify a page size
    # _smaller_ than the maximum.

    # This is an upper limit only; the actual number of results returned per call
    # may be fewer than the specified maximum.
    maximum_page_size: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When set to `true`, returns the events in reverse order. By default the
    # results are returned in ascending order of the `eventTimeStamp` of the
    # events.
    reverse_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class History(autoboto.ShapeBase):
    """
    Paginated representation of a workflow history for a workflow execution. This is
    the up to date, complete and authoritative record of the events related to all
    tasks and events in the life of the workflow execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "events",
                "events",
                autoboto.TypeInfo(typing.List[HistoryEvent]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of history events.
    events: typing.List["HistoryEvent"] = dataclasses.field(
        default_factory=list,
    )

    # If a `NextPageToken` was returned by a previous call, there are more
    # results available. To retrieve the next page of results, make the call
    # again using the returned token in `nextPageToken`. Keep all other arguments
    # unchanged.

    # The configured `maximumPageSize` determines how many results can be
    # returned in a single call.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class HistoryEvent(autoboto.ShapeBase):
    """
    Event within a workflow execution. A history event can be one of these types:

      * `ActivityTaskCancelRequested` – A `RequestCancelActivityTask` decision was received by the system.

      * `ActivityTaskCanceled` – The activity task was successfully canceled.

      * `ActivityTaskCompleted` – An activity worker successfully completed an activity task by calling RespondActivityTaskCompleted.

      * `ActivityTaskFailed` – An activity worker failed an activity task by calling RespondActivityTaskFailed.

      * `ActivityTaskScheduled` – An activity task was scheduled for execution.

      * `ActivityTaskStarted` – The scheduled activity task was dispatched to a worker.

      * `ActivityTaskTimedOut` – The activity task timed out.

      * `CancelTimerFailed` – Failed to process CancelTimer decision. This happens when the decision isn't configured properly, for example no timer exists with the specified timer Id.

      * `CancelWorkflowExecutionFailed` – A request to cancel a workflow execution failed.

      * `ChildWorkflowExecutionCanceled` – A child workflow execution, started by this workflow execution, was canceled and closed.

      * `ChildWorkflowExecutionCompleted` – A child workflow execution, started by this workflow execution, completed successfully and was closed.

      * `ChildWorkflowExecutionFailed` – A child workflow execution, started by this workflow execution, failed to complete successfully and was closed.

      * `ChildWorkflowExecutionStarted` – A child workflow execution was successfully started.

      * `ChildWorkflowExecutionTerminated` – A child workflow execution, started by this workflow execution, was terminated.

      * `ChildWorkflowExecutionTimedOut` – A child workflow execution, started by this workflow execution, timed out and was closed.

      * `CompleteWorkflowExecutionFailed` – The workflow execution failed to complete.

      * `ContinueAsNewWorkflowExecutionFailed` – The workflow execution failed to complete after being continued as a new workflow execution.

      * `DecisionTaskCompleted` – The decider successfully completed a decision task by calling RespondDecisionTaskCompleted.

      * `DecisionTaskScheduled` – A decision task was scheduled for the workflow execution.

      * `DecisionTaskStarted` – The decision task was dispatched to a decider.

      * `DecisionTaskTimedOut` – The decision task timed out.

      * `ExternalWorkflowExecutionCancelRequested` – Request to cancel an external workflow execution was successfully delivered to the target execution.

      * `ExternalWorkflowExecutionSignaled` – A signal, requested by this workflow execution, was successfully delivered to the target external workflow execution.

      * `FailWorkflowExecutionFailed` – A request to mark a workflow execution as failed, itself failed.

      * `MarkerRecorded` – A marker was recorded in the workflow history as the result of a `RecordMarker` decision.

      * `RecordMarkerFailed` – A `RecordMarker` decision was returned as failed.

      * `RequestCancelActivityTaskFailed` – Failed to process RequestCancelActivityTask decision. This happens when the decision isn't configured properly.

      * `RequestCancelExternalWorkflowExecutionFailed` – Request to cancel an external workflow execution failed.

      * `RequestCancelExternalWorkflowExecutionInitiated` – A request was made to request the cancellation of an external workflow execution.

      * `ScheduleActivityTaskFailed` – Failed to process ScheduleActivityTask decision. This happens when the decision isn't configured properly, for example the activity type specified isn't registered.

      * `SignalExternalWorkflowExecutionFailed` – The request to signal an external workflow execution failed.

      * `SignalExternalWorkflowExecutionInitiated` – A request to signal an external workflow was made.

      * `StartActivityTaskFailed` – A scheduled activity task failed to start.

      * `StartChildWorkflowExecutionFailed` – Failed to process StartChildWorkflowExecution decision. This happens when the decision isn't configured properly, for example the workflow type specified isn't registered.

      * `StartChildWorkflowExecutionInitiated` – A request was made to start a child workflow execution.

      * `StartTimerFailed` – Failed to process StartTimer decision. This happens when the decision isn't configured properly, for example a timer already exists with the specified timer Id.

      * `TimerCanceled` – A timer, previously started for this workflow execution, was successfully canceled.

      * `TimerFired` – A timer, previously started for this workflow execution, fired.

      * `TimerStarted` – A timer was started for the workflow execution due to a `StartTimer` decision.

      * `WorkflowExecutionCancelRequested` – A request to cancel this workflow execution was made.

      * `WorkflowExecutionCanceled` – The workflow execution was successfully canceled and closed.

      * `WorkflowExecutionCompleted` – The workflow execution was closed due to successful completion.

      * `WorkflowExecutionContinuedAsNew` – The workflow execution was closed and a new execution of the same type was created with the same workflowId.

      * `WorkflowExecutionFailed` – The workflow execution closed due to a failure.

      * `WorkflowExecutionSignaled` – An external signal was received for the workflow execution.

      * `WorkflowExecutionStarted` – The workflow execution was started.

      * `WorkflowExecutionTerminated` – The workflow execution was terminated.

      * `WorkflowExecutionTimedOut` – The workflow execution was closed because a time out was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_timestamp",
                "eventTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "event_type",
                "eventType",
                autoboto.TypeInfo(EventType),
            ),
            (
                "event_id",
                "eventId",
                autoboto.TypeInfo(int),
            ),
            (
                "workflow_execution_started_event_attributes",
                "workflowExecutionStartedEventAttributes",
                autoboto.TypeInfo(WorkflowExecutionStartedEventAttributes),
            ),
            (
                "workflow_execution_completed_event_attributes",
                "workflowExecutionCompletedEventAttributes",
                autoboto.TypeInfo(WorkflowExecutionCompletedEventAttributes),
            ),
            (
                "complete_workflow_execution_failed_event_attributes",
                "completeWorkflowExecutionFailedEventAttributes",
                autoboto.
                TypeInfo(CompleteWorkflowExecutionFailedEventAttributes),
            ),
            (
                "workflow_execution_failed_event_attributes",
                "workflowExecutionFailedEventAttributes",
                autoboto.TypeInfo(WorkflowExecutionFailedEventAttributes),
            ),
            (
                "fail_workflow_execution_failed_event_attributes",
                "failWorkflowExecutionFailedEventAttributes",
                autoboto.TypeInfo(FailWorkflowExecutionFailedEventAttributes),
            ),
            (
                "workflow_execution_timed_out_event_attributes",
                "workflowExecutionTimedOutEventAttributes",
                autoboto.TypeInfo(WorkflowExecutionTimedOutEventAttributes),
            ),
            (
                "workflow_execution_canceled_event_attributes",
                "workflowExecutionCanceledEventAttributes",
                autoboto.TypeInfo(WorkflowExecutionCanceledEventAttributes),
            ),
            (
                "cancel_workflow_execution_failed_event_attributes",
                "cancelWorkflowExecutionFailedEventAttributes",
                autoboto.TypeInfo(CancelWorkflowExecutionFailedEventAttributes),
            ),
            (
                "workflow_execution_continued_as_new_event_attributes",
                "workflowExecutionContinuedAsNewEventAttributes",
                autoboto.
                TypeInfo(WorkflowExecutionContinuedAsNewEventAttributes),
            ),
            (
                "continue_as_new_workflow_execution_failed_event_attributes",
                "continueAsNewWorkflowExecutionFailedEventAttributes",
                autoboto.
                TypeInfo(ContinueAsNewWorkflowExecutionFailedEventAttributes),
            ),
            (
                "workflow_execution_terminated_event_attributes",
                "workflowExecutionTerminatedEventAttributes",
                autoboto.TypeInfo(WorkflowExecutionTerminatedEventAttributes),
            ),
            (
                "workflow_execution_cancel_requested_event_attributes",
                "workflowExecutionCancelRequestedEventAttributes",
                autoboto.
                TypeInfo(WorkflowExecutionCancelRequestedEventAttributes),
            ),
            (
                "decision_task_scheduled_event_attributes",
                "decisionTaskScheduledEventAttributes",
                autoboto.TypeInfo(DecisionTaskScheduledEventAttributes),
            ),
            (
                "decision_task_started_event_attributes",
                "decisionTaskStartedEventAttributes",
                autoboto.TypeInfo(DecisionTaskStartedEventAttributes),
            ),
            (
                "decision_task_completed_event_attributes",
                "decisionTaskCompletedEventAttributes",
                autoboto.TypeInfo(DecisionTaskCompletedEventAttributes),
            ),
            (
                "decision_task_timed_out_event_attributes",
                "decisionTaskTimedOutEventAttributes",
                autoboto.TypeInfo(DecisionTaskTimedOutEventAttributes),
            ),
            (
                "activity_task_scheduled_event_attributes",
                "activityTaskScheduledEventAttributes",
                autoboto.TypeInfo(ActivityTaskScheduledEventAttributes),
            ),
            (
                "activity_task_started_event_attributes",
                "activityTaskStartedEventAttributes",
                autoboto.TypeInfo(ActivityTaskStartedEventAttributes),
            ),
            (
                "activity_task_completed_event_attributes",
                "activityTaskCompletedEventAttributes",
                autoboto.TypeInfo(ActivityTaskCompletedEventAttributes),
            ),
            (
                "activity_task_failed_event_attributes",
                "activityTaskFailedEventAttributes",
                autoboto.TypeInfo(ActivityTaskFailedEventAttributes),
            ),
            (
                "activity_task_timed_out_event_attributes",
                "activityTaskTimedOutEventAttributes",
                autoboto.TypeInfo(ActivityTaskTimedOutEventAttributes),
            ),
            (
                "activity_task_canceled_event_attributes",
                "activityTaskCanceledEventAttributes",
                autoboto.TypeInfo(ActivityTaskCanceledEventAttributes),
            ),
            (
                "activity_task_cancel_requested_event_attributes",
                "activityTaskCancelRequestedEventAttributes",
                autoboto.TypeInfo(ActivityTaskCancelRequestedEventAttributes),
            ),
            (
                "workflow_execution_signaled_event_attributes",
                "workflowExecutionSignaledEventAttributes",
                autoboto.TypeInfo(WorkflowExecutionSignaledEventAttributes),
            ),
            (
                "marker_recorded_event_attributes",
                "markerRecordedEventAttributes",
                autoboto.TypeInfo(MarkerRecordedEventAttributes),
            ),
            (
                "record_marker_failed_event_attributes",
                "recordMarkerFailedEventAttributes",
                autoboto.TypeInfo(RecordMarkerFailedEventAttributes),
            ),
            (
                "timer_started_event_attributes",
                "timerStartedEventAttributes",
                autoboto.TypeInfo(TimerStartedEventAttributes),
            ),
            (
                "timer_fired_event_attributes",
                "timerFiredEventAttributes",
                autoboto.TypeInfo(TimerFiredEventAttributes),
            ),
            (
                "timer_canceled_event_attributes",
                "timerCanceledEventAttributes",
                autoboto.TypeInfo(TimerCanceledEventAttributes),
            ),
            (
                "start_child_workflow_execution_initiated_event_attributes",
                "startChildWorkflowExecutionInitiatedEventAttributes",
                autoboto.
                TypeInfo(StartChildWorkflowExecutionInitiatedEventAttributes),
            ),
            (
                "child_workflow_execution_started_event_attributes",
                "childWorkflowExecutionStartedEventAttributes",
                autoboto.TypeInfo(ChildWorkflowExecutionStartedEventAttributes),
            ),
            (
                "child_workflow_execution_completed_event_attributes",
                "childWorkflowExecutionCompletedEventAttributes",
                autoboto.
                TypeInfo(ChildWorkflowExecutionCompletedEventAttributes),
            ),
            (
                "child_workflow_execution_failed_event_attributes",
                "childWorkflowExecutionFailedEventAttributes",
                autoboto.TypeInfo(ChildWorkflowExecutionFailedEventAttributes),
            ),
            (
                "child_workflow_execution_timed_out_event_attributes",
                "childWorkflowExecutionTimedOutEventAttributes",
                autoboto.
                TypeInfo(ChildWorkflowExecutionTimedOutEventAttributes),
            ),
            (
                "child_workflow_execution_canceled_event_attributes",
                "childWorkflowExecutionCanceledEventAttributes",
                autoboto.
                TypeInfo(ChildWorkflowExecutionCanceledEventAttributes),
            ),
            (
                "child_workflow_execution_terminated_event_attributes",
                "childWorkflowExecutionTerminatedEventAttributes",
                autoboto.
                TypeInfo(ChildWorkflowExecutionTerminatedEventAttributes),
            ),
            (
                "signal_external_workflow_execution_initiated_event_attributes",
                "signalExternalWorkflowExecutionInitiatedEventAttributes",
                autoboto.TypeInfo(
                    SignalExternalWorkflowExecutionInitiatedEventAttributes
                ),
            ),
            (
                "external_workflow_execution_signaled_event_attributes",
                "externalWorkflowExecutionSignaledEventAttributes",
                autoboto.
                TypeInfo(ExternalWorkflowExecutionSignaledEventAttributes),
            ),
            (
                "signal_external_workflow_execution_failed_event_attributes",
                "signalExternalWorkflowExecutionFailedEventAttributes",
                autoboto.
                TypeInfo(SignalExternalWorkflowExecutionFailedEventAttributes),
            ),
            (
                "external_workflow_execution_cancel_requested_event_attributes",
                "externalWorkflowExecutionCancelRequestedEventAttributes",
                autoboto.TypeInfo(
                    ExternalWorkflowExecutionCancelRequestedEventAttributes
                ),
            ),
            (
                "request_cancel_external_workflow_execution_initiated_event_attributes",
                "requestCancelExternalWorkflowExecutionInitiatedEventAttributes",
                autoboto.TypeInfo(
                    RequestCancelExternalWorkflowExecutionInitiatedEventAttributes
                ),
            ),
            (
                "request_cancel_external_workflow_execution_failed_event_attributes",
                "requestCancelExternalWorkflowExecutionFailedEventAttributes",
                autoboto.TypeInfo(
                    RequestCancelExternalWorkflowExecutionFailedEventAttributes
                ),
            ),
            (
                "schedule_activity_task_failed_event_attributes",
                "scheduleActivityTaskFailedEventAttributes",
                autoboto.TypeInfo(ScheduleActivityTaskFailedEventAttributes),
            ),
            (
                "request_cancel_activity_task_failed_event_attributes",
                "requestCancelActivityTaskFailedEventAttributes",
                autoboto.
                TypeInfo(RequestCancelActivityTaskFailedEventAttributes),
            ),
            (
                "start_timer_failed_event_attributes",
                "startTimerFailedEventAttributes",
                autoboto.TypeInfo(StartTimerFailedEventAttributes),
            ),
            (
                "cancel_timer_failed_event_attributes",
                "cancelTimerFailedEventAttributes",
                autoboto.TypeInfo(CancelTimerFailedEventAttributes),
            ),
            (
                "start_child_workflow_execution_failed_event_attributes",
                "startChildWorkflowExecutionFailedEventAttributes",
                autoboto.
                TypeInfo(StartChildWorkflowExecutionFailedEventAttributes),
            ),
            (
                "lambda_function_scheduled_event_attributes",
                "lambdaFunctionScheduledEventAttributes",
                autoboto.TypeInfo(LambdaFunctionScheduledEventAttributes),
            ),
            (
                "lambda_function_started_event_attributes",
                "lambdaFunctionStartedEventAttributes",
                autoboto.TypeInfo(LambdaFunctionStartedEventAttributes),
            ),
            (
                "lambda_function_completed_event_attributes",
                "lambdaFunctionCompletedEventAttributes",
                autoboto.TypeInfo(LambdaFunctionCompletedEventAttributes),
            ),
            (
                "lambda_function_failed_event_attributes",
                "lambdaFunctionFailedEventAttributes",
                autoboto.TypeInfo(LambdaFunctionFailedEventAttributes),
            ),
            (
                "lambda_function_timed_out_event_attributes",
                "lambdaFunctionTimedOutEventAttributes",
                autoboto.TypeInfo(LambdaFunctionTimedOutEventAttributes),
            ),
            (
                "schedule_lambda_function_failed_event_attributes",
                "scheduleLambdaFunctionFailedEventAttributes",
                autoboto.TypeInfo(ScheduleLambdaFunctionFailedEventAttributes),
            ),
            (
                "start_lambda_function_failed_event_attributes",
                "startLambdaFunctionFailedEventAttributes",
                autoboto.TypeInfo(StartLambdaFunctionFailedEventAttributes),
            ),
        ]

    # The date and time when the event occurred.
    event_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of the history event.
    event_type: "EventType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The system generated ID of the event. This ID uniquely identifies the event
    # with in the workflow execution history.
    event_id: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If the event is of type `WorkflowExecutionStarted` then this member is set
    # and provides detailed information about the event. It isn't set for other
    # event types.
    workflow_execution_started_event_attributes: "WorkflowExecutionStartedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `WorkflowExecutionCompleted` then this member is
    # set and provides detailed information about the event. It isn't set for
    # other event types.
    workflow_execution_completed_event_attributes: "WorkflowExecutionCompletedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `CompleteWorkflowExecutionFailed` then this member
    # is set and provides detailed information about the event. It isn't set for
    # other event types.
    complete_workflow_execution_failed_event_attributes: "CompleteWorkflowExecutionFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `WorkflowExecutionFailed` then this member is set
    # and provides detailed information about the event. It isn't set for other
    # event types.
    workflow_execution_failed_event_attributes: "WorkflowExecutionFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `FailWorkflowExecutionFailed` then this member is
    # set and provides detailed information about the event. It isn't set for
    # other event types.
    fail_workflow_execution_failed_event_attributes: "FailWorkflowExecutionFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `WorkflowExecutionTimedOut` then this member is set
    # and provides detailed information about the event. It isn't set for other
    # event types.
    workflow_execution_timed_out_event_attributes: "WorkflowExecutionTimedOutEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `WorkflowExecutionCanceled` then this member is set
    # and provides detailed information about the event. It isn't set for other
    # event types.
    workflow_execution_canceled_event_attributes: "WorkflowExecutionCanceledEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `CancelWorkflowExecutionFailed` then this member is
    # set and provides detailed information about the event. It isn't set for
    # other event types.
    cancel_workflow_execution_failed_event_attributes: "CancelWorkflowExecutionFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `WorkflowExecutionContinuedAsNew` then this member
    # is set and provides detailed information about the event. It isn't set for
    # other event types.
    workflow_execution_continued_as_new_event_attributes: "WorkflowExecutionContinuedAsNewEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ContinueAsNewWorkflowExecutionFailed` then this
    # member is set and provides detailed information about the event. It isn't
    # set for other event types.
    continue_as_new_workflow_execution_failed_event_attributes: "ContinueAsNewWorkflowExecutionFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `WorkflowExecutionTerminated` then this member is
    # set and provides detailed information about the event. It isn't set for
    # other event types.
    workflow_execution_terminated_event_attributes: "WorkflowExecutionTerminatedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `WorkflowExecutionCancelRequested` then this member
    # is set and provides detailed information about the event. It isn't set for
    # other event types.
    workflow_execution_cancel_requested_event_attributes: "WorkflowExecutionCancelRequestedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `DecisionTaskScheduled` then this member is set and
    # provides detailed information about the event. It isn't set for other event
    # types.
    decision_task_scheduled_event_attributes: "DecisionTaskScheduledEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `DecisionTaskStarted` then this member is set and
    # provides detailed information about the event. It isn't set for other event
    # types.
    decision_task_started_event_attributes: "DecisionTaskStartedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `DecisionTaskCompleted` then this member is set and
    # provides detailed information about the event. It isn't set for other event
    # types.
    decision_task_completed_event_attributes: "DecisionTaskCompletedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `DecisionTaskTimedOut` then this member is set and
    # provides detailed information about the event. It isn't set for other event
    # types.
    decision_task_timed_out_event_attributes: "DecisionTaskTimedOutEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ActivityTaskScheduled` then this member is set and
    # provides detailed information about the event. It isn't set for other event
    # types.
    activity_task_scheduled_event_attributes: "ActivityTaskScheduledEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ActivityTaskStarted` then this member is set and
    # provides detailed information about the event. It isn't set for other event
    # types.
    activity_task_started_event_attributes: "ActivityTaskStartedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ActivityTaskCompleted` then this member is set and
    # provides detailed information about the event. It isn't set for other event
    # types.
    activity_task_completed_event_attributes: "ActivityTaskCompletedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ActivityTaskFailed` then this member is set and
    # provides detailed information about the event. It isn't set for other event
    # types.
    activity_task_failed_event_attributes: "ActivityTaskFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ActivityTaskTimedOut` then this member is set and
    # provides detailed information about the event. It isn't set for other event
    # types.
    activity_task_timed_out_event_attributes: "ActivityTaskTimedOutEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ActivityTaskCanceled` then this member is set and
    # provides detailed information about the event. It isn't set for other event
    # types.
    activity_task_canceled_event_attributes: "ActivityTaskCanceledEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ActivityTaskcancelRequested` then this member is
    # set and provides detailed information about the event. It isn't set for
    # other event types.
    activity_task_cancel_requested_event_attributes: "ActivityTaskCancelRequestedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `WorkflowExecutionSignaled` then this member is set
    # and provides detailed information about the event. It isn't set for other
    # event types.
    workflow_execution_signaled_event_attributes: "WorkflowExecutionSignaledEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `MarkerRecorded` then this member is set and
    # provides detailed information about the event. It isn't set for other event
    # types.
    marker_recorded_event_attributes: "MarkerRecordedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `DecisionTaskFailed` then this member is set and
    # provides detailed information about the event. It isn't set for other event
    # types.
    record_marker_failed_event_attributes: "RecordMarkerFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `TimerStarted` then this member is set and provides
    # detailed information about the event. It isn't set for other event types.
    timer_started_event_attributes: "TimerStartedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `TimerFired` then this member is set and provides
    # detailed information about the event. It isn't set for other event types.
    timer_fired_event_attributes: "TimerFiredEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `TimerCanceled` then this member is set and
    # provides detailed information about the event. It isn't set for other event
    # types.
    timer_canceled_event_attributes: "TimerCanceledEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `StartChildWorkflowExecutionInitiated` then this
    # member is set and provides detailed information about the event. It isn't
    # set for other event types.
    start_child_workflow_execution_initiated_event_attributes: "StartChildWorkflowExecutionInitiatedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ChildWorkflowExecutionStarted` then this member is
    # set and provides detailed information about the event. It isn't set for
    # other event types.
    child_workflow_execution_started_event_attributes: "ChildWorkflowExecutionStartedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ChildWorkflowExecutionCompleted` then this member
    # is set and provides detailed information about the event. It isn't set for
    # other event types.
    child_workflow_execution_completed_event_attributes: "ChildWorkflowExecutionCompletedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ChildWorkflowExecutionFailed` then this member is
    # set and provides detailed information about the event. It isn't set for
    # other event types.
    child_workflow_execution_failed_event_attributes: "ChildWorkflowExecutionFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ChildWorkflowExecutionTimedOut` then this member
    # is set and provides detailed information about the event. It isn't set for
    # other event types.
    child_workflow_execution_timed_out_event_attributes: "ChildWorkflowExecutionTimedOutEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ChildWorkflowExecutionCanceled` then this member
    # is set and provides detailed information about the event. It isn't set for
    # other event types.
    child_workflow_execution_canceled_event_attributes: "ChildWorkflowExecutionCanceledEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ChildWorkflowExecutionTerminated` then this member
    # is set and provides detailed information about the event. It isn't set for
    # other event types.
    child_workflow_execution_terminated_event_attributes: "ChildWorkflowExecutionTerminatedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `SignalExternalWorkflowExecutionInitiated` then
    # this member is set and provides detailed information about the event. It
    # isn't set for other event types.
    signal_external_workflow_execution_initiated_event_attributes: "SignalExternalWorkflowExecutionInitiatedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ExternalWorkflowExecutionSignaled` then this
    # member is set and provides detailed information about the event. It isn't
    # set for other event types.
    external_workflow_execution_signaled_event_attributes: "ExternalWorkflowExecutionSignaledEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `SignalExternalWorkflowExecutionFailed` then this
    # member is set and provides detailed information about the event. It isn't
    # set for other event types.
    signal_external_workflow_execution_failed_event_attributes: "SignalExternalWorkflowExecutionFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ExternalWorkflowExecutionCancelRequested` then
    # this member is set and provides detailed information about the event. It
    # isn't set for other event types.
    external_workflow_execution_cancel_requested_event_attributes: "ExternalWorkflowExecutionCancelRequestedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `RequestCancelExternalWorkflowExecutionInitiated`
    # then this member is set and provides detailed information about the event.
    # It isn't set for other event types.
    request_cancel_external_workflow_execution_initiated_event_attributes: "RequestCancelExternalWorkflowExecutionInitiatedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `RequestCancelExternalWorkflowExecutionFailed` then
    # this member is set and provides detailed information about the event. It
    # isn't set for other event types.
    request_cancel_external_workflow_execution_failed_event_attributes: "RequestCancelExternalWorkflowExecutionFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `ScheduleActivityTaskFailed` then this member is
    # set and provides detailed information about the event. It isn't set for
    # other event types.
    schedule_activity_task_failed_event_attributes: "ScheduleActivityTaskFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `RequestCancelActivityTaskFailed` then this member
    # is set and provides detailed information about the event. It isn't set for
    # other event types.
    request_cancel_activity_task_failed_event_attributes: "RequestCancelActivityTaskFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `StartTimerFailed` then this member is set and
    # provides detailed information about the event. It isn't set for other event
    # types.
    start_timer_failed_event_attributes: "StartTimerFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `CancelTimerFailed` then this member is set and
    # provides detailed information about the event. It isn't set for other event
    # types.
    cancel_timer_failed_event_attributes: "CancelTimerFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # If the event is of type `StartChildWorkflowExecutionFailed` then this
    # member is set and provides detailed information about the event. It isn't
    # set for other event types.
    start_child_workflow_execution_failed_event_attributes: "StartChildWorkflowExecutionFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `LambdaFunctionScheduled` event. It isn't set
    # for other event types.
    lambda_function_scheduled_event_attributes: "LambdaFunctionScheduledEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `LambdaFunctionStarted` event. It isn't set for
    # other event types.
    lambda_function_started_event_attributes: "LambdaFunctionStartedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `LambdaFunctionCompleted` event. It isn't set
    # for other event types.
    lambda_function_completed_event_attributes: "LambdaFunctionCompletedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `LambdaFunctionFailed` event. It isn't set for
    # other event types.
    lambda_function_failed_event_attributes: "LambdaFunctionFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `LambdaFunctionTimedOut` event. It isn't set
    # for other event types.
    lambda_function_timed_out_event_attributes: "LambdaFunctionTimedOutEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `ScheduleLambdaFunctionFailed` event. It isn't
    # set for other event types.
    schedule_lambda_function_failed_event_attributes: "ScheduleLambdaFunctionFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )

    # Provides the details of the `StartLambdaFunctionFailed` event. It isn't set
    # for other event types.
    start_lambda_function_failed_event_attributes: "StartLambdaFunctionFailedEventAttributes" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class LambdaFunctionCompletedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `LambdaFunctionCompleted` event. It isn't set for
    other event types.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_event_id",
                "scheduledEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "result",
                "result",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the `LambdaFunctionScheduled` event that was recorded when this
    # Lambda task was scheduled. To help diagnose issues, use this information to
    # trace back the chain of events leading up to this event.
    scheduled_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `LambdaFunctionStarted` event recorded when this activity
    # task started. To help diagnose issues, use this information to trace back
    # the chain of events leading up to this event.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The results of the Lambda task.
    result: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LambdaFunctionFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `LambdaFunctionFailed` event. It isn't set for other
    event types.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_event_id",
                "scheduledEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "reason",
                "reason",
                autoboto.TypeInfo(str),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the `LambdaFunctionScheduled` event that was recorded when this
    # activity task was scheduled. To help diagnose issues, use this information
    # to trace back the chain of events leading up to this event.
    scheduled_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `LambdaFunctionStarted` event recorded when this activity
    # task started. To help diagnose issues, use this information to trace back
    # the chain of events leading up to this event.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The reason provided for the failure.
    reason: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The details of the failure.
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LambdaFunctionScheduledEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `LambdaFunctionScheduled` event. It isn't set for
    other event types.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "control",
                "control",
                autoboto.TypeInfo(str),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
            (
                "start_to_close_timeout",
                "startToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the Lambda task.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the Lambda function.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the `LambdaFunctionCompleted` event corresponding to the decision
    # that resulted in scheduling this activity task. To help diagnose issues,
    # use this information to trace back the chain of events leading up to this
    # event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Data attached to the event that the decider can use in subsequent workflow
    # tasks. This data isn't sent to the Lambda task.
    control: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The input provided to the Lambda task.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum amount of time a worker can take to process the Lambda task.
    start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class LambdaFunctionStartedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `LambdaFunctionStarted` event. It isn't set for
    other event types.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_event_id",
                "scheduledEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the `LambdaFunctionScheduled` event that was recorded when this
    # activity task was scheduled. To help diagnose issues, use this information
    # to trace back the chain of events leading up to this event.
    scheduled_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class LambdaFunctionTimedOutEventAttributes(autoboto.ShapeBase):
    """
    Provides details of the `LambdaFunctionTimedOut` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_event_id",
                "scheduledEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "timeout_type",
                "timeoutType",
                autoboto.TypeInfo(LambdaFunctionTimeoutType),
            ),
        ]

    # The ID of the `LambdaFunctionScheduled` event that was recorded when this
    # activity task was scheduled. To help diagnose issues, use this information
    # to trace back the chain of events leading up to this event.
    scheduled_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `ActivityTaskStarted` event that was recorded when this
    # activity task started. To help diagnose issues, use this information to
    # trace back the chain of events leading up to this event.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of the timeout that caused this event.
    timeout_type: "LambdaFunctionTimeoutType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class LambdaFunctionTimeoutType(Enum):
    START_TO_CLOSE = "START_TO_CLOSE"


@dataclasses.dataclass
class LimitExceededFault(autoboto.ShapeBase):
    """
    Returned by any operation if a system imposed limitation has been reached. To
    address this fault you should either clean up unused resources or increase the
    limit by contacting AWS.
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

    # A description that may help with diagnosing the cause of the fault.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListActivityTypesInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "registration_status",
                "registrationStatus",
                autoboto.TypeInfo(RegistrationStatus),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
            (
                "maximum_page_size",
                "maximumPageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "reverse_order",
                "reverseOrder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the domain in which the activity types have been registered.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the registration status of the activity types to list.
    registration_status: "RegistrationStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If specified, only lists the activity types that have this name.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If a `NextPageToken` was returned by a previous call, there are more
    # results available. To retrieve the next page of results, make the call
    # again using the returned token in `nextPageToken`. Keep all other arguments
    # unchanged.

    # The configured `maximumPageSize` determines how many results can be
    # returned in a single call.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results that are returned per call. `nextPageToken`
    # can be used to obtain futher pages of results. The default is 1000, which
    # is the maximum allowed page size. You can, however, specify a page size
    # _smaller_ than the maximum.

    # This is an upper limit only; the actual number of results returned per call
    # may be fewer than the specified maximum.
    maximum_page_size: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When set to `true`, returns the results in reverse order. By default, the
    # results are returned in ascending alphabetical order by `name` of the
    # activity types.
    reverse_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListClosedWorkflowExecutionsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "start_time_filter",
                "startTimeFilter",
                autoboto.TypeInfo(ExecutionTimeFilter),
            ),
            (
                "close_time_filter",
                "closeTimeFilter",
                autoboto.TypeInfo(ExecutionTimeFilter),
            ),
            (
                "execution_filter",
                "executionFilter",
                autoboto.TypeInfo(WorkflowExecutionFilter),
            ),
            (
                "close_status_filter",
                "closeStatusFilter",
                autoboto.TypeInfo(CloseStatusFilter),
            ),
            (
                "type_filter",
                "typeFilter",
                autoboto.TypeInfo(WorkflowTypeFilter),
            ),
            (
                "tag_filter",
                "tagFilter",
                autoboto.TypeInfo(TagFilter),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
            (
                "maximum_page_size",
                "maximumPageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "reverse_order",
                "reverseOrder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the domain that contains the workflow executions to list.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If specified, the workflow executions are included in the returned results
    # based on whether their start times are within the range specified by this
    # filter. Also, if this parameter is specified, the returned results are
    # ordered by their start times.

    # `startTimeFilter` and `closeTimeFilter` are mutually exclusive. You must
    # specify one of these in a request but not both.
    start_time_filter: "ExecutionTimeFilter" = dataclasses.field(
        default_factory=dict,
    )

    # If specified, the workflow executions are included in the returned results
    # based on whether their close times are within the range specified by this
    # filter. Also, if this parameter is specified, the returned results are
    # ordered by their close times.

    # `startTimeFilter` and `closeTimeFilter` are mutually exclusive. You must
    # specify one of these in a request but not both.
    close_time_filter: "ExecutionTimeFilter" = dataclasses.field(
        default_factory=dict,
    )

    # If specified, only workflow executions matching the workflow ID specified
    # in the filter are returned.

    # `closeStatusFilter`, `executionFilter`, `typeFilter` and `tagFilter` are
    # mutually exclusive. You can specify at most one of these in a request.
    execution_filter: "WorkflowExecutionFilter" = dataclasses.field(
        default_factory=dict,
    )

    # If specified, only workflow executions that match this _close status_ are
    # listed. For example, if TERMINATED is specified, then only TERMINATED
    # workflow executions are listed.

    # `closeStatusFilter`, `executionFilter`, `typeFilter` and `tagFilter` are
    # mutually exclusive. You can specify at most one of these in a request.
    close_status_filter: "CloseStatusFilter" = dataclasses.field(
        default_factory=dict,
    )

    # If specified, only executions of the type specified in the filter are
    # returned.

    # `closeStatusFilter`, `executionFilter`, `typeFilter` and `tagFilter` are
    # mutually exclusive. You can specify at most one of these in a request.
    type_filter: "WorkflowTypeFilter" = dataclasses.field(
        default_factory=dict,
    )

    # If specified, only executions that have the matching tag are listed.

    # `closeStatusFilter`, `executionFilter`, `typeFilter` and `tagFilter` are
    # mutually exclusive. You can specify at most one of these in a request.
    tag_filter: "TagFilter" = dataclasses.field(default_factory=dict, )

    # If a `NextPageToken` was returned by a previous call, there are more
    # results available. To retrieve the next page of results, make the call
    # again using the returned token in `nextPageToken`. Keep all other arguments
    # unchanged.

    # The configured `maximumPageSize` determines how many results can be
    # returned in a single call.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results that are returned per call. `nextPageToken`
    # can be used to obtain futher pages of results. The default is 1000, which
    # is the maximum allowed page size. You can, however, specify a page size
    # _smaller_ than the maximum.

    # This is an upper limit only; the actual number of results returned per call
    # may be fewer than the specified maximum.
    maximum_page_size: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When set to `true`, returns the results in reverse order. By default the
    # results are returned in descending order of the start or the close time of
    # the executions.
    reverse_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListDomainsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registration_status",
                "registrationStatus",
                autoboto.TypeInfo(RegistrationStatus),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
            (
                "maximum_page_size",
                "maximumPageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "reverse_order",
                "reverseOrder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Specifies the registration status of the domains to list.
    registration_status: "RegistrationStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If a `NextPageToken` was returned by a previous call, there are more
    # results available. To retrieve the next page of results, make the call
    # again using the returned token in `nextPageToken`. Keep all other arguments
    # unchanged.

    # The configured `maximumPageSize` determines how many results can be
    # returned in a single call.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results that are returned per call. `nextPageToken`
    # can be used to obtain futher pages of results. The default is 1000, which
    # is the maximum allowed page size. You can, however, specify a page size
    # _smaller_ than the maximum.

    # This is an upper limit only; the actual number of results returned per call
    # may be fewer than the specified maximum.
    maximum_page_size: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When set to `true`, returns the results in reverse order. By default, the
    # results are returned in ascending alphabetical order by `name` of the
    # domains.
    reverse_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListOpenWorkflowExecutionsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "start_time_filter",
                "startTimeFilter",
                autoboto.TypeInfo(ExecutionTimeFilter),
            ),
            (
                "type_filter",
                "typeFilter",
                autoboto.TypeInfo(WorkflowTypeFilter),
            ),
            (
                "tag_filter",
                "tagFilter",
                autoboto.TypeInfo(TagFilter),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
            (
                "maximum_page_size",
                "maximumPageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "reverse_order",
                "reverseOrder",
                autoboto.TypeInfo(bool),
            ),
            (
                "execution_filter",
                "executionFilter",
                autoboto.TypeInfo(WorkflowExecutionFilter),
            ),
        ]

    # The name of the domain that contains the workflow executions to list.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Workflow executions are included in the returned results based on whether
    # their start times are within the range specified by this filter.
    start_time_filter: "ExecutionTimeFilter" = dataclasses.field(
        default_factory=dict,
    )

    # If specified, only executions of the type specified in the filter are
    # returned.

    # `executionFilter`, `typeFilter` and `tagFilter` are mutually exclusive. You
    # can specify at most one of these in a request.
    type_filter: "WorkflowTypeFilter" = dataclasses.field(
        default_factory=dict,
    )

    # If specified, only executions that have the matching tag are listed.

    # `executionFilter`, `typeFilter` and `tagFilter` are mutually exclusive. You
    # can specify at most one of these in a request.
    tag_filter: "TagFilter" = dataclasses.field(default_factory=dict, )

    # If a `NextPageToken` was returned by a previous call, there are more
    # results available. To retrieve the next page of results, make the call
    # again using the returned token in `nextPageToken`. Keep all other arguments
    # unchanged.

    # The configured `maximumPageSize` determines how many results can be
    # returned in a single call.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results that are returned per call. `nextPageToken`
    # can be used to obtain futher pages of results. The default is 1000, which
    # is the maximum allowed page size. You can, however, specify a page size
    # _smaller_ than the maximum.

    # This is an upper limit only; the actual number of results returned per call
    # may be fewer than the specified maximum.
    maximum_page_size: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When set to `true`, returns the results in reverse order. By default the
    # results are returned in descending order of the start time of the
    # executions.
    reverse_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If specified, only workflow executions matching the workflow ID specified
    # in the filter are returned.

    # `executionFilter`, `typeFilter` and `tagFilter` are mutually exclusive. You
    # can specify at most one of these in a request.
    execution_filter: "WorkflowExecutionFilter" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ListWorkflowTypesInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "registration_status",
                "registrationStatus",
                autoboto.TypeInfo(RegistrationStatus),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
            (
                "maximum_page_size",
                "maximumPageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "reverse_order",
                "reverseOrder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the domain in which the workflow types have been registered.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the registration status of the workflow types to list.
    registration_status: "RegistrationStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If specified, lists the workflow type with this name.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If a `NextPageToken` was returned by a previous call, there are more
    # results available. To retrieve the next page of results, make the call
    # again using the returned token in `nextPageToken`. Keep all other arguments
    # unchanged.

    # The configured `maximumPageSize` determines how many results can be
    # returned in a single call.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results that are returned per call. `nextPageToken`
    # can be used to obtain futher pages of results. The default is 1000, which
    # is the maximum allowed page size. You can, however, specify a page size
    # _smaller_ than the maximum.

    # This is an upper limit only; the actual number of results returned per call
    # may be fewer than the specified maximum.
    maximum_page_size: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When set to `true`, returns the results in reverse order. By default the
    # results are returned in ascending alphabetical order of the `name` of the
    # workflow types.
    reverse_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class MarkerRecordedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `MarkerRecorded` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker_name",
                "markerName",
                autoboto.TypeInfo(str),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the marker.
    marker_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `RecordMarker` decision that requested this
    # marker. This information can be useful for diagnosing problems by tracing
    # back the chain of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The details of the marker.
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class OperationNotPermittedFault(autoboto.ShapeBase):
    """
    Returned when the caller doesn't have sufficient permissions to invoke the
    action.
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

    # A description that may help with diagnosing the cause of the fault.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PendingTaskCount(autoboto.ShapeBase):
    """
    Contains the count of tasks in a task list.
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
                "truncated",
                "truncated",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The number of tasks in the task list.
    count: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If set to true, indicates that the actual count was more than the maximum
    # supported by this API and the count returned is the truncated value.
    truncated: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PollForActivityTaskInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "task_list",
                "taskList",
                autoboto.TypeInfo(TaskList),
            ),
            (
                "identity",
                "identity",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the domain that contains the task lists being polled.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the task list to poll for activity tasks.

    # The specified string must not start or end with whitespace. It must not
    # contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control
    # characters (`\u0000-\u001f` | `\u007f-\u009f`). Also, it must not contain
    # the literal string `arn`.
    task_list: "TaskList" = dataclasses.field(default_factory=dict, )

    # Identity of the worker making the request, recorded in the
    # `ActivityTaskStarted` event in the workflow history. This enables
    # diagnostic tracing when problems arise. The form of this identity is user
    # defined.
    identity: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PollForDecisionTaskInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "task_list",
                "taskList",
                autoboto.TypeInfo(TaskList),
            ),
            (
                "identity",
                "identity",
                autoboto.TypeInfo(str),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
            (
                "maximum_page_size",
                "maximumPageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "reverse_order",
                "reverseOrder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the domain containing the task lists to poll.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the task list to poll for decision tasks.

    # The specified string must not start or end with whitespace. It must not
    # contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control
    # characters (`\u0000-\u001f` | `\u007f-\u009f`). Also, it must not contain
    # the literal string `arn`.
    task_list: "TaskList" = dataclasses.field(default_factory=dict, )

    # Identity of the decider making the request, which is recorded in the
    # DecisionTaskStarted event in the workflow history. This enables diagnostic
    # tracing when problems arise. The form of this identity is user defined.
    identity: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If a `NextPageToken` was returned by a previous call, there are more
    # results available. To retrieve the next page of results, make the call
    # again using the returned token in `nextPageToken`. Keep all other arguments
    # unchanged.

    # The configured `maximumPageSize` determines how many results can be
    # returned in a single call.

    # The `nextPageToken` returned by this action cannot be used with
    # GetWorkflowExecutionHistory to get the next page. You must call
    # PollForDecisionTask again (with the `nextPageToken`) to retrieve the next
    # page of history records. Calling PollForDecisionTask with a `nextPageToken`
    # doesn't return a new decision task.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results that are returned per call. `nextPageToken`
    # can be used to obtain futher pages of results. The default is 1000, which
    # is the maximum allowed page size. You can, however, specify a page size
    # _smaller_ than the maximum.

    # This is an upper limit only; the actual number of results returned per call
    # may be fewer than the specified maximum.
    maximum_page_size: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When set to `true`, returns the events in reverse order. By default the
    # results are returned in ascending order of the `eventTimestamp` of the
    # events.
    reverse_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RecordActivityTaskHeartbeatInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_token",
                "taskToken",
                autoboto.TypeInfo(str),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `taskToken` of the ActivityTask.

    # `taskToken` is generated by the service and should be treated as an opaque
    # value. If the task is passed to another process, its `taskToken` must also
    # be passed. This enables it to provide its progress and respond with
    # results.
    task_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If specified, contains details about the progress of the task.
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RecordMarkerDecisionAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `RecordMarker` decision.

    **Access Control**

    You can use IAM policies to control this decision's access to Amazon SWF
    resources as follows:

      * Use a `Resource` element with the domain name to limit the action to only specified domains.

      * Use an `Action` element to allow or deny permission to call this action.

      * You cannot use an IAM policy to constrain this action's parameters.

    If the caller doesn't have sufficient permissions to invoke the action, or the
    parameter values fall outside the specified constraints, the action fails. The
    associated event attribute's `cause` parameter is set to
    `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
    to Manage Access to Amazon SWF
    Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
    iam.html) in the _Amazon SWF Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker_name",
                "markerName",
                autoboto.TypeInfo(str),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the marker.
    marker_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The details of the marker.
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class RecordMarkerFailedCause(Enum):
    OPERATION_NOT_PERMITTED = "OPERATION_NOT_PERMITTED"


@dataclasses.dataclass
class RecordMarkerFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `RecordMarkerFailed` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker_name",
                "markerName",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(RecordMarkerFailedCause),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The marker's name.
    marker_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The cause of the failure. This information is generated by the system and
    # can be useful for diagnostic purposes.

    # If `cause` is set to `OPERATION_NOT_PERMITTED`, the decision failed because
    # it lacked sufficient permissions. For details and example IAM policies, see
    # [Using IAM to Manage Access to Amazon SWF
    # Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-
    # dev-iam.html) in the _Amazon SWF Developer Guide_.
    cause: "RecordMarkerFailedCause" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `RecordMarkerFailed` decision for this
    # cancellation request. This information can be useful for diagnosing
    # problems by tracing back the chain of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RegisterActivityTypeInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
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
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "default_task_start_to_close_timeout",
                "defaultTaskStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "default_task_heartbeat_timeout",
                "defaultTaskHeartbeatTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "default_task_list",
                "defaultTaskList",
                autoboto.TypeInfo(TaskList),
            ),
            (
                "default_task_priority",
                "defaultTaskPriority",
                autoboto.TypeInfo(str),
            ),
            (
                "default_task_schedule_to_start_timeout",
                "defaultTaskScheduleToStartTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "default_task_schedule_to_close_timeout",
                "defaultTaskScheduleToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the domain in which this activity is to be registered.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the activity type within the domain.

    # The specified string must not start or end with whitespace. It must not
    # contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control
    # characters (`\u0000-\u001f` | `\u007f-\u009f`). Also, it must not contain
    # the literal string `arn`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the activity type.

    # The activity type consists of the name and version, the combination of
    # which must be unique within the domain.

    # The specified string must not start or end with whitespace. It must not
    # contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control
    # characters (`\u0000-\u001f` | `\u007f-\u009f`). Also, it must not contain
    # the literal string `arn`.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A textual description of the activity type.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If set, specifies the default maximum duration that a worker can take to
    # process tasks of this activity type. This default can be overridden when
    # scheduling an activity task using the `ScheduleActivityTask` Decision.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    default_task_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If set, specifies the default maximum time before which a worker processing
    # a task of this type must report progress by calling
    # RecordActivityTaskHeartbeat. If the timeout is exceeded, the activity task
    # is automatically timed out. This default can be overridden when scheduling
    # an activity task using the `ScheduleActivityTask` Decision. If the activity
    # worker subsequently attempts to record a heartbeat or returns a result, the
    # activity worker receives an `UnknownResource` fault. In this case, Amazon
    # SWF no longer considers the activity task to be valid; the activity worker
    # should clean up the activity task.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    default_task_heartbeat_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If set, specifies the default task list to use for scheduling tasks of this
    # activity type. This default task list is used if a task list isn't provided
    # when a task is scheduled through the `ScheduleActivityTask` Decision.
    default_task_list: "TaskList" = dataclasses.field(default_factory=dict, )

    # The default task priority to assign to the activity type. If not assigned,
    # then `0` is used. Valid values are integers that range from Java's
    # `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647).
    # Higher numbers indicate higher priority.

    # For more information about setting task priority, see [Setting Task
    # Priority](http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-
    # priority.html) in the _in the _Amazon SWF Developer Guide_._.
    default_task_priority: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If set, specifies the default maximum duration that a task of this activity
    # type can wait before being assigned to a worker. This default can be
    # overridden when scheduling an activity task using the
    # `ScheduleActivityTask` Decision.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    default_task_schedule_to_start_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If set, specifies the default maximum duration for a task of this activity
    # type. This default can be overridden when scheduling an activity task using
    # the `ScheduleActivityTask` Decision.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    default_task_schedule_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RegisterDomainInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "workflow_execution_retention_period_in_days",
                "workflowExecutionRetentionPeriodInDays",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the domain to register. The name must be unique in the region that
    # the domain is registered in.

    # The specified string must not start or end with whitespace. It must not
    # contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control
    # characters (`\u0000-\u001f` | `\u007f-\u009f`). Also, it must not contain
    # the literal string `arn`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The duration (in days) that records and histories of workflow executions on
    # the domain should be kept by the service. After the retention period, the
    # workflow execution isn't available in the results of visibility calls.

    # If you pass the value `NONE` or `0` (zero), then the workflow execution
    # history isn't retained. As soon as the workflow execution completes, the
    # execution record and its history are deleted.

    # The maximum workflow execution retention period is 90 days. For more
    # information about Amazon SWF service limits, see: [Amazon SWF Service
    # Limits](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-
    # limits.html) in the _Amazon SWF Developer Guide_.
    workflow_execution_retention_period_in_days: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A text description of the domain.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RegisterWorkflowTypeInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
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
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "default_task_start_to_close_timeout",
                "defaultTaskStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "default_execution_start_to_close_timeout",
                "defaultExecutionStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "default_task_list",
                "defaultTaskList",
                autoboto.TypeInfo(TaskList),
            ),
            (
                "default_task_priority",
                "defaultTaskPriority",
                autoboto.TypeInfo(str),
            ),
            (
                "default_child_policy",
                "defaultChildPolicy",
                autoboto.TypeInfo(ChildPolicy),
            ),
            (
                "default_lambda_role",
                "defaultLambdaRole",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the domain in which to register the workflow type.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the workflow type.

    # The specified string must not start or end with whitespace. It must not
    # contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control
    # characters (`\u0000-\u001f` | `\u007f-\u009f`). Also, it must not contain
    # the literal string `arn`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the workflow type.

    # The workflow type consists of the name and version, the combination of
    # which must be unique within the domain. To get a list of all currently
    # registered workflow types, use the ListWorkflowTypes action.

    # The specified string must not start or end with whitespace. It must not
    # contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control
    # characters (`\u0000-\u001f` | `\u007f-\u009f`). Also, it must not contain
    # the literal string `arn`.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Textual description of the workflow type.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If set, specifies the default maximum duration of decision tasks for this
    # workflow type. This default can be overridden when starting a workflow
    # execution using the StartWorkflowExecution action or the
    # `StartChildWorkflowExecution` Decision.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    default_task_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If set, specifies the default maximum duration for executions of this
    # workflow type. You can override this default when starting an execution
    # through the StartWorkflowExecution Action or `StartChildWorkflowExecution`
    # Decision.

    # The duration is specified in seconds; an integer greater than or equal to
    # 0. Unlike some of the other timeout parameters in Amazon SWF, you cannot
    # specify a value of "NONE" for `defaultExecutionStartToCloseTimeout`; there
    # is a one-year max limit on the time that a workflow execution can run.
    # Exceeding this limit always causes the workflow execution to time out.
    default_execution_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If set, specifies the default task list to use for scheduling decision
    # tasks for executions of this workflow type. This default is used only if a
    # task list isn't provided when starting the execution through the
    # StartWorkflowExecution Action or `StartChildWorkflowExecution` Decision.
    default_task_list: "TaskList" = dataclasses.field(default_factory=dict, )

    # The default task priority to assign to the workflow type. If not assigned,
    # then `0` is used. Valid values are integers that range from Java's
    # `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647).
    # Higher numbers indicate higher priority.

    # For more information about setting task priority, see [Setting Task
    # Priority](http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-
    # priority.html) in the _Amazon SWF Developer Guide_.
    default_task_priority: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If set, specifies the default policy to use for the child workflow
    # executions when a workflow execution of this type is terminated, by calling
    # the TerminateWorkflowExecution action explicitly or due to an expired
    # timeout. This default can be overridden when starting a workflow execution
    # using the StartWorkflowExecution action or the
    # `StartChildWorkflowExecution` Decision.

    # The supported child policies are:

    #   * `TERMINATE` – The child executions are terminated.

    #   * `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.

    #   * `ABANDON` – No action is taken. The child executions continue to run.
    default_child_policy: "ChildPolicy" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default IAM role attached to this workflow type.

    # Executions of this workflow type need IAM roles to invoke Lambda functions.
    # If you don't specify an IAM role when you start this workflow type, the
    # default Lambda role is attached to the execution. For more information, see
    # <http://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-
    # task.html> in the _Amazon SWF Developer Guide_.
    default_lambda_role: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class RegistrationStatus(Enum):
    REGISTERED = "REGISTERED"
    DEPRECATED = "DEPRECATED"


@dataclasses.dataclass
class RequestCancelActivityTaskDecisionAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `RequestCancelActivityTask` decision.

    **Access Control**

    You can use IAM policies to control this decision's access to Amazon SWF
    resources as follows:

      * Use a `Resource` element with the domain name to limit the action to only specified domains.

      * Use an `Action` element to allow or deny permission to call this action.

      * You cannot use an IAM policy to constrain this action's parameters.

    If the caller doesn't have sufficient permissions to invoke the action, or the
    parameter values fall outside the specified constraints, the action fails. The
    associated event attribute's `cause` parameter is set to
    `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
    to Manage Access to Amazon SWF
    Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
    iam.html) in the _Amazon SWF Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activity_id",
                "activityId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `activityId` of the activity task to be canceled.
    activity_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class RequestCancelActivityTaskFailedCause(Enum):
    ACTIVITY_ID_UNKNOWN = "ACTIVITY_ID_UNKNOWN"
    OPERATION_NOT_PERMITTED = "OPERATION_NOT_PERMITTED"


@dataclasses.dataclass
class RequestCancelActivityTaskFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `RequestCancelActivityTaskFailed` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activity_id",
                "activityId",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(RequestCancelActivityTaskFailedCause),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The activityId provided in the `RequestCancelActivityTask` decision that
    # failed.
    activity_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The cause of the failure. This information is generated by the system and
    # can be useful for diagnostic purposes.

    # If `cause` is set to `OPERATION_NOT_PERMITTED`, the decision failed because
    # it lacked sufficient permissions. For details and example IAM policies, see
    # [Using IAM to Manage Access to Amazon SWF
    # Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-
    # dev-iam.html) in the _Amazon SWF Developer Guide_.
    cause: "RequestCancelActivityTaskFailedCause" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `RequestCancelActivityTask` decision for this
    # cancellation request. This information can be useful for diagnosing
    # problems by tracing back the chain of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RequestCancelExternalWorkflowExecutionDecisionAttributes(
    autoboto.ShapeBase
):
    """
    Provides the details of the `RequestCancelExternalWorkflowExecution` decision.

    **Access Control**

    You can use IAM policies to control this decision's access to Amazon SWF
    resources as follows:

      * Use a `Resource` element with the domain name to limit the action to only specified domains.

      * Use an `Action` element to allow or deny permission to call this action.

      * You cannot use an IAM policy to constrain this action's parameters.

    If the caller doesn't have sufficient permissions to invoke the action, or the
    parameter values fall outside the specified constraints, the action fails. The
    associated event attribute's `cause` parameter is set to
    `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
    to Manage Access to Amazon SWF
    Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
    iam.html) in the _Amazon SWF Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_id",
                "workflowId",
                autoboto.TypeInfo(str),
            ),
            (
                "run_id",
                "runId",
                autoboto.TypeInfo(str),
            ),
            (
                "control",
                "control",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `workflowId` of the external workflow execution to cancel.
    workflow_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The `runId` of the external workflow execution to cancel.
    run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The data attached to the event that can be used by the decider in
    # subsequent workflow tasks.
    control: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class RequestCancelExternalWorkflowExecutionFailedCause(Enum):
    UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION = "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION"
    REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED = "REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED"
    OPERATION_NOT_PERMITTED = "OPERATION_NOT_PERMITTED"


@dataclasses.dataclass
class RequestCancelExternalWorkflowExecutionFailedEventAttributes(
    autoboto.ShapeBase
):
    """
    Provides the details of the `RequestCancelExternalWorkflowExecutionFailed`
    event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_id",
                "workflowId",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.
                TypeInfo(RequestCancelExternalWorkflowExecutionFailedCause),
            ),
            (
                "initiated_event_id",
                "initiatedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "run_id",
                "runId",
                autoboto.TypeInfo(str),
            ),
            (
                "control",
                "control",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `workflowId` of the external workflow to which the cancel request was
    # to be delivered.
    workflow_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The cause of the failure. This information is generated by the system and
    # can be useful for diagnostic purposes.

    # If `cause` is set to `OPERATION_NOT_PERMITTED`, the decision failed because
    # it lacked sufficient permissions. For details and example IAM policies, see
    # [Using IAM to Manage Access to Amazon SWF
    # Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-
    # dev-iam.html) in the _Amazon SWF Developer Guide_.
    cause: "RequestCancelExternalWorkflowExecutionFailedCause" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `RequestCancelExternalWorkflowExecutionInitiated` event
    # corresponding to the `RequestCancelExternalWorkflowExecution` decision to
    # cancel this external workflow execution. This information can be useful for
    # diagnosing problems by tracing back the chain of events leading up to this
    # event.
    initiated_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `RequestCancelExternalWorkflowExecution` decision
    # for this cancellation request. This information can be useful for
    # diagnosing problems by tracing back the chain of events leading up to this
    # event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The `runId` of the external workflow execution.
    run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The data attached to the event that the decider can use in subsequent
    # workflow tasks. This data isn't sent to the workflow execution.
    control: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RequestCancelExternalWorkflowExecutionInitiatedEventAttributes(
    autoboto.ShapeBase
):
    """
    Provides the details of the `RequestCancelExternalWorkflowExecutionInitiated`
    event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_id",
                "workflowId",
                autoboto.TypeInfo(str),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "run_id",
                "runId",
                autoboto.TypeInfo(str),
            ),
            (
                "control",
                "control",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `workflowId` of the external workflow execution to be canceled.
    workflow_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `RequestCancelExternalWorkflowExecution` decision
    # for this cancellation request. This information can be useful for
    # diagnosing problems by tracing back the chain of events leading up to this
    # event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The `runId` of the external workflow execution to be canceled.
    run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Data attached to the event that can be used by the decider in subsequent
    # workflow tasks.
    control: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RequestCancelWorkflowExecutionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "workflow_id",
                "workflowId",
                autoboto.TypeInfo(str),
            ),
            (
                "run_id",
                "runId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the domain containing the workflow execution to cancel.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The workflowId of the workflow execution to cancel.
    workflow_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The runId of the workflow execution to cancel.
    run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RespondActivityTaskCanceledInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_token",
                "taskToken",
                autoboto.TypeInfo(str),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `taskToken` of the ActivityTask.

    # `taskToken` is generated by the service and should be treated as an opaque
    # value. If the task is passed to another process, its `taskToken` must also
    # be passed. This enables it to provide its progress and respond with
    # results.
    task_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information about the cancellation.
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RespondActivityTaskCompletedInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_token",
                "taskToken",
                autoboto.TypeInfo(str),
            ),
            (
                "result",
                "result",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `taskToken` of the ActivityTask.

    # `taskToken` is generated by the service and should be treated as an opaque
    # value. If the task is passed to another process, its `taskToken` must also
    # be passed. This enables it to provide its progress and respond with
    # results.
    task_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The result of the activity task. It is a free form string that is
    # implementation specific.
    result: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RespondActivityTaskFailedInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_token",
                "taskToken",
                autoboto.TypeInfo(str),
            ),
            (
                "reason",
                "reason",
                autoboto.TypeInfo(str),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `taskToken` of the ActivityTask.

    # `taskToken` is generated by the service and should be treated as an opaque
    # value. If the task is passed to another process, its `taskToken` must also
    # be passed. This enables it to provide its progress and respond with
    # results.
    task_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Description of the error that may assist in diagnostics.
    reason: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Detailed information about the failure.
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RespondDecisionTaskCompletedInput(autoboto.ShapeBase):
    """
    Input data for a TaskCompleted response to a decision task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_token",
                "taskToken",
                autoboto.TypeInfo(str),
            ),
            (
                "decisions",
                "decisions",
                autoboto.TypeInfo(typing.List[Decision]),
            ),
            (
                "execution_context",
                "executionContext",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `taskToken` from the DecisionTask.

    # `taskToken` is generated by the service and should be treated as an opaque
    # value. If the task is passed to another process, its `taskToken` must also
    # be passed. This enables it to provide its progress and respond with
    # results.
    task_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The list of decisions (possibly empty) made by the decider while processing
    # this decision task. See the docs for the Decision structure for details.
    decisions: typing.List["Decision"] = dataclasses.field(
        default_factory=list,
    )

    # User defined context to add to workflow execution.
    execution_context: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Run(autoboto.ShapeBase):
    """
    Specifies the `runId` of a workflow execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "run_id",
                "runId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `runId` of a workflow execution. This ID is generated by the service
    # and can be used to uniquely identify the workflow execution within a
    # domain.
    run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ScheduleActivityTaskDecisionAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ScheduleActivityTask` decision.

    **Access Control**

    You can use IAM policies to control this decision's access to Amazon SWF
    resources as follows:

      * Use a `Resource` element with the domain name to limit the action to only specified domains.

      * Use an `Action` element to allow or deny permission to call this action.

      * Constrain the following parameters by using a `Condition` element with the appropriate keys.

        * `activityType.name` – String constraint. The key is `swf:activityType.name`.

        * `activityType.version` – String constraint. The key is `swf:activityType.version`.

        * `taskList` – String constraint. The key is `swf:taskList.name`.

    If the caller doesn't have sufficient permissions to invoke the action, or the
    parameter values fall outside the specified constraints, the action fails. The
    associated event attribute's `cause` parameter is set to
    `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
    to Manage Access to Amazon SWF
    Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
    iam.html) in the _Amazon SWF Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activity_type",
                "activityType",
                autoboto.TypeInfo(ActivityType),
            ),
            (
                "activity_id",
                "activityId",
                autoboto.TypeInfo(str),
            ),
            (
                "control",
                "control",
                autoboto.TypeInfo(str),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule_to_close_timeout",
                "scheduleToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "task_list",
                "taskList",
                autoboto.TypeInfo(TaskList),
            ),
            (
                "task_priority",
                "taskPriority",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule_to_start_timeout",
                "scheduleToStartTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "start_to_close_timeout",
                "startToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "heartbeat_timeout",
                "heartbeatTimeout",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of the activity task to schedule.
    activity_type: "ActivityType" = dataclasses.field(default_factory=dict, )

    # The `activityId` of the activity task.

    # The specified string must not start or end with whitespace. It must not
    # contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control
    # characters (`\u0000-\u001f` | `\u007f-\u009f`). Also, it must not contain
    # the literal string `arn`.
    activity_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Data attached to the event that can be used by the decider in subsequent
    # workflow tasks. This data isn't sent to the activity.
    control: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The input provided to the activity task.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum duration for this activity task.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.

    # A schedule-to-close timeout for this activity task must be specified either
    # as a default for the activity type or through this field. If neither this
    # field is set nor a default schedule-to-close timeout was specified at
    # registration time then a fault is returned.
    schedule_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If set, specifies the name of the task list in which to schedule the
    # activity task. If not specified, the `defaultTaskList` registered with the
    # activity type is used.

    # A task list for this activity task must be specified either as a default
    # for the activity type or through this field. If neither this field is set
    # nor a default task list was specified at registration time then a fault is
    # returned.

    # The specified string must not start or end with whitespace. It must not
    # contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control
    # characters (`\u0000-\u001f` | `\u007f-\u009f`). Also, it must not contain
    # the literal string `arn`.
    task_list: "TaskList" = dataclasses.field(default_factory=dict, )

    # If set, specifies the priority with which the activity task is to be
    # assigned to a worker. This overrides the defaultTaskPriority specified when
    # registering the activity type using RegisterActivityType. Valid values are
    # integers that range from Java's `Integer.MIN_VALUE` (-2147483648) to
    # `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.

    # For more information about setting task priority, see [Setting Task
    # Priority](http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-
    # priority.html) in the _Amazon SWF Developer Guide_.
    task_priority: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If set, specifies the maximum duration the activity task can wait to be
    # assigned to a worker. This overrides the default schedule-to-start timeout
    # specified when registering the activity type using RegisterActivityType.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.

    # A schedule-to-start timeout for this activity task must be specified either
    # as a default for the activity type or through this field. If neither this
    # field is set nor a default schedule-to-start timeout was specified at
    # registration time then a fault is returned.
    schedule_to_start_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If set, specifies the maximum duration a worker may take to process this
    # activity task. This overrides the default start-to-close timeout specified
    # when registering the activity type using RegisterActivityType.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.

    # A start-to-close timeout for this activity task must be specified either as
    # a default for the activity type or through this field. If neither this
    # field is set nor a default start-to-close timeout was specified at
    # registration time then a fault is returned.
    start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If set, specifies the maximum time before which a worker processing a task
    # of this type must report progress by calling RecordActivityTaskHeartbeat.
    # If the timeout is exceeded, the activity task is automatically timed out.
    # If the worker subsequently attempts to record a heartbeat or returns a
    # result, it is ignored. This overrides the default heartbeat timeout
    # specified when registering the activity type using RegisterActivityType.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    heartbeat_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class ScheduleActivityTaskFailedCause(Enum):
    ACTIVITY_TYPE_DEPRECATED = "ACTIVITY_TYPE_DEPRECATED"
    ACTIVITY_TYPE_DOES_NOT_EXIST = "ACTIVITY_TYPE_DOES_NOT_EXIST"
    ACTIVITY_ID_ALREADY_IN_USE = "ACTIVITY_ID_ALREADY_IN_USE"
    OPEN_ACTIVITIES_LIMIT_EXCEEDED = "OPEN_ACTIVITIES_LIMIT_EXCEEDED"
    ACTIVITY_CREATION_RATE_EXCEEDED = "ACTIVITY_CREATION_RATE_EXCEEDED"
    DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED = "DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED"
    DEFAULT_TASK_LIST_UNDEFINED = "DEFAULT_TASK_LIST_UNDEFINED"
    DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED = "DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED"
    DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED = "DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED"
    DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED = "DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED"
    OPERATION_NOT_PERMITTED = "OPERATION_NOT_PERMITTED"


@dataclasses.dataclass
class ScheduleActivityTaskFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ScheduleActivityTaskFailed` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activity_type",
                "activityType",
                autoboto.TypeInfo(ActivityType),
            ),
            (
                "activity_id",
                "activityId",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(ScheduleActivityTaskFailedCause),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The activity type provided in the `ScheduleActivityTask` decision that
    # failed.
    activity_type: "ActivityType" = dataclasses.field(default_factory=dict, )

    # The activityId provided in the `ScheduleActivityTask` decision that failed.
    activity_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The cause of the failure. This information is generated by the system and
    # can be useful for diagnostic purposes.

    # If `cause` is set to `OPERATION_NOT_PERMITTED`, the decision failed because
    # it lacked sufficient permissions. For details and example IAM policies, see
    # [Using IAM to Manage Access to Amazon SWF
    # Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-
    # dev-iam.html) in the _Amazon SWF Developer Guide_.
    cause: "ScheduleActivityTaskFailedCause" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # that resulted in the scheduling of this activity task. This information can
    # be useful for diagnosing problems by tracing back the chain of events
    # leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ScheduleLambdaFunctionDecisionAttributes(autoboto.ShapeBase):
    """
    Decision attributes specified in `scheduleLambdaFunctionDecisionAttributes`
    within the list of decisions `decisions` passed to RespondDecisionTaskCompleted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "control",
                "control",
                autoboto.TypeInfo(str),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
            (
                "start_to_close_timeout",
                "startToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
        ]

    # A string that identifies the Lambda function execution in the event
    # history.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name, or ARN, of the Lambda function to schedule.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The data attached to the event that the decider can use in subsequent
    # workflow tasks. This data isn't sent to the Lambda task.
    control: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The optional input data to be supplied to the Lambda function.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The timeout value, in seconds, after which the Lambda function is
    # considered to be failed once it has started. This can be any integer from
    # 1-300 (1s-5m). If no value is supplied, than a default value of 300s is
    # assumed.
    start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class ScheduleLambdaFunctionFailedCause(Enum):
    ID_ALREADY_IN_USE = "ID_ALREADY_IN_USE"
    OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED = "OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED"
    LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED = "LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED"
    LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION = "LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION"


@dataclasses.dataclass
class ScheduleLambdaFunctionFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `ScheduleLambdaFunctionFailed` event. It isn't set
    for other event types.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(ScheduleLambdaFunctionFailedCause),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID provided in the `ScheduleLambdaFunction` decision that failed.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the Lambda function.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The cause of the failure. To help diagnose issues, use this information to
    # trace back the chain of events leading up to this event.

    # If `cause` is set to `OPERATION_NOT_PERMITTED`, the decision failed because
    # it lacked sufficient permissions. For details and example IAM policies, see
    # [Using IAM to Manage Access to Amazon SWF
    # Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-
    # dev-iam.html) in the _Amazon SWF Developer Guide_.
    cause: "ScheduleLambdaFunctionFailedCause" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `LambdaFunctionCompleted` event corresponding to the decision
    # that resulted in scheduling this Lambda task. To help diagnose issues, use
    # this information to trace back the chain of events leading up to this
    # event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SignalExternalWorkflowExecutionDecisionAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `SignalExternalWorkflowExecution` decision.

    **Access Control**

    You can use IAM policies to control this decision's access to Amazon SWF
    resources as follows:

      * Use a `Resource` element with the domain name to limit the action to only specified domains.

      * Use an `Action` element to allow or deny permission to call this action.

      * You cannot use an IAM policy to constrain this action's parameters.

    If the caller doesn't have sufficient permissions to invoke the action, or the
    parameter values fall outside the specified constraints, the action fails. The
    associated event attribute's `cause` parameter is set to
    `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
    to Manage Access to Amazon SWF
    Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
    iam.html) in the _Amazon SWF Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_id",
                "workflowId",
                autoboto.TypeInfo(str),
            ),
            (
                "signal_name",
                "signalName",
                autoboto.TypeInfo(str),
            ),
            (
                "run_id",
                "runId",
                autoboto.TypeInfo(str),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
            (
                "control",
                "control",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `workflowId` of the workflow execution to be signaled.
    workflow_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the signal.The target workflow execution uses the signal name
    # and input to process the signal.
    signal_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The `runId` of the workflow execution to be signaled.
    run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The input data to be provided with the signal. The target workflow
    # execution uses the signal name and input data to process the signal.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The data attached to the event that can be used by the decider in
    # subsequent decision tasks.
    control: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class SignalExternalWorkflowExecutionFailedCause(Enum):
    UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION = "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION"
    SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED = "SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED"
    OPERATION_NOT_PERMITTED = "OPERATION_NOT_PERMITTED"


@dataclasses.dataclass
class SignalExternalWorkflowExecutionFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `SignalExternalWorkflowExecutionFailed` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_id",
                "workflowId",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(SignalExternalWorkflowExecutionFailedCause),
            ),
            (
                "initiated_event_id",
                "initiatedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "run_id",
                "runId",
                autoboto.TypeInfo(str),
            ),
            (
                "control",
                "control",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `workflowId` of the external workflow execution that the signal was
    # being delivered to.
    workflow_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The cause of the failure. This information is generated by the system and
    # can be useful for diagnostic purposes.

    # If `cause` is set to `OPERATION_NOT_PERMITTED`, the decision failed because
    # it lacked sufficient permissions. For details and example IAM policies, see
    # [Using IAM to Manage Access to Amazon SWF
    # Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-
    # dev-iam.html) in the _Amazon SWF Developer Guide_.
    cause: "SignalExternalWorkflowExecutionFailedCause" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `SignalExternalWorkflowExecutionInitiated` event
    # corresponding to the `SignalExternalWorkflowExecution` decision to request
    # this signal. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    initiated_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `SignalExternalWorkflowExecution` decision for
    # this signal. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The `runId` of the external workflow execution that the signal was being
    # delivered to.
    run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The data attached to the event that the decider can use in subsequent
    # workflow tasks. This data isn't sent to the workflow execution.
    control: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SignalExternalWorkflowExecutionInitiatedEventAttributes(
    autoboto.ShapeBase
):
    """
    Provides the details of the `SignalExternalWorkflowExecutionInitiated` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_id",
                "workflowId",
                autoboto.TypeInfo(str),
            ),
            (
                "signal_name",
                "signalName",
                autoboto.TypeInfo(str),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "run_id",
                "runId",
                autoboto.TypeInfo(str),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
            (
                "control",
                "control",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `workflowId` of the external workflow execution.
    workflow_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the signal.
    signal_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `SignalExternalWorkflowExecution` decision for
    # this signal. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The `runId` of the external workflow execution to send the signal to.
    run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The input provided to the signal.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Data attached to the event that can be used by the decider in subsequent
    # decision tasks.
    control: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SignalWorkflowExecutionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "workflow_id",
                "workflowId",
                autoboto.TypeInfo(str),
            ),
            (
                "signal_name",
                "signalName",
                autoboto.TypeInfo(str),
            ),
            (
                "run_id",
                "runId",
                autoboto.TypeInfo(str),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the domain containing the workflow execution to signal.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The workflowId of the workflow execution to signal.
    workflow_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the signal. This name must be meaningful to the target
    # workflow.
    signal_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The runId of the workflow execution to signal.
    run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Data to attach to the `WorkflowExecutionSignaled` event in the target
    # workflow execution's history.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StartChildWorkflowExecutionDecisionAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `StartChildWorkflowExecution` decision.

    **Access Control**

    You can use IAM policies to control this decision's access to Amazon SWF
    resources as follows:

      * Use a `Resource` element with the domain name to limit the action to only specified domains.

      * Use an `Action` element to allow or deny permission to call this action.

      * Constrain the following parameters by using a `Condition` element with the appropriate keys.

        * `tagList.member.N` – The key is "swf:tagList.N" where N is the tag number from 0 to 4, inclusive.

        * `taskList` – String constraint. The key is `swf:taskList.name`.

        * `workflowType.name` – String constraint. The key is `swf:workflowType.name`.

        * `workflowType.version` – String constraint. The key is `swf:workflowType.version`.

    If the caller doesn't have sufficient permissions to invoke the action, or the
    parameter values fall outside the specified constraints, the action fails. The
    associated event attribute's `cause` parameter is set to
    `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
    to Manage Access to Amazon SWF
    Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
    iam.html) in the _Amazon SWF Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
            (
                "workflow_id",
                "workflowId",
                autoboto.TypeInfo(str),
            ),
            (
                "control",
                "control",
                autoboto.TypeInfo(str),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_start_to_close_timeout",
                "executionStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "task_list",
                "taskList",
                autoboto.TypeInfo(TaskList),
            ),
            (
                "task_priority",
                "taskPriority",
                autoboto.TypeInfo(str),
            ),
            (
                "task_start_to_close_timeout",
                "taskStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "child_policy",
                "childPolicy",
                autoboto.TypeInfo(ChildPolicy),
            ),
            (
                "tag_list",
                "tagList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "lambda_role",
                "lambdaRole",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of the workflow execution to be started.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )

    # The `workflowId` of the workflow execution.

    # The specified string must not start or end with whitespace. It must not
    # contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control
    # characters (`\u0000-\u001f` | `\u007f-\u009f`). Also, it must not contain
    # the literal string `arn`.
    workflow_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The data attached to the event that can be used by the decider in
    # subsequent workflow tasks. This data isn't sent to the child workflow
    # execution.
    control: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The input to be provided to the workflow execution.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The total duration for this workflow execution. This overrides the
    # defaultExecutionStartToCloseTimeout specified when registering the workflow
    # type.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.

    # An execution start-to-close timeout for this workflow execution must be
    # specified either as a default for the workflow type or through this
    # parameter. If neither this parameter is set nor a default execution start-
    # to-close timeout was specified at registration time then a fault is
    # returned.
    execution_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the task list to be used for decision tasks of the child
    # workflow execution.

    # A task list for this workflow execution must be specified either as a
    # default for the workflow type or through this parameter. If neither this
    # parameter is set nor a default task list was specified at registration time
    # then a fault is returned.

    # The specified string must not start or end with whitespace. It must not
    # contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control
    # characters (`\u0000-\u001f` | `\u007f-\u009f`). Also, it must not contain
    # the literal string `arn`.
    task_list: "TaskList" = dataclasses.field(default_factory=dict, )

    # A task priority that, if set, specifies the priority for a decision task of
    # this workflow execution. This overrides the defaultTaskPriority specified
    # when registering the workflow type. Valid values are integers that range
    # from Java's `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE`
    # (2147483647). Higher numbers indicate higher priority.

    # For more information about setting task priority, see [Setting Task
    # Priority](http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-
    # priority.html) in the _Amazon SWF Developer Guide_.
    task_priority: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the maximum duration of decision tasks for this workflow
    # execution. This parameter overrides the `defaultTaskStartToCloseTimout`
    # specified when registering the workflow type using RegisterWorkflowType.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.

    # A task start-to-close timeout for this workflow execution must be specified
    # either as a default for the workflow type or through this parameter. If
    # neither this parameter is set nor a default task start-to-close timeout was
    # specified at registration time then a fault is returned.
    task_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If set, specifies the policy to use for the child workflow executions if
    # the workflow execution being started is terminated by calling the
    # TerminateWorkflowExecution action explicitly or due to an expired timeout.
    # This policy overrides the default child policy specified when registering
    # the workflow type using RegisterWorkflowType.

    # The supported child policies are:

    #   * `TERMINATE` – The child executions are terminated.

    #   * `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.

    #   * `ABANDON` – No action is taken. The child executions continue to run.

    # A child policy for this workflow execution must be specified either as a
    # default for the workflow type or through this parameter. If neither this
    # parameter is set nor a default child policy was specified at registration
    # time then a fault is returned.
    child_policy: "ChildPolicy" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The list of tags to associate with the child workflow execution. A maximum
    # of 5 tags can be specified. You can list workflow executions with a
    # specific tag by calling ListOpenWorkflowExecutions or
    # ListClosedWorkflowExecutions and specifying a TagFilter.
    tag_list: typing.List[str] = dataclasses.field(default_factory=list, )

    # The IAM role attached to the child workflow execution.
    lambda_role: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class StartChildWorkflowExecutionFailedCause(Enum):
    WORKFLOW_TYPE_DOES_NOT_EXIST = "WORKFLOW_TYPE_DOES_NOT_EXIST"
    WORKFLOW_TYPE_DEPRECATED = "WORKFLOW_TYPE_DEPRECATED"
    OPEN_CHILDREN_LIMIT_EXCEEDED = "OPEN_CHILDREN_LIMIT_EXCEEDED"
    OPEN_WORKFLOWS_LIMIT_EXCEEDED = "OPEN_WORKFLOWS_LIMIT_EXCEEDED"
    CHILD_CREATION_RATE_EXCEEDED = "CHILD_CREATION_RATE_EXCEEDED"
    WORKFLOW_ALREADY_RUNNING = "WORKFLOW_ALREADY_RUNNING"
    DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED = "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED"
    DEFAULT_TASK_LIST_UNDEFINED = "DEFAULT_TASK_LIST_UNDEFINED"
    DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED = "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED"
    DEFAULT_CHILD_POLICY_UNDEFINED = "DEFAULT_CHILD_POLICY_UNDEFINED"
    OPERATION_NOT_PERMITTED = "OPERATION_NOT_PERMITTED"


@dataclasses.dataclass
class StartChildWorkflowExecutionFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `StartChildWorkflowExecutionFailed` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(StartChildWorkflowExecutionFailedCause),
            ),
            (
                "workflow_id",
                "workflowId",
                autoboto.TypeInfo(str),
            ),
            (
                "initiated_event_id",
                "initiatedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "control",
                "control",
                autoboto.TypeInfo(str),
            ),
        ]

    # The workflow type provided in the `StartChildWorkflowExecution` Decision
    # that failed.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )

    # The cause of the failure. This information is generated by the system and
    # can be useful for diagnostic purposes.

    # When `cause` is set to `OPERATION_NOT_PERMITTED`, the decision fails
    # because it lacks sufficient permissions. For details and example IAM
    # policies, see [ Using IAM to Manage Access to Amazon SWF
    # Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-
    # dev-iam.html) in the _Amazon SWF Developer Guide_.
    cause: "StartChildWorkflowExecutionFailedCause" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The `workflowId` of the child workflow execution.
    workflow_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # When the `cause` is `WORKFLOW_ALREADY_RUNNING`, `initiatedEventId` is the
    # ID of the `StartChildWorkflowExecutionInitiated` event that corresponds to
    # the `StartChildWorkflowExecution` Decision to start the workflow execution.
    # You can use this information to diagnose problems by tracing back the chain
    # of events leading up to this event.

    # When the `cause` isn't `WORKFLOW_ALREADY_RUNNING`, `initiatedEventId` is
    # set to `0` because the `StartChildWorkflowExecutionInitiated` event doesn't
    # exist.
    initiated_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `StartChildWorkflowExecution` Decision to request
    # this child workflow execution. This information can be useful for
    # diagnosing problems by tracing back the chain of events.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The data attached to the event that the decider can use in subsequent
    # workflow tasks. This data isn't sent to the child workflow execution.
    control: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StartChildWorkflowExecutionInitiatedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `StartChildWorkflowExecutionInitiated` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_id",
                "workflowId",
                autoboto.TypeInfo(str),
            ),
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
            (
                "task_list",
                "taskList",
                autoboto.TypeInfo(TaskList),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "child_policy",
                "childPolicy",
                autoboto.TypeInfo(ChildPolicy),
            ),
            (
                "control",
                "control",
                autoboto.TypeInfo(str),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_start_to_close_timeout",
                "executionStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "task_priority",
                "taskPriority",
                autoboto.TypeInfo(str),
            ),
            (
                "task_start_to_close_timeout",
                "taskStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_list",
                "tagList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "lambda_role",
                "lambdaRole",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `workflowId` of the child workflow execution.
    workflow_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of the child workflow execution.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )

    # The name of the task list used for the decision tasks of the child workflow
    # execution.
    task_list: "TaskList" = dataclasses.field(default_factory=dict, )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `StartChildWorkflowExecution` Decision to request
    # this child workflow execution. This information can be useful for
    # diagnosing problems by tracing back the cause of events.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The policy to use for the child workflow executions if this execution gets
    # terminated by explicitly calling the TerminateWorkflowExecution action or
    # due to an expired timeout.

    # The supported child policies are:

    #   * `TERMINATE` – The child executions are terminated.

    #   * `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.

    #   * `ABANDON` – No action is taken. The child executions continue to run.
    child_policy: "ChildPolicy" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Data attached to the event that can be used by the decider in subsequent
    # decision tasks. This data isn't sent to the activity.
    control: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The inputs provided to the child workflow execution.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum duration for the child workflow execution. If the workflow
    # execution isn't closed within this duration, it is timed out and force-
    # terminated.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    execution_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The priority assigned for the decision tasks for this workflow execution.
    # Valid values are integers that range from Java's `Integer.MIN_VALUE`
    # (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate
    # higher priority.

    # For more information about setting task priority, see [Setting Task
    # Priority](http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-
    # priority.html) in the _Amazon SWF Developer Guide_.
    task_priority: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum duration allowed for the decision tasks for this workflow
    # execution.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    task_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The list of tags to associated with the child workflow execution.
    tag_list: typing.List[str] = dataclasses.field(default_factory=list, )

    # The IAM role to attach to the child workflow execution.
    lambda_role: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class StartLambdaFunctionFailedCause(Enum):
    ASSUME_ROLE_FAILED = "ASSUME_ROLE_FAILED"


@dataclasses.dataclass
class StartLambdaFunctionFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `StartLambdaFunctionFailed` event. It isn't set for
    other event types.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_event_id",
                "scheduledEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(StartLambdaFunctionFailedCause),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the `ActivityTaskScheduled` event that was recorded when this
    # activity task was scheduled. To help diagnose issues, use this information
    # to trace back the chain of events leading up to this event.
    scheduled_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The cause of the failure. To help diagnose issues, use this information to
    # trace back the chain of events leading up to this event.

    # If `cause` is set to `OPERATION_NOT_PERMITTED`, the decision failed because
    # the IAM role attached to the execution lacked sufficient permissions. For
    # details and example IAM policies, see [Lambda
    # Tasks](http://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-
    # task.html) in the _Amazon SWF Developer Guide_.
    cause: "StartLambdaFunctionFailedCause" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description that can help diagnose the cause of the fault.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StartTimerDecisionAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `StartTimer` decision.

    **Access Control**

    You can use IAM policies to control this decision's access to Amazon SWF
    resources as follows:

      * Use a `Resource` element with the domain name to limit the action to only specified domains.

      * Use an `Action` element to allow or deny permission to call this action.

      * You cannot use an IAM policy to constrain this action's parameters.

    If the caller doesn't have sufficient permissions to invoke the action, or the
    parameter values fall outside the specified constraints, the action fails. The
    associated event attribute's `cause` parameter is set to
    `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM
    to Manage Access to Amazon SWF
    Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-
    iam.html) in the _Amazon SWF Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timer_id",
                "timerId",
                autoboto.TypeInfo(str),
            ),
            (
                "start_to_fire_timeout",
                "startToFireTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "control",
                "control",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the timer.

    # The specified string must not start or end with whitespace. It must not
    # contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control
    # characters (`\u0000-\u001f` | `\u007f-\u009f`). Also, it must not contain
    # the literal string `arn`.
    timer_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The duration to wait before firing the timer.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`.
    start_to_fire_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The data attached to the event that can be used by the decider in
    # subsequent workflow tasks.
    control: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class StartTimerFailedCause(Enum):
    TIMER_ID_ALREADY_IN_USE = "TIMER_ID_ALREADY_IN_USE"
    OPEN_TIMERS_LIMIT_EXCEEDED = "OPEN_TIMERS_LIMIT_EXCEEDED"
    TIMER_CREATION_RATE_EXCEEDED = "TIMER_CREATION_RATE_EXCEEDED"
    OPERATION_NOT_PERMITTED = "OPERATION_NOT_PERMITTED"


@dataclasses.dataclass
class StartTimerFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `StartTimerFailed` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timer_id",
                "timerId",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(StartTimerFailedCause),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The timerId provided in the `StartTimer` decision that failed.
    timer_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The cause of the failure. This information is generated by the system and
    # can be useful for diagnostic purposes.

    # If `cause` is set to `OPERATION_NOT_PERMITTED`, the decision failed because
    # it lacked sufficient permissions. For details and example IAM policies, see
    # [Using IAM to Manage Access to Amazon SWF
    # Workflows](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-
    # dev-iam.html) in the _Amazon SWF Developer Guide_.
    cause: "StartTimerFailedCause" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `StartTimer` decision for this activity task.
    # This information can be useful for diagnosing problems by tracing back the
    # chain of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class StartWorkflowExecutionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "workflow_id",
                "workflowId",
                autoboto.TypeInfo(str),
            ),
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
            (
                "task_list",
                "taskList",
                autoboto.TypeInfo(TaskList),
            ),
            (
                "task_priority",
                "taskPriority",
                autoboto.TypeInfo(str),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_start_to_close_timeout",
                "executionStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_list",
                "tagList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "task_start_to_close_timeout",
                "taskStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "child_policy",
                "childPolicy",
                autoboto.TypeInfo(ChildPolicy),
            ),
            (
                "lambda_role",
                "lambdaRole",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the domain in which the workflow execution is created.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user defined identifier associated with the workflow execution. You can
    # use this to associate a custom identifier with the workflow execution. You
    # may specify the same identifier if a workflow execution is logically a
    # _restart_ of a previous execution. You cannot have two open workflow
    # executions with the same `workflowId` at the same time.

    # The specified string must not start or end with whitespace. It must not
    # contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control
    # characters (`\u0000-\u001f` | `\u007f-\u009f`). Also, it must not contain
    # the literal string `arn`.
    workflow_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of the workflow to start.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )

    # The task list to use for the decision tasks generated for this workflow
    # execution. This overrides the `defaultTaskList` specified when registering
    # the workflow type.

    # A task list for this workflow execution must be specified either as a
    # default for the workflow type or through this parameter. If neither this
    # parameter is set nor a default task list was specified at registration time
    # then a fault is returned.

    # The specified string must not start or end with whitespace. It must not
    # contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control
    # characters (`\u0000-\u001f` | `\u007f-\u009f`). Also, it must not contain
    # the literal string `arn`.
    task_list: "TaskList" = dataclasses.field(default_factory=dict, )

    # The task priority to use for this workflow execution. This overrides any
    # default priority that was assigned when the workflow type was registered.
    # If not set, then the default task priority for the workflow type is used.
    # Valid values are integers that range from Java's `Integer.MIN_VALUE`
    # (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate
    # higher priority.

    # For more information about setting task priority, see [Setting Task
    # Priority](http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-
    # priority.html) in the _Amazon SWF Developer Guide_.
    task_priority: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The input for the workflow execution. This is a free form string which
    # should be meaningful to the workflow you are starting. This `input` is made
    # available to the new workflow execution in the `WorkflowExecutionStarted`
    # history event.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The total duration for this workflow execution. This overrides the
    # defaultExecutionStartToCloseTimeout specified when registering the workflow
    # type.

    # The duration is specified in seconds; an integer greater than or equal to
    # `0`. Exceeding this limit causes the workflow execution to time out. Unlike
    # some of the other timeout parameters in Amazon SWF, you cannot specify a
    # value of "NONE" for this timeout; there is a one-year max limit on the time
    # that a workflow execution can run.

    # An execution start-to-close timeout must be specified either through this
    # parameter or as a default when the workflow type is registered. If neither
    # this parameter nor a default execution start-to-close timeout is specified,
    # a fault is returned.
    execution_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The list of tags to associate with the workflow execution. You can specify
    # a maximum of 5 tags. You can list workflow executions with a specific tag
    # by calling ListOpenWorkflowExecutions or ListClosedWorkflowExecutions and
    # specifying a TagFilter.
    tag_list: typing.List[str] = dataclasses.field(default_factory=list, )

    # Specifies the maximum duration of decision tasks for this workflow
    # execution. This parameter overrides the `defaultTaskStartToCloseTimout`
    # specified when registering the workflow type using RegisterWorkflowType.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.

    # A task start-to-close timeout for this workflow execution must be specified
    # either as a default for the workflow type or through this parameter. If
    # neither this parameter is set nor a default task start-to-close timeout was
    # specified at registration time then a fault is returned.
    task_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If set, specifies the policy to use for the child workflow executions of
    # this workflow execution if it is terminated, by calling the
    # TerminateWorkflowExecution action explicitly or due to an expired timeout.
    # This policy overrides the default child policy specified when registering
    # the workflow type using RegisterWorkflowType.

    # The supported child policies are:

    #   * `TERMINATE` – The child executions are terminated.

    #   * `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.

    #   * `ABANDON` – No action is taken. The child executions continue to run.

    # A child policy for this workflow execution must be specified either as a
    # default for the workflow type or through this parameter. If neither this
    # parameter is set nor a default child policy was specified at registration
    # time then a fault is returned.
    child_policy: "ChildPolicy" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IAM role to attach to this workflow execution.

    # Executions of this workflow type need IAM roles to invoke Lambda functions.
    # If you don't attach an IAM role, any attempt to schedule a Lambda task
    # fails. This results in a `ScheduleLambdaFunctionFailed` history event. For
    # more information, see
    # <http://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-
    # task.html> in the _Amazon SWF Developer Guide_.
    lambda_role: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TagFilter(autoboto.ShapeBase):
    """
    Used to filter the workflow executions in visibility APIs based on a tag.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag",
                "tag",
                autoboto.TypeInfo(str),
            ),
        ]

    # Specifies the tag that must be associated with the execution for it to meet
    # the filter criteria.
    tag: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TaskList(autoboto.ShapeBase):
    """
    Represents a task list.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the task list.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TerminateWorkflowExecutionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(str),
            ),
            (
                "workflow_id",
                "workflowId",
                autoboto.TypeInfo(str),
            ),
            (
                "run_id",
                "runId",
                autoboto.TypeInfo(str),
            ),
            (
                "reason",
                "reason",
                autoboto.TypeInfo(str),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
            (
                "child_policy",
                "childPolicy",
                autoboto.TypeInfo(ChildPolicy),
            ),
        ]

    # The domain of the workflow execution to terminate.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The workflowId of the workflow execution to terminate.
    workflow_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The runId of the workflow execution to terminate.
    run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A descriptive reason for terminating the workflow execution.
    reason: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Details for terminating the workflow execution.
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If set, specifies the policy to use for the child workflow executions of
    # the workflow execution being terminated. This policy overrides the child
    # policy specified for the workflow execution at registration time or when
    # starting the execution.

    # The supported child policies are:

    #   * `TERMINATE` – The child executions are terminated.

    #   * `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.

    #   * `ABANDON` – No action is taken. The child executions continue to run.

    # A child policy for this workflow execution must be specified either as a
    # default for the workflow type or through this parameter. If neither this
    # parameter is set nor a default child policy was specified at registration
    # time then a fault is returned.
    child_policy: "ChildPolicy" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class TimerCanceledEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `TimerCanceled` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timer_id",
                "timerId",
                autoboto.TypeInfo(str),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique ID of the timer that was canceled.
    timer_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the `TimerStarted` event that was recorded when this timer was
    # started. This information can be useful for diagnosing problems by tracing
    # back the chain of events leading up to this event.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `CancelTimer` decision to cancel this timer. This
    # information can be useful for diagnosing problems by tracing back the chain
    # of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class TimerFiredEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `TimerFired` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timer_id",
                "timerId",
                autoboto.TypeInfo(str),
            ),
            (
                "started_event_id",
                "startedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique ID of the timer that fired.
    timer_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the `TimerStarted` event that was recorded when this timer was
    # started. This information can be useful for diagnosing problems by tracing
    # back the chain of events leading up to this event.
    started_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class TimerStartedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `TimerStarted` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timer_id",
                "timerId",
                autoboto.TypeInfo(str),
            ),
            (
                "start_to_fire_timeout",
                "startToFireTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "control",
                "control",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the timer that was started.
    timer_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The duration of time after which the timer fires.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`.
    start_to_fire_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `StartTimer` decision for this activity task.
    # This information can be useful for diagnosing problems by tracing back the
    # chain of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Data attached to the event that can be used by the decider in subsequent
    # workflow tasks.
    control: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TypeAlreadyExistsFault(autoboto.ShapeBase):
    """
    Returned if the type already exists in the specified domain. You get this fault
    even if the existing type is in deprecated status. You can specify another
    version if the intent is to create a new distinct version of the type.
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

    # A description that may help with diagnosing the cause of the fault.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TypeDeprecatedFault(autoboto.ShapeBase):
    """
    Returned when the specified activity or workflow type was already deprecated.
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

    # A description that may help with diagnosing the cause of the fault.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UnknownResourceFault(autoboto.ShapeBase):
    """
    Returned when the named resource cannot be found with in the scope of this
    operation (region or domain). This could happen if the named resource was never
    created or is no longer available for this operation.
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

    # A description that may help with diagnosing the cause of the fault.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WorkflowExecution(autoboto.ShapeBase):
    """
    Represents a workflow execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_id",
                "workflowId",
                autoboto.TypeInfo(str),
            ),
            (
                "run_id",
                "runId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user defined identifier associated with the workflow execution.
    workflow_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A system-generated unique identifier for the workflow execution.
    run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WorkflowExecutionAlreadyStartedFault(autoboto.ShapeBase):
    """
    Returned by StartWorkflowExecution when an open execution with the same
    workflowId is already running in the specified domain.
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

    # A description that may help with diagnosing the cause of the fault.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class WorkflowExecutionCancelRequestedCause(Enum):
    CHILD_POLICY_APPLIED = "CHILD_POLICY_APPLIED"


@dataclasses.dataclass
class WorkflowExecutionCancelRequestedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `WorkflowExecutionCancelRequested` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "external_workflow_execution",
                "externalWorkflowExecution",
                autoboto.TypeInfo(WorkflowExecution),
            ),
            (
                "external_initiated_event_id",
                "externalInitiatedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(WorkflowExecutionCancelRequestedCause),
            ),
        ]

    # The external workflow execution for which the cancellation was requested.
    external_workflow_execution: "WorkflowExecution" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the `RequestCancelExternalWorkflowExecutionInitiated` event
    # corresponding to the `RequestCancelExternalWorkflowExecution` decision to
    # cancel this workflow execution.The source event with this ID can be found
    # in the history of the source workflow execution. This information can be
    # useful for diagnosing problems by tracing back the chain of events leading
    # up to this event.
    external_initiated_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If set, indicates that the request to cancel the workflow execution was
    # automatically generated, and specifies the cause. This happens if the
    # parent workflow execution times out or is terminated, and the child policy
    # is set to cancel child executions.
    cause: "WorkflowExecutionCancelRequestedCause" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class WorkflowExecutionCanceledEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `WorkflowExecutionCanceled` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `CancelWorkflowExecution` decision for this
    # cancellation request. This information can be useful for diagnosing
    # problems by tracing back the chain of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The details of the cancellation.
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WorkflowExecutionCompletedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `WorkflowExecutionCompleted` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "result",
                "result",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `CompleteWorkflowExecution` decision to complete
    # this execution. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The result produced by the workflow execution upon successful completion.
    result: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WorkflowExecutionConfiguration(autoboto.ShapeBase):
    """
    The configuration settings for a workflow execution including timeout values,
    tasklist etc. These configuration settings are determined from the defaults
    specified when registering the workflow type and those specified when starting
    the workflow execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_start_to_close_timeout",
                "taskStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_start_to_close_timeout",
                "executionStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "task_list",
                "taskList",
                autoboto.TypeInfo(TaskList),
            ),
            (
                "child_policy",
                "childPolicy",
                autoboto.TypeInfo(ChildPolicy),
            ),
            (
                "task_priority",
                "taskPriority",
                autoboto.TypeInfo(str),
            ),
            (
                "lambda_role",
                "lambdaRole",
                autoboto.TypeInfo(str),
            ),
        ]

    # The maximum duration allowed for decision tasks for this workflow
    # execution.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    task_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The total duration for this workflow execution.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    execution_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The task list used for the decision tasks generated for this workflow
    # execution.
    task_list: "TaskList" = dataclasses.field(default_factory=dict, )

    # The policy to use for the child workflow executions if this workflow
    # execution is terminated, by calling the TerminateWorkflowExecution action
    # explicitly or due to an expired timeout.

    # The supported child policies are:

    #   * `TERMINATE` – The child executions are terminated.

    #   * `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.

    #   * `ABANDON` – No action is taken. The child executions continue to run.
    child_policy: "ChildPolicy" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The priority assigned to decision tasks for this workflow execution. Valid
    # values are integers that range from Java's `Integer.MIN_VALUE`
    # (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate
    # higher priority.

    # For more information about setting task priority, see [Setting Task
    # Priority](http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-
    # priority.html) in the _Amazon SWF Developer Guide_.
    task_priority: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IAM role attached to the child workflow execution.
    lambda_role: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WorkflowExecutionContinuedAsNewEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `WorkflowExecutionContinuedAsNew` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "new_execution_run_id",
                "newExecutionRunId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_list",
                "taskList",
                autoboto.TypeInfo(TaskList),
            ),
            (
                "child_policy",
                "childPolicy",
                autoboto.TypeInfo(ChildPolicy),
            ),
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_start_to_close_timeout",
                "executionStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "task_priority",
                "taskPriority",
                autoboto.TypeInfo(str),
            ),
            (
                "task_start_to_close_timeout",
                "taskStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_list",
                "tagList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "lambda_role",
                "lambdaRole",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `ContinueAsNewWorkflowExecution` decision that
    # started this execution. This information can be useful for diagnosing
    # problems by tracing back the chain of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The `runId` of the new workflow execution.
    new_execution_run_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The task list to use for the decisions of the new (continued) workflow
    # execution.
    task_list: "TaskList" = dataclasses.field(default_factory=dict, )

    # The policy to use for the child workflow executions of the new execution if
    # it is terminated by calling the TerminateWorkflowExecution action
    # explicitly or due to an expired timeout.

    # The supported child policies are:

    #   * `TERMINATE` – The child executions are terminated.

    #   * `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.

    #   * `ABANDON` – No action is taken. The child executions continue to run.
    child_policy: "ChildPolicy" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The workflow type of this execution.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )

    # The input provided to the new workflow execution.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The total duration allowed for the new workflow execution.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    execution_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The priority of the task to use for the decisions of the new (continued)
    # workflow execution.
    task_priority: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum duration of decision tasks for the new workflow execution.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    task_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The list of tags associated with the new workflow execution.
    tag_list: typing.List[str] = dataclasses.field(default_factory=list, )

    # The IAM role to attach to the new (continued) workflow execution.
    lambda_role: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WorkflowExecutionCount(autoboto.ShapeBase):
    """
    Contains the count of workflow executions returned from
    CountOpenWorkflowExecutions or CountClosedWorkflowExecutions
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
                "truncated",
                "truncated",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The number of workflow executions.
    count: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If set to true, indicates that the actual count was more than the maximum
    # supported by this API and the count returned is the truncated value.
    truncated: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WorkflowExecutionDetail(autoboto.ShapeBase):
    """
    Contains details about a workflow execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution_info",
                "executionInfo",
                autoboto.TypeInfo(WorkflowExecutionInfo),
            ),
            (
                "execution_configuration",
                "executionConfiguration",
                autoboto.TypeInfo(WorkflowExecutionConfiguration),
            ),
            (
                "open_counts",
                "openCounts",
                autoboto.TypeInfo(WorkflowExecutionOpenCounts),
            ),
            (
                "latest_activity_task_timestamp",
                "latestActivityTaskTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "latest_execution_context",
                "latestExecutionContext",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the workflow execution.
    execution_info: "WorkflowExecutionInfo" = dataclasses.field(
        default_factory=dict,
    )

    # The configuration settings for this workflow execution including timeout
    # values, tasklist etc.
    execution_configuration: "WorkflowExecutionConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The number of tasks for this workflow execution. This includes open and
    # closed tasks of all types.
    open_counts: "WorkflowExecutionOpenCounts" = dataclasses.field(
        default_factory=dict,
    )

    # The time when the last activity task was scheduled for this workflow
    # execution. You can use this information to determine if the workflow has
    # not made progress for an unusually long period of time and might require a
    # corrective action.
    latest_activity_task_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The latest executionContext provided by the decider for this workflow
    # execution. A decider can provide an executionContext (a free-form string)
    # when closing a decision task using RespondDecisionTaskCompleted.
    latest_execution_context: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class WorkflowExecutionFailedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `WorkflowExecutionFailed` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "decision_task_completed_event_id",
                "decisionTaskCompletedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "reason",
                "reason",
                autoboto.TypeInfo(str),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the `DecisionTaskCompleted` event corresponding to the decision
    # task that resulted in the `FailWorkflowExecution` decision to fail this
    # execution. This information can be useful for diagnosing problems by
    # tracing back the chain of events leading up to this event.
    decision_task_completed_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The descriptive reason provided for the failure.
    reason: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The details of the failure.
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WorkflowExecutionFilter(autoboto.ShapeBase):
    """
    Used to filter the workflow executions in visibility APIs by their `workflowId`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_id",
                "workflowId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The workflowId to pass of match the criteria of this filter.
    workflow_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WorkflowExecutionInfo(autoboto.ShapeBase):
    """
    Contains information about a workflow execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution",
                "execution",
                autoboto.TypeInfo(WorkflowExecution),
            ),
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
            (
                "start_timestamp",
                "startTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "execution_status",
                "executionStatus",
                autoboto.TypeInfo(ExecutionStatus),
            ),
            (
                "close_timestamp",
                "closeTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "close_status",
                "closeStatus",
                autoboto.TypeInfo(CloseStatus),
            ),
            (
                "parent",
                "parent",
                autoboto.TypeInfo(WorkflowExecution),
            ),
            (
                "tag_list",
                "tagList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "cancel_requested",
                "cancelRequested",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The workflow execution this information is about.
    execution: "WorkflowExecution" = dataclasses.field(default_factory=dict, )

    # The type of the workflow execution.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )

    # The time when the execution was started.
    start_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The current status of the execution.
    execution_status: "ExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time when the workflow execution was closed. Set only if the execution
    # status is CLOSED.
    close_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the execution status is closed then this specifies how the execution was
    # closed:

    #   * `COMPLETED` – the execution was successfully completed.

    #   * `CANCELED` – the execution was canceled.Cancellation allows the implementation to gracefully clean up before the execution is closed.

    #   * `TERMINATED` – the execution was force terminated.

    #   * `FAILED` – the execution failed to complete.

    #   * `TIMED_OUT` – the execution did not complete in the alloted time and was automatically timed out.

    #   * `CONTINUED_AS_NEW` – the execution is logically continued. This means the current execution was completed and a new execution was started to carry on the workflow.
    close_status: "CloseStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If this workflow execution is a child of another execution then contains
    # the workflow execution that started this execution.
    parent: "WorkflowExecution" = dataclasses.field(default_factory=dict, )

    # The list of tags associated with the workflow execution. Tags can be used
    # to identify and list workflow executions of interest through the visibility
    # APIs. A workflow execution can have a maximum of 5 tags.
    tag_list: typing.List[str] = dataclasses.field(default_factory=list, )

    # Set to true if a cancellation is requested for this workflow execution.
    cancel_requested: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class WorkflowExecutionInfos(autoboto.ShapeBase):
    """
    Contains a paginated list of information about workflow executions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution_infos",
                "executionInfos",
                autoboto.TypeInfo(typing.List[WorkflowExecutionInfo]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of workflow information structures.
    execution_infos: typing.List["WorkflowExecutionInfo"] = dataclasses.field(
        default_factory=list,
    )

    # If a `NextPageToken` was returned by a previous call, there are more
    # results available. To retrieve the next page of results, make the call
    # again using the returned token in `nextPageToken`. Keep all other arguments
    # unchanged.

    # The configured `maximumPageSize` determines how many results can be
    # returned in a single call.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class WorkflowExecutionOpenCounts(autoboto.ShapeBase):
    """
    Contains the counts of open tasks, child workflow executions and timers for a
    workflow execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "open_activity_tasks",
                "openActivityTasks",
                autoboto.TypeInfo(int),
            ),
            (
                "open_decision_tasks",
                "openDecisionTasks",
                autoboto.TypeInfo(int),
            ),
            (
                "open_timers",
                "openTimers",
                autoboto.TypeInfo(int),
            ),
            (
                "open_child_workflow_executions",
                "openChildWorkflowExecutions",
                autoboto.TypeInfo(int),
            ),
            (
                "open_lambda_functions",
                "openLambdaFunctions",
                autoboto.TypeInfo(int),
            ),
        ]

    # The count of activity tasks whose status is `OPEN`.
    open_activity_tasks: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The count of decision tasks whose status is OPEN. A workflow execution can
    # have at most one open decision task.
    open_decision_tasks: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The count of timers started by this workflow execution that have not fired
    # yet.
    open_timers: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The count of child workflow executions whose status is `OPEN`.
    open_child_workflow_executions: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The count of Lambda tasks whose status is `OPEN`.
    open_lambda_functions: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class WorkflowExecutionSignaledEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `WorkflowExecutionSignaled` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "signal_name",
                "signalName",
                autoboto.TypeInfo(str),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
            (
                "external_workflow_execution",
                "externalWorkflowExecution",
                autoboto.TypeInfo(WorkflowExecution),
            ),
            (
                "external_initiated_event_id",
                "externalInitiatedEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the signal received. The decider can use the signal name and
    # inputs to determine how to the process the signal.
    signal_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The inputs provided with the signal. The decider can use the signal name
    # and inputs to determine how to process the signal.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The workflow execution that sent the signal. This is set only of the signal
    # was sent by another workflow execution.
    external_workflow_execution: "WorkflowExecution" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the `SignalExternalWorkflowExecutionInitiated` event
    # corresponding to the `SignalExternalWorkflow` decision to signal this
    # workflow execution.The source event with this ID can be found in the
    # history of the source workflow execution. This information can be useful
    # for diagnosing problems by tracing back the chain of events leading up to
    # this event. This field is set only if the signal was initiated by another
    # workflow execution.
    external_initiated_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class WorkflowExecutionStartedEventAttributes(autoboto.ShapeBase):
    """
    Provides details of `WorkflowExecutionStarted` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "child_policy",
                "childPolicy",
                autoboto.TypeInfo(ChildPolicy),
            ),
            (
                "task_list",
                "taskList",
                autoboto.TypeInfo(TaskList),
            ),
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_start_to_close_timeout",
                "executionStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "task_start_to_close_timeout",
                "taskStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "task_priority",
                "taskPriority",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_list",
                "tagList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "continued_execution_run_id",
                "continuedExecutionRunId",
                autoboto.TypeInfo(str),
            ),
            (
                "parent_workflow_execution",
                "parentWorkflowExecution",
                autoboto.TypeInfo(WorkflowExecution),
            ),
            (
                "parent_initiated_event_id",
                "parentInitiatedEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "lambda_role",
                "lambdaRole",
                autoboto.TypeInfo(str),
            ),
        ]

    # The policy to use for the child workflow executions if this workflow
    # execution is terminated, by calling the TerminateWorkflowExecution action
    # explicitly or due to an expired timeout.

    # The supported child policies are:

    #   * `TERMINATE` – The child executions are terminated.

    #   * `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.

    #   * `ABANDON` – No action is taken. The child executions continue to run.
    child_policy: "ChildPolicy" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the task list for scheduling the decision tasks for this
    # workflow execution.
    task_list: "TaskList" = dataclasses.field(default_factory=dict, )

    # The workflow type of this execution.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )

    # The input provided to the workflow execution.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum duration for this workflow execution.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    execution_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum duration of decision tasks for this workflow type.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    task_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The priority of the decision tasks in the workflow execution.
    task_priority: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The list of tags associated with this workflow execution. An execution can
    # have up to 5 tags.
    tag_list: typing.List[str] = dataclasses.field(default_factory=list, )

    # If this workflow execution was started due to a
    # `ContinueAsNewWorkflowExecution` decision, then it contains the `runId` of
    # the previous workflow execution that was closed and continued as this
    # execution.
    continued_execution_run_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The source workflow execution that started this workflow execution. The
    # member isn't set if the workflow execution was not started by a workflow.
    parent_workflow_execution: "WorkflowExecution" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to
    # the `StartChildWorkflowExecution` Decision to start this workflow
    # execution. The source event with this ID can be found in the history of the
    # source workflow execution. This information can be useful for diagnosing
    # problems by tracing back the chain of events leading up to this event.
    parent_initiated_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IAM role attached to the workflow execution.
    lambda_role: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class WorkflowExecutionTerminatedCause(Enum):
    CHILD_POLICY_APPLIED = "CHILD_POLICY_APPLIED"
    EVENT_LIMIT_EXCEEDED = "EVENT_LIMIT_EXCEEDED"
    OPERATOR_INITIATED = "OPERATOR_INITIATED"


@dataclasses.dataclass
class WorkflowExecutionTerminatedEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `WorkflowExecutionTerminated` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "child_policy",
                "childPolicy",
                autoboto.TypeInfo(ChildPolicy),
            ),
            (
                "reason",
                "reason",
                autoboto.TypeInfo(str),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(WorkflowExecutionTerminatedCause),
            ),
        ]

    # The policy used for the child workflow executions of this workflow
    # execution.

    # The supported child policies are:

    #   * `TERMINATE` – The child executions are terminated.

    #   * `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.

    #   * `ABANDON` – No action is taken. The child executions continue to run.
    child_policy: "ChildPolicy" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The reason provided for the termination.
    reason: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The details provided for the termination.
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If set, indicates that the workflow execution was automatically terminated,
    # and specifies the cause. This happens if the parent workflow execution
    # times out or is terminated and the child policy is set to terminate child
    # executions.
    cause: "WorkflowExecutionTerminatedCause" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class WorkflowExecutionTimedOutEventAttributes(autoboto.ShapeBase):
    """
    Provides the details of the `WorkflowExecutionTimedOut` event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timeout_type",
                "timeoutType",
                autoboto.TypeInfo(WorkflowExecutionTimeoutType),
            ),
            (
                "child_policy",
                "childPolicy",
                autoboto.TypeInfo(ChildPolicy),
            ),
        ]

    # The type of timeout that caused this event.
    timeout_type: "WorkflowExecutionTimeoutType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The policy used for the child workflow executions of this workflow
    # execution.

    # The supported child policies are:

    #   * `TERMINATE` – The child executions are terminated.

    #   * `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.

    #   * `ABANDON` – No action is taken. The child executions continue to run.
    child_policy: "ChildPolicy" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class WorkflowExecutionTimeoutType(Enum):
    START_TO_CLOSE = "START_TO_CLOSE"


@dataclasses.dataclass
class WorkflowType(autoboto.ShapeBase):
    """
    Represents a workflow type.
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
                "version",
                "version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the workflow type.

    # The combination of workflow type name and version must be unique with in a
    # domain.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The version of the workflow type.

    # The combination of workflow type name and version must be unique with in a
    # domain.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WorkflowTypeConfiguration(autoboto.ShapeBase):
    """
    The configuration settings of a workflow type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "default_task_start_to_close_timeout",
                "defaultTaskStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "default_execution_start_to_close_timeout",
                "defaultExecutionStartToCloseTimeout",
                autoboto.TypeInfo(str),
            ),
            (
                "default_task_list",
                "defaultTaskList",
                autoboto.TypeInfo(TaskList),
            ),
            (
                "default_task_priority",
                "defaultTaskPriority",
                autoboto.TypeInfo(str),
            ),
            (
                "default_child_policy",
                "defaultChildPolicy",
                autoboto.TypeInfo(ChildPolicy),
            ),
            (
                "default_lambda_role",
                "defaultLambdaRole",
                autoboto.TypeInfo(str),
            ),
        ]

    # The default maximum duration, specified when registering the workflow type,
    # that a decision task for executions of this workflow type might take before
    # returning completion or failure. If the task doesn'tdo close in the
    # specified time then the task is automatically timed out and rescheduled. If
    # the decider eventually reports a completion or failure, it is ignored. This
    # default can be overridden when starting a workflow execution using the
    # StartWorkflowExecution action or the `StartChildWorkflowExecution`
    # Decision.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    default_task_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default maximum duration, specified when registering the workflow type,
    # for executions of this workflow type. This default can be overridden when
    # starting a workflow execution using the StartWorkflowExecution action or
    # the `StartChildWorkflowExecution` Decision.

    # The duration is specified in seconds, an integer greater than or equal to
    # `0`. You can use `NONE` to specify unlimited duration.
    default_execution_start_to_close_timeout: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default task list, specified when registering the workflow type, for
    # decisions tasks scheduled for workflow executions of this type. This
    # default can be overridden when starting a workflow execution using the
    # StartWorkflowExecution action or the `StartChildWorkflowExecution`
    # Decision.
    default_task_list: "TaskList" = dataclasses.field(default_factory=dict, )

    # The default task priority, specified when registering the workflow type,
    # for all decision tasks of this workflow type. This default can be
    # overridden when starting a workflow execution using the
    # StartWorkflowExecution action or the `StartChildWorkflowExecution`
    # decision.

    # Valid values are integers that range from Java's `Integer.MIN_VALUE`
    # (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate
    # higher priority.

    # For more information about setting task priority, see [Setting Task
    # Priority](http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-
    # priority.html) in the _Amazon SWF Developer Guide_.
    default_task_priority: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default policy to use for the child workflow executions when a workflow
    # execution of this type is terminated, by calling the
    # TerminateWorkflowExecution action explicitly or due to an expired timeout.
    # This default can be overridden when starting a workflow execution using the
    # StartWorkflowExecution action or the `StartChildWorkflowExecution`
    # Decision.

    # The supported child policies are:

    #   * `TERMINATE` – The child executions are terminated.

    #   * `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.

    #   * `ABANDON` – No action is taken. The child executions continue to run.
    default_child_policy: "ChildPolicy" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The default IAM role attached to this workflow type.

    # Executions of this workflow type need IAM roles to invoke Lambda functions.
    # If you don't specify an IAM role when starting this workflow type, the
    # default Lambda role is attached to the execution. For more information, see
    # <http://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-
    # task.html> in the _Amazon SWF Developer Guide_.
    default_lambda_role: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class WorkflowTypeDetail(autoboto.ShapeBase):
    """
    Contains details about a workflow type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_info",
                "typeInfo",
                autoboto.TypeInfo(WorkflowTypeInfo),
            ),
            (
                "configuration",
                "configuration",
                autoboto.TypeInfo(WorkflowTypeConfiguration),
            ),
        ]

    # General information about the workflow type.

    # The status of the workflow type (returned in the WorkflowTypeInfo
    # structure) can be one of the following.

    #   * `REGISTERED` – The type is registered and available. Workers supporting this type should be running.

    #   * `DEPRECATED` – The type was deprecated using DeprecateWorkflowType, but is still in use. You should keep workers supporting this type running. You cannot create new workflow executions of this type.
    type_info: "WorkflowTypeInfo" = dataclasses.field(default_factory=dict, )

    # Configuration settings of the workflow type registered through
    # RegisterWorkflowType
    configuration: "WorkflowTypeConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class WorkflowTypeFilter(autoboto.ShapeBase):
    """
    Used to filter workflow execution query results by type. Each parameter, if
    specified, defines a rule that must be satisfied by each returned result.
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
                "version",
                "version",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the workflow type.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Version of the workflow type.
    version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WorkflowTypeInfo(autoboto.ShapeBase):
    """
    Contains information about a workflow type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workflow_type",
                "workflowType",
                autoboto.TypeInfo(WorkflowType),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(RegistrationStatus),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "deprecation_date",
                "deprecationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The workflow type this information is about.
    workflow_type: "WorkflowType" = dataclasses.field(default_factory=dict, )

    # The current status of the workflow type.
    status: "RegistrationStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date when this type was registered.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The description of the type registered through RegisterWorkflowType.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If the type is in deprecated state, then it is set to the date when the
    # type was deprecated.
    deprecation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class WorkflowTypeInfos(autoboto.ShapeBase):
    """
    Contains a paginated list of information structures about workflow types.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_infos",
                "typeInfos",
                autoboto.TypeInfo(typing.List[WorkflowTypeInfo]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of workflow type information.
    type_infos: typing.List["WorkflowTypeInfo"] = dataclasses.field(
        default_factory=list,
    )

    # If a `NextPageToken` was returned by a previous call, there are more
    # results available. To retrieve the next page of results, make the call
    # again using the returned token in `nextPageToken`. Keep all other arguments
    # unchanged.

    # The configured `maximumPageSize` determines how many results can be
    # returned in a single call.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
