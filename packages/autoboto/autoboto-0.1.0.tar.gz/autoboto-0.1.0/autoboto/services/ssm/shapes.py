import datetime
import typing
import autoboto
from enum import Enum
import botocore.response
import dataclasses


@dataclasses.dataclass
class Activation(autoboto.ShapeBase):
    """
    An activation registers one or more on-premises servers or virtual machines
    (VMs) with AWS so that you can configure those servers or VMs using Run Command.
    A server or VM that has been registered with AWS is called a managed instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activation_id",
                "ActivationId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "default_instance_name",
                "DefaultInstanceName",
                autoboto.TypeInfo(str),
            ),
            (
                "iam_role",
                "IamRole",
                autoboto.TypeInfo(str),
            ),
            (
                "registration_limit",
                "RegistrationLimit",
                autoboto.TypeInfo(int),
            ),
            (
                "registrations_count",
                "RegistrationsCount",
                autoboto.TypeInfo(int),
            ),
            (
                "expiration_date",
                "ExpirationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "expired",
                "Expired",
                autoboto.TypeInfo(bool),
            ),
            (
                "created_date",
                "CreatedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ID created by Systems Manager when you submitted the activation.
    activation_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A user defined description of the activation.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A name for the managed instance when it is created.
    default_instance_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Identity and Access Management (IAM) role to assign to the
    # managed instance.
    iam_role: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of managed instances that can be registered using this
    # activation.
    registration_limit: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of managed instances already registered with this activation.
    registrations_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date when this activation can no longer be used to register managed
    # instances.
    expiration_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether or not the activation is expired.
    expired: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date the activation was created.
    created_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddTagsToResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(ResourceTypeForTagging),
            ),
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # Specifies the type of resource you are tagging.

    # The ManagedInstance type for this API action is for on-premises managed
    # instances. You must specify the the name of the managed instance in the
    # following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.
    resource_type: "ResourceTypeForTagging" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The resource ID you want to tag.

    # Use the ID of the resource. Here are some examples:

    # ManagedInstance: mi-012345abcde

    # MaintenanceWindow: mw-012345abcde

    # PatchBaseline: pb-012345abcde

    # For the Document and Parameter values, use the name of the resource.

    # The ManagedInstance type for this API action is only for on-premises
    # managed instances. You must specify the the name of the managed instance in
    # the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more tags. The value parameter is required, but if you don't want
    # the tag to have a value, specify the parameter with no value, and we set
    # the value to an empty string.

    # Do not enter personally identifiable information in this field.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class AddTagsToResourceResult(autoboto.OutputShapeBase):
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
class AlreadyExistsException(autoboto.ShapeBase):
    """
    Error returned if an attempt is made to register a patch group with a patch
    baseline that is already registered with a different patch baseline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociatedInstances(autoboto.ShapeBase):
    """
    You must disassociate a document from all instances before you can delete it.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Association(autoboto.ShapeBase):
    """
    Describes an association of a Systems Manager document and an instance.
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
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "association_id",
                "AssociationId",
                autoboto.TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "last_execution_date",
                "LastExecutionDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "overview",
                "Overview",
                autoboto.TypeInfo(AssociationOverview),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                autoboto.TypeInfo(str),
            ),
            (
                "association_name",
                "AssociationName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID created by the system when you create an association. An association
    # is a binding between a document and a set of targets with a schedule.
    association_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The association version.
    association_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The version of the document used in the association.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instances targeted by the request to create an association.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # The date on which the association was last run.
    last_execution_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the association.
    overview: "AssociationOverview" = dataclasses.field(default_factory=dict, )

    # A cron expression that specifies a schedule when the association runs.
    schedule_expression: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The association name.
    association_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociationAlreadyExists(autoboto.ShapeBase):
    """
    The specified association already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AssociationDescription(autoboto.ShapeBase):
    """
    Describes the parameters for a document.
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
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "date",
                "Date",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_update_association_date",
                "LastUpdateAssociationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(AssociationStatus),
            ),
            (
                "overview",
                "Overview",
                autoboto.TypeInfo(AssociationOverview),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "association_id",
                "AssociationId",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                autoboto.TypeInfo(str),
            ),
            (
                "output_location",
                "OutputLocation",
                autoboto.TypeInfo(InstanceAssociationOutputLocation),
            ),
            (
                "last_execution_date",
                "LastExecutionDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_successful_execution_date",
                "LastSuccessfulExecutionDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "association_name",
                "AssociationName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The association version.
    association_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date when the association was made.
    date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date when the association was last updated.
    last_update_association_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The association status.
    status: "AssociationStatus" = dataclasses.field(default_factory=dict, )

    # Information about the association.
    overview: "AssociationOverview" = dataclasses.field(default_factory=dict, )

    # The document version.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A description of the parameters for a document.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The association ID.
    association_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instances targeted by the request.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # A cron expression that specifies a schedule when the association runs.
    schedule_expression: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An Amazon S3 bucket where you want to store the output details of the
    # request.
    output_location: "InstanceAssociationOutputLocation" = dataclasses.field(
        default_factory=dict,
    )

    # The date on which the association was last run.
    last_execution_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The last date on which the association was successfully run.
    last_successful_execution_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The association name.
    association_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociationDoesNotExist(autoboto.ShapeBase):
    """
    The specified association does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociationExecution(autoboto.ShapeBase):
    """
    Includes information about the specified association.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                autoboto.TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_id",
                "ExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
            (
                "detailed_status",
                "DetailedStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_execution_date",
                "LastExecutionDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "resource_count_by_status",
                "ResourceCountByStatus",
                autoboto.TypeInfo(str),
            ),
        ]

    # The association ID.
    association_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The association version.
    association_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The execution ID for the association. If the association does not run at
    # intervals or according to a schedule, then the ExecutionID is the same as
    # the AssociationID.
    execution_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the association execution.
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Detailed status information about the execution.
    detailed_status: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the execution started.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date of the last execution.
    last_execution_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An aggregate status of the resources in the execution based on the status
    # type.
    resource_count_by_status: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociationExecutionDoesNotExist(autoboto.ShapeBase):
    """
    The specified execution ID does not exist. Verify the ID number and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociationExecutionFilter(autoboto.ShapeBase):
    """
    Filters used in the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(AssociationExecutionFilterKey),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(AssociationFilterOperatorType),
            ),
        ]

    # The key value used in the request.
    key: "AssociationExecutionFilterKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The value specified for the key.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The filter type specified in the request.
    type: "AssociationFilterOperatorType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class AssociationExecutionFilterKey(Enum):
    ExecutionId = "ExecutionId"
    Status = "Status"
    CreatedTime = "CreatedTime"


@dataclasses.dataclass
class AssociationExecutionTarget(autoboto.ShapeBase):
    """
    Includes information about the specified association execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                autoboto.TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_id",
                "ExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
            (
                "detailed_status",
                "DetailedStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "last_execution_date",
                "LastExecutionDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "output_source",
                "OutputSource",
                autoboto.TypeInfo(OutputSource),
            ),
        ]

    # The association ID.
    association_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The association version.
    association_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The execution ID. If the association does not run at intervals or according
    # to a schedule, then the ExecutionID is the same as the AssociationID.
    execution_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The resource ID, for example, the instance ID where the association ran.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The resource type, for example, instance.
    resource_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The association execution status.
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Detailed information about the execution status.
    detailed_status: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date of the last execution.
    last_execution_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The location where the association details are saved.
    output_source: "OutputSource" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class AssociationExecutionTargetsFilter(autoboto.ShapeBase):
    """
    Filters for the association execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(AssociationExecutionTargetsFilterKey),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
        ]

    # The key value used in the request.
    key: "AssociationExecutionTargetsFilterKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The value specified for the key.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class AssociationExecutionTargetsFilterKey(Enum):
    Status = "Status"
    ResourceId = "ResourceId"
    ResourceType = "ResourceType"


@dataclasses.dataclass
class AssociationFilter(autoboto.ShapeBase):
    """
    Describes a filter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                autoboto.TypeInfo(AssociationFilterKey),
            ),
            (
                "value",
                "value",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the filter.
    key: "AssociationFilterKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The filter value.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class AssociationFilterKey(Enum):
    InstanceId = "InstanceId"
    Name = "Name"
    AssociationId = "AssociationId"
    AssociationStatusName = "AssociationStatusName"
    LastExecutedBefore = "LastExecutedBefore"
    LastExecutedAfter = "LastExecutedAfter"
    AssociationName = "AssociationName"


class AssociationFilterOperatorType(Enum):
    EQUAL = "EQUAL"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"


@dataclasses.dataclass
class AssociationLimitExceeded(autoboto.ShapeBase):
    """
    You can have at most 2,000 active associations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AssociationOverview(autoboto.ShapeBase):
    """
    Information about the association.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
            (
                "detailed_status",
                "DetailedStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "association_status_aggregated_count",
                "AssociationStatusAggregatedCount",
                autoboto.TypeInfo(typing.Dict[str, int]),
            ),
        ]

    # The status of the association. Status can be: Pending, Success, or Failed.
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A detailed status of the association.
    detailed_status: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Returns the number of targets for the association status. For example, if
    # you created an association with two instances, and one of them was
    # successful, this would return the count of instances by status.
    association_status_aggregated_count: typing.Dict[
        str, int
    ] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociationStatus(autoboto.ShapeBase):
    """
    Describes an association status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "date",
                "Date",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(AssociationStatusName),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "additional_info",
                "AdditionalInfo",
                autoboto.TypeInfo(str),
            ),
        ]

    # The date when the status changed.
    date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status.
    name: "AssociationStatusName" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The reason for the status.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A user-defined string.
    additional_info: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class AssociationStatusName(Enum):
    Pending = "Pending"
    Success = "Success"
    Failed = "Failed"


@dataclasses.dataclass
class AssociationVersionInfo(autoboto.ShapeBase):
    """
    Information about the association version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                autoboto.TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "created_date",
                "CreatedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                autoboto.TypeInfo(str),
            ),
            (
                "output_location",
                "OutputLocation",
                autoboto.TypeInfo(InstanceAssociationOutputLocation),
            ),
            (
                "association_name",
                "AssociationName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID created by the system when the association was created.
    association_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The association version.
    association_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date the association version was created.
    created_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name specified when the association was created.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version of a Systems Manager document used when the association version
    # was created.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Parameters specified when the association version was created.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The targets specified for the association when the association version was
    # created.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # The cron or rate schedule specified for the association when the
    # association version was created.
    schedule_expression: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The location in Amazon S3 specified for the association when the
    # association version was created.
    output_location: "InstanceAssociationOutputLocation" = dataclasses.field(
        default_factory=dict,
    )

    # The name specified for the association version when the association version
    # was created.
    association_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociationVersionLimitExceeded(autoboto.ShapeBase):
    """
    You have reached the maximum number versions allowed for an association. Each
    association has a limit of 1,000 versions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AutomationDefinitionNotFoundException(autoboto.ShapeBase):
    """
    An Automation document with the specified name could not be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AutomationDefinitionVersionNotFoundException(autoboto.ShapeBase):
    """
    An Automation document with the specified name and version could not be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AutomationExecution(autoboto.ShapeBase):
    """
    Detailed information about the current state of an individual Automation
    execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "automation_execution_id",
                "AutomationExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "document_name",
                "DocumentName",
                autoboto.TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_start_time",
                "ExecutionStartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "execution_end_time",
                "ExecutionEndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "automation_execution_status",
                "AutomationExecutionStatus",
                autoboto.TypeInfo(AutomationExecutionStatus),
            ),
            (
                "step_executions",
                "StepExecutions",
                autoboto.TypeInfo(typing.List[StepExecution]),
            ),
            (
                "step_executions_truncated",
                "StepExecutionsTruncated",
                autoboto.TypeInfo(bool),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "outputs",
                "Outputs",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "failure_message",
                "FailureMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "mode",
                "Mode",
                autoboto.TypeInfo(ExecutionMode),
            ),
            (
                "parent_automation_execution_id",
                "ParentAutomationExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "executed_by",
                "ExecutedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "current_step_name",
                "CurrentStepName",
                autoboto.TypeInfo(str),
            ),
            (
                "current_action",
                "CurrentAction",
                autoboto.TypeInfo(str),
            ),
            (
                "target_parameter_name",
                "TargetParameterName",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "target_maps",
                "TargetMaps",
                autoboto.TypeInfo(
                    typing.List[typing.Dict[str, typing.List[str]]]
                ),
            ),
            (
                "resolved_targets",
                "ResolvedTargets",
                autoboto.TypeInfo(ResolvedTargets),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                autoboto.TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                autoboto.TypeInfo(str),
            ),
            (
                "target",
                "Target",
                autoboto.TypeInfo(str),
            ),
        ]

    # The execution ID.
    automation_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the Automation document used during the execution.
    document_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version of the document to use during execution.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the execution started.
    execution_start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the execution finished.
    execution_end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The execution status of the Automation.
    automation_execution_status: "AutomationExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of details about the current state of all steps that comprise an
    # execution. An Automation document contains a list of steps that are
    # executed in order.
    step_executions: typing.List["StepExecution"] = dataclasses.field(
        default_factory=list,
    )

    # A boolean value that indicates if the response contains the full list of
    # the Automation step executions. If true, use the
    # DescribeAutomationStepExecutions API action to get the full list of step
    # executions.
    step_executions_truncated: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The key-value map of execution parameters, which were supplied when calling
    # StartAutomationExecution.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The list of execution outputs as defined in the automation document.
    outputs: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A message describing why an execution has failed, if the status is set to
    # Failed.
    failure_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The automation execution mode.
    mode: "ExecutionMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AutomationExecutionId of the parent automation.
    parent_automation_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the user who executed the automation.
    executed_by: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the currently executing step.
    current_step_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The action of the currently executing step.
    current_action: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameter name.
    target_parameter_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The specified targets.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # The specified key-value mapping of document parameters to target resources.
    target_maps: typing.List[typing.Dict[str, typing.List[str]]
                            ] = dataclasses.field(
                                default_factory=list,
                            )

    # A list of resolved targets in the rate control execution.
    resolved_targets: "ResolvedTargets" = dataclasses.field(
        default_factory=dict,
    )

    # The MaxConcurrency value specified by the user when the execution started.
    max_concurrency: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The MaxErrors value specified by the user when the execution started.
    max_errors: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The target of the execution.
    target: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AutomationExecutionFilter(autoboto.ShapeBase):
    """
    A filter used to match specific automation executions. This is used to limit the
    scope of Automation execution information returned.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(AutomationExecutionFilterKey),
            ),
            (
                "values",
                "Values",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # One or more keys to limit the results. Valid filter keys include the
    # following: DocumentNamePrefix, ExecutionStatus, ExecutionId,
    # ParentExecutionId, CurrentAction, StartTimeBefore, StartTimeAfter.
    key: "AutomationExecutionFilterKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The values used to limit the execution information associated with the
    # filter's key.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


class AutomationExecutionFilterKey(Enum):
    DocumentNamePrefix = "DocumentNamePrefix"
    ExecutionStatus = "ExecutionStatus"
    ExecutionId = "ExecutionId"
    ParentExecutionId = "ParentExecutionId"
    CurrentAction = "CurrentAction"
    StartTimeBefore = "StartTimeBefore"
    StartTimeAfter = "StartTimeAfter"


@dataclasses.dataclass
class AutomationExecutionLimitExceededException(autoboto.ShapeBase):
    """
    The number of simultaneously running Automation executions exceeded the
    allowable limit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AutomationExecutionMetadata(autoboto.ShapeBase):
    """
    Details about a specific Automation execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "automation_execution_id",
                "AutomationExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "document_name",
                "DocumentName",
                autoboto.TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "automation_execution_status",
                "AutomationExecutionStatus",
                autoboto.TypeInfo(AutomationExecutionStatus),
            ),
            (
                "execution_start_time",
                "ExecutionStartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "execution_end_time",
                "ExecutionEndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "executed_by",
                "ExecutedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "log_file",
                "LogFile",
                autoboto.TypeInfo(str),
            ),
            (
                "outputs",
                "Outputs",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "mode",
                "Mode",
                autoboto.TypeInfo(ExecutionMode),
            ),
            (
                "parent_automation_execution_id",
                "ParentAutomationExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "current_step_name",
                "CurrentStepName",
                autoboto.TypeInfo(str),
            ),
            (
                "current_action",
                "CurrentAction",
                autoboto.TypeInfo(str),
            ),
            (
                "failure_message",
                "FailureMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "target_parameter_name",
                "TargetParameterName",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "target_maps",
                "TargetMaps",
                autoboto.TypeInfo(
                    typing.List[typing.Dict[str, typing.List[str]]]
                ),
            ),
            (
                "resolved_targets",
                "ResolvedTargets",
                autoboto.TypeInfo(ResolvedTargets),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                autoboto.TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                autoboto.TypeInfo(str),
            ),
            (
                "target",
                "Target",
                autoboto.TypeInfo(str),
            ),
        ]

    # The execution ID.
    automation_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the Automation document used during execution.
    document_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The document version used during the execution.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the execution. Valid values include: Running, Succeeded,
    # Failed, Timed out, or Cancelled.
    automation_execution_status: "AutomationExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the execution started.>
    execution_start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the execution finished. This is not populated if the execution is
    # still in progress.
    execution_end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The IAM role ARN of the user who executed the Automation.
    executed_by: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An Amazon S3 bucket where execution information is stored.
    log_file: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of execution outputs as defined in the Automation document.
    outputs: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Automation execution mode.
    mode: "ExecutionMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ExecutionId of the parent Automation.
    parent_automation_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the currently executing step.
    current_step_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The action of the currently executing step.
    current_action: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The list of execution outputs as defined in the Automation document.
    failure_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The list of execution outputs as defined in the Automation document.
    target_parameter_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The targets defined by the user when starting the Automation.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # The specified key-value mapping of document parameters to target resources.
    target_maps: typing.List[typing.Dict[str, typing.List[str]]
                            ] = dataclasses.field(
                                default_factory=list,
                            )

    # A list of targets that resolved during the execution.
    resolved_targets: "ResolvedTargets" = dataclasses.field(
        default_factory=dict,
    )

    # The MaxConcurrency value specified by the user when starting the
    # Automation.
    max_concurrency: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The MaxErrors value specified by the user when starting the Automation.
    max_errors: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of execution outputs as defined in the Automation document.
    target: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AutomationExecutionNotFoundException(autoboto.ShapeBase):
    """
    There is no automation execution information for the requested automation
    execution ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class AutomationExecutionStatus(Enum):
    Pending = "Pending"
    InProgress = "InProgress"
    Waiting = "Waiting"
    Success = "Success"
    TimedOut = "TimedOut"
    Cancelling = "Cancelling"
    Cancelled = "Cancelled"
    Failed = "Failed"


@dataclasses.dataclass
class AutomationStepNotFoundException(autoboto.ShapeBase):
    """
    The specified step name and execution ID don't exist. Verify the information and
    try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelCommandRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "command_id",
                "CommandId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_ids",
                "InstanceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the command you want to cancel.
    command_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Optional) A list of instance IDs on which you want to cancel the command.
    # If not provided, the command is canceled on every instance on which it was
    # requested.
    instance_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CancelCommandResult(autoboto.OutputShapeBase):
    """
    Whether or not the command was successfully canceled. There is no guarantee that
    a request can be canceled.
    """

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
class CloudWatchOutputConfig(autoboto.ShapeBase):
    """
    Configuration options for sending command output to CloudWatch Logs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cloud_watch_log_group_name",
                "CloudWatchLogGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "cloud_watch_output_enabled",
                "CloudWatchOutputEnabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the CloudWatch log group where you want to send command output.
    # If you don't specify a group name, Systems Manager automatically creates a
    # log group for you. The log group uses the following naming format: aws/ssm/
    # _SystemsManagerDocumentName_.
    cloud_watch_log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Enables Systems Manager to send command output to CloudWatch Logs.
    cloud_watch_output_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Command(autoboto.ShapeBase):
    """
    Describes a command request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "command_id",
                "CommandId",
                autoboto.TypeInfo(str),
            ),
            (
                "document_name",
                "DocumentName",
                autoboto.TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "comment",
                "Comment",
                autoboto.TypeInfo(str),
            ),
            (
                "expires_after",
                "ExpiresAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "instance_ids",
                "InstanceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "requested_date_time",
                "RequestedDateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(CommandStatus),
            ),
            (
                "status_details",
                "StatusDetails",
                autoboto.TypeInfo(str),
            ),
            (
                "output_s3_region",
                "OutputS3Region",
                autoboto.TypeInfo(str),
            ),
            (
                "output_s3_bucket_name",
                "OutputS3BucketName",
                autoboto.TypeInfo(str),
            ),
            (
                "output_s3_key_prefix",
                "OutputS3KeyPrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                autoboto.TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                autoboto.TypeInfo(str),
            ),
            (
                "target_count",
                "TargetCount",
                autoboto.TypeInfo(int),
            ),
            (
                "completed_count",
                "CompletedCount",
                autoboto.TypeInfo(int),
            ),
            (
                "error_count",
                "ErrorCount",
                autoboto.TypeInfo(int),
            ),
            (
                "delivery_timed_out_count",
                "DeliveryTimedOutCount",
                autoboto.TypeInfo(int),
            ),
            (
                "service_role",
                "ServiceRole",
                autoboto.TypeInfo(str),
            ),
            (
                "notification_config",
                "NotificationConfig",
                autoboto.TypeInfo(NotificationConfig),
            ),
            (
                "cloud_watch_output_config",
                "CloudWatchOutputConfig",
                autoboto.TypeInfo(CloudWatchOutputConfig),
            ),
        ]

    # A unique identifier for this command.
    command_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the document requested for execution.
    document_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The SSM document version.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # User-specified information about the command, such as a brief description
    # of what the command should do.
    comment: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If this time is reached and the command has not already started executing,
    # it will not run. Calculated based on the ExpiresAfter user input provided
    # as part of the SendCommand API.
    expires_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameter values to be inserted in the document when executing the
    # command.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance IDs against which this command was requested.
    instance_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # An array of search criteria that targets instances using a Key,Value
    # combination that you specify. Targets is required if you don't provide one
    # or more instance IDs in the call.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # The date and time the command was requested.
    requested_date_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the command.
    status: "CommandStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A detailed status of the command execution. StatusDetails includes more
    # information than Status because it includes states resulting from error and
    # concurrency control parameters. StatusDetails can show different results
    # than Status. For more information about these statuses, see [Understanding
    # Command Statuses](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/monitor-commands.html) in the _AWS Systems Manager
    # User Guide_. StatusDetails can be one of the following values:

    #   * Pending: The command has not been sent to any instances.

    #   * In Progress: The command has been sent to at least one instance but has not reached a final state on all instances.

    #   * Success: The command successfully executed on all invocations. This is a terminal state.

    #   * Delivery Timed Out: The value of MaxErrors or more command invocations shows a status of Delivery Timed Out. This is a terminal state.

    #   * Execution Timed Out: The value of MaxErrors or more command invocations shows a status of Execution Timed Out. This is a terminal state.

    #   * Failed: The value of MaxErrors or more command invocations shows a status of Failed. This is a terminal state.

    #   * Incomplete: The command was attempted on all instances and one or more invocations does not have a value of Success but not enough invocations failed for the status to be Failed. This is a terminal state.

    #   * Canceled: The command was terminated before it was completed. This is a terminal state.

    #   * Rate Exceeded: The number of instances targeted by the command exceeded the account limit for pending invocations. The system has canceled the command before executing it on any instance. This is a terminal state.
    status_details: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # (Deprecated) You can no longer specify this parameter. The system ignores
    # it. Instead, Systems Manager automatically determines the Amazon S3 bucket
    # region.
    output_s3_region: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The S3 bucket where the responses to the command executions should be
    # stored. This was requested when issuing the command.
    output_s3_bucket_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The S3 directory path inside the bucket where the responses to the command
    # executions should be stored. This was requested when issuing the command.
    output_s3_key_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of instances that are allowed to execute the command at
    # the same time. You can specify a number of instances, such as 10, or a
    # percentage of instances, such as 10%. The default value is 50. For more
    # information about how to use MaxConcurrency, see [Executing Commands Using
    # Systems Manager Run Command](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/run-command.html) in the _AWS Systems Manager User
    # Guide_.
    max_concurrency: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of errors allowed before the system stops sending the
    # command to additional targets. You can specify a number of errors, such as
    # 10, or a percentage or errors, such as 10%. The default value is 0. For
    # more information about how to use MaxErrors, see [Executing Commands Using
    # Systems Manager Run Command](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/run-command.html) in the _AWS Systems Manager User
    # Guide_.
    max_errors: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of targets for the command.
    target_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of targets for which the command invocation reached a terminal
    # state. Terminal states include the following: Success, Failed, Execution
    # Timed Out, Delivery Timed Out, Canceled, Terminated, or Undeliverable.
    completed_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of targets for which the status is Failed or Execution Timed
    # Out.
    error_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of targets for which the status is Delivery Timed Out.
    delivery_timed_out_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The IAM service role that Run Command uses to act on your behalf when
    # sending notifications about command status changes.
    service_role: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Configurations for sending notifications about command status changes.
    notification_config: "NotificationConfig" = dataclasses.field(
        default_factory=dict,
    )

    # CloudWatch Logs information where you want Systems Manager to send the
    # command output.
    cloud_watch_output_config: "CloudWatchOutputConfig" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CommandFilter(autoboto.ShapeBase):
    """
    Describes a command filter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                autoboto.TypeInfo(CommandFilterKey),
            ),
            (
                "value",
                "value",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the filter.
    key: "CommandFilterKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The filter value.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class CommandFilterKey(Enum):
    InvokedAfter = "InvokedAfter"
    InvokedBefore = "InvokedBefore"
    Status = "Status"
    ExecutionStage = "ExecutionStage"
    DocumentName = "DocumentName"


@dataclasses.dataclass
class CommandInvocation(autoboto.ShapeBase):
    """
    An invocation is copy of a command sent to a specific instance. A command can
    apply to one or more instances. A command invocation applies to one instance.
    For example, if a user executes SendCommand against three instances, then a
    command invocation is created for each requested instance ID. A command
    invocation returns status and detail information about a command you executed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "command_id",
                "CommandId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_name",
                "InstanceName",
                autoboto.TypeInfo(str),
            ),
            (
                "comment",
                "Comment",
                autoboto.TypeInfo(str),
            ),
            (
                "document_name",
                "DocumentName",
                autoboto.TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "requested_date_time",
                "RequestedDateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(CommandInvocationStatus),
            ),
            (
                "status_details",
                "StatusDetails",
                autoboto.TypeInfo(str),
            ),
            (
                "trace_output",
                "TraceOutput",
                autoboto.TypeInfo(str),
            ),
            (
                "standard_output_url",
                "StandardOutputUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "standard_error_url",
                "StandardErrorUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "command_plugins",
                "CommandPlugins",
                autoboto.TypeInfo(typing.List[CommandPlugin]),
            ),
            (
                "service_role",
                "ServiceRole",
                autoboto.TypeInfo(str),
            ),
            (
                "notification_config",
                "NotificationConfig",
                autoboto.TypeInfo(NotificationConfig),
            ),
            (
                "cloud_watch_output_config",
                "CloudWatchOutputConfig",
                autoboto.TypeInfo(CloudWatchOutputConfig),
            ),
        ]

    # The command against which this invocation was requested.
    command_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance ID in which this invocation was requested.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the invocation target. For Amazon EC2 instances this is the
    # value for the aws:Name tag. For on-premises instances, this is the name of
    # the instance.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # User-specified information about the command, such as a brief description
    # of what the command should do.
    comment: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The document name that was requested for execution.
    document_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The SSM document version.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time and date the request was sent to this instance.
    requested_date_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether or not the invocation succeeded, failed, or is pending.
    status: "CommandInvocationStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A detailed status of the command execution for each invocation (each
    # instance targeted by the command). StatusDetails includes more information
    # than Status because it includes states resulting from error and concurrency
    # control parameters. StatusDetails can show different results than Status.
    # For more information about these statuses, see [Understanding Command
    # Statuses](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/monitor-commands.html) in the _AWS Systems Manager
    # User Guide_. StatusDetails can be one of the following values:

    #   * Pending: The command has not been sent to the instance.

    #   * In Progress: The command has been sent to the instance but has not reached a terminal state.

    #   * Success: The execution of the command or plugin was successfully completed. This is a terminal state.

    #   * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command's MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.

    #   * Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state.

    #   * Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state.

    #   * Canceled: The command was terminated before it was completed. This is a terminal state.

    #   * Undeliverable: The command can't be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit and don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state.

    #   * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.
    status_details: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Gets the trace output sent by the agent.
    trace_output: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The URL to the plugin's StdOut file in Amazon S3, if the Amazon S3 bucket
    # was defined for the parent command. For an invocation, StandardOutputUrl is
    # populated if there is just one plugin defined for the command, and the
    # Amazon S3 bucket was defined for the command.
    standard_output_url: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL to the plugin's StdErr file in Amazon S3, if the Amazon S3 bucket
    # was defined for the parent command. For an invocation, StandardErrorUrl is
    # populated if there is just one plugin defined for the command, and the
    # Amazon S3 bucket was defined for the command.
    standard_error_url: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    command_plugins: typing.List["CommandPlugin"] = dataclasses.field(
        default_factory=list,
    )

    # The IAM service role that Run Command uses to act on your behalf when
    # sending notifications about command status changes on a per instance basis.
    service_role: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Configurations for sending notifications about command status changes on a
    # per instance basis.
    notification_config: "NotificationConfig" = dataclasses.field(
        default_factory=dict,
    )

    # CloudWatch Logs information where you want Systems Manager to send the
    # command output.
    cloud_watch_output_config: "CloudWatchOutputConfig" = dataclasses.field(
        default_factory=dict,
    )


