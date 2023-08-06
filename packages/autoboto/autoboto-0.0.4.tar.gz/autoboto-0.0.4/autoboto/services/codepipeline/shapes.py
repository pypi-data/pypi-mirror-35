import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AWSSessionCredentials(autoboto.ShapeBase):
    """
    Represents an AWS session credentials object. These credentials are temporary
    credentials that are issued by AWS Secure Token Service (STS). They can be used
    to access input and output artifacts in the Amazon S3 bucket used to store
    artifact for the pipeline in AWS CodePipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_key_id",
                "accessKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "secret_access_key",
                "secretAccessKey",
                autoboto.TypeInfo(str),
            ),
            (
                "session_token",
                "sessionToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The access key for the session.
    access_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The secret access key for the session.
    secret_access_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The token for the session.
    session_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AcknowledgeJobInput(autoboto.ShapeBase):
    """
    Represents the input of an AcknowledgeJob action.
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
                "nonce",
                "nonce",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique system-generated ID of the job for which you want to confirm
    # receipt.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A system-generated random number that AWS CodePipeline uses to ensure that
    # the job is being worked on by only one job worker. Get this number from the
    # response of the PollForJobs request that returned this job.
    nonce: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AcknowledgeJobOutput(autoboto.OutputShapeBase):
    """
    Represents the output of an AcknowledgeJob action.
    """

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
                autoboto.TypeInfo(JobStatus),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether the job worker has received the specified job.
    status: "JobStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AcknowledgeThirdPartyJobInput(autoboto.ShapeBase):
    """
    Represents the input of an AcknowledgeThirdPartyJob action.
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
                "nonce",
                "nonce",
                autoboto.TypeInfo(str),
            ),
            (
                "client_token",
                "clientToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique system-generated ID of the job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A system-generated random number that AWS CodePipeline uses to ensure that
    # the job is being worked on by only one job worker. Get this number from the
    # response to a GetThirdPartyJobDetails request.
    nonce: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The clientToken portion of the clientId and clientToken pair used to verify
    # that the calling entity is allowed access to the job and its details.
    client_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AcknowledgeThirdPartyJobOutput(autoboto.OutputShapeBase):
    """
    Represents the output of an AcknowledgeThirdPartyJob action.
    """

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
                autoboto.TypeInfo(JobStatus),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status information for the third party job, if any.
    status: "JobStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ActionCategory(Enum):
    Source = "Source"
    Build = "Build"
    Deploy = "Deploy"
    Test = "Test"
    Invoke = "Invoke"
    Approval = "Approval"


@dataclasses.dataclass
class ActionConfiguration(autoboto.ShapeBase):
    """
    Represents information about an action configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration",
                "configuration",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The configuration data for the action.
    configuration: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ActionConfigurationProperty(autoboto.ShapeBase):
    """
    Represents information about an action configuration property.
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
                "required",
                "required",
                autoboto.TypeInfo(bool),
            ),
            (
                "key",
                "key",
                autoboto.TypeInfo(bool),
            ),
            (
                "secret",
                "secret",
                autoboto.TypeInfo(bool),
            ),
            (
                "queryable",
                "queryable",
                autoboto.TypeInfo(bool),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "type",
                autoboto.TypeInfo(ActionConfigurationPropertyType),
            ),
        ]

    # The name of the action configuration property.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether the configuration property is a required value.
    required: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether the configuration property is a key.
    key: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether the configuration property is secret. Secrets are hidden from all
    # calls except for GetJobDetails, GetThirdPartyJobDetails, PollForJobs, and
    # PollForThirdPartyJobs.

    # When updating a pipeline, passing * * * * * without changing any other
    # values of the action will preserve the prior value of the secret.
    secret: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates that the property will be used in conjunction with PollForJobs.
    # When creating a custom action, an action can have up to one queryable
    # property. If it has one, that property must be both required and not
    # secret.

    # If you create a pipeline with a custom action type, and that custom action
    # contains a queryable property, the value for that configuration property is
    # subject to additional restrictions. The value must be less than or equal to
    # twenty (20) characters. The value can contain only alphanumeric characters,
    # underscores, and hyphens.
    queryable: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the action configuration property that will be displayed
    # to users.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of the configuration property.
    type: "ActionConfigurationPropertyType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ActionConfigurationPropertyType(Enum):
    String = "String"
    Number = "Number"
    Boolean = "Boolean"


@dataclasses.dataclass
class ActionContext(autoboto.ShapeBase):
    """
    Represents the context of an action within the stage of a pipeline to a job
    worker.
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

    # The name of the action within the context of a job.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ActionDeclaration(autoboto.ShapeBase):
    """
    Represents information about an action declaration.
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
                "action_type_id",
                "actionTypeId",
                autoboto.TypeInfo(ActionTypeId),
            ),
            (
                "run_order",
                "runOrder",
                autoboto.TypeInfo(int),
            ),
            (
                "configuration",
                "configuration",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "output_artifacts",
                "outputArtifacts",
                autoboto.TypeInfo(typing.List[OutputArtifact]),
            ),
            (
                "input_artifacts",
                "inputArtifacts",
                autoboto.TypeInfo(typing.List[InputArtifact]),
            ),
            (
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The action declaration's name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The configuration information for the action type.
    action_type_id: "ActionTypeId" = dataclasses.field(default_factory=dict, )

    # The order in which actions are run.
    run_order: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The action declaration's configuration.
    configuration: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name or ID of the result of the action declaration, such as a test or
    # build artifact.
    output_artifacts: typing.List["OutputArtifact"] = dataclasses.field(
        default_factory=list,
    )

    # The name or ID of the artifact consumed by the action, such as a test or
    # build artifact.
    input_artifacts: typing.List["InputArtifact"] = dataclasses.field(
        default_factory=list,
    )

    # The ARN of the IAM service role that will perform the declared action. This
    # is assumed through the roleArn for the pipeline.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ActionExecution(autoboto.ShapeBase):
    """
    Represents information about the run of an action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "status",
                autoboto.TypeInfo(ActionExecutionStatus),
            ),
            (
                "summary",
                "summary",
                autoboto.TypeInfo(str),
            ),
            (
                "last_status_change",
                "lastStatusChange",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "token",
                "token",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_by",
                "lastUpdatedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "external_execution_id",
                "externalExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "external_execution_url",
                "externalExecutionUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "percent_complete",
                "percentComplete",
                autoboto.TypeInfo(int),
            ),
            (
                "error_details",
                "errorDetails",
                autoboto.TypeInfo(ErrorDetails),
            ),
        ]

    # The status of the action, or for a completed action, the last status of the
    # action.
    status: "ActionExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A summary of the run of the action.
    summary: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The last status change of the action.
    last_status_change: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The system-generated token used to identify a unique approval request. The
    # token for each open approval request can be obtained using the
    # GetPipelineState command and is used to validate that the approval request
    # corresponding to this token is still valid.
    token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the user who last changed the pipeline.
    last_updated_by: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The external ID of the run of the action.
    external_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL of a resource external to AWS that will be used when running the
    # action, for example an external repository URL.
    external_execution_url: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A percentage of completeness of the action as it runs.
    percent_complete: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details of an error returned by a URL external to AWS.
    error_details: "ErrorDetails" = dataclasses.field(default_factory=dict, )


class ActionExecutionStatus(Enum):
    InProgress = "InProgress"
    Succeeded = "Succeeded"
    Failed = "Failed"


