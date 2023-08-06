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
                "resource_arn",
                "ResourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource that you want to tag.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of `Tag` objects. Each tag is a key-value pair. Only the `key`
    # parameter is required. If you don't specify a value, Amazon SageMaker sets
    # the value to an empty string.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class AddTagsOutput(autoboto.OutputShapeBase):
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
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of tags associated with the Amazon SageMaker resource.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class AlgorithmSpecification(autoboto.ShapeBase):
    """
    Specifies the training algorithm to use in a
    [CreateTrainingJob](http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateTrainingJob.html)
    request.

    For more information about algorithms provided by Amazon SageMaker, see
    [Algorithms](http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html). For
    information about using your own algorithms, see your-algorithms.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "training_image",
                "TrainingImage",
                autoboto.TypeInfo(str),
            ),
            (
                "training_input_mode",
                "TrainingInputMode",
                autoboto.TypeInfo(TrainingInputMode),
            ),
        ]

    # The registry path of the Docker image that contains the training algorithm.
    # For information about docker registry paths for built-in algorithms, see
    # sagemaker-algo-docker-registry-paths.
    training_image: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The input mode that the algorithm supports. For the input modes that Amazon
    # SageMaker algorithms support, see
    # [Algorithms](http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html). If
    # an algorithm supports the `File` input mode, Amazon SageMaker downloads the
    # training data from S3 to the provisioned ML storage Volume, and mounts the
    # directory to docker volume for training container. If an algorithm supports
    # the `Pipe` input mode, Amazon SageMaker streams data directly from S3 to
    # the container.

    # In File mode, make sure you provision ML storage volume with sufficient
    # capacity to accommodate the data download from S3. In addition to the
    # training data, the ML storage volume also stores the output model. The
    # algorithm container use ML storage volume to also store intermediate
    # information, if any.

    # For distributed algorithms using File mode, training data is distributed
    # uniformly, and your training duration is predictable if the input data
    # objects size is approximately same. Amazon SageMaker does not split the
    # files any further for model training. If the object sizes are skewed,
    # training won't be optimal as the data distribution is also skewed where one
    # host in a training cluster is overloaded, thus becoming bottleneck in
    # training.
    training_input_mode: "TrainingInputMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class AssemblyType(Enum):
    NONE = "None"
    LINE = "Line"


class BatchStrategy(Enum):
    MultiRecord = "MultiRecord"
    SingleRecord = "SingleRecord"


@dataclasses.dataclass
class CategoricalParameterRange(autoboto.ShapeBase):
    """
    A list of categorical hyperparameters to tune.
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
                "values",
                "Values",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the categorical hyperparameter to tune.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of the categories for the hyperparameter.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class Channel(autoboto.ShapeBase):
    """
    A channel is a named input source that training algorithms can consume.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "ChannelName",
                autoboto.TypeInfo(str),
            ),
            (
                "data_source",
                "DataSource",
                autoboto.TypeInfo(DataSource),
            ),
            (
                "content_type",
                "ContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "compression_type",
                "CompressionType",
                autoboto.TypeInfo(CompressionType),
            ),
            (
                "record_wrapper_type",
                "RecordWrapperType",
                autoboto.TypeInfo(RecordWrapper),
            ),
        ]

    # The name of the channel.
    channel_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The location of the channel data.
    data_source: "DataSource" = dataclasses.field(default_factory=dict, )

    # The MIME type of the data.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If training data is compressed, the compression type. The default value is
    # `None`. `CompressionType` is used only in Pipe input mode. In File mode,
    # leave this field unset or set it to None.
    compression_type: "CompressionType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specify RecordIO as the value when input data is in raw format but the
    # training algorithm requires the RecordIO format, in which case, Amazon
    # SageMaker wraps each individual S3 object in a RecordIO record. If the
    # input data is already in RecordIO format, you don't need to set this
    # attribute. For more information, see [Create a Dataset Using
    # RecordIO](https://mxnet.incubator.apache.org/architecture/note_data_loading.html#data-
    # format).

    # In FILE mode, leave this field unset or set it to None.
    record_wrapper_type: "RecordWrapper" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class CompressionType(Enum):
    NONE = "None"
    GZIP = "Gzip"


@dataclasses.dataclass
class ContainerDefinition(autoboto.ShapeBase):
    """
    Describes the container, as part of model definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image",
                "Image",
                autoboto.TypeInfo(str),
            ),
            (
                "container_hostname",
                "ContainerHostname",
                autoboto.TypeInfo(str),
            ),
            (
                "model_data_url",
                "ModelDataUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "environment",
                "Environment",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The Amazon EC2 Container Registry (Amazon ECR) path where inference code is
    # stored. If you are using your own custom algorithm instead of an algorithm
    # provided by Amazon SageMaker, the inference code must meet Amazon SageMaker
    # requirements. Amazon SageMaker supports both `registry/repository[:tag]`
    # and `registry/repository[@digest]` image path formats. For more
    # information, see [Using Your Own Algorithms with Amazon
    # SageMaker](http://docs.aws.amazon.com/sagemaker/latest/dg/your-
    # algorithms.html)
    image: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The DNS host name for the container after Amazon SageMaker deploys it.
    container_hostname: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The S3 path where the model artifacts, which result from model training,
    # are stored. This path must point to a single gzip compressed tar archive
    # (.tar.gz suffix).

    # If you provide a value for this parameter, Amazon SageMaker uses AWS
    # Security Token Service to download model artifacts from the S3 path you
    # provide. AWS STS is activated in your IAM user account by default. If you
    # previously deactivated AWS STS for a region, you need to reactivate AWS STS
    # for that region. For more information, see [Activating and Deactivating AWS
    # STS i an AWS
    # Region](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-
    # regions.html) in the _AWS Identity and Access Management User Guide_.
    model_data_url: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The environment variables to set in the Docker container. Each key and
    # value in the `Environment` string to string map can have length of up to
    # 1024. We support up to 16 entries in the map.
    environment: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ContinuousParameterRange(autoboto.ShapeBase):
    """
    A list of continuous hyperparameters to tune.
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
                "min_value",
                "MinValue",
                autoboto.TypeInfo(str),
            ),
            (
                "max_value",
                "MaxValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the continuous hyperparameter to tune.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The minimum value for the hyperparameter. The tuning job uses floating-
    # point values between this value and `MaxValue`for tuning.
    min_value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum value for the hyperparameter. The tuning job uses floating-
    # point values between `MinValue` value and this value for tuning.
    max_value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateEndpointConfigInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_config_name",
                "EndpointConfigName",
                autoboto.TypeInfo(str),
            ),
            (
                "production_variants",
                "ProductionVariants",
                autoboto.TypeInfo(typing.List[ProductionVariant]),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the endpoint configuration. You specify this name in a
    # [CreateEndpoint](http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html)
    # request.
    endpoint_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of `ProductionVariant` objects, one for each model that you want
    # to host at this endpoint.
    production_variants: typing.List["ProductionVariant"] = dataclasses.field(
        default_factory=list,
    )

    # An array of key-value pairs. For more information, see [Using Cost
    # Allocation
    # Tags](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-
    # alloc-tags.html#allocation-what) in the _AWS Billing and Cost Management
    # User Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # The Amazon Resource Name (ARN) of a AWS Key Management Service key that
    # Amazon SageMaker uses to encrypt data on the storage volume attached to the
    # ML compute instance that hosts the endpoint.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateEndpointConfigOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_config_arn",
                "EndpointConfigArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the endpoint configuration.
    endpoint_config_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateEndpointInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_config_name",
                "EndpointConfigName",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the endpoint. The name must be unique within an AWS Region in
    # your AWS account.
    endpoint_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of an endpoint configuration. For more information, see
    # [CreateEndpointConfig](http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpointConfig.html).
    endpoint_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of key-value pairs. For more information, see [Using Cost
    # Allocation
    # Tags](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-
    # alloc-tags.html#allocation-what)in the _AWS Billing and Cost Management
    # User Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateEndpointOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_arn",
                "EndpointArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the endpoint.
    endpoint_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateHyperParameterTuningJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hyper_parameter_tuning_job_name",
                "HyperParameterTuningJobName",
                autoboto.TypeInfo(str),
            ),
            (
                "hyper_parameter_tuning_job_config",
                "HyperParameterTuningJobConfig",
                autoboto.TypeInfo(HyperParameterTuningJobConfig),
            ),
            (
                "training_job_definition",
                "TrainingJobDefinition",
                autoboto.TypeInfo(HyperParameterTrainingJobDefinition),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the tuning job. This name is the prefix for the names of all
    # training jobs that this tuning job launches. The name must be unique within
    # the same AWS account and AWS Region. Names are not case sensitive, and must
    # be between 1-32 characters.
    hyper_parameter_tuning_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The HyperParameterTuningJobConfig object that describes the tuning job,
    # including the search strategy, metric used to evaluate training jobs,
    # ranges of parameters to search, and resource limits for the tuning job.
    hyper_parameter_tuning_job_config: "HyperParameterTuningJobConfig" = dataclasses.field(
        default_factory=dict,
    )

    # The HyperParameterTrainingJobDefinition object that describes the training
    # jobs that this tuning job launches, including static hyperparameters, input
    # data configuration, output data configuration, resource configuration, and
    # stopping condition.
    training_job_definition: "HyperParameterTrainingJobDefinition" = dataclasses.field(
        default_factory=dict,
    )

    # An array of key-value pairs. You can use tags to categorize your AWS
    # resources in different ways, for example, by purpose, owner, or
    # environment. For more information, see [Using Cost Allocation
    # Tags](http://docs.aws.amazon.com//awsaccountbilling/latest/aboutv2/cost-
    # alloc-tags.html#allocation-what) in the _AWS Billing and Cost Management
    # User Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateHyperParameterTuningJobResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hyper_parameter_tuning_job_arn",
                "HyperParameterTuningJobArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the tuning job.
    hyper_parameter_tuning_job_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateModelInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "model_name",
                "ModelName",
                autoboto.TypeInfo(str),
            ),
            (
                "primary_container",
                "PrimaryContainer",
                autoboto.TypeInfo(ContainerDefinition),
            ),
            (
                "execution_role_arn",
                "ExecutionRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "vpc_config",
                "VpcConfig",
                autoboto.TypeInfo(VpcConfig),
            ),
        ]

    # The name of the new model.
    model_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The location of the primary docker image containing inference code,
    # associated artifacts, and custom environment map that the inference code
    # uses when the model is deployed for predictions.
    primary_container: "ContainerDefinition" = dataclasses.field(
        default_factory=dict,
    )

    # The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker can
    # assume to access model artifacts and docker image for deployment on ML
    # compute instances or for batch transform jobs. Deploying on ML compute
    # instances is part of model hosting. For more information, see [Amazon
    # SageMaker Roles](http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-
    # roles.html).

    # To be able to pass this role to Amazon SageMaker, the caller of this API
    # must have the `iam:PassRole` permission.
    execution_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of key-value pairs. For more information, see [Using Cost
    # Allocation
    # Tags](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-
    # alloc-tags.html#allocation-what) in the _AWS Billing and Cost Management
    # User Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # A VpcConfig object that specifies the VPC that you want your model to
    # connect to. Control access to and from your model container by configuring
    # the VPC. `VpcConfig` is currently used in hosting services but not in batch
    # transform. For more information, see host-vpc.
    vpc_config: "VpcConfig" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateModelOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "model_arn",
                "ModelArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of the model created in Amazon SageMaker.
    model_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateNotebookInstanceInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                autoboto.TypeInfo(InstanceType),
            ),
            (
                "role_arn",
                "RoleArn",
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
                "kms_key_id",
                "KmsKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "lifecycle_config_name",
                "LifecycleConfigName",
                autoboto.TypeInfo(str),
            ),
            (
                "direct_internet_access",
                "DirectInternetAccess",
                autoboto.TypeInfo(DirectInternetAccess),
            ),
        ]

    # The name of the new notebook instance.
    notebook_instance_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of ML compute instance to launch for the notebook instance.
    instance_type: "InstanceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When you send any requests to AWS resources from the notebook instance,
    # Amazon SageMaker assumes this role to perform tasks on your behalf. You
    # must grant this role necessary permissions so Amazon SageMaker can perform
    # these tasks. The policy must allow the Amazon SageMaker service principal
    # (sagemaker.amazonaws.com) permissions to assume this role. For more
    # information, see [Amazon SageMaker
    # Roles](http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-
    # roles.html).

    # To be able to pass this role to Amazon SageMaker, the caller of this API
    # must have the `iam:PassRole` permission.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the subnet in a VPC to which you would like to have a
    # connectivity from your ML compute instance.
    subnet_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The VPC security group IDs, in the form sg-xxxxxxxx. The security groups
    # must be for the same VPC as specified in the subnet.
    security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # If you provide a AWS KMS key ID, Amazon SageMaker uses it to encrypt data
    # at rest on the ML storage volume that is attached to your notebook
    # instance.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of tags to associate with the notebook instance. You can add tags
    # later by using the `CreateTags` API.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # The name of a lifecycle configuration to associate with the notebook
    # instance. For information about lifestyle configurations, see notebook-
    # lifecycle-config.
    lifecycle_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Sets whether Amazon SageMaker provides internet access to the notebook
    # instance. If you set this to `Disabled` this notebook instance will be able
    # to access resources only in your VPC, and will not be able to connect to
    # Amazon SageMaker training and endpoint services unless your configure a NAT
    # Gateway in your VPC.

    # For more information, see appendix-notebook-and-internet-access. You can
    # set the value of this parameter to `Disabled` only if you set a value for
    # the `SubnetId` parameter.
    direct_internet_access: "DirectInternetAccess" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateNotebookInstanceLifecycleConfigInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_lifecycle_config_name",
                "NotebookInstanceLifecycleConfigName",
                autoboto.TypeInfo(str),
            ),
            (
                "on_create",
                "OnCreate",
                autoboto.TypeInfo(typing.List[NotebookInstanceLifecycleHook]),
            ),
            (
                "on_start",
                "OnStart",
                autoboto.TypeInfo(typing.List[NotebookInstanceLifecycleHook]),
            ),
        ]

    # The name of the lifecycle configuration.
    notebook_instance_lifecycle_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A shell script that runs only once, when you create a notebook instance.
    on_create: typing.List["NotebookInstanceLifecycleHook"] = dataclasses.field(
        default_factory=list,
    )

    # A shell script that runs every time you start a notebook instance,
    # including when you create the notebook instance.
    on_start: typing.List["NotebookInstanceLifecycleHook"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateNotebookInstanceLifecycleConfigOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "notebook_instance_lifecycle_config_arn",
                "NotebookInstanceLifecycleConfigArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the lifecycle configuration.
    notebook_instance_lifecycle_config_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateNotebookInstanceOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "notebook_instance_arn",
                "NotebookInstanceArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the notebook instance.
    notebook_instance_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePresignedNotebookInstanceUrlInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                autoboto.TypeInfo(str),
            ),
            (
                "session_expiration_duration_in_seconds",
                "SessionExpirationDurationInSeconds",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the notebook instance.
    notebook_instance_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The duration of the session, in seconds. The default is 12 hours.
    session_expiration_duration_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePresignedNotebookInstanceUrlOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "authorized_url",
                "AuthorizedUrl",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A JSON object that contains the URL string.
    authorized_url: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateTrainingJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "training_job_name",
                "TrainingJobName",
                autoboto.TypeInfo(str),
            ),
            (
                "algorithm_specification",
                "AlgorithmSpecification",
                autoboto.TypeInfo(AlgorithmSpecification),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "input_data_config",
                "InputDataConfig",
                autoboto.TypeInfo(typing.List[Channel]),
            ),
            (
                "output_data_config",
                "OutputDataConfig",
                autoboto.TypeInfo(OutputDataConfig),
            ),
            (
                "resource_config",
                "ResourceConfig",
                autoboto.TypeInfo(ResourceConfig),
            ),
            (
                "stopping_condition",
                "StoppingCondition",
                autoboto.TypeInfo(StoppingCondition),
            ),
            (
                "hyper_parameters",
                "HyperParameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "vpc_config",
                "VpcConfig",
                autoboto.TypeInfo(VpcConfig),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the training job. The name must be unique within an AWS Region
    # in an AWS account.
    training_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The registry path of the Docker image that contains the training algorithm
    # and algorithm-specific metadata, including the input mode. For more
    # information about algorithms provided by Amazon SageMaker, see
    # [Algorithms](http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html).
    # For information about providing your own algorithms, see your-algorithms.
    algorithm_specification: "AlgorithmSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can
    # assume to perform tasks on your behalf.

    # During model training, Amazon SageMaker needs your permission to read input
    # data from an S3 bucket, download a Docker image that contains training
    # code, write model artifacts to an S3 bucket, write logs to Amazon
    # CloudWatch Logs, and publish metrics to Amazon CloudWatch. You grant
    # permissions for all of these tasks to an IAM role. For more information,
    # see [Amazon SageMaker
    # Roles](http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-
    # roles.html).

    # To be able to pass this role to Amazon SageMaker, the caller of this API
    # must have the `iam:PassRole` permission.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of `Channel` objects. Each channel is a named input source.
    # `InputDataConfig` describes the input data and its location.

    # Algorithms can accept input data from one or more channels. For example, an
    # algorithm might have two channels of input data, `training_data` and
    # `validation_data`. The configuration for each channel provides the S3
    # location where the input data is stored. It also provides information about
    # the stored data: the MIME type, compression method, and whether the data is
    # wrapped in RecordIO format.

    # Depending on the input mode that the algorithm supports, Amazon SageMaker
    # either copies input data files from an S3 bucket to a local directory in
    # the Docker container, or makes it available as input streams.
    input_data_config: typing.List["Channel"] = dataclasses.field(
        default_factory=list,
    )

    # Specifies the path to the S3 bucket where you want to store model
    # artifacts. Amazon SageMaker creates subfolders for the artifacts.
    output_data_config: "OutputDataConfig" = dataclasses.field(
        default_factory=dict,
    )

    # The resources, including the ML compute instances and ML storage volumes,
    # to use for model training.

    # ML storage volumes store model artifacts and incremental states. Training
    # algorithms might also use ML storage volumes for scratch space. If you want
    # Amazon SageMaker to use the ML storage volume to store the training data,
    # choose `File` as the `TrainingInputMode` in the algorithm specification.
    # For distributed training algorithms, specify an instance count greater than
    # 1.
    resource_config: "ResourceConfig" = dataclasses.field(
        default_factory=dict,
    )

    # Sets a duration for training. Use this parameter to cap model training
    # costs. To stop a job, Amazon SageMaker sends the algorithm the `SIGTERM`
    # signal, which delays job termination for 120 seconds. Algorithms might use
    # this 120-second window to save the model artifacts.

    # When Amazon SageMaker terminates a job because the stopping condition has
    # been met, training algorithms provided by Amazon SageMaker save the
    # intermediate results of the job. This intermediate data is a valid model
    # artifact. You can use it to create a model using the `CreateModel` API.
    stopping_condition: "StoppingCondition" = dataclasses.field(
        default_factory=dict,
    )

    # Algorithm-specific parameters that influence the quality of the model. You
    # set hyperparameters before you start the learning process. For a list of
    # hyperparameters for each training algorithm provided by Amazon SageMaker,
    # see
    # [Algorithms](http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html).

    # You can specify a maximum of 100 hyperparameters. Each hyperparameter is a
    # key-value pair. Each key and value is limited to 256 characters, as
    # specified by the `Length Constraint`.
    hyper_parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A VpcConfig object that specifies the VPC that you want your training job
    # to connect to. Control access to and from your training container by
    # configuring the VPC. For more information, see train-vpc
    vpc_config: "VpcConfig" = dataclasses.field(default_factory=dict, )

    # An array of key-value pairs. For more information, see [Using Cost
    # Allocation
    # Tags](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-
    # alloc-tags.html#allocation-what) in the _AWS Billing and Cost Management
    # User Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateTrainingJobResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "training_job_arn",
                "TrainingJobArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the training job.
    training_job_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateTransformJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "transform_job_name",
                "TransformJobName",
                autoboto.TypeInfo(str),
            ),
            (
                "model_name",
                "ModelName",
                autoboto.TypeInfo(str),
            ),
            (
                "transform_input",
                "TransformInput",
                autoboto.TypeInfo(TransformInput),
            ),
            (
                "transform_output",
                "TransformOutput",
                autoboto.TypeInfo(TransformOutput),
            ),
            (
                "transform_resources",
                "TransformResources",
                autoboto.TypeInfo(TransformResources),
            ),
            (
                "max_concurrent_transforms",
                "MaxConcurrentTransforms",
                autoboto.TypeInfo(int),
            ),
            (
                "max_payload_in_mb",
                "MaxPayloadInMB",
                autoboto.TypeInfo(int),
            ),
            (
                "batch_strategy",
                "BatchStrategy",
                autoboto.TypeInfo(BatchStrategy),
            ),
            (
                "environment",
                "Environment",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the transform job. The name must be unique within an AWS Region
    # in an AWS account.
    transform_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the model that you want to use for the transform job.
    # `ModelName` must be the name of an existing Amazon SageMaker model within
    # an AWS Region in an AWS account.
    model_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Describes the input source and the way the transform job consumes it.
    transform_input: "TransformInput" = dataclasses.field(
        default_factory=dict,
    )

    # Describes the results of the transform job.
    transform_output: "TransformOutput" = dataclasses.field(
        default_factory=dict,
    )

    # Describes the resources, including ML instance types and ML instance count,
    # to use for the transform job.
    transform_resources: "TransformResources" = dataclasses.field(
        default_factory=dict,
    )

    # The maximum number of parallel requests that can be sent to each instance
    # in a transform job. This is good for algorithms that implement multiple
    # workers on larger instances . The default value is `1`. To allow Amazon
    # SageMaker to determine the appropriate number for
    # `MaxConcurrentTransforms`, set the value to `0`.
    max_concurrent_transforms: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum payload size allowed, in MB. A payload is the data portion of a
    # record (without metadata). The value in `MaxPayloadInMB` must be greater or
    # equal to the size of a single record. You can approximate the size of a
    # record by dividing the size of your dataset by the number of records. Then
    # multiply this value by the number of records you want in a mini-batch. It
    # is recommended to enter a value slightly larger than this to ensure the
    # records fit within the maximum payload size. The default value is `6` MB.
    # For an unlimited payload size, set the value to `0`.
    max_payload_in_mb: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Determines the number of records included in a single mini-batch.
    # `SingleRecord` means only one record is used per mini-batch. `MultiRecord`
    # means a mini-batch is set to contain as many records that can fit within
    # the `MaxPayloadInMB` limit.

    # Batch transform will automatically split your input data into whatever
    # payload size is specified if you set `SplitType` to `Line` and
    # `BatchStrategy` to `MultiRecord`. There's no need to split the dataset into
    # smaller files or to use larger payload sizes unless the records in your
    # dataset are very large.
    batch_strategy: "BatchStrategy" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The environment variables to set in the Docker container. We support up to
    # 16 key and values entries in the map.
    environment: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of key-value pairs. Adding tags is optional. For more information,
    # see [Using Cost Allocation
    # Tags](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-
    # alloc-tags.html#allocation-what) in the _AWS Billing and Cost Management
    # User Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateTransformJobResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "transform_job_arn",
                "TransformJobArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the transform job.
    transform_job_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DataSource(autoboto.ShapeBase):
    """
    Describes the location of the channel data.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_data_source",
                "S3DataSource",
                autoboto.TypeInfo(S3DataSource),
            ),
        ]

    # The S3 location of the data source that is associated with a channel.
    s3_data_source: "S3DataSource" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteEndpointConfigInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_config_name",
                "EndpointConfigName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the endpoint configuration that you want to delete.
    endpoint_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteEndpointInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the endpoint that you want to delete.
    endpoint_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteModelInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "model_name",
                "ModelName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the model to delete.
    model_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteNotebookInstanceInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the Amazon SageMaker notebook instance to delete.
    notebook_instance_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteNotebookInstanceLifecycleConfigInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_lifecycle_config_name",
                "NotebookInstanceLifecycleConfigName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the lifecycle configuration to delete.
    notebook_instance_lifecycle_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteTagsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource whose tags you want to
    # delete.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array or one or more tag keys to delete.
    tag_keys: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DeleteTagsOutput(autoboto.OutputShapeBase):
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
class DeployedImage(autoboto.ShapeBase):
    """
    Gets the Amazon EC2 Container Registry path of the docker image of the model
    that is hosted in this ProductionVariant.

    If you used the `registry/repository[:tag]` form to to specify the image path of
    the primary container when you created the model hosted in this
    `ProductionVariant`, the path resolves to a path of the form
    `registry/repository[@digest]`. A digest is a hash value that identifies a
    specific version of an image. For information about Amazon ECR paths, see
    [Pulling an
    Image](http://docs.aws.amazon.com//AmazonECR/latest/userguide/docker-pull-ecr-
    image.html) in the _Amazon ECR User Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "specified_image",
                "SpecifiedImage",
                autoboto.TypeInfo(str),
            ),
            (
                "resolved_image",
                "ResolvedImage",
                autoboto.TypeInfo(str),
            ),
            (
                "resolution_time",
                "ResolutionTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The image path you specified when you created the model.
    specified_image: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The specific digest path of the image hosted in this `ProductionVariant`.
    resolved_image: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time when the image path for the model resolved to the
    # `ResolvedImage`
    resolution_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeEndpointConfigInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_config_name",
                "EndpointConfigName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the endpoint configuration.
    endpoint_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeEndpointConfigOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_config_name",
                "EndpointConfigName",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_config_arn",
                "EndpointConfigArn",
                autoboto.TypeInfo(str),
            ),
            (
                "production_variants",
                "ProductionVariants",
                autoboto.TypeInfo(typing.List[ProductionVariant]),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Name of the Amazon SageMaker endpoint configuration.
    endpoint_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the endpoint configuration.
    endpoint_config_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of `ProductionVariant` objects, one for each model that you want
    # to host at this endpoint.
    production_variants: typing.List["ProductionVariant"] = dataclasses.field(
        default_factory=list,
    )

    # A timestamp that shows when the endpoint configuration was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # AWS KMS key ID Amazon SageMaker uses to encrypt data when storing it on the
    # ML storage volume attached to the instance.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEndpointInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the endpoint.
    endpoint_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEndpointOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_name",
                "EndpointName",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_arn",
                "EndpointArn",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_config_name",
                "EndpointConfigName",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_status",
                "EndpointStatus",
                autoboto.TypeInfo(EndpointStatus),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "production_variants",
                "ProductionVariants",
                autoboto.TypeInfo(typing.List[ProductionVariantSummary]),
            ),
            (
                "failure_reason",
                "FailureReason",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Name of the endpoint.
    endpoint_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the endpoint.
    endpoint_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the endpoint configuration associated with this endpoint.
    endpoint_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the endpoint.
    endpoint_status: "EndpointStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the endpoint was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the endpoint was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of ProductionVariantSummary objects, one for each model hosted
    # behind this endpoint.
    production_variants: typing.List["ProductionVariantSummary"
                                    ] = dataclasses.field(
                                        default_factory=list,
                                    )

    # If the status of the endpoint is `Failed`, the reason why it failed.
    failure_reason: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeHyperParameterTuningJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hyper_parameter_tuning_job_name",
                "HyperParameterTuningJobName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the tuning job to describe.
    hyper_parameter_tuning_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeHyperParameterTuningJobResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hyper_parameter_tuning_job_name",
                "HyperParameterTuningJobName",
                autoboto.TypeInfo(str),
            ),
            (
                "hyper_parameter_tuning_job_arn",
                "HyperParameterTuningJobArn",
                autoboto.TypeInfo(str),
            ),
            (
                "hyper_parameter_tuning_job_config",
                "HyperParameterTuningJobConfig",
                autoboto.TypeInfo(HyperParameterTuningJobConfig),
            ),
            (
                "training_job_definition",
                "TrainingJobDefinition",
                autoboto.TypeInfo(HyperParameterTrainingJobDefinition),
            ),
            (
                "hyper_parameter_tuning_job_status",
                "HyperParameterTuningJobStatus",
                autoboto.TypeInfo(HyperParameterTuningJobStatus),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "training_job_status_counters",
                "TrainingJobStatusCounters",
                autoboto.TypeInfo(TrainingJobStatusCounters),
            ),
            (
                "objective_status_counters",
                "ObjectiveStatusCounters",
                autoboto.TypeInfo(ObjectiveStatusCounters),
            ),
            (
                "hyper_parameter_tuning_end_time",
                "HyperParameterTuningEndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "best_training_job",
                "BestTrainingJob",
                autoboto.TypeInfo(HyperParameterTrainingJobSummary),
            ),
            (
                "failure_reason",
                "FailureReason",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the tuning job.
    hyper_parameter_tuning_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the tuning job.
    hyper_parameter_tuning_job_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The HyperParameterTuningJobConfig object that specifies the configuration
    # of the tuning job.
    hyper_parameter_tuning_job_config: "HyperParameterTuningJobConfig" = dataclasses.field(
        default_factory=dict,
    )

    # The HyperParameterTrainingJobDefinition object that specifies the
    # definition of the training jobs that this tuning job launches.
    training_job_definition: "HyperParameterTrainingJobDefinition" = dataclasses.field(
        default_factory=dict,
    )

    # The status of the tuning job: InProgress, Completed, Failed, Stopping, or
    # Stopped.
    hyper_parameter_tuning_job_status: "HyperParameterTuningJobStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time that the tuning job started.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The TrainingJobStatusCounters object that specifies the number of training
    # jobs, categorized by status, that this tuning job launched.
    training_job_status_counters: "TrainingJobStatusCounters" = dataclasses.field(
        default_factory=dict,
    )

    # The ObjectiveStatusCounters object that specifies the number of training
    # jobs, categorized by the status of their final objective metric, that this
    # tuning job launched.
    objective_status_counters: "ObjectiveStatusCounters" = dataclasses.field(
        default_factory=dict,
    )

    # The date and time that the tuning job ended.
    hyper_parameter_tuning_end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time that the status of the tuning job was modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A TrainingJobSummary object that describes the training job that completed
    # with the best current HyperParameterTuningJobObjective.
    best_training_job: "HyperParameterTrainingJobSummary" = dataclasses.field(
        default_factory=dict,
    )

    # If the tuning job failed, the reason it failed.
    failure_reason: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeModelInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "model_name",
                "ModelName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the model.
    model_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeModelOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "model_name",
                "ModelName",
                autoboto.TypeInfo(str),
            ),
            (
                "primary_container",
                "PrimaryContainer",
                autoboto.TypeInfo(ContainerDefinition),
            ),
            (
                "execution_role_arn",
                "ExecutionRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "model_arn",
                "ModelArn",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_config",
                "VpcConfig",
                autoboto.TypeInfo(VpcConfig),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Name of the Amazon SageMaker model.
    model_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The location of the primary inference code, associated artifacts, and
    # custom environment map that the inference code uses when it is deployed in
    # production.
    primary_container: "ContainerDefinition" = dataclasses.field(
        default_factory=dict,
    )

    # The Amazon Resource Name (ARN) of the IAM role that you specified for the
    # model.
    execution_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the model was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the model.
    model_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A VpcConfig object that specifies the VPC that this model has access to.
    # For more information, see host-vpc
    vpc_config: "VpcConfig" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeNotebookInstanceInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the notebook instance that you want information about.
    notebook_instance_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeNotebookInstanceLifecycleConfigInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_lifecycle_config_name",
                "NotebookInstanceLifecycleConfigName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the lifecycle configuration to describe.
    notebook_instance_lifecycle_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeNotebookInstanceLifecycleConfigOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "notebook_instance_lifecycle_config_arn",
                "NotebookInstanceLifecycleConfigArn",
                autoboto.TypeInfo(str),
            ),
            (
                "notebook_instance_lifecycle_config_name",
                "NotebookInstanceLifecycleConfigName",
                autoboto.TypeInfo(str),
            ),
            (
                "on_create",
                "OnCreate",
                autoboto.TypeInfo(typing.List[NotebookInstanceLifecycleHook]),
            ),
            (
                "on_start",
                "OnStart",
                autoboto.TypeInfo(typing.List[NotebookInstanceLifecycleHook]),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the lifecycle configuration.
    notebook_instance_lifecycle_config_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the lifecycle configuration.
    notebook_instance_lifecycle_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The shell script that runs only once, when you create a notebook instance.
    on_create: typing.List["NotebookInstanceLifecycleHook"] = dataclasses.field(
        default_factory=list,
    )

    # The shell script that runs every time you start a notebook instance,
    # including when you create the notebook instance.
    on_start: typing.List["NotebookInstanceLifecycleHook"] = dataclasses.field(
        default_factory=list,
    )

    # A timestamp that tells when the lifecycle configuration was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp that tells when the lifecycle configuration was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeNotebookInstanceOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "notebook_instance_arn",
                "NotebookInstanceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                autoboto.TypeInfo(str),
            ),
            (
                "notebook_instance_status",
                "NotebookInstanceStatus",
                autoboto.TypeInfo(NotebookInstanceStatus),
            ),
            (
                "failure_reason",
                "FailureReason",
                autoboto.TypeInfo(str),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                autoboto.TypeInfo(InstanceType),
            ),
            (
                "subnet_id",
                "SubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "security_groups",
                "SecurityGroups",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "network_interface_id",
                "NetworkInterfaceId",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "notebook_instance_lifecycle_config_name",
                "NotebookInstanceLifecycleConfigName",
                autoboto.TypeInfo(str),
            ),
            (
                "direct_internet_access",
                "DirectInternetAccess",
                autoboto.TypeInfo(DirectInternetAccess),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the notebook instance.
    notebook_instance_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Name of the Amazon SageMaker notebook instance.
    notebook_instance_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the notebook instance.
    notebook_instance_status: "NotebookInstanceStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If status is failed, the reason it failed.
    failure_reason: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL that you use to connect to the Jupyter notebook that is running in
    # your notebook instance.
    url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of ML compute instance running on the notebook instance.
    instance_type: "InstanceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the VPC subnet.
    subnet_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The IDs of the VPC security groups.
    security_groups: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Amazon Resource Name (ARN) of the IAM role associated with the instance.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # AWS KMS key ID Amazon SageMaker uses to encrypt data when storing it on the
    # ML storage volume attached to the instance.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Network interface IDs that Amazon SageMaker created at the time of creating
    # the instance.
    network_interface_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp. Use this parameter to retrieve the time when the notebook
    # instance was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp. Use this parameter to return the time when the notebook
    # instance was created
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Returns the name of a notebook instance lifecycle configuration.

    # For information about notebook instance lifestyle configurations, see
    # notebook-lifecycle-config.
    notebook_instance_lifecycle_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Describes whether Amazon SageMaker provides internet access to the notebook
    # instance. If this value is set to _Disabled, he notebook instance does not
    # have internet access, and cannot connect to Amazon SageMaker training and
    # endpoint services_.

    # For more information, see appendix-notebook-and-internet-access.
    direct_internet_access: "DirectInternetAccess" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTrainingJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "training_job_name",
                "TrainingJobName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the training job.
    training_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTrainingJobResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "training_job_name",
                "TrainingJobName",
                autoboto.TypeInfo(str),
            ),
            (
                "training_job_arn",
                "TrainingJobArn",
                autoboto.TypeInfo(str),
            ),
            (
                "model_artifacts",
                "ModelArtifacts",
                autoboto.TypeInfo(ModelArtifacts),
            ),
            (
                "training_job_status",
                "TrainingJobStatus",
                autoboto.TypeInfo(TrainingJobStatus),
            ),
            (
                "secondary_status",
                "SecondaryStatus",
                autoboto.TypeInfo(SecondaryStatus),
            ),
            (
                "algorithm_specification",
                "AlgorithmSpecification",
                autoboto.TypeInfo(AlgorithmSpecification),
            ),
            (
                "input_data_config",
                "InputDataConfig",
                autoboto.TypeInfo(typing.List[Channel]),
            ),
            (
                "resource_config",
                "ResourceConfig",
                autoboto.TypeInfo(ResourceConfig),
            ),
            (
                "stopping_condition",
                "StoppingCondition",
                autoboto.TypeInfo(StoppingCondition),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "tuning_job_arn",
                "TuningJobArn",
                autoboto.TypeInfo(str),
            ),
            (
                "failure_reason",
                "FailureReason",
                autoboto.TypeInfo(str),
            ),
            (
                "hyper_parameters",
                "HyperParameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "output_data_config",
                "OutputDataConfig",
                autoboto.TypeInfo(OutputDataConfig),
            ),
            (
                "vpc_config",
                "VpcConfig",
                autoboto.TypeInfo(VpcConfig),
            ),
            (
                "training_start_time",
                "TrainingStartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "training_end_time",
                "TrainingEndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "secondary_status_transitions",
                "SecondaryStatusTransitions",
                autoboto.TypeInfo(typing.List[SecondaryStatusTransition]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Name of the model training job.
    training_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the training job.
    training_job_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the Amazon S3 location that is configured for storing
    # model artifacts.
    model_artifacts: "ModelArtifacts" = dataclasses.field(
        default_factory=dict,
    )

    # The status of the training job.

    # For the `InProgress` status, Amazon SageMaker can return these secondary
    # statuses:

    #   * Starting - Preparing for training.

    #   * Downloading - Optional stage for algorithms that support File training input mode. It indicates data is being downloaded to ML storage volumes.

    #   * Training - Training is in progress.

    #   * Uploading - Training is complete and model upload is in progress.

    # For the `Stopped` training status, Amazon SageMaker can return these
    # secondary statuses:

    #   * MaxRuntimeExceeded - Job stopped as a result of maximum allowed runtime exceeded.
    training_job_status: "TrainingJobStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides granular information about the system state. For more information,
    # see `TrainingJobStatus`.

    #   * `Starting` \- starting the training job.

    #   * `Downloading` \- downloading the input data.

    #   * `Training` \- model training is in progress.

    #   * `Uploading` \- uploading the trained model.

    #   * `Stopping` \- stopping the training job.

    #   * `Stopped` \- the training job has stopped.

    #   * `MaxRuntimeExceeded` \- the training job exceeded the specified max run time and has been stopped.

    #   * `Completed` \- the training job has completed.

    #   * `Failed` \- the training job has failed. The failure reason is stored in the `FailureReason` field of `DescribeTrainingJobResponse`.

    # The valid values for `SecondaryStatus` are subject to change. They
    # primarily provide information on the progress of the training job.
    secondary_status: "SecondaryStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the algorithm used for training, and algorithm metadata.
    algorithm_specification: "AlgorithmSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # An array of `Channel` objects that describes each data input channel.
    input_data_config: typing.List["Channel"] = dataclasses.field(
        default_factory=list,
    )

    # Resources, including ML compute instances and ML storage volumes, that are
    # configured for model training.
    resource_config: "ResourceConfig" = dataclasses.field(
        default_factory=dict,
    )

    # The condition under which to stop the training job.
    stopping_condition: "StoppingCondition" = dataclasses.field(
        default_factory=dict,
    )

    # A timestamp that indicates when the training job was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the associated hyperparameter tuning job
    # if the training job was launched by a hyperparameter tuning job.
    tuning_job_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the training job failed, the reason it failed.
    failure_reason: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Algorithm-specific parameters.
    hyper_parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS Identity and Access Management (IAM) role configured for the
    # training job.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The S3 path where model artifacts that you configured when creating the job
    # are stored. Amazon SageMaker creates subfolders for model artifacts.
    output_data_config: "OutputDataConfig" = dataclasses.field(
        default_factory=dict,
    )

    # A VpcConfig object that specifies the VPC that this training job has access
    # to. For more information, see train-vpc.
    vpc_config: "VpcConfig" = dataclasses.field(default_factory=dict, )

    # Indicates the time when the training job starts on training instances. You
    # are billed for the time interval between this time and the value of
    # `TrainingEndTime`. The start time in CloudWatch Logs might be later than
    # this time. The difference is due to the time it takes to download the
    # training data and to the size of the training container.
    training_start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates the time when the training job ends on training instances. You
    # are billed for the time interval between the value of `TrainingStartTime`
    # and this time. For successful jobs and stopped jobs, this is the time after
    # model artifacts are uploaded. For failed jobs, this is the time when Amazon
    # SageMaker detects a job failure.
    training_end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp that indicates when the status of the training job was last
    # modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # To give an overview of the training job lifecycle,
    # `SecondaryStatusTransitions` is a log of time-ordered secondary statuses
    # that a training job has transitioned.
    secondary_status_transitions: typing.List["SecondaryStatusTransition"
                                             ] = dataclasses.field(
                                                 default_factory=list,
                                             )


@dataclasses.dataclass
class DescribeTransformJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "transform_job_name",
                "TransformJobName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the transform job that you want to view details of.
    transform_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTransformJobResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "transform_job_name",
                "TransformJobName",
                autoboto.TypeInfo(str),
            ),
            (
                "transform_job_arn",
                "TransformJobArn",
                autoboto.TypeInfo(str),
            ),
            (
                "transform_job_status",
                "TransformJobStatus",
                autoboto.TypeInfo(TransformJobStatus),
            ),
            (
                "model_name",
                "ModelName",
                autoboto.TypeInfo(str),
            ),
            (
                "transform_input",
                "TransformInput",
                autoboto.TypeInfo(TransformInput),
            ),
            (
                "transform_resources",
                "TransformResources",
                autoboto.TypeInfo(TransformResources),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "failure_reason",
                "FailureReason",
                autoboto.TypeInfo(str),
            ),
            (
                "max_concurrent_transforms",
                "MaxConcurrentTransforms",
                autoboto.TypeInfo(int),
            ),
            (
                "max_payload_in_mb",
                "MaxPayloadInMB",
                autoboto.TypeInfo(int),
            ),
            (
                "batch_strategy",
                "BatchStrategy",
                autoboto.TypeInfo(BatchStrategy),
            ),
            (
                "environment",
                "Environment",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "transform_output",
                "TransformOutput",
                autoboto.TypeInfo(TransformOutput),
            ),
            (
                "transform_start_time",
                "TransformStartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "transform_end_time",
                "TransformEndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the transform job.
    transform_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the transform job.
    transform_job_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the transform job. If the transform job failed, the reason is
    # returned in the `FailureReason` field.
    transform_job_status: "TransformJobStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the model used in the transform job.
    model_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Describes the dataset to be transformed and the Amazon S3 location where it
    # is stored.
    transform_input: "TransformInput" = dataclasses.field(
        default_factory=dict,
    )

    # Describes the resources, including ML instance types and ML instance count,
    # to use for the transform job.
    transform_resources: "TransformResources" = dataclasses.field(
        default_factory=dict,
    )

    # A timestamp that shows when the transform Job was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the transform job failed, the reason that it failed.
    failure_reason: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of parallel requests on each instance node that can be
    # launched in a transform job. The default value is 1.
    max_concurrent_transforms: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum payload size , in MB used in the transform job.
    max_payload_in_mb: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # SingleRecord means only one record was used per a batch. `MultiRecord`
    # means batches contained as many records that could possibly fit within the
    # `MaxPayloadInMB` limit.
    batch_strategy: "BatchStrategy" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    environment: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Identifies the Amazon S3 location where you want Amazon SageMaker to save
    # the results from the transform job.
    transform_output: "TransformOutput" = dataclasses.field(
        default_factory=dict,
    )

    # Indicates when the transform job starts on ML instances. You are billed for
    # the time interval between this time and the value of `TransformEndTime`.
    transform_start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates when the transform job is `Completed`, `Stopped`, or `Failed`.
    # You are billed for the time interval between this time and the value of
    # `TransformStartTime`.
    transform_end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DesiredWeightAndCapacity(autoboto.ShapeBase):
    """
    Specifies weight and capacity values for a production variant.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "variant_name",
                "VariantName",
                autoboto.TypeInfo(str),
            ),
            (
                "desired_weight",
                "DesiredWeight",
                autoboto.TypeInfo(float),
            ),
            (
                "desired_instance_count",
                "DesiredInstanceCount",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the variant to update.
    variant_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The variant's weight.
    desired_weight: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The variant's capacity.
    desired_instance_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class DirectInternetAccess(Enum):
    Enabled = "Enabled"
    Disabled = "Disabled"


class EndpointConfigSortKey(Enum):
    Name = "Name"
    CreationTime = "CreationTime"


@dataclasses.dataclass
class EndpointConfigSummary(autoboto.ShapeBase):
    """
    Provides summary information for an endpoint configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_config_name",
                "EndpointConfigName",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_config_arn",
                "EndpointConfigArn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the endpoint configuration.
    endpoint_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the endpoint configuration.
    endpoint_config_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the endpoint configuration was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class EndpointSortKey(Enum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class EndpointStatus(Enum):
    OutOfService = "OutOfService"
    Creating = "Creating"
    Updating = "Updating"
    SystemUpdating = "SystemUpdating"
    RollingBack = "RollingBack"
    InService = "InService"
    Deleting = "Deleting"
    Failed = "Failed"


@dataclasses.dataclass
class EndpointSummary(autoboto.ShapeBase):
    """
    Provides summary information for an endpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_arn",
                "EndpointArn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "endpoint_status",
                "EndpointStatus",
                autoboto.TypeInfo(EndpointStatus),
            ),
        ]

    # The name of the endpoint.
    endpoint_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the endpoint.
    endpoint_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A timestamp that shows when the endpoint was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the endpoint was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the endpoint.
    endpoint_status: "EndpointStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FinalHyperParameterTuningJobObjectiveMetric(autoboto.ShapeBase):
    """
    Shows the final value for the objective metric for a training job that was
    launched by a hyperparameter tuning job. You define the objective metric in the
    `HyperParameterTuningJobObjective` parameter of HyperParameterTuningJobConfig.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metric_name",
                "MetricName",
                autoboto.TypeInfo(str),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(float),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(HyperParameterTuningJobObjectiveType),
            ),
        ]

    # The name of the objective metric.
    metric_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value of the objective metric.
    value: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether to minimize or maximize the objective metric. Valid values are
    # Minimize and Maximize.
    type: "HyperParameterTuningJobObjectiveType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class HyperParameterAlgorithmSpecification(autoboto.ShapeBase):
    """
    Specifies which training algorithm to use for training jobs that a
    hyperparameter tuning job launches and the metrics to monitor.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "training_image",
                "TrainingImage",
                autoboto.TypeInfo(str),
            ),
            (
                "training_input_mode",
                "TrainingInputMode",
                autoboto.TypeInfo(TrainingInputMode),
            ),
            (
                "metric_definitions",
                "MetricDefinitions",
                autoboto.TypeInfo(typing.List[MetricDefinition]),
            ),
        ]

    # The registry path of the Docker image that contains the training algorithm.
    # For information about Docker registry paths for built-in algorithms, see
    # sagemaker-algo-docker-registry-paths.
    training_image: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The input mode that the algorithm supports: File or Pipe. In File input
    # mode, Amazon SageMaker downloads the training data from Amazon S3 to the
    # storage volume that is attached to the training instance and mounts the
    # directory to the Docker volume for the training container. In Pipe input
    # mode, Amazon SageMaker streams data directly from Amazon S3 to the
    # container.

    # If you specify File mode, make sure that you provision the storage volume
    # that is attached to the training instance with enough capacity to
    # accommodate the training data downloaded from Amazon S3, the model
    # artifacts, and intermediate information.

    # For more information about input modes, see
    # [Algorithms](http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html).
    training_input_mode: "TrainingInputMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of MetricDefinition objects that specify the metrics that the
    # algorithm emits.
    metric_definitions: typing.List["MetricDefinition"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class HyperParameterTrainingJobDefinition(autoboto.ShapeBase):
    """
    Defines the training jobs launched by a hyperparameter tuning job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "algorithm_specification",
                "AlgorithmSpecification",
                autoboto.TypeInfo(HyperParameterAlgorithmSpecification),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "input_data_config",
                "InputDataConfig",
                autoboto.TypeInfo(typing.List[Channel]),
            ),
            (
                "output_data_config",
                "OutputDataConfig",
                autoboto.TypeInfo(OutputDataConfig),
            ),
            (
                "resource_config",
                "ResourceConfig",
                autoboto.TypeInfo(ResourceConfig),
            ),
            (
                "stopping_condition",
                "StoppingCondition",
                autoboto.TypeInfo(StoppingCondition),
            ),
            (
                "static_hyper_parameters",
                "StaticHyperParameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "vpc_config",
                "VpcConfig",
                autoboto.TypeInfo(VpcConfig),
            ),
        ]

    # The HyperParameterAlgorithmSpecification object that specifies the
    # algorithm to use for the training jobs that the tuning job launches.
    algorithm_specification: "HyperParameterAlgorithmSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # The Amazon Resource Name (ARN) of the IAM role associated with the training
    # jobs that the tuning job launches.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of Channel objects that specify the input for the training jobs
    # that the tuning job launches.
    input_data_config: typing.List["Channel"] = dataclasses.field(
        default_factory=list,
    )

    # Specifies the path to the Amazon S3 bucket where you store model artifacts
    # from the training jobs that the tuning job launches.
    output_data_config: "OutputDataConfig" = dataclasses.field(
        default_factory=dict,
    )

    # The resources, including the compute instances and storage volumes, to use
    # for the training jobs that the tuning job launches.

    # Storage volumes store model artifacts and incremental states. Training
    # algorithms might also use storage volumes for scratch space. If you want
    # Amazon SageMaker to use the storage volume to store the training data,
    # choose `File` as the `TrainingInputMode` in the algorithm specification.
    # For distributed training algorithms, specify an instance count greater than
    # 1.
    resource_config: "ResourceConfig" = dataclasses.field(
        default_factory=dict,
    )

    # Sets a maximum duration for the training jobs that the tuning job launches.
    # Use this parameter to limit model training costs.

    # To stop a job, Amazon SageMaker sends the algorithm the `SIGTERM` signal.
    # This delays job termination for 120 seconds. Algorithms might use this
    # 120-second window to save the model artifacts.

    # When Amazon SageMaker terminates a job because the stopping condition has
    # been met, training algorithms provided by Amazon SageMaker save the
    # intermediate results of the job.
    stopping_condition: "StoppingCondition" = dataclasses.field(
        default_factory=dict,
    )

    # Specifies the values of hyperparameters that do not change for the tuning
    # job.
    static_hyper_parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The VpcConfig object that specifies the VPC that you want the training jobs
    # that this hyperparameter tuning job launches to connect to. Control access
    # to and from your training container by configuring the VPC. For more
    # information, see train-vpc.
    vpc_config: "VpcConfig" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class HyperParameterTrainingJobSummary(autoboto.ShapeBase):
    """
    Specifies summary information about a training job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "training_job_name",
                "TrainingJobName",
                autoboto.TypeInfo(str),
            ),
            (
                "training_job_arn",
                "TrainingJobArn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "training_job_status",
                "TrainingJobStatus",
                autoboto.TypeInfo(TrainingJobStatus),
            ),
            (
                "tuned_hyper_parameters",
                "TunedHyperParameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "training_start_time",
                "TrainingStartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "training_end_time",
                "TrainingEndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "failure_reason",
                "FailureReason",
                autoboto.TypeInfo(str),
            ),
            (
                "final_hyper_parameter_tuning_job_objective_metric",
                "FinalHyperParameterTuningJobObjectiveMetric",
                autoboto.TypeInfo(FinalHyperParameterTuningJobObjectiveMetric),
            ),
            (
                "objective_status",
                "ObjectiveStatus",
                autoboto.TypeInfo(ObjectiveStatus),
            ),
        ]

    # The name of the training job.
    training_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the training job.
    training_job_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time that the training job was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the training job.
    training_job_status: "TrainingJobStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of the hyperparameters for which you specified ranges to search.
    tuned_hyper_parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time that the training job started.
    training_start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time that the training job ended.
    training_end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The reason that the training job failed.
    failure_reason: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The FinalHyperParameterTuningJobObjectiveMetric object that specifies the
    # value of the objective metric of the tuning job that launched this training
    # job.
    final_hyper_parameter_tuning_job_objective_metric: "FinalHyperParameterTuningJobObjectiveMetric" = dataclasses.field(
        default_factory=dict,
    )

    # The status of the objective metric for the training job:

    #   * Succeeded: The final objective metric for the training job was evaluated by the hyperparameter tuning job and used in the hyperparameter tuning process.

    #   * Pending: The training job is in progress and evaluation of its final objective metric is pending.

    #   * Failed: The final objective metric for the training job was not evaluated, and was not used in the hyperparameter tuning process. This typically occurs when the training job failed or did not emit an objective metric.
    objective_status: "ObjectiveStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class HyperParameterTuningJobConfig(autoboto.ShapeBase):
    """
    Configures a hyperparameter tuning job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "strategy",
                "Strategy",
                autoboto.TypeInfo(HyperParameterTuningJobStrategyType),
            ),
            (
                "hyper_parameter_tuning_job_objective",
                "HyperParameterTuningJobObjective",
                autoboto.TypeInfo(HyperParameterTuningJobObjective),
            ),
            (
                "resource_limits",
                "ResourceLimits",
                autoboto.TypeInfo(ResourceLimits),
            ),
            (
                "parameter_ranges",
                "ParameterRanges",
                autoboto.TypeInfo(ParameterRanges),
            ),
        ]

    # Specifies the search strategy for hyperparameters. Currently, the only
    # valid value is `Bayesian`.
    strategy: "HyperParameterTuningJobStrategyType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The HyperParameterTuningJobObjective object that specifies the objective
    # metric for this tuning job.
    hyper_parameter_tuning_job_objective: "HyperParameterTuningJobObjective" = dataclasses.field(
        default_factory=dict,
    )

    # The ResourceLimits object that specifies the maximum number of training
    # jobs and parallel training jobs for this tuning job.
    resource_limits: "ResourceLimits" = dataclasses.field(
        default_factory=dict,
    )

    # The ParameterRanges object that specifies the ranges of hyperparameters
    # that this tuning job searches.
    parameter_ranges: "ParameterRanges" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class HyperParameterTuningJobObjective(autoboto.ShapeBase):
    """
    Defines the objective metric for a hyperparameter tuning job. Hyperparameter
    tuning uses the value of this metric to evaluate the training jobs it launches,
    and returns the training job that results in either the highest or lowest value
    for this metric, depending on the value you specify for the `Type` parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(HyperParameterTuningJobObjectiveType),
            ),
            (
                "metric_name",
                "MetricName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Whether to minimize or maximize the objective metric.
    type: "HyperParameterTuningJobObjectiveType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the metric to use for the objective metric.
    metric_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class HyperParameterTuningJobObjectiveType(Enum):
    Maximize = "Maximize"
    Minimize = "Minimize"


class HyperParameterTuningJobSortByOptions(Enum):
    Name = "Name"
    Status = "Status"
    CreationTime = "CreationTime"


class HyperParameterTuningJobStatus(Enum):
    Completed = "Completed"
    InProgress = "InProgress"
    Failed = "Failed"
    Stopped = "Stopped"
    Stopping = "Stopping"


class HyperParameterTuningJobStrategyType(Enum):
    """
    The strategy hyperparameter tuning uses to find the best combination of
    hyperparameters for your model. Currently, the only supported value is
    `Bayesian`.
    """
    Bayesian = "Bayesian"


@dataclasses.dataclass
class HyperParameterTuningJobSummary(autoboto.ShapeBase):
    """
    Provides summary information about a hyperparameter tuning job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hyper_parameter_tuning_job_name",
                "HyperParameterTuningJobName",
                autoboto.TypeInfo(str),
            ),
            (
                "hyper_parameter_tuning_job_arn",
                "HyperParameterTuningJobArn",
                autoboto.TypeInfo(str),
            ),
            (
                "hyper_parameter_tuning_job_status",
                "HyperParameterTuningJobStatus",
                autoboto.TypeInfo(HyperParameterTuningJobStatus),
            ),
            (
                "strategy",
                "Strategy",
                autoboto.TypeInfo(HyperParameterTuningJobStrategyType),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "training_job_status_counters",
                "TrainingJobStatusCounters",
                autoboto.TypeInfo(TrainingJobStatusCounters),
            ),
            (
                "objective_status_counters",
                "ObjectiveStatusCounters",
                autoboto.TypeInfo(ObjectiveStatusCounters),
            ),
            (
                "hyper_parameter_tuning_end_time",
                "HyperParameterTuningEndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "resource_limits",
                "ResourceLimits",
                autoboto.TypeInfo(ResourceLimits),
            ),
        ]

    # The name of the tuning job.
    hyper_parameter_tuning_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the tuning job.
    hyper_parameter_tuning_job_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the tuning job.
    hyper_parameter_tuning_job_status: "HyperParameterTuningJobStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the search strategy hyperparameter tuning uses to choose which
    # hyperparameters to use for each iteration. Currently, the only valid value
    # is Bayesian.
    strategy: "HyperParameterTuningJobStrategyType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time that the tuning job was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The TrainingJobStatusCounters object that specifies the numbers of training
    # jobs, categorized by status, that this tuning job launched.
    training_job_status_counters: "TrainingJobStatusCounters" = dataclasses.field(
        default_factory=dict,
    )

    # The ObjectiveStatusCounters object that specifies the numbers of training
    # jobs, categorized by objective metric status, that this tuning job
    # launched.
    objective_status_counters: "ObjectiveStatusCounters" = dataclasses.field(
        default_factory=dict,
    )

    # The date and time that the tuning job ended.
    hyper_parameter_tuning_end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time that the tuning job was modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ResourceLimits object that specifies the maximum number of training
    # jobs and parallel training jobs allowed for this tuning job.
    resource_limits: "ResourceLimits" = dataclasses.field(
        default_factory=dict,
    )


class InstanceType(Enum):
    ml_t2_medium = "ml.t2.medium"
    ml_t2_large = "ml.t2.large"
    ml_t2_xlarge = "ml.t2.xlarge"
    ml_t2_2xlarge = "ml.t2.2xlarge"
    ml_m4_xlarge = "ml.m4.xlarge"
    ml_m4_2xlarge = "ml.m4.2xlarge"
    ml_m4_4xlarge = "ml.m4.4xlarge"
    ml_m4_10xlarge = "ml.m4.10xlarge"
    ml_m4_16xlarge = "ml.m4.16xlarge"
    ml_p2_xlarge = "ml.p2.xlarge"
    ml_p2_8xlarge = "ml.p2.8xlarge"
    ml_p2_16xlarge = "ml.p2.16xlarge"
    ml_p3_2xlarge = "ml.p3.2xlarge"
    ml_p3_8xlarge = "ml.p3.8xlarge"
    ml_p3_16xlarge = "ml.p3.16xlarge"


@dataclasses.dataclass
class IntegerParameterRange(autoboto.ShapeBase):
    """
    For a hyperparameter of the integer type, specifies the range that a
    hyperparameter tuning job searches.
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
                "min_value",
                "MinValue",
                autoboto.TypeInfo(str),
            ),
            (
                "max_value",
                "MaxValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the hyperparameter to search.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The minimum value of the hyperparameter to search.
    min_value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum value of the hyperparameter to search.
    max_value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListEndpointConfigsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sort_by",
                "SortBy",
                autoboto.TypeInfo(EndpointConfigSortKey),
            ),
            (
                "sort_order",
                "SortOrder",
                autoboto.TypeInfo(OrderKey),
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
                "name_contains",
                "NameContains",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time_before",
                "CreationTimeBefore",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_time_after",
                "CreationTimeAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The field to sort results by. The default is `CreationTime`.
    sort_by: "EndpointConfigSortKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The sort order for results. The default is `Ascending`.
    sort_order: "OrderKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the result of the previous `ListEndpointConfig` request was truncated,
    # the response includes a `NextToken`. To retrieve the next set of endpoint
    # configurations, use the token in the next request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of training jobs to return in the response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A string in the endpoint configuration name. This filter returns only
    # endpoint configurations whose name contains the specified string.
    name_contains: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A filter that returns only endpoint configurations created before the
    # specified time (timestamp).
    creation_time_before: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only endpoint configurations created after the
    # specified time (timestamp).
    creation_time_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListEndpointConfigsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_configs",
                "EndpointConfigs",
                autoboto.TypeInfo(typing.List[EndpointConfigSummary]),
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

    # An array of endpoint configurations.
    endpoint_configs: typing.List["EndpointConfigSummary"] = dataclasses.field(
        default_factory=list,
    )

    # If the response is truncated, Amazon SageMaker returns this token. To
    # retrieve the next set of endpoint configurations, use it in the subsequent
    # request
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListEndpointsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sort_by",
                "SortBy",
                autoboto.TypeInfo(EndpointSortKey),
            ),
            (
                "sort_order",
                "SortOrder",
                autoboto.TypeInfo(OrderKey),
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
                "name_contains",
                "NameContains",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time_before",
                "CreationTimeBefore",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_time_after",
                "CreationTimeAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_before",
                "LastModifiedTimeBefore",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_after",
                "LastModifiedTimeAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "status_equals",
                "StatusEquals",
                autoboto.TypeInfo(EndpointStatus),
            ),
        ]

    # Sorts the list of results. The default is `CreationTime`.
    sort_by: "EndpointSortKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The sort order for results. The default is `Ascending`.
    sort_order: "OrderKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the result of a `ListEndpoints` request was truncated, the response
    # includes a `NextToken`. To retrieve the next set of endpoints, use the
    # token in the next request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of endpoints to return in the response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A string in endpoint names. This filter returns only endpoints whose name
    # contains the specified string.
    name_contains: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A filter that returns only endpoints that were created before the specified
    # time (timestamp).
    creation_time_before: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only endpoints that were created after the specified
    # time (timestamp).
    creation_time_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only endpoints that were modified before the
    # specified timestamp.
    last_modified_time_before: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only endpoints that were modified after the specified
    # timestamp.
    last_modified_time_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only endpoints with the specified status.
    status_equals: "EndpointStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListEndpointsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoints",
                "Endpoints",
                autoboto.TypeInfo(typing.List[EndpointSummary]),
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

    # An array or endpoint objects.
    endpoints: typing.List["EndpointSummary"] = dataclasses.field(
        default_factory=list,
    )

    # If the response is truncated, Amazon SageMaker returns this token. To
    # retrieve the next set of training jobs, use it in the subsequent request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListHyperParameterTuningJobsRequest(autoboto.ShapeBase):
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
            (
                "sort_by",
                "SortBy",
                autoboto.TypeInfo(HyperParameterTuningJobSortByOptions),
            ),
            (
                "sort_order",
                "SortOrder",
                autoboto.TypeInfo(SortOrder),
            ),
            (
                "name_contains",
                "NameContains",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time_after",
                "CreationTimeAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_time_before",
                "CreationTimeBefore",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_after",
                "LastModifiedTimeAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_before",
                "LastModifiedTimeBefore",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "status_equals",
                "StatusEquals",
                autoboto.TypeInfo(HyperParameterTuningJobStatus),
            ),
        ]

    # If the result of the previous `ListHyperParameterTuningJobs` request was
    # truncated, the response includes a `NextToken`. To retrieve the next set of
    # tuning jobs, use the token in the next request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of tuning jobs to return. The default value is 10.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The field to sort results by. The default is `Name`.
    sort_by: "HyperParameterTuningJobSortByOptions" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The sort order for results. The default is `Ascending`.
    sort_order: "SortOrder" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string in the tuning job name. This filter returns only tuning jobs whose
    # name contains the specified string.
    name_contains: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A filter that returns only tuning jobs that were created after the
    # specified time.
    creation_time_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only tuning jobs that were created before the
    # specified time.
    creation_time_before: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only tuning jobs that were modified after the
    # specified time.
    last_modified_time_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only tuning jobs that were modified before the
    # specified time.
    last_modified_time_before: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only tuning jobs with the specified status.
    status_equals: "HyperParameterTuningJobStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListHyperParameterTuningJobsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hyper_parameter_tuning_job_summaries",
                "HyperParameterTuningJobSummaries",
                autoboto.TypeInfo(typing.List[HyperParameterTuningJobSummary]),
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

    # A list of HyperParameterTuningJobSummary objects that describe the tuning
    # jobs that the `ListHyperParameterTuningJobs` request returned.
    hyper_parameter_tuning_job_summaries: typing.List[
        "HyperParameterTuningJobSummary"
    ] = dataclasses.field(
        default_factory=list,
    )

    # If the result of this `ListHyperParameterTuningJobs` request was truncated,
    # the response includes a `NextToken`. To retrieve the next set of tuning
    # jobs, use the token in the next request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListModelsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sort_by",
                "SortBy",
                autoboto.TypeInfo(ModelSortKey),
            ),
            (
                "sort_order",
                "SortOrder",
                autoboto.TypeInfo(OrderKey),
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
                "name_contains",
                "NameContains",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time_before",
                "CreationTimeBefore",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_time_after",
                "CreationTimeAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # Sorts the list of results. The default is `CreationTime`.
    sort_by: "ModelSortKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The sort order for results. The default is `Ascending`.
    sort_order: "OrderKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the response to a previous `ListModels` request was truncated, the
    # response includes a `NextToken`. To retrieve the next set of models, use
    # the token in the next request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of models to return in the response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A string in the training job name. This filter returns only models in the
    # training job whose name contains the specified string.
    name_contains: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A filter that returns only models created before the specified time
    # (timestamp).
    creation_time_before: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only models created after the specified time
    # (timestamp).
    creation_time_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListModelsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "models",
                "Models",
                autoboto.TypeInfo(typing.List[ModelSummary]),
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

    # An array of `ModelSummary` objects, each of which lists a model.
    models: typing.List["ModelSummary"] = dataclasses.field(
        default_factory=list,
    )

    # If the response is truncated, Amazon SageMaker returns this token. To
    # retrieve the next set of models, use it in the subsequent request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListNotebookInstanceLifecycleConfigsInput(autoboto.ShapeBase):
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
            (
                "sort_by",
                "SortBy",
                autoboto.TypeInfo(NotebookInstanceLifecycleConfigSortKey),
            ),
            (
                "sort_order",
                "SortOrder",
                autoboto.TypeInfo(NotebookInstanceLifecycleConfigSortOrder),
            ),
            (
                "name_contains",
                "NameContains",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time_before",
                "CreationTimeBefore",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_time_after",
                "CreationTimeAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_before",
                "LastModifiedTimeBefore",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_after",
                "LastModifiedTimeAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # If the result of a `ListNotebookInstanceLifecycleConfigs` request was
    # truncated, the response includes a `NextToken`. To get the next set of
    # lifecycle configurations, use the token in the next request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of lifecycle configurations to return in the response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Sorts the list of results. The default is `CreationTime`.
    sort_by: "NotebookInstanceLifecycleConfigSortKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The sort order for results.
    sort_order: "NotebookInstanceLifecycleConfigSortOrder" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string in the lifecycle configuration name. This filter returns only
    # lifecycle configurations whose name contains the specified string.
    name_contains: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A filter that returns only lifecycle configurations that were created
    # before the specified time (timestamp).
    creation_time_before: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only lifecycle configurations that were created after
    # the specified time (timestamp).
    creation_time_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only lifecycle configurations that were modified
    # before the specified time (timestamp).
    last_modified_time_before: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only lifecycle configurations that were modified
    # after the specified time (timestamp).
    last_modified_time_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListNotebookInstanceLifecycleConfigsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "notebook_instance_lifecycle_configs",
                "NotebookInstanceLifecycleConfigs",
                autoboto.TypeInfo(
                    typing.List[NotebookInstanceLifecycleConfigSummary]
                ),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the response is truncated, Amazon SageMaker returns this token. To get
    # the next set of lifecycle configurations, use it in the next request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of `NotebookInstanceLifecycleConfiguration` objects, each listing
    # a lifecycle configuration.
    notebook_instance_lifecycle_configs: typing.List[
        "NotebookInstanceLifecycleConfigSummary"
    ] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListNotebookInstancesInput(autoboto.ShapeBase):
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
            (
                "sort_by",
                "SortBy",
                autoboto.TypeInfo(NotebookInstanceSortKey),
            ),
            (
                "sort_order",
                "SortOrder",
                autoboto.TypeInfo(NotebookInstanceSortOrder),
            ),
            (
                "name_contains",
                "NameContains",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time_before",
                "CreationTimeBefore",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_time_after",
                "CreationTimeAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_before",
                "LastModifiedTimeBefore",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_after",
                "LastModifiedTimeAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "status_equals",
                "StatusEquals",
                autoboto.TypeInfo(NotebookInstanceStatus),
            ),
            (
                "notebook_instance_lifecycle_config_name_contains",
                "NotebookInstanceLifecycleConfigNameContains",
                autoboto.TypeInfo(str),
            ),
        ]

    # If the previous call to the `ListNotebookInstances` is truncated, the
    # response includes a `NextToken`. You can use this token in your subsequent
    # `ListNotebookInstances` request to fetch the next set of notebook
    # instances.

    # You might specify a filter or a sort order in your request. When response
    # is truncated, you must use the same values for the filer and sort order in
    # the next request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of notebook instances to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The field to sort results by. The default is `Name`.
    sort_by: "NotebookInstanceSortKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The sort order for results.
    sort_order: "NotebookInstanceSortOrder" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string in the notebook instances' name. This filter returns only notebook
    # instances whose name contains the specified string.
    name_contains: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A filter that returns only notebook instances that were created before the
    # specified time (timestamp).
    creation_time_before: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only notebook instances that were created after the
    # specified time (timestamp).
    creation_time_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only notebook instances that were modified before the
    # specified time (timestamp).
    last_modified_time_before: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only notebook instances that were modified after the
    # specified time (timestamp).
    last_modified_time_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only notebook instances with the specified status.
    status_equals: "NotebookInstanceStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string in the name of a notebook instances lifecycle configuration
    # associated with this notebook instance. This filter returns only notebook
    # instances associated with a lifecycle configuration with a name that
    # contains the specified string.
    notebook_instance_lifecycle_config_name_contains: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListNotebookInstancesOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "notebook_instances",
                "NotebookInstances",
                autoboto.TypeInfo(typing.List[NotebookInstanceSummary]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the response to the previous `ListNotebookInstances` request was
    # truncated, Amazon SageMaker returns this token. To retrieve the next set of
    # notebook instances, use the token in the next request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of `NotebookInstanceSummary` objects, one for each notebook
    # instance.
    notebook_instances: typing.List["NotebookInstanceSummary"
                                   ] = dataclasses.field(
                                       default_factory=list,
                                   )


@dataclasses.dataclass
class ListTagsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
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

    # The Amazon Resource Name (ARN) of the resource whose tags you want to
    # retrieve.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the response to the previous `ListTags` request is truncated, Amazon
    # SageMaker returns this token. To retrieve the next set of tags, use it in
    # the subsequent request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Maximum number of tags to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsOutput(autoboto.OutputShapeBase):
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
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
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

    # An array of `Tag` objects, each with a tag key and a value.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # If response is truncated, Amazon SageMaker includes a token in the
    # response. You can use this token in your subsequent request to fetch next
    # set of tokens.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTrainingJobsForHyperParameterTuningJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hyper_parameter_tuning_job_name",
                "HyperParameterTuningJobName",
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
                "status_equals",
                "StatusEquals",
                autoboto.TypeInfo(TrainingJobStatus),
            ),
            (
                "sort_by",
                "SortBy",
                autoboto.TypeInfo(TrainingJobSortByOptions),
            ),
            (
                "sort_order",
                "SortOrder",
                autoboto.TypeInfo(SortOrder),
            ),
        ]

    # The name of the tuning job whose training jobs you want to list.
    hyper_parameter_tuning_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the result of the previous `ListTrainingJobsForHyperParameterTuningJob`
    # request was truncated, the response includes a `NextToken`. To retrieve the
    # next set of training jobs, use the token in the next request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of training jobs to return. The default value is 10.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A filter that returns only training jobs with the specified status.
    status_equals: "TrainingJobStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The field to sort results by. The default is `Name`.

    # If the value of this field is `FinalObjectiveMetricValue`, any training
    # jobs that did not return an objective metric are not listed.
    sort_by: "TrainingJobSortByOptions" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The sort order for results. The default is `Ascending`.
    sort_order: "SortOrder" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListTrainingJobsForHyperParameterTuningJobResponse(
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
                "training_job_summaries",
                "TrainingJobSummaries",
                autoboto.TypeInfo(
                    typing.List[HyperParameterTrainingJobSummary]
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

    # A list of TrainingJobSummary objects that describe the training jobs that
    # the `ListTrainingJobsForHyperParameterTuningJob` request returned.
    training_job_summaries: typing.List["HyperParameterTrainingJobSummary"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )

    # If the result of this `ListTrainingJobsForHyperParameterTuningJob` request
    # was truncated, the response includes a `NextToken`. To retrieve the next
    # set of training jobs, use the token in the next request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTrainingJobsRequest(autoboto.ShapeBase):
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
            (
                "creation_time_after",
                "CreationTimeAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_time_before",
                "CreationTimeBefore",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_after",
                "LastModifiedTimeAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_before",
                "LastModifiedTimeBefore",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "name_contains",
                "NameContains",
                autoboto.TypeInfo(str),
            ),
            (
                "status_equals",
                "StatusEquals",
                autoboto.TypeInfo(TrainingJobStatus),
            ),
            (
                "sort_by",
                "SortBy",
                autoboto.TypeInfo(SortBy),
            ),
            (
                "sort_order",
                "SortOrder",
                autoboto.TypeInfo(SortOrder),
            ),
        ]

    # If the result of the previous `ListTrainingJobs` request was truncated, the
    # response includes a `NextToken`. To retrieve the next set of training jobs,
    # use the token in the next request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of training jobs to return in the response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A filter that returns only training jobs created after the specified time
    # (timestamp).
    creation_time_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only training jobs created before the specified time
    # (timestamp).
    creation_time_before: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only training jobs modified after the specified time
    # (timestamp).
    last_modified_time_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only training jobs modified before the specified time
    # (timestamp).
    last_modified_time_before: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string in the training job name. This filter returns only training jobs
    # whose name contains the specified string.
    name_contains: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A filter that retrieves only training jobs with a specific status.
    status_equals: "TrainingJobStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The field to sort results by. The default is `CreationTime`.
    sort_by: "SortBy" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The sort order for results. The default is `Ascending`.
    sort_order: "SortOrder" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListTrainingJobsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "training_job_summaries",
                "TrainingJobSummaries",
                autoboto.TypeInfo(typing.List[TrainingJobSummary]),
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

    # An array of `TrainingJobSummary` objects, each listing a training job.
    training_job_summaries: typing.List["TrainingJobSummary"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )

    # If the response is truncated, Amazon SageMaker returns this token. To
    # retrieve the next set of training jobs, use it in the subsequent request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTransformJobsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "creation_time_after",
                "CreationTimeAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_time_before",
                "CreationTimeBefore",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_after",
                "LastModifiedTimeAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_before",
                "LastModifiedTimeBefore",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "name_contains",
                "NameContains",
                autoboto.TypeInfo(str),
            ),
            (
                "status_equals",
                "StatusEquals",
                autoboto.TypeInfo(TransformJobStatus),
            ),
            (
                "sort_by",
                "SortBy",
                autoboto.TypeInfo(SortBy),
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
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # A filter that returns only transform jobs created after the specified time.
    creation_time_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only transform jobs created before the specified
    # time.
    creation_time_before: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only transform jobs modified after the specified
    # time.
    last_modified_time_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that returns only transform jobs modified before the specified
    # time.
    last_modified_time_before: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string in the transform job name. This filter returns only transform jobs
    # whose name contains the specified string.
    name_contains: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A filter that retrieves only transform jobs with a specific status.
    status_equals: "TransformJobStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The field to sort results by. The default is `CreationTime`.
    sort_by: "SortBy" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The sort order for results. The default is `Descending`.
    sort_order: "SortOrder" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the result of the previous `ListTransformJobs` request was truncated,
    # the response includes a `NextToken`. To retrieve the next set of transform
    # jobs, use the token in the next request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of transform jobs to return in the response. The default
    # value is `10`.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTransformJobsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "transform_job_summaries",
                "TransformJobSummaries",
                autoboto.TypeInfo(typing.List[TransformJobSummary]),
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

    # An array of `TransformJobSummary` objects.
    transform_job_summaries: typing.List["TransformJobSummary"
                                        ] = dataclasses.field(
                                            default_factory=list,
                                        )

    # If the response is truncated, Amazon SageMaker returns this token. To
    # retrieve the next set of transform jobs, use it in the next request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricDefinition(autoboto.ShapeBase):
    """
    Specifies a metric that the training algorithm writes to `stderr` or `stdout`.
    Amazon SageMakerHyperparamter tuning captures all defined metrics. You specify
    one metric that a hyperparameter tuning job uses as its objective metric to
    choose the best training job.
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
                "regex",
                "Regex",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the metric.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A regular expression that searches the output of a training job and gets
    # the value of the metric. For more information about using regular
    # expressions to define metrics, see automatic-model-tuning-define-metrics.
    regex: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModelArtifacts(autoboto.ShapeBase):
    """
    Provides information about the location that is configured for storing model
    artifacts.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_model_artifacts",
                "S3ModelArtifacts",
                autoboto.TypeInfo(str),
            ),
        ]

    # The path of the S3 object that contains the model artifacts. For example,
    # `s3://bucket-name/keynameprefix/model.tar.gz`.
    s3_model_artifacts: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ModelSortKey(Enum):
    Name = "Name"
    CreationTime = "CreationTime"


