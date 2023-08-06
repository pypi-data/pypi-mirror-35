import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class ActivityDoesNotExist(autoboto.ShapeBase):
    """
    The specified activity does not exist.
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
class ActivityFailedEventDetails(autoboto.ShapeBase):
    """
    Contains details about an activity which failed during an execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error",
                "error",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error code of the failure.
    error: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A more detailed explanation of the cause of the failure.
    cause: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ActivityLimitExceeded(autoboto.ShapeBase):
    """
    The maximum number of activities has been reached. Existing activities must be
    deleted before a new activity can be created.
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
class ActivityListItem(autoboto.ShapeBase):
    """
    Contains details about an activity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activity_arn",
                "activityArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Resource Name (ARN) that identifies the activity.
    activity_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the activity.

    # A name must _not_ contain:

    #   * whitespace

    #   * brackets `< > { } [ ]`

    #   * wildcard characters `? *`

    #   * special characters `" # % \ ^ | ~ ` $ & , ; : /`

    #   * control characters (`U+0000-001F`, `U+007F-009F`)
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date the activity is created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ActivityScheduleFailedEventDetails(autoboto.ShapeBase):
    """
    Contains details about an activity schedule failure which occurred during an
    execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error",
                "error",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error code of the failure.
    error: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A more detailed explanation of the cause of the failure.
    cause: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ActivityScheduledEventDetails(autoboto.ShapeBase):
    """
    Contains details about an activity scheduled during an execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource",
                "resource",
                autoboto.TypeInfo(str),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
            (
                "timeout_in_seconds",
                "timeoutInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "heartbeat_in_seconds",
                "heartbeatInSeconds",
                autoboto.TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the scheduled activity.
    resource: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The JSON data input to the activity task.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum allowed duration of the activity task.
    timeout_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum allowed duration between two heartbeats for the activity task.
    heartbeat_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ActivityStartedEventDetails(autoboto.ShapeBase):
    """
    Contains details about the start of an activity during an execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "worker_name",
                "workerName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the worker that the task is assigned to. These names are
    # provided by the workers when calling GetActivityTask.
    worker_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ActivitySucceededEventDetails(autoboto.ShapeBase):
    """
    Contains details about an activity which successfully terminated during an
    execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output",
                "output",
                autoboto.TypeInfo(str),
            ),
        ]

    # The JSON data output by the activity task.
    output: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ActivityTimedOutEventDetails(autoboto.ShapeBase):
    """
    Contains details about an activity timeout which occurred during an execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error",
                "error",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error code of the failure.
    error: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A more detailed explanation of the cause of the timeout.
    cause: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ActivityWorkerLimitExceeded(autoboto.ShapeBase):
    """
    The maximum number of workers concurrently polling for activity tasks has been
    reached.
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
class CreateActivityInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the activity to create. This name must be unique for your AWS
    # account and region for 90 days. For more information, see [ Limits Related
    # to State Machine Executions](http://docs.aws.amazon.com/step-
    # functions/latest/dg/limits.html#service-limits-state-machine-executions) in
    # the _AWS Step Functions Developer Guide_.

    # A name must _not_ contain:

    #   * whitespace

    #   * brackets `< > { } [ ]`

    #   * wildcard characters `? *`

    #   * special characters `" # % \ ^ | ~ ` $ & , ; : /`

    #   * control characters (`U+0000-001F`, `U+007F-009F`)
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateActivityOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activity_arn",
                "activityArn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Resource Name (ARN) that identifies the created activity.
    activity_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date the activity is created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateStateMachineInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "definition",
                "definition",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the state machine. This name must be unique for your AWS
    # account and region for 90 days. For more information, see [ Limits Related
    # to State Machine Executions](http://docs.aws.amazon.com/step-
    # functions/latest/dg/limits.html#service-limits-state-machine-executions) in
    # the _AWS Step Functions Developer Guide_.

    # A name must _not_ contain:

    #   * whitespace

    #   * brackets `< > { } [ ]`

    #   * wildcard characters `? *`

    #   * special characters `" # % \ ^ | ~ ` $ & , ; : /`

    #   * control characters (`U+0000-001F`, `U+007F-009F`)
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon States Language definition of the state machine.
    definition: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role to use for this state
    # machine.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateStateMachineOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state_machine_arn",
                "stateMachineArn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Resource Name (ARN) that identifies the created state machine.
    state_machine_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the state machine is created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteActivityInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activity_arn",
                "activityArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the activity to delete.
    activity_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteActivityOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteStateMachineInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state_machine_arn",
                "stateMachineArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the state machine to delete.
    state_machine_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteStateMachineOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeActivityInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activity_arn",
                "activityArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the activity to describe.
    activity_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeActivityOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activity_arn",
                "activityArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Resource Name (ARN) that identifies the activity.
    activity_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the activity.

    # A name must _not_ contain:

    #   * whitespace

    #   * brackets `< > { } [ ]`

    #   * wildcard characters `? *`

    #   * special characters `" # % \ ^ | ~ ` $ & , ; : /`

    #   * control characters (`U+0000-001F`, `U+007F-009F`)
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date the activity is created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeExecutionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution_arn",
                "executionArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the execution to describe.
    execution_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeExecutionOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution_arn",
                "executionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "state_machine_arn",
                "stateMachineArn",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(ExecutionStatus),
            ),
            (
                "start_date",
                "startDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "stop_date",
                "stopDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "output",
                "output",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) that identifies the execution.
    execution_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the executed stated machine.
    state_machine_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The current status of the execution.
    status: "ExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the execution is started.
    start_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The string that contains the JSON input data of the execution.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the execution.

    # A name must _not_ contain:

    #   * whitespace

    #   * brackets `< > { } [ ]`

    #   * wildcard characters `? *`

    #   * special characters `" # % \ ^ | ~ ` $ & , ; : /`

    #   * control characters (`U+0000-001F`, `U+007F-009F`)
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If the execution has already ended, the date the execution stopped.
    stop_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The JSON output data of the execution.

    # This field is set only if the execution succeeds. If the execution fails,
    # this field is null.
    output: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeStateMachineForExecutionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution_arn",
                "executionArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the execution you want state machine
    # information for.
    execution_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeStateMachineForExecutionOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state_machine_arn",
                "stateMachineArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "definition",
                "definition",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "update_date",
                "updateDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Resource Name (ARN) of the state machine associated with the
    # execution.
    state_machine_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the state machine associated with the execution.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon States Language definition of the state machine.
    definition: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role of the State Machine for the
    # execution.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date and time the state machine associated with an execution was
    # updated. For a newly created state machine, this is the creation date.
    update_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeStateMachineInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state_machine_arn",
                "stateMachineArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the state machine to describe.
    state_machine_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeStateMachineOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state_machine_arn",
                "stateMachineArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "definition",
                "definition",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(StateMachineStatus),
            ),
        ]

    # The Amazon Resource Name (ARN) that identifies the state machine.
    state_machine_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the state machine.

    # A name must _not_ contain:

    #   * whitespace

    #   * brackets `< > { } [ ]`

    #   * wildcard characters `? *`

    #   * special characters `" # % \ ^ | ~ ` $ & , ; : /`

    #   * control characters (`U+0000-001F`, `U+007F-009F`)
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon States Language definition of the state machine.
    definition: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role used when creating this
    # state machine. (The IAM role maintains security by granting Step Functions
    # access to AWS resources.)
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date the state machine is created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The current status of the state machine.
    status: "StateMachineStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ExecutionAbortedEventDetails(autoboto.ShapeBase):
    """
    Contains details about an abort of an execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error",
                "error",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error code of the failure.
    error: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A more detailed explanation of the cause of the failure.
    cause: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ExecutionAlreadyExists(autoboto.ShapeBase):
    """
    The execution has the same `name` as another execution (but a different
    `input`).

    Executions with the same `name` and `input` are considered idempotent.
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
class ExecutionDoesNotExist(autoboto.ShapeBase):
    """
    The specified execution does not exist.
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
class ExecutionFailedEventDetails(autoboto.ShapeBase):
    """
    Contains details about an execution failure event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error",
                "error",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error code of the failure.
    error: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A more detailed explanation of the cause of the failure.
    cause: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ExecutionLimitExceeded(autoboto.ShapeBase):
    """
    The maximum number of running executions has been reached. Running executions
    must end or be stopped before a new execution can be started.
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
class ExecutionListItem(autoboto.ShapeBase):
    """
    Contains details about an execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution_arn",
                "executionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "state_machine_arn",
                "stateMachineArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(ExecutionStatus),
            ),
            (
                "start_date",
                "startDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "stop_date",
                "stopDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Resource Name (ARN) that identifies the execution.
    execution_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the executed state machine.
    state_machine_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the execution.

    # A name must _not_ contain:

    #   * whitespace

    #   * brackets `< > { } [ ]`

    #   * wildcard characters `? *`

    #   * special characters `" # % \ ^ | ~ ` $ & , ; : /`

    #   * control characters (`U+0000-001F`, `U+007F-009F`)
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The current status of the execution.
    status: "ExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the execution started.
    start_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the execution already ended, the date the execution stopped.
    stop_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ExecutionStartedEventDetails(autoboto.ShapeBase):
    """
    Contains details about the start of the execution.
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
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The JSON data input to the execution.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role used for executing AWS
    # Lambda tasks.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class ExecutionStatus(Enum):
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    TIMED_OUT = "TIMED_OUT"
    ABORTED = "ABORTED"


@dataclasses.dataclass
class ExecutionSucceededEventDetails(autoboto.ShapeBase):
    """
    Contains details about the successful termination of the execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output",
                "output",
                autoboto.TypeInfo(str),
            ),
        ]

    # The JSON data output by the execution.
    output: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ExecutionTimedOutEventDetails(autoboto.ShapeBase):
    """
    Contains details about the execution timeout which occurred during the
    execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error",
                "error",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error code of the failure.
    error: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A more detailed explanation of the cause of the timeout.
    cause: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetActivityTaskInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activity_arn",
                "activityArn",
                autoboto.TypeInfo(str),
            ),
            (
                "worker_name",
                "workerName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the activity to retrieve tasks from
    # (assigned when you create the task using CreateActivity.)
    activity_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # You can provide an arbitrary name in order to identify the worker that the
    # task is assigned to. This name is used when it is logged in the execution
    # history.
    worker_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetActivityTaskOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_token",
                "taskToken",
                autoboto.TypeInfo(str),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
        ]

    # A token that identifies the scheduled task. This token must be copied and
    # included in subsequent calls to SendTaskHeartbeat, SendTaskSuccess or
    # SendTaskFailure in order to report the progress or completion of the task.
    task_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The string that contains the JSON input data for the task.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetExecutionHistoryInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution_arn",
                "executionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "reverse_order",
                "reverseOrder",
                autoboto.TypeInfo(bool),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the execution.
    execution_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results that are returned per call. You can use
    # `nextToken` to obtain further pages of results. The default is 100 and the
    # maximum allowed page size is 100. A value of 0 uses the default.

    # This is only an upper limit. The actual number of results returned per call
    # might be fewer than the specified maximum.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Lists events in descending order of their `timeStamp`.
    reverse_order: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If a `nextToken` is returned by a previous call, there are more results
    # available. To retrieve the next page of results, make the call again using
    # the returned token in `nextToken`. Keep all other arguments unchanged.

    # The configured `maxResults` determines how many results can be returned in
    # a single call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetExecutionHistoryOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "events",
                "events",
                autoboto.TypeInfo(typing.List[HistoryEvent]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of events that occurred in the execution.
    events: typing.List["HistoryEvent"] = dataclasses.field(
        default_factory=list,
    )

    # If a `nextToken` is returned by a previous call, there are more results
    # available. To retrieve the next page of results, make the call again using
    # the returned token in `nextToken`. Keep all other arguments unchanged.

    # The configured `maxResults` determines how many results can be returned in
    # a single call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class HistoryEvent(autoboto.ShapeBase):
    """
    Contains details about the events of an execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timestamp",
                "timestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "type",
                "type",
                autoboto.TypeInfo(HistoryEventType),
            ),
            (
                "id",
                "id",
                autoboto.TypeInfo(int),
            ),
            (
                "previous_event_id",
                "previousEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "activity_failed_event_details",
                "activityFailedEventDetails",
                autoboto.TypeInfo(ActivityFailedEventDetails),
            ),
            (
                "activity_schedule_failed_event_details",
                "activityScheduleFailedEventDetails",
                autoboto.TypeInfo(ActivityScheduleFailedEventDetails),
            ),
            (
                "activity_scheduled_event_details",
                "activityScheduledEventDetails",
                autoboto.TypeInfo(ActivityScheduledEventDetails),
            ),
            (
                "activity_started_event_details",
                "activityStartedEventDetails",
                autoboto.TypeInfo(ActivityStartedEventDetails),
            ),
            (
                "activity_succeeded_event_details",
                "activitySucceededEventDetails",
                autoboto.TypeInfo(ActivitySucceededEventDetails),
            ),
            (
                "activity_timed_out_event_details",
                "activityTimedOutEventDetails",
                autoboto.TypeInfo(ActivityTimedOutEventDetails),
            ),
            (
                "execution_failed_event_details",
                "executionFailedEventDetails",
                autoboto.TypeInfo(ExecutionFailedEventDetails),
            ),
            (
                "execution_started_event_details",
                "executionStartedEventDetails",
                autoboto.TypeInfo(ExecutionStartedEventDetails),
            ),
            (
                "execution_succeeded_event_details",
                "executionSucceededEventDetails",
                autoboto.TypeInfo(ExecutionSucceededEventDetails),
            ),
            (
                "execution_aborted_event_details",
                "executionAbortedEventDetails",
                autoboto.TypeInfo(ExecutionAbortedEventDetails),
            ),
            (
                "execution_timed_out_event_details",
                "executionTimedOutEventDetails",
                autoboto.TypeInfo(ExecutionTimedOutEventDetails),
            ),
            (
                "lambda_function_failed_event_details",
                "lambdaFunctionFailedEventDetails",
                autoboto.TypeInfo(LambdaFunctionFailedEventDetails),
            ),
            (
                "lambda_function_schedule_failed_event_details",
                "lambdaFunctionScheduleFailedEventDetails",
                autoboto.TypeInfo(LambdaFunctionScheduleFailedEventDetails),
            ),
            (
                "lambda_function_scheduled_event_details",
                "lambdaFunctionScheduledEventDetails",
                autoboto.TypeInfo(LambdaFunctionScheduledEventDetails),
            ),
            (
                "lambda_function_start_failed_event_details",
                "lambdaFunctionStartFailedEventDetails",
                autoboto.TypeInfo(LambdaFunctionStartFailedEventDetails),
            ),
            (
                "lambda_function_succeeded_event_details",
                "lambdaFunctionSucceededEventDetails",
                autoboto.TypeInfo(LambdaFunctionSucceededEventDetails),
            ),
            (
                "lambda_function_timed_out_event_details",
                "lambdaFunctionTimedOutEventDetails",
                autoboto.TypeInfo(LambdaFunctionTimedOutEventDetails),
            ),
            (
                "state_entered_event_details",
                "stateEnteredEventDetails",
                autoboto.TypeInfo(StateEnteredEventDetails),
            ),
            (
                "state_exited_event_details",
                "stateExitedEventDetails",
                autoboto.TypeInfo(StateExitedEventDetails),
            ),
        ]

    # The date the event occurred.
    timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of the event.
    type: "HistoryEventType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The id of the event. Events are numbered sequentially, starting at one.
    id: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The id of the previous event.
    previous_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Contains details about an activity which failed during an execution.
    activity_failed_event_details: "ActivityFailedEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about an activity schedule event which failed during an
    # execution.
    activity_schedule_failed_event_details: "ActivityScheduleFailedEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about an activity scheduled during an execution.
    activity_scheduled_event_details: "ActivityScheduledEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about the start of an activity during an execution.
    activity_started_event_details: "ActivityStartedEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about an activity which successfully terminated during an
    # execution.
    activity_succeeded_event_details: "ActivitySucceededEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about an activity timeout which occurred during an
    # execution.
    activity_timed_out_event_details: "ActivityTimedOutEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about an execution failure event.
    execution_failed_event_details: "ExecutionFailedEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about the start of the execution.
    execution_started_event_details: "ExecutionStartedEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about the successful termination of the execution.
    execution_succeeded_event_details: "ExecutionSucceededEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about an abort of an execution.
    execution_aborted_event_details: "ExecutionAbortedEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about the execution timeout which occurred during the
    # execution.
    execution_timed_out_event_details: "ExecutionTimedOutEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about a lambda function which failed during an execution.
    lambda_function_failed_event_details: "LambdaFunctionFailedEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about a failed lambda function schedule event which
    # occurred during an execution.
    lambda_function_schedule_failed_event_details: "LambdaFunctionScheduleFailedEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about a lambda function scheduled during an execution.
    lambda_function_scheduled_event_details: "LambdaFunctionScheduledEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about a lambda function which failed to start during an
    # execution.
    lambda_function_start_failed_event_details: "LambdaFunctionStartFailedEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about a lambda function which terminated successfully
    # during an execution.
    lambda_function_succeeded_event_details: "LambdaFunctionSucceededEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about a lambda function timeout which occurred during an
    # execution.
    lambda_function_timed_out_event_details: "LambdaFunctionTimedOutEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about a state entered during an execution.
    state_entered_event_details: "StateEnteredEventDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Contains details about an exit from a state during an execution.
    state_exited_event_details: "StateExitedEventDetails" = dataclasses.field(
        default_factory=dict,
    )


