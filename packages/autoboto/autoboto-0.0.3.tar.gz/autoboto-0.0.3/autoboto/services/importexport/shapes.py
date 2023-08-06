import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class Artifact(autoboto.ShapeBase):
    """
    A discrete item that contains the description and URL of an artifact (such as a
    PDF).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "url",
                "URL",
                autoboto.TypeInfo(str),
            ),
        ]

    # The associated description for this object.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL for a given Artifact.
    url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BucketPermissionException(autoboto.ShapeBase):
    """
    The account specified does not have the appropriate bucket permissions.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CancelJobInput(autoboto.ShapeBase):
    """
    Input structure for the CancelJob operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                autoboto.TypeInfo(str),
            ),
            (
                "api_version",
                "APIVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier which refers to a particular job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the version of the client tool.
    api_version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CancelJobOutput(autoboto.ShapeBase):
    """
    Output structure for the CancelJob operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "success",
                "Success",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Specifies whether (true) or not (false) AWS Import/Export updated your job.
    success: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CanceledJobIdException(autoboto.ShapeBase):
    """
    The specified job ID has been canceled and is no longer valid.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateJobInput(autoboto.ShapeBase):
    """
    Input structure for the CreateJob operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_type",
                "JobType",
                autoboto.TypeInfo(JobType),
            ),
            (
                "manifest",
                "Manifest",
                autoboto.TypeInfo(str),
            ),
            (
                "validate_only",
                "ValidateOnly",
                autoboto.TypeInfo(bool),
            ),
            (
                "manifest_addendum",
                "ManifestAddendum",
                autoboto.TypeInfo(str),
            ),
            (
                "api_version",
                "APIVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # Specifies whether the job to initiate is an import or export job.
    job_type: "JobType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The UTF-8 encoded text of the manifest file.
    manifest: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Validate the manifest and parameter values in the request but do not
    # actually create a job.
    validate_only: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # For internal use only.
    manifest_addendum: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the version of the client tool.
    api_version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateJobOutput(autoboto.ShapeBase):
    """
    Output structure for the CreateJob operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                autoboto.TypeInfo(str),
            ),
            (
                "job_type",
                "JobType",
                autoboto.TypeInfo(JobType),
            ),
            (
                "signature",
                "Signature",
                autoboto.TypeInfo(str),
            ),
            (
                "signature_file_contents",
                "SignatureFileContents",
                autoboto.TypeInfo(str),
            ),
            (
                "warning_message",
                "WarningMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "artifact_list",
                "ArtifactList",
                autoboto.TypeInfo(typing.List[Artifact]),
            ),
        ]

    # A unique identifier which refers to a particular job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies whether the job to initiate is an import or export job.
    job_type: "JobType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An encrypted code used to authenticate the request and response, for
    # example, "DV+TpDfx1/TdSE9ktyK9k/bDTVI=". Only use this value is you want to
    # create the signature file yourself. Generally you should use the
    # SignatureFileContents value.
    signature: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The actual text of the SIGNATURE file to be written to disk.
    signature_file_contents: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An optional message notifying you of non-fatal issues with the job, such as
    # use of an incompatible Amazon S3 bucket name.
    warning_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A collection of artifacts.
    artifact_list: typing.List["Artifact"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateJobQuotaExceededException(autoboto.ShapeBase):
    """
    Each account can create only a certain number of jobs per day. If you need to
    create more than this, please contact awsimportexport@amazon.com to explain your
    particular use case.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ExpiredJobIdException(autoboto.ShapeBase):
    """
    Indicates that the specified job has expired out of the system.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetShippingLabelInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_ids",
                "jobIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "company",
                "company",
                autoboto.TypeInfo(str),
            ),
            (
                "phone_number",
                "phoneNumber",
                autoboto.TypeInfo(str),
            ),
            (
                "country",
                "country",
                autoboto.TypeInfo(str),
            ),
            (
                "state_or_province",
                "stateOrProvince",
                autoboto.TypeInfo(str),
            ),
            (
                "city",
                "city",
                autoboto.TypeInfo(str),
            ),
            (
                "postal_code",
                "postalCode",
                autoboto.TypeInfo(str),
            ),
            (
                "street1",
                "street1",
                autoboto.TypeInfo(str),
            ),
            (
                "street2",
                "street2",
                autoboto.TypeInfo(str),
            ),
            (
                "street3",
                "street3",
                autoboto.TypeInfo(str),
            ),
            (
                "api_version",
                "APIVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    job_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # Specifies the name of the person responsible for shipping this package.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the name of the company that will ship this package.
    company: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the phone number of the person responsible for shipping this
    # package.
    phone_number: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the name of your country for the return address.
    country: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the name of your state or your province for the return address.
    state_or_province: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the name of your city for the return address.
    city: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the postal code for the return address.
    postal_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the first part of the street address for the return address, for
    # example 1234 Main Street.
    street1: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the optional second part of the street address for the return
    # address, for example Suite 100.
    street2: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the optional third part of the street address for the return
    # address, for example c/o Jane Doe.
    street3: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the version of the client tool.
    api_version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetShippingLabelOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "shipping_label_url",
                "ShippingLabelURL",
                autoboto.TypeInfo(str),
            ),
            (
                "warning",
                "Warning",
                autoboto.TypeInfo(str),
            ),
        ]

    shipping_label_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
    warning: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetStatusInput(autoboto.ShapeBase):
    """
    Input structure for the GetStatus operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                autoboto.TypeInfo(str),
            ),
            (
                "api_version",
                "APIVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier which refers to a particular job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the version of the client tool.
    api_version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetStatusOutput(autoboto.ShapeBase):
    """
    Output structure for the GetStatus operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                autoboto.TypeInfo(str),
            ),
            (
                "job_type",
                "JobType",
                autoboto.TypeInfo(JobType),
            ),
            (
                "location_code",
                "LocationCode",
                autoboto.TypeInfo(str),
            ),
            (
                "location_message",
                "LocationMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "progress_code",
                "ProgressCode",
                autoboto.TypeInfo(str),
            ),
            (
                "progress_message",
                "ProgressMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "carrier",
                "Carrier",
                autoboto.TypeInfo(str),
            ),
            (
                "tracking_number",
                "TrackingNumber",
                autoboto.TypeInfo(str),
            ),
            (
                "log_bucket",
                "LogBucket",
                autoboto.TypeInfo(str),
            ),
            (
                "log_key",
                "LogKey",
                autoboto.TypeInfo(str),
            ),
            (
                "error_count",
                "ErrorCount",
                autoboto.TypeInfo(int),
            ),
            (
                "signature",
                "Signature",
                autoboto.TypeInfo(str),
            ),
            (
                "signature_file_contents",
                "SignatureFileContents",
                autoboto.TypeInfo(str),
            ),
            (
                "current_manifest",
                "CurrentManifest",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "artifact_list",
                "ArtifactList",
                autoboto.TypeInfo(typing.List[Artifact]),
            ),
        ]

    # A unique identifier which refers to a particular job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies whether the job to initiate is an import or export job.
    job_type: "JobType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A token representing the location of the storage device, such as "AtAWS".
    location_code: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A more human readable form of the physical location of the storage device.
    location_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A token representing the state of the job, such as "Started".
    progress_code: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A more human readable form of the job status.
    progress_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Name of the shipping company. This value is included when the LocationCode
    # is "Returned".
    carrier: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The shipping tracking number assigned by AWS Import/Export to the storage
    # device when it's returned to you. We return this value when the
    # LocationCode is "Returned".
    tracking_number: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Amazon S3 bucket for user logs.
    log_bucket: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The key where the user logs were stored.
    log_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Number of errors. We return this value when the ProgressCode is Success or
    # SuccessWithErrors.
    error_count: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An encrypted code used to authenticate the request and response, for
    # example, "DV+TpDfx1/TdSE9ktyK9k/bDTVI=". Only use this value is you want to
    # create the signature file yourself. Generally you should use the
    # SignatureFileContents value.
    signature: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An encrypted code used to authenticate the request and response, for
    # example, "DV+TpDfx1/TdSE9ktyK9k/bDTVI=". Only use this value is you want to
    # create the signature file yourself. Generally you should use the
    # SignatureFileContents value.
    signature_file_contents: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The last manifest submitted, which will be used to process the job.
    current_manifest: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Timestamp of the CreateJob request in ISO8601 date format. For example
    # "2010-03-28T20:27:35Z".
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A collection of artifacts.
    artifact_list: typing.List["Artifact"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class InvalidAccessKeyIdException(autoboto.ShapeBase):
    """
    The AWS Access Key ID specified in the request did not match the manifest's
    accessKeyId value. The manifest and the request authentication must use the same
    AWS Access Key ID.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidAddressException(autoboto.ShapeBase):
    """
    The address specified in the manifest is invalid.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidCustomsException(autoboto.ShapeBase):
    """
    One or more customs parameters was invalid. Please correct and resubmit.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidFileSystemException(autoboto.ShapeBase):
    """
    File system specified in export manifest is invalid.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidJobIdException(autoboto.ShapeBase):
    """
    The JOBID was missing, not found, or not associated with the AWS account.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidManifestFieldException(autoboto.ShapeBase):
    """
    One or more manifest fields was invalid. Please correct and resubmit.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidParameterException(autoboto.ShapeBase):
    """
    One or more parameters had an invalid value.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidVersionException(autoboto.ShapeBase):
    """
    The client tool version is invalid.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Job(autoboto.ShapeBase):
    """
    Representation of a job returned by the ListJobs operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "is_canceled",
                "IsCanceled",
                autoboto.TypeInfo(bool),
            ),
            (
                "job_type",
                "JobType",
                autoboto.TypeInfo(JobType),
            ),
        ]

    # A unique identifier which refers to a particular job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Timestamp of the CreateJob request in ISO8601 date format. For example
    # "2010-03-28T20:27:35Z".
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates whether the job was canceled.
    is_canceled: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies whether the job to initiate is an import or export job.
    job_type: "JobType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class JobType(Enum):
    """
    Specifies whether the job to initiate is an import or export job.
    """
    Import = "Import"
    Export = "Export"