@dataclasses.dataclass
class ModelSummary(autoboto.ShapeBase):
    """
    Provides summary information about a model.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "model_name",
                "ModelName",
                autoboto.TypeInfo(str),
            ),
            (
                "model_arn",
                "ModelArn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the model that you want a summary for.
    model_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the model.
    model_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A timestamp that indicates when the model was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class NotebookInstanceLifecycleConfigSortKey(Enum):
    Name = "Name"
    CreationTime = "CreationTime"
    LastModifiedTime = "LastModifiedTime"


class NotebookInstanceLifecycleConfigSortOrder(Enum):
    Ascending = "Ascending"
    Descending = "Descending"


@dataclasses.dataclass
class NotebookInstanceLifecycleConfigSummary(autoboto.ShapeBase):
    """
    Provides a summary of a notebook instance lifecycle configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_lifecycle_config_name",
                "NotebookInstanceLifecycleConfigName",
                autoboto.TypeInfo(str),
            ),
            (
                "notebook_instance_lifecycle_config_arn",
                "NotebookInstanceLifecycleConfigArn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the lifecycle configuration.
    notebook_instance_lifecycle_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the lifecycle configuration.
    notebook_instance_lifecycle_config_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp that tells when the lifecycle configuration was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp that tells when the lifecycle configuration was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NotebookInstanceLifecycleHook(autoboto.ShapeBase):
    """
    Contains the notebook instance lifecycle configuration script.

    Each lifecycle configuration script has a limit of 16384 characters.

    The value of the `$PATH` environment variable that is available to both scripts
    is `/sbin:bin:/usr/sbin:/usr/bin`.

    View CloudWatch Logs for notebook instance lifecycle configurations in log group
    `/aws/sagemaker/NotebookInstances` in log stream `[notebook-instance-
    name]/[LifecycleConfigHook]`.

    Lifecycle configuration scripts cannot run for longer than 5 minutes. If a
    script runs for longer than 5 minutes, it fails and the notebook instance is not
    created or started.

    For information about notebook instance lifestyle configurations, see notebook-
    lifecycle-config.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "content",
                "Content",
                autoboto.TypeInfo(str),
            ),
        ]

    # A base64-encoded string that contains a shell script for a notebook
    # instance lifecycle configuration.
    content: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class NotebookInstanceSortKey(Enum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class NotebookInstanceSortOrder(Enum):
    Ascending = "Ascending"
    Descending = "Descending"


class NotebookInstanceStatus(Enum):
    Pending = "Pending"
    InService = "InService"
    Stopping = "Stopping"
    Stopped = "Stopped"
    Failed = "Failed"
    Deleting = "Deleting"
    Updating = "Updating"


@dataclasses.dataclass
class NotebookInstanceSummary(autoboto.ShapeBase):
    """
    Provides summary information for an Amazon SageMaker notebook instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                autoboto.TypeInfo(str),
            ),
            (
                "notebook_instance_arn",
                "NotebookInstanceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "notebook_instance_status",
                "NotebookInstanceStatus",
                autoboto.TypeInfo(NotebookInstanceStatus),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                autoboto.TypeInfo(InstanceType),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "notebook_instance_lifecycle_config_name",
                "NotebookInstanceLifecycleConfigName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the notebook instance that you want a summary for.
    notebook_instance_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the notebook instance.
    notebook_instance_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the notebook instance.
    notebook_instance_status: "NotebookInstanceStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL that you use to connect to the Jupyter instance running in your
    # notebook instance.
    url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of ML compute instance that the notebook instance is running on.
    instance_type: "InstanceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the notebook instance was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the notebook instance was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of a notebook instance lifecycle configuration associated with
    # this notebook instance.

    # For information about notebook instance lifestyle configurations, see
    # notebook-lifecycle-config.
    notebook_instance_lifecycle_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ObjectiveStatus(Enum):
    Succeeded = "Succeeded"
    Pending = "Pending"
    Failed = "Failed"


@dataclasses.dataclass
class ObjectiveStatusCounters(autoboto.ShapeBase):
    """
    Specifies the number of training jobs that this hyperparameter tuning job
    launched, categorized by the status of their objective metric. The objective
    metric status shows whether the final objective metric for the training job has
    been evaluated by the tuning job and used in the hyperparameter tuning process.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "succeeded",
                "Succeeded",
                autoboto.TypeInfo(int),
            ),
            (
                "pending",
                "Pending",
                autoboto.TypeInfo(int),
            ),
            (
                "failed",
                "Failed",
                autoboto.TypeInfo(int),
            ),
        ]

    # The number of training jobs whose final objective metric was evaluated by
    # the hyperparameter tuning job and used in the hyperparameter tuning
    # process.
    succeeded: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of training jobs that are in progress and pending evaluation of
    # their final objective metric.
    pending: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of training jobs whose final objective metric was not evaluated
    # and used in the hyperparameter tuning process. This typically occurs when
    # the training job failed or did not emit an objective metric.
    failed: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class OrderKey(Enum):
    Ascending = "Ascending"
    Descending = "Descending"


@dataclasses.dataclass
class OutputDataConfig(autoboto.ShapeBase):
    """
    Provides information about how to store model training results (model
    artifacts).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_output_path",
                "S3OutputPath",
                autoboto.TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Identifies the S3 path where you want Amazon SageMaker to store the model
    # artifacts. For example, `s3://bucket-name/key-name-prefix`.
    s3_output_path: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to
    # encrypt the model artifacts at rest using Amazon S3 server-side encryption.

    # If you don't provide the KMS key ID, Amazon SageMaker uses the default KMS
    # key for Amazon S3 for your role's account. For more information, see [KMS-
    # Managed Encryption
    # Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html)
    # in Amazon Simple Storage Service developer guide.

    # The KMS key policy must grant permission to the IAM role you specify in
    # your `CreateTrainingJob` request. [Using Key Policies in AWS
    # KMS](http://docs.aws.amazon.com/kms/latest/developerguide/key-
    # policies.html) in the AWS Key Management Service Developer Guide.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ParameterRanges(autoboto.ShapeBase):
    """
    Specifies ranges of integer, continuous, and categorical hyperparameters that a
    hyperparameter tuning job searches.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "integer_parameter_ranges",
                "IntegerParameterRanges",
                autoboto.TypeInfo(typing.List[IntegerParameterRange]),
            ),
            (
                "continuous_parameter_ranges",
                "ContinuousParameterRanges",
                autoboto.TypeInfo(typing.List[ContinuousParameterRange]),
            ),
            (
                "categorical_parameter_ranges",
                "CategoricalParameterRanges",
                autoboto.TypeInfo(typing.List[CategoricalParameterRange]),
            ),
        ]

    # The array of IntegerParameterRange objects that specify ranges of integer
    # hyperparameters that a hyperparameter tuning job searches.
    integer_parameter_ranges: typing.List["IntegerParameterRange"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )

    # The array of ContinuousParameterRange objects that specify ranges of
    # continuous hyperparameters that a hyperparameter tuning job searches.
    continuous_parameter_ranges: typing.List["ContinuousParameterRange"
                                            ] = dataclasses.field(
                                                default_factory=list,
                                            )

    # The array of CategoricalParameterRange objects that specify ranges of
    # categorical hyperparameters that a hyperparameter tuning job searches.
    categorical_parameter_ranges: typing.List["CategoricalParameterRange"
                                             ] = dataclasses.field(
                                                 default_factory=list,
                                             )


@dataclasses.dataclass
class ProductionVariant(autoboto.ShapeBase):
    """
    Identifies a model that you want to host and the resources to deploy for hosting
    it. If you are deploying multiple models, tell Amazon SageMaker how to
    distribute traffic among the models by specifying variant weights.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "variant_name",
                "VariantName",
                autoboto.TypeInfo(str),
            ),
            (
                "model_name",
                "ModelName",
                autoboto.TypeInfo(str),
            ),
            (
                "initial_instance_count",
                "InitialInstanceCount",
                autoboto.TypeInfo(int),
            ),
            (
                "instance_type",
                "InstanceType",
                autoboto.TypeInfo(ProductionVariantInstanceType),
            ),
            (
                "initial_variant_weight",
                "InitialVariantWeight",
                autoboto.TypeInfo(float),
            ),
        ]

    # The name of the production variant.
    variant_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the model that you want to host. This is the name that you
    # specified when creating the model.
    model_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Number of instances to launch initially.
    initial_instance_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ML compute instance type.
    instance_type: "ProductionVariantInstanceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Determines initial traffic distribution among all of the models that you
    # specify in the endpoint configuration. The traffic to a production variant
    # is determined by the ratio of the `VariantWeight` to the sum of all
    # `VariantWeight` values across all ProductionVariants. If unspecified, it
    # defaults to 1.0.
    initial_variant_weight: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ProductionVariantInstanceType(Enum):
    ml_t2_medium = "ml.t2.medium"
    ml_t2_large = "ml.t2.large"
    ml_t2_xlarge = "ml.t2.xlarge"
    ml_t2_2xlarge = "ml.t2.2xlarge"
    ml_m4_xlarge = "ml.m4.xlarge"
    ml_m4_2xlarge = "ml.m4.2xlarge"
    ml_m4_4xlarge = "ml.m4.4xlarge"
    ml_m4_10xlarge = "ml.m4.10xlarge"
    ml_m4_16xlarge = "ml.m4.16xlarge"
    ml_m5_large = "ml.m5.large"
    ml_m5_xlarge = "ml.m5.xlarge"
    ml_m5_2xlarge = "ml.m5.2xlarge"
    ml_m5_4xlarge = "ml.m5.4xlarge"
    ml_m5_12xlarge = "ml.m5.12xlarge"
    ml_m5_24xlarge = "ml.m5.24xlarge"
    ml_c4_large = "ml.c4.large"
    ml_c4_xlarge = "ml.c4.xlarge"
    ml_c4_2xlarge = "ml.c4.2xlarge"
    ml_c4_4xlarge = "ml.c4.4xlarge"
    ml_c4_8xlarge = "ml.c4.8xlarge"
    ml_p2_xlarge = "ml.p2.xlarge"
    ml_p2_8xlarge = "ml.p2.8xlarge"
    ml_p2_16xlarge = "ml.p2.16xlarge"
    ml_p3_2xlarge = "ml.p3.2xlarge"
    ml_p3_8xlarge = "ml.p3.8xlarge"
    ml_p3_16xlarge = "ml.p3.16xlarge"
    ml_c5_large = "ml.c5.large"
    ml_c5_xlarge = "ml.c5.xlarge"
    ml_c5_2xlarge = "ml.c5.2xlarge"
    ml_c5_4xlarge = "ml.c5.4xlarge"
    ml_c5_9xlarge = "ml.c5.9xlarge"
    ml_c5_18xlarge = "ml.c5.18xlarge"