class HistoryEventType(Enum):
    ActivityFailed = "ActivityFailed"
    ActivityScheduleFailed = "ActivityScheduleFailed"
    ActivityScheduled = "ActivityScheduled"
    ActivityStarted = "ActivityStarted"
    ActivitySucceeded = "ActivitySucceeded"
    ActivityTimedOut = "ActivityTimedOut"
    ChoiceStateEntered = "ChoiceStateEntered"
    ChoiceStateExited = "ChoiceStateExited"
    ExecutionFailed = "ExecutionFailed"
    ExecutionStarted = "ExecutionStarted"
    ExecutionSucceeded = "ExecutionSucceeded"
    ExecutionAborted = "ExecutionAborted"
    ExecutionTimedOut = "ExecutionTimedOut"
    FailStateEntered = "FailStateEntered"
    LambdaFunctionFailed = "LambdaFunctionFailed"
    LambdaFunctionScheduleFailed = "LambdaFunctionScheduleFailed"
    LambdaFunctionScheduled = "LambdaFunctionScheduled"
    LambdaFunctionStartFailed = "LambdaFunctionStartFailed"
    LambdaFunctionStarted = "LambdaFunctionStarted"
    LambdaFunctionSucceeded = "LambdaFunctionSucceeded"
    LambdaFunctionTimedOut = "LambdaFunctionTimedOut"
    SucceedStateEntered = "SucceedStateEntered"
    SucceedStateExited = "SucceedStateExited"
    TaskStateAborted = "TaskStateAborted"
    TaskStateEntered = "TaskStateEntered"
    TaskStateExited = "TaskStateExited"
    PassStateEntered = "PassStateEntered"
    PassStateExited = "PassStateExited"
    ParallelStateAborted = "ParallelStateAborted"
    ParallelStateEntered = "ParallelStateEntered"
    ParallelStateExited = "ParallelStateExited"
    ParallelStateFailed = "ParallelStateFailed"
    ParallelStateStarted = "ParallelStateStarted"
    ParallelStateSucceeded = "ParallelStateSucceeded"
    WaitStateAborted = "WaitStateAborted"
    WaitStateEntered = "WaitStateEntered"
    WaitStateExited = "WaitStateExited"


