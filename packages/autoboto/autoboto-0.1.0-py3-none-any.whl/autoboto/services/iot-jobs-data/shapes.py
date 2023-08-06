import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


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
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


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
                "include_job_document",
                "includeJobDocument",
                autoboto.TypeInfo(bool),
            ),
            (
                "execution_number",
                "executionNumber",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique identifier assigned to this job when it was created.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The thing name associated with the device the job execution is running on.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Optional. When set to true, the response contains the job document. The
    # default is false.
    include_job_document: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional. A number that identifies a particular job execution on a
    # particular device. If not specified, the latest job execution is returned.
    execution_number: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeJobExecutionResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "execution",
                "execution",
                autoboto.TypeInfo(JobExecution),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains data about a job execution.
    execution: "JobExecution" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetPendingJobExecutionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the thing that is executing the job.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPendingJobExecutionsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "in_progress_jobs",
                "inProgressJobs",
                autoboto.TypeInfo(typing.List[JobExecutionSummary]),
            ),
            (
                "queued_jobs",
                "queuedJobs",
                autoboto.TypeInfo(typing.List[JobExecutionSummary]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of JobExecutionSummary objects with status IN_PROGRESS.
    in_progress_jobs: typing.List["JobExecutionSummary"] = dataclasses.field(
        default_factory=list,
    )

    # A list of JobExecutionSummary objects with status QUEUED.
    queued_jobs: typing.List["JobExecutionSummary"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class InvalidRequestException(autoboto.ShapeBase):
    """
    The contents of the request were invalid. For example, this code is returned
    when an UpdateJobExecution request contains invalid status details. The message
    contains details about the error.
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
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidStateTransitionException(autoboto.ShapeBase):
    """
    An update attempted to change the job execution to a state that is invalid
    because of the job execution's current state (for example, an attempt to change
    a request in state SUCCESS to state IN_PROGRESS). In this case, the body of the
    error message also contains the executionState field.
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
class JobExecution(autoboto.ShapeBase):
    """
    Contains data about a job execution.
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
                "status_details",
                "statusDetails",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "queued_at",
                "queuedAt",
                autoboto.TypeInfo(int),
            ),
            (
                "started_at",
                "startedAt",
                autoboto.TypeInfo(int),
            ),
            (
                "last_updated_at",
                "lastUpdatedAt",
                autoboto.TypeInfo(int),
            ),
            (
                "version_number",
                "versionNumber",
                autoboto.TypeInfo(int),
            ),
            (
                "execution_number",
                "executionNumber",
                autoboto.TypeInfo(int),
            ),
            (
                "job_document",
                "jobDocument",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier you assigned to this job when it was created.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the thing that is executing the job.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the job execution. Can be one of: "QUEUED", "IN_PROGRESS",
    # "FAILED", "SUCCESS", "CANCELED", "REJECTED", or "REMOVED".
    status: "JobExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A collection of name/value pairs that describe the status of the job
    # execution.
    status_details: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time, in milliseconds since the epoch, when the job execution was
    # enqueued.
    queued_at: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the job execution was
    # started.
    started_at: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the job execution was last
    # updated.
    last_updated_at: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The version of the job execution. Job execution versions are incremented
    # each time they are updated by a device.
    version_number: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A number that identifies a particular job execution on a particular device.
    # It can be used later in commands that return or update job execution
    # information.
    execution_number: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The content of the job document.
    job_document: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class JobExecutionState(autoboto.ShapeBase):
    """
    Contains data about the state of a job execution.
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
                "status_details",
                "statusDetails",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "version_number",
                "versionNumber",
                autoboto.TypeInfo(int),
            ),
        ]

    # The status of the job execution. Can be one of: "QUEUED", "IN_PROGRESS",
    # "FAILED", "SUCCESS", "CANCELED", "REJECTED", or "REMOVED".
    status: "JobExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A collection of name/value pairs that describe the status of the job
    # execution.
    status_details: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The version of the job execution. Job execution versions are incremented
    # each time they are updated by a device.
    version_number: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
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
class JobExecutionSummary(autoboto.ShapeBase):
    """
    Contains a subset of information about a job execution.
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
                "queued_at",
                "queuedAt",
                autoboto.TypeInfo(int),
            ),
            (
                "started_at",
                "startedAt",
                autoboto.TypeInfo(int),
            ),
            (
                "last_updated_at",
                "lastUpdatedAt",
                autoboto.TypeInfo(int),
            ),
            (
                "version_number",
                "versionNumber",
                autoboto.TypeInfo(int),
            ),
            (
                "execution_number",
                "executionNumber",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique identifier you assigned to this job when it was created.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the job execution was
    # enqueued.
    queued_at: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the job execution started.
    started_at: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the job execution was last
    # updated.
    last_updated_at: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The version of the job execution. Job execution versions are incremented
    # each time AWS IoT Jobs receives an update from a device.
    version_number: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A number that identifies a particular job execution on a particular device.
    execution_number: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


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
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


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
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartNextPendingJobExecutionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "thingName",
                autoboto.TypeInfo(str),
            ),
            (
                "status_details",
                "statusDetails",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the thing associated with the device.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A collection of name/value pairs that describe the status of the job
    # execution. If not specified, the statusDetails are unchanged.
    status_details: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartNextPendingJobExecutionResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "execution",
                "execution",
                autoboto.TypeInfo(JobExecution),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A JobExecution object.
    execution: "JobExecution" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class TerminalStateException(autoboto.ShapeBase):
    """
    The job is in a terminal state.
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
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateJobExecutionRequest(autoboto.ShapeBase):
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
                "status",
                "status",
                autoboto.TypeInfo(JobExecutionStatus),
            ),
            (
                "status_details",
                "statusDetails",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "expected_version",
                "expectedVersion",
                autoboto.TypeInfo(int),
            ),
            (
                "include_job_execution_state",
                "includeJobExecutionState",
                autoboto.TypeInfo(bool),
            ),
            (
                "include_job_document",
                "includeJobDocument",
                autoboto.TypeInfo(bool),
            ),
            (
                "execution_number",
                "executionNumber",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique identifier assigned to this job when it was created.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the thing associated with the device.
    thing_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The new status for the job execution (IN_PROGRESS, FAILED, SUCCESS, or
    # REJECTED). This must be specified on every update.
    status: "JobExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional. A collection of name/value pairs that describe the status of the
    # job execution. If not specified, the statusDetails are unchanged.
    status_details: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional. The expected current version of the job execution. Each time you
    # update the job execution, its version is incremented. If the version of the
    # job execution stored in Jobs does not match, the update is rejected with a
    # VersionMismatch error, and an ErrorResponse that contains the current job
    # execution status data is returned. (This makes it unnecessary to perform a
    # separate DescribeJobExecution request in order to obtain the job execution
    # status data.)
    expected_version: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional. When included and set to true, the response contains the
    # JobExecutionState data. The default is false.
    include_job_execution_state: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional. When set to true, the response contains the job document. The
    # default is false.
    include_job_document: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional. A number that identifies a particular job execution on a
    # particular device.
    execution_number: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateJobExecutionResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "execution_state",
                "executionState",
                autoboto.TypeInfo(JobExecutionState),
            ),
            (
                "job_document",
                "jobDocument",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A JobExecutionState object.
    execution_state: "JobExecutionState" = dataclasses.field(
        default_factory=dict,
    )

    # The contents of the Job Documents.
    job_document: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