class CommandInvocationStatus(Enum):
    Pending = "Pending"
    InProgress = "InProgress"
    Delayed = "Delayed"
    Success = "Success"
    Cancelled = "Cancelled"
    TimedOut = "TimedOut"
    Failed = "Failed"
    Cancelling = "Cancelling"


@dataclasses.dataclass
class CommandPlugin(autoboto.ShapeBase):
    """
    Describes plugin details.
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
                "status",
                "Status",
                autoboto.TypeInfo(CommandPluginStatus),
            ),
            (
                "status_details",
                "StatusDetails",
                autoboto.TypeInfo(str),
            ),
            (
                "response_code",
                "ResponseCode",
                autoboto.TypeInfo(int),
            ),
            (
                "response_start_date_time",
                "ResponseStartDateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "response_finish_date_time",
                "ResponseFinishDateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "output",
                "Output",
                autoboto.TypeInfo(str),
            ),
            (
                "standard_output_url",
                "StandardOutputUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "standard_error_url",
                "StandardErrorUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "output_s3_region",
                "OutputS3Region",
                autoboto.TypeInfo(str),
            ),
            (
                "output_s3_bucket_name",
                "OutputS3BucketName",
                autoboto.TypeInfo(str),
            ),
            (
                "output_s3_key_prefix",
                "OutputS3KeyPrefix",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the plugin. Must be one of the following: aws:updateAgent,
    # aws:domainjoin, aws:applications, aws:runPowerShellScript, aws:psmodule,
    # aws:cloudWatch, aws:runShellScript, or aws:updateSSMAgent.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of this plugin. You can execute a document with multiple
    # plugins.
    status: "CommandPluginStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A detailed status of the plugin execution. StatusDetails includes more
    # information than Status because it includes states resulting from error and
    # concurrency control parameters. StatusDetails can show different results
    # than Status. For more information about these statuses, see [Understanding
    # Command Statuses](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/monitor-commands.html) in the _AWS Systems Manager
    # User Guide_. StatusDetails can be one of the following values:

    #   * Pending: The command has not been sent to the instance.

    #   * In Progress: The command has been sent to the instance but has not reached a terminal state.

    #   * Success: The execution of the command or plugin was successfully completed. This is a terminal state.

    #   * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command's MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.

    #   * Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state.

    #   * Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state.

    #   * Canceled: The command was terminated before it was completed. This is a terminal state.

    #   * Undeliverable: The command can't be delivered to the instance. The instance might not exist, or it might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit, and they don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state.

    #   * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.
    status_details: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A numeric response code generated after executing the plugin.
    response_code: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time the plugin started executing.
    response_start_date_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the plugin stopped executing. Could stop prematurely if, for
    # example, a cancel command was sent.
    response_finish_date_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Output of the plugin execution.
    output: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The URL for the complete text written by the plugin to stdout in Amazon S3.
    # If the Amazon S3 bucket for the command was not specified, then this string
    # is empty.
    standard_output_url: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL for the complete text written by the plugin to stderr. If execution
    # is not yet complete, then this string is empty.
    standard_error_url: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # (Deprecated) You can no longer specify this parameter. The system ignores
    # it. Instead, Systems Manager automatically determines the Amazon S3 bucket
    # region.
    output_s3_region: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The S3 bucket where the responses to the command executions should be
    # stored. This was requested when issuing the command. For example, in the
    # following response:

    # test_folder/ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-
    # Fix/i-1234567876543/awsrunShellScript

    # test_folder is the name of the Amazon S3 bucket;

    # ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix is the name of the S3 prefix;

    # i-1234567876543 is the instance ID;

    # awsrunShellScript is the name of the plugin.
    output_s3_bucket_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The S3 directory path inside the bucket where the responses to the command
    # executions should be stored. This was requested when issuing the command.
    # For example, in the following response:

    # test_folder/ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-
    # Fix/i-1234567876543/awsrunShellScript

    # test_folder is the name of the Amazon S3 bucket;

    # ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix is the name of the S3 prefix;

    # i-1234567876543 is the instance ID;

    # awsrunShellScript is the name of the plugin.
    output_s3_key_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class CommandPluginStatus(Enum):
    Pending = "Pending"
    InProgress = "InProgress"
    Success = "Success"
    TimedOut = "TimedOut"
    Cancelled = "Cancelled"
    Failed = "Failed"


class CommandStatus(Enum):
    Pending = "Pending"
    InProgress = "InProgress"
    Success = "Success"
    Cancelled = "Cancelled"
    Failed = "Failed"
    TimedOut = "TimedOut"
    Cancelling = "Cancelling"


@dataclasses.dataclass
class ComplianceExecutionSummary(autoboto.ShapeBase):
    """
    A summary of the call execution that includes an execution ID, the type of
    execution (for example, `Command`), and the date/time of the execution using a
    datetime object that is saved in the following format: yyyy-MM-dd'T'HH:mm:ss'Z'.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution_time",
                "ExecutionTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "execution_id",
                "ExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_type",
                "ExecutionType",
                autoboto.TypeInfo(str),
            ),
        ]

    # The time the execution ran as a datetime object that is saved in the
    # following format: yyyy-MM-dd'T'HH:mm:ss'Z'.
    execution_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An ID created by the system when `PutComplianceItems` was called. For
    # example, `CommandID` is a valid execution ID. You can use this ID in
    # subsequent calls.
    execution_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of execution. For example, `Command` is a valid execution type.
    execution_type: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ComplianceItem(autoboto.ShapeBase):
    """
    Information about the compliance as defined by the resource type. For example,
    for a patch resource type, `Items` includes information about the PatchSeverity,
    Classification, etc.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compliance_type",
                "ComplianceType",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "title",
                "Title",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(ComplianceStatus),
            ),
            (
                "severity",
                "Severity",
                autoboto.TypeInfo(ComplianceSeverity),
            ),
            (
                "execution_summary",
                "ExecutionSummary",
                autoboto.TypeInfo(ComplianceExecutionSummary),
            ),
            (
                "details",
                "Details",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The compliance type. For example, Association (for a State Manager
    # association), Patch, or Custom:`string` are all valid compliance types.
    compliance_type: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of resource. `ManagedInstance` is currently the only supported
    # resource type.
    resource_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An ID for the resource. For a managed instance, this is the instance ID.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An ID for the compliance item. For example, if the compliance item is a
    # Windows patch, the ID could be the number of the KB article; for example:
    # KB4010320.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A title for the compliance item. For example, if the compliance item is a
    # Windows patch, the title could be the title of the KB article for the
    # patch; for example: Security Update for Active Directory Federation
    # Services.
    title: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the compliance item. An item is either COMPLIANT or
    # NON_COMPLIANT.
    status: "ComplianceStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The severity of the compliance status. Severity can be one of the
    # following: Critical, High, Medium, Low, Informational, Unspecified.
    severity: "ComplianceSeverity" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A summary for the compliance item. The summary includes an execution ID,
    # the execution type (for example, command), and the execution time.
    execution_summary: "ComplianceExecutionSummary" = dataclasses.field(
        default_factory=dict,
    )

    # A "Key": "Value" tag combination for the compliance item.
    details: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ComplianceItemEntry(autoboto.ShapeBase):
    """
    Information about a compliance item.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "severity",
                "Severity",
                autoboto.TypeInfo(ComplianceSeverity),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(ComplianceStatus),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "title",
                "Title",
                autoboto.TypeInfo(str),
            ),
            (
                "details",
                "Details",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The severity of the compliance status. Severity can be one of the
    # following: Critical, High, Medium, Low, Informational, Unspecified.
    severity: "ComplianceSeverity" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the compliance item. An item is either COMPLIANT or
    # NON_COMPLIANT.
    status: "ComplianceStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The compliance item ID. For example, if the compliance item is a Windows
    # patch, the ID could be the number of the KB article.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The title of the compliance item. For example, if the compliance item is a
    # Windows patch, the title could be the title of the KB article for the
    # patch; for example: Security Update for Active Directory Federation
    # Services.
    title: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A "Key": "Value" tag combination for the compliance item.
    details: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ComplianceQueryOperatorType(Enum):
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"
    BEGIN_WITH = "BEGIN_WITH"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"


class ComplianceSeverity(Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFORMATIONAL = "INFORMATIONAL"
    UNSPECIFIED = "UNSPECIFIED"


class ComplianceStatus(Enum):
    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON_COMPLIANT"


@dataclasses.dataclass
class ComplianceStringFilter(autoboto.ShapeBase):
    """
    One or more filters. Use a filter to return a more specific list of results.
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
            (
                "type",
                "Type",
                autoboto.TypeInfo(ComplianceQueryOperatorType),
            ),
        ]

    # The name of the filter.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value for which to search.
    values: typing.List[str] = dataclasses.field(default_factory=list, )

    # The type of comparison that should be performed for the value: Equal,
    # NotEqual, BeginWith, LessThan, or GreaterThan.
    type: "ComplianceQueryOperatorType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ComplianceSummaryItem(autoboto.ShapeBase):
    """
    A summary of compliance information by compliance type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compliance_type",
                "ComplianceType",
                autoboto.TypeInfo(str),
            ),
            (
                "compliant_summary",
                "CompliantSummary",
                autoboto.TypeInfo(CompliantSummary),
            ),
            (
                "non_compliant_summary",
                "NonCompliantSummary",
                autoboto.TypeInfo(NonCompliantSummary),
            ),
        ]

    # The type of compliance item. For example, the compliance type can be
    # Association, Patch, or Custom:string.
    compliance_type: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of COMPLIANT items for the specified compliance type.
    compliant_summary: "CompliantSummary" = dataclasses.field(
        default_factory=dict,
    )

    # A list of NON_COMPLIANT items for the specified compliance type.
    non_compliant_summary: "NonCompliantSummary" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ComplianceTypeCountLimitExceededException(autoboto.ShapeBase):
    """
    You specified too many custom compliance types. You can specify a maximum of 10
    different types.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CompliantSummary(autoboto.ShapeBase):
    """
    A summary of resources that are compliant. The summary is organized according to
    the resource count for each compliance type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compliant_count",
                "CompliantCount",
                autoboto.TypeInfo(int),
            ),
            (
                "severity_summary",
                "SeveritySummary",
                autoboto.TypeInfo(SeveritySummary),
            ),
        ]

    # The total number of resources that are compliant.
    compliant_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A summary of the compliance severity by compliance type.
    severity_summary: "SeveritySummary" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateActivationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "iam_role",
                "IamRole",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "default_instance_name",
                "DefaultInstanceName",
                autoboto.TypeInfo(str),
            ),
            (
                "registration_limit",
                "RegistrationLimit",
                autoboto.TypeInfo(int),
            ),
            (
                "expiration_date",
                "ExpirationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Identity and Access Management (IAM) role that you want to
    # assign to the managed instance.
    iam_role: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A user-defined description of the resource that you want to register with
    # Amazon EC2.

    # Do not enter personally identifiable information in this field.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the registered, managed instance as it will appear in the
    # Amazon EC2 console or when you use the AWS command line tools to list EC2
    # resources.

    # Do not enter personally identifiable information in this field.
    default_instance_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specify the maximum number of managed instances you want to register. The
    # default value is 1 instance.
    registration_limit: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date by which this activation request should expire. The default value
    # is 24 hours.
    expiration_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateActivationResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "activation_id",
                "ActivationId",
                autoboto.TypeInfo(str),
            ),
            (
                "activation_code",
                "ActivationCode",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID number generated by the system when it processed the activation. The
    # activation ID functions like a user name.
    activation_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The code the system generates when it processes the activation. The
    # activation code functions like a password to validate the activation ID.
    activation_code: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateAssociationBatchRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "entries",
                "Entries",
                autoboto.TypeInfo(
                    typing.List[CreateAssociationBatchRequestEntry]
                ),
            ),
        ]

    # One or more associations.
    entries: typing.List["CreateAssociationBatchRequestEntry"
                        ] = dataclasses.field(
                            default_factory=list,
                        )