@dataclasses.dataclass
class InvalidArn(autoboto.ShapeBase):
    """
    The provided Amazon Resource Name (ARN) is invalid.
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
class InvalidDefinition(autoboto.ShapeBase):
    """
    The provided Amazon States Language definition is invalid.
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
class InvalidExecutionInput(autoboto.ShapeBase):
    """
    The provided JSON input data is invalid.
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
class InvalidName(autoboto.ShapeBase):
    """
    The provided name is invalid.
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
class InvalidOutput(autoboto.ShapeBase):
    """
    The provided JSON output data is invalid.
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
class InvalidToken(autoboto.ShapeBase):
    """
    The provided token is invalid.
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
class LambdaFunctionFailedEventDetails(autoboto.ShapeBase):
    """
    Contains details about a lambda function which failed during an execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error",
                "error",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error code of the failure.
    error: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A more detailed explanation of the cause of the failure.
    cause: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LambdaFunctionScheduleFailedEventDetails(autoboto.ShapeBase):
    """
    Contains details about a failed lambda function schedule event which occurred
    during an execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error",
                "error",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error code of the failure.
    error: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A more detailed explanation of the cause of the failure.
    cause: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LambdaFunctionScheduledEventDetails(autoboto.ShapeBase):
    """
    Contains details about a lambda function scheduled during an execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource",
                "resource",
                autoboto.TypeInfo(str),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
            (
                "timeout_in_seconds",
                "timeoutInSeconds",
                autoboto.TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the scheduled lambda function.
    resource: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The JSON data input to the lambda function.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum allowed duration of the lambda function.
    timeout_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class LambdaFunctionStartFailedEventDetails(autoboto.ShapeBase):
    """
    Contains details about a lambda function which failed to start during an
    execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error",
                "error",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error code of the failure.
    error: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A more detailed explanation of the cause of the failure.
    cause: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LambdaFunctionSucceededEventDetails(autoboto.ShapeBase):
    """
    Contains details about a lambda function which successfully terminated during an
    execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output",
                "output",
                autoboto.TypeInfo(str),
            ),
        ]

    # The JSON data output by the lambda function.
    output: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LambdaFunctionTimedOutEventDetails(autoboto.ShapeBase):
    """
    Contains details about a lambda function timeout which occurred during an
    execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error",
                "error",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error code of the failure.
    error: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A more detailed explanation of the cause of the timeout.
    cause: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListActivitiesInput(autoboto.ShapeBase):
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

    # The maximum number of results that are returned per call. You can use
    # `nextToken` to obtain further pages of results. The default is 100 and the
    # maximum allowed page size is 100. A value of 0 uses the default.

    # This is only an upper limit. The actual number of results returned per call
    # might be fewer than the specified maximum.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If a `nextToken` is returned by a previous call, there are more results
    # available. To retrieve the next page of results, make the call again using
    # the returned token in `nextToken`. Keep all other arguments unchanged.

    # The configured `maxResults` determines how many results can be returned in
    # a single call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListActivitiesOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activities",
                "activities",
                autoboto.TypeInfo(typing.List[ActivityListItem]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of activities.
    activities: typing.List["ActivityListItem"] = dataclasses.field(
        default_factory=list,
    )

    # If a `nextToken` is returned by a previous call, there are more results
    # available. To retrieve the next page of results, make the call again using
    # the returned token in `nextToken`. Keep all other arguments unchanged.

    # The configured `maxResults` determines how many results can be returned in
    # a single call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListExecutionsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state_machine_arn",
                "stateMachineArn",
                autoboto.TypeInfo(str),
            ),
            (
                "status_filter",
                "statusFilter",
                autoboto.TypeInfo(ExecutionStatus),
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

    # The Amazon Resource Name (ARN) of the state machine whose executions is
    # listed.
    state_machine_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If specified, only list the executions whose current execution status
    # matches the given filter.
    status_filter: "ExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of results that are returned per call. You can use
    # `nextToken` to obtain further pages of results. The default is 100 and the
    # maximum allowed page size is 100. A value of 0 uses the default.

    # This is only an upper limit. The actual number of results returned per call
    # might be fewer than the specified maximum.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If a `nextToken` is returned by a previous call, there are more results
    # available. To retrieve the next page of results, make the call again using
    # the returned token in `nextToken`. Keep all other arguments unchanged.

    # The configured `maxResults` determines how many results can be returned in
    # a single call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListExecutionsOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "executions",
                "executions",
                autoboto.TypeInfo(typing.List[ExecutionListItem]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of matching executions.
    executions: typing.List["ExecutionListItem"] = dataclasses.field(
        default_factory=list,
    )

    # If a `nextToken` is returned by a previous call, there are more results
    # available. To retrieve the next page of results, make the call again using
    # the returned token in `nextToken`. Keep all other arguments unchanged.

    # The configured `maxResults` determines how many results can be returned in
    # a single call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListStateMachinesInput(autoboto.ShapeBase):
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

    # The maximum number of results that are returned per call. You can use
    # `nextToken` to obtain further pages of results. The default is 100 and the
    # maximum allowed page size is 100. A value of 0 uses the default.

    # This is only an upper limit. The actual number of results returned per call
    # might be fewer than the specified maximum.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If a `nextToken` is returned by a previous call, there are more results
    # available. To retrieve the next page of results, make the call again using
    # the returned token in `nextToken`. Keep all other arguments unchanged.

    # The configured `maxResults` determines how many results can be returned in
    # a single call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListStateMachinesOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state_machines",
                "stateMachines",
                autoboto.TypeInfo(typing.List[StateMachineListItem]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    state_machines: typing.List["StateMachineListItem"] = dataclasses.field(
        default_factory=list,
    )

    # If a `nextToken` is returned by a previous call, there are more results
    # available. To retrieve the next page of results, make the call again using
    # the returned token in `nextToken`. Keep all other arguments unchanged.

    # The configured `maxResults` determines how many results can be returned in
    # a single call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class MissingRequiredParameter(autoboto.ShapeBase):
    """
    Request is missing a required parameter. This error occurs if both `definition`
    and `roleArn` are not specified.
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
class SendTaskFailureInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_token",
                "taskToken",
                autoboto.TypeInfo(str),
            ),
            (
                "error",
                "error",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(str),
            ),
        ]

    # The token that represents this task. Task tokens are generated by the
    # service when the tasks are assigned to a worker (see
    # GetActivityTask::taskToken).
    task_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An arbitrary error code that identifies the cause of the failure.
    error: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A more detailed explanation of the cause of the failure.
    cause: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SendTaskFailureOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SendTaskHeartbeatInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_token",
                "taskToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The token that represents this task. Task tokens are generated by the
    # service when the tasks are assigned to a worker (see
    # GetActivityTaskOutput$taskToken).
    task_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SendTaskHeartbeatOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SendTaskSuccessInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_token",
                "taskToken",
                autoboto.TypeInfo(str),
            ),
            (
                "output",
                "output",
                autoboto.TypeInfo(str),
            ),
        ]

    # The token that represents this task. Task tokens are generated by the
    # service when the tasks are assigned to a worker (see
    # GetActivityTaskOutput$taskToken).
    task_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The JSON output of the task.
    output: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SendTaskSuccessOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StartExecutionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state_machine_arn",
                "stateMachineArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the state machine to execute.
    state_machine_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the execution. This name must be unique for your AWS account
    # and region for 90 days. For more information, see [ Limits Related to State
    # Machine Executions](http://docs.aws.amazon.com/step-
    # functions/latest/dg/limits.html#service-limits-state-machine-executions) in
    # the _AWS Step Functions Developer Guide_.

    # An execution can't use the name of another execution for 90 days.

    # When you make multiple `StartExecution` calls with the same name, the new
    # execution doesn't run and the following rules apply:

    #   * When the original execution is open and the execution input from the new call is _different_ , the `ExecutionAlreadyExists` message is returned.

    #   * When the original execution is open and the execution input from the new call is _identical_ , the `Success` message is returned.

    #   * When the original execution is closed, the `ExecutionAlreadyExists` message is returned regardless of input.

    # A name must _not_ contain:

    #   * whitespace

    #   * brackets `< > { } [ ]`

    #   * wildcard characters `? *`

    #   * special characters `" # % \ ^ | ~ ` $ & , ; : /`

    #   * control characters (`U+0000-001F`, `U+007F-009F`)
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The string that contains the JSON input data for the execution, for
    # example:

    # `"input": "{\"first_name\" : \"test\"}"`

    # If you don't include any JSON input data, you still must include the two
    # braces, for example: `"input": "{}"`
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StartExecutionOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution_arn",
                "executionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "start_date",
                "startDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Resource Name (ARN) that identifies the execution.
    execution_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date the execution is started.
    start_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class StateEnteredEventDetails(autoboto.ShapeBase):
    """
    Contains details about a state entered during an execution.
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
                "input",
                "input",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the state.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The string that contains the JSON input data for the state.
    input: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StateExitedEventDetails(autoboto.ShapeBase):
    """
    Contains details about an exit from a state during an execution.
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
                "output",
                "output",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the state.

    # A name must _not_ contain:

    #   * whitespace

    #   * brackets `< > { } [ ]`

    #   * wildcard characters `? *`

    #   * special characters `" # % \ ^ | ~ ` $ & , ; : /`

    #   * control characters (`U+0000-001F`, `U+007F-009F`)
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The JSON output data of the state.
    output: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StateMachineAlreadyExists(autoboto.ShapeBase):
    """
    A state machine with the same name but a different definition or role ARN
    already exists.
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
class StateMachineDeleting(autoboto.ShapeBase):
    """
    The specified state machine is being deleted.
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
class StateMachineDoesNotExist(autoboto.ShapeBase):
    """
    The specified state machine does not exist.
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
class StateMachineLimitExceeded(autoboto.ShapeBase):
    """
    The maximum number of state machines has been reached. Existing state machines
    must be deleted before a new state machine can be created.
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
class StateMachineListItem(autoboto.ShapeBase):
    """
    Contains details about the state machine.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state_machine_arn",
                "stateMachineArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Resource Name (ARN) that identifies the state machine.
    state_machine_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the state machine.

    # A name must _not_ contain:

    #   * whitespace

    #   * brackets `< > { } [ ]`

    #   * wildcard characters `? *`

    #   * special characters `" # % \ ^ | ~ ` $ & , ; : /`

    #   * control characters (`U+0000-001F`, `U+007F-009F`)
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date the state machine is created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class StateMachineStatus(Enum):
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


@dataclasses.dataclass
class StopExecutionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution_arn",
                "executionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "error",
                "error",
                autoboto.TypeInfo(str),
            ),
            (
                "cause",
                "cause",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the execution to stop.
    execution_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An arbitrary error code that identifies the cause of the termination.
    error: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A more detailed explanation of the cause of the termination.
    cause: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StopExecutionOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stop_date",
                "stopDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The date the execution is stopped.
    stop_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class TaskDoesNotExist(autoboto.ShapeBase):
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
class TaskTimedOut(autoboto.ShapeBase):
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
class UpdateStateMachineInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state_machine_arn",
                "stateMachineArn",
                autoboto.TypeInfo(str),
            ),
            (
                "definition",
                "definition",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the state machine.
    state_machine_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon States Language definition of the state machine.
    definition: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role of the state machine.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateStateMachineOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "update_date",
                "updateDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The date and time the state machine was updated.
    update_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