@dataclasses.dataclass
class ActionNotFoundException(autoboto.ShapeBase):
    """
    The specified action cannot be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class ActionOwner(Enum):
    AWS = "AWS"
    ThirdParty = "ThirdParty"
    Custom = "Custom"


@dataclasses.dataclass
class ActionRevision(autoboto.ShapeBase):
    """
    Represents information about the version (or revision) of an action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "revision_id",
                "revisionId",
                autoboto.TypeInfo(str),
            ),
            (
                "revision_change_id",
                "revisionChangeId",
                autoboto.TypeInfo(str),
            ),
            (
                "created",
                "created",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The system-generated unique ID that identifies the revision number of the
    # action.
    revision_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The unique identifier of the change that set the state to this revision,
    # for example a deployment ID or timestamp.
    revision_change_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time when the most recent version of the action was created,
    # in timestamp format.
    created: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ActionState(autoboto.ShapeBase):
    """
    Represents information about the state of an action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_name",
                "actionName",
                autoboto.TypeInfo(str),
            ),
            (
                "current_revision",
                "currentRevision",
                autoboto.TypeInfo(ActionRevision),
            ),
            (
                "latest_execution",
                "latestExecution",
                autoboto.TypeInfo(ActionExecution),
            ),
            (
                "entity_url",
                "entityUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "revision_url",
                "revisionUrl",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the action.
    action_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Represents information about the version (or revision) of an action.
    current_revision: "ActionRevision" = dataclasses.field(
        default_factory=dict,
    )

    # Represents information about the run of an action.
    latest_execution: "ActionExecution" = dataclasses.field(
        default_factory=dict,
    )

    # A URL link for more information about the state of the action, such as a
    # deployment group details page.
    entity_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A URL link for more information about the revision, such as a commit
    # details page.
    revision_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ActionType(autoboto.ShapeBase):
    """
    Returns information about the details of an action type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                autoboto.TypeInfo(ActionTypeId),
            ),
            (
                "input_artifact_details",
                "inputArtifactDetails",
                autoboto.TypeInfo(ArtifactDetails),
            ),
            (
                "output_artifact_details",
                "outputArtifactDetails",
                autoboto.TypeInfo(ArtifactDetails),
            ),
            (
                "settings",
                "settings",
                autoboto.TypeInfo(ActionTypeSettings),
            ),
            (
                "action_configuration_properties",
                "actionConfigurationProperties",
                autoboto.TypeInfo(typing.List[ActionConfigurationProperty]),
            ),
        ]

    # Represents information about an action type.
    id: "ActionTypeId" = dataclasses.field(default_factory=dict, )

    # The details of the input artifact for the action, such as its commit ID.
    input_artifact_details: "ArtifactDetails" = dataclasses.field(
        default_factory=dict,
    )

    # The details of the output artifact of the action, such as its commit ID.
    output_artifact_details: "ArtifactDetails" = dataclasses.field(
        default_factory=dict,
    )

    # The settings for the action type.
    settings: "ActionTypeSettings" = dataclasses.field(default_factory=dict, )

    # The configuration properties for the action type.
    action_configuration_properties: typing.List["ActionConfigurationProperty"
                                                ] = dataclasses.field(
                                                    default_factory=list,
                                                )


@dataclasses.dataclass
class ActionTypeId(autoboto.ShapeBase):
    """
    Represents information about an action type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "category",
                "category",
                autoboto.TypeInfo(ActionCategory),
            ),
            (
                "owner",
                "owner",
                autoboto.TypeInfo(ActionOwner),
            ),
            (
                "provider",
                "provider",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(str),
            ),
        ]

    # A category defines what kind of action can be taken in the stage, and
    # constrains the provider type for the action. Valid categories are limited
    # to one of the values below.
    category: "ActionCategory" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The creator of the action being called.
    owner: "ActionOwner" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The provider of the service being called by the action. Valid providers are
    # determined by the action category. For example, an action in the Deploy
    # category type might have a provider of AWS CodeDeploy, which would be
    # specified as CodeDeploy.
    provider: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A string that describes the action version.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ActionTypeNotFoundException(autoboto.ShapeBase):
    """
    The specified action type cannot be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ActionTypeSettings(autoboto.ShapeBase):
    """
    Returns information about the settings for an action type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "third_party_configuration_url",
                "thirdPartyConfigurationUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "entity_url_template",
                "entityUrlTemplate",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_url_template",
                "executionUrlTemplate",
                autoboto.TypeInfo(str),
            ),
            (
                "revision_url_template",
                "revisionUrlTemplate",
                autoboto.TypeInfo(str),
            ),
        ]

    # The URL of a sign-up page where users can sign up for an external service
    # and perform initial configuration of the action provided by that service.
    third_party_configuration_url: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL returned to the AWS CodePipeline console that provides a deep link
    # to the resources of the external system, such as the configuration page for
    # an AWS CodeDeploy deployment group. This link is provided as part of the
    # action display within the pipeline.
    entity_url_template: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL returned to the AWS CodePipeline console that contains a link to
    # the top-level landing page for the external system, such as console page
    # for AWS CodeDeploy. This link is shown on the pipeline view page in the AWS
    # CodePipeline console and provides a link to the execution entity of the
    # external action.
    execution_url_template: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL returned to the AWS CodePipeline console that contains a link to
    # the page where customers can update or change the configuration of the
    # external action.
    revision_url_template: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ApprovalAlreadyCompletedException(autoboto.ShapeBase):
    """
    The approval action has already been approved or rejected.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ApprovalResult(autoboto.ShapeBase):
    """
    Represents information about the result of an approval request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "summary",
                "summary",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(ApprovalStatus),
            ),
        ]

    # The summary of the current status of the approval request.
    summary: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The response submitted by a reviewer assigned to an approval action
    # request.
    status: "ApprovalStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ApprovalStatus(Enum):
    Approved = "Approved"
    Rejected = "Rejected"


@dataclasses.dataclass
class Artifact(autoboto.ShapeBase):
    """
    Represents information about an artifact that will be worked upon by actions in
    the pipeline.
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
                "revision",
                "revision",
                autoboto.TypeInfo(str),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(ArtifactLocation),
            ),
        ]

    # The artifact's name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The artifact's revision ID. Depending on the type of object, this could be
    # a commit ID (GitHub) or a revision ID (Amazon S3).
    revision: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The location of an artifact.
    location: "ArtifactLocation" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ArtifactDetails(autoboto.ShapeBase):
    """
    Returns information about the details of an artifact.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "minimum_count",
                "minimumCount",
                autoboto.TypeInfo(int),
            ),
            (
                "maximum_count",
                "maximumCount",
                autoboto.TypeInfo(int),
            ),
        ]

    # The minimum number of artifacts allowed for the action type.
    minimum_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of artifacts allowed for the action type.
    maximum_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ArtifactLocation(autoboto.ShapeBase):
    """
    Represents information about the location of an artifact.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(ArtifactLocationType),
            ),
            (
                "s3_location",
                "s3Location",
                autoboto.TypeInfo(S3ArtifactLocation),
            ),
        ]

    # The type of artifact in the location.
    type: "ArtifactLocationType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon S3 bucket that contains the artifact.
    s3_location: "S3ArtifactLocation" = dataclasses.field(
        default_factory=dict,
    )


class ArtifactLocationType(Enum):
    S3 = "S3"


@dataclasses.dataclass
class ArtifactRevision(autoboto.ShapeBase):
    """
    Represents revision details of an artifact.
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
                "revision_id",
                "revisionId",
                autoboto.TypeInfo(str),
            ),
            (
                "revision_change_identifier",
                "revisionChangeIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "revision_summary",
                "revisionSummary",
                autoboto.TypeInfo(str),
            ),
            (
                "created",
                "created",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "revision_url",
                "revisionUrl",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of an artifact. This name might be system-generated, such as
    # "MyApp", or might be defined by the user when an action is created.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The revision ID of the artifact.
    revision_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An additional identifier for a revision, such as a commit date or, for
    # artifacts stored in Amazon S3 buckets, the ETag value.
    revision_change_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Summary information about the most recent revision of the artifact. For
    # GitHub and AWS CodeCommit repositories, the commit message. For Amazon S3
    # buckets or actions, the user-provided content of a `codepipeline-artifact-
    # revision-summary` key specified in the object metadata.
    revision_summary: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time when the most recent revision of the artifact was
    # created, in timestamp format.
    created: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The commit ID for the artifact revision. For artifacts stored in GitHub or
    # AWS CodeCommit repositories, the commit ID is linked to a commit details
    # page.
    revision_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ArtifactStore(autoboto.ShapeBase):
    """
    The Amazon S3 bucket where artifacts are stored for the pipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(ArtifactStoreType),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(str),
            ),
            (
                "encryption_key",
                "encryptionKey",
                autoboto.TypeInfo(EncryptionKey),
            ),
        ]

    # The type of the artifact store, such as S3.
    type: "ArtifactStoreType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon S3 bucket used for storing the artifacts for a pipeline. You can
    # specify the name of an S3 bucket but not a folder within the bucket. A
    # folder to contain the pipeline artifacts is created for you based on the
    # name of the pipeline. You can use any Amazon S3 bucket in the same AWS
    # Region as the pipeline to store your pipeline artifacts.
    location: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The encryption key used to encrypt the data in the artifact store, such as
    # an AWS Key Management Service (AWS KMS) key. If this is undefined, the
    # default key for Amazon S3 is used.
    encryption_key: "EncryptionKey" = dataclasses.field(default_factory=dict, )


