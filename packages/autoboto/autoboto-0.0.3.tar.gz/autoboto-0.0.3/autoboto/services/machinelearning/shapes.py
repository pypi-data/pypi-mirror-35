import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AddTagsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(TaggableResourceType),
            ),
        ]

    # The key-value pairs to use to create tags. If you specify a key without
    # specifying a value, Amazon ML creates a tag with the specified key and a
    # value of null.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # The ID of the ML object to tag. For example, `exampleModelId`.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of the ML object to tag.
    resource_type: "TaggableResourceType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AddTagsOutput(autoboto.ShapeBase):
    """
    Amazon ML returns the following elements.
    """

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
                autoboto.TypeInfo(TaggableResourceType),
            ),
        ]

    # The ID of the ML object that was tagged.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of the ML object that was tagged.
    resource_type: "TaggableResourceType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class Algorithm(Enum):
    """
    The function used to train an `MLModel`. Training choices supported by Amazon ML
    include the following:

      * `SGD` \- Stochastic Gradient Descent.
      * `RandomForest` \- Random forest of decision trees.
    """
    sgd = "sgd"


@dataclasses.dataclass
class BatchPrediction(autoboto.ShapeBase):
    """
    Represents the output of a `GetBatchPrediction` operation.

    The content consists of the detailed metadata, the status, and the data file
    information of a `Batch Prediction`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "batch_prediction_id",
                "BatchPredictionId",
                autoboto.TypeInfo(str),
            ),
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
            (
                "batch_prediction_data_source_id",
                "BatchPredictionDataSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "input_data_location_s3",
                "InputDataLocationS3",
                autoboto.TypeInfo(str),
            ),
            (
                "created_by_iam_user",
                "CreatedByIamUser",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_at",
                "LastUpdatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(EntityStatus),
            ),
            (
                "output_uri",
                "OutputUri",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "compute_time",
                "ComputeTime",
                autoboto.TypeInfo(int),
            ),
            (
                "finished_at",
                "FinishedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "started_at",
                "StartedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "total_record_count",
                "TotalRecordCount",
                autoboto.TypeInfo(int),
            ),
            (
                "invalid_record_count",
                "InvalidRecordCount",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID assigned to the `BatchPrediction` at creation. This value should be
    # identical to the value of the `BatchPredictionID` in the request.
    batch_prediction_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `MLModel` that generated predictions for the
    # `BatchPrediction` request.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the `DataSource` that points to the group of observations to
    # predict.
    batch_prediction_data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The location of the data file or directory in Amazon Simple Storage Service
    # (Amazon S3).
    input_data_location_s3: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS user account that invoked the `BatchPrediction`. The account type
    # can be either an AWS root account or an AWS Identity and Access Management
    # (IAM) user account.
    created_by_iam_user: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time that the `BatchPrediction` was created. The time is expressed in
    # epoch time.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time of the most recent edit to the `BatchPrediction`. The time is
    # expressed in epoch time.
    last_updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A user-supplied name or description of the `BatchPrediction`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the `BatchPrediction`. This element can have one of the
    # following values:

    #   * `PENDING` \- Amazon Machine Learning (Amazon ML) submitted a request to generate predictions for a batch of observations.
    #   * `INPROGRESS` \- The process is underway.
    #   * `FAILED` \- The request to perform a batch prediction did not run to completion. It is not usable.
    #   * `COMPLETED` \- The batch prediction process completed successfully.
    #   * `DELETED` \- The `BatchPrediction` is marked as deleted. It is not usable.
    status: "EntityStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The location of an Amazon S3 bucket or directory to receive the operation
    # results. The following substrings are not allowed in the `s3 key` portion
    # of the `outputURI` field: ':', '//', '/./', '/../'.
    output_uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A description of the most recent details about processing the batch
    # prediction request.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Long integer type that is a 64-bit signed number.
    compute_time: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A timestamp represented in epoch time.
    finished_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A timestamp represented in epoch time.
    started_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Long integer type that is a 64-bit signed number.
    total_record_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Long integer type that is a 64-bit signed number.
    invalid_record_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class BatchPredictionFilterVariable(Enum):
    """
    A list of the variables to use in searching or filtering `BatchPrediction`.

      * `CreatedAt` \- Sets the search criteria to `BatchPrediction` creation date.
      * `Status` \- Sets the search criteria to `BatchPrediction` status.
      * `Name` \- Sets the search criteria to the contents of `BatchPrediction` **** `Name`.
      * `IAMUser` \- Sets the search criteria to the user account that invoked the `BatchPrediction` creation.
      * `MLModelId` \- Sets the search criteria to the `MLModel` used in the `BatchPrediction`.
      * `DataSourceId` \- Sets the search criteria to the `DataSource` used in the `BatchPrediction`.
      * `DataURI` \- Sets the search criteria to the data file(s) used in the `BatchPrediction`. The URL can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
    """
    CreatedAt = "CreatedAt"
    LastUpdatedAt = "LastUpdatedAt"
    Status = "Status"
    Name = "Name"
    IAMUser = "IAMUser"
    MLModelId = "MLModelId"
    DataSourceId = "DataSourceId"
    DataURI = "DataURI"


@dataclasses.dataclass
class CreateBatchPredictionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "batch_prediction_id",
                "BatchPredictionId",
                autoboto.TypeInfo(str),
            ),
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
            (
                "batch_prediction_data_source_id",
                "BatchPredictionDataSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "output_uri",
                "OutputUri",
                autoboto.TypeInfo(str),
            ),
            (
                "batch_prediction_name",
                "BatchPredictionName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `BatchPrediction`.
    batch_prediction_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `MLModel` that will generate predictions for the group of
    # observations.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the `DataSource` that points to the group of observations to
    # predict.
    batch_prediction_data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The location of an Amazon Simple Storage Service (Amazon S3) bucket or
    # directory to store the batch prediction results. The following substrings
    # are not allowed in the `s3 key` portion of the `outputURI` field: ':',
    # '//', '/./', '/../'.

    # Amazon ML needs permissions to store and retrieve the logs on your behalf.
    # For information about how to set permissions, see the [Amazon Machine
    # Learning Developer Guide](http://docs.aws.amazon.com/machine-
    # learning/latest/dg).
    output_uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A user-supplied name or description of the `BatchPrediction`.
    # `BatchPredictionName` can only use the UTF-8 character set.
    batch_prediction_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateBatchPredictionOutput(autoboto.ShapeBase):
    """
    Represents the output of a `CreateBatchPrediction` operation, and is an
    acknowledgement that Amazon ML received the request.

    The `CreateBatchPrediction` operation is asynchronous. You can poll for status
    updates by using the `>GetBatchPrediction` operation and checking the `Status`
    parameter of the result.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "batch_prediction_id",
                "BatchPredictionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `BatchPrediction`. This
    # value is identical to the value of the `BatchPredictionId` in the request.
    batch_prediction_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateDataSourceFromRDSInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source_id",
                "DataSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "rds_data",
                "RDSData",
                autoboto.TypeInfo(RDSDataSpec),
            ),
            (
                "role_arn",
                "RoleARN",
                autoboto.TypeInfo(str),
            ),
            (
                "data_source_name",
                "DataSourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "compute_statistics",
                "ComputeStatistics",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `DataSource`. Typically, an
    # Amazon Resource Number (ARN) becomes the ID for a `DataSource`.
    data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The data specification of an Amazon RDS `DataSource`:

    #   * DatabaseInformation -
    #     * `DatabaseName` \- The name of the Amazon RDS database.
    #     * `InstanceIdentifier ` \- A unique identifier for the Amazon RDS database instance.

    #   * DatabaseCredentials - AWS Identity and Access Management (IAM) credentials that are used to connect to the Amazon RDS database.

    #   * ResourceRole - A role (DataPipelineDefaultResourceRole) assumed by an EC2 instance to carry out the copy task from Amazon RDS to Amazon Simple Storage Service (Amazon S3). For more information, see [Role templates](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html) for data pipelines.

    #   * ServiceRole - A role (DataPipelineDefaultRole) assumed by the AWS Data Pipeline service to monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see [Role templates](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html) for data pipelines.

    #   * SecurityInfo - The security information to use to access an RDS DB instance. You need to set up appropriate ingress rules for the security entity IDs provided to allow access to the Amazon RDS instance. Specify a [`SubnetId`, `SecurityGroupIds`] pair for a VPC-based RDS DB instance.

    #   * SelectSqlQuery - A query that is used to retrieve the observation data for the `Datasource`.

    #   * S3StagingLocation - The Amazon S3 location for staging Amazon RDS data. The data retrieved from Amazon RDS using `SelectSqlQuery` is stored in this location.

    #   * DataSchemaUri - The Amazon S3 location of the `DataSchema`.

    #   * DataSchema - A JSON string representing the schema. This is not required if `DataSchemaUri` is specified.

    #   * DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the `Datasource`.

    # Sample - ` "{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"`
    rds_data: "RDSDataSpec" = dataclasses.field(default_factory=dict, )

    # The role that Amazon ML assumes on behalf of the user to create and
    # activate a data pipeline in the user's account and copy data using the
    # `SelectSqlQuery` query from Amazon RDS to Amazon S3.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A user-supplied name or description of the `DataSource`.
    data_source_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The compute statistics for a `DataSource`. The statistics are generated
    # from the observation data referenced by a `DataSource`. Amazon ML uses the
    # statistics internally during `MLModel` training. This parameter must be set
    # to `true` if the ``DataSource`` needs to be used for `MLModel` training.
    compute_statistics: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateDataSourceFromRDSOutput(autoboto.ShapeBase):
    """
    Represents the output of a `CreateDataSourceFromRDS` operation, and is an
    acknowledgement that Amazon ML received the request.

    The `CreateDataSourceFromRDS`> operation is asynchronous. You can poll for
    updates by using the `GetBatchPrediction` operation and checking the `Status`
    parameter. You can inspect the `Message` when `Status` shows up as `FAILED`. You
    can also check the progress of the copy operation by going to the `DataPipeline`
    console and looking up the pipeline using the `pipelineId ` from the describe
    call.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source_id",
                "DataSourceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-supplied ID that uniquely identifies the datasource. This value
    # should be identical to the value of the `DataSourceID` in the request.
    data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateDataSourceFromRedshiftInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source_id",
                "DataSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "data_spec",
                "DataSpec",
                autoboto.TypeInfo(RedshiftDataSpec),
            ),
            (
                "role_arn",
                "RoleARN",
                autoboto.TypeInfo(str),
            ),
            (
                "data_source_name",
                "DataSourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "compute_statistics",
                "ComputeStatistics",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `DataSource`.
    data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The data specification of an Amazon Redshift `DataSource`:

    #   * DatabaseInformation -
    #     * `DatabaseName` \- The name of the Amazon Redshift database.
    #     * ` ClusterIdentifier` \- The unique ID for the Amazon Redshift cluster.

    #   * DatabaseCredentials - The AWS Identity and Access Management (IAM) credentials that are used to connect to the Amazon Redshift database.

    #   * SelectSqlQuery - The query that is used to retrieve the observation data for the `Datasource`.

    #   * S3StagingLocation - The Amazon Simple Storage Service (Amazon S3) location for staging Amazon Redshift data. The data retrieved from Amazon Redshift using the `SelectSqlQuery` query is stored in this location.

    #   * DataSchemaUri - The Amazon S3 location of the `DataSchema`.

    #   * DataSchema - A JSON string representing the schema. This is not required if `DataSchemaUri` is specified.

    #   * DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the `DataSource`.

    # Sample - ` "{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"`
    data_spec: "RedshiftDataSpec" = dataclasses.field(default_factory=dict, )

    # A fully specified role Amazon Resource Name (ARN). Amazon ML assumes the
    # role on behalf of the user to create the following:

    #   * A security group to allow Amazon ML to execute the `SelectSqlQuery` query on an Amazon Redshift cluster

    #   * An Amazon S3 bucket policy to grant Amazon ML read/write permissions on the `S3StagingLocation`
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A user-supplied name or description of the `DataSource`.
    data_source_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The compute statistics for a `DataSource`. The statistics are generated
    # from the observation data referenced by a `DataSource`. Amazon ML uses the
    # statistics internally during `MLModel` training. This parameter must be set
    # to `true` if the `DataSource` needs to be used for `MLModel` training.
    compute_statistics: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateDataSourceFromRedshiftOutput(autoboto.ShapeBase):
    """
    Represents the output of a `CreateDataSourceFromRedshift` operation, and is an
    acknowledgement that Amazon ML received the request.

    The `CreateDataSourceFromRedshift` operation is asynchronous. You can poll for
    updates by using the `GetBatchPrediction` operation and checking the `Status`
    parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source_id",
                "DataSourceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-supplied ID that uniquely identifies the datasource. This value
    # should be identical to the value of the `DataSourceID` in the request.
    data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateDataSourceFromS3Input(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source_id",
                "DataSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "data_spec",
                "DataSpec",
                autoboto.TypeInfo(S3DataSpec),
            ),
            (
                "data_source_name",
                "DataSourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "compute_statistics",
                "ComputeStatistics",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A user-supplied identifier that uniquely identifies the `DataSource`.
    data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The data specification of a `DataSource`:

    #   * DataLocationS3 - The Amazon S3 location of the observation data.

    #   * DataSchemaLocationS3 - The Amazon S3 location of the `DataSchema`.

    #   * DataSchema - A JSON string representing the schema. This is not required if `DataSchemaUri` is specified.

    #   * DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the `Datasource`.

    # Sample - ` "{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"`
    data_spec: "S3DataSpec" = dataclasses.field(default_factory=dict, )

    # A user-supplied name or description of the `DataSource`.
    data_source_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The compute statistics for a `DataSource`. The statistics are generated
    # from the observation data referenced by a `DataSource`. Amazon ML uses the
    # statistics internally during `MLModel` training. This parameter must be set
    # to `true` if the ``DataSource`` needs to be used for `MLModel` training.
    compute_statistics: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateDataSourceFromS3Output(autoboto.ShapeBase):
    """
    Represents the output of a `CreateDataSourceFromS3` operation, and is an
    acknowledgement that Amazon ML received the request.

    The `CreateDataSourceFromS3` operation is asynchronous. You can poll for updates
    by using the `GetBatchPrediction` operation and checking the `Status` parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source_id",
                "DataSourceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `DataSource`. This value
    # should be identical to the value of the `DataSourceID` in the request.
    data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateEvaluationInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "evaluation_id",
                "EvaluationId",
                autoboto.TypeInfo(str),
            ),
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
            (
                "evaluation_data_source_id",
                "EvaluationDataSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "evaluation_name",
                "EvaluationName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `Evaluation`.
    evaluation_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `MLModel` to evaluate.

    # The schema used in creating the `MLModel` must match the schema of the
    # `DataSource` used in the `Evaluation`.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the `DataSource` for the evaluation. The schema of the
    # `DataSource` must match the schema used to create the `MLModel`.
    evaluation_data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A user-supplied name or description of the `Evaluation`.
    evaluation_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateEvaluationOutput(autoboto.ShapeBase):
    """
    Represents the output of a `CreateEvaluation` operation, and is an
    acknowledgement that Amazon ML received the request.

    `CreateEvaluation` operation is asynchronous. You can poll for status updates by
    using the `GetEvcaluation` operation and checking the `Status` parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "evaluation_id",
                "EvaluationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user-supplied ID that uniquely identifies the `Evaluation`. This value
    # should be identical to the value of the `EvaluationId` in the request.
    evaluation_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateMLModelInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
            (
                "ml_model_type",
                "MLModelType",
                autoboto.TypeInfo(MLModelType),
            ),
            (
                "training_data_source_id",
                "TrainingDataSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "ml_model_name",
                "MLModelName",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "recipe",
                "Recipe",
                autoboto.TypeInfo(str),
            ),
            (
                "recipe_uri",
                "RecipeUri",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `MLModel`.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The category of supervised learning that this `MLModel` will address.
    # Choose from the following types:

    #   * Choose `REGRESSION` if the `MLModel` will be used to predict a numeric value.
    #   * Choose `BINARY` if the `MLModel` result has two possible values.
    #   * Choose `MULTICLASS` if the `MLModel` result has a limited number of values.

    # For more information, see the [Amazon Machine Learning Developer
    # Guide](http://docs.aws.amazon.com/machine-learning/latest/dg).
    ml_model_type: "MLModelType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The `DataSource` that points to the training data.
    training_data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A user-supplied name or description of the `MLModel`.
    ml_model_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of the training parameters in the `MLModel`. The list is implemented
    # as a map of key-value pairs.

    # The following is the current set of training parameters:

    #   * `sgd.maxMLModelSizeInBytes` \- The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance.

    # The value is an integer that ranges from `100000` to `2147483648`. The
    # default value is `33554432`.

    #   * `sgd.maxPasses` \- The number of times that the training process traverses the observations to build the `MLModel`. The value is an integer that ranges from `1` to `10000`. The default value is `10`.

    #   * `sgd.shuffleType` \- Whether Amazon ML shuffles the training data. Shuffling the data improves a model's ability to find the optimal solution for a variety of data types. The valid values are `auto` and `none`. The default value is `none`. We strongly recommend that you shuffle your data.

    #   * `sgd.l1RegularizationAmount` \- The coefficient regularization L1 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to zero, resulting in a sparse feature set. If you use this parameter, start by specifying a small value, such as `1.0E-08`.

    # The value is a double that ranges from `0` to `MAX_DOUBLE`. The default is
    # to not use L1 normalization. This parameter can't be used when `L2` is
    # specified. Use this parameter sparingly.

    #   * `sgd.l2RegularizationAmount` \- The coefficient regularization L2 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as `1.0E-08`.

    # The value is a double that ranges from `0` to `MAX_DOUBLE`. The default is
    # to not use L2 normalization. This parameter can't be used when `L1` is
    # specified. Use this parameter sparingly.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The data recipe for creating the `MLModel`. You must specify either the
    # recipe or its URI. If you don't specify a recipe or its URI, Amazon ML
    # creates a default.
    recipe: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Simple Storage Service (Amazon S3) location and file name that
    # contains the `MLModel` recipe. You must specify either the recipe or its
    # URI. If you don't specify a recipe or its URI, Amazon ML creates a default.
    recipe_uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateMLModelOutput(autoboto.ShapeBase):
    """
    Represents the output of a `CreateMLModel` operation, and is an acknowledgement
    that Amazon ML received the request.

    The `CreateMLModel` operation is asynchronous. You can poll for status updates
    by using the `GetMLModel` operation and checking the `Status` parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `MLModel`. This value
    # should be identical to the value of the `MLModelId` in the request.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateRealtimeEndpointInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID assigned to the `MLModel` during creation.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateRealtimeEndpointOutput(autoboto.ShapeBase):
    """
    Represents the output of an `CreateRealtimeEndpoint` operation.

    The result contains the `MLModelId` and the endpoint information for the
    `MLModel`.

    The endpoint information includes the URI of the `MLModel`; that is, the
    location to send online prediction requests for the specified `MLModel`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
            (
                "realtime_endpoint_info",
                "RealtimeEndpointInfo",
                autoboto.TypeInfo(RealtimeEndpointInfo),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `MLModel`. This value
    # should be identical to the value of the `MLModelId` in the request.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The endpoint information of the `MLModel`
    realtime_endpoint_info: "RealtimeEndpointInfo" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DataSource(autoboto.ShapeBase):
    """
    Represents the output of the `GetDataSource` operation.

    The content consists of the detailed metadata and data file information and the
    current status of the `DataSource`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source_id",
                "DataSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "data_location_s3",
                "DataLocationS3",
                autoboto.TypeInfo(str),
            ),
            (
                "data_rearrangement",
                "DataRearrangement",
                autoboto.TypeInfo(str),
            ),
            (
                "created_by_iam_user",
                "CreatedByIamUser",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_at",
                "LastUpdatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "data_size_in_bytes",
                "DataSizeInBytes",
                autoboto.TypeInfo(int),
            ),
            (
                "number_of_files",
                "NumberOfFiles",
                autoboto.TypeInfo(int),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(EntityStatus),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "redshift_metadata",
                "RedshiftMetadata",
                autoboto.TypeInfo(RedshiftMetadata),
            ),
            (
                "rds_metadata",
                "RDSMetadata",
                autoboto.TypeInfo(RDSMetadata),
            ),
            (
                "role_arn",
                "RoleARN",
                autoboto.TypeInfo(str),
            ),
            (
                "compute_statistics",
                "ComputeStatistics",
                autoboto.TypeInfo(bool),
            ),
            (
                "compute_time",
                "ComputeTime",
                autoboto.TypeInfo(int),
            ),
            (
                "finished_at",
                "FinishedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "started_at",
                "StartedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ID that is assigned to the `DataSource` during creation.
    data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The location and name of the data in Amazon Simple Storage Service (Amazon
    # S3) that is used by a `DataSource`.
    data_location_s3: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A JSON string that represents the splitting and rearrangement requirement
    # used when this `DataSource` was created.
    data_rearrangement: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS user account from which the `DataSource` was created. The account
    # type can be either an AWS root account or an AWS Identity and Access
    # Management (IAM) user account.
    created_by_iam_user: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time that the `DataSource` was created. The time is expressed in epoch
    # time.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time of the most recent edit to the `BatchPrediction`. The time is
    # expressed in epoch time.
    last_updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The total number of observations contained in the data files that the
    # `DataSource` references.
    data_size_in_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of data files referenced by the `DataSource`.
    number_of_files: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A user-supplied name or description of the `DataSource`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The current status of the `DataSource`. This element can have one of the
    # following values:

    #   * PENDING - Amazon Machine Learning (Amazon ML) submitted a request to create a `DataSource`.
    #   * INPROGRESS - The creation process is underway.
    #   * FAILED - The request to create a `DataSource` did not run to completion. It is not usable.
    #   * COMPLETED - The creation process completed successfully.
    #   * DELETED - The `DataSource` is marked as deleted. It is not usable.
    status: "EntityStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the most recent details about creating the `DataSource`.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Describes the `DataSource` details specific to Amazon Redshift.
    redshift_metadata: "RedshiftMetadata" = dataclasses.field(
        default_factory=dict,
    )

    # The datasource details that are specific to Amazon RDS.
    rds_metadata: "RDSMetadata" = dataclasses.field(default_factory=dict, )

    # The Amazon Resource Name (ARN) of an [AWS IAM
    # Role](http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-
    # toplevel.html#roles-about-termsandconcepts), such as the following:
    # arn:aws:iam::account:role/rolename.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The parameter is `true` if statistics need to be generated from the
    # observation data.
    compute_statistics: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Long integer type that is a 64-bit signed number.
    compute_time: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A timestamp represented in epoch time.
    finished_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A timestamp represented in epoch time.
    started_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class DataSourceFilterVariable(Enum):
    """
    A list of the variables to use in searching or filtering `DataSource`.

      * `CreatedAt` \- Sets the search criteria to `DataSource` creation date.
      * `Status` \- Sets the search criteria to `DataSource` status.
      * `Name` \- Sets the search criteria to the contents of `DataSource` **** `Name`.
      * `DataUri` \- Sets the search criteria to the URI of data files used to create the `DataSource`. The URI can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
      * `IAMUser` \- Sets the search criteria to the user account that invoked the `DataSource` creation.

    Note

    The variable names should match the variable names in the `DataSource`.
    """
    CreatedAt = "CreatedAt"
    LastUpdatedAt = "LastUpdatedAt"
    Status = "Status"
    Name = "Name"
    DataLocationS3 = "DataLocationS3"
    IAMUser = "IAMUser"


@dataclasses.dataclass
class DeleteBatchPredictionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "batch_prediction_id",
                "BatchPredictionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `BatchPrediction`.
    batch_prediction_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteBatchPredictionOutput(autoboto.ShapeBase):
    """
    Represents the output of a `DeleteBatchPrediction` operation.

    You can use the `GetBatchPrediction` operation and check the value of the
    `Status` parameter to see whether a `BatchPrediction` is marked as `DELETED`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "batch_prediction_id",
                "BatchPredictionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `BatchPrediction`. This
    # value should be identical to the value of the `BatchPredictionID` in the
    # request.
    batch_prediction_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteDataSourceInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source_id",
                "DataSourceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `DataSource`.
    data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteDataSourceOutput(autoboto.ShapeBase):
    """
    Represents the output of a `DeleteDataSource` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source_id",
                "DataSourceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `DataSource`. This value
    # should be identical to the value of the `DataSourceID` in the request.
    data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteEvaluationInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "evaluation_id",
                "EvaluationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `Evaluation` to delete.
    evaluation_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteEvaluationOutput(autoboto.ShapeBase):
    """
    Represents the output of a `DeleteEvaluation` operation. The output indicates
    that Amazon Machine Learning (Amazon ML) received the request.

    You can use the `GetEvaluation` operation and check the value of the `Status`
    parameter to see whether an `Evaluation` is marked as `DELETED`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "evaluation_id",
                "EvaluationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `Evaluation`. This value
    # should be identical to the value of the `EvaluationId` in the request.
    evaluation_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteMLModelInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `MLModel`.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteMLModelOutput(autoboto.ShapeBase):
    """
    Represents the output of a `DeleteMLModel` operation.

    You can use the `GetMLModel` operation and check the value of the `Status`
    parameter to see whether an `MLModel` is marked as `DELETED`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `MLModel`. This value
    # should be identical to the value of the `MLModelID` in the request.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteRealtimeEndpointInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID assigned to the `MLModel` during creation.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteRealtimeEndpointOutput(autoboto.ShapeBase):
    """
    Represents the output of an `DeleteRealtimeEndpoint` operation.

    The result contains the `MLModelId` and the endpoint information for the
    `MLModel`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
            (
                "realtime_endpoint_info",
                "RealtimeEndpointInfo",
                autoboto.TypeInfo(RealtimeEndpointInfo),
            ),
        ]

    # A user-supplied ID that uniquely identifies the `MLModel`. This value
    # should be identical to the value of the `MLModelId` in the request.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The endpoint information of the `MLModel`
    realtime_endpoint_info: "RealtimeEndpointInfo" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteTagsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_keys",
                "TagKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(TaggableResourceType),
            ),
        ]

    # One or more tags to delete.
    tag_keys: typing.List[str] = dataclasses.field(default_factory=list, )

    # The ID of the tagged ML object. For example, `exampleModelId`.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of the tagged ML object.
    resource_type: "TaggableResourceType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteTagsOutput(autoboto.ShapeBase):
    """
    Amazon ML returns the following elements.
    """

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
                autoboto.TypeInfo(TaggableResourceType),
            ),
        ]

    # The ID of the ML object from which tags were deleted.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of the ML object from which tags were deleted.
    resource_type: "TaggableResourceType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeBatchPredictionsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter_variable",
                "FilterVariable",
                autoboto.TypeInfo(BatchPredictionFilterVariable),
            ),
            (
                "eq",
                "EQ",
                autoboto.TypeInfo(str),
            ),
            (
                "gt",
                "GT",
                autoboto.TypeInfo(str),
            ),
            (
                "lt",
                "LT",
                autoboto.TypeInfo(str),
            ),
            (
                "ge",
                "GE",
                autoboto.TypeInfo(str),
            ),
            (
                "le",
                "LE",
                autoboto.TypeInfo(str),
            ),
            (
                "ne",
                "NE",
                autoboto.TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "sort_order",
                "SortOrder",
                autoboto.TypeInfo(SortOrder),
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

    # Use one of the following variables to filter a list of `BatchPrediction`:

    #   * `CreatedAt` \- Sets the search criteria to the `BatchPrediction` creation date.
    #   * `Status` \- Sets the search criteria to the `BatchPrediction` status.
    #   * `Name` \- Sets the search criteria to the contents of the `BatchPrediction` **** `Name`.
    #   * `IAMUser` \- Sets the search criteria to the user account that invoked the `BatchPrediction` creation.
    #   * `MLModelId` \- Sets the search criteria to the `MLModel` used in the `BatchPrediction`.
    #   * `DataSourceId` \- Sets the search criteria to the `DataSource` used in the `BatchPrediction`.
    #   * `DataURI` \- Sets the search criteria to the data file(s) used in the `BatchPrediction`. The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.
    filter_variable: "BatchPredictionFilterVariable" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The equal to operator. The `BatchPrediction` results will have
    # `FilterVariable` values that exactly match the value specified with `EQ`.
    eq: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The greater than operator. The `BatchPrediction` results will have
    # `FilterVariable` values that are greater than the value specified with
    # `GT`.
    gt: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The less than operator. The `BatchPrediction` results will have
    # `FilterVariable` values that are less than the value specified with `LT`.
    lt: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The greater than or equal to operator. The `BatchPrediction` results will
    # have `FilterVariable` values that are greater than or equal to the value
    # specified with `GE`.
    ge: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The less than or equal to operator. The `BatchPrediction` results will have
    # `FilterVariable` values that are less than or equal to the value specified
    # with `LE`.
    le: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The not equal to operator. The `BatchPrediction` results will have
    # `FilterVariable` values not equal to the value specified with `NE`.
    ne: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A string that is found at the beginning of a variable, such as `Name` or
    # `Id`.

    # For example, a `Batch Prediction` operation could have the `Name`
    # `2014-09-09-HolidayGiftMailer`. To search for this `BatchPrediction`,
    # select `Name` for the `FilterVariable` and any of the following strings for
    # the `Prefix`:

    #   * 2014-09

    #   * 2014-09-09

    #   * 2014-09-09-Holiday
    prefix: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A two-value parameter that determines the sequence of the resulting list of
    # `MLModel`s.

    #   * `asc` \- Arranges the list in ascending order (A-Z, 0-9).
    #   * `dsc` \- Arranges the list in descending order (Z-A, 9-0).

    # Results are sorted by `FilterVariable`.
    sort_order: "SortOrder" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An ID of the page in the paginated results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of pages of information to include in the result. The range of
    # acceptable values is `1` through `100`. The default value is `100`.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeBatchPredictionsOutput(autoboto.ShapeBase):
    """
    Represents the output of a `DescribeBatchPredictions` operation. The content is
    essentially a list of `BatchPrediction`s.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "results",
                "Results",
                autoboto.TypeInfo(typing.List[BatchPrediction]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of `BatchPrediction` objects that meet the search criteria.
    results: typing.List["BatchPrediction"] = dataclasses.field(
        default_factory=list,
    )

    # The ID of the next page in the paginated results that indicates at least
    # one more page follows.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeDataSourcesInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter_variable",
                "FilterVariable",
                autoboto.TypeInfo(DataSourceFilterVariable),
            ),
            (
                "eq",
                "EQ",
                autoboto.TypeInfo(str),
            ),
            (
                "gt",
                "GT",
                autoboto.TypeInfo(str),
            ),
            (
                "lt",
                "LT",
                autoboto.TypeInfo(str),
            ),
            (
                "ge",
                "GE",
                autoboto.TypeInfo(str),
            ),
            (
                "le",
                "LE",
                autoboto.TypeInfo(str),
            ),
            (
                "ne",
                "NE",
                autoboto.TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "sort_order",
                "SortOrder",
                autoboto.TypeInfo(SortOrder),
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

    # Use one of the following variables to filter a list of `DataSource`:

    #   * `CreatedAt` \- Sets the search criteria to `DataSource` creation dates.
    #   * `Status` \- Sets the search criteria to `DataSource` statuses.
    #   * `Name` \- Sets the search criteria to the contents of `DataSource` **** `Name`.
    #   * `DataUri` \- Sets the search criteria to the URI of data files used to create the `DataSource`. The URI can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
    #   * `IAMUser` \- Sets the search criteria to the user account that invoked the `DataSource` creation.
    filter_variable: "DataSourceFilterVariable" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The equal to operator. The `DataSource` results will have `FilterVariable`
    # values that exactly match the value specified with `EQ`.
    eq: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The greater than operator. The `DataSource` results will have
    # `FilterVariable` values that are greater than the value specified with
    # `GT`.
    gt: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The less than operator. The `DataSource` results will have `FilterVariable`
    # values that are less than the value specified with `LT`.
    lt: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The greater than or equal to operator. The `DataSource` results will have
    # `FilterVariable` values that are greater than or equal to the value
    # specified with `GE`.
    ge: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The less than or equal to operator. The `DataSource` results will have
    # `FilterVariable` values that are less than or equal to the value specified
    # with `LE`.
    le: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The not equal to operator. The `DataSource` results will have
    # `FilterVariable` values not equal to the value specified with `NE`.
    ne: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A string that is found at the beginning of a variable, such as `Name` or
    # `Id`.

    # For example, a `DataSource` could have the `Name`
    # `2014-09-09-HolidayGiftMailer`. To search for this `DataSource`, select
    # `Name` for the `FilterVariable` and any of the following strings for the
    # `Prefix`:

    #   * 2014-09

    #   * 2014-09-09

    #   * 2014-09-09-Holiday
    prefix: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A two-value parameter that determines the sequence of the resulting list of
    # `DataSource`.

    #   * `asc` \- Arranges the list in ascending order (A-Z, 0-9).
    #   * `dsc` \- Arranges the list in descending order (Z-A, 9-0).

    # Results are sorted by `FilterVariable`.
    sort_order: "SortOrder" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the page in the paginated results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of `DataSource` to include in the result.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeDataSourcesOutput(autoboto.ShapeBase):
    """
    Represents the query results from a DescribeDataSources operation. The content
    is essentially a list of `DataSource`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "results",
                "Results",
                autoboto.TypeInfo(typing.List[DataSource]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of `DataSource` that meet the search criteria.
    results: typing.List["DataSource"] = dataclasses.field(
        default_factory=list,
    )

    # An ID of the next page in the paginated results that indicates at least one
    # more page follows.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeEvaluationsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter_variable",
                "FilterVariable",
                autoboto.TypeInfo(EvaluationFilterVariable),
            ),
            (
                "eq",
                "EQ",
                autoboto.TypeInfo(str),
            ),
            (
                "gt",
                "GT",
                autoboto.TypeInfo(str),
            ),
            (
                "lt",
                "LT",
                autoboto.TypeInfo(str),
            ),
            (
                "ge",
                "GE",
                autoboto.TypeInfo(str),
            ),
            (
                "le",
                "LE",
                autoboto.TypeInfo(str),
            ),
            (
                "ne",
                "NE",
                autoboto.TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "sort_order",
                "SortOrder",
                autoboto.TypeInfo(SortOrder),
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

    # Use one of the following variable to filter a list of `Evaluation` objects:

    #   * `CreatedAt` \- Sets the search criteria to the `Evaluation` creation date.
    #   * `Status` \- Sets the search criteria to the `Evaluation` status.
    #   * `Name` \- Sets the search criteria to the contents of `Evaluation` **** `Name`.
    #   * `IAMUser` \- Sets the search criteria to the user account that invoked an `Evaluation`.
    #   * `MLModelId` \- Sets the search criteria to the `MLModel` that was evaluated.
    #   * `DataSourceId` \- Sets the search criteria to the `DataSource` used in `Evaluation`.
    #   * `DataUri` \- Sets the search criteria to the data file(s) used in `Evaluation`. The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.
    filter_variable: "EvaluationFilterVariable" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The equal to operator. The `Evaluation` results will have `FilterVariable`
    # values that exactly match the value specified with `EQ`.
    eq: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The greater than operator. The `Evaluation` results will have
    # `FilterVariable` values that are greater than the value specified with
    # `GT`.
    gt: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The less than operator. The `Evaluation` results will have `FilterVariable`
    # values that are less than the value specified with `LT`.
    lt: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The greater than or equal to operator. The `Evaluation` results will have
    # `FilterVariable` values that are greater than or equal to the value
    # specified with `GE`.
    ge: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The less than or equal to operator. The `Evaluation` results will have
    # `FilterVariable` values that are less than or equal to the value specified
    # with `LE`.
    le: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The not equal to operator. The `Evaluation` results will have
    # `FilterVariable` values not equal to the value specified with `NE`.
    ne: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A string that is found at the beginning of a variable, such as `Name` or
    # `Id`.

    # For example, an `Evaluation` could have the `Name`
    # `2014-09-09-HolidayGiftMailer`. To search for this `Evaluation`, select
    # `Name` for the `FilterVariable` and any of the following strings for the
    # `Prefix`:

    #   * 2014-09

    #   * 2014-09-09

    #   * 2014-09-09-Holiday
    prefix: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A two-value parameter that determines the sequence of the resulting list of
    # `Evaluation`.

    #   * `asc` \- Arranges the list in ascending order (A-Z, 0-9).
    #   * `dsc` \- Arranges the list in descending order (Z-A, 9-0).

    # Results are sorted by `FilterVariable`.
    sort_order: "SortOrder" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the page in the paginated results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of `Evaluation` to include in the result.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeEvaluationsOutput(autoboto.ShapeBase):
    """
    Represents the query results from a `DescribeEvaluations` operation. The content
    is essentially a list of `Evaluation`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "results",
                "Results",
                autoboto.TypeInfo(typing.List[Evaluation]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of `Evaluation` that meet the search criteria.
    results: typing.List["Evaluation"] = dataclasses.field(
        default_factory=list,
    )

    # The ID of the next page in the paginated results that indicates at least
    # one more page follows.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeMLModelsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter_variable",
                "FilterVariable",
                autoboto.TypeInfo(MLModelFilterVariable),
            ),
            (
                "eq",
                "EQ",
                autoboto.TypeInfo(str),
            ),
            (
                "gt",
                "GT",
                autoboto.TypeInfo(str),
            ),
            (
                "lt",
                "LT",
                autoboto.TypeInfo(str),
            ),
            (
                "ge",
                "GE",
                autoboto.TypeInfo(str),
            ),
            (
                "le",
                "LE",
                autoboto.TypeInfo(str),
            ),
            (
                "ne",
                "NE",
                autoboto.TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "sort_order",
                "SortOrder",
                autoboto.TypeInfo(SortOrder),
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

    # Use one of the following variables to filter a list of `MLModel`:

    #   * `CreatedAt` \- Sets the search criteria to `MLModel` creation date.
    #   * `Status` \- Sets the search criteria to `MLModel` status.
    #   * `Name` \- Sets the search criteria to the contents of `MLModel` **** `Name`.
    #   * `IAMUser` \- Sets the search criteria to the user account that invoked the `MLModel` creation.
    #   * `TrainingDataSourceId` \- Sets the search criteria to the `DataSource` used to train one or more `MLModel`.
    #   * `RealtimeEndpointStatus` \- Sets the search criteria to the `MLModel` real-time endpoint status.
    #   * `MLModelType` \- Sets the search criteria to `MLModel` type: binary, regression, or multi-class.
    #   * `Algorithm` \- Sets the search criteria to the algorithm that the `MLModel` uses.
    #   * `TrainingDataURI` \- Sets the search criteria to the data file(s) used in training a `MLModel`. The URL can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
    filter_variable: "MLModelFilterVariable" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The equal to operator. The `MLModel` results will have `FilterVariable`
    # values that exactly match the value specified with `EQ`.
    eq: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The greater than operator. The `MLModel` results will have `FilterVariable`
    # values that are greater than the value specified with `GT`.
    gt: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The less than operator. The `MLModel` results will have `FilterVariable`
    # values that are less than the value specified with `LT`.
    lt: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The greater than or equal to operator. The `MLModel` results will have
    # `FilterVariable` values that are greater than or equal to the value
    # specified with `GE`.
    ge: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The less than or equal to operator. The `MLModel` results will have
    # `FilterVariable` values that are less than or equal to the value specified
    # with `LE`.
    le: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The not equal to operator. The `MLModel` results will have `FilterVariable`
    # values not equal to the value specified with `NE`.
    ne: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A string that is found at the beginning of a variable, such as `Name` or
    # `Id`.

    # For example, an `MLModel` could have the `Name`
    # `2014-09-09-HolidayGiftMailer`. To search for this `MLModel`, select `Name`
    # for the `FilterVariable` and any of the following strings for the `Prefix`:

    #   * 2014-09

    #   * 2014-09-09

    #   * 2014-09-09-Holiday
    prefix: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A two-value parameter that determines the sequence of the resulting list of
    # `MLModel`.

    #   * `asc` \- Arranges the list in ascending order (A-Z, 0-9).
    #   * `dsc` \- Arranges the list in descending order (Z-A, 9-0).

    # Results are sorted by `FilterVariable`.
    sort_order: "SortOrder" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the page in the paginated results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of pages of information to include in the result. The range of
    # acceptable values is `1` through `100`. The default value is `100`.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeMLModelsOutput(autoboto.ShapeBase):
    """
    Represents the output of a `DescribeMLModels` operation. The content is
    essentially a list of `MLModel`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "results",
                "Results",
                autoboto.TypeInfo(typing.List[MLModel]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of `MLModel` that meet the search criteria.
    results: typing.List["MLModel"] = dataclasses.field(default_factory=list, )

    # The ID of the next page in the paginated results that indicates at least
    # one more page follows.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeTagsInput(autoboto.ShapeBase):
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
                autoboto.TypeInfo(TaggableResourceType),
            ),
        ]

    # The ID of the ML object. For example, `exampleModelId`.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of the ML object.
    resource_type: "TaggableResourceType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeTagsOutput(autoboto.ShapeBase):
    """
    Amazon ML returns the following elements.
    """

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
                autoboto.TypeInfo(TaggableResourceType),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The ID of the tagged ML object.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of the tagged ML object.
    resource_type: "TaggableResourceType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of tags associated with the ML object.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


class DetailsAttributes(Enum):
    """
    Contains the key values of `DetailsMap`: `PredictiveModelType` \- Indicates the
    type of the `MLModel`. `Algorithm` \- Indicates the algorithm that was used for
    the `MLModel`.
    """
    PredictiveModelType = "PredictiveModelType"
    Algorithm = "Algorithm"


class EntityStatus(Enum):
    """
    Object status with the following possible values:

      * `PENDING`
      * `INPROGRESS`
      * `FAILED`
      * `COMPLETED`
      * `DELETED`
    """
    PENDING = "PENDING"
    INPROGRESS = "INPROGRESS"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    DELETED = "DELETED"


@dataclasses.dataclass
class Evaluation(autoboto.ShapeBase):
    """
    Represents the output of `GetEvaluation` operation.

    The content consists of the detailed metadata and data file information and the
    current status of the `Evaluation`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "evaluation_id",
                "EvaluationId",
                autoboto.TypeInfo(str),
            ),
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
            (
                "evaluation_data_source_id",
                "EvaluationDataSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "input_data_location_s3",
                "InputDataLocationS3",
                autoboto.TypeInfo(str),
            ),
            (
                "created_by_iam_user",
                "CreatedByIamUser",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_at",
                "LastUpdatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(EntityStatus),
            ),
            (
                "performance_metrics",
                "PerformanceMetrics",
                autoboto.TypeInfo(PerformanceMetrics),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "compute_time",
                "ComputeTime",
                autoboto.TypeInfo(int),
            ),
            (
                "finished_at",
                "FinishedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "started_at",
                "StartedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ID that is assigned to the `Evaluation` at creation.
    evaluation_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `MLModel` that is the focus of the evaluation.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the `DataSource` that is used to evaluate the `MLModel`.
    evaluation_data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The location and name of the data in Amazon Simple Storage Server (Amazon
    # S3) that is used in the evaluation.
    input_data_location_s3: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS user account that invoked the evaluation. The account type can be
    # either an AWS root account or an AWS Identity and Access Management (IAM)
    # user account.
    created_by_iam_user: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time that the `Evaluation` was created. The time is expressed in epoch
    # time.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time of the most recent edit to the `Evaluation`. The time is expressed
    # in epoch time.
    last_updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A user-supplied name or description of the `Evaluation`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the evaluation. This element can have one of the following
    # values:

    #   * `PENDING` \- Amazon Machine Learning (Amazon ML) submitted a request to evaluate an `MLModel`.
    #   * `INPROGRESS` \- The evaluation is underway.
    #   * `FAILED` \- The request to evaluate an `MLModel` did not run to completion. It is not usable.
    #   * `COMPLETED` \- The evaluation process completed successfully.
    #   * `DELETED` \- The `Evaluation` is marked as deleted. It is not usable.
    status: "EntityStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Measurements of how well the `MLModel` performed, using observations
    # referenced by the `DataSource`. One of the following metrics is returned,
    # based on the type of the `MLModel`:

    #   * BinaryAUC: A binary `MLModel` uses the Area Under the Curve (AUC) technique to measure performance.

    #   * RegressionRMSE: A regression `MLModel` uses the Root Mean Square Error (RMSE) technique to measure performance. RMSE measures the difference between predicted and actual values for a single variable.

    #   * MulticlassAvgFScore: A multiclass `MLModel` uses the F1 score technique to measure performance.

    # For more information about performance metrics, please see the [Amazon
    # Machine Learning Developer Guide](http://docs.aws.amazon.com/machine-
    # learning/latest/dg).
    performance_metrics: "PerformanceMetrics" = dataclasses.field(
        default_factory=dict,
    )

    # A description of the most recent details about evaluating the `MLModel`.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Long integer type that is a 64-bit signed number.
    compute_time: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A timestamp represented in epoch time.
    finished_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A timestamp represented in epoch time.
    started_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class EvaluationFilterVariable(Enum):
    """
    A list of the variables to use in searching or filtering `Evaluation`.

      * `CreatedAt` \- Sets the search criteria to `Evaluation` creation date.
      * `Status` \- Sets the search criteria to `Evaluation` status.
      * `Name` \- Sets the search criteria to the contents of `Evaluation` **** `Name`.
      * `IAMUser` \- Sets the search criteria to the user account that invoked an evaluation.
      * `MLModelId` \- Sets the search criteria to the `Predictor` that was evaluated.
      * `DataSourceId` \- Sets the search criteria to the `DataSource` used in evaluation.
      * `DataUri` \- Sets the search criteria to the data file(s) used in evaluation. The URL can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
    """
    CreatedAt = "CreatedAt"
    LastUpdatedAt = "LastUpdatedAt"
    Status = "Status"
    Name = "Name"
    IAMUser = "IAMUser"
    MLModelId = "MLModelId"
    DataSourceId = "DataSourceId"
    DataURI = "DataURI"


@dataclasses.dataclass
class GetBatchPredictionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "batch_prediction_id",
                "BatchPredictionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # An ID assigned to the `BatchPrediction` at creation.
    batch_prediction_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetBatchPredictionOutput(autoboto.ShapeBase):
    """
    Represents the output of a `GetBatchPrediction` operation and describes a
    `BatchPrediction`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "batch_prediction_id",
                "BatchPredictionId",
                autoboto.TypeInfo(str),
            ),
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
            (
                "batch_prediction_data_source_id",
                "BatchPredictionDataSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "input_data_location_s3",
                "InputDataLocationS3",
                autoboto.TypeInfo(str),
            ),
            (
                "created_by_iam_user",
                "CreatedByIamUser",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_at",
                "LastUpdatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(EntityStatus),
            ),
            (
                "output_uri",
                "OutputUri",
                autoboto.TypeInfo(str),
            ),
            (
                "log_uri",
                "LogUri",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "compute_time",
                "ComputeTime",
                autoboto.TypeInfo(int),
            ),
            (
                "finished_at",
                "FinishedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "started_at",
                "StartedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "total_record_count",
                "TotalRecordCount",
                autoboto.TypeInfo(int),
            ),
            (
                "invalid_record_count",
                "InvalidRecordCount",
                autoboto.TypeInfo(int),
            ),
        ]

    # An ID assigned to the `BatchPrediction` at creation. This value should be
    # identical to the value of the `BatchPredictionID` in the request.
    batch_prediction_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `MLModel` that generated predictions for the
    # `BatchPrediction` request.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the `DataSource` that was used to create the `BatchPrediction`.
    batch_prediction_data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The location of the data file or directory in Amazon Simple Storage Service
    # (Amazon S3).
    input_data_location_s3: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS user account that invoked the `BatchPrediction`. The account type
    # can be either an AWS root account or an AWS Identity and Access Management
    # (IAM) user account.
    created_by_iam_user: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time when the `BatchPrediction` was created. The time is expressed in
    # epoch time.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time of the most recent edit to `BatchPrediction`. The time is
    # expressed in epoch time.
    last_updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A user-supplied name or description of the `BatchPrediction`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the `BatchPrediction`, which can be one of the following
    # values:

    #   * `PENDING` \- Amazon Machine Learning (Amazon ML) submitted a request to generate batch predictions.
    #   * `INPROGRESS` \- The batch predictions are in progress.
    #   * `FAILED` \- The request to perform a batch prediction did not run to completion. It is not usable.
    #   * `COMPLETED` \- The batch prediction process completed successfully.
    #   * `DELETED` \- The `BatchPrediction` is marked as deleted. It is not usable.
    status: "EntityStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The location of an Amazon S3 bucket or directory to receive the operation
    # results.
    output_uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A link to the file that contains logs of the `CreateBatchPrediction`
    # operation.
    log_uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A description of the most recent details about processing the batch
    # prediction request.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The approximate CPU time in milliseconds that Amazon Machine Learning spent
    # processing the `BatchPrediction`, normalized and scaled on computation
    # resources. `ComputeTime` is only available if the `BatchPrediction` is in
    # the `COMPLETED` state.
    compute_time: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The epoch time when Amazon Machine Learning marked the `BatchPrediction` as
    # `COMPLETED` or `FAILED`. `FinishedAt` is only available when the
    # `BatchPrediction` is in the `COMPLETED` or `FAILED` state.
    finished_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The epoch time when Amazon Machine Learning marked the `BatchPrediction` as
    # `INPROGRESS`. `StartedAt` isn't available if the `BatchPrediction` is in
    # the `PENDING` state.
    started_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of total records that Amazon Machine Learning saw while
    # processing the `BatchPrediction`.
    total_record_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of invalid records that Amazon Machine Learning saw while
    # processing the `BatchPrediction`.
    invalid_record_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetDataSourceInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source_id",
                "DataSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "verbose",
                "Verbose",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID assigned to the `DataSource` at creation.
    data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether the `GetDataSource` operation should return
    # `DataSourceSchema`.

    # If true, `DataSourceSchema` is returned.

    # If false, `DataSourceSchema` is not returned.
    verbose: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDataSourceOutput(autoboto.ShapeBase):
    """
    Represents the output of a `GetDataSource` operation and describes a
    `DataSource`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source_id",
                "DataSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "data_location_s3",
                "DataLocationS3",
                autoboto.TypeInfo(str),
            ),
            (
                "data_rearrangement",
                "DataRearrangement",
                autoboto.TypeInfo(str),
            ),
            (
                "created_by_iam_user",
                "CreatedByIamUser",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_at",
                "LastUpdatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "data_size_in_bytes",
                "DataSizeInBytes",
                autoboto.TypeInfo(int),
            ),
            (
                "number_of_files",
                "NumberOfFiles",
                autoboto.TypeInfo(int),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(EntityStatus),
            ),
            (
                "log_uri",
                "LogUri",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "redshift_metadata",
                "RedshiftMetadata",
                autoboto.TypeInfo(RedshiftMetadata),
            ),
            (
                "rds_metadata",
                "RDSMetadata",
                autoboto.TypeInfo(RDSMetadata),
            ),
            (
                "role_arn",
                "RoleARN",
                autoboto.TypeInfo(str),
            ),
            (
                "compute_statistics",
                "ComputeStatistics",
                autoboto.TypeInfo(bool),
            ),
            (
                "compute_time",
                "ComputeTime",
                autoboto.TypeInfo(int),
            ),
            (
                "finished_at",
                "FinishedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "started_at",
                "StartedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "data_source_schema",
                "DataSourceSchema",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID assigned to the `DataSource` at creation. This value should be
    # identical to the value of the `DataSourceId` in the request.
    data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The location of the data file or directory in Amazon Simple Storage Service
    # (Amazon S3).
    data_location_s3: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A JSON string that represents the splitting and rearrangement requirement
    # used when this `DataSource` was created.
    data_rearrangement: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS user account from which the `DataSource` was created. The account
    # type can be either an AWS root account or an AWS Identity and Access
    # Management (IAM) user account.
    created_by_iam_user: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time that the `DataSource` was created. The time is expressed in epoch
    # time.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time of the most recent edit to the `DataSource`. The time is expressed
    # in epoch time.
    last_updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The total size of observations in the data files.
    data_size_in_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of data files referenced by the `DataSource`.
    number_of_files: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A user-supplied name or description of the `DataSource`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The current status of the `DataSource`. This element can have one of the
    # following values:

    #   * `PENDING` \- Amazon ML submitted a request to create a `DataSource`.
    #   * `INPROGRESS` \- The creation process is underway.
    #   * `FAILED` \- The request to create a `DataSource` did not run to completion. It is not usable.
    #   * `COMPLETED` \- The creation process completed successfully.
    #   * `DELETED` \- The `DataSource` is marked as deleted. It is not usable.
    status: "EntityStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A link to the file containing logs of `CreateDataSourceFrom*` operations.
    log_uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user-supplied description of the most recent details about creating the
    # `DataSource`.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Describes the `DataSource` details specific to Amazon Redshift.
    redshift_metadata: "RedshiftMetadata" = dataclasses.field(
        default_factory=dict,
    )

    # The datasource details that are specific to Amazon RDS.
    rds_metadata: "RDSMetadata" = dataclasses.field(default_factory=dict, )

    # The Amazon Resource Name (ARN) of an [AWS IAM
    # Role](http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-
    # toplevel.html#roles-about-termsandconcepts), such as the following:
    # arn:aws:iam::account:role/rolename.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The parameter is `true` if statistics need to be generated from the
    # observation data.
    compute_statistics: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The approximate CPU time in milliseconds that Amazon Machine Learning spent
    # processing the `DataSource`, normalized and scaled on computation
    # resources. `ComputeTime` is only available if the `DataSource` is in the
    # `COMPLETED` state and the `ComputeStatistics` is set to true.
    compute_time: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The epoch time when Amazon Machine Learning marked the `DataSource` as
    # `COMPLETED` or `FAILED`. `FinishedAt` is only available when the
    # `DataSource` is in the `COMPLETED` or `FAILED` state.
    finished_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The epoch time when Amazon Machine Learning marked the `DataSource` as
    # `INPROGRESS`. `StartedAt` isn't available if the `DataSource` is in the
    # `PENDING` state.
    started_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The schema used by all of the data files of this `DataSource`.

    # Note

    # This parameter is provided as part of the verbose format.
    data_source_schema: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetEvaluationInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "evaluation_id",
                "EvaluationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the `Evaluation` to retrieve. The evaluation of each `MLModel` is
    # recorded and cataloged. The ID provides the means to access the
    # information.
    evaluation_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetEvaluationOutput(autoboto.ShapeBase):
    """
    Represents the output of a `GetEvaluation` operation and describes an
    `Evaluation`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "evaluation_id",
                "EvaluationId",
                autoboto.TypeInfo(str),
            ),
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
            (
                "evaluation_data_source_id",
                "EvaluationDataSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "input_data_location_s3",
                "InputDataLocationS3",
                autoboto.TypeInfo(str),
            ),
            (
                "created_by_iam_user",
                "CreatedByIamUser",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_at",
                "LastUpdatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(EntityStatus),
            ),
            (
                "performance_metrics",
                "PerformanceMetrics",
                autoboto.TypeInfo(PerformanceMetrics),
            ),
            (
                "log_uri",
                "LogUri",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "compute_time",
                "ComputeTime",
                autoboto.TypeInfo(int),
            ),
            (
                "finished_at",
                "FinishedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "started_at",
                "StartedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The evaluation ID which is same as the `EvaluationId` in the request.
    evaluation_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `MLModel` that was the focus of the evaluation.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The `DataSource` used for this evaluation.
    evaluation_data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The location of the data file or directory in Amazon Simple Storage Service
    # (Amazon S3).
    input_data_location_s3: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS user account that invoked the evaluation. The account type can be
    # either an AWS root account or an AWS Identity and Access Management (IAM)
    # user account.
    created_by_iam_user: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time that the `Evaluation` was created. The time is expressed in epoch
    # time.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time of the most recent edit to the `Evaluation`. The time is expressed
    # in epoch time.
    last_updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A user-supplied name or description of the `Evaluation`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the evaluation. This element can have one of the following
    # values:

    #   * `PENDING` \- Amazon Machine Language (Amazon ML) submitted a request to evaluate an `MLModel`.
    #   * `INPROGRESS` \- The evaluation is underway.
    #   * `FAILED` \- The request to evaluate an `MLModel` did not run to completion. It is not usable.
    #   * `COMPLETED` \- The evaluation process completed successfully.
    #   * `DELETED` \- The `Evaluation` is marked as deleted. It is not usable.
    status: "EntityStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Measurements of how well the `MLModel` performed using observations
    # referenced by the `DataSource`. One of the following metric is returned
    # based on the type of the `MLModel`:

    #   * BinaryAUC: A binary `MLModel` uses the Area Under the Curve (AUC) technique to measure performance.

    #   * RegressionRMSE: A regression `MLModel` uses the Root Mean Square Error (RMSE) technique to measure performance. RMSE measures the difference between predicted and actual values for a single variable.

    #   * MulticlassAvgFScore: A multiclass `MLModel` uses the F1 score technique to measure performance.

    # For more information about performance metrics, please see the [Amazon
    # Machine Learning Developer Guide](http://docs.aws.amazon.com/machine-
    # learning/latest/dg).
    performance_metrics: "PerformanceMetrics" = dataclasses.field(
        default_factory=dict,
    )

    # A link to the file that contains logs of the `CreateEvaluation` operation.
    log_uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A description of the most recent details about evaluating the `MLModel`.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The approximate CPU time in milliseconds that Amazon Machine Learning spent
    # processing the `Evaluation`, normalized and scaled on computation
    # resources. `ComputeTime` is only available if the `Evaluation` is in the
    # `COMPLETED` state.
    compute_time: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The epoch time when Amazon Machine Learning marked the `Evaluation` as
    # `COMPLETED` or `FAILED`. `FinishedAt` is only available when the
    # `Evaluation` is in the `COMPLETED` or `FAILED` state.
    finished_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The epoch time when Amazon Machine Learning marked the `Evaluation` as
    # `INPROGRESS`. `StartedAt` isn't available if the `Evaluation` is in the
    # `PENDING` state.
    started_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetMLModelInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
            (
                "verbose",
                "Verbose",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID assigned to the `MLModel` at creation.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies whether the `GetMLModel` operation should return `Recipe`.

    # If true, `Recipe` is returned.

    # If false, `Recipe` is not returned.
    verbose: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetMLModelOutput(autoboto.ShapeBase):
    """
    Represents the output of a `GetMLModel` operation, and provides detailed
    information about a `MLModel`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
            (
                "training_data_source_id",
                "TrainingDataSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "created_by_iam_user",
                "CreatedByIamUser",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_at",
                "LastUpdatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(EntityStatus),
            ),
            (
                "size_in_bytes",
                "SizeInBytes",
                autoboto.TypeInfo(int),
            ),
            (
                "endpoint_info",
                "EndpointInfo",
                autoboto.TypeInfo(RealtimeEndpointInfo),
            ),
            (
                "training_parameters",
                "TrainingParameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "input_data_location_s3",
                "InputDataLocationS3",
                autoboto.TypeInfo(str),
            ),
            (
                "ml_model_type",
                "MLModelType",
                autoboto.TypeInfo(MLModelType),
            ),
            (
                "score_threshold",
                "ScoreThreshold",
                autoboto.TypeInfo(float),
            ),
            (
                "score_threshold_last_updated_at",
                "ScoreThresholdLastUpdatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "log_uri",
                "LogUri",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "compute_time",
                "ComputeTime",
                autoboto.TypeInfo(int),
            ),
            (
                "finished_at",
                "FinishedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "started_at",
                "StartedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "recipe",
                "Recipe",
                autoboto.TypeInfo(str),
            ),
            (
                "schema",
                "Schema",
                autoboto.TypeInfo(str),
            ),
        ]

    # The MLModel ID, which is same as the `MLModelId` in the request.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the training `DataSource`.
    training_data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS user account from which the `MLModel` was created. The account type
    # can be either an AWS root account or an AWS Identity and Access Management
    # (IAM) user account.
    created_by_iam_user: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time that the `MLModel` was created. The time is expressed in epoch
    # time.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time of the most recent edit to the `MLModel`. The time is expressed in
    # epoch time.
    last_updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A user-supplied name or description of the `MLModel`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The current status of the `MLModel`. This element can have one of the
    # following values:

    #   * `PENDING` \- Amazon Machine Learning (Amazon ML) submitted a request to describe a `MLModel`.
    #   * `INPROGRESS` \- The request is processing.
    #   * `FAILED` \- The request did not run to completion. The ML model isn't usable.
    #   * `COMPLETED` \- The request completed successfully.
    #   * `DELETED` \- The `MLModel` is marked as deleted. It isn't usable.
    status: "EntityStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Long integer type that is a 64-bit signed number.
    size_in_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The current endpoint of the `MLModel`
    endpoint_info: "RealtimeEndpointInfo" = dataclasses.field(
        default_factory=dict,
    )

    # A list of the training parameters in the `MLModel`. The list is implemented
    # as a map of key-value pairs.

    # The following is the current set of training parameters:

    #   * `sgd.maxMLModelSizeInBytes` \- The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance.

    # The value is an integer that ranges from `100000` to `2147483648`. The
    # default value is `33554432`.

    #   * `sgd.maxPasses` \- The number of times that the training process traverses the observations to build the `MLModel`. The value is an integer that ranges from `1` to `10000`. The default value is `10`.

    #   * `sgd.shuffleType` \- Whether Amazon ML shuffles the training data. Shuffling data improves a model's ability to find the optimal solution for a variety of data types. The valid values are `auto` and `none`. The default value is `none`. We strongly recommend that you shuffle your data.

    #   * `sgd.l1RegularizationAmount` \- The coefficient regularization L1 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to zero, resulting in a sparse feature set. If you use this parameter, start by specifying a small value, such as `1.0E-08`.

    # The value is a double that ranges from `0` to `MAX_DOUBLE`. The default is
    # to not use L1 normalization. This parameter can't be used when `L2` is
    # specified. Use this parameter sparingly.

    #   * `sgd.l2RegularizationAmount` \- The coefficient regularization L2 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as `1.0E-08`.

    # The value is a double that ranges from `0` to `MAX_DOUBLE`. The default is
    # to not use L2 normalization. This parameter can't be used when `L1` is
    # specified. Use this parameter sparingly.
    training_parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The location of the data file or directory in Amazon Simple Storage Service
    # (Amazon S3).
    input_data_location_s3: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Identifies the `MLModel` category. The following are the available types:

    #   * REGRESSION -- Produces a numeric result. For example, "What price should a house be listed at?"
    #   * BINARY -- Produces one of two possible results. For example, "Is this an e-commerce website?"
    #   * MULTICLASS -- Produces one of several possible results. For example, "Is this a HIGH, LOW or MEDIUM risk trade?"
    ml_model_type: "MLModelType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The scoring threshold is used in binary classification `MLModel` models. It
    # marks the boundary between a positive prediction and a negative prediction.

    # Output values greater than or equal to the threshold receive a positive
    # result from the MLModel, such as `true`. Output values less than the
    # threshold receive a negative response from the MLModel, such as `false`.
    score_threshold: float = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time of the most recent edit to the `ScoreThreshold`. The time is
    # expressed in epoch time.
    score_threshold_last_updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A link to the file that contains logs of the `CreateMLModel` operation.
    log_uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A description of the most recent details about accessing the `MLModel`.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The approximate CPU time in milliseconds that Amazon Machine Learning spent
    # processing the `MLModel`, normalized and scaled on computation resources.
    # `ComputeTime` is only available if the `MLModel` is in the `COMPLETED`
    # state.
    compute_time: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The epoch time when Amazon Machine Learning marked the `MLModel` as
    # `COMPLETED` or `FAILED`. `FinishedAt` is only available when the `MLModel`
    # is in the `COMPLETED` or `FAILED` state.
    finished_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The epoch time when Amazon Machine Learning marked the `MLModel` as
    # `INPROGRESS`. `StartedAt` isn't available if the `MLModel` is in the
    # `PENDING` state.
    started_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The recipe to use when training the `MLModel`. The `Recipe` provides
    # detailed information about the observation data to use during training, and
    # manipulations to perform on the observation data during training.

    # Note

    # This parameter is provided as part of the verbose format.
    recipe: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The schema used by all of the data files referenced by the `DataSource`.

    # Note

    # This parameter is provided as part of the verbose format.
    schema: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class IdempotentParameterMismatchException(autoboto.ShapeBase):
    """
    A second request to use or change an object was not allowed. This can result
    from retrying a request using a parameter that was not present in the original
    request.
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
                "code",
                "code",
                autoboto.TypeInfo(int),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
    code: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InternalServerException(autoboto.ShapeBase):
    """
    An error on the server occurred when trying to process a request.
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
                "code",
                "code",
                autoboto.TypeInfo(int),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
    code: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidInputException(autoboto.ShapeBase):
    """
    An error on the client occurred. Typically, the cause is an invalid input value.
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
                "code",
                "code",
                autoboto.TypeInfo(int),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
    code: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidTagException(autoboto.ShapeBase):
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
class LimitExceededException(autoboto.ShapeBase):
    """
    The subscriber exceeded the maximum number of operations. This exception can
    occur when listing objects such as `DataSource`.
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
                "code",
                "code",
                autoboto.TypeInfo(int),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
    code: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class MLModel(autoboto.ShapeBase):
    """
    Represents the output of a `GetMLModel` operation.

    The content consists of the detailed metadata and the current status of the
    `MLModel`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
            (
                "training_data_source_id",
                "TrainingDataSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "created_by_iam_user",
                "CreatedByIamUser",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_at",
                "LastUpdatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(EntityStatus),
            ),
            (
                "size_in_bytes",
                "SizeInBytes",
                autoboto.TypeInfo(int),
            ),
            (
                "endpoint_info",
                "EndpointInfo",
                autoboto.TypeInfo(RealtimeEndpointInfo),
            ),
            (
                "training_parameters",
                "TrainingParameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "input_data_location_s3",
                "InputDataLocationS3",
                autoboto.TypeInfo(str),
            ),
            (
                "algorithm",
                "Algorithm",
                autoboto.TypeInfo(Algorithm),
            ),
            (
                "ml_model_type",
                "MLModelType",
                autoboto.TypeInfo(MLModelType),
            ),
            (
                "score_threshold",
                "ScoreThreshold",
                autoboto.TypeInfo(float),
            ),
            (
                "score_threshold_last_updated_at",
                "ScoreThresholdLastUpdatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "compute_time",
                "ComputeTime",
                autoboto.TypeInfo(int),
            ),
            (
                "finished_at",
                "FinishedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "started_at",
                "StartedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ID assigned to the `MLModel` at creation.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the training `DataSource`. The `CreateMLModel` operation uses the
    # `TrainingDataSourceId`.
    training_data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS user account from which the `MLModel` was created. The account type
    # can be either an AWS root account or an AWS Identity and Access Management
    # (IAM) user account.
    created_by_iam_user: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time that the `MLModel` was created. The time is expressed in epoch
    # time.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time of the most recent edit to the `MLModel`. The time is expressed in
    # epoch time.
    last_updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A user-supplied name or description of the `MLModel`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The current status of an `MLModel`. This element can have one of the
    # following values:

    #   * `PENDING` \- Amazon Machine Learning (Amazon ML) submitted a request to create an `MLModel`.
    #   * `INPROGRESS` \- The creation process is underway.
    #   * `FAILED` \- The request to create an `MLModel` didn't run to completion. The model isn't usable.
    #   * `COMPLETED` \- The creation process completed successfully.
    #   * `DELETED` \- The `MLModel` is marked as deleted. It isn't usable.
    status: "EntityStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Long integer type that is a 64-bit signed number.
    size_in_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The current endpoint of the `MLModel`.
    endpoint_info: "RealtimeEndpointInfo" = dataclasses.field(
        default_factory=dict,
    )

    # A list of the training parameters in the `MLModel`. The list is implemented
    # as a map of key-value pairs.

    # The following is the current set of training parameters:

    #   * `sgd.maxMLModelSizeInBytes` \- The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance.

    # The value is an integer that ranges from `100000` to `2147483648`. The
    # default value is `33554432`.

    #   * `sgd.maxPasses` \- The number of times that the training process traverses the observations to build the `MLModel`. The value is an integer that ranges from `1` to `10000`. The default value is `10`.

    #   * `sgd.shuffleType` \- Whether Amazon ML shuffles the training data. Shuffling the data improves a model's ability to find the optimal solution for a variety of data types. The valid values are `auto` and `none`. The default value is `none`.

    #   * `sgd.l1RegularizationAmount` \- The coefficient regularization L1 norm, which controls overfitting the data by penalizing large coefficients. This parameter tends to drive coefficients to zero, resulting in sparse feature set. If you use this parameter, start by specifying a small value, such as `1.0E-08`.

    # The value is a double that ranges from `0` to `MAX_DOUBLE`. The default is
    # to not use L1 normalization. This parameter can't be used when `L2` is
    # specified. Use this parameter sparingly.

    #   * `sgd.l2RegularizationAmount` \- The coefficient regularization L2 norm, which controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as `1.0E-08`.

    # The value is a double that ranges from `0` to `MAX_DOUBLE`. The default is
    # to not use L2 normalization. This parameter can't be used when `L1` is
    # specified. Use this parameter sparingly.
    training_parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The location of the data file or directory in Amazon Simple Storage Service
    # (Amazon S3).
    input_data_location_s3: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The algorithm used to train the `MLModel`. The following algorithm is
    # supported:

    #   * `SGD` \-- Stochastic gradient descent. The goal of `SGD` is to minimize the gradient of the loss function.
    algorithm: "Algorithm" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Identifies the `MLModel` category. The following are the available types:

    #   * `REGRESSION` \- Produces a numeric result. For example, "What price should a house be listed at?"
    #   * `BINARY` \- Produces one of two possible results. For example, "Is this a child-friendly web site?".
    #   * `MULTICLASS` \- Produces one of several possible results. For example, "Is this a HIGH-, LOW-, or MEDIUM-risk trade?".
    ml_model_type: "MLModelType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
    score_threshold: float = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time of the most recent edit to the `ScoreThreshold`. The time is
    # expressed in epoch time.
    score_threshold_last_updated_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the most recent details about accessing the `MLModel`.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Long integer type that is a 64-bit signed number.
    compute_time: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A timestamp represented in epoch time.
    finished_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A timestamp represented in epoch time.
    started_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class MLModelFilterVariable(Enum):
    CreatedAt = "CreatedAt"
    LastUpdatedAt = "LastUpdatedAt"
    Status = "Status"
    Name = "Name"
    IAMUser = "IAMUser"
    TrainingDataSourceId = "TrainingDataSourceId"
    RealtimeEndpointStatus = "RealtimeEndpointStatus"
    MLModelType = "MLModelType"
    Algorithm = "Algorithm"
    TrainingDataURI = "TrainingDataURI"


class MLModelType(Enum):
    REGRESSION = "REGRESSION"
    BINARY = "BINARY"
    MULTICLASS = "MULTICLASS"


@dataclasses.dataclass
class PerformanceMetrics(autoboto.ShapeBase):
    """
    Measurements of how well the `MLModel` performed on known observations. One of
    the following metrics is returned, based on the type of the `MLModel`:

      * BinaryAUC: The binary `MLModel` uses the Area Under the Curve (AUC) technique to measure performance. 

      * RegressionRMSE: The regression `MLModel` uses the Root Mean Square Error (RMSE) technique to measure performance. RMSE measures the difference between predicted and actual values for a single variable.

      * MulticlassAvgFScore: The multiclass `MLModel` uses the F1 score technique to measure performance. 

    For more information about performance metrics, please see the [Amazon Machine
    Learning Developer Guide](http://docs.aws.amazon.com/machine-
    learning/latest/dg).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "properties",
                "Properties",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    properties: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PredictInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
            (
                "record",
                "Record",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "predict_endpoint",
                "PredictEndpoint",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier of the `MLModel`.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A map of variable name-value pairs that represent an observation.
    record: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
    predict_endpoint: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PredictOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prediction",
                "Prediction",
                autoboto.TypeInfo(Prediction),
            ),
        ]

    # The output from a `Predict` operation:

    #   * `Details` \- Contains the following attributes: `DetailsAttributes.PREDICTIVE_MODEL_TYPE - REGRESSION | BINARY | MULTICLASS` `DetailsAttributes.ALGORITHM - SGD`

    #   * `PredictedLabel` \- Present for either a `BINARY` or `MULTICLASS` `MLModel` request.

    #   * `PredictedScores` \- Contains the raw classification score corresponding to each label.

    #   * `PredictedValue` \- Present for a `REGRESSION` `MLModel` request.
    prediction: "Prediction" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class Prediction(autoboto.ShapeBase):
    """
    The output from a `Predict` operation:

      * `Details` \- Contains the following attributes: `DetailsAttributes.PREDICTIVE_MODEL_TYPE - REGRESSION | BINARY | MULTICLASS` `DetailsAttributes.ALGORITHM - SGD`

      * `PredictedLabel` \- Present for either a `BINARY` or `MULTICLASS` `MLModel` request. 

      * `PredictedScores` \- Contains the raw classification score corresponding to each label. 

      * `PredictedValue` \- Present for a `REGRESSION` `MLModel` request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "predicted_label",
                "predictedLabel",
                autoboto.TypeInfo(str),
            ),
            (
                "predicted_value",
                "predictedValue",
                autoboto.TypeInfo(float),
            ),
            (
                "predicted_scores",
                "predictedScores",
                autoboto.TypeInfo(typing.Dict[str, float]),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(typing.Dict[DetailsAttributes, str]),
            ),
        ]

    # The prediction label for either a `BINARY` or `MULTICLASS` `MLModel`.
    predicted_label: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The prediction value for `REGRESSION` `MLModel`.
    predicted_value: float = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Provides the raw classification score corresponding to each label.
    predicted_scores: typing.Dict[str, float] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Provides any additional details regarding the prediction.
    details: typing.Dict["DetailsAttributes", str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PredictorNotMountedException(autoboto.ShapeBase):
    """
    The exception is thrown when a predict request is made to an unmounted
    `MLModel`.
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
class RDSDataSpec(autoboto.ShapeBase):
    """
    The data specification of an Amazon Relational Database Service (Amazon RDS)
    `DataSource`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_information",
                "DatabaseInformation",
                autoboto.TypeInfo(RDSDatabase),
            ),
            (
                "select_sql_query",
                "SelectSqlQuery",
                autoboto.TypeInfo(str),
            ),
            (
                "database_credentials",
                "DatabaseCredentials",
                autoboto.TypeInfo(RDSDatabaseCredentials),
            ),
            (
                "s3_staging_location",
                "S3StagingLocation",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_role",
                "ResourceRole",
                autoboto.TypeInfo(str),
            ),
            (
                "service_role",
                "ServiceRole",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_id",
                "SubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "data_rearrangement",
                "DataRearrangement",
                autoboto.TypeInfo(str),
            ),
            (
                "data_schema",
                "DataSchema",
                autoboto.TypeInfo(str),
            ),
            (
                "data_schema_uri",
                "DataSchemaUri",
                autoboto.TypeInfo(str),
            ),
        ]

    # Describes the `DatabaseName` and `InstanceIdentifier` of an Amazon RDS
    # database.
    database_information: "RDSDatabase" = dataclasses.field(
        default_factory=dict,
    )

    # The query that is used to retrieve the observation data for the
    # `DataSource`.
    select_sql_query: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS Identity and Access Management (IAM) credentials that are used
    # connect to the Amazon RDS database.
    database_credentials: "RDSDatabaseCredentials" = dataclasses.field(
        default_factory=dict,
    )

    # The Amazon S3 location for staging Amazon RDS data. The data retrieved from
    # Amazon RDS using `SelectSqlQuery` is stored in this location.
    s3_staging_location: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The role (DataPipelineDefaultResourceRole) assumed by an Amazon Elastic
    # Compute Cloud (Amazon EC2) instance to carry out the copy operation from
    # Amazon RDS to an Amazon S3 task. For more information, see [Role
    # templates](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-
    # iam-roles.html) for data pipelines.
    resource_role: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The role (DataPipelineDefaultRole) assumed by AWS Data Pipeline service to
    # monitor the progress of the copy task from Amazon RDS to Amazon S3. For
    # more information, see [Role
    # templates](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-
    # iam-roles.html) for data pipelines.
    service_role: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The subnet ID to be used to access a VPC-based RDS DB instance. This
    # attribute is used by Data Pipeline to carry out the copy task from Amazon
    # RDS to Amazon S3.
    subnet_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The security group IDs to be used to access a VPC-based RDS DB instance.
    # Ensure that there are appropriate ingress rules set up to allow access to
    # the RDS DB instance. This attribute is used by Data Pipeline to carry out
    # the copy operation from Amazon RDS to an Amazon S3 task.
    security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A JSON string that represents the splitting and rearrangement processing to
    # be applied to a `DataSource`. If the `DataRearrangement` parameter is not
    # provided, all of the input data is used to create the `Datasource`.

    # There are multiple parameters that control what data is used to create a
    # datasource:

    #   * **`percentBegin`**

    # Use `percentBegin` to indicate the beginning of the range of the data used
    # to create the Datasource. If you do not include `percentBegin` and
    # `percentEnd`, Amazon ML includes all of the data when creating the
    # datasource.

    #   * **`percentEnd`**

    # Use `percentEnd` to indicate the end of the range of the data used to
    # create the Datasource. If you do not include `percentBegin` and
    # `percentEnd`, Amazon ML includes all of the data when creating the
    # datasource.

    #   * **`complement`**

    # The `complement` parameter instructs Amazon ML to use the data that is not
    # included in the range of `percentBegin` to `percentEnd` to create a
    # datasource. The `complement` parameter is useful if you need to create
    # complementary datasources for training and evaluation. To create a
    # complementary datasource, use the same values for `percentBegin` and
    # `percentEnd`, along with the `complement` parameter.

    # For example, the following two datasources do not share any data, and can
    # be used to train and evaluate a model. The first datasource has 25 percent
    # of the data, and the second one has 75 percent of the data.

    # Datasource for evaluation: `{"splitting":{"percentBegin":0,
    # "percentEnd":25}}`

    # Datasource for training: `{"splitting":{"percentBegin":0, "percentEnd":25,
    # "complement":"true"}}`

    #   * **`strategy`**

    # To change how Amazon ML splits the data for a datasource, use the
    # `strategy` parameter.

    # The default value for the `strategy` parameter is `sequential`, meaning
    # that Amazon ML takes all of the data records between the `percentBegin` and
    # `percentEnd` parameters for the datasource, in the order that the records
    # appear in the input data.

    # The following two `DataRearrangement` lines are examples of sequentially
    # ordered training and evaluation datasources:

    # Datasource for evaluation: `{"splitting":{"percentBegin":70,
    # "percentEnd":100, "strategy":"sequential"}}`

    # Datasource for training: `{"splitting":{"percentBegin":70,
    # "percentEnd":100, "strategy":"sequential", "complement":"true"}}`

    # To randomly split the input data into the proportions indicated by the
    # percentBegin and percentEnd parameters, set the `strategy` parameter to
    # `random` and provide a string that is used as the seed value for the random
    # data splitting (for example, you can use the S3 path to your data as the
    # random seed string). If you choose the random split strategy, Amazon ML
    # assigns each row of data a pseudo-random number between 0 and 100, and then
    # selects the rows that have an assigned number between `percentBegin` and
    # `percentEnd`. Pseudo-random numbers are assigned using both the input seed
    # string value and the byte offset as a seed, so changing the data results in
    # a different split. Any existing ordering is preserved. The random splitting
    # strategy ensures that variables in the training and evaluation data are
    # distributed similarly. It is useful in the cases where the input data may
    # have an implicit sort order, which would otherwise result in training and
    # evaluation datasources containing non-similar data records.

    # The following two `DataRearrangement` lines are examples of non-
    # sequentially ordered training and evaluation datasources:

    # Datasource for evaluation: `{"splitting":{"percentBegin":70,
    # "percentEnd":100, "strategy":"random",
    # "randomSeed"="s3://my_s3_path/bucket/file.csv"}}`

    # Datasource for training: `{"splitting":{"percentBegin":70,
    # "percentEnd":100, "strategy":"random",
    # "randomSeed"="s3://my_s3_path/bucket/file.csv", "complement":"true"}}`
    data_rearrangement: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A JSON string that represents the schema for an Amazon RDS `DataSource`.
    # The `DataSchema` defines the structure of the observation data in the data
    # file(s) referenced in the `DataSource`.

    # A `DataSchema` is not required if you specify a `DataSchemaUri`

    # Define your `DataSchema` as a series of key-value pairs. `attributes` and
    # `excludedVariableNames` have an array of key-value pairs for their value.
    # Use the following format to define your `DataSchema`.

    # { "version": "1.0",

    # "recordAnnotationFieldName": "F1",

    # "recordWeightFieldName": "F2",

    # "targetFieldName": "F3",

    # "dataFormat": "CSV",

    # "dataFileContainsHeader": true,

    # "attributes": [

    # { "fieldName": "F1", "fieldType": "TEXT" }, { "fieldName": "F2",
    # "fieldType": "NUMERIC" }, { "fieldName": "F3", "fieldType": "CATEGORICAL"
    # }, { "fieldName": "F4", "fieldType": "NUMERIC" }, { "fieldName": "F5",
    # "fieldType": "CATEGORICAL" }, { "fieldName": "F6", "fieldType": "TEXT" }, {
    # "fieldName": "F7", "fieldType": "WEIGHTED_INT_SEQUENCE" }, { "fieldName":
    # "F8", "fieldType": "WEIGHTED_STRING_SEQUENCE" } ],

    # "excludedVariableNames": [ "F6" ] }
    data_schema: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon S3 location of the `DataSchema`.
    data_schema_uri: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RDSDatabase(autoboto.ShapeBase):
    """
    The database details of an Amazon RDS database.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_identifier",
                "InstanceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of an RDS DB instance.
    instance_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of a database hosted on an RDS DB instance.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RDSDatabaseCredentials(autoboto.ShapeBase):
    """
    The database credentials to connect to a database on an RDS DB instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "password",
                "Password",
                autoboto.TypeInfo(str),
            ),
        ]

    # The username to be used by Amazon ML to connect to database on an Amazon
    # RDS instance. The username should have sufficient permissions to execute an
    # `RDSSelectSqlQuery` query.
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The password to be used by Amazon ML to connect to a database on an RDS DB
    # instance. The password should have sufficient permissions to execute the
    # `RDSSelectQuery` query.
    password: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RDSMetadata(autoboto.ShapeBase):
    """
    The datasource details that are specific to Amazon RDS.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database",
                "Database",
                autoboto.TypeInfo(RDSDatabase),
            ),
            (
                "database_user_name",
                "DatabaseUserName",
                autoboto.TypeInfo(str),
            ),
            (
                "select_sql_query",
                "SelectSqlQuery",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_role",
                "ResourceRole",
                autoboto.TypeInfo(str),
            ),
            (
                "service_role",
                "ServiceRole",
                autoboto.TypeInfo(str),
            ),
            (
                "data_pipeline_id",
                "DataPipelineId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The database details required to connect to an Amazon RDS.
    database: "RDSDatabase" = dataclasses.field(default_factory=dict, )

    # The username to be used by Amazon ML to connect to database on an Amazon
    # RDS instance. The username should have sufficient permissions to execute an
    # `RDSSelectSqlQuery` query.
    database_user_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The SQL query that is supplied during CreateDataSourceFromRDS. Returns only
    # if `Verbose` is true in `GetDataSourceInput`.
    select_sql_query: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The role (DataPipelineDefaultResourceRole) assumed by an Amazon EC2
    # instance to carry out the copy task from Amazon RDS to Amazon S3. For more
    # information, see [Role
    # templates](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-
    # iam-roles.html) for data pipelines.
    resource_role: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The role (DataPipelineDefaultRole) assumed by the Data Pipeline service to
    # monitor the progress of the copy task from Amazon RDS to Amazon S3. For
    # more information, see [Role
    # templates](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-
    # iam-roles.html) for data pipelines.
    service_role: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the Data Pipeline instance that is used to carry to copy data
    # from Amazon RDS to Amazon S3. You can use the ID to find details about the
    # instance in the Data Pipeline console.
    data_pipeline_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RealtimeEndpointInfo(autoboto.ShapeBase):
    """
    Describes the real-time endpoint information for an `MLModel`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "peak_requests_per_second",
                "PeakRequestsPerSecond",
                autoboto.TypeInfo(int),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "endpoint_url",
                "EndpointUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_status",
                "EndpointStatus",
                autoboto.TypeInfo(RealtimeEndpointStatus),
            ),
        ]

    # The maximum processing rate for the real-time endpoint for `MLModel`,
    # measured in incoming requests per second.
    peak_requests_per_second: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time that the request to create the real-time endpoint for the
    # `MLModel` was received. The time is expressed in epoch time.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URI that specifies where to send real-time prediction requests for the
    # `MLModel`.

    # Note

    # The application must wait until the real-time endpoint is ready before
    # using this URI.
    endpoint_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The current status of the real-time endpoint for the `MLModel`. This
    # element can have one of the following values:

    #   * `NONE` \- Endpoint does not exist or was previously deleted.
    #   * `READY` \- Endpoint is ready to be used for real-time predictions.
    #   * `UPDATING` \- Updating/creating the endpoint.
    endpoint_status: "RealtimeEndpointStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class RealtimeEndpointStatus(Enum):
    NONE = "NONE"
    READY = "READY"
    UPDATING = "UPDATING"
    FAILED = "FAILED"