@dataclasses.dataclass
class CreateAssociationBatchRequestEntry(autoboto.ShapeBase):
    """
    Describes the association of a Systems Manager document and an instance.
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
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                autoboto.TypeInfo(str),
            ),
            (
                "output_location",
                "OutputLocation",
                autoboto.TypeInfo(InstanceAssociationOutputLocation),
            ),
            (
                "association_name",
                "AssociationName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the configuration document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A description of the parameters for a document.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The document version.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instances targeted by the request.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # A cron expression that specifies a schedule when the association runs.
    schedule_expression: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An Amazon S3 bucket where you want to store the results of this request.
    output_location: "InstanceAssociationOutputLocation" = dataclasses.field(
        default_factory=dict,
    )

    # Specify a descriptive name for the association.
    association_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateAssociationBatchResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "successful",
                "Successful",
                autoboto.TypeInfo(typing.List[AssociationDescription]),
            ),
            (
                "failed",
                "Failed",
                autoboto.TypeInfo(typing.List[FailedCreateAssociation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the associations that succeeded.
    successful: typing.List["AssociationDescription"] = dataclasses.field(
        default_factory=list,
    )

    # Information about the associations that failed.
    failed: typing.List["FailedCreateAssociation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateAssociationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                autoboto.TypeInfo(str),
            ),
            (
                "output_location",
                "OutputLocation",
                autoboto.TypeInfo(InstanceAssociationOutputLocation),
            ),
            (
                "association_name",
                "AssociationName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The document version you want to associate with the target(s). Can be a
    # specific version or the default version.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The parameters for the documents runtime configuration.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The targets (either instances or tags) for the association.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # A cron expression when the association will be applied to the target(s).
    schedule_expression: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An Amazon S3 bucket where you want to store the output details of the
    # request.
    output_location: "InstanceAssociationOutputLocation" = dataclasses.field(
        default_factory=dict,
    )

    # Specify a descriptive name for the association.
    association_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateAssociationResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "association_description",
                "AssociationDescription",
                autoboto.TypeInfo(AssociationDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the association.
    association_description: "AssociationDescription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateDocumentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "content",
                "Content",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "document_type",
                "DocumentType",
                autoboto.TypeInfo(DocumentType),
            ),
            (
                "document_format",
                "DocumentFormat",
                autoboto.TypeInfo(DocumentFormat),
            ),
            (
                "target_type",
                "TargetType",
                autoboto.TypeInfo(str),
            ),
        ]

    # A valid JSON or YAML string.
    content: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A name for the Systems Manager document.

    # Do not use the following to begin the names of documents you create. They
    # are reserved by AWS for use as document prefixes:

    #   * `aws`

    #   * `amazon`

    #   * `amzn`
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of document to create. Valid document types include: Policy,
    # Automation, and Command.
    document_type: "DocumentType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specify the document format for the request. The document format can be
    # either JSON or YAML. JSON is the default format.
    document_format: "DocumentFormat" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specify a target type to define the kinds of resources the document can run
    # on. For example, to run a document on EC2 instances, specify the following
    # value: /AWS::EC2::Instance. If you specify a value of '/' the document can
    # run on all types of resources. If you don't specify a value, the document
    # can't run on any resources. For a list of valid resource types, see [AWS
    # Resource Types
    # Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # template-resource-type-ref.html) in the _AWS CloudFormation User Guide_.
    target_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDocumentResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "document_description",
                "DocumentDescription",
                autoboto.TypeInfo(DocumentDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the Systems Manager document.
    document_description: "DocumentDescription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateMaintenanceWindowRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                autoboto.TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(int),
            ),
            (
                "cutoff",
                "Cutoff",
                autoboto.TypeInfo(int),
            ),
            (
                "allow_unassociated_targets",
                "AllowUnassociatedTargets",
                autoboto.TypeInfo(bool),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "client_token",
                "ClientToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the Maintenance Window.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The schedule of the Maintenance Window in the form of a cron or rate
    # expression.
    schedule: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The duration of the Maintenance Window in hours.
    duration: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of hours before the end of the Maintenance Window that Systems
    # Manager stops scheduling new tasks for execution.
    cutoff: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Enables a Maintenance Window task to execute on managed instances, even if
    # you have not registered those instances as targets. If enabled, then you
    # must specify the unregistered instances (by instance ID) when you register
    # a task with the Maintenance Window

    # If you don't enable this option, then you must specify previously-
    # registered targets when you register a task with the Maintenance Window.
    allow_unassociated_targets: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An optional description for the Maintenance Window. We recommend specifying
    # a description to help you organize your Maintenance Windows.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # User-provided idempotency token.
    client_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateMaintenanceWindowResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the created Maintenance Window.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePatchBaselineRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "operating_system",
                "OperatingSystem",
                autoboto.TypeInfo(OperatingSystem),
            ),
            (
                "global_filters",
                "GlobalFilters",
                autoboto.TypeInfo(PatchFilterGroup),
            ),
            (
                "approval_rules",
                "ApprovalRules",
                autoboto.TypeInfo(PatchRuleGroup),
            ),
            (
                "approved_patches",
                "ApprovedPatches",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "approved_patches_compliance_level",
                "ApprovedPatchesComplianceLevel",
                autoboto.TypeInfo(PatchComplianceLevel),
            ),
            (
                "approved_patches_enable_non_security",
                "ApprovedPatchesEnableNonSecurity",
                autoboto.TypeInfo(bool),
            ),
            (
                "rejected_patches",
                "RejectedPatches",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "sources",
                "Sources",
                autoboto.TypeInfo(typing.List[PatchSource]),
            ),
            (
                "client_token",
                "ClientToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the patch baseline.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Defines the operating system the patch baseline applies to. The Default
    # value is WINDOWS.
    operating_system: "OperatingSystem" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A set of global filters used to exclude patches from the baseline.
    global_filters: "PatchFilterGroup" = dataclasses.field(
        default_factory=dict,
    )

    # A set of rules used to include patches in the baseline.
    approval_rules: "PatchRuleGroup" = dataclasses.field(default_factory=dict, )

    # A list of explicitly approved patches for the baseline.

    # For information about accepted formats for lists of approved patches and
    # rejected patches, see [Package Name Formats for Approved and Rejected Patch
    # Lists](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-
    # manager-approved-rejected-package-name-formats.html) in the _AWS Systems
    # Manager User Guide_.
    approved_patches: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Defines the compliance level for approved patches. This means that if an
    # approved patch is reported as missing, this is the severity of the
    # compliance violation. The default value is UNSPECIFIED.
    approved_patches_compliance_level: "PatchComplianceLevel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the list of approved patches includes non-security
    # updates that should be applied to the instances. The default value is
    # 'false'. Applies to Linux instances only.
    approved_patches_enable_non_security: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of explicitly rejected patches for the baseline.

    # For information about accepted formats for lists of approved patches and
    # rejected patches, see [Package Name Formats for Approved and Rejected Patch
    # Lists](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-
    # manager-approved-rejected-package-name-formats.html) in the _AWS Systems
    # Manager User Guide_.
    rejected_patches: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A description of the patch baseline.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Information about the patches to use to update the instances, including
    # target operating systems and source repositories. Applies to Linux
    # instances only.
    sources: typing.List["PatchSource"] = dataclasses.field(
        default_factory=list,
    )

    # User-provided idempotency token.
    client_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePatchBaselineResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the created patch baseline.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateResourceDataSyncRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sync_name",
                "SyncName",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_destination",
                "S3Destination",
                autoboto.TypeInfo(ResourceDataSyncS3Destination),
            ),
        ]

    # A name for the configuration.
    sync_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon S3 configuration details for the sync.
    s3_destination: "ResourceDataSyncS3Destination" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateResourceDataSyncResult(autoboto.OutputShapeBase):
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
class CustomSchemaCountLimitExceededException(autoboto.ShapeBase):
    """
    You have exceeded the limit for custom schemas. Delete one or more custom
    schemas and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteActivationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activation_id",
                "ActivationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the activation that you want to delete.
    activation_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteActivationResult(autoboto.OutputShapeBase):
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
class DeleteAssociationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "association_id",
                "AssociationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The association ID that you want to delete.
    association_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteAssociationResult(autoboto.OutputShapeBase):
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
class DeleteDocumentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDocumentResult(autoboto.OutputShapeBase):
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
class DeleteInventoryRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "schema_delete_option",
                "SchemaDeleteOption",
                autoboto.TypeInfo(InventorySchemaDeleteOption),
            ),
            (
                "dry_run",
                "DryRun",
                autoboto.TypeInfo(bool),
            ),
            (
                "client_token",
                "ClientToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the custom inventory type for which you want to delete either
    # all previously collected data, or the inventory type itself.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Use the `SchemaDeleteOption` to delete a custom inventory type (schema). If
    # you don't choose this option, the system only deletes existing inventory
    # data associated with the custom inventory type. Choose one of the following
    # options:

    # DisableSchema: If you choose this option, the system ignores all inventory
    # data for the specified version, and any earlier versions. To enable this
    # schema again, you must call the `PutInventory` action for a version greater
    # than the disbled version.

    # DeleteSchema: This option deletes the specified custom type from the
    # Inventory service. You can recreate the schema later, if you want.
    schema_delete_option: "InventorySchemaDeleteOption" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Use this option to view a summary of the deletion request without deleting
    # any data or the data type. This option is useful when you only want to
    # understand what will be deleted. Once you validate that the data to be
    # deleted is what you intend to delete, you can run the same command without
    # specifying the `DryRun` option.
    dry_run: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # User-provided idempotency token.
    client_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteInventoryResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "deletion_id",
                "DeletionId",
                autoboto.TypeInfo(str),
            ),
            (
                "type_name",
                "TypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "deletion_summary",
                "DeletionSummary",
                autoboto.TypeInfo(InventoryDeletionSummary),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Every `DeleteInventory` action is assigned a unique ID. This option returns
    # a unique ID. You can use this ID to query the status of a delete operation.
    # This option is useful for ensuring that a delete operation has completed
    # before you begin other actions.
    deletion_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the inventory data type specified in the request.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A summary of the delete operation. For more information about this summary,
    # see [Understanding the Delete Inventory
    # Summary](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/sysman-inventory-delete.html#sysman-inventory-
    # delete-summary) in the _AWS Systems Manager User Guide_.
    deletion_summary: "InventoryDeletionSummary" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteMaintenanceWindowRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window to delete.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteMaintenanceWindowResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the deleted Maintenance Window.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteParameterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the parameter to delete.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteParameterResult(autoboto.OutputShapeBase):
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
class DeleteParametersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The names of the parameters to delete.
    names: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DeleteParametersResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "deleted_parameters",
                "DeletedParameters",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "invalid_parameters",
                "InvalidParameters",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The names of the deleted parameters.
    deleted_parameters: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The names of parameters that weren't deleted because the parameters are not
    # valid.
    invalid_parameters: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DeletePatchBaselineRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the patch baseline to delete.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletePatchBaselineResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the deleted patch baseline.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteResourceDataSyncRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sync_name",
                "SyncName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the configuration to delete.
    sync_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteResourceDataSyncResult(autoboto.OutputShapeBase):
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
class DeregisterManagedInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID assigned to the managed instance when you registered it using the
    # activation process.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterManagedInstanceResult(autoboto.OutputShapeBase):
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
class DeregisterPatchBaselineForPatchGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
            (
                "patch_group",
                "PatchGroup",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the patch baseline to deregister the patch group from.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the patch group that should be deregistered from the patch
    # baseline.
    patch_group: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterPatchBaselineForPatchGroupResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
            (
                "patch_group",
                "PatchGroup",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the patch baseline the patch group was deregistered from.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the patch group deregistered from the patch baseline.
    patch_group: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterTargetFromMaintenanceWindowRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "window_target_id",
                "WindowTargetId",
                autoboto.TypeInfo(str),
            ),
            (
                "safe",
                "Safe",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the Maintenance Window the target should be removed from.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the target definition to remove.
    window_target_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The system checks if the target is being referenced by a task. If the
    # target is being referenced, the system returns an error and does not
    # deregister the target from the Maintenance Window.
    safe: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterTargetFromMaintenanceWindowResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "window_target_id",
                "WindowTargetId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the Maintenance Window the target was removed from.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the removed target definition.
    window_target_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeregisterTaskFromMaintenanceWindowRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "window_task_id",
                "WindowTaskId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window the task should be removed from.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the task to remove from the Maintenance Window.
    window_task_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeregisterTaskFromMaintenanceWindowResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "window_task_id",
                "WindowTaskId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the Maintenance Window the task was removed from.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the task removed from the Maintenance Window.
    window_task_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeActivationsFilter(autoboto.ShapeBase):
    """
    Filter for the DescribeActivation API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter_key",
                "FilterKey",
                autoboto.TypeInfo(DescribeActivationsFilterKeys),
            ),
            (
                "filter_values",
                "FilterValues",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the filter.
    filter_key: "DescribeActivationsFilterKeys" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The filter values.
    filter_values: typing.List[str] = dataclasses.field(default_factory=list, )


class DescribeActivationsFilterKeys(Enum):
    ActivationIds = "ActivationIds"
    DefaultInstanceName = "DefaultInstanceName"
    IamRole = "IamRole"


@dataclasses.dataclass
class DescribeActivationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[DescribeActivationsFilter]),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A filter to view information about your activations.
    filters: typing.List["DescribeActivationsFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeActivationsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "activation_list",
                "ActivationList",
                autoboto.TypeInfo(typing.List[Activation]),
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

    # A list of activations for your AWS account.
    activation_list: typing.List["Activation"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAssociationExecutionTargetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_id",
                "ExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(
                    typing.List[AssociationExecutionTargetsFilter]
                ),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The association ID that includes the execution for which you want to view
    # details.
    association_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The execution ID for which you want to view details.
    execution_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filters for the request. You can specify the following filters and values.

    # Status (EQUAL)

    # ResourceId (EQUAL)

    # ResourceType (EQUAL)
    filters: typing.List["AssociationExecutionTargetsFilter"
                        ] = dataclasses.field(
                            default_factory=list,
                        )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAssociationExecutionTargetsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "association_execution_targets",
                "AssociationExecutionTargets",
                autoboto.TypeInfo(typing.List[AssociationExecutionTarget]),
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

    # Information about the execution.
    association_execution_targets: typing.List["AssociationExecutionTarget"
                                              ] = dataclasses.field(
                                                  default_factory=list,
                                              )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAssociationExecutionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[AssociationExecutionFilter]),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The association ID for which you want to view execution history details.
    association_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Filters for the request. You can specify the following filters and values.

    # ExecutionId (EQUAL)

    # Status (EQUAL)

    # CreatedTime (EQUAL, GREATER_THAN, LESS_THAN)
    filters: typing.List["AssociationExecutionFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAssociationExecutionsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "association_executions",
                "AssociationExecutions",
                autoboto.TypeInfo(typing.List[AssociationExecution]),
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

    # A list of the executions for the specified association ID.
    association_executions: typing.List["AssociationExecution"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAssociationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "association_id",
                "AssociationId",
                autoboto.TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The association ID for which you want information.
    association_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specify the association version to retrieve. To view the latest version,
    # either specify `$LATEST` for this parameter, or omit this parameter. To
    # view a list of all associations for an instance, use
    # ListInstanceAssociations. To get a list of versions for a specific
    # association, use ListAssociationVersions.
    association_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAssociationResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "association_description",
                "AssociationDescription",
                autoboto.TypeInfo(AssociationDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the association.
    association_description: "AssociationDescription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeAutomationExecutionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[AutomationExecutionFilter]),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Filters used to limit the scope of executions that are requested.
    filters: typing.List["AutomationExecutionFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAutomationExecutionsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "automation_execution_metadata_list",
                "AutomationExecutionMetadataList",
                autoboto.TypeInfo(typing.List[AutomationExecutionMetadata]),
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

    # The list of details about each automation execution which has occurred
    # which matches the filter specification, if any.
    automation_execution_metadata_list: typing.List[
        "AutomationExecutionMetadata"
    ] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAutomationStepExecutionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "automation_execution_id",
                "AutomationExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[StepExecutionFilter]),
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
            (
                "reverse_order",
                "ReverseOrder",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The Automation execution ID for which you want step execution descriptions.
    automation_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # One or more filters to limit the number of step executions returned by the
    # request.
    filters: typing.List["StepExecutionFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A boolean that indicates whether to list step executions in reverse order
    # by start time. The default value is false.
    reverse_order: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAutomationStepExecutionsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "step_executions",
                "StepExecutions",
                autoboto.TypeInfo(typing.List[StepExecution]),
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

    # A list of details about the current state of all steps that make up an
    # execution.
    step_executions: typing.List["StepExecution"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAvailablePatchesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[PatchOrchestratorFilter]),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Filters used to scope down the returned patches.
    filters: typing.List["PatchOrchestratorFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of patches to return (per page).
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAvailablePatchesResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "patches",
                "Patches",
                autoboto.TypeInfo(typing.List[Patch]),
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

    # An array of patches. Each entry in the array is a patch structure.
    patches: typing.List["Patch"] = dataclasses.field(default_factory=list, )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDocumentPermissionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "permission_type",
                "PermissionType",
                autoboto.TypeInfo(DocumentPermissionType),
            ),
        ]

    # The name of the document for which you are the owner.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The permission type for the document. The permission type can be _Share_.
    permission_type: "DocumentPermissionType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeDocumentPermissionResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "account_ids",
                "AccountIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The account IDs that have permission to use this document. The ID can be
    # either an AWS account or _All_.
    account_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeDocumentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The document version for which you want information. Can be a specific
    # version or the default version.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeDocumentResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "document",
                "Document",
                autoboto.TypeInfo(DocumentDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the Systems Manager document.
    document: "DocumentDescription" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeEffectiveInstanceAssociationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The instance ID for which you want to view all associations.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEffectiveInstanceAssociationsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "associations",
                "Associations",
                autoboto.TypeInfo(typing.List[InstanceAssociation]),
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

    # The associations for the requested instance.
    associations: typing.List["InstanceAssociation"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEffectivePatchesForPatchBaselineRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the patch baseline to retrieve the effective patches for.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of patches to return (per page).
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEffectivePatchesForPatchBaselineResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "effective_patches",
                "EffectivePatches",
                autoboto.TypeInfo(typing.List[EffectivePatch]),
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

    # An array of patches and patch status.
    effective_patches: typing.List["EffectivePatch"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstanceAssociationsStatusRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The instance IDs for which you want association status information.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstanceAssociationsStatusResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_association_status_infos",
                "InstanceAssociationStatusInfos",
                autoboto.TypeInfo(typing.List[InstanceAssociationStatusInfo]),
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

    # Status information about the association.
    instance_association_status_infos: typing.List[
        "InstanceAssociationStatusInfo"
    ] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstanceInformationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_information_filter_list",
                "InstanceInformationFilterList",
                autoboto.TypeInfo(typing.List[InstanceInformationFilter]),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[InstanceInformationStringFilter]),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # One or more filters. Use a filter to return a more specific list of
    # instances.
    instance_information_filter_list: typing.List["InstanceInformationFilter"
                                                 ] = dataclasses.field(
                                                     default_factory=list,
                                                 )

    # One or more filters. Use a filter to return a more specific list of
    # instances.
    filters: typing.List["InstanceInformationStringFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstanceInformationResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_information_list",
                "InstanceInformationList",
                autoboto.TypeInfo(typing.List[InstanceInformation]),
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

    # The instance information list.
    instance_information_list: typing.List["InstanceInformation"
                                          ] = dataclasses.field(
                                              default_factory=list,
                                          )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstancePatchStatesForPatchGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch_group",
                "PatchGroup",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[InstancePatchStateFilter]),
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

    # The name of the patch group for which the patch state information should be
    # retrieved.
    patch_group: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Each entry in the array is a structure containing:

    # Key (string between 1 and 200 characters)

    # Values (array containing a single string)

    # Type (string "Equal", "NotEqual", "LessThan", "GreaterThan")
    filters: typing.List["InstancePatchStateFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of patches to return (per page).
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstancePatchStatesForPatchGroupResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_patch_states",
                "InstancePatchStates",
                autoboto.TypeInfo(typing.List[InstancePatchState]),
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

    # The high-level patch state for the requested instances.
    instance_patch_states: typing.List["InstancePatchState"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstancePatchStatesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_ids",
                "InstanceIds",
                autoboto.TypeInfo(typing.List[str]),
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

    # The ID of the instance whose patch state information should be retrieved.
    instance_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of instances to return (per page).
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstancePatchStatesResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_patch_states",
                "InstancePatchStates",
                autoboto.TypeInfo(typing.List[InstancePatchState]),
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

    # The high-level patch state for the requested instances.
    instance_patch_states: typing.List["InstancePatchState"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstancePatchesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[PatchOrchestratorFilter]),
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

    # The ID of the instance whose patch state information should be retrieved.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Each entry in the array is a structure containing:

    # Key (string, between 1 and 128 characters)

    # Values (array of strings, each string between 1 and 256 characters)
    filters: typing.List["PatchOrchestratorFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of patches to return (per page).
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstancePatchesResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "patches",
                "Patches",
                autoboto.TypeInfo(typing.List[PatchComplianceData]),
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

    # Each entry in the array is a structure containing:

    # Title (string)

    # KBId (string)

    # Classification (string)

    # Severity (string)

    # State (string: "INSTALLED", "INSTALLED OTHER", "MISSING", "NOT APPLICABLE",
    # "FAILED")

    # InstalledTime (DateTime)

    # InstalledBy (string)
    patches: typing.List["PatchComplianceData"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInventoryDeletionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deletion_id",
                "DeletionId",
                autoboto.TypeInfo(str),
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

    # Specify the delete inventory ID for which you want information. This ID was
    # returned by the `DeleteInventory` action.
    deletion_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInventoryDeletionsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "inventory_deletions",
                "InventoryDeletions",
                autoboto.TypeInfo(typing.List[InventoryDeletionStatusItem]),
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

    # A list of status items for deleted inventory.
    inventory_deletions: typing.List["InventoryDeletionStatusItem"
                                    ] = dataclasses.field(
                                        default_factory=list,
                                    )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowExecutionTaskInvocationsRequest(
    autoboto.ShapeBase
):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_execution_id",
                "WindowExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_id",
                "TaskId",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[MaintenanceWindowFilter]),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window execution the task is part of.
    window_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the specific task in the Maintenance Window task that should be
    # retrieved.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Optional filters used to scope down the returned task invocations. The
    # supported filter key is STATUS with the corresponding values PENDING,
    # IN_PROGRESS, SUCCESS, FAILED, TIMED_OUT, CANCELLING, and CANCELLED.
    filters: typing.List["MaintenanceWindowFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowExecutionTaskInvocationsResult(
    autoboto.OutputShapeBase
):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_execution_task_invocation_identities",
                "WindowExecutionTaskInvocationIdentities",
                autoboto.TypeInfo(
                    typing.List[MaintenanceWindowExecutionTaskInvocationIdentity
                               ]
                ),
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

    # Information about the task invocation results per invocation.
    window_execution_task_invocation_identities: typing.List[
        "MaintenanceWindowExecutionTaskInvocationIdentity"
    ] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowExecutionTasksRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_execution_id",
                "WindowExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[MaintenanceWindowFilter]),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window execution whose task executions should be
    # retrieved.
    window_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional filters used to scope down the returned tasks. The supported
    # filter key is STATUS with the corresponding values PENDING, IN_PROGRESS,
    # SUCCESS, FAILED, TIMED_OUT, CANCELLING, and CANCELLED.
    filters: typing.List["MaintenanceWindowFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowExecutionTasksResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_execution_task_identities",
                "WindowExecutionTaskIdentities",
                autoboto.TypeInfo(
                    typing.List[MaintenanceWindowExecutionTaskIdentity]
                ),
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

    # Information about the task executions.
    window_execution_task_identities: typing.List[
        "MaintenanceWindowExecutionTaskIdentity"
    ] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowExecutionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[MaintenanceWindowFilter]),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window whose executions should be retrieved.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Each entry in the array is a structure containing:

    # Key (string, between 1 and 128 characters)

    # Values (array of strings, each string is between 1 and 256 characters)

    # The supported Keys are ExecutedBefore and ExecutedAfter with the value
    # being a date/time string such as 2016-11-04T05:00:00Z.
    filters: typing.List["MaintenanceWindowFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowExecutionsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_executions",
                "WindowExecutions",
                autoboto.TypeInfo(typing.List[MaintenanceWindowExecution]),
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

    # Information about the Maintenance Windows execution.
    window_executions: typing.List["MaintenanceWindowExecution"
                                  ] = dataclasses.field(
                                      default_factory=list,
                                  )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowTargetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[MaintenanceWindowFilter]),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window whose targets should be retrieved.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Optional filters that can be used to narrow down the scope of the returned
    # window targets. The supported filter keys are Type, WindowTargetId and
    # OwnerInformation.
    filters: typing.List["MaintenanceWindowFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowTargetsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[MaintenanceWindowTarget]),
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

    # Information about the targets in the Maintenance Window.
    targets: typing.List["MaintenanceWindowTarget"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowTasksRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[MaintenanceWindowFilter]),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window whose tasks should be retrieved.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Optional filters used to narrow down the scope of the returned tasks. The
    # supported filter keys are WindowTaskId, TaskArn, Priority, and TaskType.
    filters: typing.List["MaintenanceWindowFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowTasksResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tasks",
                "Tasks",
                autoboto.TypeInfo(typing.List[MaintenanceWindowTask]),
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

    # Information about the tasks in the Maintenance Window.
    tasks: typing.List["MaintenanceWindowTask"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[MaintenanceWindowFilter]),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Optional filters used to narrow down the scope of the returned Maintenance
    # Windows. Supported filter keys are Name and Enabled.
    filters: typing.List["MaintenanceWindowFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_identities",
                "WindowIdentities",
                autoboto.TypeInfo(typing.List[MaintenanceWindowIdentity]),
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

    # Information about the Maintenance Windows.
    window_identities: typing.List["MaintenanceWindowIdentity"
                                  ] = dataclasses.field(
                                      default_factory=list,
                                  )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeParametersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[ParametersFilter]),
            ),
            (
                "parameter_filters",
                "ParameterFilters",
                autoboto.TypeInfo(typing.List[ParameterStringFilter]),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # One or more filters. Use a filter to return a more specific list of
    # results.
    filters: typing.List["ParametersFilter"] = dataclasses.field(
        default_factory=list,
    )

    # Filters to limit the request results.
    parameter_filters: typing.List["ParameterStringFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeParametersResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.List[ParameterMetadata]),
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

    # Parameters returned by the request.
    parameters: typing.List["ParameterMetadata"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePatchBaselinesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[PatchOrchestratorFilter]),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Each element in the array is a structure containing:

    # Key: (string, "NAME_PREFIX" or "OWNER")

    # Value: (array of strings, exactly 1 entry, between 1 and 255 characters)
    filters: typing.List["PatchOrchestratorFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of patch baselines to return (per page).
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePatchBaselinesResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_identities",
                "BaselineIdentities",
                autoboto.TypeInfo(typing.List[PatchBaselineIdentity]),
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

    # An array of PatchBaselineIdentity elements.
    baseline_identities: typing.List["PatchBaselineIdentity"
                                    ] = dataclasses.field(
                                        default_factory=list,
                                    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePatchGroupStateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch_group",
                "PatchGroup",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the patch group whose patch snapshot should be retrieved.
    patch_group: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePatchGroupStateResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instances",
                "Instances",
                autoboto.TypeInfo(int),
            ),
            (
                "instances_with_installed_patches",
                "InstancesWithInstalledPatches",
                autoboto.TypeInfo(int),
            ),
            (
                "instances_with_installed_other_patches",
                "InstancesWithInstalledOtherPatches",
                autoboto.TypeInfo(int),
            ),
            (
                "instances_with_missing_patches",
                "InstancesWithMissingPatches",
                autoboto.TypeInfo(int),
            ),
            (
                "instances_with_failed_patches",
                "InstancesWithFailedPatches",
                autoboto.TypeInfo(int),
            ),
            (
                "instances_with_not_applicable_patches",
                "InstancesWithNotApplicablePatches",
                autoboto.TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of instances in the patch group.
    instances: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances with installed patches.
    instances_with_installed_patches: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of instances with patches installed that aren't defined in the
    # patch baseline.
    instances_with_installed_other_patches: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of instances with missing patches from the patch baseline.
    instances_with_missing_patches: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of instances with patches from the patch baseline that failed to
    # install.
    instances_with_failed_patches: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of instances with patches that aren't applicable.
    instances_with_not_applicable_patches: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribePatchGroupsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[PatchOrchestratorFilter]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The maximum number of patch groups to return (per page).
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more filters. Use a filter to return a more specific list of
    # results.
    filters: typing.List["PatchOrchestratorFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePatchGroupsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "mappings",
                "Mappings",
                autoboto.TypeInfo(typing.List[PatchGroupPatchBaselineMapping]),
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

    # Each entry in the array contains:

    # PatchGroup: string (between 1 and 256 characters, Regex:
    # ^([\p{L}\p{Z}\p{N}_.:/=+\\-@]*)$)

    # PatchBaselineIdentity: A PatchBaselineIdentity element.
    mappings: typing.List["PatchGroupPatchBaselineMapping"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DocumentAlreadyExists(autoboto.ShapeBase):
    """
    The specified document already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DocumentDefaultVersionDescription(autoboto.ShapeBase):
    """
    A default version of a document.
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
                "default_version",
                "DefaultVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The default version of the document.
    default_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DocumentDescription(autoboto.ShapeBase):
    """
    Describes a Systems Manager document.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sha1",
                "Sha1",
                autoboto.TypeInfo(str),
            ),
            (
                "hash",
                "Hash",
                autoboto.TypeInfo(str),
            ),
            (
                "hash_type",
                "HashType",
                autoboto.TypeInfo(DocumentHashType),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(str),
            ),
            (
                "created_date",
                "CreatedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(DocumentStatus),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.List[DocumentParameter]),
            ),
            (
                "platform_types",
                "PlatformTypes",
                autoboto.TypeInfo(typing.List[PlatformType]),
            ),
            (
                "document_type",
                "DocumentType",
                autoboto.TypeInfo(DocumentType),
            ),
            (
                "schema_version",
                "SchemaVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "default_version",
                "DefaultVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "document_format",
                "DocumentFormat",
                autoboto.TypeInfo(DocumentFormat),
            ),
            (
                "target_type",
                "TargetType",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The SHA1 hash of the document, which you can use for verification.
    sha1: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Sha256 or Sha1 hash created by the system when the document was
    # created.

    # Sha1 hashes have been deprecated.
    hash: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Sha256 or Sha1.

    # Sha1 hashes have been deprecated.
    hash_type: "DocumentHashType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The AWS user account that created the document.
    owner: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date when the document was created.
    created_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the Systems Manager document.
    status: "DocumentStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The document version.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A description of the document.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A description of the parameters for a document.
    parameters: typing.List["DocumentParameter"] = dataclasses.field(
        default_factory=list,
    )

    # The list of OS platforms compatible with this Systems Manager document.
    platform_types: typing.List["PlatformType"] = dataclasses.field(
        default_factory=list,
    )

    # The type of document.
    document_type: "DocumentType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The schema version.
    schema_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The latest version of the document.
    latest_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The default version.
    default_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The document format, either JSON or YAML.
    document_format: "DocumentFormat" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The target type which defines the kinds of resources the document can run
    # on. For example, /AWS::EC2::Instance. For a list of valid resource types,
    # see [AWS Resource Types
    # Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # template-resource-type-ref.html) in the _AWS CloudFormation User Guide_.
    target_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tags, or metadata, that have been applied to the document.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DocumentFilter(autoboto.ShapeBase):
    """
    Describes a filter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                autoboto.TypeInfo(DocumentFilterKey),
            ),
            (
                "value",
                "value",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the filter.
    key: "DocumentFilterKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The value of the filter.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class DocumentFilterKey(Enum):
    Name = "Name"
    Owner = "Owner"
    PlatformTypes = "PlatformTypes"
    DocumentType = "DocumentType"


class DocumentFormat(Enum):
    YAML = "YAML"
    JSON = "JSON"


class DocumentHashType(Enum):
    Sha256 = "Sha256"
    Sha1 = "Sha1"


@dataclasses.dataclass
class DocumentIdentifier(autoboto.ShapeBase):
    """
    Describes the name of a Systems Manager document.
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
                "owner",
                "Owner",
                autoboto.TypeInfo(str),
            ),
            (
                "platform_types",
                "PlatformTypes",
                autoboto.TypeInfo(typing.List[PlatformType]),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "document_type",
                "DocumentType",
                autoboto.TypeInfo(DocumentType),
            ),
            (
                "schema_version",
                "SchemaVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "document_format",
                "DocumentFormat",
                autoboto.TypeInfo(DocumentFormat),
            ),
            (
                "target_type",
                "TargetType",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The AWS user account that created the document.
    owner: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The operating system platform.
    platform_types: typing.List["PlatformType"] = dataclasses.field(
        default_factory=list,
    )

    # The document version.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The document type.
    document_type: "DocumentType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The schema version.
    schema_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The document format, either JSON or YAML.
    document_format: "DocumentFormat" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The target type which defines the kinds of resources the document can run
    # on. For example, /AWS::EC2::Instance. For a list of valid resource types,
    # see [AWS Resource Types
    # Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # template-resource-type-ref.html) in the _AWS CloudFormation User Guide_.
    target_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tags, or metadata, that have been applied to the document.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DocumentKeyValuesFilter(autoboto.ShapeBase):
    """
    One or more filters. Use a filter to return a more specific list of documents.

    For keys, you can specify one or more tags that have been applied to a document.

    Other valid values include Owner, Name, PlatformTypes, and DocumentType.

    Note that only one Owner can be specified in a request. For example:
    `Key=Owner,Values=Self`.

    If you use Name as a key, you can use a name prefix to return a list of
    documents. For example, in the AWS CLI, to return a list of all documents that
    begin with `Te`, run the following command:

    `aws ssm list-documents --filters Key=Name,Values=Te`

    If you specify more than two keys, only documents that are identified by all the
    tags are returned in the results. If you specify more than two values for a key,
    documents that are identified by any of the values are returned in the results.

    To specify a custom key and value pair, use the format
    `Key=tag:[tagName],Values=[valueName]`.

    For example, if you created a Key called region and are using the AWS CLI to
    call the `list-documents` command:

    `aws ssm list-documents --filters Key=tag:region,Values=east,west
    Key=Owner,Values=Self`
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

    # The name of the filter key.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value for the filter key.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DocumentLimitExceeded(autoboto.ShapeBase):
    """
    You can have at most 200 active Systems Manager documents.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DocumentParameter(autoboto.ShapeBase):
    """
    Parameters specified in a System Manager document that execute on the server
    when the command is run.
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
                "type",
                "Type",
                autoboto.TypeInfo(DocumentParameterType),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "default_value",
                "DefaultValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the parameter.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of parameter. The type can be either String or StringList.
    type: "DocumentParameterType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A description of what the parameter does, how to use it, the default value,
    # and whether or not the parameter is optional.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If specified, the default values for the parameters. Parameters without a
    # default value are required. Parameters with a default value are optional.
    default_value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class DocumentParameterType(Enum):
    String = "String"
    StringList = "StringList"


@dataclasses.dataclass
class DocumentPermissionLimit(autoboto.ShapeBase):
    """
    The document cannot be shared with more AWS user accounts. You can share a
    document with a maximum of 20 accounts. You can publicly share up to five
    documents. If you need to increase this limit, contact AWS Support.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class DocumentPermissionType(Enum):
    Share = "Share"


class DocumentStatus(Enum):
    Creating = "Creating"
    Active = "Active"
    Updating = "Updating"
    Deleting = "Deleting"


class DocumentType(Enum):
    Command = "Command"
    Policy = "Policy"
    Automation = "Automation"


@dataclasses.dataclass
class DocumentVersionInfo(autoboto.ShapeBase):
    """
    Version information about the document.
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
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "created_date",
                "CreatedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "is_default_version",
                "IsDefaultVersion",
                autoboto.TypeInfo(bool),
            ),
            (
                "document_format",
                "DocumentFormat",
                autoboto.TypeInfo(DocumentFormat),
            ),
        ]

    # The document name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The document version.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date the document was created.
    created_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An identifier for the default version of the document.
    is_default_version: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The document format, either JSON or YAML.
    document_format: "DocumentFormat" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DocumentVersionLimitExceeded(autoboto.ShapeBase):
    """
    The document has too many versions. Delete one or more document versions and try
    again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DoesNotExistException(autoboto.ShapeBase):
    """
    Error returned when the ID specified for a resource, such as a Maintenance
    Window or Patch baseline, doesn't exist.

    For information about resource limits in Systems Manager, see [AWS Systems
    Manager
    Limits](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_ssm).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DuplicateDocumentContent(autoboto.ShapeBase):
    """
    The content of the association document matches another document. Change the
    content of the document and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DuplicateInstanceId(autoboto.ShapeBase):
    """
    You cannot specify an instance ID in more than one association.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EffectivePatch(autoboto.ShapeBase):
    """
    The EffectivePatch structure defines metadata about a patch along with the
    approval state of the patch in a particular patch baseline. The approval state
    includes information about whether the patch is currently approved, due to be
    approved by a rule, explicitly approved, or explicitly rejected and the date the
    patch was or will be approved.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch",
                "Patch",
                autoboto.TypeInfo(Patch),
            ),
            (
                "patch_status",
                "PatchStatus",
                autoboto.TypeInfo(PatchStatus),
            ),
        ]

    # Provides metadata for a patch, including information such as the KB ID,
    # severity, classification and a URL for where more information can be
    # obtained about the patch.
    patch: "Patch" = dataclasses.field(default_factory=dict, )

    # The status of the patch in a patch baseline. This includes information
    # about whether the patch is currently approved, due to be approved by a
    # rule, explicitly approved, or explicitly rejected and the date the patch
    # was or will be approved.
    patch_status: "PatchStatus" = dataclasses.field(default_factory=dict, )


class ExecutionMode(Enum):
    Auto = "Auto"
    Interactive = "Interactive"


@dataclasses.dataclass
class FailedCreateAssociation(autoboto.ShapeBase):
    """
    Describes a failed association.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "entry",
                "Entry",
                autoboto.TypeInfo(CreateAssociationBatchRequestEntry),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "fault",
                "Fault",
                autoboto.TypeInfo(Fault),
            ),
        ]

    # The association.
    entry: "CreateAssociationBatchRequestEntry" = dataclasses.field(
        default_factory=dict,
    )

    # A description of the failure.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The source of the failure.
    fault: "Fault" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FailureDetails(autoboto.ShapeBase):
    """
    Information about an Automation failure.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failure_stage",
                "FailureStage",
                autoboto.TypeInfo(str),
            ),
            (
                "failure_type",
                "FailureType",
                autoboto.TypeInfo(str),
            ),
            (
                "details",
                "Details",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
        ]

    # The stage of the Automation execution when the failure occurred. The stages
    # include the following: InputValidation, PreVerification, Invocation,
    # PostVerification.
    failure_stage: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of Automation failure. Failure types include the following:
    # Action, Permission, Throttling, Verification, Internal.
    failure_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Detailed information about the Automation step failure.
    details: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class Fault(Enum):
    Client = "Client"
    Server = "Server"
    Unknown = "Unknown"