class ArtifactStoreType(Enum):
    S3 = "S3"


@dataclasses.dataclass
class BlockerDeclaration(autoboto.ShapeBase):
    """
    Reserved for future use.
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
                "type",
                "type",
                autoboto.TypeInfo(BlockerType),
            ),
        ]

    # Reserved for future use.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Reserved for future use.
    type: "BlockerType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class BlockerType(Enum):
    Schedule = "Schedule"


@dataclasses.dataclass
class CreateCustomActionTypeInput(autoboto.ShapeBase):
    """
    Represents the input of a CreateCustomActionType operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "category",
                "category",
                autoboto.TypeInfo(ActionCategory),
            ),
            (
                "provider",
                "provider",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(str),
            ),
            (
                "input_artifact_details",
                "inputArtifactDetails",
                autoboto.TypeInfo(ArtifactDetails),
            ),
            (
                "output_artifact_details",
                "outputArtifactDetails",
                autoboto.TypeInfo(ArtifactDetails),
            ),
            (
                "settings",
                "settings",
                autoboto.TypeInfo(ActionTypeSettings),
            ),
            (
                "configuration_properties",
                "configurationProperties",
                autoboto.TypeInfo(typing.List[ActionConfigurationProperty]),
            ),
        ]

    # The category of the custom action, such as a build action or a test action.

    # Although Source and Approval are listed as valid values, they are not
    # currently functional. These values are reserved for future use.
    category: "ActionCategory" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The provider of the service used in the custom action, such as AWS
    # CodeDeploy.
    provider: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version identifier of the custom action.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The details of the input artifact for the action, such as its commit ID.
    input_artifact_details: "ArtifactDetails" = dataclasses.field(
        default_factory=dict,
    )

    # The details of the output artifact of the action, such as its commit ID.
    output_artifact_details: "ArtifactDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Returns information about the settings for an action type.
    settings: "ActionTypeSettings" = dataclasses.field(default_factory=dict, )

    # The configuration properties for the custom action.

    # You can refer to a name in the configuration properties of the custom
    # action within the URL templates by following the format of {Config:name},
    # as long as the configuration property is both required and not secret. For
    # more information, see [Create a Custom Action for a
    # Pipeline](http://docs.aws.amazon.com/codepipeline/latest/userguide/how-to-
    # create-custom-action.html).
    configuration_properties: typing.List["ActionConfigurationProperty"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )


@dataclasses.dataclass
class CreateCustomActionTypeOutput(autoboto.OutputShapeBase):
    """
    Represents the output of a CreateCustomActionType operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "action_type",
                "actionType",
                autoboto.TypeInfo(ActionType),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Returns information about the details of an action type.
    action_type: "ActionType" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreatePipelineInput(autoboto.ShapeBase):
    """
    Represents the input of a CreatePipeline action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline",
                "pipeline",
                autoboto.TypeInfo(PipelineDeclaration),
            ),
        ]

    # Represents the structure of actions and stages to be performed in the
    # pipeline.
    pipeline: "PipelineDeclaration" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreatePipelineOutput(autoboto.OutputShapeBase):
    """
    Represents the output of a CreatePipeline action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipeline",
                "pipeline",
                autoboto.TypeInfo(PipelineDeclaration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Represents the structure of actions and stages to be performed in the
    # pipeline.
    pipeline: "PipelineDeclaration" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CurrentRevision(autoboto.ShapeBase):
    """
    Represents information about a current revision.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "revision",
                "revision",
                autoboto.TypeInfo(str),
            ),
            (
                "change_identifier",
                "changeIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "created",
                "created",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "revision_summary",
                "revisionSummary",
                autoboto.TypeInfo(str),
            ),
        ]

    # The revision ID of the current version of an artifact.
    revision: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The change identifier for the current revision.
    change_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time when the most recent revision of the artifact was
    # created, in timestamp format.
    created: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The summary of the most recent revision of the artifact.
    revision_summary: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteCustomActionTypeInput(autoboto.ShapeBase):
    """
    Represents the input of a DeleteCustomActionType operation. The custom action
    will be marked as deleted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "category",
                "category",
                autoboto.TypeInfo(ActionCategory),
            ),
            (
                "provider",
                "provider",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The category of the custom action that you want to delete, such as source
    # or deploy.
    category: "ActionCategory" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The provider of the service used in the custom action, such as AWS
    # CodeDeploy.
    provider: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version of the custom action to delete.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletePipelineInput(autoboto.ShapeBase):
    """
    Represents the input of a DeletePipeline action.
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

    # The name of the pipeline to be deleted.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteWebhookInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the webhook you want to delete.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteWebhookOutput(autoboto.OutputShapeBase):
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
class DeregisterWebhookWithThirdPartyInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "webhook_name",
                "webhookName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the webhook you want to deregister.
    webhook_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterWebhookWithThirdPartyOutput(autoboto.OutputShapeBase):
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
class DisableStageTransitionInput(autoboto.ShapeBase):
    """
    Represents the input of a DisableStageTransition action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                autoboto.TypeInfo(str),
            ),
            (
                "transition_type",
                "transitionType",
                autoboto.TypeInfo(StageTransitionType),
            ),
            (
                "reason",
                "reason",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the pipeline in which you want to disable the flow of artifacts
    # from one stage to another.
    pipeline_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the stage where you want to disable the inbound or outbound
    # transition of artifacts.
    stage_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies whether artifacts will be prevented from transitioning into the
    # stage and being processed by the actions in that stage (inbound), or
    # prevented from transitioning from the stage after they have been processed
    # by the actions in that stage (outbound).
    transition_type: "StageTransitionType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The reason given to the user why a stage is disabled, such as waiting for
    # manual approval or manual tests. This message is displayed in the pipeline
    # console UI.
    reason: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnableStageTransitionInput(autoboto.ShapeBase):
    """
    Represents the input of an EnableStageTransition action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                autoboto.TypeInfo(str),
            ),
            (
                "transition_type",
                "transitionType",
                autoboto.TypeInfo(StageTransitionType),
            ),
        ]

    # The name of the pipeline in which you want to enable the flow of artifacts
    # from one stage to another.
    pipeline_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the stage where you want to enable the transition of artifacts,
    # either into the stage (inbound) or from that stage to the next stage
    # (outbound).
    stage_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies whether artifacts will be allowed to enter the stage and be
    # processed by the actions in that stage (inbound) or whether already-
    # processed artifacts will be allowed to transition to the next stage
    # (outbound).
    transition_type: "StageTransitionType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EncryptionKey(autoboto.ShapeBase):
    """
    Represents information about the key used to encrypt data in the artifact store,
    such as an AWS Key Management Service (AWS KMS) key.
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
                "type",
                "type",
                autoboto.TypeInfo(EncryptionKeyType),
            ),
        ]

    # The ID used to identify the key. For an AWS KMS key, this is the key ID or
    # key ARN.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of encryption key, such as an AWS Key Management Service (AWS KMS)
    # key. When creating or updating a pipeline, the value must be set to 'KMS'.
    type: "EncryptionKeyType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class EncryptionKeyType(Enum):
    KMS = "KMS"


@dataclasses.dataclass
class ErrorDetails(autoboto.ShapeBase):
    """
    Represents information about an error in AWS CodePipeline.
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

    # The system ID or error number code of the error.
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The text of the error message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExecutionDetails(autoboto.ShapeBase):
    """
    The details of the actions taken and results produced on an artifact as it
    passes through stages in the pipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "summary",
                "summary",
                autoboto.TypeInfo(str),
            ),
            (
                "external_execution_id",
                "externalExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "percent_complete",
                "percentComplete",
                autoboto.TypeInfo(int),
            ),
        ]

    # The summary of the current status of the actions.
    summary: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The system-generated unique ID of this action used to identify this job
    # worker in any external systems, such as AWS CodeDeploy.
    external_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The percentage of work completed on the action, represented on a scale of
    # zero to one hundred percent.
    percent_complete: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FailureDetails(autoboto.ShapeBase):
    """
    Represents information about failure details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(FailureType),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "external_execution_id",
                "externalExecutionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of the failure.
    type: "FailureType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The message about the failure.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The external ID of the run of the action that failed.
    external_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class FailureType(Enum):
    JobFailed = "JobFailed"
    ConfigurationError = "ConfigurationError"
    PermissionError = "PermissionError"
    RevisionOutOfSync = "RevisionOutOfSync"
    RevisionUnavailable = "RevisionUnavailable"
    SystemUnavailable = "SystemUnavailable"