@dataclasses.dataclass
class ListJobsInput(autoboto.ShapeBase):
    """
    Input structure for the ListJobs operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_jobs",
                "MaxJobs",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "api_version",
                "APIVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # Sets the maximum number of jobs returned in the response. If there are
    # additional jobs that were not returned because MaxJobs was exceeded, the
    # response contains <IsTruncated>true</IsTruncated>. To return the additional
    # jobs, see Marker.
    max_jobs: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the JOBID to start after when listing the jobs created with your
    # account. AWS Import/Export lists your jobs in reverse chronological order.
    # See MaxJobs.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the version of the client tool.
    api_version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListJobsOutput(autoboto.ShapeBase):
    """
    Output structure for the ListJobs operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "jobs",
                "Jobs",
                autoboto.TypeInfo(typing.List[Job]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A list container for Jobs returned by the ListJobs operation.
    jobs: typing.List["Job"] = dataclasses.field(default_factory=list, )

    # Indicates whether the list of jobs was truncated. If true, then call
    # ListJobs again using the last JobId element as the marker.
    is_truncated: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class MalformedManifestException(autoboto.ShapeBase):
    """
    Your manifest is not well-formed.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class MissingCustomsException(autoboto.ShapeBase):
    """
    One or more required customs parameters was missing from the manifest.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class MissingManifestFieldException(autoboto.ShapeBase):
    """
    One or more required fields were missing from the manifest file. Please correct
    and resubmit.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class MissingParameterException(autoboto.ShapeBase):
    """
    One or more required parameters was missing from the request.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class MultipleRegionsException(autoboto.ShapeBase):
    """
    Your manifest file contained buckets from multiple regions. A job is restricted
    to buckets from one region. Please correct and resubmit.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class NoSuchBucketException(autoboto.ShapeBase):
    """
    The specified bucket does not exist. Create the specified bucket or change the
    manifest's bucket, exportBucket, or logBucket field to a bucket that the
    account, as specified by the manifest's Access Key ID, has write permissions to.
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UnableToCancelJobIdException(autoboto.ShapeBase):
    """
    AWS Import/Export cannot cancel the job
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UnableToUpdateJobIdException(autoboto.ShapeBase):
    """
    AWS Import/Export cannot update the job
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

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateJobInput(autoboto.ShapeBase):
    """
    Input structure for the UpateJob operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                autoboto.TypeInfo(str),
            ),
            (
                "manifest",
                "Manifest",
                autoboto.TypeInfo(str),
            ),
            (
                "job_type",
                "JobType",
                autoboto.TypeInfo(JobType),
            ),
            (
                "validate_only",
                "ValidateOnly",
                autoboto.TypeInfo(bool),
            ),
            (
                "api_version",
                "APIVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier which refers to a particular job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The UTF-8 encoded text of the manifest file.
    manifest: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies whether the job to initiate is an import or export job.
    job_type: "JobType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Validate the manifest and parameter values in the request but do not
    # actually create a job.
    validate_only: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the version of the client tool.
    api_version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateJobOutput(autoboto.ShapeBase):
    """
    Output structure for the UpateJob operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "success",
                "Success",
                autoboto.TypeInfo(bool),
            ),
            (
                "warning_message",
                "WarningMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "artifact_list",
                "ArtifactList",
                autoboto.TypeInfo(typing.List[Artifact]),
            ),
        ]

    # Specifies whether (true) or not (false) AWS Import/Export updated your job.
    success: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An optional message notifying you of non-fatal issues with the job, such as
    # use of an incompatible Amazon S3 bucket name.
    warning_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A collection of artifacts.
    artifact_list: typing.List["Artifact"] = dataclasses.field(
        default_factory=list,
    )