@dataclasses.dataclass
class RedshiftDataSpec(autoboto.ShapeBase):
    """
    Describes the data specification of an Amazon Redshift `DataSource`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_information",
                "DatabaseInformation",
                autoboto.TypeInfo(RedshiftDatabase),
            ),
            (
                "select_sql_query",
                "SelectSqlQuery",
                autoboto.TypeInfo(str),
            ),
            (
                "database_credentials",
                "DatabaseCredentials",
                autoboto.TypeInfo(RedshiftDatabaseCredentials),
            ),
            (
                "s3_staging_location",
                "S3StagingLocation",
                autoboto.TypeInfo(str),
            ),
            (
                "data_rearrangement",
                "DataRearrangement",
                autoboto.TypeInfo(str),
            ),
            (
                "data_schema",
                "DataSchema",
                autoboto.TypeInfo(str),
            ),
            (
                "data_schema_uri",
                "DataSchemaUri",
                autoboto.TypeInfo(str),
            ),
        ]

    # Describes the `DatabaseName` and `ClusterIdentifier` for an Amazon Redshift
    # `DataSource`.
    database_information: "RedshiftDatabase" = dataclasses.field(
        default_factory=dict,
    )

    # Describes the SQL Query to execute on an Amazon Redshift database for an
    # Amazon Redshift `DataSource`.
    select_sql_query: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Describes AWS Identity and Access Management (IAM) credentials that are
    # used connect to the Amazon Redshift database.
    database_credentials: "RedshiftDatabaseCredentials" = dataclasses.field(
        default_factory=dict,
    )

    # Describes an Amazon S3 location to store the result set of the
    # `SelectSqlQuery` query.
    s3_staging_location: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A JSON string that represents the splitting and rearrangement processing to
    # be applied to a `DataSource`. If the `DataRearrangement` parameter is not
    # provided, all of the input data is used to create the `Datasource`.

    # There are multiple parameters that control what data is used to create a
    # datasource:

    #   * **`percentBegin`**

    # Use `percentBegin` to indicate the beginning of the range of the data used
    # to create the Datasource. If you do not include `percentBegin` and
    # `percentEnd`, Amazon ML includes all of the data when creating the
    # datasource.

    #   * **`percentEnd`**

    # Use `percentEnd` to indicate the end of the range of the data used to
    # create the Datasource. If you do not include `percentBegin` and
    # `percentEnd`, Amazon ML includes all of the data when creating the
    # datasource.

    #   * **`complement`**

    # The `complement` parameter instructs Amazon ML to use the data that is not
    # included in the range of `percentBegin` to `percentEnd` to create a
    # datasource. The `complement` parameter is useful if you need to create
    # complementary datasources for training and evaluation. To create a
    # complementary datasource, use the same values for `percentBegin` and
    # `percentEnd`, along with the `complement` parameter.

    # For example, the following two datasources do not share any data, and can
    # be used to train and evaluate a model. The first datasource has 25 percent
    # of the data, and the second one has 75 percent of the data.

    # Datasource for evaluation: `{"splitting":{"percentBegin":0,
    # "percentEnd":25}}`

    # Datasource for training: `{"splitting":{"percentBegin":0, "percentEnd":25,
    # "complement":"true"}}`

    #   * **`strategy`**

    # To change how Amazon ML splits the data for a datasource, use the
    # `strategy` parameter.

    # The default value for the `strategy` parameter is `sequential`, meaning
    # that Amazon ML takes all of the data records between the `percentBegin` and
    # `percentEnd` parameters for the datasource, in the order that the records
    # appear in the input data.

    # The following two `DataRearrangement` lines are examples of sequentially
    # ordered training and evaluation datasources:

    # Datasource for evaluation: `{"splitting":{"percentBegin":70,
    # "percentEnd":100, "strategy":"sequential"}}`

    # Datasource for training: `{"splitting":{"percentBegin":70,
    # "percentEnd":100, "strategy":"sequential", "complement":"true"}}`

    # To randomly split the input data into the proportions indicated by the
    # percentBegin and percentEnd parameters, set the `strategy` parameter to
    # `random` and provide a string that is used as the seed value for the random
    # data splitting (for example, you can use the S3 path to your data as the
    # random seed string). If you choose the random split strategy, Amazon ML
    # assigns each row of data a pseudo-random number between 0 and 100, and then
    # selects the rows that have an assigned number between `percentBegin` and
    # `percentEnd`. Pseudo-random numbers are assigned using both the input seed
    # string value and the byte offset as a seed, so changing the data results in
    # a different split. Any existing ordering is preserved. The random splitting
    # strategy ensures that variables in the training and evaluation data are
    # distributed similarly. It is useful in the cases where the input data may
    # have an implicit sort order, which would otherwise result in training and
    # evaluation datasources containing non-similar data records.

    # The following two `DataRearrangement` lines are examples of non-
    # sequentially ordered training and evaluation datasources:

    # Datasource for evaluation: `{"splitting":{"percentBegin":70,
    # "percentEnd":100, "strategy":"random",
    # "randomSeed"="s3://my_s3_path/bucket/file.csv"}}`

    # Datasource for training: `{"splitting":{"percentBegin":70,
    # "percentEnd":100, "strategy":"random",
    # "randomSeed"="s3://my_s3_path/bucket/file.csv", "complement":"true"}}`
    data_rearrangement: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A JSON string that represents the schema for an Amazon Redshift
    # `DataSource`. The `DataSchema` defines the structure of the observation
    # data in the data file(s) referenced in the `DataSource`.

    # A `DataSchema` is not required if you specify a `DataSchemaUri`.

    # Define your `DataSchema` as a series of key-value pairs. `attributes` and
    # `excludedVariableNames` have an array of key-value pairs for their value.
    # Use the following format to define your `DataSchema`.

    # { "version": "1.0",

    # "recordAnnotationFieldName": "F1",

    # "recordWeightFieldName": "F2",

    # "targetFieldName": "F3",

    # "dataFormat": "CSV",

    # "dataFileContainsHeader": true,

    # "attributes": [

    # { "fieldName": "F1", "fieldType": "TEXT" }, { "fieldName": "F2",
    # "fieldType": "NUMERIC" }, { "fieldName": "F3", "fieldType": "CATEGORICAL"
    # }, { "fieldName": "F4", "fieldType": "NUMERIC" }, { "fieldName": "F5",
    # "fieldType": "CATEGORICAL" }, { "fieldName": "F6", "fieldType": "TEXT" }, {
    # "fieldName": "F7", "fieldType": "WEIGHTED_INT_SEQUENCE" }, { "fieldName":
    # "F8", "fieldType": "WEIGHTED_STRING_SEQUENCE" } ],

    # "excludedVariableNames": [ "F6" ] }
    data_schema: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Describes the schema location for an Amazon Redshift `DataSource`.
    data_schema_uri: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RedshiftDatabase(autoboto.ShapeBase):
    """
    Describes the database details required to connect to an Amazon Redshift
    database.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "cluster_identifier",
                "ClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of a database hosted on an Amazon Redshift cluster.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of an Amazon Redshift cluster.
    cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RedshiftDatabaseCredentials(autoboto.ShapeBase):
    """
    Describes the database credentials for connecting to a database on an Amazon
    Redshift cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "password",
                "Password",
                autoboto.TypeInfo(str),
            ),
        ]

    # A username to be used by Amazon Machine Learning (Amazon ML)to connect to a
    # database on an Amazon Redshift cluster. The username should have sufficient
    # permissions to execute the `RedshiftSelectSqlQuery` query. The username
    # should be valid for an Amazon Redshift
    # [USER](http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html).
    username: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A password to be used by Amazon ML to connect to a database on an Amazon
    # Redshift cluster. The password should have sufficient permissions to
    # execute a `RedshiftSelectSqlQuery` query. The password should be valid for
    # an Amazon Redshift
    # [USER](http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html).
    password: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RedshiftMetadata(autoboto.ShapeBase):
    """
    Describes the `DataSource` details specific to Amazon Redshift.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "redshift_database",
                "RedshiftDatabase",
                autoboto.TypeInfo(RedshiftDatabase),
            ),
            (
                "database_user_name",
                "DatabaseUserName",
                autoboto.TypeInfo(str),
            ),
            (
                "select_sql_query",
                "SelectSqlQuery",
                autoboto.TypeInfo(str),
            ),
        ]

    # Describes the database details required to connect to an Amazon Redshift
    # database.
    redshift_database: "RedshiftDatabase" = dataclasses.field(
        default_factory=dict,
    )

    # A username to be used by Amazon Machine Learning (Amazon ML)to connect to a
    # database on an Amazon Redshift cluster. The username should have sufficient
    # permissions to execute the `RedshiftSelectSqlQuery` query. The username
    # should be valid for an Amazon Redshift
    # [USER](http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html).
    database_user_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The SQL query that is specified during CreateDataSourceFromRedshift.
    # Returns only if `Verbose` is true in GetDataSourceInput.
    select_sql_query: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    A specified resource cannot be located.
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
                "code",
                "code",
                autoboto.TypeInfo(int),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
    code: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class S3DataSpec(autoboto.ShapeBase):
    """
    Describes the data specification of a `DataSource`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_location_s3",
                "DataLocationS3",
                autoboto.TypeInfo(str),
            ),
            (
                "data_rearrangement",
                "DataRearrangement",
                autoboto.TypeInfo(str),
            ),
            (
                "data_schema",
                "DataSchema",
                autoboto.TypeInfo(str),
            ),
            (
                "data_schema_location_s3",
                "DataSchemaLocationS3",
                autoboto.TypeInfo(str),
            ),
        ]

    # The location of the data file(s) used by a `DataSource`. The URI specifies
    # a data file or an Amazon Simple Storage Service (Amazon S3) directory or
    # bucket containing data files.
    data_location_s3: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A JSON string that represents the splitting and rearrangement processing to
    # be applied to a `DataSource`. If the `DataRearrangement` parameter is not
    # provided, all of the input data is used to create the `Datasource`.

    # There are multiple parameters that control what data is used to create a
    # datasource:

    #   * **`percentBegin`**

    # Use `percentBegin` to indicate the beginning of the range of the data used
    # to create the Datasource. If you do not include `percentBegin` and
    # `percentEnd`, Amazon ML includes all of the data when creating the
    # datasource.

    #   * **`percentEnd`**

    # Use `percentEnd` to indicate the end of the range of the data used to
    # create the Datasource. If you do not include `percentBegin` and
    # `percentEnd`, Amazon ML includes all of the data when creating the
    # datasource.

    #   * **`complement`**

    # The `complement` parameter instructs Amazon ML to use the data that is not
    # included in the range of `percentBegin` to `percentEnd` to create a
    # datasource. The `complement` parameter is useful if you need to create
    # complementary datasources for training and evaluation. To create a
    # complementary datasource, use the same values for `percentBegin` and
    # `percentEnd`, along with the `complement` parameter.

    # For example, the following two datasources do not share any data, and can
    # be used to train and evaluate a model. The first datasource has 25 percent
    # of the data, and the second one has 75 percent of the data.

    # Datasource for evaluation: `{"splitting":{"percentBegin":0,
    # "percentEnd":25}}`

    # Datasource for training: `{"splitting":{"percentBegin":0, "percentEnd":25,
    # "complement":"true"}}`

    #   * **`strategy`**

    # To change how Amazon ML splits the data for a datasource, use the
    # `strategy` parameter.

    # The default value for the `strategy` parameter is `sequential`, meaning
    # that Amazon ML takes all of the data records between the `percentBegin` and
    # `percentEnd` parameters for the datasource, in the order that the records
    # appear in the input data.

    # The following two `DataRearrangement` lines are examples of sequentially
    # ordered training and evaluation datasources:

    # Datasource for evaluation: `{"splitting":{"percentBegin":70,
    # "percentEnd":100, "strategy":"sequential"}}`

    # Datasource for training: `{"splitting":{"percentBegin":70,
    # "percentEnd":100, "strategy":"sequential", "complement":"true"}}`

    # To randomly split the input data into the proportions indicated by the
    # percentBegin and percentEnd parameters, set the `strategy` parameter to
    # `random` and provide a string that is used as the seed value for the random
    # data splitting (for example, you can use the S3 path to your data as the
    # random seed string). If you choose the random split strategy, Amazon ML
    # assigns each row of data a pseudo-random number between 0 and 100, and then
    # selects the rows that have an assigned number between `percentBegin` and
    # `percentEnd`. Pseudo-random numbers are assigned using both the input seed
    # string value and the byte offset as a seed, so changing the data results in
    # a different split. Any existing ordering is preserved. The random splitting
    # strategy ensures that variables in the training and evaluation data are
    # distributed similarly. It is useful in the cases where the input data may
    # have an implicit sort order, which would otherwise result in training and
    # evaluation datasources containing non-similar data records.

    # The following two `DataRearrangement` lines are examples of non-
    # sequentially ordered training and evaluation datasources:

    # Datasource for evaluation: `{"splitting":{"percentBegin":70,
    # "percentEnd":100, "strategy":"random",
    # "randomSeed"="s3://my_s3_path/bucket/file.csv"}}`

    # Datasource for training: `{"splitting":{"percentBegin":70,
    # "percentEnd":100, "strategy":"random",
    # "randomSeed"="s3://my_s3_path/bucket/file.csv", "complement":"true"}}`
    data_rearrangement: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A JSON string that represents the schema for an Amazon S3 `DataSource`. The
    # `DataSchema` defines the structure of the observation data in the data
    # file(s) referenced in the `DataSource`.

    # You must provide either the `DataSchema` or the `DataSchemaLocationS3`.

    # Define your `DataSchema` as a series of key-value pairs. `attributes` and
    # `excludedVariableNames` have an array of key-value pairs for their value.
    # Use the following format to define your `DataSchema`.

    # { "version": "1.0",

    # "recordAnnotationFieldName": "F1",

    # "recordWeightFieldName": "F2",

    # "targetFieldName": "F3",

    # "dataFormat": "CSV",

    # "dataFileContainsHeader": true,

    # "attributes": [

    # { "fieldName": "F1", "fieldType": "TEXT" }, { "fieldName": "F2",
    # "fieldType": "NUMERIC" }, { "fieldName": "F3", "fieldType": "CATEGORICAL"
    # }, { "fieldName": "F4", "fieldType": "NUMERIC" }, { "fieldName": "F5",
    # "fieldType": "CATEGORICAL" }, { "fieldName": "F6", "fieldType": "TEXT" }, {
    # "fieldName": "F7", "fieldType": "WEIGHTED_INT_SEQUENCE" }, { "fieldName":
    # "F8", "fieldType": "WEIGHTED_STRING_SEQUENCE" } ],

    # "excludedVariableNames": [ "F6" ] }
    data_schema: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Describes the schema location in Amazon S3. You must provide either the
    # `DataSchema` or the `DataSchemaLocationS3`.
    data_schema_location_s3: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class SortOrder(Enum):
    """
    The sort order specified in a listing condition. Possible values include the
    following:

      * `asc` \- Present the information in ascending order (from A-Z).
      * `dsc` \- Present the information in descending order (from Z-A).
    """
    asc = "asc"
    dsc = "dsc"


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    """
    A custom key-value pair associated with an ML object, such as an ML model.
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

    # A unique identifier for the tag. Valid characters include Unicode letters,
    # digits, white space, _, ., /, =, +, -, %, and @.
    key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An optional string, typically used to describe or define the tag. Valid
    # characters include Unicode letters, digits, white space, _, ., /, =, +, -,
    # %, and @.
    value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TagLimitExceededException(autoboto.ShapeBase):
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