@dataclasses.dataclass
class GetJobDetailsInput(autoboto.ShapeBase):
    """
    Represents the input of a GetJobDetails action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique system-generated ID for the job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetJobDetailsOutput(autoboto.OutputShapeBase):
    """
    Represents the output of a GetJobDetails action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_details",
                "jobDetails",
                autoboto.TypeInfo(JobDetails),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details of the job.

    # If AWSSessionCredentials is used, a long-running job can call GetJobDetails
    # again to obtain new credentials.
    job_details: "JobDetails" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetPipelineExecutionInput(autoboto.ShapeBase):
    """
    Represents the input of a GetPipelineExecution action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
            (
                "pipeline_execution_id",
                "pipelineExecutionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the pipeline about which you want to get execution details.
    pipeline_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the pipeline execution about which you want to get execution
    # details.
    pipeline_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetPipelineExecutionOutput(autoboto.OutputShapeBase):
    """
    Represents the output of a GetPipelineExecution action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipeline_execution",
                "pipelineExecution",
                autoboto.TypeInfo(PipelineExecution),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Represents information about the execution of a pipeline.
    pipeline_execution: "PipelineExecution" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetPipelineInput(autoboto.ShapeBase):
    """
    Represents the input of a GetPipeline action.
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
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the pipeline for which you want to get information. Pipeline
    # names must be unique under an Amazon Web Services (AWS) user account.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version number of the pipeline. If you do not specify a version,
    # defaults to the most current version.
    version: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPipelineOutput(autoboto.OutputShapeBase):
    """
    Represents the output of a GetPipeline action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipeline",
                "pipeline",
                autoboto.TypeInfo(PipelineDeclaration),
            ),
            (
                "metadata",
                "metadata",
                autoboto.TypeInfo(PipelineMetadata),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Represents the structure of actions and stages to be performed in the
    # pipeline.
    pipeline: "PipelineDeclaration" = dataclasses.field(default_factory=dict, )

    # Represents the pipeline metadata information returned as part of the output
    # of a GetPipeline action.
    metadata: "PipelineMetadata" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetPipelineStateInput(autoboto.ShapeBase):
    """
    Represents the input of a GetPipelineState action.
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

    # The name of the pipeline about which you want to get information.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPipelineStateOutput(autoboto.OutputShapeBase):
    """
    Represents the output of a GetPipelineState action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
            (
                "pipeline_version",
                "pipelineVersion",
                autoboto.TypeInfo(int),
            ),
            (
                "stage_states",
                "stageStates",
                autoboto.TypeInfo(typing.List[StageState]),
            ),
            (
                "created",
                "created",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "updated",
                "updated",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the pipeline for which you want to get the state.
    pipeline_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version number of the pipeline.

    # A newly-created pipeline is always assigned a version number of `1`.
    pipeline_version: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of the pipeline stage output information, including stage name,
    # state, most recent run details, whether the stage is disabled, and other
    # data.
    stage_states: typing.List["StageState"] = dataclasses.field(
        default_factory=list,
    )

    # The date and time the pipeline was created, in timestamp format.
    created: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time the pipeline was last updated, in timestamp format.
    updated: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetThirdPartyJobDetailsInput(autoboto.ShapeBase):
    """
    Represents the input of a GetThirdPartyJobDetails action.
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
                "client_token",
                "clientToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique system-generated ID used for identifying the job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The clientToken portion of the clientId and clientToken pair used to verify
    # that the calling entity is allowed access to the job and its details.
    client_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetThirdPartyJobDetailsOutput(autoboto.OutputShapeBase):
    """
    Represents the output of a GetThirdPartyJobDetails action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_details",
                "jobDetails",
                autoboto.TypeInfo(ThirdPartyJobDetails),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details of the job, including any protected values defined for the job.
    job_details: "ThirdPartyJobDetails" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class InputArtifact(autoboto.ShapeBase):
    """
    Represents information about an artifact to be worked on, such as a test or
    build artifact.
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

    # The name of the artifact to be worked on, for example, "My App".

    # The input artifact of an action must exactly match the output artifact
    # declared in a preceding action, but the input artifact does not have to be
    # the next action in strict sequence from the action that provided the output
    # artifact. Actions in parallel can declare different output artifacts, which
    # are in turn consumed by different following actions.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidActionDeclarationException(autoboto.ShapeBase):
    """
    The specified action declaration was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidApprovalTokenException(autoboto.ShapeBase):
    """
    The approval request already received a response or has expired.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidBlockerDeclarationException(autoboto.ShapeBase):
    """
    Reserved for future use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidClientTokenException(autoboto.ShapeBase):
    """
    The client token was specified in an invalid format
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidJobException(autoboto.ShapeBase):
    """
    The specified job was specified in an invalid format or cannot be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidJobStateException(autoboto.ShapeBase):
    """
    The specified job state was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidNextTokenException(autoboto.ShapeBase):
    """
    The next token was specified in an invalid format. Make sure that the next token
    you provided is the token returned by a previous call.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidNonceException(autoboto.ShapeBase):
    """
    The specified nonce was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidStageDeclarationException(autoboto.ShapeBase):
    """
    The specified stage declaration was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidStructureException(autoboto.ShapeBase):
    """
    The specified structure was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidWebhookAuthenticationParametersException(autoboto.ShapeBase):
    """
    The specified authentication type is in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidWebhookFilterPatternException(autoboto.ShapeBase):
    """
    The specified event filter rule is in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Job(autoboto.ShapeBase):
    """
    Represents information about a job.
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
                "data",
                "data",
                autoboto.TypeInfo(JobData),
            ),
            (
                "nonce",
                "nonce",
                autoboto.TypeInfo(str),
            ),
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique system-generated ID of the job.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Additional data about a job.
    data: "JobData" = dataclasses.field(default_factory=dict, )

    # A system-generated random number that AWS CodePipeline uses to ensure that
    # the job is being worked on by only one job worker. Use this number in an
    # AcknowledgeJob request.
    nonce: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the AWS account to use when performing the job.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class JobData(autoboto.ShapeBase):
    """
    Represents additional information about a job required for a job worker to
    complete the job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_type_id",
                "actionTypeId",
                autoboto.TypeInfo(ActionTypeId),
            ),
            (
                "action_configuration",
                "actionConfiguration",
                autoboto.TypeInfo(ActionConfiguration),
            ),
            (
                "pipeline_context",
                "pipelineContext",
                autoboto.TypeInfo(PipelineContext),
            ),
            (
                "input_artifacts",
                "inputArtifacts",
                autoboto.TypeInfo(typing.List[Artifact]),
            ),
            (
                "output_artifacts",
                "outputArtifacts",
                autoboto.TypeInfo(typing.List[Artifact]),
            ),
            (
                "artifact_credentials",
                "artifactCredentials",
                autoboto.TypeInfo(AWSSessionCredentials),
            ),
            (
                "continuation_token",
                "continuationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "encryption_key",
                "encryptionKey",
                autoboto.TypeInfo(EncryptionKey),
            ),
        ]

    # Represents information about an action type.
    action_type_id: "ActionTypeId" = dataclasses.field(default_factory=dict, )

    # Represents information about an action configuration.
    action_configuration: "ActionConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # Represents information about a pipeline to a job worker.
    pipeline_context: "PipelineContext" = dataclasses.field(
        default_factory=dict,
    )

    # The artifact supplied to the job.
    input_artifacts: typing.List["Artifact"] = dataclasses.field(
        default_factory=list,
    )

    # The output of the job.
    output_artifacts: typing.List["Artifact"] = dataclasses.field(
        default_factory=list,
    )

    # Represents an AWS session credentials object. These credentials are
    # temporary credentials that are issued by AWS Secure Token Service (STS).
    # They can be used to access input and output artifacts in the Amazon S3
    # bucket used to store artifact for the pipeline in AWS CodePipeline.
    artifact_credentials: "AWSSessionCredentials" = dataclasses.field(
        default_factory=dict,
    )

    # A system-generated token, such as a AWS CodeDeploy deployment ID, that a
    # job requires in order to continue the job asynchronously.
    continuation_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Represents information about the key used to encrypt data in the artifact
    # store, such as an AWS Key Management Service (AWS KMS) key.
    encryption_key: "EncryptionKey" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class JobDetails(autoboto.ShapeBase):
    """
    Represents information about the details of a job.
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
                "data",
                "data",
                autoboto.TypeInfo(JobData),
            ),
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique system-generated ID of the job.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Represents additional information about a job required for a job worker to
    # complete the job.
    data: "JobData" = dataclasses.field(default_factory=dict, )

    # The AWS account ID associated with the job.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class JobNotFoundException(autoboto.ShapeBase):
    """
    The specified job was specified in an invalid format or cannot be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class JobStatus(Enum):
    Created = "Created"
    Queued = "Queued"
    Dispatched = "Dispatched"
    InProgress = "InProgress"
    TimedOut = "TimedOut"
    Succeeded = "Succeeded"
    Failed = "Failed"


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    The number of pipelines associated with the AWS account has exceeded the limit
    allowed for the account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListActionTypesInput(autoboto.ShapeBase):
    """
    Represents the input of a ListActionTypes action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_owner_filter",
                "actionOwnerFilter",
                autoboto.TypeInfo(ActionOwner),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Filters the list of action types to those created by a specified entity.
    action_owner_filter: "ActionOwner" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An identifier that was returned from the previous list action types call,
    # which can be used to return the next set of action types in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListActionTypesOutput(autoboto.OutputShapeBase):
    """
    Represents the output of a ListActionTypes action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "action_types",
                "actionTypes",
                autoboto.TypeInfo(typing.List[ActionType]),
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

    # Provides details of the action types.
    action_types: typing.List["ActionType"] = dataclasses.field(
        default_factory=list,
    )

    # If the amount of returned information is significantly large, an identifier
    # is also returned which can be used in a subsequent list action types call
    # to return the next set of action types in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPipelineExecutionsInput(autoboto.ShapeBase):
    """
    Represents the input of a ListPipelineExecutions action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
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
        ]

    # The name of the pipeline for which you want to get execution summary
    # information.
    pipeline_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to return in a single call. To retrieve the
    # remaining results, make another call with the returned nextToken value. The
    # available pipeline execution history is limited to the most recent 12
    # months, based on pipeline execution start times. Default value is 100.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token that was returned from the previous ListPipelineExecutions call,
    # which can be used to return the next set of pipeline executions in the
    # list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPipelineExecutionsOutput(autoboto.OutputShapeBase):
    """
    Represents the output of a ListPipelineExecutions action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipeline_execution_summaries",
                "pipelineExecutionSummaries",
                autoboto.TypeInfo(typing.List[PipelineExecutionSummary]),
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

    # A list of executions in the history of a pipeline.
    pipeline_execution_summaries: typing.List["PipelineExecutionSummary"
                                             ] = dataclasses.field(
                                                 default_factory=list,
                                             )

    # A token that can be used in the next ListPipelineExecutions call. To view
    # all items in the list, continue to call this operation with each subsequent
    # token until no more nextToken values are returned.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPipelinesInput(autoboto.ShapeBase):
    """
    Represents the input of a ListPipelines action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An identifier that was returned from the previous list pipelines call,
    # which can be used to return the next set of pipelines in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPipelinesOutput(autoboto.OutputShapeBase):
    """
    Represents the output of a ListPipelines action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipelines",
                "pipelines",
                autoboto.TypeInfo(typing.List[PipelineSummary]),
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

    # The list of pipelines.
    pipelines: typing.List["PipelineSummary"] = dataclasses.field(
        default_factory=list,
    )

    # If the amount of returned information is significantly large, an identifier
    # is also returned which can be used in a subsequent list pipelines call to
    # return the next set of pipelines in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListWebhookItem(autoboto.ShapeBase):
    """
    The detail returned for each webhook after listing webhooks, such as the webhook
    URL, the webhook name, and the webhook ARN.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "definition",
                "definition",
                autoboto.TypeInfo(WebhookDefinition),
            ),
            (
                "url",
                "url",
                autoboto.TypeInfo(str),
            ),
            (
                "error_message",
                "errorMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "error_code",
                "errorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "last_triggered",
                "lastTriggered",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The detail returned for each webhook, such as the webhook authentication
    # type and filter rules.
    definition: "WebhookDefinition" = dataclasses.field(default_factory=dict, )

    # A unique URL generated by CodePipeline. When a POST request is made to this
    # URL, the defined pipeline is started as long as the body of the post
    # request satisfies the defined authentication and filtering conditions.
    # Deleting and re-creating a webhook will make the old URL invalid and
    # generate a new URL.
    url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The text of the error message about the webhook.
    error_message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number code of the error.
    error_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date and time a webhook was last successfully triggered, in timestamp
    # format.
    last_triggered: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the webhook.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListWebhooksInput(autoboto.ShapeBase):
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

    # The token that was returned from the previous ListWebhooks call, which can
    # be used to return the next set of webhooks in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to return in a single call. To retrieve the
    # remaining results, make another call with the returned nextToken value.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListWebhooksOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "webhooks",
                "webhooks",
                autoboto.TypeInfo(typing.List[ListWebhookItem]),
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

    # The JSON detail returned for each webhook in the list output for the
    # ListWebhooks call.
    webhooks: typing.List["ListWebhookItem"] = dataclasses.field(
        default_factory=list,
    )

    # If the amount of returned information is significantly large, an identifier
    # is also returned and can be used in a subsequent ListWebhooks call to
    # return the next set of webhooks in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotLatestPipelineExecutionException(autoboto.ShapeBase):
    """
    The stage has failed in a later run of the pipeline and the pipelineExecutionId
    associated with the request is out of date.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class OutputArtifact(autoboto.ShapeBase):
    """
    Represents information about the output of an action.
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

    # The name of the output of an artifact, such as "My App".

    # The input artifact of an action must exactly match the output artifact
    # declared in a preceding action, but the input artifact does not have to be
    # the next action in strict sequence from the action that provided the output
    # artifact. Actions in parallel can declare different output artifacts, which
    # are in turn consumed by different following actions.

    # Output artifact names must be unique within a pipeline.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PipelineContext(autoboto.ShapeBase):
    """
    Represents information about a pipeline to a job worker.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
            (
                "stage",
                "stage",
                autoboto.TypeInfo(StageContext),
            ),
            (
                "action",
                "action",
                autoboto.TypeInfo(ActionContext),
            ),
        ]

    # The name of the pipeline. This is a user-specified value. Pipeline names
    # must be unique across all pipeline names under an Amazon Web Services
    # account.
    pipeline_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stage of the pipeline.
    stage: "StageContext" = dataclasses.field(default_factory=dict, )

    # The context of an action to a job worker within the stage of a pipeline.
    action: "ActionContext" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PipelineDeclaration(autoboto.ShapeBase):
    """
    Represents the structure of actions and stages to be performed in the pipeline.
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
                "role_arn",
                "roleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "artifact_store",
                "artifactStore",
                autoboto.TypeInfo(ArtifactStore),
            ),
            (
                "stages",
                "stages",
                autoboto.TypeInfo(typing.List[StageDeclaration]),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the action to be performed.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for AWS CodePipeline to use to either
    # perform actions with no actionRoleArn, or to use to assume roles for
    # actions with an actionRoleArn.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Represents information about the Amazon S3 bucket where artifacts are
    # stored for the pipeline.
    artifact_store: "ArtifactStore" = dataclasses.field(default_factory=dict, )

    # The stage in which to perform the action.
    stages: typing.List["StageDeclaration"] = dataclasses.field(
        default_factory=list,
    )

    # The version number of the pipeline. A new pipeline always has a version
    # number of 1. This number is automatically incremented when a pipeline is
    # updated.
    version: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PipelineExecution(autoboto.ShapeBase):
    """
    Represents information about an execution of a pipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
            (
                "pipeline_version",
                "pipelineVersion",
                autoboto.TypeInfo(int),
            ),
            (
                "pipeline_execution_id",
                "pipelineExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(PipelineExecutionStatus),
            ),
            (
                "artifact_revisions",
                "artifactRevisions",
                autoboto.TypeInfo(typing.List[ArtifactRevision]),
            ),
        ]

    # The name of the pipeline that was executed.
    pipeline_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version number of the pipeline that was executed.
    pipeline_version: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the pipeline execution.
    pipeline_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the pipeline execution.

    #   * InProgress: The pipeline execution is currently running.

    #   * Succeeded: The pipeline execution was completed successfully.

    #   * Superseded: While this pipeline execution was waiting for the next stage to be completed, a newer pipeline execution advanced and continued through the pipeline instead.

    #   * Failed: The pipeline execution was not completed successfully.
    status: "PipelineExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of ArtifactRevision objects included in a pipeline execution.
    artifact_revisions: typing.List["ArtifactRevision"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class PipelineExecutionNotFoundException(autoboto.ShapeBase):
    """
    The pipeline execution was specified in an invalid format or cannot be found, or
    an execution ID does not belong to the specified pipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class PipelineExecutionStatus(Enum):
    InProgress = "InProgress"
    Succeeded = "Succeeded"
    Superseded = "Superseded"
    Failed = "Failed"


@dataclasses.dataclass
class PipelineExecutionSummary(autoboto.ShapeBase):
    """
    Summary information about a pipeline execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_execution_id",
                "pipelineExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(PipelineExecutionStatus),
            ),
            (
                "start_time",
                "startTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "source_revisions",
                "sourceRevisions",
                autoboto.TypeInfo(typing.List[SourceRevision]),
            ),
        ]

    # The ID of the pipeline execution.
    pipeline_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the pipeline execution.

    #   * InProgress: The pipeline execution is currently running.

    #   * Succeeded: The pipeline execution was completed successfully.

    #   * Superseded: While this pipeline execution was waiting for the next stage to be completed, a newer pipeline execution advanced and continued through the pipeline instead.

    #   * Failed: The pipeline execution was not completed successfully.
    status: "PipelineExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time when the pipeline execution began, in timestamp format.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time of the last change to the pipeline execution, in
    # timestamp format.
    last_update_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    source_revisions: typing.List["SourceRevision"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class PipelineMetadata(autoboto.ShapeBase):
    """
    Information about a pipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_arn",
                "pipelineArn",
                autoboto.TypeInfo(str),
            ),
            (
                "created",
                "created",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "updated",
                "updated",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Resource Name (ARN) of the pipeline.
    pipeline_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date and time the pipeline was created, in timestamp format.
    created: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time the pipeline was last updated, in timestamp format.
    updated: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PipelineNameInUseException(autoboto.ShapeBase):
    """
    The specified pipeline name is already in use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PipelineNotFoundException(autoboto.ShapeBase):
    """
    The specified pipeline was specified in an invalid format or cannot be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PipelineSummary(autoboto.ShapeBase):
    """
    Returns a summary of a pipeline.
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
                autoboto.TypeInfo(int),
            ),
            (
                "created",
                "created",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "updated",
                "updated",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the pipeline.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version number of the pipeline.
    version: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date and time the pipeline was created, in timestamp format.
    created: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time of the last update to the pipeline, in timestamp format.
    updated: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PipelineVersionNotFoundException(autoboto.ShapeBase):
    """
    The specified pipeline version was specified in an invalid format or cannot be
    found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PollForJobsInput(autoboto.ShapeBase):
    """
    Represents the input of a PollForJobs action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_type_id",
                "actionTypeId",
                autoboto.TypeInfo(ActionTypeId),
            ),
            (
                "max_batch_size",
                "maxBatchSize",
                autoboto.TypeInfo(int),
            ),
            (
                "query_param",
                "queryParam",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Represents information about an action type.
    action_type_id: "ActionTypeId" = dataclasses.field(default_factory=dict, )

    # The maximum number of jobs to return in a poll for jobs call.
    max_batch_size: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A map of property names and values. For an action type with no queryable
    # properties, this value must be null or an empty map. For an action type
    # with a queryable property, you must supply that property as a key in the
    # map. Only jobs whose action configuration matches the mapped value will be
    # returned.
    query_param: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PollForJobsOutput(autoboto.OutputShapeBase):
    """
    Represents the output of a PollForJobs action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "jobs",
                "jobs",
                autoboto.TypeInfo(typing.List[Job]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the jobs to take action on.
    jobs: typing.List["Job"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class PollForThirdPartyJobsInput(autoboto.ShapeBase):
    """
    Represents the input of a PollForThirdPartyJobs action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_type_id",
                "actionTypeId",
                autoboto.TypeInfo(ActionTypeId),
            ),
            (
                "max_batch_size",
                "maxBatchSize",
                autoboto.TypeInfo(int),
            ),
        ]

    # Represents information about an action type.
    action_type_id: "ActionTypeId" = dataclasses.field(default_factory=dict, )

    # The maximum number of jobs to return in a poll for jobs call.
    max_batch_size: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PollForThirdPartyJobsOutput(autoboto.OutputShapeBase):
    """
    Represents the output of a PollForThirdPartyJobs action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "jobs",
                "jobs",
                autoboto.TypeInfo(typing.List[ThirdPartyJob]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the jobs to take action on.
    jobs: typing.List["ThirdPartyJob"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class PutActionRevisionInput(autoboto.ShapeBase):
    """
    Represents the input of a PutActionRevision action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                autoboto.TypeInfo(str),
            ),
            (
                "action_name",
                "actionName",
                autoboto.TypeInfo(str),
            ),
            (
                "action_revision",
                "actionRevision",
                autoboto.TypeInfo(ActionRevision),
            ),
        ]

    # The name of the pipeline that will start processing the revision to the
    # source.
    pipeline_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the stage that contains the action that will act upon the
    # revision.
    stage_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the action that will process the revision.
    action_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Represents information about the version (or revision) of an action.
    action_revision: "ActionRevision" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutActionRevisionOutput(autoboto.OutputShapeBase):
    """
    Represents the output of a PutActionRevision action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "new_revision",
                "newRevision",
                autoboto.TypeInfo(bool),
            ),
            (
                "pipeline_execution_id",
                "pipelineExecutionId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the artifact revision was previously used in an execution
    # of the specified pipeline.
    new_revision: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the current workflow state of the pipeline.
    pipeline_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutApprovalResultInput(autoboto.ShapeBase):
    """
    Represents the input of a PutApprovalResult action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                autoboto.TypeInfo(str),
            ),
            (
                "action_name",
                "actionName",
                autoboto.TypeInfo(str),
            ),
            (
                "result",
                "result",
                autoboto.TypeInfo(ApprovalResult),
            ),
            (
                "token",
                "token",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the pipeline that contains the action.
    pipeline_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the stage that contains the action.
    stage_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the action for which approval is requested.
    action_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Represents information about the result of the approval request.
    result: "ApprovalResult" = dataclasses.field(default_factory=dict, )

    # The system-generated token used to identify a unique approval request. The
    # token for each open approval request can be obtained using the
    # GetPipelineState action and is used to validate that the approval request
    # corresponding to this token is still valid.
    token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutApprovalResultOutput(autoboto.OutputShapeBase):
    """
    Represents the output of a PutApprovalResult action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "approved_at",
                "approvedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp showing when the approval or rejection was submitted.
    approved_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutJobFailureResultInput(autoboto.ShapeBase):
    """
    Represents the input of a PutJobFailureResult action.
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
                "failure_details",
                "failureDetails",
                autoboto.TypeInfo(FailureDetails),
            ),
        ]

    # The unique system-generated ID of the job that failed. This is the same ID
    # returned from PollForJobs.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The details about the failure of a job.
    failure_details: "FailureDetails" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutJobSuccessResultInput(autoboto.ShapeBase):
    """
    Represents the input of a PutJobSuccessResult action.
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
                "current_revision",
                "currentRevision",
                autoboto.TypeInfo(CurrentRevision),
            ),
            (
                "continuation_token",
                "continuationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_details",
                "executionDetails",
                autoboto.TypeInfo(ExecutionDetails),
            ),
        ]

    # The unique system-generated ID of the job that succeeded. This is the same
    # ID returned from PollForJobs.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the current revision of the artifact successfully worked upon by
    # the job.
    current_revision: "CurrentRevision" = dataclasses.field(
        default_factory=dict,
    )

    # A token generated by a job worker, such as an AWS CodeDeploy deployment ID,
    # that a successful job provides to identify a custom action in progress.
    # Future jobs will use this token in order to identify the running instance
    # of the action. It can be reused to return additional information about the
    # progress of the custom action. When the action is complete, no continuation
    # token should be supplied.
    continuation_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The execution details of the successful job, such as the actions taken by
    # the job worker.
    execution_details: "ExecutionDetails" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutThirdPartyJobFailureResultInput(autoboto.ShapeBase):
    """
    Represents the input of a PutThirdPartyJobFailureResult action.
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
                "client_token",
                "clientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "failure_details",
                "failureDetails",
                autoboto.TypeInfo(FailureDetails),
            ),
        ]

    # The ID of the job that failed. This is the same ID returned from
    # PollForThirdPartyJobs.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The clientToken portion of the clientId and clientToken pair used to verify
    # that the calling entity is allowed access to the job and its details.
    client_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Represents information about failure details.
    failure_details: "FailureDetails" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutThirdPartyJobSuccessResultInput(autoboto.ShapeBase):
    """
    Represents the input of a PutThirdPartyJobSuccessResult action.
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
                "client_token",
                "clientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "current_revision",
                "currentRevision",
                autoboto.TypeInfo(CurrentRevision),
            ),
            (
                "continuation_token",
                "continuationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_details",
                "executionDetails",
                autoboto.TypeInfo(ExecutionDetails),
            ),
        ]

    # The ID of the job that successfully completed. This is the same ID returned
    # from PollForThirdPartyJobs.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The clientToken portion of the clientId and clientToken pair used to verify
    # that the calling entity is allowed access to the job and its details.
    client_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Represents information about a current revision.
    current_revision: "CurrentRevision" = dataclasses.field(
        default_factory=dict,
    )

    # A token generated by a job worker, such as an AWS CodeDeploy deployment ID,
    # that a successful job provides to identify a partner action in progress.
    # Future jobs will use this token in order to identify the running instance
    # of the action. It can be reused to return additional information about the
    # progress of the partner action. When the action is complete, no
    # continuation token should be supplied.
    continuation_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details of the actions taken and results produced on an artifact as it
    # passes through stages in the pipeline.
    execution_details: "ExecutionDetails" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutWebhookInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "webhook",
                "webhook",
                autoboto.TypeInfo(WebhookDefinition),
            ),
        ]

    # The detail provided in an input file to create the webhook, such as the
    # webhook name, the pipeline name, and the action name. Give the webhook a
    # unique name which identifies the webhook being defined. You may choose to
    # name the webhook after the pipeline and action it targets so that you can
    # easily recognize what it's used for later.
    webhook: "WebhookDefinition" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PutWebhookOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "webhook",
                "webhook",
                autoboto.TypeInfo(ListWebhookItem),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The detail returned from creating the webhook, such as the webhook name,
    # webhook URL, and webhook ARN.
    webhook: "ListWebhookItem" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class RegisterWebhookWithThirdPartyInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "webhook_name",
                "webhookName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of an existing webhook created with PutWebhook to register with a
    # supported third party.
    webhook_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterWebhookWithThirdPartyOutput(autoboto.OutputShapeBase):
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
class RetryStageExecutionInput(autoboto.ShapeBase):
    """
    Represents the input of a RetryStageExecution action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                autoboto.TypeInfo(str),
            ),
            (
                "stage_name",
                "stageName",
                autoboto.TypeInfo(str),
            ),
            (
                "pipeline_execution_id",
                "pipelineExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "retry_mode",
                "retryMode",
                autoboto.TypeInfo(StageRetryMode),
            ),
        ]

    # The name of the pipeline that contains the failed stage.
    pipeline_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the failed stage to be retried.
    stage_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the pipeline execution in the failed stage to be retried. Use the
    # GetPipelineState action to retrieve the current pipelineExecutionId of the
    # failed stage
    pipeline_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The scope of the retry attempt. Currently, the only supported value is
    # FAILED_ACTIONS.
    retry_mode: "StageRetryMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RetryStageExecutionOutput(autoboto.OutputShapeBase):
    """
    Represents the output of a RetryStageExecution action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipeline_execution_id",
                "pipelineExecutionId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the current workflow execution in the failed stage.
    pipeline_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class S3ArtifactLocation(autoboto.ShapeBase):
    """
    The location of the Amazon S3 bucket that contains a revision.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket_name",
                "bucketName",
                autoboto.TypeInfo(str),
            ),
            (
                "object_key",
                "objectKey",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the Amazon S3 bucket.
    bucket_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The key of the object in the Amazon S3 bucket, which uniquely identifies
    # the object in the bucket.
    object_key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SourceRevision(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_name",
                "actionName",
                autoboto.TypeInfo(str),
            ),
            (
                "revision_id",
                "revisionId",
                autoboto.TypeInfo(str),
            ),
            (
                "revision_summary",
                "revisionSummary",
                autoboto.TypeInfo(str),
            ),
            (
                "revision_url",
                "revisionUrl",
                autoboto.TypeInfo(str),
            ),
        ]

    action_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    revision_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    revision_summary: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    revision_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StageContext(autoboto.ShapeBase):
    """
    Represents information about a stage to a job worker.
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

    # The name of the stage.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StageDeclaration(autoboto.ShapeBase):
    """
    Represents information about a stage and its definition.
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
                "actions",
                "actions",
                autoboto.TypeInfo(typing.List[ActionDeclaration]),
            ),
            (
                "blockers",
                "blockers",
                autoboto.TypeInfo(typing.List[BlockerDeclaration]),
            ),
        ]

    # The name of the stage.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The actions included in a stage.
    actions: typing.List["ActionDeclaration"] = dataclasses.field(
        default_factory=list,
    )

    # Reserved for future use.
    blockers: typing.List["BlockerDeclaration"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class StageExecution(autoboto.ShapeBase):
    """
    Represents information about the run of a stage.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_execution_id",
                "pipelineExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(StageExecutionStatus),
            ),
        ]

    # The ID of the pipeline execution associated with the stage.
    pipeline_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the stage, or for a completed stage, the last status of the
    # stage.
    status: "StageExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class StageExecutionStatus(Enum):
    InProgress = "InProgress"
    Failed = "Failed"
    Succeeded = "Succeeded"