@dataclasses.dataclass
class FeatureNotAvailableException(autoboto.ShapeBase):
    """
    You attempted to register a LAMBDA or STEP_FUNCTION task in a region where the
    corresponding service is not available.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAutomationExecutionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "automation_execution_id",
                "AutomationExecutionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier for an existing automation execution to examine. The
    # execution ID is returned by StartAutomationExecution when the execution of
    # an Automation document is initiated.
    automation_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetAutomationExecutionResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "automation_execution",
                "AutomationExecution",
                autoboto.TypeInfo(AutomationExecution),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Detailed information about the current state of an automation execution.
    automation_execution: "AutomationExecution" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetCommandInvocationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "command_id",
                "CommandId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "plugin_name",
                "PluginName",
                autoboto.TypeInfo(str),
            ),
        ]

    # (Required) The parent command ID of the invocation plugin.
    command_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Required) The ID of the managed instance targeted by the command. A
    # managed instance can be an Amazon EC2 instance or an instance in your
    # hybrid environment that is configured for Systems Manager.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Optional) The name of the plugin for which you want detailed results. If
    # the document contains only one plugin, the name can be omitted and the
    # details will be returned.
    plugin_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCommandInvocationResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "command_id",
                "CommandId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "comment",
                "Comment",
                autoboto.TypeInfo(str),
            ),
            (
                "document_name",
                "DocumentName",
                autoboto.TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "plugin_name",
                "PluginName",
                autoboto.TypeInfo(str),
            ),
            (
                "response_code",
                "ResponseCode",
                autoboto.TypeInfo(int),
            ),
            (
                "execution_start_date_time",
                "ExecutionStartDateTime",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_elapsed_time",
                "ExecutionElapsedTime",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_end_date_time",
                "ExecutionEndDateTime",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(CommandInvocationStatus),
            ),
            (
                "status_details",
                "StatusDetails",
                autoboto.TypeInfo(str),
            ),
            (
                "standard_output_content",
                "StandardOutputContent",
                autoboto.TypeInfo(str),
            ),
            (
                "standard_output_url",
                "StandardOutputUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "standard_error_content",
                "StandardErrorContent",
                autoboto.TypeInfo(str),
            ),
            (
                "standard_error_url",
                "StandardErrorUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "cloud_watch_output_config",
                "CloudWatchOutputConfig",
                autoboto.TypeInfo(CloudWatchOutputConfig),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parent command ID of the invocation plugin.
    command_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the managed instance targeted by the command. A managed instance
    # can be an Amazon EC2 instance or an instance in your hybrid environment
    # that is configured for Systems Manager.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The comment text for the command.
    comment: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the document that was executed. For example, AWS-
    # RunShellScript.
    document_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The SSM document version used in the request.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the plugin for which you want detailed results. For example,
    # aws:RunShellScript is a plugin.
    plugin_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The error level response code for the plugin script. If the response code
    # is -1, then the command has not started executing on the instance, or it
    # was not received by the instance.
    response_code: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date and time the plugin started executing. Date and time are written
    # in ISO 8601 format. For example, June 7, 2017 is represented as 2017-06-7.
    # The following sample AWS CLI command uses the `InvokedBefore` filter.

    # `aws ssm list-commands --filters
    # key=InvokedBefore,value=2017-06-07T00:00:00Z`

    # If the plugin has not started to execute, the string is empty.
    execution_start_date_time: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Duration since ExecutionStartDateTime.
    execution_elapsed_time: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time the plugin was finished executing. Date and time are
    # written in ISO 8601 format. For example, June 7, 2017 is represented as
    # 2017-06-7. The following sample AWS CLI command uses the `InvokedAfter`
    # filter.

    # `aws ssm list-commands --filters
    # key=InvokedAfter,value=2017-06-07T00:00:00Z`

    # If the plugin has not started to execute, the string is empty.
    execution_end_date_time: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of this invocation plugin. This status can be different than
    # StatusDetails.
    status: "CommandInvocationStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A detailed status of the command execution for an invocation. StatusDetails
    # includes more information than Status because it includes states resulting
    # from error and concurrency control parameters. StatusDetails can show
    # different results than Status. For more information about these statuses,
    # see [Understanding Command Statuses](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/monitor-commands.html) in the _AWS Systems Manager
    # User Guide_. StatusDetails can be one of the following values:

    #   * Pending: The command has not been sent to the instance.

    #   * In Progress: The command has been sent to the instance but has not reached a terminal state.

    #   * Delayed: The system attempted to send the command to the target, but the target was not available. The instance might not be available because of network issues, the instance was stopped, etc. The system will try to deliver the command again.

    #   * Success: The command or plugin was executed successfully. This is a terminal state.

    #   * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command's MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.

    #   * Execution Timed Out: The command started to execute on the instance, but the execution was not complete before the timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state.

    #   * Failed: The command wasn't executed successfully on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state.

    #   * Canceled: The command was terminated before it was completed. This is a terminal state.

    #   * Undeliverable: The command can't be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit and don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state.

    #   * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.
    status_details: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The first 24,000 characters written by the plugin to stdout. If the command
    # has not finished executing, if ExecutionStatus is neither Succeeded nor
    # Failed, then this string is empty.
    standard_output_content: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL for the complete text written by the plugin to stdout in Amazon S3.
    # If an Amazon S3 bucket was not specified, then this string is empty.
    standard_output_url: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The first 8,000 characters written by the plugin to stderr. If the command
    # has not finished executing, then this string is empty.
    standard_error_content: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL for the complete text written by the plugin to stderr. If the
    # command has not finished executing, then this string is empty.
    standard_error_url: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # CloudWatch Logs information where Systems Manager sent the command output.
    cloud_watch_output_config: "CloudWatchOutputConfig" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetDefaultPatchBaselineRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operating_system",
                "OperatingSystem",
                autoboto.TypeInfo(OperatingSystem),
            ),
        ]

    # Returns the default patch baseline for the specified operating system.
    operating_system: "OperatingSystem" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDefaultPatchBaselineResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
            (
                "operating_system",
                "OperatingSystem",
                autoboto.TypeInfo(OperatingSystem),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the default patch baseline.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The operating system for the returned patch baseline.
    operating_system: "OperatingSystem" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDeployablePatchSnapshotForInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "snapshot_id",
                "SnapshotId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the instance for which the appropriate patch snapshot should be
    # retrieved.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user-defined snapshot ID.
    snapshot_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeployablePatchSnapshotForInstanceResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "snapshot_id",
                "SnapshotId",
                autoboto.TypeInfo(str),
            ),
            (
                "snapshot_download_url",
                "SnapshotDownloadUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "product",
                "Product",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user-defined snapshot ID.
    snapshot_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A pre-signed Amazon S3 URL that can be used to download the patch snapshot.
    snapshot_download_url: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Returns the specific operating system (for example Windows Server 2012 or
    # Amazon Linux 2015.09) on the instance for the specified patch snapshot.
    product: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDocumentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "document_format",
                "DocumentFormat",
                autoboto.TypeInfo(DocumentFormat),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The document version for which you want information.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Returns the document in the specified format. The document format can be
    # either JSON or YAML. JSON is the default format.
    document_format: "DocumentFormat" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDocumentResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "content",
                "Content",
                autoboto.TypeInfo(str),
            ),
            (
                "document_type",
                "DocumentType",
                autoboto.TypeInfo(DocumentType),
            ),
            (
                "document_format",
                "DocumentFormat",
                autoboto.TypeInfo(DocumentFormat),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The document version.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The contents of the Systems Manager document.
    content: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The document type.
    document_type: "DocumentType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The document format, either JSON or YAML.
    document_format: "DocumentFormat" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetInventoryRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[InventoryFilter]),
            ),
            (
                "aggregators",
                "Aggregators",
                autoboto.TypeInfo(typing.List[InventoryAggregator]),
            ),
            (
                "result_attributes",
                "ResultAttributes",
                autoboto.TypeInfo(typing.List[ResultAttribute]),
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

    # One or more filters. Use a filter to return a more specific list of
    # results.
    filters: typing.List["InventoryFilter"] = dataclasses.field(
        default_factory=list,
    )

    # Returns counts of inventory types based on one or more expressions. For
    # example, if you aggregate by using an expression that uses the
    # `AWS:InstanceInformation.PlatformType` type, you can see a count of how
    # many Windows and Linux instances exist in your inventoried fleet.
    aggregators: typing.List["InventoryAggregator"] = dataclasses.field(
        default_factory=list,
    )

    # The list of inventory item types to return.
    result_attributes: typing.List["ResultAttribute"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInventoryResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "entities",
                "Entities",
                autoboto.TypeInfo(typing.List[InventoryResultEntity]),
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

    # Collection of inventory entities such as a collection of instance
    # inventory.
    entities: typing.List["InventoryResultEntity"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInventorySchemaRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                autoboto.TypeInfo(str),
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
            (
                "aggregator",
                "Aggregator",
                autoboto.TypeInfo(bool),
            ),
            (
                "sub_type",
                "SubType",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The type of inventory item to return.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Returns inventory schemas that support aggregation. For example, this call
    # returns the `AWS:InstanceInformation` type, because it supports aggregation
    # based on the `PlatformName`, `PlatformType`, and `PlatformVersion`
    # attributes.
    aggregator: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Returns the sub-type schema for a specified inventory type.
    sub_type: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInventorySchemaResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "schemas",
                "Schemas",
                autoboto.TypeInfo(typing.List[InventoryItemSchema]),
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

    # Inventory schemas returned by the request.
    schemas: typing.List["InventoryItemSchema"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMaintenanceWindowExecutionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_execution_id",
                "WindowExecutionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window execution that includes the task.
    window_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetMaintenanceWindowExecutionResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_execution_id",
                "WindowExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_ids",
                "TaskIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(MaintenanceWindowExecutionStatus),
            ),
            (
                "status_details",
                "StatusDetails",
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
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the Maintenance Window execution.
    window_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the task executions from the Maintenance Window execution.
    task_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The status of the Maintenance Window execution.
    status: "MaintenanceWindowExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details explaining the Status. Only available for certain status
    # values.
    status_details: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the Maintenance Window started executing.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the Maintenance Window finished executing.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetMaintenanceWindowExecutionTaskInvocationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_execution_id",
                "WindowExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_id",
                "TaskId",
                autoboto.TypeInfo(str),
            ),
            (
                "invocation_id",
                "InvocationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window execution for which the task is a part.
    window_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the specific task in the Maintenance Window task that should be
    # retrieved.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The invocation ID to retrieve.
    invocation_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMaintenanceWindowExecutionTaskInvocationResult(
    autoboto.OutputShapeBase
):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_execution_id",
                "WindowExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_execution_id",
                "TaskExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "invocation_id",
                "InvocationId",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_id",
                "ExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_type",
                "TaskType",
                autoboto.TypeInfo(MaintenanceWindowTaskType),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(MaintenanceWindowExecutionStatus),
            ),
            (
                "status_details",
                "StatusDetails",
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
                "owner_information",
                "OwnerInformation",
                autoboto.TypeInfo(str),
            ),
            (
                "window_target_id",
                "WindowTargetId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Maintenance Window execution ID.
    window_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The task execution ID.
    task_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The invocation ID.
    invocation_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The execution ID.
    execution_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Retrieves the task type for a Maintenance Window. Task types include the
    # following: LAMBDA, STEP_FUNCTION, AUTOMATION, RUN_COMMAND.
    task_type: "MaintenanceWindowTaskType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameters used at the time that the task executed.
    parameters: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The task status for an invocation.
    status: "MaintenanceWindowExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details explaining the status. Details are only available for certain
    # status values.
    status_details: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time that the task started executing on the target.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time that the task finished executing on the target.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # User-provided value to be included in any CloudWatch events raised while
    # running tasks for these targets in this Maintenance Window.
    owner_information: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Maintenance Window target ID.
    window_target_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetMaintenanceWindowExecutionTaskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_execution_id",
                "WindowExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_id",
                "TaskId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window execution that includes the task.
    window_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the specific task execution in the Maintenance Window task that
    # should be retrieved.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMaintenanceWindowExecutionTaskResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_execution_id",
                "WindowExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_execution_id",
                "TaskExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_arn",
                "TaskArn",
                autoboto.TypeInfo(str),
            ),
            (
                "service_role",
                "ServiceRole",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(MaintenanceWindowTaskType),
            ),
            (
                "task_parameters",
                "TaskParameters",
                autoboto.TypeInfo(
                    typing.List[typing.Dict[
                        str, MaintenanceWindowTaskParameterValueExpression
                    ]]
                ),
            ),
            (
                "priority",
                "Priority",
                autoboto.TypeInfo(int),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                autoboto.TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(MaintenanceWindowExecutionStatus),
            ),
            (
                "status_details",
                "StatusDetails",
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
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the Maintenance Window execution that includes the task.
    window_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the specific task execution in the Maintenance Window task that
    # was retrieved.
    task_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the executed task.
    task_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The role that was assumed when executing the task.
    service_role: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of task executed.
    type: "MaintenanceWindowTaskType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameters passed to the task when it was executed.

    # `TaskParameters` has been deprecated. To specify parameters to pass to a
    # task when it runs, instead use the `Parameters` option in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.

    # The map has the following format:

    # Key: string, between 1 and 255 characters

    # Value: an array of strings, each string is between 1 and 255 characters
    task_parameters: typing.List[
        typing.Dict[str, "MaintenanceWindowTaskParameterValueExpression"]
    ] = dataclasses.field(
        default_factory=list,
    )

    # The priority of the task.
    priority: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The defined maximum number of task executions that could be run in
    # parallel.
    max_concurrency: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The defined maximum number of task execution errors allowed before
    # scheduling of the task execution would have been stopped.
    max_errors: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the task.
    status: "MaintenanceWindowExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details explaining the Status. Only available for certain status
    # values.
    status_details: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the task execution started.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the task execution completed.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetMaintenanceWindowRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the desired Maintenance Window.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMaintenanceWindowResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                autoboto.TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(int),
            ),
            (
                "cutoff",
                "Cutoff",
                autoboto.TypeInfo(int),
            ),
            (
                "allow_unassociated_targets",
                "AllowUnassociatedTargets",
                autoboto.TypeInfo(bool),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "created_date",
                "CreatedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "modified_date",
                "ModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the created Maintenance Window.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the Maintenance Window.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the Maintenance Window.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The schedule of the Maintenance Window in the form of a cron or rate
    # expression.
    schedule: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The duration of the Maintenance Window in hours.
    duration: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of hours before the end of the Maintenance Window that Systems
    # Manager stops scheduling new tasks for execution.
    cutoff: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether targets must be registered with the Maintenance Window before tasks
    # can be defined for those targets.
    allow_unassociated_targets: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether the Maintenance Windows is enabled.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date the Maintenance Window was created.
    created_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date the Maintenance Window was last modified.
    modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetMaintenanceWindowTaskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "window_task_id",
                "WindowTaskId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Maintenance Window ID that includes the task to retrieve.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Maintenance Window task ID to retrieve.
    window_task_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetMaintenanceWindowTaskResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "window_task_id",
                "WindowTaskId",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "task_arn",
                "TaskArn",
                autoboto.TypeInfo(str),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "task_type",
                "TaskType",
                autoboto.TypeInfo(MaintenanceWindowTaskType),
            ),
            (
                "task_parameters",
                "TaskParameters",
                autoboto.TypeInfo(
                    typing.Dict[str,
                                MaintenanceWindowTaskParameterValueExpression]
                ),
            ),
            (
                "task_invocation_parameters",
                "TaskInvocationParameters",
                autoboto.TypeInfo(MaintenanceWindowTaskInvocationParameters),
            ),
            (
                "priority",
                "Priority",
                autoboto.TypeInfo(int),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                autoboto.TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                autoboto.TypeInfo(str),
            ),
            (
                "logging_info",
                "LoggingInfo",
                autoboto.TypeInfo(LoggingInfo),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The retrieved Maintenance Window ID.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The retrieved Maintenance Window task ID.
    window_task_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The targets where the task should execute.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # The resource that the task used during execution. For RUN_COMMAND and
    # AUTOMATION task types, the TaskArn is the Systems Manager Document
    # name/ARN. For LAMBDA tasks, the value is the function name/ARN. For
    # STEP_FUNCTION tasks, the value is the state machine ARN.
    task_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The IAM service role to assume during task execution.
    service_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of task to execute.
    task_type: "MaintenanceWindowTaskType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameters to pass to the task when it executes.

    # `TaskParameters` has been deprecated. To specify parameters to pass to a
    # task when it runs, instead use the `Parameters` option in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    task_parameters: typing.Dict[
        str, "MaintenanceWindowTaskParameterValueExpression"
    ] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameters to pass to the task when it executes.
    task_invocation_parameters: "MaintenanceWindowTaskInvocationParameters" = dataclasses.field(
        default_factory=dict,
    )

    # The priority of the task when it executes. The lower the number, the higher
    # the priority. Tasks that have the same priority are scheduled in parallel.
    priority: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of targets allowed to run this task in parallel.
    max_concurrency: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of errors allowed before the task stops being scheduled.
    max_errors: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The location in Amazon S3 where the task results are logged.

    # `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    # instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    logging_info: "LoggingInfo" = dataclasses.field(default_factory=dict, )

    # The retrieved task name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The retrieved task description.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetParameterHistoryRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "with_decryption",
                "WithDecryption",
                autoboto.TypeInfo(bool),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of a parameter you want to query.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Return decrypted values for secure string parameters. This flag is ignored
    # for String and StringList parameter types.
    with_decryption: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetParameterHistoryResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.List[ParameterHistory]),
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

    # A list of parameters returned by the request.
    parameters: typing.List["ParameterHistory"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetParameterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "with_decryption",
                "WithDecryption",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the parameter you want to query.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Return decrypted values for secure string parameters. This flag is ignored
    # for String and StringList parameter types.
    with_decryption: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetParameterResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "parameter",
                "Parameter",
                autoboto.TypeInfo(Parameter),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about a parameter.
    parameter: "Parameter" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetParametersByPathRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                autoboto.TypeInfo(str),
            ),
            (
                "recursive",
                "Recursive",
                autoboto.TypeInfo(bool),
            ),
            (
                "parameter_filters",
                "ParameterFilters",
                autoboto.TypeInfo(typing.List[ParameterStringFilter]),
            ),
            (
                "with_decryption",
                "WithDecryption",
                autoboto.TypeInfo(bool),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The hierarchy for the parameter. Hierarchies start with a forward slash (/)
    # and end with the parameter name. A parameter name hierarchy can have a
    # maximum of 15 levels. Here is an example of a hierarchy:
    # `/Finance/Prod/IAD/WinServ2016/license33`
    path: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Retrieve all parameters within a hierarchy.

    # If a user has access to a path, then the user can access all levels of that
    # path. For example, if a user has permission to access path /a, then the
    # user can also access /a/b. Even if a user has explicitly been denied access
    # in IAM for parameter /a, they can still call the GetParametersByPath API
    # action recursively and view /a/b.
    recursive: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filters to limit the request results.

    # You can't filter using the parameter name.
    parameter_filters: typing.List["ParameterStringFilter"] = dataclasses.field(
        default_factory=list,
    )

    # Retrieve all parameters in a hierarchy with their value decrypted.
    with_decryption: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetParametersByPathResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.List[Parameter]),
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

    # A list of parameters found in the specified hierarchy.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetParametersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "with_decryption",
                "WithDecryption",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Names of the parameters for which you want to query information.
    names: typing.List[str] = dataclasses.field(default_factory=list, )

    # Return decrypted secure string value. Return decrypted values for secure
    # string parameters. This flag is ignored for String and StringList parameter
    # types.
    with_decryption: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetParametersResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.List[Parameter]),
            ),
            (
                "invalid_parameters",
                "InvalidParameters",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of details for a parameter.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default_factory=list,
    )

    # A list of parameters that are not formatted correctly or do not run when
    # executed.
    invalid_parameters: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetPatchBaselineForPatchGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch_group",
                "PatchGroup",
                autoboto.TypeInfo(str),
            ),
            (
                "operating_system",
                "OperatingSystem",
                autoboto.TypeInfo(OperatingSystem),
            ),
        ]

    # The name of the patch group whose patch baseline should be retrieved.
    patch_group: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Returns he operating system rule specified for patch groups using the patch
    # baseline.
    operating_system: "OperatingSystem" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetPatchBaselineForPatchGroupResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
            (
                "patch_group",
                "PatchGroup",
                autoboto.TypeInfo(str),
            ),
            (
                "operating_system",
                "OperatingSystem",
                autoboto.TypeInfo(OperatingSystem),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the patch baseline that should be used for the patch group.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the patch group.
    patch_group: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The operating system rule specified for patch groups using the patch
    # baseline.
    operating_system: "OperatingSystem" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetPatchBaselineRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the patch baseline to retrieve.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPatchBaselineResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "operating_system",
                "OperatingSystem",
                autoboto.TypeInfo(OperatingSystem),
            ),
            (
                "global_filters",
                "GlobalFilters",
                autoboto.TypeInfo(PatchFilterGroup),
            ),
            (
                "approval_rules",
                "ApprovalRules",
                autoboto.TypeInfo(PatchRuleGroup),
            ),
            (
                "approved_patches",
                "ApprovedPatches",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "approved_patches_compliance_level",
                "ApprovedPatchesComplianceLevel",
                autoboto.TypeInfo(PatchComplianceLevel),
            ),
            (
                "approved_patches_enable_non_security",
                "ApprovedPatchesEnableNonSecurity",
                autoboto.TypeInfo(bool),
            ),
            (
                "rejected_patches",
                "RejectedPatches",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "patch_groups",
                "PatchGroups",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "created_date",
                "CreatedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "modified_date",
                "ModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "sources",
                "Sources",
                autoboto.TypeInfo(typing.List[PatchSource]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the retrieved patch baseline.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the patch baseline.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Returns the operating system specified for the patch baseline.
    operating_system: "OperatingSystem" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A set of global filters used to exclude patches from the baseline.
    global_filters: "PatchFilterGroup" = dataclasses.field(
        default_factory=dict,
    )

    # A set of rules used to include patches in the baseline.
    approval_rules: "PatchRuleGroup" = dataclasses.field(default_factory=dict, )

    # A list of explicitly approved patches for the baseline.
    approved_patches: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Returns the specified compliance severity level for approved patches in the
    # patch baseline.
    approved_patches_compliance_level: "PatchComplianceLevel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the list of approved patches includes non-security
    # updates that should be applied to the instances. The default value is
    # 'false'. Applies to Linux instances only.
    approved_patches_enable_non_security: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of explicitly rejected patches for the baseline.
    rejected_patches: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Patch groups included in the patch baseline.
    patch_groups: typing.List[str] = dataclasses.field(default_factory=list, )

    # The date the patch baseline was created.
    created_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date the patch baseline was last modified.
    modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A description of the patch baseline.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Information about the patches to use to update the instances, including
    # target operating systems and source repositories. Applies to Linux
    # instances only.
    sources: typing.List["PatchSource"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class HierarchyLevelLimitExceededException(autoboto.ShapeBase):
    """
    A hierarchy can have a maximum of 15 levels. For more information, see
    [Requirements and Constraints for Parameter
    Names](http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-
    parameter-name-constraints.html) in the _AWS Systems Manager User Guide_.
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

    # A hierarchy can have a maximum of 15 levels. For more information, see
    # [Requirements and Constraints for Parameter
    # Names](http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-
    # parameter-name-constraints.html) in the _AWS Systems Manager User Guide_.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HierarchyTypeMismatchException(autoboto.ShapeBase):
    """
    Parameter Store does not support changing a parameter type in a hierarchy. For
    example, you can't change a parameter from a String type to a SecureString type.
    You must create a new, unique parameter.
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

    # Parameter Store does not support changing a parameter type in a hierarchy.
    # For example, you can't change a parameter from a String type to a
    # SecureString type. You must create a new, unique parameter.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IdempotentParameterMismatch(autoboto.ShapeBase):
    """
    Error returned when an idempotent operation is retried and the parameters don't
    match the original call to the API with the same idempotency token.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstanceAggregatedAssociationOverview(autoboto.ShapeBase):
    """
    Status information about the aggregated associations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detailed_status",
                "DetailedStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_association_status_aggregated_count",
                "InstanceAssociationStatusAggregatedCount",
                autoboto.TypeInfo(typing.Dict[str, int]),
            ),
        ]

    # Detailed status information about the aggregated associations.
    detailed_status: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of associations for the instance(s).
    instance_association_status_aggregated_count: typing.Dict[
        str, int
    ] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceAssociation(autoboto.ShapeBase):
    """
    One or more association documents on the instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "content",
                "Content",
                autoboto.TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The association ID.
    association_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The content of the association document for the instance(s).
    content: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Version information for the association on the instance.
    association_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceAssociationOutputLocation(autoboto.ShapeBase):
    """
    An Amazon S3 bucket where you want to store the results of this request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_location",
                "S3Location",
                autoboto.TypeInfo(S3OutputLocation),
            ),
        ]

    # An Amazon S3 bucket where you want to store the results of this request.
    s3_location: "S3OutputLocation" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class InstanceAssociationOutputUrl(autoboto.ShapeBase):
    """
    The URL of Amazon S3 bucket where you want to store the results of this request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_output_url",
                "S3OutputUrl",
                autoboto.TypeInfo(S3OutputUrl),
            ),
        ]

    # The URL of Amazon S3 bucket where you want to store the results of this
    # request.
    s3_output_url: "S3OutputUrl" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class InstanceAssociationStatusInfo(autoboto.ShapeBase):
    """
    Status information about the instance association.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_date",
                "ExecutionDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
            (
                "detailed_status",
                "DetailedStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_summary",
                "ExecutionSummary",
                autoboto.TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "output_url",
                "OutputUrl",
                autoboto.TypeInfo(InstanceAssociationOutputUrl),
            ),
            (
                "association_name",
                "AssociationName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The association ID.
    association_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the association.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The association document verions.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The version of the association applied to the instance.
    association_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance ID where the association was created.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date the instance association executed.
    execution_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Status information about the instance association.
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Detailed status information about the instance association.
    detailed_status: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Summary information about association execution.
    execution_summary: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An error code returned by the request to create the association.
    error_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A URL for an Amazon S3 bucket where you want to store the results of this
    # request.
    output_url: "InstanceAssociationOutputUrl" = dataclasses.field(
        default_factory=dict,
    )

    # The name of the association applied to the instance.
    association_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceInformation(autoboto.ShapeBase):
    """
    Describes a filter for a specific list of instances.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "ping_status",
                "PingStatus",
                autoboto.TypeInfo(PingStatus),
            ),
            (
                "last_ping_date_time",
                "LastPingDateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "agent_version",
                "AgentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "is_latest_version",
                "IsLatestVersion",
                autoboto.TypeInfo(bool),
            ),
            (
                "platform_type",
                "PlatformType",
                autoboto.TypeInfo(PlatformType),
            ),
            (
                "platform_name",
                "PlatformName",
                autoboto.TypeInfo(str),
            ),
            (
                "platform_version",
                "PlatformVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "activation_id",
                "ActivationId",
                autoboto.TypeInfo(str),
            ),
            (
                "iam_role",
                "IamRole",
                autoboto.TypeInfo(str),
            ),
            (
                "registration_date",
                "RegistrationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "ip_address",
                "IPAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "computer_name",
                "ComputerName",
                autoboto.TypeInfo(str),
            ),
            (
                "association_status",
                "AssociationStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "last_association_execution_date",
                "LastAssociationExecutionDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_successful_association_execution_date",
                "LastSuccessfulAssociationExecutionDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "association_overview",
                "AssociationOverview",
                autoboto.TypeInfo(InstanceAggregatedAssociationOverview),
            ),
        ]

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Connection status of SSM Agent.
    ping_status: "PingStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time when agent last pinged Systems Manager service.
    last_ping_date_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The version of SSM Agent running on your Linux instance.
    agent_version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether latest version of SSM Agent is running on your instance.
    # Some older versions of Windows Server use the EC2Config service to process
    # SSM requests. For this reason, this field does not indicate whether or not
    # the latest version is installed on Windows managed instances.
    is_latest_version: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The operating system platform type.
    platform_type: "PlatformType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the operating system platform running on your instance.
    platform_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version of the OS platform running on your instance.
    platform_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The activation ID created by Systems Manager when the server or VM was
    # registered.
    activation_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Identity and Access Management (IAM) role assigned to the on-
    # premises Systems Manager managed instances. This call does not return the
    # IAM role for Amazon EC2 instances.
    iam_role: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date the server or VM was registered with AWS as a managed instance.
    registration_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of instance. Instances are either EC2 instances or managed
    # instances.
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the managed instance.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The IP address of the managed instance.
    ip_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The fully qualified host name of the managed instance.
    computer_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the association.
    association_status: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date the association was last executed.
    last_association_execution_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The last date the association was successfully run.
    last_successful_association_execution_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the association.
    association_overview: "InstanceAggregatedAssociationOverview" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class InstanceInformationFilter(autoboto.ShapeBase):
    """
    Describes a filter for a specific list of instances.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                autoboto.TypeInfo(InstanceInformationFilterKey),
            ),
            (
                "value_set",
                "valueSet",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the filter.
    key: "InstanceInformationFilterKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The filter values.
    value_set: typing.List[str] = dataclasses.field(default_factory=list, )


class InstanceInformationFilterKey(Enum):
    InstanceIds = "InstanceIds"
    AgentVersion = "AgentVersion"
    PingStatus = "PingStatus"
    PlatformTypes = "PlatformTypes"
    ActivationIds = "ActivationIds"
    IamRole = "IamRole"
    ResourceType = "ResourceType"
    AssociationStatus = "AssociationStatus"


@dataclasses.dataclass
class InstanceInformationStringFilter(autoboto.ShapeBase):
    """
    The filters to describe or get information about your managed instances.
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

    # The filter key name to describe your instances. For example:

    # "InstanceIds"|"AgentVersion"|"PingStatus"|"PlatformTypes"|"ActivationIds"|"IamRole"|"ResourceType"|"AssociationStatus"|"Tag
    # Key"
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The filter values.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class InstancePatchState(autoboto.ShapeBase):
    """
    Defines the high-level patch compliance state for a managed instance, providing
    information about the number of installed, missing, not applicable, and failed
    patches along with metadata about the operation when this information was
    gathered for the instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "patch_group",
                "PatchGroup",
                autoboto.TypeInfo(str),
            ),
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
            (
                "operation_start_time",
                "OperationStartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "operation_end_time",
                "OperationEndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "operation",
                "Operation",
                autoboto.TypeInfo(PatchOperationType),
            ),
            (
                "snapshot_id",
                "SnapshotId",
                autoboto.TypeInfo(str),
            ),
            (
                "owner_information",
                "OwnerInformation",
                autoboto.TypeInfo(str),
            ),
            (
                "installed_count",
                "InstalledCount",
                autoboto.TypeInfo(int),
            ),
            (
                "installed_other_count",
                "InstalledOtherCount",
                autoboto.TypeInfo(int),
            ),
            (
                "missing_count",
                "MissingCount",
                autoboto.TypeInfo(int),
            ),
            (
                "failed_count",
                "FailedCount",
                autoboto.TypeInfo(int),
            ),
            (
                "not_applicable_count",
                "NotApplicableCount",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the managed instance the high-level patch compliance information
    # was collected for.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the patch group the managed instance belongs to.
    patch_group: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the patch baseline used to patch the instance.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time the most recent patching operation was started on the instance.
    operation_start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the most recent patching operation completed on the instance.
    operation_end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of patching operation that was performed: SCAN (assess patch
    # compliance state) or INSTALL (install missing patches).
    operation: "PatchOperationType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the patch baseline snapshot used during the patching operation
    # when this compliance data was collected.
    snapshot_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placeholder information. This field will always be empty in the current
    # release of the service.
    owner_information: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of patches from the patch baseline that are installed on the
    # instance.
    installed_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of patches not specified in the patch baseline that are
    # installed on the instance.
    installed_other_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of patches from the patch baseline that are applicable for the
    # instance but aren't currently installed.
    missing_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of patches from the patch baseline that were attempted to be
    # installed during the last patching operation, but failed to install.
    failed_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of patches from the patch baseline that aren't applicable for
    # the instance and hence aren't installed on the instance.
    not_applicable_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstancePatchStateFilter(autoboto.ShapeBase):
    """
    Defines a filter used in DescribeInstancePatchStatesForPatchGroup used to scope
    down the information returned by the API.
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
            (
                "type",
                "Type",
                autoboto.TypeInfo(InstancePatchStateOperatorType),
            ),
        ]

    # The key for the filter. Supported values are FailedCount, InstalledCount,
    # InstalledOtherCount, MissingCount and NotApplicableCount.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value for the filter, must be an integer greater than or equal to 0.
    values: typing.List[str] = dataclasses.field(default_factory=list, )

    # The type of comparison that should be performed for the value: Equal,
    # NotEqual, LessThan or GreaterThan.
    type: "InstancePatchStateOperatorType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class InstancePatchStateOperatorType(Enum):
    Equal = "Equal"
    NotEqual = "NotEqual"
    LessThan = "LessThan"
    GreaterThan = "GreaterThan"


@dataclasses.dataclass
class InternalServerError(autoboto.ShapeBase):
    """
    An error occurred on the server side.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidActivation(autoboto.ShapeBase):
    """
    The activation is not valid. The activation might have been deleted, or the
    ActivationId and the ActivationCode do not match.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidActivationId(autoboto.ShapeBase):
    """
    The activation ID is not valid. Verify the you entered the correct ActivationId
    or ActivationCode and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidAggregatorException(autoboto.ShapeBase):
    """
    The specified aggregator is not valid for inventory groups. Verify that the
    aggregator uses a valid inventory type such as `AWS:Application` or
    `AWS:InstanceInformation`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidAllowedPatternException(autoboto.ShapeBase):
    """
    The request does not meet the regular expression requirement.
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

    # The request does not meet the regular expression requirement.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidAssociation(autoboto.ShapeBase):
    """
    The association is not valid or does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidAssociationVersion(autoboto.ShapeBase):
    """
    The version you specified is not valid. Use ListAssociationVersions to view all
    versions of an association according to the association ID. Or, use the
    `$LATEST` parameter to view the latest version of the association.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidAutomationExecutionParametersException(autoboto.ShapeBase):
    """
    The supplied parameters for invoking the specified Automation document are
    incorrect. For example, they may not match the set of parameters permitted for
    the specified Automation document.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidAutomationSignalException(autoboto.ShapeBase):
    """
    The signal is not valid for the current Automation execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidAutomationStatusUpdateException(autoboto.ShapeBase):
    """
    The specified update status operation is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidCommandId(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDeleteInventoryParametersException(autoboto.ShapeBase):
    """
    One or more of the parameters specified for the delete operation is not valid.
    Verify all parameters and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidDeletionIdException(autoboto.ShapeBase):
    """
    The ID specified for the delete operation does not exist or is not valide.
    Verify the ID and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidDocument(autoboto.ShapeBase):
    """
    The specified document does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The document does not exist or the document is not available to the user.
    # This exception can be issued by CreateAssociation, CreateAssociationBatch,
    # DeleteAssociation, DeleteDocument, DescribeAssociation, DescribeDocument,
    # GetDocument, SendCommand, or UpdateAssociationStatus.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidDocumentContent(autoboto.ShapeBase):
    """
    The content for the document is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # A description of the validation error.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidDocumentOperation(autoboto.ShapeBase):
    """
    You attempted to delete a document while it is still shared. You must stop
    sharing the document before you can delete it.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidDocumentSchemaVersion(autoboto.ShapeBase):
    """
    The version of the document schema is not supported.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidDocumentVersion(autoboto.ShapeBase):
    """
    The document version is not valid or does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidFilter(autoboto.ShapeBase):
    """
    The filter name is not valid. Verify the you entered the correct name and try
    again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidFilterKey(autoboto.ShapeBase):
    """
    The specified key is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidFilterOption(autoboto.ShapeBase):
    """
    The specified filter option is not valid. Valid options are Equals and
    BeginsWith. For Path filter, valid options are Recursive and OneLevel.
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

    # The specified filter option is not valid. Valid options are Equals and
    # BeginsWith. For Path filter, valid options are Recursive and OneLevel.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidFilterValue(autoboto.ShapeBase):
    """
    The filter value is not valid. Verify the value and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidInstanceId(autoboto.ShapeBase):
    """
    The following problems can cause this exception:

    You do not have permission to access the instance.

    SSM Agent is not running. On managed instances and Linux instances, verify that
    the SSM Agent is running. On EC2 Windows instances, verify that the EC2Config
    service is running.

    SSM Agent or EC2Config service is not registered to the SSM endpoint. Try
    reinstalling SSM Agent or EC2Config service.

    The instance is not in valid state. Valid states are: Running, Pending, Stopped,
    Stopping. Invalid states are: Shutting-down and Terminated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidInstanceInformationFilterValue(autoboto.ShapeBase):
    """
    The specified filter value is not valid.
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
class InvalidInventoryGroupException(autoboto.ShapeBase):
    """
    The specified inventory group is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidInventoryItemContextException(autoboto.ShapeBase):
    """
    You specified invalid keys or values in the `Context` attribute for
    `InventoryItem`. Verify the keys and values, and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidInventoryRequestException(autoboto.ShapeBase):
    """
    The request is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidItemContentException(autoboto.ShapeBase):
    """
    One or more content items is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    type_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidKeyId(autoboto.ShapeBase):
    """
    The query key ID is not valid.
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
class InvalidNextToken(autoboto.ShapeBase):
    """
    The specified token is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidNotificationConfig(autoboto.ShapeBase):
    """
    One or more configuration items is not valid. Verify that a valid Amazon
    Resource Name (ARN) was provided for an Amazon SNS topic.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidOptionException(autoboto.ShapeBase):
    """
    The delete inventory option specified is not valid. Verify the option and try
    again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidOutputFolder(autoboto.ShapeBase):
    """
    The S3 bucket does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidOutputLocation(autoboto.ShapeBase):
    """
    The output location is not valid or does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidParameters(autoboto.ShapeBase):
    """
    You must specify values for all required parameters in the Systems Manager
    document. You can only supply values to parameters defined in the Systems
    Manager document.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidPermissionType(autoboto.ShapeBase):
    """
    The permission type is not supported. _Share_ is the only supported permission
    type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidPluginName(autoboto.ShapeBase):
    """
    The plugin name is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidResourceId(autoboto.ShapeBase):
    """
    The resource ID is not valid. Verify that you entered the correct ID and try
    again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidResourceType(autoboto.ShapeBase):
    """
    The resource type is not valid. For example, if you are attempting to tag an
    instance, the instance must be a registered, managed instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidResultAttributeException(autoboto.ShapeBase):
    """
    The specified inventory item result attribute is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRole(autoboto.ShapeBase):
    """
    The role name can't contain invalid characters. Also verify that you specified
    an IAM role for notifications that includes the required trust policy. For
    information about configuring the IAM role for Run Command notifications, see
    [Configuring Amazon SNS Notifications for Run
    Command](http://docs.aws.amazon.com/systems-manager/latest/userguide/rc-sns-
    notifications.html) in the _AWS Systems Manager User Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidSchedule(autoboto.ShapeBase):
    """
    The schedule is invalid. Verify your cron or rate expression and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidTarget(autoboto.ShapeBase):
    """
    The target is not valid or does not exist. It might not be configured for EC2
    Systems Manager or you might not have permission to perform the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidTypeNameException(autoboto.ShapeBase):
    """
    The parameter type name is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidUpdate(autoboto.ShapeBase):
    """
    The update is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InventoryAggregator(autoboto.ShapeBase):
    """
    Specifies the inventory type and attribute for the aggregation execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "expression",
                "Expression",
                autoboto.TypeInfo(str),
            ),
            (
                "aggregators",
                "Aggregators",
                autoboto.TypeInfo(typing.List[InventoryAggregator]),
            ),
            (
                "groups",
                "Groups",
                autoboto.TypeInfo(typing.List[InventoryGroup]),
            ),
        ]

    # The inventory type and attribute name for aggregation.
    expression: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Nested aggregators to further refine aggregation for an inventory type.
    aggregators: typing.List["InventoryAggregator"] = dataclasses.field(
        default_factory=list,
    )

    # A user-defined set of one or more filters on which to aggregate inventory
    # data. Groups return a count of resources that match and don't match the
    # specified criteria.
    groups: typing.List["InventoryGroup"] = dataclasses.field(
        default_factory=list,
    )


class InventoryAttributeDataType(Enum):
    string = "string"
    number = "number"


class InventoryDeletionStatus(Enum):
    InProgress = "InProgress"
    Complete = "Complete"


@dataclasses.dataclass
class InventoryDeletionStatusItem(autoboto.ShapeBase):
    """
    Status information returned by the `DeleteInventory` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deletion_id",
                "DeletionId",
                autoboto.TypeInfo(str),
            ),
            (
                "type_name",
                "TypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "deletion_start_time",
                "DeletionStartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_status",
                "LastStatus",
                autoboto.TypeInfo(InventoryDeletionStatus),
            ),
            (
                "last_status_message",
                "LastStatusMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "deletion_summary",
                "DeletionSummary",
                autoboto.TypeInfo(InventoryDeletionSummary),
            ),
            (
                "last_status_update_time",
                "LastStatusUpdateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The deletion ID returned by the `DeleteInventory` action.
    deletion_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the inventory data type.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The UTC timestamp when the delete operation started.
    deletion_start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the operation. Possible values are InProgress and Complete.
    last_status: "InventoryDeletionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the status.
    last_status_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the delete operation. For more information about this
    # summary, see [Understanding the Delete Inventory
    # Summary](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/sysman-inventory-delete.html#sysman-inventory-
    # delete-summary) in the _AWS Systems Manager User Guide_.
    deletion_summary: "InventoryDeletionSummary" = dataclasses.field(
        default_factory=dict,
    )

    # The UTC timestamp of when the last status report.
    last_status_update_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InventoryDeletionSummary(autoboto.ShapeBase):
    """
    Information about the delete operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "total_count",
                "TotalCount",
                autoboto.TypeInfo(int),
            ),
            (
                "remaining_count",
                "RemainingCount",
                autoboto.TypeInfo(int),
            ),
            (
                "summary_items",
                "SummaryItems",
                autoboto.TypeInfo(typing.List[InventoryDeletionSummaryItem]),
            ),
        ]

    # The total number of items to delete. This count does not change during the
    # delete operation.
    total_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Remaining number of items to delete.
    remaining_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of counts and versions for deleted items.
    summary_items: typing.List["InventoryDeletionSummaryItem"
                              ] = dataclasses.field(
                                  default_factory=list,
                              )


@dataclasses.dataclass
class InventoryDeletionSummaryItem(autoboto.ShapeBase):
    """
    Either a count, remaining count, or a version number in a delete inventory
    summary.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
            (
                "count",
                "Count",
                autoboto.TypeInfo(int),
            ),
            (
                "remaining_count",
                "RemainingCount",
                autoboto.TypeInfo(int),
            ),
        ]

    # The inventory type version.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A count of the number of deleted items.
    count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The remaining number of items to delete.
    remaining_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InventoryFilter(autoboto.ShapeBase):
    """
    One or more filters. Use a filter to return a more specific list of results.
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
            (
                "type",
                "Type",
                autoboto.TypeInfo(InventoryQueryOperatorType),
            ),
        ]

    # The name of the filter key.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Inventory filter values. Example: inventory filter where instance IDs are
    # specified as values Key=AWS:InstanceInformation.InstanceId,Values=
    # i-a12b3c4d5e6g, i-1a2b3c4d5e6,Type=Equal
    values: typing.List[str] = dataclasses.field(default_factory=list, )

    # The type of filter. Valid values include the following:
    # "Equal"|"NotEqual"|"BeginWith"|"LessThan"|"GreaterThan"
    type: "InventoryQueryOperatorType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InventoryGroup(autoboto.ShapeBase):
    """
    A user-defined set of one or more filters on which to aggregate inventory data.
    Groups return a count of resources that match and don't match the specified
    criteria.
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
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[InventoryFilter]),
            ),
        ]

    # The name of the group.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filters define the criteria for the group. The `matchingCount` field
    # displays the number of resources that match the criteria. The
    # `notMatchingCount` field displays the number of resources that don't match
    # the criteria.
    filters: typing.List["InventoryFilter"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class InventoryItem(autoboto.ShapeBase):
    """
    Information collected from managed instances based on your inventory policy
    document
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "schema_version",
                "SchemaVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "capture_time",
                "CaptureTime",
                autoboto.TypeInfo(str),
            ),
            (
                "content_hash",
                "ContentHash",
                autoboto.TypeInfo(str),
            ),
            (
                "content",
                "Content",
                autoboto.TypeInfo(typing.List[typing.Dict[str, str]]),
            ),
            (
                "context",
                "Context",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the inventory type. Default inventory item type names start
    # with AWS. Custom inventory type names will start with Custom. Default
    # inventory item types include the following: AWS:AWSComponent,
    # AWS:Application, AWS:InstanceInformation, AWS:Network, and
    # AWS:WindowsUpdate.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The schema version for the inventory item.
    schema_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the inventory information was collected.
    capture_time: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # MD5 hash of the inventory item type contents. The content hash is used to
    # determine whether to update inventory information. The PutInventory API
    # does not update the inventory item type contents if the MD5 hash has not
    # changed since last update.
    content_hash: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The inventory data of the inventory type.
    content: typing.List[typing.Dict[str, str]] = dataclasses.field(
        default_factory=list,
    )

    # A map of associated properties for a specified inventory type. For example,
    # with this attribute, you can specify the `ExecutionId`, `ExecutionType`,
    # `ComplianceType` properties of the `AWS:ComplianceItem` type.
    context: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InventoryItemAttribute(autoboto.ShapeBase):
    """
    Attributes are the entries within the inventory item content. It contains name
    and value.
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
                "data_type",
                "DataType",
                autoboto.TypeInfo(InventoryAttributeDataType),
            ),
        ]

    # Name of the inventory item attribute.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The data type of the inventory item attribute.
    data_type: "InventoryAttributeDataType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InventoryItemSchema(autoboto.ShapeBase):
    """
    The inventory item schema definition. Users can use this to compose inventory
    query filters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.List[InventoryItemAttribute]),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the inventory type. Default inventory item type names start
    # with AWS. Custom inventory type names will start with Custom. Default
    # inventory item types include the following: AWS:AWSComponent,
    # AWS:Application, AWS:InstanceInformation, AWS:Network, and
    # AWS:WindowsUpdate.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The schema attributes for inventory. This contains data type and attribute
    # name.
    attributes: typing.List["InventoryItemAttribute"] = dataclasses.field(
        default_factory=list,
    )

    # The schema version for the inventory item.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The alias name of the inventory type. The alias name is used for display
    # purposes.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class InventoryQueryOperatorType(Enum):
    Equal = "Equal"
    NotEqual = "NotEqual"
    BeginWith = "BeginWith"
    LessThan = "LessThan"
    GreaterThan = "GreaterThan"
    Exists = "Exists"


@dataclasses.dataclass
class InventoryResultEntity(autoboto.ShapeBase):
    """
    Inventory query results.
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
                "data",
                "Data",
                autoboto.TypeInfo(typing.Dict[str, InventoryResultItem]),
            ),
        ]

    # ID of the inventory result entity. For example, for managed instance
    # inventory the result will be the managed instance ID. For EC2 instance
    # inventory, the result will be the instance ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The data section in the inventory result entity JSON.
    data: typing.Dict[str, "InventoryResultItem"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InventoryResultItem(autoboto.ShapeBase):
    """
    The inventory result item.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "schema_version",
                "SchemaVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "content",
                "Content",
                autoboto.TypeInfo(typing.List[typing.Dict[str, str]]),
            ),
            (
                "capture_time",
                "CaptureTime",
                autoboto.TypeInfo(str),
            ),
            (
                "content_hash",
                "ContentHash",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the inventory result item type.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The schema version for the inventory result item/
    schema_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains all the inventory data of the item type. Results include attribute
    # names and values.
    content: typing.List[typing.Dict[str, str]] = dataclasses.field(
        default_factory=list,
    )

    # The time inventory item data was captured.
    capture_time: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # MD5 hash of the inventory item type contents. The content hash is used to
    # determine whether to update inventory information. The PutInventory API
    # does not update the inventory item type contents if the MD5 hash has not
    # changed since last update.
    content_hash: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class InventorySchemaDeleteOption(Enum):
    DisableSchema = "DisableSchema"
    DeleteSchema = "DeleteSchema"


@dataclasses.dataclass
class InvocationDoesNotExist(autoboto.ShapeBase):
    """
    The command ID and instance ID you specified did not match any invocations.
    Verify the command ID adn the instance ID and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ItemContentMismatchException(autoboto.ShapeBase):
    """
    The inventory item has invalid content.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    type_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ItemSizeLimitExceededException(autoboto.ShapeBase):
    """
    The inventory item size has exceeded the size limit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    type_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LabelParameterVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "parameter_version",
                "ParameterVersion",
                autoboto.TypeInfo(int),
            ),
        ]

    # The parameter name on which you want to attach one or more labels.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more labels to attach to the specified parameter version.
    labels: typing.List[str] = dataclasses.field(default_factory=list, )

    # The specific version of the parameter on which you want to attach one or
    # more labels. If no version is specified, the system attaches the label to
    # the latest version.)
    parameter_version: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LabelParameterVersionResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "invalid_labels",
                "InvalidLabels",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The label does not meet the requirements. For information about parameter
    # label requirements, see [Labeling
    # Parameters](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/sysman-paramstore-labels.html) in the _AWS Systems
    # Manager User Guide_.
    invalid_labels: typing.List[str] = dataclasses.field(default_factory=list, )


class LastResourceDataSyncStatus(Enum):
    Successful = "Successful"
    Failed = "Failed"
    InProgress = "InProgress"