@dataclasses.dataclass
class ProductionVariantSummary(autoboto.ShapeBase):
    """
    Describes weight and capacities for a production variant associated with an
    endpoint. If you sent a request to the `UpdateEndpointWeightsAndCapacities` API
    and the endpoint status is `Updating`, you get different desired and current
    values.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "variant_name",
                "VariantName",
                autoboto.TypeInfo(str),
            ),
            (
                "deployed_images",
                "DeployedImages",
                autoboto.TypeInfo(typing.List[DeployedImage]),
            ),
            (
                "current_weight",
                "CurrentWeight",
                autoboto.TypeInfo(float),
            ),
            (
                "desired_weight",
                "DesiredWeight",
                autoboto.TypeInfo(float),
            ),
            (
                "current_instance_count",
                "CurrentInstanceCount",
                autoboto.TypeInfo(int),
            ),
            (
                "desired_instance_count",
                "DesiredInstanceCount",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the variant.
    variant_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of `DeployedImage` objects that specify the Amazon EC2 Container
    # Registry paths of the inference images deployed on instances of this
    # `ProductionVariant`.
    deployed_images: typing.List["DeployedImage"] = dataclasses.field(
        default_factory=list,
    )

    # The weight associated with the variant.
    current_weight: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The requested weight, as specified in the
    # `UpdateEndpointWeightsAndCapacities` request.
    desired_weight: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of instances associated with the variant.
    current_instance_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of instances requested in the
    # `UpdateEndpointWeightsAndCapacities` request.
    desired_instance_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class RecordWrapper(Enum):
    NONE = "None"
    RECORDIO = "RecordIO"


@dataclasses.dataclass
class ResourceConfig(autoboto.ShapeBase):
    """
    Describes the resources, including ML compute instances and ML storage volumes,
    to use for model training.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_type",
                "InstanceType",
                autoboto.TypeInfo(TrainingInstanceType),
            ),
            (
                "instance_count",
                "InstanceCount",
                autoboto.TypeInfo(int),
            ),
            (
                "volume_size_in_gb",
                "VolumeSizeInGB",
                autoboto.TypeInfo(int),
            ),
            (
                "volume_kms_key_id",
                "VolumeKmsKeyId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ML compute instance type.
    instance_type: "TrainingInstanceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of ML compute instances to use. For distributed training,
    # provide a value greater than 1.
    instance_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The size of the ML storage volume that you want to provision.

    # ML storage volumes store model artifacts and incremental states. Training
    # algorithms might also use the ML storage volume for scratch space. If you
    # want to store the training data in the ML storage volume, choose `File` as
    # the `TrainingInputMode` in the algorithm specification.

    # You must specify sufficient ML storage for your scenario.

    # Amazon SageMaker supports only the General Purpose SSD (gp2) ML storage
    # volume type.
    volume_size_in_gb: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of a AWS Key Management Service key that
    # Amazon SageMaker uses to encrypt data on the storage volume attached to the
    # ML compute instance(s) that run the training job.
    volume_kms_key_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceInUse(autoboto.ShapeBase):
    """
    Resource being accessed is in use.
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
class ResourceLimitExceeded(autoboto.ShapeBase):
    """
    You have exceeded an Amazon SageMaker resource limit. For example, you might
    have too many training jobs created.
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
class ResourceLimits(autoboto.ShapeBase):
    """
    Specifies the maximum number of training jobs and parallel training jobs that a
    hyperparameter tuning job can launch.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_number_of_training_jobs",
                "MaxNumberOfTrainingJobs",
                autoboto.TypeInfo(int),
            ),
            (
                "max_parallel_training_jobs",
                "MaxParallelTrainingJobs",
                autoboto.TypeInfo(int),
            ),
        ]

    # The maximum number of training jobs that a hyperparameter tuning job can
    # launch.
    max_number_of_training_jobs: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of concurrent training jobs that a hyperparameter tuning
    # job can launch.
    max_parallel_training_jobs: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceNotFound(autoboto.ShapeBase):
    """
    Resource being access is not found.
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


class S3DataDistribution(Enum):
    FullyReplicated = "FullyReplicated"
    ShardedByS3Key = "ShardedByS3Key"


@dataclasses.dataclass
class S3DataSource(autoboto.ShapeBase):
    """
    Describes the S3 data source.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_data_type",
                "S3DataType",
                autoboto.TypeInfo(S3DataType),
            ),
            (
                "s3_uri",
                "S3Uri",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_data_distribution_type",
                "S3DataDistributionType",
                autoboto.TypeInfo(S3DataDistribution),
            ),
        ]

    # If you choose `S3Prefix`, `S3Uri` identifies a key name prefix. Amazon
    # SageMaker uses all objects with the specified key name prefix for model
    # training.

    # If you choose `ManifestFile`, `S3Uri` identifies an object that is a
    # manifest file containing a list of object keys that you want Amazon
    # SageMaker to use for model training.
    s3_data_type: "S3DataType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Depending on the value specified for the `S3DataType`, identifies either a
    # key name prefix or a manifest. For example:

    #   * A key name prefix might look like this: `s3://bucketname/exampleprefix`.

    #   * A manifest might look like this: `s3://bucketname/example.manifest`

    # The manifest is an S3 object which is a JSON file with the following
    # format:

    # `[`

    # ` {"prefix": "s3://customer_bucket/some/prefix/"},`

    # ` "relative/path/to/custdata-1",`

    # ` "relative/path/custdata-2",`

    # ` ...`

    # ` ]`

    # The preceding JSON matches the following `s3Uris`:

    # `s3://customer_bucket/some/prefix/relative/path/to/custdata-1`

    # `s3://customer_bucket/some/prefix/relative/path/custdata-1`

    # `...`

    # The complete set of `s3uris` in this manifest constitutes the input data
    # for the channel for this datasource. The object that each `s3uris` points
    # to must readable by the IAM role that Amazon SageMaker uses to perform
    # tasks on your behalf.
    s3_uri: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If you want Amazon SageMaker to replicate the entire dataset on each ML
    # compute instance that is launched for model training, specify
    # `FullyReplicated`.

    # If you want Amazon SageMaker to replicate a subset of data on each ML
    # compute instance that is launched for model training, specify
    # `ShardedByS3Key`. If there are _n_ ML compute instances launched for a
    # training job, each instance gets approximately 1/ _n_ of the number of S3
    # objects. In this case, model training on each machine uses only the subset
    # of training data.

    # Don't choose more ML compute instances for training than available S3
    # objects. If you do, some nodes won't get any data and you will pay for
    # nodes that aren't getting any training data. This applies in both FILE and
    # PIPE modes. Keep this in mind when developing algorithms.

    # In distributed training, where you use multiple ML compute EC2 instances,
    # you might choose `ShardedByS3Key`. If the algorithm requires copying
    # training data to the ML storage volume (when `TrainingInputMode` is set to
    # `File`), this copies 1/ _n_ of the number of objects.
    s3_data_distribution_type: "S3DataDistribution" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class S3DataType(Enum):
    ManifestFile = "ManifestFile"
    S3Prefix = "S3Prefix"


class SecondaryStatus(Enum):
    Starting = "Starting"
    LaunchingMLInstances = "LaunchingMLInstances"
    PreparingTrainingStack = "PreparingTrainingStack"
    Downloading = "Downloading"
    DownloadingTrainingImage = "DownloadingTrainingImage"
    Training = "Training"
    Uploading = "Uploading"
    Stopping = "Stopping"
    Stopped = "Stopped"
    MaxRuntimeExceeded = "MaxRuntimeExceeded"
    Completed = "Completed"
    Failed = "Failed"


@dataclasses.dataclass
class SecondaryStatusTransition(autoboto.ShapeBase):
    """
    Specifies a secondary status the job has transitioned into. It includes a start
    timestamp and later an end timestamp. The end timestamp is added either after
    the job transitions to a different secondary status or after the job has ended.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                autoboto.TypeInfo(SecondaryStatus),
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
                "status_message",
                "StatusMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # Provides granular information about the system state. For more information,
    # see `SecondaryStatus` under the DescribeTrainingJob response elements.
    status: "SecondaryStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the training job has entered this secondary
    # status.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the secondary status has ended and the job has
    # transitioned into another secondary status. The `EndTime` timestamp is also
    # set after the training job has ended.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Shows a brief description and other information about the secondary status.
    # For example, the `LaunchingMLInstances` secondary status could show a
    # status message of "Insufficent capacity error while launching instances".
    status_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class SortBy(Enum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class SortOrder(Enum):
    Ascending = "Ascending"
    Descending = "Descending"


class SplitType(Enum):
    NONE = "None"
    LINE = "Line"
    RECORDIO = "RecordIO"


@dataclasses.dataclass
class StartNotebookInstanceInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the notebook instance to start.
    notebook_instance_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopHyperParameterTuningJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hyper_parameter_tuning_job_name",
                "HyperParameterTuningJobName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the tuning job to stop.
    hyper_parameter_tuning_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopNotebookInstanceInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the notebook instance to terminate.
    notebook_instance_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopTrainingJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "training_job_name",
                "TrainingJobName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the training job to stop.
    training_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopTransformJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "transform_job_name",
                "TransformJobName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the transform job to stop.
    transform_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StoppingCondition(autoboto.ShapeBase):
    """
    Specifies how long model training can run. When model training reaches the
    limit, Amazon SageMaker ends the training job. Use this API to cap model
    training cost.

    To stop a job, Amazon SageMaker sends the algorithm the `SIGTERM` signal, which
    delays job termination for120 seconds. Algorithms might use this 120-second
    window to save the model artifacts, so the results of training is not lost.

    Training algorithms provided by Amazon SageMaker automatically saves the
    intermediate results of a model training job (it is best effort case, as model
    might not be ready to save as some stages, for example training just started).
    This intermediate data is a valid model artifact. You can use it to create a
    model (`CreateModel`).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_runtime_in_seconds",
                "MaxRuntimeInSeconds",
                autoboto.TypeInfo(int),
            ),
        ]

    # The maximum length of time, in seconds, that the training job can run. If
    # model training does not complete during this time, Amazon SageMaker ends
    # the job. If value is not specified, default value is 1 day. Maximum value
    # is 5 days.
    max_runtime_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    """
    Describes a tag.
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

    # The tag key.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tag value.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class TrainingInputMode(Enum):
    Pipe = "Pipe"
    File = "File"


class TrainingInstanceType(Enum):
    ml_m4_xlarge = "ml.m4.xlarge"
    ml_m4_2xlarge = "ml.m4.2xlarge"
    ml_m4_4xlarge = "ml.m4.4xlarge"
    ml_m4_10xlarge = "ml.m4.10xlarge"
    ml_m4_16xlarge = "ml.m4.16xlarge"
    ml_m5_large = "ml.m5.large"
    ml_m5_xlarge = "ml.m5.xlarge"
    ml_m5_2xlarge = "ml.m5.2xlarge"
    ml_m5_4xlarge = "ml.m5.4xlarge"
    ml_m5_12xlarge = "ml.m5.12xlarge"
    ml_m5_24xlarge = "ml.m5.24xlarge"
    ml_c4_xlarge = "ml.c4.xlarge"
    ml_c4_2xlarge = "ml.c4.2xlarge"
    ml_c4_4xlarge = "ml.c4.4xlarge"
    ml_c4_8xlarge = "ml.c4.8xlarge"
    ml_p2_xlarge = "ml.p2.xlarge"
    ml_p2_8xlarge = "ml.p2.8xlarge"
    ml_p2_16xlarge = "ml.p2.16xlarge"
    ml_p3_2xlarge = "ml.p3.2xlarge"
    ml_p3_8xlarge = "ml.p3.8xlarge"
    ml_p3_16xlarge = "ml.p3.16xlarge"
    ml_c5_xlarge = "ml.c5.xlarge"
    ml_c5_2xlarge = "ml.c5.2xlarge"
    ml_c5_4xlarge = "ml.c5.4xlarge"
    ml_c5_9xlarge = "ml.c5.9xlarge"
    ml_c5_18xlarge = "ml.c5.18xlarge"


class TrainingJobSortByOptions(Enum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"
    FinalObjectiveMetricValue = "FinalObjectiveMetricValue"


class TrainingJobStatus(Enum):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Stopping = "Stopping"
    Stopped = "Stopped"


@dataclasses.dataclass
class TrainingJobStatusCounters(autoboto.ShapeBase):
    """
    The numbers of training jobs launched by a hyperparameter tuning job,
    categorized by status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "completed",
                "Completed",
                autoboto.TypeInfo(int),
            ),
            (
                "in_progress",
                "InProgress",
                autoboto.TypeInfo(int),
            ),
            (
                "retryable_error",
                "RetryableError",
                autoboto.TypeInfo(int),
            ),
            (
                "non_retryable_error",
                "NonRetryableError",
                autoboto.TypeInfo(int),
            ),
            (
                "stopped",
                "Stopped",
                autoboto.TypeInfo(int),
            ),
        ]

    # The number of completed training jobs launched by a hyperparameter tuning
    # job.
    completed: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of in-progress training jobs launched by a hyperparameter tuning
    # job.
    in_progress: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of training jobs that failed, but can be retried. A failed
    # training job can be retried only if it failed because an internal service
    # error occurred.
    retryable_error: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of training jobs that failed and can't be retried. A failed
    # training job can't be retried if it failed because a client error occurred.
    non_retryable_error: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of training jobs launched by a hyperparameter tuning job that
    # were manually stopped.
    stopped: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TrainingJobSummary(autoboto.ShapeBase):
    """
    Provides summary information about a training job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "training_job_name",
                "TrainingJobName",
                autoboto.TypeInfo(str),
            ),
            (
                "training_job_arn",
                "TrainingJobArn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "training_job_status",
                "TrainingJobStatus",
                autoboto.TypeInfo(TrainingJobStatus),
            ),
            (
                "training_end_time",
                "TrainingEndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the training job that you want a summary for.
    training_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the training job.
    training_job_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the training job was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the training job.
    training_job_status: "TrainingJobStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the training job ended. This field is set only
    # if the training job has one of the terminal statuses (`Completed`,
    # `Failed`, or `Stopped`).
    training_end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Timestamp when the training job was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TransformDataSource(autoboto.ShapeBase):
    """
    Describes the location of the channel data.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_data_source",
                "S3DataSource",
                autoboto.TypeInfo(TransformS3DataSource),
            ),
        ]

    # The S3 location of the data source that is associated with a channel.
    s3_data_source: "TransformS3DataSource" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class TransformInput(autoboto.ShapeBase):
    """
    Describes the input source of a transform job and the way the transform job
    consumes it.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source",
                "DataSource",
                autoboto.TypeInfo(TransformDataSource),
            ),
            (
                "content_type",
                "ContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "compression_type",
                "CompressionType",
                autoboto.TypeInfo(CompressionType),
            ),
            (
                "split_type",
                "SplitType",
                autoboto.TypeInfo(SplitType),
            ),
        ]

    # Describes the location of the channel data, meaning the S3 location of the
    # input data that the model can consume.
    data_source: "TransformDataSource" = dataclasses.field(
        default_factory=dict,
    )

    # The multipurpose internet mail extension (MIME) type of the data. Amazon
    # SageMaker uses the MIME type with each http call to transfer data to the
    # transform job.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Compressing data helps save on storage space. If your transform data is
    # compressed, specify the compression type.and Amazon SageMaker will
    # automatically decompress the data for the transform job accordingly. The
    # default value is `None`.
    compression_type: "CompressionType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The method to use to split the transform job's data into smaller batches.
    # The default value is `None`. If you don't want to split the data, specify
    # `None`. If you want to split records on a newline character boundary,
    # specify `Line`. To split records according to the RecordIO format, specify
    # `RecordIO`.

    # Amazon SageMaker will send maximum number of records per batch in each
    # request up to the MaxPayloadInMB limit. For more information, see [RecordIO
    # data format](http://mxnet.io/architecture/note_data_loading.html#data-
    # format).

    # For information about the `RecordIO` format, see [Data
    # Format](http://mxnet.io/architecture/note_data_loading.html#data-format).
    split_type: "SplitType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class TransformInstanceType(Enum):
    ml_m4_xlarge = "ml.m4.xlarge"
    ml_m4_2xlarge = "ml.m4.2xlarge"
    ml_m4_4xlarge = "ml.m4.4xlarge"
    ml_m4_10xlarge = "ml.m4.10xlarge"
    ml_m4_16xlarge = "ml.m4.16xlarge"
    ml_c4_xlarge = "ml.c4.xlarge"
    ml_c4_2xlarge = "ml.c4.2xlarge"
    ml_c4_4xlarge = "ml.c4.4xlarge"
    ml_c4_8xlarge = "ml.c4.8xlarge"
    ml_p2_xlarge = "ml.p2.xlarge"
    ml_p2_8xlarge = "ml.p2.8xlarge"
    ml_p2_16xlarge = "ml.p2.16xlarge"
    ml_p3_2xlarge = "ml.p3.2xlarge"
    ml_p3_8xlarge = "ml.p3.8xlarge"
    ml_p3_16xlarge = "ml.p3.16xlarge"
    ml_c5_xlarge = "ml.c5.xlarge"
    ml_c5_2xlarge = "ml.c5.2xlarge"
    ml_c5_4xlarge = "ml.c5.4xlarge"
    ml_c5_9xlarge = "ml.c5.9xlarge"
    ml_c5_18xlarge = "ml.c5.18xlarge"
    ml_m5_large = "ml.m5.large"
    ml_m5_xlarge = "ml.m5.xlarge"
    ml_m5_2xlarge = "ml.m5.2xlarge"
    ml_m5_4xlarge = "ml.m5.4xlarge"
    ml_m5_12xlarge = "ml.m5.12xlarge"
    ml_m5_24xlarge = "ml.m5.24xlarge"


class TransformJobStatus(Enum):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Stopping = "Stopping"
    Stopped = "Stopped"


@dataclasses.dataclass
class TransformJobSummary(autoboto.ShapeBase):
    """
    Provides a summary information for a transform job. Multiple TransformJobSummary
    objects are returned as a list after calling ListTransformJobs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "transform_job_name",
                "TransformJobName",
                autoboto.TypeInfo(str),
            ),
            (
                "transform_job_arn",
                "TransformJobArn",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "transform_job_status",
                "TransformJobStatus",
                autoboto.TypeInfo(TransformJobStatus),
            ),
            (
                "transform_end_time",
                "TransformEndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "failure_reason",
                "FailureReason",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the transform job.
    transform_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the transform job.
    transform_job_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the transform Job was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the transform job.
    transform_job_status: "TransformJobStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates when the transform job ends on compute instances. For successful
    # jobs and stopped jobs, this is the exact time recorded after the results
    # are uploaded. For failed jobs, this is when Amazon SageMaker detected that
    # the job failed.
    transform_end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates when the transform job was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the transform job failed, the reason it failed.
    failure_reason: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TransformOutput(autoboto.ShapeBase):
    """
    Describes the results of a transform job output.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_output_path",
                "S3OutputPath",
                autoboto.TypeInfo(str),
            ),
            (
                "accept",
                "Accept",
                autoboto.TypeInfo(str),
            ),
            (
                "assemble_with",
                "AssembleWith",
                autoboto.TypeInfo(AssemblyType),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon S3 path where you want Amazon SageMaker to store the results of
    # the transform job. For example, `s3://bucket-name/key-name-prefix`.

    # For every S3 object used as input for the transform job, the transformed
    # data is stored in a corresponding subfolder in the location under the
    # output prefix. For example, the input data `s3://bucket-name/input-name-
    # prefix/dataset01/data.csv` will have the transformed data stored at
    # `s3://bucket-name/key-name-prefix/dataset01/`, based on the original name,
    # as a series of .part files (.part0001, part0002, etc).
    s3_output_path: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The MIME type used to specify the output data. Amazon SageMaker uses the
    # MIME type with each http call to transfer data from the transform job.
    accept: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Defines how to assemble the results of the transform job as a single S3
    # object. You should select a format that is most convenient to you. To
    # concatenate the results in binary format, specify `None`. To add a newline
    # character at the end of every transformed record, specify `Line`. To
    # assemble the output in RecordIO format, specify `RecordIO`. The default
    # value is `None`.

    # For information about the `RecordIO` format, see [Data
    # Format](http://mxnet.io/architecture/note_data_loading.html#data-format).
    assemble_with: "AssemblyType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS Key Management Service (AWS KMS) key for Amazon S3 server-side
    # encryption that Amazon SageMaker uses to encrypt the transformed data.

    # If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS
    # key for Amazon S3 for your role's account. For more information, see [KMS-
    # Managed Encryption
    # Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html)
    # in the _Amazon Simple Storage Service Developer Guide._

    # The KMS key policy must grant permission to the IAM role that you specify
    # in your `CreateTramsformJob` request. For more information, see [Using Key
    # Policies in AWS
    # KMS](http://docs.aws.amazon.com/kms/latest/developerguide/key-
    # policies.html) in the _AWS Key Management Service Developer Guide_.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TransformResources(autoboto.ShapeBase):
    """
    Describes the resources, including ML instance types and ML instance count, to
    use for transform job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_type",
                "InstanceType",
                autoboto.TypeInfo(TransformInstanceType),
            ),
            (
                "instance_count",
                "InstanceCount",
                autoboto.TypeInfo(int),
            ),
            (
                "volume_kms_key_id",
                "VolumeKmsKeyId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ML compute instance type for the transform job. For using built-in
    # algorithms to transform moderately sized datasets, ml.m4.xlarge or
    # `ml.m5.large` should suffice. There is no default value for `InstanceType`.
    instance_type: "TransformInstanceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of ML compute instances to use in the transform job. For
    # distributed transform, provide a value greater than 1. The default value is
    # `1`.
    instance_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of a AWS Key Management Service key that
    # Amazon SageMaker uses to encrypt data on the storage volume attached to the
    # ML compute instance(s) that run the batch transform job.
    volume_kms_key_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TransformS3DataSource(autoboto.ShapeBase):
    """
    Describes the S3 data source.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_data_type",
                "S3DataType",
                autoboto.TypeInfo(S3DataType),
            ),
            (
                "s3_uri",
                "S3Uri",
                autoboto.TypeInfo(str),
            ),
        ]

    # If you choose `S3Prefix`, `S3Uri` identifies a key name prefix. Amazon
    # SageMaker uses all objects with the specified key name prefix for batch
    # transform.

    # If you choose `ManifestFile`, `S3Uri` identifies an object that is a
    # manifest file containing a list of object keys that you want Amazon
    # SageMaker to use for batch transform.
    s3_data_type: "S3DataType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Depending on the value specified for the `S3DataType`, identifies either a
    # key name prefix or a manifest. For example:

    #   * A key name prefix might look like this: `s3://bucketname/exampleprefix`.

    #   * A manifest might look like this: `s3://bucketname/example.manifest`

    # The manifest is an S3 object which is a JSON file with the following
    # format:

    # `[`

    # ` {"prefix": "s3://customer_bucket/some/prefix/"},`

    # ` "relative/path/to/custdata-1",`

    # ` "relative/path/custdata-2",`

    # ` ...`

    # ` ]`

    # The preceding JSON matches the following `S3Uris`:

    # `s3://customer_bucket/some/prefix/relative/path/to/custdata-1`

    # `s3://customer_bucket/some/prefix/relative/path/custdata-1`

    # `...`

    # The complete set of `S3Uris` in this manifest constitutes the input data
    # for the channel for this datasource. The object that each `S3Uris` points
    # to must be readable by the IAM role that Amazon SageMaker uses to perform
    # tasks on your behalf.
    s3_uri: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateEndpointInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint_config_name",
                "EndpointConfigName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the endpoint whose configuration you want to update.
    endpoint_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the new endpoint configuration.
    endpoint_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateEndpointOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_arn",
                "EndpointArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the endpoint.
    endpoint_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateEndpointWeightsAndCapacitiesInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                autoboto.TypeInfo(str),
            ),
            (
                "desired_weights_and_capacities",
                "DesiredWeightsAndCapacities",
                autoboto.TypeInfo(typing.List[DesiredWeightAndCapacity]),
            ),
        ]

    # The name of an existing Amazon SageMaker endpoint.
    endpoint_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An object that provides new capacity and weight values for a variant.
    desired_weights_and_capacities: typing.List["DesiredWeightAndCapacity"
                                               ] = dataclasses.field(
                                                   default_factory=list,
                                               )


@dataclasses.dataclass
class UpdateEndpointWeightsAndCapacitiesOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_arn",
                "EndpointArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the updated endpoint.
    endpoint_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateNotebookInstanceInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                autoboto.TypeInfo(InstanceType),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "lifecycle_config_name",
                "LifecycleConfigName",
                autoboto.TypeInfo(str),
            ),
            (
                "disassociate_lifecycle_config",
                "DisassociateLifecycleConfig",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the notebook instance to update.
    notebook_instance_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon ML compute instance type.
    instance_type: "InstanceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker can
    # assume to access the notebook instance. For more information, see [Amazon
    # SageMaker Roles](http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-
    # roles.html).

    # To be able to pass this role to Amazon SageMaker, the caller of this API
    # must have the `iam:PassRole` permission.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of a lifecycle configuration to associate with the notebook
    # instance. For information about lifestyle configurations, see notebook-
    # lifecycle-config.
    lifecycle_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Set to `true` to remove the notebook instance lifecycle configuration
    # currently associated with the notebook instance.
    disassociate_lifecycle_config: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateNotebookInstanceLifecycleConfigInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_lifecycle_config_name",
                "NotebookInstanceLifecycleConfigName",
                autoboto.TypeInfo(str),
            ),
            (
                "on_create",
                "OnCreate",
                autoboto.TypeInfo(typing.List[NotebookInstanceLifecycleHook]),
            ),
            (
                "on_start",
                "OnStart",
                autoboto.TypeInfo(typing.List[NotebookInstanceLifecycleHook]),
            ),
        ]

    # The name of the lifecycle configuration.
    notebook_instance_lifecycle_config_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The shell script that runs only once, when you create a notebook instance
    on_create: typing.List["NotebookInstanceLifecycleHook"] = dataclasses.field(
        default_factory=list,
    )

    # The shell script that runs every time you start a notebook instance,
    # including when you create the notebook instance.
    on_start: typing.List["NotebookInstanceLifecycleHook"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateNotebookInstanceLifecycleConfigOutput(autoboto.OutputShapeBase):
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
class UpdateNotebookInstanceOutput(autoboto.OutputShapeBase):
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
class VpcConfig(autoboto.ShapeBase):
    """
    Specifies a VPC that your training jobs and hosted models have access to.
    Control access to and from your training and model containers by configuring the
    VPC. For more information, see host-vpc and train-vpc.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_group_ids",
                "SecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "subnets",
                "Subnets",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security
    # groups for the VPC that is specified in the `Subnets` field.
    security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The ID of the subnets in the VPC to which you want to connect your training
    # job or model.
    subnets: typing.List[str] = dataclasses.field(default_factory=list, )