@dataclasses.dataclass
class StageNotFoundException(autoboto.ShapeBase):
    """
    The specified stage was specified in an invalid format or cannot be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StageNotRetryableException(autoboto.ShapeBase):
    """
    The specified stage can't be retried because the pipeline structure or stage
    state changed after the stage was not completed; the stage contains no failed
    actions; one or more actions are still in progress; or another retry attempt is
    already in progress.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class StageRetryMode(Enum):
    FAILED_ACTIONS = "FAILED_ACTIONS"


@dataclasses.dataclass
class StageState(autoboto.ShapeBase):
    """
    Represents information about the state of the stage.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stage_name",
                "stageName",
                autoboto.TypeInfo(str),
            ),
            (
                "inbound_transition_state",
                "inboundTransitionState",
                autoboto.TypeInfo(TransitionState),
            ),
            (
                "action_states",
                "actionStates",
                autoboto.TypeInfo(typing.List[ActionState]),
            ),
            (
                "latest_execution",
                "latestExecution",
                autoboto.TypeInfo(StageExecution),
            ),
        ]

    # The name of the stage.
    stage_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The state of the inbound transition, which is either enabled or disabled.
    inbound_transition_state: "TransitionState" = dataclasses.field(
        default_factory=dict,
    )

    # The state of the stage.
    action_states: typing.List["ActionState"] = dataclasses.field(
        default_factory=list,
    )

    # Information about the latest execution in the stage, including its ID and
    # status.
    latest_execution: "StageExecution" = dataclasses.field(
        default_factory=dict,
    )


class StageTransitionType(Enum):
    Inbound = "Inbound"
    Outbound = "Outbound"


@dataclasses.dataclass
class StartPipelineExecutionInput(autoboto.ShapeBase):
    """
    Represents the input of a StartPipelineExecution action.
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

    # The name of the pipeline to start.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartPipelineExecutionOutput(autoboto.OutputShapeBase):
    """
    Represents the output of a StartPipelineExecution action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipeline_execution_id",
                "pipelineExecutionId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The unique system-generated ID of the pipeline execution that was started.
    pipeline_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ThirdPartyJob(autoboto.ShapeBase):
    """
    A response to a PollForThirdPartyJobs request returned by AWS CodePipeline when
    there is a job to be worked upon by a partner action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_id",
                "clientId",
                autoboto.TypeInfo(str),
            ),
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The clientToken portion of the clientId and clientToken pair used to verify
    # that the calling entity is allowed access to the job and its details.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier used to identify the job in AWS CodePipeline.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ThirdPartyJobData(autoboto.ShapeBase):
    """
    Represents information about the job data for a partner action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_type_id",
                "actionTypeId",
                autoboto.TypeInfo(ActionTypeId),
            ),
            (
                "action_configuration",
                "actionConfiguration",
                autoboto.TypeInfo(ActionConfiguration),
            ),
            (
                "pipeline_context",
                "pipelineContext",
                autoboto.TypeInfo(PipelineContext),
            ),
            (
                "input_artifacts",
                "inputArtifacts",
                autoboto.TypeInfo(typing.List[Artifact]),
            ),
            (
                "output_artifacts",
                "outputArtifacts",
                autoboto.TypeInfo(typing.List[Artifact]),
            ),
            (
                "artifact_credentials",
                "artifactCredentials",
                autoboto.TypeInfo(AWSSessionCredentials),
            ),
            (
                "continuation_token",
                "continuationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "encryption_key",
                "encryptionKey",
                autoboto.TypeInfo(EncryptionKey),
            ),
        ]

    # Represents information about an action type.
    action_type_id: "ActionTypeId" = dataclasses.field(default_factory=dict, )

    # Represents information about an action configuration.
    action_configuration: "ActionConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # Represents information about a pipeline to a job worker.
    pipeline_context: "PipelineContext" = dataclasses.field(
        default_factory=dict,
    )

    # The name of the artifact that will be worked upon by the action, if any.
    # This name might be system-generated, such as "MyApp", or might be defined
    # by the user when the action is created. The input artifact name must match
    # the name of an output artifact generated by an action in an earlier action
    # or stage of the pipeline.
    input_artifacts: typing.List["Artifact"] = dataclasses.field(
        default_factory=list,
    )

    # The name of the artifact that will be the result of the action, if any.
    # This name might be system-generated, such as "MyBuiltApp", or might be
    # defined by the user when the action is created.
    output_artifacts: typing.List["Artifact"] = dataclasses.field(
        default_factory=list,
    )

    # Represents an AWS session credentials object. These credentials are
    # temporary credentials that are issued by AWS Secure Token Service (STS).
    # They can be used to access input and output artifacts in the Amazon S3
    # bucket used to store artifact for the pipeline in AWS CodePipeline.
    artifact_credentials: "AWSSessionCredentials" = dataclasses.field(
        default_factory=dict,
    )

    # A system-generated token, such as a AWS CodeDeploy deployment ID, that a
    # job requires in order to continue the job asynchronously.
    continuation_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The encryption key used to encrypt and decrypt data in the artifact store
    # for the pipeline, such as an AWS Key Management Service (AWS KMS) key. This
    # is optional and might not be present.
    encryption_key: "EncryptionKey" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ThirdPartyJobDetails(autoboto.ShapeBase):
    """
    The details of a job sent in response to a GetThirdPartyJobDetails request.
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
                "data",
                "data",
                autoboto.TypeInfo(ThirdPartyJobData),
            ),
            (
                "nonce",
                "nonce",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier used to identify the job details in AWS CodePipeline.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The data to be returned by the third party job worker.
    data: "ThirdPartyJobData" = dataclasses.field(default_factory=dict, )

    # A system-generated random number that AWS CodePipeline uses to ensure that
    # the job is being worked on by only one job worker. Use this number in an
    # AcknowledgeThirdPartyJob request.
    nonce: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TransitionState(autoboto.ShapeBase):
    """
    Represents information about the state of transitions between one stage and
    another stage.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "last_changed_by",
                "lastChangedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "last_changed_at",
                "lastChangedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "disabled_reason",
                "disabledReason",
                autoboto.TypeInfo(str),
            ),
        ]

    # Whether the transition between stages is enabled (true) or disabled
    # (false).
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the user who last changed the transition state.
    last_changed_by: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp when the transition state was last changed.
    last_changed_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The user-specified reason why the transition between two stages of a
    # pipeline was disabled.
    disabled_reason: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdatePipelineInput(autoboto.ShapeBase):
    """
    Represents the input of an UpdatePipeline action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline",
                "pipeline",
                autoboto.TypeInfo(PipelineDeclaration),
            ),
        ]

    # The name of the pipeline to be updated.
    pipeline: "PipelineDeclaration" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdatePipelineOutput(autoboto.OutputShapeBase):
    """
    Represents the output of an UpdatePipeline action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipeline",
                "pipeline",
                autoboto.TypeInfo(PipelineDeclaration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The structure of the updated pipeline.
    pipeline: "PipelineDeclaration" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ValidationException(autoboto.ShapeBase):
    """
    The validation was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class WebhookAuthConfiguration(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "allowed_ip_range",
                "AllowedIPRange",
                autoboto.TypeInfo(str),
            ),
            (
                "secret_token",
                "SecretToken",
                autoboto.TypeInfo(str),
            ),
        ]

    allowed_ip_range: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    secret_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class WebhookAuthenticationType(Enum):
    GITHUB_HMAC = "GITHUB_HMAC"
    IP = "IP"
    UNAUTHENTICATED = "UNAUTHENTICATED"