@dataclasses.dataclass
class ListAssociationVersionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The association ID for which you want to view all versions.
    association_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssociationVersionsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "association_versions",
                "AssociationVersions",
                autoboto.TypeInfo(typing.List[AssociationVersionInfo]),
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

    # Information about all versions of the association for the specified
    # association ID.
    association_versions: typing.List["AssociationVersionInfo"
                                     ] = dataclasses.field(
                                         default_factory=list,
                                     )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssociationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_filter_list",
                "AssociationFilterList",
                autoboto.TypeInfo(typing.List[AssociationFilter]),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # One or more filters. Use a filter to return a more specific list of
    # results.
    association_filter_list: typing.List["AssociationFilter"
                                        ] = dataclasses.field(
                                            default_factory=list,
                                        )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssociationsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "associations",
                "Associations",
                autoboto.TypeInfo(typing.List[Association]),
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

    # The associations.
    associations: typing.List["Association"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCommandInvocationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "command_id",
                "CommandId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[CommandFilter]),
            ),
            (
                "details",
                "Details",
                autoboto.TypeInfo(bool),
            ),
        ]

    # (Optional) The invocations for a specific command ID.
    command_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Optional) The command execution details for a specific instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Optional) The maximum number of items to return for this call. The call
    # also returns a token that you can specify in a subsequent call to get the
    # next set of results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Optional) The token for the next set of items to return. (You received
    # this token from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Optional) One or more filters. Use a filter to return a more specific list
    # of results.
    filters: typing.List["CommandFilter"] = dataclasses.field(
        default_factory=list,
    )

    # (Optional) If set this returns the response of the command executions and
    # any command output. By default this is set to False.
    details: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCommandInvocationsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "command_invocations",
                "CommandInvocations",
                autoboto.TypeInfo(typing.List[CommandInvocation]),
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

    # (Optional) A list of all invocations.
    command_invocations: typing.List["CommandInvocation"] = dataclasses.field(
        default_factory=list,
    )

    # (Optional) The token for the next set of items to return. (You received
    # this token from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCommandsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "command_id",
                "CommandId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[CommandFilter]),
            ),
        ]

    # (Optional) If provided, lists only the specified command.
    command_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Optional) Lists commands issued against this instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Optional) The maximum number of items to return for this call. The call
    # also returns a token that you can specify in a subsequent call to get the
    # next set of results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Optional) The token for the next set of items to return. (You received
    # this token from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Optional) One or more filters. Use a filter to return a more specific list
    # of results.
    filters: typing.List["CommandFilter"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListCommandsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "commands",
                "Commands",
                autoboto.TypeInfo(typing.List[Command]),
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

    # (Optional) The list of commands requested by the user.
    commands: typing.List["Command"] = dataclasses.field(default_factory=list, )

    # (Optional) The token for the next set of items to return. (You received
    # this token from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListComplianceItemsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[ComplianceStringFilter]),
            ),
            (
                "resource_ids",
                "ResourceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "resource_types",
                "ResourceTypes",
                autoboto.TypeInfo(typing.List[str]),
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

    # One or more compliance filters. Use a filter to return a more specific list
    # of results.
    filters: typing.List["ComplianceStringFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The ID for the resources from which to get compliance information.
    # Currently, you can only specify one resource ID.
    resource_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The type of resource from which to get compliance information. Currently,
    # the only supported resource type is `ManagedInstance`.
    resource_types: typing.List[str] = dataclasses.field(default_factory=list, )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListComplianceItemsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "compliance_items",
                "ComplianceItems",
                autoboto.TypeInfo(typing.List[ComplianceItem]),
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

    # A list of compliance information for the specified resource ID.
    compliance_items: typing.List["ComplianceItem"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListComplianceSummariesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[ComplianceStringFilter]),
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

    # One or more compliance or inventory filters. Use a filter to return a more
    # specific list of results.
    filters: typing.List["ComplianceStringFilter"] = dataclasses.field(
        default_factory=list,
    )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. Currently, you can
    # specify null or 50. The call also returns a token that you can specify in a
    # subsequent call to get the next set of results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListComplianceSummariesResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "compliance_summary_items",
                "ComplianceSummaryItems",
                autoboto.TypeInfo(typing.List[ComplianceSummaryItem]),
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

    # A list of compliant and non-compliant summary counts based on compliance
    # types. For example, this call returns State Manager associations, patches,
    # or custom compliance types according to the filter criteria that you
    # specified.
    compliance_summary_items: typing.List["ComplianceSummaryItem"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDocumentVersionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the document about which you want version information.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDocumentVersionsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "document_versions",
                "DocumentVersions",
                autoboto.TypeInfo(typing.List[DocumentVersionInfo]),
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

    # The document versions.
    document_versions: typing.List["DocumentVersionInfo"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDocumentsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_filter_list",
                "DocumentFilterList",
                autoboto.TypeInfo(typing.List[DocumentFilter]),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[DocumentKeyValuesFilter]),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # One or more filters. Use a filter to return a more specific list of
    # results.
    document_filter_list: typing.List["DocumentFilter"] = dataclasses.field(
        default_factory=list,
    )

    # One or more filters. Use a filter to return a more specific list of
    # results.
    filters: typing.List["DocumentKeyValuesFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDocumentsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "document_identifiers",
                "DocumentIdentifiers",
                autoboto.TypeInfo(typing.List[DocumentIdentifier]),
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

    # The names of the Systems Manager documents.
    document_identifiers: typing.List["DocumentIdentifier"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInventoryEntriesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "type_name",
                "TypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[InventoryFilter]),
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

    # The instance ID for which you want inventory information.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of inventory item for which you want information.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more filters. Use a filter to return a more specific list of
    # results.
    filters: typing.List["InventoryFilter"] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInventoryEntriesResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "type_name",
                "TypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "schema_version",
                "SchemaVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "capture_time",
                "CaptureTime",
                autoboto.TypeInfo(str),
            ),
            (
                "entries",
                "Entries",
                autoboto.TypeInfo(typing.List[typing.Dict[str, str]]),
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

    # The type of inventory item returned by the request.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance ID targeted by the request to query inventory information.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The inventory schema version used by the instance(s).
    schema_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time that inventory information was collected for the instance(s).
    capture_time: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of inventory items on the instance(s).
    entries: typing.List[typing.Dict[str, str]] = dataclasses.field(
        default_factory=list,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourceComplianceSummariesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[ComplianceStringFilter]),
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

    # One or more filters. Use a filter to return a more specific list of
    # results.
    filters: typing.List["ComplianceStringFilter"] = dataclasses.field(
        default_factory=list,
    )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourceComplianceSummariesResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_compliance_summary_items",
                "ResourceComplianceSummaryItems",
                autoboto.TypeInfo(typing.List[ResourceComplianceSummaryItem]),
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

    # A summary count for specified or targeted managed instances. Summary count
    # includes information about compliant and non-compliant State Manager
    # associations, patch status, or custom items according to the filter
    # criteria that you specify.
    resource_compliance_summary_items: typing.List[
        "ResourceComplianceSummaryItem"
    ] = dataclasses.field(
        default_factory=list,
    )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourceDataSyncRequest(autoboto.ShapeBase):
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

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourceDataSyncResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_data_sync_items",
                "ResourceDataSyncItems",
                autoboto.TypeInfo(typing.List[ResourceDataSyncItem]),
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

    # A list of your current Resource Data Sync configurations and their
    # statuses.
    resource_data_sync_items: typing.List["ResourceDataSyncItem"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(ResourceTypeForTagging),
            ),
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Returns a list of tags for a specific resource type.
    resource_type: "ResourceTypeForTagging" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The resource ID for which you want to see a list of tags.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tag_list",
                "TagList",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of tags.
    tag_list: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class LoggingInfo(autoboto.ShapeBase):
    """
    Information about an Amazon S3 bucket to write instance-level logs to.

    `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    `TaskInvocationParameters` structure. For information about how Systems Manager
    handles these options for the supported Maintenance Window task types, see
    MaintenanceWindowTaskInvocationParameters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_bucket_name",
                "S3BucketName",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_region",
                "S3Region",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_key_prefix",
                "S3KeyPrefix",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of an Amazon S3 bucket where execution logs are stored .
    s3_bucket_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The region where the Amazon S3 bucket is located.
    s3_region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Optional) The Amazon S3 bucket subfolder.
    s3_key_prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaintenanceWindowAutomationParameters(autoboto.ShapeBase):
    """
    The parameters for an AUTOMATION task type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
        ]

    # The version of an Automation document to use during task execution.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameters for the AUTOMATION task.

    # For information about specifying and updating task parameters, see
    # RegisterTaskWithMaintenanceWindow and UpdateMaintenanceWindowTask.

    # `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    # instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.

    # `TaskParameters` has been deprecated. To specify parameters to pass to a
    # task when it runs, instead use the `Parameters` option in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.

    # For AUTOMATION task types, Systems Manager ignores any values specified for
    # these parameters.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MaintenanceWindowExecution(autoboto.ShapeBase):
    """
    Describes the information about an execution of a Maintenance Window.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "window_execution_id",
                "WindowExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(MaintenanceWindowExecutionStatus),
            ),
            (
                "status_details",
                "StatusDetails",
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
        ]

    # The ID of the Maintenance Window.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the Maintenance Window execution.
    window_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the execution.
    status: "MaintenanceWindowExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details explaining the Status. Only available for certain status
    # values.
    status_details: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the execution started.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the execution finished.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class MaintenanceWindowExecutionStatus(Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    TIMED_OUT = "TIMED_OUT"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    SKIPPED_OVERLAPPING = "SKIPPED_OVERLAPPING"


@dataclasses.dataclass
class MaintenanceWindowExecutionTaskIdentity(autoboto.ShapeBase):
    """
    Information about a task execution performed as part of a Maintenance Window
    execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_execution_id",
                "WindowExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_execution_id",
                "TaskExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(MaintenanceWindowExecutionStatus),
            ),
            (
                "status_details",
                "StatusDetails",
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
                "task_arn",
                "TaskArn",
                autoboto.TypeInfo(str),
            ),
            (
                "task_type",
                "TaskType",
                autoboto.TypeInfo(MaintenanceWindowTaskType),
            ),
        ]

    # The ID of the Maintenance Window execution that ran the task.
    window_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the specific task execution in the Maintenance Window execution.
    task_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the task execution.
    status: "MaintenanceWindowExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details explaining the status of the task execution. Only available for
    # certain status values.
    status_details: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the task execution started.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the task execution finished.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the executed task.
    task_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of executed task.
    task_type: "MaintenanceWindowTaskType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MaintenanceWindowExecutionTaskInvocationIdentity(autoboto.ShapeBase):
    """
    Describes the information about a task invocation for a particular target as
    part of a task execution performed as part of a Maintenance Window execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_execution_id",
                "WindowExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_execution_id",
                "TaskExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "invocation_id",
                "InvocationId",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_id",
                "ExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_type",
                "TaskType",
                autoboto.TypeInfo(MaintenanceWindowTaskType),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(MaintenanceWindowExecutionStatus),
            ),
            (
                "status_details",
                "StatusDetails",
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
                "owner_information",
                "OwnerInformation",
                autoboto.TypeInfo(str),
            ),
            (
                "window_target_id",
                "WindowTargetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window execution that ran the task.
    window_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the specific task execution in the Maintenance Window execution.
    task_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the task invocation.
    invocation_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the action performed in the service that actually handled the
    # task invocation. If the task type is RUN_COMMAND, this value is the command
    # ID.
    execution_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The task type.
    task_type: "MaintenanceWindowTaskType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameters that were provided for the invocation when it was executed.
    parameters: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the task invocation.
    status: "MaintenanceWindowExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The details explaining the status of the task invocation. Only available
    # for certain Status values.
    status_details: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the invocation started.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the invocation finished.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # User-provided value that was specified when the target was registered with
    # the Maintenance Window. This was also included in any CloudWatch events
    # raised during the task invocation.
    owner_information: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the target definition in this Maintenance Window the invocation
    # was performed for.
    window_target_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MaintenanceWindowFilter(autoboto.ShapeBase):
    """
    Filter used in the request.
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

    # The name of the filter.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The filter values.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class MaintenanceWindowIdentity(autoboto.ShapeBase):
    """
    Information about the Maintenance Window.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(int),
            ),
            (
                "cutoff",
                "Cutoff",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the Maintenance Window.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the Maintenance Window.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A description of the Maintenance Window.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether the Maintenance Window is enabled.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The duration of the Maintenance Window in hours.
    duration: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of hours before the end of the Maintenance Window that Systems
    # Manager stops scheduling new tasks for execution.
    cutoff: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaintenanceWindowLambdaParameters(autoboto.ShapeBase):
    """
    The parameters for a LAMBDA task type.

    For information about specifying and updating task parameters, see
    RegisterTaskWithMaintenanceWindow and UpdateMaintenanceWindowTask.

    `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    `TaskInvocationParameters` structure. For information about how Systems Manager
    handles these options for the supported Maintenance Window task types, see
    MaintenanceWindowTaskInvocationParameters.

    `TaskParameters` has been deprecated. To specify parameters to pass to a task
    when it runs, instead use the `Parameters` option in the
    `TaskInvocationParameters` structure. For information about how Systems Manager
    handles these options for the supported Maintenance Window task types, see
    MaintenanceWindowTaskInvocationParameters.

    For Lambda tasks, Systems Manager ignores any values specified for
    TaskParameters and LoggingInfo.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_context",
                "ClientContext",
                autoboto.TypeInfo(str),
            ),
            (
                "qualifier",
                "Qualifier",
                autoboto.TypeInfo(str),
            ),
            (
                "payload",
                "Payload",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # Pass client-specific information to the Lambda function that you are
    # invoking. You can then process the client information in your Lambda
    # function as you choose through the context variable.
    client_context: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # (Optional) Specify a Lambda function version or alias name. If you specify
    # a function version, the action uses the qualified function ARN to invoke a
    # specific Lambda function. If you specify an alias name, the action uses the
    # alias ARN to invoke the Lambda function version to which the alias points.
    qualifier: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # JSON to provide to your Lambda function as input.
    payload: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class MaintenanceWindowLambdaPayload(botocore.response.StreamingBody):
    pass


class MaintenanceWindowResourceType(Enum):
    INSTANCE = "INSTANCE"


@dataclasses.dataclass
class MaintenanceWindowRunCommandParameters(autoboto.ShapeBase):
    """
    The parameters for a RUN_COMMAND task type.

    For information about specifying and updating task parameters, see
    RegisterTaskWithMaintenanceWindow and UpdateMaintenanceWindowTask.

    `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    `TaskInvocationParameters` structure. For information about how Systems Manager
    handles these options for the supported Maintenance Window task types, see
    MaintenanceWindowTaskInvocationParameters.

    `TaskParameters` has been deprecated. To specify parameters to pass to a task
    when it runs, instead use the `Parameters` option in the
    `TaskInvocationParameters` structure. For information about how Systems Manager
    handles these options for the supported Maintenance Window task types, see
    MaintenanceWindowTaskInvocationParameters.

    For Run Command tasks, Systems Manager uses specified values for
    `TaskParameters` and `LoggingInfo` only if no values are specified for
    `TaskInvocationParameters`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment",
                "Comment",
                autoboto.TypeInfo(str),
            ),
            (
                "document_hash",
                "DocumentHash",
                autoboto.TypeInfo(str),
            ),
            (
                "document_hash_type",
                "DocumentHashType",
                autoboto.TypeInfo(DocumentHashType),
            ),
            (
                "notification_config",
                "NotificationConfig",
                autoboto.TypeInfo(NotificationConfig),
            ),
            (
                "output_s3_bucket_name",
                "OutputS3BucketName",
                autoboto.TypeInfo(str),
            ),
            (
                "output_s3_key_prefix",
                "OutputS3KeyPrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "timeout_seconds",
                "TimeoutSeconds",
                autoboto.TypeInfo(int),
            ),
        ]

    # Information about the command(s) to execute.
    comment: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The SHA-256 or SHA-1 hash created by the system when the document was
    # created. SHA-1 hashes have been deprecated.
    document_hash: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # SHA-256 or SHA-1. SHA-1 hashes have been deprecated.
    document_hash_type: "DocumentHashType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Configurations for sending notifications about command status changes on a
    # per-instance basis.
    notification_config: "NotificationConfig" = dataclasses.field(
        default_factory=dict,
    )

    # The name of the Amazon S3 bucket.
    output_s3_bucket_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon S3 bucket subfolder.
    output_s3_key_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameters for the RUN_COMMAND task execution.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The IAM service role to assume during task execution.
    service_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If this time is reached and the command has not already started executing,
    # it doesn not execute.
    timeout_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MaintenanceWindowStepFunctionsParameters(autoboto.ShapeBase):
    """
    The parameters for a STEP_FUNCTION task.

    For information about specifying and updating task parameters, see
    RegisterTaskWithMaintenanceWindow and UpdateMaintenanceWindowTask.

    `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    `TaskInvocationParameters` structure. For information about how Systems Manager
    handles these options for the supported Maintenance Window task types, see
    MaintenanceWindowTaskInvocationParameters.

    `TaskParameters` has been deprecated. To specify parameters to pass to a task
    when it runs, instead use the `Parameters` option in the
    `TaskInvocationParameters` structure. For information about how Systems Manager
    handles these options for the supported Maintenance Window task types, see
    MaintenanceWindowTaskInvocationParameters.

    For Step Functions tasks, Systems Manager ignores any values specified for
    `TaskParameters` and `LoggingInfo`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input",
                "Input",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The inputs for the STEP_FUNCTION task.
    input: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the STEP_FUNCTION task.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaintenanceWindowTarget(autoboto.ShapeBase):
    """
    The target registered with the Maintenance Window.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "window_target_id",
                "WindowTargetId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(MaintenanceWindowResourceType),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "owner_information",
                "OwnerInformation",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Maintenance Window ID where the target is registered.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the target.
    window_target_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of target.
    resource_type: "MaintenanceWindowResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The targets (either instances or tags). Instances are specified using
    # Key=instanceids,Values=<instanceid1>,<instanceid2>. Tags are specified
    # using Key=<tag name>,Values=<tag value>.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # User-provided value that will be included in any CloudWatch events raised
    # while running tasks for these targets in this Maintenance Window.
    owner_information: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The target name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A description of the target.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaintenanceWindowTask(autoboto.ShapeBase):
    """
    Information about a task defined for a Maintenance Window.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "window_task_id",
                "WindowTaskId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_arn",
                "TaskArn",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(MaintenanceWindowTaskType),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "task_parameters",
                "TaskParameters",
                autoboto.TypeInfo(
                    typing.Dict[str,
                                MaintenanceWindowTaskParameterValueExpression]
                ),
            ),
            (
                "priority",
                "Priority",
                autoboto.TypeInfo(int),
            ),
            (
                "logging_info",
                "LoggingInfo",
                autoboto.TypeInfo(LoggingInfo),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                autoboto.TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Maintenance Window ID where the task is registered.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The task ID.
    window_task_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The resource that the task uses during execution. For RUN_COMMAND and
    # AUTOMATION task types, `TaskArn` is the Systems Manager document name or
    # ARN. For LAMBDA tasks, it's the function name or ARN. For STEP_FUNCTION
    # tasks, it's the state machine ARN.
    task_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of task. The type can be one of the following: RUN_COMMAND,
    # AUTOMATION, LAMBDA, or STEP_FUNCTION.
    type: "MaintenanceWindowTaskType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The targets (either instances or tags). Instances are specified using
    # Key=instanceids,Values=<instanceid1>,<instanceid2>. Tags are specified
    # using Key=<tag name>,Values=<tag value>.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # The parameters that should be passed to the task when it is executed.

    # `TaskParameters` has been deprecated. To specify parameters to pass to a
    # task when it runs, instead use the `Parameters` option in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    task_parameters: typing.Dict[
        str, "MaintenanceWindowTaskParameterValueExpression"
    ] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The priority of the task in the Maintenance Window. The lower the number,
    # the higher the priority. Tasks that have the same priority are scheduled in
    # parallel.
    priority: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Information about an Amazon S3 bucket to write task-level logs to.

    # `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    # instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    logging_info: "LoggingInfo" = dataclasses.field(default_factory=dict, )

    # The role that should be assumed when executing the task
    service_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of targets this task can be run for in parallel.
    max_concurrency: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of errors allowed before this task stops being
    # scheduled.
    max_errors: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The task name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A description of the task.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaintenanceWindowTaskInvocationParameters(autoboto.ShapeBase):
    """
    The parameters for task execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "run_command",
                "RunCommand",
                autoboto.TypeInfo(MaintenanceWindowRunCommandParameters),
            ),
            (
                "automation",
                "Automation",
                autoboto.TypeInfo(MaintenanceWindowAutomationParameters),
            ),
            (
                "step_functions",
                "StepFunctions",
                autoboto.TypeInfo(MaintenanceWindowStepFunctionsParameters),
            ),
            (
                "lambda_",
                "Lambda",
                autoboto.TypeInfo(MaintenanceWindowLambdaParameters),
            ),
        ]

    # The parameters for a RUN_COMMAND task type.
    run_command: "MaintenanceWindowRunCommandParameters" = dataclasses.field(
        default_factory=dict,
    )

    # The parameters for an AUTOMATION task type.
    automation: "MaintenanceWindowAutomationParameters" = dataclasses.field(
        default_factory=dict,
    )

    # The parameters for a STEP_FUNCTION task type.
    step_functions: "MaintenanceWindowStepFunctionsParameters" = dataclasses.field(
        default_factory=dict,
    )

    # The parameters for a LAMBDA task type.
    lambda_: "MaintenanceWindowLambdaParameters" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class MaintenanceWindowTaskParameterValueExpression(autoboto.ShapeBase):
    """
    Defines the values for a task parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "values",
                "Values",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # This field contains an array of 0 or more strings, each 1 to 255 characters
    # in length.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


class MaintenanceWindowTaskType(Enum):
    RUN_COMMAND = "RUN_COMMAND"
    AUTOMATION = "AUTOMATION"
    STEP_FUNCTIONS = "STEP_FUNCTIONS"
    LAMBDA = "LAMBDA"


@dataclasses.dataclass
class MaxDocumentSizeExceeded(autoboto.ShapeBase):
    """
    The size limit of a document is 64 KB.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyDocumentPermissionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "permission_type",
                "PermissionType",
                autoboto.TypeInfo(DocumentPermissionType),
            ),
            (
                "account_ids_to_add",
                "AccountIdsToAdd",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "account_ids_to_remove",
                "AccountIdsToRemove",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the document that you want to share.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The permission type for the document. The permission type can be _Share_.
    permission_type: "DocumentPermissionType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS user accounts that should have access to the document. The account
    # IDs can either be a group of account IDs or _All_.
    account_ids_to_add: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The AWS user accounts that should no longer have access to the document.
    # The AWS user account can either be a group of account IDs or _All_. This
    # action has a higher priority than _AccountIdsToAdd_. If you specify an
    # account ID to add and the same ID to remove, the system removes access to
    # the document.
    account_ids_to_remove: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ModifyDocumentPermissionResponse(autoboto.OutputShapeBase):
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
class NonCompliantSummary(autoboto.ShapeBase):
    """
    A summary of resources that are not compliant. The summary is organized
    according to resource type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "non_compliant_count",
                "NonCompliantCount",
                autoboto.TypeInfo(int),
            ),
            (
                "severity_summary",
                "SeveritySummary",
                autoboto.TypeInfo(SeveritySummary),
            ),
        ]

    # The total number of compliance items that are not compliant.
    non_compliant_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A summary of the non-compliance severity by compliance type
    severity_summary: "SeveritySummary" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class NotificationConfig(autoboto.ShapeBase):
    """
    Configurations for sending notifications.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notification_arn",
                "NotificationArn",
                autoboto.TypeInfo(str),
            ),
            (
                "notification_events",
                "NotificationEvents",
                autoboto.TypeInfo(typing.List[NotificationEvent]),
            ),
            (
                "notification_type",
                "NotificationType",
                autoboto.TypeInfo(NotificationType),
            ),
        ]

    # An Amazon Resource Name (ARN) for a Simple Notification Service (SNS)
    # topic. Run Command pushes notifications about command status changes to
    # this topic.
    notification_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The different events for which you can receive notifications. These events
    # include the following: All (events), InProgress, Success, TimedOut,
    # Cancelled, Failed. To learn more about these events, see [Configuring
    # Amazon SNS Notifications for Run
    # Command](http://docs.aws.amazon.com/systems-manager/latest/userguide/rc-
    # sns-notifications.html) in the _AWS Systems Manager User Guide_.
    notification_events: typing.List["NotificationEvent"] = dataclasses.field(
        default_factory=list,
    )

    # Command: Receive notification when the status of a command changes.
    # Invocation: For commands sent to multiple instances, receive notification
    # on a per-instance basis when the status of a command changes.
    notification_type: "NotificationType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class NotificationEvent(Enum):
    All = "All"
    InProgress = "InProgress"
    Success = "Success"
    TimedOut = "TimedOut"
    Cancelled = "Cancelled"
    Failed = "Failed"


class NotificationType(Enum):
    Command = "Command"
    Invocation = "Invocation"


class OperatingSystem(Enum):
    WINDOWS = "WINDOWS"
    AMAZON_LINUX = "AMAZON_LINUX"
    AMAZON_LINUX_2 = "AMAZON_LINUX_2"
    UBUNTU = "UBUNTU"
    REDHAT_ENTERPRISE_LINUX = "REDHAT_ENTERPRISE_LINUX"
    SUSE = "SUSE"
    CENTOS = "CENTOS"


@dataclasses.dataclass
class OutputSource(autoboto.ShapeBase):
    """
    Information about the source where the association execution details are stored.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_source_id",
                "OutputSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "output_source_type",
                "OutputSourceType",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the output source, for example the URL of an Amazon S3 bucket.
    output_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of source where the association execution details are stored, for
    # example, Amazon S3.
    output_source_type: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Parameter(autoboto.ShapeBase):
    """
    An Amazon EC2 Systems Manager parameter in Parameter Store.
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
                "type",
                "Type",
                autoboto.TypeInfo(ParameterType),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
            (
                "selector",
                "Selector",
                autoboto.TypeInfo(str),
            ),
            (
                "source_result",
                "SourceResult",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "arn",
                "ARN",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the parameter.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of parameter. Valid values include the following: String, String
    # list, Secure string.
    type: "ParameterType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameter value.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The parameter version.
    version: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Either the version number or the label used to retrieve the parameter
    # value. Specify selectors by using one of the following formats:

    # parameter_name:version

    # parameter_name:label
    selector: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Applies to parameters that reference information in other AWS services.
    # SourceResult is the raw result or response from the source.
    source_result: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Date the parameter was last changed or updated and the parameter version
    # was created.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the parameter.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ParameterAlreadyExists(autoboto.ShapeBase):
    """
    The parameter already exists. You can't create duplicate parameters.
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
class ParameterHistory(autoboto.ShapeBase):
    """
    Information about parameter usage.
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
                "type",
                "Type",
                autoboto.TypeInfo(ParameterType),
            ),
            (
                "key_id",
                "KeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_user",
                "LastModifiedUser",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
            (
                "allowed_pattern",
                "AllowedPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
            (
                "labels",
                "Labels",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the parameter.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of parameter used.
    type: "ParameterType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the query key used for this parameter.
    key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Date the parameter was last changed or updated.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Amazon Resource Name (ARN) of the AWS user who last changed the parameter.
    last_modified_user: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the parameter.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The parameter value.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Parameter names can include the following letters and symbols.

    # a-zA-Z0-9_.-
    allowed_pattern: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameter version.
    version: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Labels assigned to the parameter version.
    labels: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class ParameterLimitExceeded(autoboto.ShapeBase):
    """
    You have exceeded the number of parameters for this AWS account. Delete one or
    more parameters and try again.
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
class ParameterMaxVersionLimitExceeded(autoboto.ShapeBase):
    """
    The parameter exceeded the maximum number of allowed versions.
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
class ParameterMetadata(autoboto.ShapeBase):
    """
    Metada includes information like the ARN of the last user and the date/time the
    parameter was last used.
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
                "type",
                "Type",
                autoboto.TypeInfo(ParameterType),
            ),
            (
                "key_id",
                "KeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_user",
                "LastModifiedUser",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "allowed_pattern",
                "AllowedPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
        ]

    # The parameter name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of parameter. Valid parameter types include the following: String,
    # String list, Secure string.
    type: "ParameterType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the query key used for this parameter.
    key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Date the parameter was last changed or updated.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Amazon Resource Name (ARN) of the AWS user who last changed the parameter.
    last_modified_user: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Description of the parameter actions.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A parameter name can include only the following letters and symbols.

    # a-zA-Z0-9_.-
    allowed_pattern: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameter version.
    version: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ParameterNotFound(autoboto.ShapeBase):
    """
    The parameter could not be found. Verify the name and try again.
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
class ParameterPatternMismatchException(autoboto.ShapeBase):
    """
    The parameter name is not valid.
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

    # The parameter name is not valid.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ParameterStringFilter(autoboto.ShapeBase):
    """
    One or more filters. Use a filter to return a more specific list of results.

    The `Name` field can't be used with the GetParametersByPath API action.
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
                "option",
                "Option",
                autoboto.TypeInfo(str),
            ),
            (
                "values",
                "Values",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the filter.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Valid options are Equals and BeginsWith. For Path filter, valid options are
    # Recursive and OneLevel.
    option: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value you want to search for.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


class ParameterType(Enum):
    String = "String"
    StringList = "StringList"
    SecureString = "SecureString"


@dataclasses.dataclass
class ParameterVersionLabelLimitExceeded(autoboto.ShapeBase):
    """
    A parameter version can have a maximum of ten labels.
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
class ParameterVersionNotFound(autoboto.ShapeBase):
    """
    The specified parameter version was not found. Verify the parameter name and
    version, and try again.
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
class ParametersFilter(autoboto.ShapeBase):
    """
    This data type is deprecated. Instead, use ParameterStringFilter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(ParametersFilterKey),
            ),
            (
                "values",
                "Values",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the filter.
    key: "ParametersFilterKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The filter values.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


class ParametersFilterKey(Enum):
    Name = "Name"
    Type = "Type"
    KeyId = "KeyId"


@dataclasses.dataclass
class Patch(autoboto.ShapeBase):
    """
    Represents metadata about a patch.
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
                "release_date",
                "ReleaseDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "title",
                "Title",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "content_url",
                "ContentUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "vendor",
                "Vendor",
                autoboto.TypeInfo(str),
            ),
            (
                "product_family",
                "ProductFamily",
                autoboto.TypeInfo(str),
            ),
            (
                "product",
                "Product",
                autoboto.TypeInfo(str),
            ),
            (
                "classification",
                "Classification",
                autoboto.TypeInfo(str),
            ),
            (
                "msrc_severity",
                "MsrcSeverity",
                autoboto.TypeInfo(str),
            ),
            (
                "kb_number",
                "KbNumber",
                autoboto.TypeInfo(str),
            ),
            (
                "msrc_number",
                "MsrcNumber",
                autoboto.TypeInfo(str),
            ),
            (
                "language",
                "Language",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the patch (this is different than the Microsoft Knowledge Base
    # ID).
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date the patch was released.
    release_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The title of the patch.
    title: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the patch.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The URL where more information can be obtained about the patch.
    content_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the vendor providing the patch.
    vendor: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The product family the patch is applicable for (for example, Windows).
    product_family: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The specific product the patch is applicable for (for example,
    # WindowsServer2016).
    product: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The classification of the patch (for example, SecurityUpdates, Updates,
    # CriticalUpdates).
    classification: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The severity of the patch (for example Critical, Important, Moderate).
    msrc_severity: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Microsoft Knowledge Base ID of the patch.
    kb_number: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the MSRC bulletin the patch is related to.
    msrc_number: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language of the patch if it's language-specific.
    language: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PatchBaselineIdentity(autoboto.ShapeBase):
    """
    Defines the basic information about a patch baseline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
            (
                "baseline_name",
                "BaselineName",
                autoboto.TypeInfo(str),
            ),
            (
                "operating_system",
                "OperatingSystem",
                autoboto.TypeInfo(OperatingSystem),
            ),
            (
                "baseline_description",
                "BaselineDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "default_baseline",
                "DefaultBaseline",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the patch baseline.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the patch baseline.
    baseline_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Defines the operating system the patch baseline applies to. The Default
    # value is WINDOWS.
    operating_system: "OperatingSystem" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description of the patch baseline.
    baseline_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether this is the default baseline. Note that Systems Manager supports
    # creating multiple default patch baselines. For example, you can create a
    # default patch baseline for each operating system.
    default_baseline: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PatchComplianceData(autoboto.ShapeBase):
    """
    Information about the state of a patch on a particular instance as it relates to
    the patch baseline used to patch the instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "title",
                "Title",
                autoboto.TypeInfo(str),
            ),
            (
                "kb_id",
                "KBId",
                autoboto.TypeInfo(str),
            ),
            (
                "classification",
                "Classification",
                autoboto.TypeInfo(str),
            ),
            (
                "severity",
                "Severity",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(PatchComplianceDataState),
            ),
            (
                "installed_time",
                "InstalledTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The title of the patch.
    title: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The operating system-specific ID of the patch.
    kb_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The classification of the patch (for example, SecurityUpdates, Updates,
    # CriticalUpdates).
    classification: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The severity of the patch (for example, Critical, Important, Moderate).
    severity: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The state of the patch on the instance (INSTALLED, INSTALLED_OTHER,
    # MISSING, NOT_APPLICABLE or FAILED).
    state: "PatchComplianceDataState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date/time the patch was installed on the instance. Note that not all
    # operating systems provide this level of information.
    installed_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class PatchComplianceDataState(Enum):
    INSTALLED = "INSTALLED"
    INSTALLED_OTHER = "INSTALLED_OTHER"
    MISSING = "MISSING"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    FAILED = "FAILED"


class PatchComplianceLevel(Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFORMATIONAL = "INFORMATIONAL"
    UNSPECIFIED = "UNSPECIFIED"


class PatchDeploymentStatus(Enum):
    APPROVED = "APPROVED"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    EXPLICIT_APPROVED = "EXPLICIT_APPROVED"
    EXPLICIT_REJECTED = "EXPLICIT_REJECTED"


@dataclasses.dataclass
class PatchFilter(autoboto.ShapeBase):
    """
    Defines a patch filter.

    A patch filter consists of key/value pairs, but not all keys are valid for all
    operating system types. For example, the key `PRODUCT` is valid for all
    supported operating system types. The key `MSRC_SEVERITY`, however, is valid
    only for Windows operating systems, and the key `SECTION` is valid only for
    Ubuntu operating systems.

    Refer to the following sections for information about which keys may be used
    with each major operating system, and which values are valid for each key.

    **Windows Operating Systems**

    The supported keys for Windows operating systems are `PRODUCT`,
    `CLASSIFICATION`, and `MSRC_SEVERITY`. See the following lists for valid values
    for each of these keys.

    _Supported key:_ `PRODUCT`

    _Supported values:_

      * `Windows7`

      * `Windows8`

      * `Windows8.1`

      * `Windows8Embedded`

      * `Windows10`

      * `Windows10LTSB`

      * `WindowsServer2008`

      * `WindowsServer2008R2`

      * `WindowsServer2012`

      * `WindowsServer2012R2`

      * `WindowsServer2016`

      * `*`

    _Use a wildcard character (*) to target all supported operating system
    versions._

    _Supported key:_ `CLASSIFICATION`

    _Supported values:_

      * `CriticalUpdates`

      * `DefinitionUpdates`

      * `Drivers`

      * `FeaturePacks`

      * `SecurityUpdates`

      * `ServicePacks`

      * `Tools`

      * `UpdateRollups`

      * `Updates`

      * `Upgrades`

    _Supported key:_ `MSRC_SEVERITY`

    _Supported values:_

      * `Critical`

      * `Important`

      * `Moderate`

      * `Low`

      * `Unspecified`

    **Ubuntu Operating Systems**

    The supported keys for Ubuntu operating systems are `PRODUCT`, `PRIORITY`, and
    `SECTION`. See the following lists for valid values for each of these keys.

    _Supported key:_ `PRODUCT`

    _Supported values:_

      * `Ubuntu14.04`

      * `Ubuntu16.04`

      * `*`

    _Use a wildcard character (*) to target all supported operating system
    versions._

    _Supported key:_ `PRIORITY`

    _Supported values:_

      * `Required`

      * `Important`

      * `Standard`

      * `Optional`

      * `Extra`

    _Supported key:_ `SECTION`

    Only the length of the key value is validated. Minimum length is 1. Maximum
    length is 64.

    **Amazon Linux Operating Systems**

    The supported keys for Amazon Linux operating systems are `PRODUCT`,
    `CLASSIFICATION`, and `SEVERITY`. See the following lists for valid values for
    each of these keys.

    _Supported key:_ `PRODUCT`

    _Supported values:_

      * `AmazonLinux2012.03`

      * `AmazonLinux2012.09`

      * `AmazonLinux2013.03`

      * `AmazonLinux2013.09`

      * `AmazonLinux2014.03`

      * `AmazonLinux2014.09`

      * `AmazonLinux2015.03`

      * `AmazonLinux2015.09`

      * `AmazonLinux2016.03`

      * `AmazonLinux2016.09`

      * `AmazonLinux2017.03`

      * `AmazonLinux2017.09`

      * `*`

    _Use a wildcard character (*) to target all supported operating system
    versions._

    _Supported key:_ `CLASSIFICATION`

    _Supported values:_

      * `Security`

      * `Bugfix`

      * `Enhancement`

      * `Recommended`

      * `Newpackage`

    _Supported key:_ `SEVERITY`

    _Supported values:_

      * `Critical`

      * `Important`

      * `Medium`

      * `Low`

    **Amazon Linux 2 Operating Systems**

    The supported keys for Amazon Linux 2 operating systems are `PRODUCT`,
    `CLASSIFICATION`, and `SEVERITY`. See the following lists for valid values for
    each of these keys.

    _Supported key:_ `PRODUCT`

    _Supported values:_

      * `AmazonLinux2`

      * `AmazonLinux2.0`

      * `*`

    _Use a wildcard character (*) to target all supported operating system
    versions._

    _Supported key:_ `CLASSIFICATION`

    _Supported values:_

      * `Security`

      * `Bugfix`

      * `Enhancement`

      * `Recommended`

      * `Newpackage`

    _Supported key:_ `SEVERITY`

    _Supported values:_

      * `Critical`

      * `Important`

      * `Medium`

      * `Low`

    **RedHat Enterprise Linux (RHEL) Operating Systems**

    The supported keys for RedHat Enterprise Linux operating systems are `PRODUCT`,
    `CLASSIFICATION`, and `SEVERITY`. See the following lists for valid values for
    each of these keys.

    _Supported key:_ `PRODUCT`

    _Supported values:_

      * `RedhatEnterpriseLinux6.5`

      * `RedhatEnterpriseLinux6.6`

      * `RedhatEnterpriseLinux6.7`

      * `RedhatEnterpriseLinux6.8`

      * `RedhatEnterpriseLinux6.9`

      * `RedhatEnterpriseLinux7.0`

      * `RedhatEnterpriseLinux7.1`

      * `RedhatEnterpriseLinux7.2`

      * `RedhatEnterpriseLinux7.3`

      * `RedhatEnterpriseLinux7.4`

      * `*`

    _Use a wildcard character (*) to target all supported operating system
    versions._

    _Supported key:_ `CLASSIFICATION`

    _Supported values:_

      * `Security`

      * `Bugfix`

      * `Enhancement`

      * `Recommended`

      * `Newpackage`

    _Supported key:_ `SEVERITY`

    _Supported values:_

      * `Critical`

      * `Important`

      * `Medium`

      * `Low`

    **SUSE Linux Enterprise Server (SLES) Operating Systems**

    The supported keys for SLES operating systems are `PRODUCT`, `CLASSIFICATION`,
    and `SEVERITY`. See the following lists for valid values for each of these keys.

    _Supported key:_ `PRODUCT`

    _Supported values:_

      * `Suse12.0`

      * `Suse12.1`

      * `Suse12.2`

      * `Suse12.3`

      * `Suse12.4`

      * `Suse12.5`

      * `Suse12.6`

      * `Suse12.7`

      * `Suse12.8`

      * `Suse12.9`

      * `*`

    _Use a wildcard character (*) to target all supported operating system
    versions._

    _Supported key:_ `CLASSIFICATION`

    _Supported values:_

      * `Security`

      * `Recommended`

      * `Optional`

      * `Feature`

      * `Document`

      * `Yast`

    _Supported key:_ `SEVERITY`

    _Supported values:_

      * `Critical`

      * `Important`

      * `Moderate`

      * `Low`

    **CentOS Operating Systems**

    The supported keys for CentOS operating systems are `PRODUCT`, `CLASSIFICATION`,
    and `SEVERITY`. See the following lists for valid values for each of these keys.

    _Supported key:_ `PRODUCT`

    _Supported values:_

      * `CentOS6.5`

      * `CentOS6.6`

      * `CentOS6.7`

      * `CentOS6.8`

      * `CentOS6.9`

      * `CentOS7.0`

      * `CentOS7.1`

      * `CentOS7.2`

      * `CentOS7.3`

      * `CentOS7.4`

      * `*`

    _Use a wildcard character (*) to target all supported operating system
    versions._

    _Supported key:_ `CLASSIFICATION`

    _Supported values:_

      * `Security`

      * `Bugfix`

      * `Enhancement`

      * `Recommended`

      * `Newpackage`

    _Supported key:_ `SEVERITY`

    _Supported values:_

      * `Critical`

      * `Important`

      * `Medium`

      * `Low`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(PatchFilterKey),
            ),
            (
                "values",
                "Values",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The key for the filter.

    # See PatchFilter for lists of valid keys for each operating system type.
    key: "PatchFilterKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The value for the filter key.

    # See PatchFilter for lists of valid values for each key based on operating
    # system type.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class PatchFilterGroup(autoboto.ShapeBase):
    """
    A set of patch filters, typically used for approval rules.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch_filters",
                "PatchFilters",
                autoboto.TypeInfo(typing.List[PatchFilter]),
            ),
        ]

    # The set of patch filters that make up the group.
    patch_filters: typing.List["PatchFilter"] = dataclasses.field(
        default_factory=list,
    )


class PatchFilterKey(Enum):
    PRODUCT = "PRODUCT"
    CLASSIFICATION = "CLASSIFICATION"
    MSRC_SEVERITY = "MSRC_SEVERITY"
    PATCH_ID = "PATCH_ID"
    SECTION = "SECTION"
    PRIORITY = "PRIORITY"
    SEVERITY = "SEVERITY"


@dataclasses.dataclass
class PatchGroupPatchBaselineMapping(autoboto.ShapeBase):
    """
    The mapping between a patch group and the patch baseline the patch group is
    registered with.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch_group",
                "PatchGroup",
                autoboto.TypeInfo(str),
            ),
            (
                "baseline_identity",
                "BaselineIdentity",
                autoboto.TypeInfo(PatchBaselineIdentity),
            ),
        ]

    # The name of the patch group registered with the patch baseline.
    patch_group: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The patch baseline the patch group is registered with.
    baseline_identity: "PatchBaselineIdentity" = dataclasses.field(
        default_factory=dict,
    )


class PatchOperationType(Enum):
    Scan = "Scan"
    Install = "Install"


@dataclasses.dataclass
class PatchOrchestratorFilter(autoboto.ShapeBase):
    """
    Defines a filter used in Patch Manager APIs.
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

    # The key for the filter.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value for the filter.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class PatchRule(autoboto.ShapeBase):
    """
    Defines an approval rule for a patch baseline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch_filter_group",
                "PatchFilterGroup",
                autoboto.TypeInfo(PatchFilterGroup),
            ),
            (
                "approve_after_days",
                "ApproveAfterDays",
                autoboto.TypeInfo(int),
            ),
            (
                "compliance_level",
                "ComplianceLevel",
                autoboto.TypeInfo(PatchComplianceLevel),
            ),
            (
                "enable_non_security",
                "EnableNonSecurity",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The patch filter group that defines the criteria for the rule.
    patch_filter_group: "PatchFilterGroup" = dataclasses.field(
        default_factory=dict,
    )

    # The number of days after the release date of each patch matched by the rule
    # that the patch is marked as approved in the patch baseline. For example, a
    # value of `7` means that patches are approved seven days after they are
    # released.
    approve_after_days: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A compliance severity level for all approved patches in a patch baseline.
    # Valid compliance severity levels include the following: Unspecified,
    # Critical, High, Medium, Low, and Informational.
    compliance_level: "PatchComplianceLevel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # For instances identified by the approval rule filters, enables a patch
    # baseline to apply non-security updates available in the specified
    # repository. The default value is 'false'. Applies to Linux instances only.
    enable_non_security: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PatchRuleGroup(autoboto.ShapeBase):
    """
    A set of rules defining the approval rules for a patch baseline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch_rules",
                "PatchRules",
                autoboto.TypeInfo(typing.List[PatchRule]),
            ),
        ]

    # The rules that make up the rule group.
    patch_rules: typing.List["PatchRule"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class PatchSource(autoboto.ShapeBase):
    """
    Information about the patches to use to update the instances, including target
    operating systems and source repository. Applies to Linux instances only.
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
                "products",
                "Products",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "configuration",
                "Configuration",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name specified to identify the patch source.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The specific operating system versions a patch repository applies to, such
    # as "Ubuntu16.04", "AmazonLinux2016.09", "RedhatEnterpriseLinux7.2" or
    # "Suse12.7". For lists of supported product values, see PatchFilter.
    products: typing.List[str] = dataclasses.field(default_factory=list, )

    # The value of the yum repo configuration. For example:

    # `cachedir=/var/cache/yum/$basesearch`

    # `$releasever`

    # `keepcache=0`

    # `debuglevel=2`
    configuration: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PatchStatus(autoboto.ShapeBase):
    """
    Information about the approval status of a patch.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_status",
                "DeploymentStatus",
                autoboto.TypeInfo(PatchDeploymentStatus),
            ),
            (
                "compliance_level",
                "ComplianceLevel",
                autoboto.TypeInfo(PatchComplianceLevel),
            ),
            (
                "approval_date",
                "ApprovalDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The approval status of a patch (APPROVED, PENDING_APPROVAL,
    # EXPLICIT_APPROVED, EXPLICIT_REJECTED).
    deployment_status: "PatchDeploymentStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The compliance severity level for a patch.
    compliance_level: "PatchComplianceLevel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date the patch was approved (or will be approved if the status is
    # PENDING_APPROVAL).
    approval_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class PingStatus(Enum):
    Online = "Online"
    ConnectionLost = "ConnectionLost"
    Inactive = "Inactive"


class PlatformType(Enum):
    Windows = "Windows"
    Linux = "Linux"


@dataclasses.dataclass
class PutComplianceItemsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "compliance_type",
                "ComplianceType",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_summary",
                "ExecutionSummary",
                autoboto.TypeInfo(ComplianceExecutionSummary),
            ),
            (
                "items",
                "Items",
                autoboto.TypeInfo(typing.List[ComplianceItemEntry]),
            ),
            (
                "item_content_hash",
                "ItemContentHash",
                autoboto.TypeInfo(str),
            ),
        ]

    # Specify an ID for this resource. For a managed instance, this is the
    # instance ID.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specify the type of resource. `ManagedInstance` is currently the only
    # supported resource type.
    resource_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specify the compliance type. For example, specify Association (for a State
    # Manager association), Patch, or Custom:`string`.
    compliance_type: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A summary of the call execution that includes an execution ID, the type of
    # execution (for example, `Command`), and the date/time of the execution
    # using a datetime object that is saved in the following format: yyyy-MM-
    # dd'T'HH:mm:ss'Z'.
    execution_summary: "ComplianceExecutionSummary" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the compliance as defined by the resource type. For
    # example, for a patch compliance type, `Items` includes information about
    # the PatchSeverity, Classification, etc.
    items: typing.List["ComplianceItemEntry"] = dataclasses.field(
        default_factory=list,
    )

    # MD5 or SHA-256 content hash. The content hash is used to determine if
    # existing information should be overwritten or ignored. If the content
    # hashes match, the request to put compliance information is ignored.
    item_content_hash: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutComplianceItemsResult(autoboto.OutputShapeBase):
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
class PutInventoryRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "items",
                "Items",
                autoboto.TypeInfo(typing.List[InventoryItem]),
            ),
        ]

    # One or more instance IDs where you want to add or update inventory items.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The inventory items that you want to add or update on instances.
    items: typing.List["InventoryItem"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class PutInventoryResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the request.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutParameterRequest(autoboto.ShapeBase):
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
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(ParameterType),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "key_id",
                "KeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "overwrite",
                "Overwrite",
                autoboto.TypeInfo(bool),
            ),
            (
                "allowed_pattern",
                "AllowedPattern",
                autoboto.TypeInfo(str),
            ),
        ]

    # The fully qualified name of the parameter that you want to add to the
    # system. The fully qualified name includes the complete hierarchy of the
    # parameter path and name. For example: `/Dev/DBServer/MySQL/db-string13`

    # Naming Constraints:

    #   * Parameter names are case sensitive.

    #   * A parameter name must be unique within an AWS Region

    #   * A parameter name can't be prefixed with "aws" or "ssm" (case-insensitive).

    #   * Parameter names can include only the following symbols and letters: `a-zA-Z0-9_.-/`

    #   * A parameter name can't include spaces.

    #   * Parameter hierarchies are limited to a maximum depth of fifteen levels.

    # For additional information about valid values for parameter names, see
    # [Requirements and Constraints for Parameter
    # Names](http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-
    # parameter-name-constraints.html) in the _AWS Systems Manager User Guide_.

    # The maximum length constraint listed below includes capacity for additional
    # system attributes that are not part of the name. The maximum length for the
    # fully qualified parameter name is 1011 characters.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The parameter value that you want to add to the system.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of parameter that you want to add to the system.

    # Items in a `StringList` must be separated by a comma (,). You can't use
    # other punctuation or special character to escape items in the list. If you
    # have a parameter value that requires a comma, then use the `String` data
    # type.

    # `SecureString` is not currently supported for AWS CloudFormation templates
    # or in the China Regions.
    type: "ParameterType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the parameter that you want to add to the system.
    # Optional but recommended.

    # Do not enter personally identifiable information in this field.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The KMS Key ID that you want to use to encrypt a parameter. Either the
    # default AWS Key Management Service (AWS KMS) key automatically assigned to
    # your AWS account or a custom key. Required for parameters that use the
    # `SecureString` data type.

    # If you don't specify a key ID, the system uses the default key associated
    # with your AWS account.

    #   * To use your default AWS KMS key, choose the `SecureString` data type, and do _not_ specify the `Key ID` when you create the parameter. The system automatically populates `Key ID` with your default KMS key.

    #   * To use a custom KMS key, choose the `SecureString` data type with the `Key ID` parameter.
    key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Overwrite an existing parameter. If not specified, will default to "false".
    overwrite: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A regular expression used to validate the parameter value. For example, for
    # String types with values restricted to numbers, you can specify the
    # following: AllowedPattern=^\d+$
    allowed_pattern: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutParameterResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The new version number of a parameter. If you edit a parameter value,
    # Parameter Store automatically creates a new version and assigns this new
    # version a unique ID. You can reference a parameter version ID in API
    # actions or in Systems Manager documents (SSM documents). By default, if you
    # don't specify a specific version, the system returns the latest parameter
    # value when a parameter is called.
    version: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterDefaultPatchBaselineRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the patch baseline that should be the default patch baseline.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterDefaultPatchBaselineResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the default patch baseline.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterPatchBaselineForPatchGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
            (
                "patch_group",
                "PatchGroup",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the patch baseline to register the patch group with.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the patch group that should be registered with the patch
    # baseline.
    patch_group: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterPatchBaselineForPatchGroupResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
            (
                "patch_group",
                "PatchGroup",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the patch baseline the patch group was registered with.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the patch group registered with the patch baseline.
    patch_group: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterTargetWithMaintenanceWindowRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(MaintenanceWindowResourceType),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "owner_information",
                "OwnerInformation",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "client_token",
                "ClientToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window the target should be registered with.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of target being registered with the Maintenance Window.
    resource_type: "MaintenanceWindowResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The targets (either instances or tags).

    # Specify instances using the following format:

    # `Key=InstanceIds,Values=<instance-id-1>,<instance-id-2>`

    # Specify tags using either of the following formats:

    # `Key=tag:<tag-key>,Values=<tag-value-1>,<tag-value-2>`

    # `Key=tag-key,Values=<tag-key-1>,<tag-key-2>`
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # User-provided value that will be included in any CloudWatch events raised
    # while running tasks for these targets in this Maintenance Window.
    owner_information: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An optional name for the target.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional description for the target.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # User-provided idempotency token.
    client_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterTargetWithMaintenanceWindowResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_target_id",
                "WindowTargetId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the target definition in this Maintenance Window.
    window_target_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RegisterTaskWithMaintenanceWindowRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "task_arn",
                "TaskArn",
                autoboto.TypeInfo(str),
            ),
            (
                "task_type",
                "TaskType",
                autoboto.TypeInfo(MaintenanceWindowTaskType),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                autoboto.TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                autoboto.TypeInfo(str),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "task_parameters",
                "TaskParameters",
                autoboto.TypeInfo(
                    typing.Dict[str,
                                MaintenanceWindowTaskParameterValueExpression]
                ),
            ),
            (
                "task_invocation_parameters",
                "TaskInvocationParameters",
                autoboto.TypeInfo(MaintenanceWindowTaskInvocationParameters),
            ),
            (
                "priority",
                "Priority",
                autoboto.TypeInfo(int),
            ),
            (
                "logging_info",
                "LoggingInfo",
                autoboto.TypeInfo(LoggingInfo),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "client_token",
                "ClientToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window the task should be added to.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The targets (either instances or Maintenance Window targets).

    # Specify instances using the following format:

    # `Key=InstanceIds,Values=<instance-id-1>,<instance-id-2>`

    # Specify Maintenance Window targets using the following format:

    # `Key=<WindowTargetIds>,Values=<window-target-id-1>,<window-target-id-2>`
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # The ARN of the task to execute
    task_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of task being registered.
    task_type: "MaintenanceWindowTaskType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of targets this task can be run for in parallel.
    max_concurrency: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of errors allowed before this task stops being
    # scheduled.
    max_errors: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The role to assume when running the Maintenance Window task.

    # If you do not specify a service role ARN, Systems Manager will use your
    # account's service-linked role for Systems Manager by default. If no
    # service-linked role for Systems Manager exists in your account, it will be
    # created when you run `RegisterTaskWithMaintenanceWindow` without specifying
    # a service role ARN.

    # For more information, see [Service-Linked Role Permissions for Systems
    # Manager](http://docs.aws.amazon.com/systems-manager/latest/userguide/using-
    # service-linked-roles.html#slr-permissions) and [Should I Use a Service-
    # Linked Role or a Custom Service Role to Run Maintenance Window Tasks?
    # ](http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-
    # maintenance-permissions.html#maintenance-window-tasks-service-role) in the
    # _AWS Systems Manager User Guide_.
    service_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameters that should be passed to the task when it is executed.

    # `TaskParameters` has been deprecated. To specify parameters to pass to a
    # task when it runs, instead use the `Parameters` option in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    task_parameters: typing.Dict[
        str, "MaintenanceWindowTaskParameterValueExpression"
    ] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameters that the task should use during execution. Populate only the
    # fields that match the task type. All other fields should be empty.
    task_invocation_parameters: "MaintenanceWindowTaskInvocationParameters" = dataclasses.field(
        default_factory=dict,
    )

    # The priority of the task in the Maintenance Window, the lower the number
    # the higher the priority. Tasks in a Maintenance Window are scheduled in
    # priority order with tasks that have the same priority scheduled in
    # parallel.
    priority: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A structure containing information about an Amazon S3 bucket to write
    # instance-level logs to.

    # `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    # instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    logging_info: "LoggingInfo" = dataclasses.field(default_factory=dict, )

    # An optional name for the task.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional description for the task.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # User-provided idempotency token.
    client_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterTaskWithMaintenanceWindowResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_task_id",
                "WindowTaskId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The id of the task in the Maintenance Window.
    window_task_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveTagsFromResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(ResourceTypeForTagging),
            ),
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The type of resource of which you want to remove a tag.

    # The ManagedInstance type for this API action is only for on-premises
    # managed instances. You must specify the the name of the managed instance in
    # the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.
    resource_type: "ResourceTypeForTagging" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The resource ID for which you want to remove tags. Use the ID of the
    # resource. Here are some examples:

    # ManagedInstance: mi-012345abcde

    # MaintenanceWindow: mw-012345abcde

    # PatchBaseline: pb-012345abcde

    # For the Document and Parameter values, use the name of the resource.

    # The ManagedInstance type for this API action is only for on-premises
    # managed instances. You must specify the the name of the managed instance in
    # the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Tag keys that you want to remove from the specified resource.
    tag_keys: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class RemoveTagsFromResourceResult(autoboto.OutputShapeBase):
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
class ResolvedTargets(autoboto.ShapeBase):
    """
    Information about targets that resolved during the Automation execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_values",
                "ParameterValues",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "truncated",
                "Truncated",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A list of parameter values sent to targets that resolved during the
    # Automation execution.
    parameter_values: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A boolean value indicating whether the resolved target list is truncated.
    truncated: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceComplianceSummaryItem(autoboto.ShapeBase):
    """
    Compliance summary information for a specific resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compliance_type",
                "ComplianceType",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(ComplianceStatus),
            ),
            (
                "overall_severity",
                "OverallSeverity",
                autoboto.TypeInfo(ComplianceSeverity),
            ),
            (
                "execution_summary",
                "ExecutionSummary",
                autoboto.TypeInfo(ComplianceExecutionSummary),
            ),
            (
                "compliant_summary",
                "CompliantSummary",
                autoboto.TypeInfo(CompliantSummary),
            ),
            (
                "non_compliant_summary",
                "NonCompliantSummary",
                autoboto.TypeInfo(NonCompliantSummary),
            ),
        ]

    # The compliance type.
    compliance_type: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The resource type.
    resource_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The resource ID.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The compliance status for the resource.
    status: "ComplianceStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The highest severity item found for the resource. The resource is compliant
    # for this item.
    overall_severity: "ComplianceSeverity" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the execution.
    execution_summary: "ComplianceExecutionSummary" = dataclasses.field(
        default_factory=dict,
    )

    # A list of items that are compliant for the resource.
    compliant_summary: "CompliantSummary" = dataclasses.field(
        default_factory=dict,
    )

    # A list of items that aren't compliant for the resource.
    non_compliant_summary: "NonCompliantSummary" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ResourceDataSyncAlreadyExistsException(autoboto.ShapeBase):
    """
    A sync configuration with the same name already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sync_name",
                "SyncName",
                autoboto.TypeInfo(str),
            ),
        ]

    sync_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceDataSyncCountExceededException(autoboto.ShapeBase):
    """
    You have exceeded the allowed maximum sync configurations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceDataSyncInvalidConfigurationException(autoboto.ShapeBase):
    """
    The specified sync configuration is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceDataSyncItem(autoboto.ShapeBase):
    """
    Information about a Resource Data Sync configuration, including its current
    status and last successful sync.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sync_name",
                "SyncName",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_destination",
                "S3Destination",
                autoboto.TypeInfo(ResourceDataSyncS3Destination),
            ),
            (
                "last_sync_time",
                "LastSyncTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_successful_sync_time",
                "LastSuccessfulSyncTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_status",
                "LastStatus",
                autoboto.TypeInfo(LastResourceDataSyncStatus),
            ),
            (
                "sync_created_time",
                "SyncCreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_sync_status_message",
                "LastSyncStatusMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the Resource Data Sync.
    sync_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Configuration information for the target Amazon S3 bucket.
    s3_destination: "ResourceDataSyncS3Destination" = dataclasses.field(
        default_factory=dict,
    )

    # The last time the configuration attempted to sync (UTC).
    last_sync_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The last time the sync operations returned a status of `SUCCESSFUL` (UTC).
    last_successful_sync_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status reported by the last sync.
    last_status: "LastResourceDataSyncStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time the configuration was created (UTC).
    sync_created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status message details reported by the last sync.
    last_sync_status_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceDataSyncNotFoundException(autoboto.ShapeBase):
    """
    The specified sync name was not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sync_name",
                "SyncName",
                autoboto.TypeInfo(str),
            ),
        ]

    sync_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceDataSyncS3Destination(autoboto.ShapeBase):
    """
    Information about the target Amazon S3 bucket for the Resource Data Sync.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket_name",
                "BucketName",
                autoboto.TypeInfo(str),
            ),
            (
                "sync_format",
                "SyncFormat",
                autoboto.TypeInfo(ResourceDataSyncS3Format),
            ),
            (
                "region",
                "Region",
                autoboto.TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "awskms_key_arn",
                "AWSKMSKeyARN",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the Amazon S3 bucket where the aggregated data is stored.
    bucket_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A supported sync format. The following format is currently supported:
    # JsonSerDe
    sync_format: "ResourceDataSyncS3Format" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS Region with the Amazon S3 bucket targeted by the Resource Data
    # Sync.
    region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An Amazon S3 prefix for the bucket.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of an encryption key for a destination in Amazon S3. Must belong to
    # the same region as the destination Amazon S3 bucket.
    awskms_key_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ResourceDataSyncS3Format(Enum):
    JsonSerDe = "JsonSerDe"


@dataclasses.dataclass
class ResourceInUseException(autoboto.ShapeBase):
    """
    Error returned if an attempt is made to delete a patch baseline that is
    registered for a patch group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceLimitExceededException(autoboto.ShapeBase):
    """
    Error returned when the caller has exceeded the default resource limits. For
    example, too many Maintenance Windows or Patch baselines have been created.

    For information about resource limits in Systems Manager, see [AWS Systems
    Manager
    Limits](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_ssm).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ResourceType(Enum):
    ManagedInstance = "ManagedInstance"
    Document = "Document"
    EC2Instance = "EC2Instance"


class ResourceTypeForTagging(Enum):
    Document = "Document"
    ManagedInstance = "ManagedInstance"
    MaintenanceWindow = "MaintenanceWindow"
    Parameter = "Parameter"
    PatchBaseline = "PatchBaseline"


@dataclasses.dataclass
class ResultAttribute(autoboto.ShapeBase):
    """
    The inventory item result attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the inventory item type. Valid value: AWS:InstanceInformation.
    # Default Value: AWS:InstanceInformation.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class S3OutputLocation(autoboto.ShapeBase):
    """
    An Amazon S3 bucket where you want to store the results of this request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_s3_region",
                "OutputS3Region",
                autoboto.TypeInfo(str),
            ),
            (
                "output_s3_bucket_name",
                "OutputS3BucketName",
                autoboto.TypeInfo(str),
            ),
            (
                "output_s3_key_prefix",
                "OutputS3KeyPrefix",
                autoboto.TypeInfo(str),
            ),
        ]

    # (Deprecated) You can no longer specify this parameter. The system ignores
    # it. Instead, Systems Manager automatically determines the Amazon S3 bucket
    # region.
    output_s3_region: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the Amazon S3 bucket.
    output_s3_bucket_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon S3 bucket subfolder.
    output_s3_key_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class S3OutputUrl(autoboto.ShapeBase):
    """
    A URL for the Amazon S3 bucket where you want to store the results of this
    request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_url",
                "OutputUrl",
                autoboto.TypeInfo(str),
            ),
        ]

    # A URL for an Amazon S3 bucket where you want to store the results of this
    # request.
    output_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendAutomationSignalRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "automation_execution_id",
                "AutomationExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "signal_type",
                "SignalType",
                autoboto.TypeInfo(SignalType),
            ),
            (
                "payload",
                "Payload",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
        ]

    # The unique identifier for an existing Automation execution that you want to
    # send the signal to.
    automation_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of signal. Valid signal types include the following: Approve and
    # Reject
    signal_type: "SignalType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The data sent with the signal. The data schema depends on the type of
    # signal used in the request.
    payload: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SendAutomationSignalResult(autoboto.OutputShapeBase):
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
class SendCommandRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_name",
                "DocumentName",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_ids",
                "InstanceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "document_hash",
                "DocumentHash",
                autoboto.TypeInfo(str),
            ),
            (
                "document_hash_type",
                "DocumentHashType",
                autoboto.TypeInfo(DocumentHashType),
            ),
            (
                "timeout_seconds",
                "TimeoutSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "comment",
                "Comment",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "output_s3_region",
                "OutputS3Region",
                autoboto.TypeInfo(str),
            ),
            (
                "output_s3_bucket_name",
                "OutputS3BucketName",
                autoboto.TypeInfo(str),
            ),
            (
                "output_s3_key_prefix",
                "OutputS3KeyPrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                autoboto.TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                autoboto.TypeInfo(str),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "notification_config",
                "NotificationConfig",
                autoboto.TypeInfo(NotificationConfig),
            ),
            (
                "cloud_watch_output_config",
                "CloudWatchOutputConfig",
                autoboto.TypeInfo(CloudWatchOutputConfig),
            ),
        ]

    # Required. The name of the Systems Manager document to execute. This can be
    # a public document or a custom document.
    document_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance IDs where the command should execute. You can specify a
    # maximum of 50 IDs. If you prefer not to list individual instance IDs, you
    # can instead send commands to a fleet of instances using the Targets
    # parameter, which accepts EC2 tags. For more information about how to use
    # Targets, see [Sending Commands to a
    # Fleet](http://docs.aws.amazon.com/systems-manager/latest/userguide/send-
    # commands-multiple.html) in the _AWS Systems Manager User Guide_.
    instance_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # (Optional) An array of search criteria that targets instances using a
    # Key,Value combination that you specify. Targets is required if you don't
    # provide one or more instance IDs in the call. For more information about
    # how to use Targets, see [Sending Commands to a
    # Fleet](http://docs.aws.amazon.com/systems-manager/latest/userguide/send-
    # commands-multiple.html) in the _AWS Systems Manager User Guide_.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # The SSM document version to use in the request. You can specify $DEFAULT,
    # $LATEST, or a specific version number. If you execute commands by using the
    # AWS CLI, then you must escape the first two options by using a backslash.
    # If you specify a version number, then you don't need to use the backslash.
    # For example:

    # \--document-version "\$DEFAULT"

    # \--document-version "\$LATEST"

    # \--document-version "3"
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Sha256 or Sha1 hash created by the system when the document was
    # created.

    # Sha1 hashes have been deprecated.
    document_hash: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Sha256 or Sha1.

    # Sha1 hashes have been deprecated.
    document_hash_type: "DocumentHashType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If this time is reached and the command has not already started executing,
    # it will not run.
    timeout_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # User-specified information about the command, such as a brief description
    # of what the command should do.
    comment: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The required and optional parameters specified in the document being
    # executed.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # (Deprecated) You can no longer specify this parameter. The system ignores
    # it. Instead, Systems Manager automatically determines the Amazon S3 bucket
    # region.
    output_s3_region: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the S3 bucket where command execution responses should be
    # stored.
    output_s3_bucket_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The directory structure within the S3 bucket where the responses should be
    # stored.
    output_s3_key_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # (Optional) The maximum number of instances that are allowed to execute the
    # command at the same time. You can specify a number such as 10 or a
    # percentage such as 10%. The default value is 50. For more information about
    # how to use MaxConcurrency, see [Using Concurrency
    # Controls](http://docs.aws.amazon.com/systems-manager/latest/userguide/send-
    # commands-multiple.html#send-commands-velocity) in the _AWS Systems Manager
    # User Guide_.
    max_concurrency: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of errors allowed without the command failing. When the
    # command fails one more time beyond the value of MaxErrors, the systems
    # stops sending the command to additional targets. You can specify a number
    # like 10 or a percentage like 10%. The default value is 0. For more
    # information about how to use MaxErrors, see [Using Error
    # Controls](http://docs.aws.amazon.com/systems-manager/latest/userguide/send-
    # commands-multiple.html#send-commands-maxerrors) in the _AWS Systems Manager
    # User Guide_.
    max_errors: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The IAM role that Systems Manager uses to send notifications.
    service_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Configurations for sending notifications.
    notification_config: "NotificationConfig" = dataclasses.field(
        default_factory=dict,
    )

    # Enables Systems Manager to send Run Command output to Amazon CloudWatch
    # Logs.
    cloud_watch_output_config: "CloudWatchOutputConfig" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SendCommandResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "command",
                "Command",
                autoboto.TypeInfo(Command),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The request as it was received by Systems Manager. Also provides the
    # command ID which can be used future references to this request.
    command: "Command" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class SeveritySummary(autoboto.ShapeBase):
    """
    The number of managed instances found for each patch severity level defined in
    the request filter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "critical_count",
                "CriticalCount",
                autoboto.TypeInfo(int),
            ),
            (
                "high_count",
                "HighCount",
                autoboto.TypeInfo(int),
            ),
            (
                "medium_count",
                "MediumCount",
                autoboto.TypeInfo(int),
            ),
            (
                "low_count",
                "LowCount",
                autoboto.TypeInfo(int),
            ),
            (
                "informational_count",
                "InformationalCount",
                autoboto.TypeInfo(int),
            ),
            (
                "unspecified_count",
                "UnspecifiedCount",
                autoboto.TypeInfo(int),
            ),
        ]

    # The total number of resources or compliance items that have a severity
    # level of critical. Critical severity is determined by the organization that
    # published the compliance items.
    critical_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The total number of resources or compliance items that have a severity
    # level of high. High severity is determined by the organization that
    # published the compliance items.
    high_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total number of resources or compliance items that have a severity
    # level of medium. Medium severity is determined by the organization that
    # published the compliance items.
    medium_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total number of resources or compliance items that have a severity
    # level of low. Low severity is determined by the organization that published
    # the compliance items.
    low_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total number of resources or compliance items that have a severity
    # level of informational. Informational severity is determined by the
    # organization that published the compliance items.
    informational_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The total number of resources or compliance items that have a severity
    # level of unspecified. Unspecified severity is determined by the
    # organization that published the compliance items.
    unspecified_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class SignalType(Enum):
    Approve = "Approve"
    Reject = "Reject"
    StartStep = "StartStep"
    StopStep = "StopStep"
    Resume = "Resume"