class TaggableResourceType(Enum):
    BatchPrediction = "BatchPrediction"
    DataSource = "DataSource"
    Evaluation = "Evaluation"
    MLModel = "MLModel"


@dataclasses.dataclass
class UpdateBatchPredictionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "batch_prediction_id",
                "BatchPredictionId",
                autoboto.TypeInfo(str),
            ),
            (
                "batch_prediction_name",
                "BatchPredictionName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID assigned to the `BatchPrediction` during creation.
    batch_prediction_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A new user-supplied name or description of the `BatchPrediction`.
    batch_prediction_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateBatchPredictionOutput(autoboto.ShapeBase):
    """
    Represents the output of an `UpdateBatchPrediction` operation.

    You can see the updated content by using the `GetBatchPrediction` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "batch_prediction_id",
                "BatchPredictionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID assigned to the `BatchPrediction` during creation. This value should
    # be identical to the value of the `BatchPredictionId` in the request.
    batch_prediction_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateDataSourceInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source_id",
                "DataSourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "data_source_name",
                "DataSourceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID assigned to the `DataSource` during creation.
    data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A new user-supplied name or description of the `DataSource` that will
    # replace the current description.
    data_source_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateDataSourceOutput(autoboto.ShapeBase):
    """
    Represents the output of an `UpdateDataSource` operation.

    You can see the updated content by using the `GetBatchPrediction` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source_id",
                "DataSourceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID assigned to the `DataSource` during creation. This value should be
    # identical to the value of the `DataSourceID` in the request.
    data_source_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateEvaluationInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "evaluation_id",
                "EvaluationId",
                autoboto.TypeInfo(str),
            ),
            (
                "evaluation_name",
                "EvaluationName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID assigned to the `Evaluation` during creation.
    evaluation_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A new user-supplied name or description of the `Evaluation` that will
    # replace the current content.
    evaluation_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateEvaluationOutput(autoboto.ShapeBase):
    """
    Represents the output of an `UpdateEvaluation` operation.

    You can see the updated content by using the `GetEvaluation` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "evaluation_id",
                "EvaluationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID assigned to the `Evaluation` during creation. This value should be
    # identical to the value of the `Evaluation` in the request.
    evaluation_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateMLModelInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
            (
                "ml_model_name",
                "MLModelName",
                autoboto.TypeInfo(str),
            ),
            (
                "score_threshold",
                "ScoreThreshold",
                autoboto.TypeInfo(float),
            ),
        ]

    # The ID assigned to the `MLModel` during creation.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A user-supplied name or description of the `MLModel`.
    ml_model_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The `ScoreThreshold` used in binary classification `MLModel` that marks the
    # boundary between a positive prediction and a negative prediction.

    # Output values greater than or equal to the `ScoreThreshold` receive a
    # positive result from the `MLModel`, such as `true`. Output values less than
    # the `ScoreThreshold` receive a negative response from the `MLModel`, such
    # as `false`.
    score_threshold: float = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateMLModelOutput(autoboto.ShapeBase):
    """
    Represents the output of an `UpdateMLModel` operation.

    You can see the updated content by using the `GetMLModel` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ml_model_id",
                "MLModelId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID assigned to the `MLModel` during creation. This value should be
    # identical to the value of the `MLModelID` in the request.
    ml_model_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
