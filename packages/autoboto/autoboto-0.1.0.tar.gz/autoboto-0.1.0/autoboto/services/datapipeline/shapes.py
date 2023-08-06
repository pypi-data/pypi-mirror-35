import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class ActivatePipelineInput(autoboto.ShapeBase):
    """
    Contains the parameters for ActivatePipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_values",
                "parameterValues",
                autoboto.TypeInfo(typing.List[ParameterValue]),
            ),
            (
                "start_timestamp",
                "startTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of parameter values to pass to the pipeline at activation.
    parameter_values: typing.List["ParameterValue"] = dataclasses.field(
        default_factory=list,
    )

    # The date and time to resume the pipeline. By default, the pipeline resumes
    # from the last completed execution.
    start_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ActivatePipelineOutput(autoboto.OutputShapeBase):
    """
    Contains the output of ActivatePipeline.
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
class AddTagsInput(autoboto.ShapeBase):
    """
    Contains the parameters for AddTags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tags to add, as key/value pairs.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class AddTagsOutput(autoboto.OutputShapeBase):
    """
    Contains the output of AddTags.
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
class CreatePipelineInput(autoboto.ShapeBase):
    """
    Contains the parameters for CreatePipeline.
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
                "unique_id",
                "uniqueId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name for the pipeline. You can use the same name for multiple pipelines
    # associated with your AWS account, because AWS Data Pipeline assigns each
    # pipeline a unique pipeline identifier.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A unique identifier. This identifier is not the same as the pipeline
    # identifier assigned by AWS Data Pipeline. You are responsible for defining
    # the format and ensuring the uniqueness of this identifier. You use this
    # parameter to ensure idempotency during repeated calls to `CreatePipeline`.
    # For example, if the first call to `CreatePipeline` does not succeed, you
    # can pass in the same unique identifier and pipeline name combination on a
    # subsequent call to `CreatePipeline`. `CreatePipeline` ensures that if a
    # pipeline already exists with the same name and unique identifier, a new
    # pipeline is not created. Instead, you'll receive the pipeline identifier
    # from the previous attempt. The uniqueness of the name and unique identifier
    # combination is scoped to the AWS account or IAM user credentials.
    unique_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description for the pipeline.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of tags to associate with the pipeline at creation. Tags let you
    # control access to pipelines. For more information, see [Controlling User
    # Access to
    # Pipelines](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-
    # control-access.html) in the _AWS Data Pipeline Developer Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreatePipelineOutput(autoboto.OutputShapeBase):
    """
    Contains the output of CreatePipeline.
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
                "pipeline_id",
                "pipelineId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID that AWS Data Pipeline assigns the newly created pipeline. For
    # example, `df-06372391ZG65EXAMPLE`.
    pipeline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeactivatePipelineInput(autoboto.ShapeBase):
    """
    Contains the parameters for DeactivatePipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                autoboto.TypeInfo(str),
            ),
            (
                "cancel_active",
                "cancelActive",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether to cancel any running objects. The default is true, which
    # sets the state of any running objects to `CANCELED`. If this value is
    # false, the pipeline is deactivated after all running objects finish.
    cancel_active: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeactivatePipelineOutput(autoboto.OutputShapeBase):
    """
    Contains the output of DeactivatePipeline.
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
class DeletePipelineInput(autoboto.ShapeBase):
    """
    Contains the parameters for DeletePipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeObjectsInput(autoboto.ShapeBase):
    """
    Contains the parameters for DescribeObjects.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                autoboto.TypeInfo(str),
            ),
            (
                "object_ids",
                "objectIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "evaluate_expressions",
                "evaluateExpressions",
                autoboto.TypeInfo(bool),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the pipeline that contains the object definitions.
    pipeline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The IDs of the pipeline objects that contain the definitions to be
    # described. You can pass as many as 25 identifiers in a single call to
    # `DescribeObjects`.
    object_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # Indicates whether any expressions in the object should be evaluated when
    # the object descriptions are returned.
    evaluate_expressions: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The starting point for the results to be returned. For the first call, this
    # value should be empty. As long as there are more results, continue to call
    # `DescribeObjects` with the marker value from the previous call to retrieve
    # the next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeObjectsOutput(autoboto.OutputShapeBase):
    """
    Contains the output of DescribeObjects.
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
                "pipeline_objects",
                "pipelineObjects",
                autoboto.TypeInfo(typing.List[PipelineObject]),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "has_more_results",
                "hasMoreResults",
                autoboto.TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of object definitions.
    pipeline_objects: typing.List["PipelineObject"] = dataclasses.field(
        default_factory=list,
    )

    # The starting point for the next page of results. To view the next page of
    # results, call `DescribeObjects` again with this marker value. If the value
    # is null, there are no more results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether there are more results to return.
    has_more_results: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribePipelinesInput(autoboto.ShapeBase):
    """
    Contains the parameters for DescribePipelines.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_ids",
                "pipelineIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The IDs of the pipelines to describe. You can pass as many as 25
    # identifiers in a single call. To obtain pipeline IDs, call ListPipelines.
    pipeline_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribePipelinesOutput(autoboto.OutputShapeBase):
    """
    Contains the output of DescribePipelines.
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
                "pipeline_description_list",
                "pipelineDescriptionList",
                autoboto.TypeInfo(typing.List[PipelineDescription]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of descriptions for the specified pipelines.
    pipeline_description_list: typing.List["PipelineDescription"
                                          ] = dataclasses.field(
                                              default_factory=list,
                                          )


@dataclasses.dataclass
class EvaluateExpressionInput(autoboto.ShapeBase):
    """
    Contains the parameters for EvaluateExpression.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                autoboto.TypeInfo(str),
            ),
            (
                "object_id",
                "objectId",
                autoboto.TypeInfo(str),
            ),
            (
                "expression",
                "expression",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the object.
    object_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The expression to evaluate.
    expression: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EvaluateExpressionOutput(autoboto.OutputShapeBase):
    """
    Contains the output of EvaluateExpression.
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
                "evaluated_expression",
                "evaluatedExpression",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The evaluated expression.
    evaluated_expression: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Field(autoboto.ShapeBase):
    """
    A key-value pair that describes a property of a pipeline object. The value is
    specified as either a string value (`StringValue`) or a reference to another
    object (`RefValue`) but not as both.
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
                "string_value",
                "stringValue",
                autoboto.TypeInfo(str),
            ),
            (
                "ref_value",
                "refValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The field identifier.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The field value, expressed as a String.
    string_value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The field value, expressed as the identifier of another object.
    ref_value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPipelineDefinitionInput(autoboto.ShapeBase):
    """
    Contains the parameters for GetPipelineDefinition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version of the pipeline definition to retrieve. Set this parameter to
    # `latest` (default) to use the last definition saved to the pipeline or
    # `active` to use the last definition that was activated.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPipelineDefinitionOutput(autoboto.OutputShapeBase):
    """
    Contains the output of GetPipelineDefinition.
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
                "pipeline_objects",
                "pipelineObjects",
                autoboto.TypeInfo(typing.List[PipelineObject]),
            ),
            (
                "parameter_objects",
                "parameterObjects",
                autoboto.TypeInfo(typing.List[ParameterObject]),
            ),
            (
                "parameter_values",
                "parameterValues",
                autoboto.TypeInfo(typing.List[ParameterValue]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The objects defined in the pipeline.
    pipeline_objects: typing.List["PipelineObject"] = dataclasses.field(
        default_factory=list,
    )

    # The parameter objects used in the pipeline definition.
    parameter_objects: typing.List["ParameterObject"] = dataclasses.field(
        default_factory=list,
    )

    # The parameter values used in the pipeline definition.
    parameter_values: typing.List["ParameterValue"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class InstanceIdentity(autoboto.ShapeBase):
    """
    Identity information for the EC2 instance that is hosting the task runner. You
    can get this value by calling a metadata URI from the EC2 instance. For more
    information, see [Instance
    Metadata](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-
    instancedata.html) in the _Amazon Elastic Compute Cloud User Guide._ Passing in
    this value proves that your task runner is running on an EC2 instance, and
    ensures the proper AWS Data Pipeline service charges are applied to your
    pipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document",
                "document",
                autoboto.TypeInfo(str),
            ),
            (
                "signature",
                "signature",
                autoboto.TypeInfo(str),
            ),
        ]

    # A description of an EC2 instance that is generated when the instance is
    # launched and exposed to the instance via the instance metadata service in
    # the form of a JSON representation of an object.
    document: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A signature which can be used to verify the accuracy and authenticity of
    # the information provided in the instance identity document.
    signature: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServiceError(autoboto.ShapeBase):
    """
    An internal service error occurred.
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

    # Description of the error message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRequestException(autoboto.ShapeBase):
    """
    The request was not valid. Verify that your request was properly formatted, that
    the signature was generated with the correct credentials, and that you haven't
    exceeded any of the service limits for your account.
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

    # Description of the error message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPipelinesInput(autoboto.ShapeBase):
    """
    Contains the parameters for ListPipelines.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The starting point for the results to be returned. For the first call, this
    # value should be empty. As long as there are more results, continue to call
    # `ListPipelines` with the marker value from the previous call to retrieve
    # the next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPipelinesOutput(autoboto.OutputShapeBase):
    """
    Contains the output of ListPipelines.
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
                "pipeline_id_list",
                "pipelineIdList",
                autoboto.TypeInfo(typing.List[PipelineIdName]),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "has_more_results",
                "hasMoreResults",
                autoboto.TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The pipeline identifiers. If you require additional information about the
    # pipelines, you can use these identifiers to call DescribePipelines and
    # GetPipelineDefinition.
    pipeline_id_list: typing.List["PipelineIdName"] = dataclasses.field(
        default_factory=list,
    )

    # The starting point for the next page of results. To view the next page of
    # results, call `ListPipelinesOutput` again with this marker value. If the
    # value is null, there are no more results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether there are more results that can be obtained by a
    # subsequent call.
    has_more_results: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Operator(autoboto.ShapeBase):
    """
    Contains a logical operation for comparing the value of a field with a specified
    value.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(OperatorType),
            ),
            (
                "values",
                "values",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The logical operation to be performed: equal (`EQ`), equal reference
    # (`REF_EQ`), less than or equal (`LE`), greater than or equal (`GE`), or
    # between (`BETWEEN`). Equal reference (`REF_EQ`) can be used only with
    # reference fields. The other comparison types can be used only with String
    # fields. The comparison types you can use apply only to certain object
    # fields, as detailed below.

    # The comparison operators EQ and REF_EQ act on the following fields:

    #   * name
    #   * @sphere
    #   * parent
    #   * @componentParent
    #   * @instanceParent
    #   * @status
    #   * @scheduledStartTime
    #   * @scheduledEndTime
    #   * @actualStartTime
    #   * @actualEndTime

    # The comparison operators `GE`, `LE`, and `BETWEEN` act on the following
    # fields:

    #   * @scheduledStartTime
    #   * @scheduledEndTime
    #   * @actualStartTime
    #   * @actualEndTime

    # Note that fields beginning with the at sign (@) are read-only and set by
    # the web service. When you name fields, you should choose names containing
    # only alpha-numeric values, as symbols may be reserved by AWS Data Pipeline.
    # User-defined fields that you add to a pipeline should prefix their name
    # with the string "my".
    type: "OperatorType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The value that the actual field value will be compared with.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


class OperatorType(Enum):
    EQ = "EQ"
    REF_EQ = "REF_EQ"
    LE = "LE"
    GE = "GE"
    BETWEEN = "BETWEEN"


@dataclasses.dataclass
class ParameterAttribute(autoboto.ShapeBase):
    """
    The attributes allowed or specified with a parameter object.
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
                "string_value",
                "stringValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The field identifier.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The field value, expressed as a String.
    string_value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ParameterObject(autoboto.ShapeBase):
    """
    Contains information about a parameter object.
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
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.List[ParameterAttribute]),
            ),
        ]

    # The ID of the parameter object.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The attributes of the parameter object.
    attributes: typing.List["ParameterAttribute"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ParameterValue(autoboto.ShapeBase):
    """
    A value or list of parameter values.
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
                "string_value",
                "stringValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the parameter value.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The field value, expressed as a String.
    string_value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PipelineDeletedException(autoboto.ShapeBase):
    """
    The specified pipeline has been deleted.
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

    # Description of the error message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PipelineDescription(autoboto.ShapeBase):
    """
    Contains pipeline metadata.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "fields",
                "fields",
                autoboto.TypeInfo(typing.List[Field]),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The pipeline identifier that was assigned by AWS Data Pipeline. This is a
    # string of the form `df-297EG78HU43EEXAMPLE`.
    pipeline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the pipeline.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of read-only fields that contain metadata about the pipeline:
    # @userId, @accountId, and @pipelineState.
    fields: typing.List["Field"] = dataclasses.field(default_factory=list, )

    # Description of the pipeline.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of tags to associated with a pipeline. Tags let you control access
    # to pipelines. For more information, see [Controlling User Access to
    # Pipelines](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-
    # control-access.html) in the _AWS Data Pipeline Developer Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class PipelineIdName(autoboto.ShapeBase):
    """
    Contains the name and identifier of a pipeline.
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
        ]

    # The ID of the pipeline that was assigned by AWS Data Pipeline. This is a
    # string of the form `df-297EG78HU43EEXAMPLE`.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the pipeline.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PipelineNotFoundException(autoboto.ShapeBase):
    """
    The specified pipeline was not found. Verify that you used the correct user and
    account identifiers.
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

    # Description of the error message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PipelineObject(autoboto.ShapeBase):
    """
    Contains information about a pipeline object. This can be a logical, physical,
    or physical attempt pipeline object. The complete set of components of a
    pipeline defines the pipeline.
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
                "fields",
                "fields",
                autoboto.TypeInfo(typing.List[Field]),
            ),
        ]

    # The ID of the object.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the object.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Key-value pairs that define the properties of the object.
    fields: typing.List["Field"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class PollForTaskInput(autoboto.ShapeBase):
    """
    Contains the parameters for PollForTask.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "worker_group",
                "workerGroup",
                autoboto.TypeInfo(str),
            ),
            (
                "hostname",
                "hostname",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_identity",
                "instanceIdentity",
                autoboto.TypeInfo(InstanceIdentity),
            ),
        ]

    # The type of task the task runner is configured to accept and process. The
    # worker group is set as a field on objects in the pipeline when they are
    # created. You can only specify a single value for `workerGroup` in the call
    # to `PollForTask`. There are no wildcard values permitted in `workerGroup`;
    # the string must be an exact, case-sensitive, match.
    worker_group: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The public DNS name of the calling task runner.
    hostname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Identity information for the EC2 instance that is hosting the task runner.
    # You can get this value from the instance using
    # `http://169.254.169.254/latest/meta-data/instance-id`. For more
    # information, see [Instance
    # Metadata](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-
    # instancedata.html) in the _Amazon Elastic Compute Cloud User Guide._
    # Passing in this value proves that your task runner is running on an EC2
    # instance, and ensures the proper AWS Data Pipeline service charges are
    # applied to your pipeline.
    instance_identity: "InstanceIdentity" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PollForTaskOutput(autoboto.OutputShapeBase):
    """
    Contains the output of PollForTask.
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
                "task_object",
                "taskObject",
                autoboto.TypeInfo(TaskObject),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The information needed to complete the task that is being assigned to the
    # task runner. One of the fields returned in this object is `taskId`, which
    # contains an identifier for the task being assigned. The calling task runner
    # uses `taskId` in subsequent calls to ReportTaskProgress and SetTaskStatus.
    task_object: "TaskObject" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PutPipelineDefinitionInput(autoboto.ShapeBase):
    """
    Contains the parameters for PutPipelineDefinition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                autoboto.TypeInfo(str),
            ),
            (
                "pipeline_objects",
                "pipelineObjects",
                autoboto.TypeInfo(typing.List[PipelineObject]),
            ),
            (
                "parameter_objects",
                "parameterObjects",
                autoboto.TypeInfo(typing.List[ParameterObject]),
            ),
            (
                "parameter_values",
                "parameterValues",
                autoboto.TypeInfo(typing.List[ParameterValue]),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The objects that define the pipeline. These objects overwrite the existing
    # pipeline definition.
    pipeline_objects: typing.List["PipelineObject"] = dataclasses.field(
        default_factory=list,
    )

    # The parameter objects used with the pipeline.
    parameter_objects: typing.List["ParameterObject"] = dataclasses.field(
        default_factory=list,
    )

    # The parameter values used with the pipeline.
    parameter_values: typing.List["ParameterValue"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class PutPipelineDefinitionOutput(autoboto.OutputShapeBase):
    """
    Contains the output of PutPipelineDefinition.
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
                "errored",
                "errored",
                autoboto.TypeInfo(bool),
            ),
            (
                "validation_errors",
                "validationErrors",
                autoboto.TypeInfo(typing.List[ValidationError]),
            ),
            (
                "validation_warnings",
                "validationWarnings",
                autoboto.TypeInfo(typing.List[ValidationWarning]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether there were validation errors, and the pipeline definition
    # is stored but cannot be activated until you correct the pipeline and call
    # `PutPipelineDefinition` to commit the corrected pipeline.
    errored: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The validation errors that are associated with the objects defined in
    # `pipelineObjects`.
    validation_errors: typing.List["ValidationError"] = dataclasses.field(
        default_factory=list,
    )

    # The validation warnings that are associated with the objects defined in
    # `pipelineObjects`.
    validation_warnings: typing.List["ValidationWarning"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Query(autoboto.ShapeBase):
    """
    Defines the query to run against an object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "selectors",
                "selectors",
                autoboto.TypeInfo(typing.List[Selector]),
            ),
        ]

    # List of selectors that define the query. An object must satisfy all of the
    # selectors to match the query.
    selectors: typing.List["Selector"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class QueryObjectsInput(autoboto.ShapeBase):
    """
    Contains the parameters for QueryObjects.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                autoboto.TypeInfo(str),
            ),
            (
                "sphere",
                "sphere",
                autoboto.TypeInfo(str),
            ),
            (
                "query",
                "query",
                autoboto.TypeInfo(Query),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether the query applies to components or instances. The
    # possible values are: `COMPONENT`, `INSTANCE`, and `ATTEMPT`.
    sphere: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The query that defines the objects to be returned. The `Query` object can
    # contain a maximum of ten selectors. The conditions in the query are limited
    # to top-level String fields in the object. These filters can be applied to
    # components, instances, and attempts.
    query: "Query" = dataclasses.field(default_factory=dict, )

    # The starting point for the results to be returned. For the first call, this
    # value should be empty. As long as there are more results, continue to call
    # `QueryObjects` with the marker value from the previous call to retrieve the
    # next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of object names that `QueryObjects` will return in a
    # single call. The default value is 100.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class QueryObjectsOutput(autoboto.OutputShapeBase):
    """
    Contains the output of QueryObjects.
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
                "ids",
                "ids",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "has_more_results",
                "hasMoreResults",
                autoboto.TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifiers that match the query selectors.
    ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The starting point for the next page of results. To view the next page of
    # results, call `QueryObjects` again with this marker value. If the value is
    # null, there are no more results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether there are more results that can be obtained by a
    # subsequent call.
    has_more_results: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveTagsInput(autoboto.ShapeBase):
    """
    Contains the parameters for RemoveTags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_keys",
                "tagKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The keys of the tags to remove.
    tag_keys: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class RemoveTagsOutput(autoboto.OutputShapeBase):
    """
    Contains the output of RemoveTags.
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
class ReportTaskProgressInput(autoboto.ShapeBase):
    """
    Contains the parameters for ReportTaskProgress.
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
                "fields",
                "fields",
                autoboto.TypeInfo(typing.List[Field]),
            ),
        ]

    # The ID of the task assigned to the task runner. This value is provided in
    # the response for PollForTask.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Key-value pairs that define the properties of the ReportTaskProgressInput
    # object.
    fields: typing.List["Field"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class ReportTaskProgressOutput(autoboto.OutputShapeBase):
    """
    Contains the output of ReportTaskProgress.
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
                "canceled",
                "canceled",
                autoboto.TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If true, the calling task runner should cancel processing of the task. The
    # task runner does not need to call SetTaskStatus for canceled tasks.
    canceled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReportTaskRunnerHeartbeatInput(autoboto.ShapeBase):
    """
    Contains the parameters for ReportTaskRunnerHeartbeat.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "taskrunner_id",
                "taskrunnerId",
                autoboto.TypeInfo(str),
            ),
            (
                "worker_group",
                "workerGroup",
                autoboto.TypeInfo(str),
            ),
            (
                "hostname",
                "hostname",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the task runner. This value should be unique across your AWS
    # account. In the case of AWS Data Pipeline Task Runner launched on a
    # resource managed by AWS Data Pipeline, the web service provides a unique
    # identifier when it launches the application. If you have written a custom
    # task runner, you should assign a unique identifier for the task runner.
    taskrunner_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of task the task runner is configured to accept and process. The
    # worker group is set as a field on objects in the pipeline when they are
    # created. You can only specify a single value for `workerGroup`. There are
    # no wildcard values permitted in `workerGroup`; the string must be an exact,
    # case-sensitive, match.
    worker_group: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The public DNS name of the task runner.
    hostname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReportTaskRunnerHeartbeatOutput(autoboto.OutputShapeBase):
    """
    Contains the output of ReportTaskRunnerHeartbeat.
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
                "terminate",
                "terminate",
                autoboto.TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the calling task runner should terminate.
    terminate: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Selector(autoboto.ShapeBase):
    """
    A comparision that is used to determine whether a query should return this
    object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_name",
                "fieldName",
                autoboto.TypeInfo(str),
            ),
            (
                "operator",
                "operator",
                autoboto.TypeInfo(Operator),
            ),
        ]

    # The name of the field that the operator will be applied to. The field name
    # is the "key" portion of the field definition in the pipeline definition
    # syntax that is used by the AWS Data Pipeline API. If the field is not set
    # on the object, the condition fails.
    field_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Contains a logical operation for comparing the value of a field with a
    # specified value.
    operator: "Operator" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class SetStatusInput(autoboto.ShapeBase):
    """
    Contains the parameters for SetStatus.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                autoboto.TypeInfo(str),
            ),
            (
                "object_ids",
                "objectIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the pipeline that contains the objects.
    pipeline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The IDs of the objects. The corresponding objects can be either physical or
    # components, but not a mix of both types.
    object_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The status to be set on all the objects specified in `objectIds`. For
    # components, use `PAUSE` or `RESUME`. For instances, use `TRY_CANCEL`,
    # `RERUN`, or `MARK_FINISHED`.
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetTaskStatusInput(autoboto.ShapeBase):
    """
    Contains the parameters for SetTaskStatus.
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
                autoboto.TypeInfo(TaskStatus),
            ),
            (
                "error_id",
                "errorId",
                autoboto.TypeInfo(str),
            ),
            (
                "error_message",
                "errorMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "error_stack_trace",
                "errorStackTrace",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the task assigned to the task runner. This value is provided in
    # the response for PollForTask.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If `FINISHED`, the task successfully completed. If `FAILED`, the task ended
    # unsuccessfully. Preconditions use false.
    task_status: "TaskStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If an error occurred during the task, this value specifies the error code.
    # This value is set on the physical attempt object. It is used to display
    # error information to the user. It should not start with string "Service_"
    # which is reserved by the system.
    error_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If an error occurred during the task, this value specifies a text
    # description of the error. This value is set on the physical attempt object.
    # It is used to display error information to the user. The web service does
    # not parse this value.
    error_message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If an error occurred during the task, this value specifies the stack trace
    # associated with the error. This value is set on the physical attempt
    # object. It is used to display error information to the user. The web
    # service does not parse this value.
    error_stack_trace: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetTaskStatusOutput(autoboto.OutputShapeBase):
    """
    Contains the output of SetTaskStatus.
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
class Tag(autoboto.ShapeBase):
    """
    Tags are key/value pairs defined by a user and associated with a pipeline to
    control access. AWS Data Pipeline allows you to associate ten tags per pipeline.
    For more information, see [Controlling User Access to
    Pipelines](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-
    control-access.html) in the _AWS Data Pipeline Developer Guide_.
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

    # The key name of a tag defined by a user. For more information, see
    # [Controlling User Access to
    # Pipelines](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-
    # control-access.html) in the _AWS Data Pipeline Developer Guide_.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The optional value portion of a tag defined by a user. For more
    # information, see [Controlling User Access to
    # Pipelines](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-
    # control-access.html) in the _AWS Data Pipeline Developer Guide_.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TaskNotFoundException(autoboto.ShapeBase):
    """
    The specified task was not found.
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

    # Description of the error message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TaskObject(autoboto.ShapeBase):
    """
    Contains information about a pipeline task that is assigned to a task runner.
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
                "pipeline_id",
                "pipelineId",
                autoboto.TypeInfo(str),
            ),
            (
                "attempt_id",
                "attemptId",
                autoboto.TypeInfo(str),
            ),
            (
                "objects",
                "objects",
                autoboto.TypeInfo(typing.Dict[str, PipelineObject]),
            ),
        ]

    # An internal identifier for the task. This ID is passed to the SetTaskStatus
    # and ReportTaskProgress actions.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the pipeline that provided the task.
    pipeline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the pipeline task attempt object. AWS Data Pipeline uses this
    # value to track how many times a task is attempted.
    attempt_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Connection information for the location where the task runner will publish
    # the output of the task.
    objects: typing.Dict[str, "PipelineObject"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class TaskStatus(Enum):
    FINISHED = "FINISHED"
    FAILED = "FAILED"
    FALSE = "FALSE"


@dataclasses.dataclass
class ValidatePipelineDefinitionInput(autoboto.ShapeBase):
    """
    Contains the parameters for ValidatePipelineDefinition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                autoboto.TypeInfo(str),
            ),
            (
                "pipeline_objects",
                "pipelineObjects",
                autoboto.TypeInfo(typing.List[PipelineObject]),
            ),
            (
                "parameter_objects",
                "parameterObjects",
                autoboto.TypeInfo(typing.List[ParameterObject]),
            ),
            (
                "parameter_values",
                "parameterValues",
                autoboto.TypeInfo(typing.List[ParameterValue]),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The objects that define the pipeline changes to validate against the
    # pipeline.
    pipeline_objects: typing.List["PipelineObject"] = dataclasses.field(
        default_factory=list,
    )

    # The parameter objects used with the pipeline.
    parameter_objects: typing.List["ParameterObject"] = dataclasses.field(
        default_factory=list,
    )

    # The parameter values used with the pipeline.
    parameter_values: typing.List["ParameterValue"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ValidatePipelineDefinitionOutput(autoboto.OutputShapeBase):
    """
    Contains the output of ValidatePipelineDefinition.
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
                "errored",
                "errored",
                autoboto.TypeInfo(bool),
            ),
            (
                "validation_errors",
                "validationErrors",
                autoboto.TypeInfo(typing.List[ValidationError]),
            ),
            (
                "validation_warnings",
                "validationWarnings",
                autoboto.TypeInfo(typing.List[ValidationWarning]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether there were validation errors.
    errored: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Any validation errors that were found.
    validation_errors: typing.List["ValidationError"] = dataclasses.field(
        default_factory=list,
    )

    # Any validation warnings that were found.
    validation_warnings: typing.List["ValidationWarning"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ValidationError(autoboto.ShapeBase):
    """
    Defines a validation error. Validation errors prevent pipeline activation. The
    set of validation errors that can be returned are defined by AWS Data Pipeline.
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
                "errors",
                "errors",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The identifier of the object that contains the validation error.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A description of the validation error.
    errors: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class ValidationWarning(autoboto.ShapeBase):
    """
    Defines a validation warning. Validation warnings do not prevent pipeline
    activation. The set of validation warnings that can be returned are defined by
    AWS Data Pipeline.
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
                "warnings",
                "warnings",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The identifier of the object that contains the validation warning.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A description of the validation warning.
    warnings: typing.List[str] = dataclasses.field(default_factory=list, )