@dataclasses.dataclass
class StartAssociationsOnceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_ids",
                "AssociationIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The association IDs that you want to execute immediately and only one time.
    association_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class StartAssociationsOnceResult(autoboto.OutputShapeBase):
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
class StartAutomationExecutionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_name",
                "DocumentName",
                autoboto.TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "client_token",
                "ClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "mode",
                "Mode",
                autoboto.TypeInfo(ExecutionMode),
            ),
            (
                "target_parameter_name",
                "TargetParameterName",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "target_maps",
                "TargetMaps",
                autoboto.TypeInfo(
                    typing.List[typing.Dict[str, typing.List[str]]]
                ),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                autoboto.TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the Automation document to use for this execution.
    document_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version of the Automation document to use for this execution.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A key-value map of execution parameters, which match the declared
    # parameters in the Automation document.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # User-provided idempotency token. The token must be unique, is case
    # insensitive, enforces the UUID format, and can't be reused.
    client_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The execution mode of the automation. Valid modes include the following:
    # Auto and Interactive. The default mode is Auto.
    mode: "ExecutionMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the parameter used as the target resource for the rate-
    # controlled execution. Required if you specify Targets.
    target_parameter_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A key-value mapping to target resources. Required if you specify
    # TargetParameterName.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # A key-value mapping of document parameters to target resources. Both
    # Targets and TargetMaps cannot be specified together.
    target_maps: typing.List[typing.Dict[str, typing.List[str]]
                            ] = dataclasses.field(
                                default_factory=list,
                            )

    # The maximum number of targets allowed to run this task in parallel. You can
    # specify a number, such as 10, or a percentage, such as 10%. The default
    # value is 10.
    max_concurrency: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of errors that are allowed before the system stops running the
    # automation on additional targets. You can specify either an absolute number
    # of errors, for example 10, or a percentage of the target set, for example
    # 10%. If you specify 3, for example, the system stops running the automation
    # when the fourth error is received. If you specify 0, then the system stops
    # running the automation on additional targets after the first error result
    # is returned. If you run an automation on 50 resources and set max-errors to
    # 10%, then the system stops running the automation on additional targets
    # when the sixth error is received.

    # Executions that are already running an automation when max-errors is
    # reached are allowed to complete, but some of these executions may fail as
    # well. If you need to ensure that there won't be more than max-errors failed
    # executions, set max-concurrency to 1 so the executions proceed one at a
    # time.
    max_errors: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartAutomationExecutionResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "automation_execution_id",
                "AutomationExecutionId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The unique ID of a newly scheduled automation execution.
    automation_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StatusUnchanged(autoboto.ShapeBase):
    """
    The updated status is the same as the current status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StepExecution(autoboto.ShapeBase):
    """
    Detailed information about an the execution state of an Automation step.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "step_name",
                "StepName",
                autoboto.TypeInfo(str),
            ),
            (
                "action",
                "Action",
                autoboto.TypeInfo(str),
            ),
            (
                "timeout_seconds",
                "TimeoutSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "on_failure",
                "OnFailure",
                autoboto.TypeInfo(str),
            ),
            (
                "max_attempts",
                "MaxAttempts",
                autoboto.TypeInfo(int),
            ),
            (
                "execution_start_time",
                "ExecutionStartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "execution_end_time",
                "ExecutionEndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "step_status",
                "StepStatus",
                autoboto.TypeInfo(AutomationExecutionStatus),
            ),
            (
                "response_code",
                "ResponseCode",
                autoboto.TypeInfo(str),
            ),
            (
                "inputs",
                "Inputs",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "outputs",
                "Outputs",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "response",
                "Response",
                autoboto.TypeInfo(str),
            ),
            (
                "failure_message",
                "FailureMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "failure_details",
                "FailureDetails",
                autoboto.TypeInfo(FailureDetails),
            ),
            (
                "step_execution_id",
                "StepExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "overridden_parameters",
                "OverriddenParameters",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "is_end",
                "IsEnd",
                autoboto.TypeInfo(bool),
            ),
            (
                "next_step",
                "NextStep",
                autoboto.TypeInfo(str),
            ),
            (
                "is_critical",
                "IsCritical",
                autoboto.TypeInfo(bool),
            ),
            (
                "valid_next_steps",
                "ValidNextSteps",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of this execution step.
    step_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The action this step performs. The action determines the behavior of the
    # step.
    action: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The timeout seconds of the step.
    timeout_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The action to take if the step fails. The default value is Abort.
    on_failure: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of tries to run the action of the step. The default
    # value is 1.
    max_attempts: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If a step has begun execution, this contains the time the step started. If
    # the step is in Pending status, this field is not populated.
    execution_start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If a step has finished execution, this contains the time the execution
    # ended. If the step has not yet concluded, this field is not populated.
    execution_end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The execution status for this step. Valid values include: Pending,
    # InProgress, Success, Cancelled, Failed, and TimedOut.
    step_status: "AutomationExecutionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The response code returned by the execution of the step.
    response_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Fully-resolved values passed into the step before execution.
    inputs: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Returned values from the execution of the step.
    outputs: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A message associated with the response code for an execution.
    response: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If a step failed, this message explains why the execution failed.
    failure_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the Automation failure.
    failure_details: "FailureDetails" = dataclasses.field(
        default_factory=dict,
    )

    # The unique ID of a step execution.
    step_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A user-specified list of parameters to override when executing a step.
    overridden_parameters: typing.Dict[str, typing.List[str]
                                      ] = dataclasses.field(
                                          default=autoboto.ShapeBase.NOT_SET,
                                      )

    # The flag which can be used to end automation no matter whether the step
    # succeeds or fails.
    is_end: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The next step after the step succeeds.
    next_step: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The flag which can be used to help decide whether the failure of current
    # step leads to the Automation failure.
    is_critical: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Strategies used when step fails, we support Continue and Abort. Abort will
    # fail the automation when the step fails. Continue will ignore the failure
    # of current step and allow automation to execute the next step. With
    # conditional branching, we add step:stepName to support the automation to go
    # to another specific step.
    valid_next_steps: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class StepExecutionFilter(autoboto.ShapeBase):
    """
    A filter to limit the amount of step execution information returned by the call.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(StepExecutionFilterKey),
            ),
            (
                "values",
                "Values",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # One or more keys to limit the results. Valid filter keys include the
    # following: StepName, Action, StepExecutionId, StepExecutionStatus,
    # StartTimeBefore, StartTimeAfter.
    key: "StepExecutionFilterKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The values of the filter key.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


class StepExecutionFilterKey(Enum):
    StartTimeBefore = "StartTimeBefore"
    StartTimeAfter = "StartTimeAfter"
    StepExecutionStatus = "StepExecutionStatus"
    StepExecutionId = "StepExecutionId"
    StepName = "StepName"
    Action = "Action"


@dataclasses.dataclass
class StopAutomationExecutionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "automation_execution_id",
                "AutomationExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(StopType),
            ),
        ]

    # The execution ID of the Automation to stop.
    automation_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stop request type. Valid types include the following: Cancel and
    # Complete. The default type is Cancel.
    type: "StopType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopAutomationExecutionResult(autoboto.OutputShapeBase):
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


class StopType(Enum):
    Complete = "Complete"
    Cancel = "Cancel"


@dataclasses.dataclass
class SubTypeCountLimitExceededException(autoboto.ShapeBase):
    """
    The sub-type count exceeded the limit for the inventory type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    """
    Metadata that you assign to your AWS resources. Tags enable you to categorize
    your resources in different ways, for example, by purpose, owner, or
    environment. In Systems Manager, you can apply tags to documents, managed
    instances, Maintenance Windows, Parameter Store parameters, and patch baselines.
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

    # The name of the tag.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value of the tag.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Target(autoboto.ShapeBase):
    """
    An array of search criteria that targets instances using a Key,Value combination
    that you specify. `Targets` is required if you don't provide one or more
    instance IDs in the call.
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

    # User-defined criteria for sending commands that target instances that meet
    # the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more
    # information about how to send commands that target instances using
    # Key,Value parameters, see [Targeting Multiple
    # Instances](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/send-commands-multiple.html#send-commands-
    # targeting) in the _AWS Systems Manager User Guide_.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # User-defined criteria that maps to Key. For example, if you specified
    # tag:ServerRole, you could specify value:WebServer to execute a command on
    # instances that include Amazon EC2 tags of ServerRole,WebServer. For more
    # information about how to send commands that target instances using
    # Key,Value parameters, see [Sending Commands to a
    # Fleet](http://docs.aws.amazon.com/systems-manager/latest/userguide/send-
    # commands-multiple.html) in the _AWS Systems Manager User Guide_.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class TargetInUseException(autoboto.ShapeBase):
    """
    You specified the `Safe` option for the DeregisterTargetFromMaintenanceWindow
    operation, but the target is still referenced in a task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyTagsError(autoboto.ShapeBase):
    """
    The Targets parameter includes too many tags. Remove one or more tags and try
    the command again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TooManyUpdates(autoboto.ShapeBase):
    """
    There are concurrent updates for a resource that supports one update at a time.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TotalSizeLimitExceededException(autoboto.ShapeBase):
    """
    The size of inventory data has exceeded the total size limit for the resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsupportedInventoryItemContextException(autoboto.ShapeBase):
    """
    The `Context` attribute that you specified for the `InventoryItem` is not
    allowed for this inventory type. You can only use the `Context` attribute with
    inventory types like `AWS:ComplianceItem`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    type_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsupportedInventorySchemaVersionException(autoboto.ShapeBase):
    """
    Inventory item type schema version has to match supported versions in the
    service. Check output of GetInventorySchema to see the available schema version
    for each type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsupportedOperatingSystem(autoboto.ShapeBase):
    """
    The operating systems you specified is not supported, or the operation is not
    supported for the operating system. Valid operating systems include: Windows,
    AmazonLinux, RedhatEnterpriseLinux, and Ubuntu.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsupportedParameterType(autoboto.ShapeBase):
    """
    The parameter type is not supported.
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
class UnsupportedPlatformType(autoboto.ShapeBase):
    """
    The document does not support the platform type of the given instance ID(s). For
    example, you sent an document for a Windows instance to a Linux instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateAssociationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                autoboto.TypeInfo(str),
            ),
            (
                "output_location",
                "OutputLocation",
                autoboto.TypeInfo(InstanceAssociationOutputLocation),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "association_name",
                "AssociationName",
                autoboto.TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the association you want to update.
    association_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameters you want to update for the association. If you create a
    # parameter using Parameter Store, you can reference the parameter using
    # {{ssm:parameter-name}}
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The document version you want update for the association.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The cron expression used to schedule the association that you want to
    # update.
    schedule_expression: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An Amazon S3 bucket where you want to store the results of this request.
    output_location: "InstanceAssociationOutputLocation" = dataclasses.field(
        default_factory=dict,
    )

    # The name of the association document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The targets of the association.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # The name of the association that you want to update.
    association_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This parameter is provided for concurrency control purposes. You must
    # specify the latest association version in the service. If you want to
    # ensure that this request succeeds, either specify `$LATEST`, or omit this
    # parameter.
    association_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateAssociationResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "association_description",
                "AssociationDescription",
                autoboto.TypeInfo(AssociationDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description of the association that was updated.
    association_description: "AssociationDescription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateAssociationStatusRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "association_status",
                "AssociationStatus",
                autoboto.TypeInfo(AssociationStatus),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The association status.
    association_status: "AssociationStatus" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateAssociationStatusResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "association_description",
                "AssociationDescription",
                autoboto.TypeInfo(AssociationDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the association.
    association_description: "AssociationDescription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateDocumentDefaultVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of a custom document that you want to set as the default version.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version of a custom document that you want to set as the default
    # version.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateDocumentDefaultVersionResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(DocumentDefaultVersionDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description of a custom document that you want to set as the default
    # version.
    description: "DocumentDefaultVersionDescription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateDocumentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "content",
                "Content",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "document_format",
                "DocumentFormat",
                autoboto.TypeInfo(DocumentFormat),
            ),
            (
                "target_type",
                "TargetType",
                autoboto.TypeInfo(str),
            ),
        ]

    # The content in a document that you want to update.
    content: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the document that you want to update.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version of the document that you want to update.
    document_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specify the document format for the new document version. Systems Manager
    # supports JSON and YAML documents. JSON is the default format.
    document_format: "DocumentFormat" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specify a new target type for the document.
    target_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDocumentResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "document_description",
                "DocumentDescription",
                autoboto.TypeInfo(DocumentDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A description of the document that was updated.
    document_description: "DocumentDescription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateMaintenanceWindowRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                autoboto.TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(int),
            ),
            (
                "cutoff",
                "Cutoff",
                autoboto.TypeInfo(int),
            ),
            (
                "allow_unassociated_targets",
                "AllowUnassociatedTargets",
                autoboto.TypeInfo(bool),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "replace",
                "Replace",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the Maintenance Window to update.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the Maintenance Window.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional description for the update request.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The schedule of the Maintenance Window in the form of a cron or rate
    # expression.
    schedule: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The duration of the Maintenance Window in hours.
    duration: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of hours before the end of the Maintenance Window that Systems
    # Manager stops scheduling new tasks for execution.
    cutoff: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether targets must be registered with the Maintenance Window before tasks
    # can be defined for those targets.
    allow_unassociated_targets: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether the Maintenance Window is enabled.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If True, then all fields that are required by the CreateMaintenanceWindow
    # action are also required for this API request. Optional fields that are not
    # specified are set to null.
    replace: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateMaintenanceWindowResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                autoboto.TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(int),
            ),
            (
                "cutoff",
                "Cutoff",
                autoboto.TypeInfo(int),
            ),
            (
                "allow_unassociated_targets",
                "AllowUnassociatedTargets",
                autoboto.TypeInfo(bool),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the created Maintenance Window.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the Maintenance Window.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional description of the update.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The schedule of the Maintenance Window in the form of a cron or rate
    # expression.
    schedule: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The duration of the Maintenance Window in hours.
    duration: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of hours before the end of the Maintenance Window that Systems
    # Manager stops scheduling new tasks for execution.
    cutoff: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether targets must be registered with the Maintenance Window before tasks
    # can be defined for those targets.
    allow_unassociated_targets: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether the Maintenance Window is enabled.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateMaintenanceWindowTargetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "window_target_id",
                "WindowTargetId",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "owner_information",
                "OwnerInformation",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "replace",
                "Replace",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The Maintenance Window ID with which to modify the target.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The target ID to modify.
    window_target_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The targets to add or replace.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # User-provided value that will be included in any CloudWatch events raised
    # while running tasks for these targets in this Maintenance Window.
    owner_information: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A name for the update.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional description for the update.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If True, then all fields that are required by the
    # RegisterTargetWithMaintenanceWindow action are also required for this API
    # request. Optional fields that are not specified are set to null.
    replace: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateMaintenanceWindowTargetResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "window_target_id",
                "WindowTargetId",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "owner_information",
                "OwnerInformation",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Maintenance Window ID specified in the update request.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The target ID specified in the update request.
    window_target_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated targets.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # The updated owner.
    owner_information: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated description.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateMaintenanceWindowTaskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "window_task_id",
                "WindowTaskId",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "task_arn",
                "TaskArn",
                autoboto.TypeInfo(str),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "task_parameters",
                "TaskParameters",
                autoboto.TypeInfo(
                    typing.Dict[str,
                                MaintenanceWindowTaskParameterValueExpression]
                ),
            ),
            (
                "task_invocation_parameters",
                "TaskInvocationParameters",
                autoboto.TypeInfo(MaintenanceWindowTaskInvocationParameters),
            ),
            (
                "priority",
                "Priority",
                autoboto.TypeInfo(int),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                autoboto.TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                autoboto.TypeInfo(str),
            ),
            (
                "logging_info",
                "LoggingInfo",
                autoboto.TypeInfo(LoggingInfo),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "replace",
                "Replace",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The Maintenance Window ID that contains the task to modify.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The task ID to modify.
    window_task_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The targets (either instances or tags) to modify. Instances are specified
    # using Key=instanceids,Values=instanceID_1,instanceID_2. Tags are specified
    # using Key=tag_name,Values=tag_value.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # The task ARN to modify.
    task_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The IAM service role ARN to modify. The system assumes this role during
    # task execution.

    # If you do not specify a service role ARN, Systems Manager will use your
    # account's service-linked role for Systems Manager by default. If no
    # service-linked role for Systems Manager exists in your account, it will be
    # created when you run `RegisterTaskWithMaintenanceWindow` without specifying
    # a service role ARN.

    # For more information, see [Service-Linked Role Permissions for Systems
    # Manager](http://docs.aws.amazon.com/systems-manager/latest/userguide/using-
    # service-linked-roles.html#slr-permissions) and [Should I Use a Service-
    # Linked Role or a Custom Service Role to Run Maintenance Window Tasks?
    # ](http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-
    # maintenance-permissions.html#maintenance-window-tasks-service-role) in the
    # _AWS Systems Manager User Guide_.
    service_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameters to modify.

    # `TaskParameters` has been deprecated. To specify parameters to pass to a
    # task when it runs, instead use the `Parameters` option in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.

    # The map has the following format:

    # Key: string, between 1 and 255 characters

    # Value: an array of strings, each string is between 1 and 255 characters
    task_parameters: typing.Dict[
        str, "MaintenanceWindowTaskParameterValueExpression"
    ] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameters that the task should use during execution. Populate only the
    # fields that match the task type. All other fields should be empty.
    task_invocation_parameters: "MaintenanceWindowTaskInvocationParameters" = dataclasses.field(
        default_factory=dict,
    )

    # The new task priority to specify. The lower the number, the higher the
    # priority. Tasks that have the same priority are scheduled in parallel.
    priority: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The new `MaxConcurrency` value you want to specify. `MaxConcurrency` is the
    # number of targets that are allowed to run this task in parallel.
    max_concurrency: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The new `MaxErrors` value to specify. `MaxErrors` is the maximum number of
    # errors that are allowed before the task stops being scheduled.
    max_errors: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The new logging location in Amazon S3 to specify.

    # `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    # instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    logging_info: "LoggingInfo" = dataclasses.field(default_factory=dict, )

    # The new task name to specify.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The new task description to specify.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If True, then all fields that are required by the
    # RegisterTaskWithMaintenanceWndow action are also required for this API
    # request. Optional fields that are not specified are set to null.
    replace: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateMaintenanceWindowTaskResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
                autoboto.TypeInfo(str),
            ),
            (
                "window_task_id",
                "WindowTaskId",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(typing.List[Target]),
            ),
            (
                "task_arn",
                "TaskArn",
                autoboto.TypeInfo(str),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "task_parameters",
                "TaskParameters",
                autoboto.TypeInfo(
                    typing.Dict[str,
                                MaintenanceWindowTaskParameterValueExpression]
                ),
            ),
            (
                "task_invocation_parameters",
                "TaskInvocationParameters",
                autoboto.TypeInfo(MaintenanceWindowTaskInvocationParameters),
            ),
            (
                "priority",
                "Priority",
                autoboto.TypeInfo(int),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                autoboto.TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                autoboto.TypeInfo(str),
            ),
            (
                "logging_info",
                "LoggingInfo",
                autoboto.TypeInfo(LoggingInfo),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the Maintenance Window that was updated.
    window_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The task ID of the Maintenance Window that was updated.
    window_task_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated target values.
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # The updated task ARN value.
    task_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated service role ARN value.
    service_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated parameter values.

    # `TaskParameters` has been deprecated. To specify parameters to pass to a
    # task when it runs, instead use the `Parameters` option in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    task_parameters: typing.Dict[
        str, "MaintenanceWindowTaskParameterValueExpression"
    ] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated parameter values.
    task_invocation_parameters: "MaintenanceWindowTaskInvocationParameters" = dataclasses.field(
        default_factory=dict,
    )

    # The updated priority value.
    priority: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated MaxConcurrency value.
    max_concurrency: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated MaxErrors value.
    max_errors: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated logging information in Amazon S3.

    # `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    # instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    logging_info: "LoggingInfo" = dataclasses.field(default_factory=dict, )

    # The updated task name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated task description.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateManagedInstanceRoleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "iam_role",
                "IamRole",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the managed instance where you want to update the role.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The IAM role you want to assign or change.
    iam_role: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateManagedInstanceRoleResult(autoboto.OutputShapeBase):
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
class UpdatePatchBaselineRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "global_filters",
                "GlobalFilters",
                autoboto.TypeInfo(PatchFilterGroup),
            ),
            (
                "approval_rules",
                "ApprovalRules",
                autoboto.TypeInfo(PatchRuleGroup),
            ),
            (
                "approved_patches",
                "ApprovedPatches",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "approved_patches_compliance_level",
                "ApprovedPatchesComplianceLevel",
                autoboto.TypeInfo(PatchComplianceLevel),
            ),
            (
                "approved_patches_enable_non_security",
                "ApprovedPatchesEnableNonSecurity",
                autoboto.TypeInfo(bool),
            ),
            (
                "rejected_patches",
                "RejectedPatches",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "sources",
                "Sources",
                autoboto.TypeInfo(typing.List[PatchSource]),
            ),
            (
                "replace",
                "Replace",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the patch baseline to update.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the patch baseline.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A set of global filters used to exclude patches from the baseline.
    global_filters: "PatchFilterGroup" = dataclasses.field(
        default_factory=dict,
    )

    # A set of rules used to include patches in the baseline.
    approval_rules: "PatchRuleGroup" = dataclasses.field(default_factory=dict, )

    # A list of explicitly approved patches for the baseline.

    # For information about accepted formats for lists of approved patches and
    # rejected patches, see [Package Name Formats for Approved and Rejected Patch
    # Lists](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-
    # manager-approved-rejected-package-name-formats.html) in the _AWS Systems
    # Manager User Guide_.
    approved_patches: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Assigns a new compliance severity level to an existing patch baseline.
    approved_patches_compliance_level: "PatchComplianceLevel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the list of approved patches includes non-security
    # updates that should be applied to the instances. The default value is
    # 'false'. Applies to Linux instances only.
    approved_patches_enable_non_security: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of explicitly rejected patches for the baseline.

    # For information about accepted formats for lists of approved patches and
    # rejected patches, see [Package Name Formats for Approved and Rejected Patch
    # Lists](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-
    # manager-approved-rejected-package-name-formats.html) in the _AWS Systems
    # Manager User Guide_.
    rejected_patches: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A description of the patch baseline.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Information about the patches to use to update the instances, including
    # target operating systems and source repositories. Applies to Linux
    # instances only.
    sources: typing.List["PatchSource"] = dataclasses.field(
        default_factory=list,
    )

    # If True, then all fields that are required by the CreatePatchBaseline
    # action are also required for this API request. Optional fields that are not
    # specified are set to null.
    replace: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePatchBaselineResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "operating_system",
                "OperatingSystem",
                autoboto.TypeInfo(OperatingSystem),
            ),
            (
                "global_filters",
                "GlobalFilters",
                autoboto.TypeInfo(PatchFilterGroup),
            ),
            (
                "approval_rules",
                "ApprovalRules",
                autoboto.TypeInfo(PatchRuleGroup),
            ),
            (
                "approved_patches",
                "ApprovedPatches",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "approved_patches_compliance_level",
                "ApprovedPatchesComplianceLevel",
                autoboto.TypeInfo(PatchComplianceLevel),
            ),
            (
                "approved_patches_enable_non_security",
                "ApprovedPatchesEnableNonSecurity",
                autoboto.TypeInfo(bool),
            ),
            (
                "rejected_patches",
                "RejectedPatches",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "created_date",
                "CreatedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "modified_date",
                "ModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "sources",
                "Sources",
                autoboto.TypeInfo(typing.List[PatchSource]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the deleted patch baseline.
    baseline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the patch baseline.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The operating system rule used by the updated patch baseline.
    operating_system: "OperatingSystem" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A set of global filters used to exclude patches from the baseline.
    global_filters: "PatchFilterGroup" = dataclasses.field(
        default_factory=dict,
    )

    # A set of rules used to include patches in the baseline.
    approval_rules: "PatchRuleGroup" = dataclasses.field(default_factory=dict, )

    # A list of explicitly approved patches for the baseline.
    approved_patches: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The compliance severity level assigned to the patch baseline after the
    # update completed.
    approved_patches_compliance_level: "PatchComplianceLevel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the list of approved patches includes non-security
    # updates that should be applied to the instances. The default value is
    # 'false'. Applies to Linux instances only.
    approved_patches_enable_non_security: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of explicitly rejected patches for the baseline.
    rejected_patches: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The date when the patch baseline was created.
    created_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date when the patch baseline was last modified.
    modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A description of the Patch Baseline.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Information about the patches to use to update the instances, including
    # target operating systems and source repositories. Applies to Linux
    # instances only.
    sources: typing.List["PatchSource"] = dataclasses.field(
        default_factory=list,
    )