@dataclasses.dataclass
class WebhookDefinition(autoboto.ShapeBase):
    """
    Represents information about a webhook and its definition.
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
                "target_pipeline",
                "targetPipeline",
                autoboto.TypeInfo(str),
            ),
            (
                "target_action",
                "targetAction",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "filters",
                autoboto.TypeInfo(typing.List[WebhookFilterRule]),
            ),
            (
                "authentication",
                "authentication",
                autoboto.TypeInfo(WebhookAuthenticationType),
            ),
            (
                "authentication_configuration",
                "authenticationConfiguration",
                autoboto.TypeInfo(WebhookAuthConfiguration),
            ),
        ]

    # The name of the webhook.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the pipeline you want to connect to the webhook.
    target_pipeline: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the action in a pipeline you want to connect to the webhook.
    # The action must be from the source (first) stage of the pipeline.
    target_action: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of rules applied to the body/payload sent in the POST request to a
    # webhook URL. All defined rules must pass for the request to be accepted and
    # the pipeline started.
    filters: typing.List["WebhookFilterRule"] = dataclasses.field(
        default_factory=list,
    )

    # Supported options are GITHUB_HMAC, IP and UNAUTHENTICATED.

    #   * GITHUB_HMAC implements the authentication scheme described here: https://developer.github.com/webhooks/securing/

    #   * IP will reject webhooks trigger requests unless they originate from an IP within the IP range whitelisted in the authentication configuration.

    #   * UNAUTHENTICATED will accept all webhook trigger requests regardless of origin.
    authentication: "WebhookAuthenticationType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Properties that configure the authentication applied to incoming webhook
    # trigger requests. The required properties depend on the authentication
    # type. For GITHUB_HMAC, only the SecretToken property must be set. For IP,
    # only the AllowedIPRange property must be set to a valid CIDR range. For
    # UNAUTHENTICATED, no properties can be set.
    authentication_configuration: "WebhookAuthConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class WebhookFilterRule(autoboto.ShapeBase):
    """
    The event criteria that specify when a webhook notification is sent to your URL.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "json_path",
                "jsonPath",
                autoboto.TypeInfo(str),
            ),
            (
                "match_equals",
                "matchEquals",
                autoboto.TypeInfo(str),
            ),
        ]

    # A JsonPath expression that will be applied to the body/payload of the
    # webhook. The value selected by JsonPath expression must match the value
    # specified in the matchEquals field, otherwise the request will be ignored.
    # More information on JsonPath expressions can be found here:
    # https://github.com/json-path/JsonPath.
    json_path: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value selected by the JsonPath expression must match what is supplied
    # in the MatchEquals field, otherwise the request will be ignored. Properties
    # from the target action configuration can be included as placeholders in
    # this value by surrounding the action configuration key with curly braces.
    # For example, if the value supplied here is "refs/heads/{Branch}" and the
    # target action has an action configuration property called "Branch" with a
    # value of "master", the MatchEquals value will be evaluated as
    # "refs/heads/master". A list of action configuration properties for built-in
    # action types can be found here: [Pipeline Structure Reference Action
    # Requirements](http://docs.aws.amazon.com/codepipeline/latest/userguide/reference-
    # pipeline-structure.html#action-requirements).
    match_equals: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class WebhookNotFoundException(autoboto.ShapeBase):
    """
    The specified webhook was entered in an invalid format or cannot be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []
