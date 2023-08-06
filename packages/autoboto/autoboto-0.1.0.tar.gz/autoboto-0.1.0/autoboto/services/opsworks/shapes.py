import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AgentVersion(autoboto.ShapeBase):
    """
    Describes an agent version.
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
                "configuration_manager",
                "ConfigurationManager",
                autoboto.TypeInfo(StackConfigurationManager),
            ),
        ]

    # The agent version.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The configuration manager.
    configuration_manager: "StackConfigurationManager" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class App(autoboto.ShapeBase):
    """
    A description of the app.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "app_id",
                "AppId",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "shortname",
                "Shortname",
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
                "data_sources",
                "DataSources",
                autoboto.TypeInfo(typing.List[DataSource]),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(AppType),
            ),
            (
                "app_source",
                "AppSource",
                autoboto.TypeInfo(Source),
            ),
            (
                "domains",
                "Domains",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "enable_ssl",
                "EnableSsl",
                autoboto.TypeInfo(bool),
            ),
            (
                "ssl_configuration",
                "SslConfiguration",
                autoboto.TypeInfo(SslConfiguration),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[AppAttributesKeys, str]),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "environment",
                "Environment",
                autoboto.TypeInfo(typing.List[EnvironmentVariable]),
            ),
        ]

    # The app ID.
    app_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The app stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The app's short name.
    shortname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The app name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A description of the app.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The app's data sources.
    data_sources: typing.List["DataSource"] = dataclasses.field(
        default_factory=list,
    )

    # The app type.
    type: "AppType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A `Source` object that describes the app repository.
    app_source: "Source" = dataclasses.field(default_factory=dict, )

    # The app vhost settings with multiple domains separated by commas. For
    # example: `'www.example.com, example.com'`
    domains: typing.List[str] = dataclasses.field(default_factory=list, )

    # Whether to enable SSL for the app.
    enable_ssl: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An `SslConfiguration` object with the SSL configuration.
    ssl_configuration: "SslConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The stack attributes.
    attributes: typing.Dict["AppAttributesKeys", str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When the app was created.
    created_at: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of `EnvironmentVariable` objects that specify environment
    # variables to be associated with the app. After you deploy the app, these
    # variables are defined on the associated app server instances. For more
    # information, see [ Environment
    # Variables](http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-
    # creating.html#workingapps-creating-environment).

    # There is no specific limit on the number of environment variables. However,
    # the size of the associated data structure - which includes the variable
    # names, values, and protected flag values - cannot exceed 10 KB (10240
    # Bytes). This limit should accommodate most if not all use cases, but if you
    # do exceed it, you will cause an exception (API) with an "Environment: is
    # too large (maximum is 10KB)" message.
    environment: typing.List["EnvironmentVariable"] = dataclasses.field(
        default_factory=list,
    )


class AppAttributesKeys(Enum):
    DocumentRoot = "DocumentRoot"
    RailsEnv = "RailsEnv"
    AutoBundleOnDeploy = "AutoBundleOnDeploy"
    AwsFlowRubySettings = "AwsFlowRubySettings"


class AppType(Enum):
    aws_flow_ruby = "aws-flow-ruby"
    java = "java"
    rails = "rails"
    php = "php"
    nodejs = "nodejs"
    static = "static"
    other = "other"


class Architecture(Enum):
    x86_64 = "x86_64"
    i386 = "i386"


@dataclasses.dataclass
class AssignInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_ids",
                "LayerIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The layer ID, which must correspond to a custom layer. You cannot assign a
    # registered instance to a built-in layer.
    layer_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class AssignVolumeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_id",
                "VolumeId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The volume ID.
    volume_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateElasticIpRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "elastic_ip",
                "ElasticIp",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Elastic IP address.
    elastic_ip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachElasticLoadBalancerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "elastic_load_balancer_name",
                "ElasticLoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_id",
                "LayerId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Elastic Load Balancing instance's name.
    elastic_load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the layer to which the Elastic Load Balancing instance is to be
    # attached.
    layer_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AutoScalingThresholds(autoboto.ShapeBase):
    """
    Describes a load-based auto scaling upscaling or downscaling threshold
    configuration, which specifies when AWS OpsWorks Stacks starts or stops load-
    based instances.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_count",
                "InstanceCount",
                autoboto.TypeInfo(int),
            ),
            (
                "thresholds_wait_time",
                "ThresholdsWaitTime",
                autoboto.TypeInfo(int),
            ),
            (
                "ignore_metrics_time",
                "IgnoreMetricsTime",
                autoboto.TypeInfo(int),
            ),
            (
                "cpu_threshold",
                "CpuThreshold",
                autoboto.TypeInfo(float),
            ),
            (
                "memory_threshold",
                "MemoryThreshold",
                autoboto.TypeInfo(float),
            ),
            (
                "load_threshold",
                "LoadThreshold",
                autoboto.TypeInfo(float),
            ),
            (
                "alarms",
                "Alarms",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The number of instances to add or remove when the load exceeds a threshold.
    instance_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The amount of time, in minutes, that the load must exceed a threshold
    # before more instances are added or removed.
    thresholds_wait_time: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The amount of time (in minutes) after a scaling event occurs that AWS
    # OpsWorks Stacks should ignore metrics and suppress additional scaling
    # events. For example, AWS OpsWorks Stacks adds new instances following an
    # upscaling event but the instances won't start reducing the load until they
    # have been booted and configured. There is no point in raising additional
    # scaling events during that operation, which typically takes several
    # minutes. `IgnoreMetricsTime` allows you to direct AWS OpsWorks Stacks to
    # suppress scaling events long enough to get the new instances online.
    ignore_metrics_time: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The CPU utilization threshold, as a percent of the available CPU. A value
    # of -1 disables the threshold.
    cpu_threshold: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The memory utilization threshold, as a percent of the available memory. A
    # value of -1 disables the threshold.
    memory_threshold: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The load threshold. A value of -1 disables the threshold. For more
    # information about how load is computed, see [Load
    # (computing)](http://en.wikipedia.org/wiki/Load_%28computing%29).
    load_threshold: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Custom Cloudwatch auto scaling alarms, to be used as thresholds. This
    # parameter takes a list of up to five alarm names, which are case sensitive
    # and must be in the same region as the stack.

    # To use custom alarms, you must update your service role to allow
    # `cloudwatch:DescribeAlarms`. You can either have AWS OpsWorks Stacks update
    # the role for you when you first use this feature or you can edit the role
    # manually. For more information, see [Allowing AWS OpsWorks Stacks to Act on
    # Your Behalf](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
    # security-servicerole.html).
    alarms: typing.List[str] = dataclasses.field(default_factory=list, )


class AutoScalingType(Enum):
    load = "load"
    timer = "timer"


@dataclasses.dataclass
class BlockDeviceMapping(autoboto.ShapeBase):
    """
    Describes a block device mapping. This data type maps directly to the Amazon EC2
    [BlockDeviceMapping](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html)
    data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_name",
                "DeviceName",
                autoboto.TypeInfo(str),
            ),
            (
                "no_device",
                "NoDevice",
                autoboto.TypeInfo(str),
            ),
            (
                "virtual_name",
                "VirtualName",
                autoboto.TypeInfo(str),
            ),
            (
                "ebs",
                "Ebs",
                autoboto.TypeInfo(EbsBlockDevice),
            ),
        ]

    # The device name that is exposed to the instance, such as `/dev/sdh`. For
    # the root device, you can use the explicit device name or you can set this
    # parameter to `ROOT_DEVICE` and AWS OpsWorks Stacks will provide the correct
    # device name.
    device_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Suppresses the specified device included in the AMI's block device mapping.
    no_device: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The virtual device name. For more information, see
    # [BlockDeviceMapping](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html).
    virtual_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An `EBSBlockDevice` that defines how to configure an Amazon EBS volume when
    # the instance is launched.
    ebs: "EbsBlockDevice" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ChefConfiguration(autoboto.ShapeBase):
    """
    Describes the Chef configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "manage_berkshelf",
                "ManageBerkshelf",
                autoboto.TypeInfo(bool),
            ),
            (
                "berkshelf_version",
                "BerkshelfVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # Whether to enable Berkshelf.
    manage_berkshelf: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Berkshelf version.
    berkshelf_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CloneStackRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_stack_id",
                "SourceStackId",
                autoboto.TypeInfo(str),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "region",
                "Region",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[StackAttributesKeys, str]),
            ),
            (
                "default_instance_profile_arn",
                "DefaultInstanceProfileArn",
                autoboto.TypeInfo(str),
            ),
            (
                "default_os",
                "DefaultOs",
                autoboto.TypeInfo(str),
            ),
            (
                "hostname_theme",
                "HostnameTheme",
                autoboto.TypeInfo(str),
            ),
            (
                "default_availability_zone",
                "DefaultAvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "default_subnet_id",
                "DefaultSubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_json",
                "CustomJson",
                autoboto.TypeInfo(str),
            ),
            (
                "configuration_manager",
                "ConfigurationManager",
                autoboto.TypeInfo(StackConfigurationManager),
            ),
            (
                "chef_configuration",
                "ChefConfiguration",
                autoboto.TypeInfo(ChefConfiguration),
            ),
            (
                "use_custom_cookbooks",
                "UseCustomCookbooks",
                autoboto.TypeInfo(bool),
            ),
            (
                "use_opsworks_security_groups",
                "UseOpsworksSecurityGroups",
                autoboto.TypeInfo(bool),
            ),
            (
                "custom_cookbooks_source",
                "CustomCookbooksSource",
                autoboto.TypeInfo(Source),
            ),
            (
                "default_ssh_key_name",
                "DefaultSshKeyName",
                autoboto.TypeInfo(str),
            ),
            (
                "clone_permissions",
                "ClonePermissions",
                autoboto.TypeInfo(bool),
            ),
            (
                "clone_app_ids",
                "CloneAppIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "default_root_device_type",
                "DefaultRootDeviceType",
                autoboto.TypeInfo(RootDeviceType),
            ),
            (
                "agent_version",
                "AgentVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The source stack ID.
    source_stack_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stack AWS Identity and Access Management (IAM) role, which allows AWS
    # OpsWorks Stacks to work with AWS resources on your behalf. You must set
    # this parameter to the Amazon Resource Name (ARN) for an existing IAM role.
    # If you create a stack by using the AWS OpsWorks Stacks console, it creates
    # the role for you. You can obtain an existing stack's IAM ARN
    # programmatically by calling DescribePermissions. For more information about
    # IAM ARNs, see [Using
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html).

    # You must set this parameter to a valid service role ARN or the action will
    # fail; there is no default value. You can specify the source stack's service
    # role ARN, if you prefer, but you must do so explicitly.
    service_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The cloned stack name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The cloned stack AWS region, such as "ap-northeast-2". For more information
    # about AWS regions, see [Regions and
    # Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html).
    region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the VPC that the cloned stack is to be launched into. It must be
    # in the specified region. All instances are launched into this VPC, and you
    # cannot change the ID later.

    #   * If your account supports EC2 Classic, the default value is no VPC.

    #   * If your account does not support EC2 Classic, the default value is the default VPC for the specified region.

    # If the VPC ID corresponds to a default VPC and you have specified either
    # the `DefaultAvailabilityZone` or the `DefaultSubnetId` parameter only, AWS
    # OpsWorks Stacks infers the value of the other parameter. If you specify
    # neither parameter, AWS OpsWorks Stacks sets these parameters to the first
    # valid Availability Zone for the specified region and the corresponding
    # default VPC subnet ID, respectively.

    # If you specify a nondefault VPC ID, note the following:

    #   * It must belong to a VPC in your account that is in the specified region.

    #   * You must specify a value for `DefaultSubnetId`.

    # For more information about how to use AWS OpsWorks Stacks with a VPC, see
    # [Running a Stack in a
    # VPC](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
    # vpc.html). For more information about default VPC and EC2 Classic, see
    # [Supported
    # Platforms](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-
    # platforms.html).
    vpc_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of stack attributes and values as key/value pairs to be added to the
    # cloned stack.
    attributes: typing.Dict["StackAttributesKeys", str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of an IAM profile that is the default
    # profile for all of the stack's EC2 instances. For more information about
    # IAM ARNs, see [Using
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html).
    default_instance_profile_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stack's operating system, which must be set to one of the following.

    #   * A supported Linux operating system: An Amazon Linux version, such as `Amazon Linux 2017.09`, `Amazon Linux 2017.03`, `Amazon Linux 2016.09`, `Amazon Linux 2016.03`, `Amazon Linux 2015.09`, or `Amazon Linux 2015.03`.

    #   * A supported Ubuntu operating system, such as `Ubuntu 16.04 LTS`, `Ubuntu 14.04 LTS`, or `Ubuntu 12.04 LTS`.

    #   * `CentOS Linux 7`

    #   * `Red Hat Enterprise Linux 7`

    #   * `Microsoft Windows Server 2012 R2 Base`, `Microsoft Windows Server 2012 R2 with SQL Server Express`, `Microsoft Windows Server 2012 R2 with SQL Server Standard`, or `Microsoft Windows Server 2012 R2 with SQL Server Web`.

    #   * A custom AMI: `Custom`. You specify the custom AMI you want to use when you create instances. For more information about how to use custom AMIs with OpsWorks, see [Using Custom AMIs](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html).

    # The default option is the parent stack's operating system. For more
    # information about supported operating systems, see [AWS OpsWorks Stacks
    # Operating
    # Systems](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # os.html).

    # You can specify a different Linux operating system for the cloned stack,
    # but you cannot change from Linux to Windows or Windows to Linux.
    default_os: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack's host name theme, with spaces are replaced by underscores. The
    # theme is used to generate host names for the stack's instances. By default,
    # `HostnameTheme` is set to `Layer_Dependent`, which creates host names by
    # appending integers to the layer's short name. The other themes are:

    #   * `Baked_Goods`

    #   * `Clouds`

    #   * `Europe_Cities`

    #   * `Fruits`

    #   * `Greek_Deities`

    #   * `Legendary_creatures_from_Japan`

    #   * `Planets_and_Moons`

    #   * `Roman_Deities`

    #   * `Scottish_Islands`

    #   * `US_Cities`

    #   * `Wild_Cats`

    # To obtain a generated host name, call `GetHostNameSuggestion`, which
    # returns a host name based on the current theme.
    hostname_theme: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The cloned stack's default Availability Zone, which must be in the
    # specified region. For more information, see [Regions and
    # Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html). If you
    # also specify a value for `DefaultSubnetId`, the subnet must be in the same
    # zone. For more information, see the `VpcId` parameter description.
    default_availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stack's default VPC subnet ID. This parameter is required if you
    # specify a value for the `VpcId` parameter. All instances are launched into
    # this subnet unless you specify otherwise when you create the instance. If
    # you also specify a value for `DefaultAvailabilityZone`, the subnet must be
    # in that zone. For information on default values and when this parameter is
    # required, see the `VpcId` parameter description.
    default_subnet_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string that contains user-defined, custom JSON. It is used to override
    # the corresponding default stack configuration JSON values. The string
    # should be in the following format:

    # `"{\"key1\": \"value1\", \"key2\": \"value2\",...}"`

    # For more information about custom JSON, see [Use Custom JSON to Modify the
    # Stack Configuration
    # Attributes](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
    # json.html)
    custom_json: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The configuration manager. When you clone a stack we recommend that you use
    # the configuration manager to specify the Chef version: 12, 11.10, or 11.4
    # for Linux stacks, or 12.2 for Windows stacks. The default value for Linux
    # stacks is currently 12.
    configuration_manager: "StackConfigurationManager" = dataclasses.field(
        default_factory=dict,
    )

    # A `ChefConfiguration` object that specifies whether to enable Berkshelf and
    # the Berkshelf version on Chef 11.10 stacks. For more information, see
    # [Create a New
    # Stack](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
    # creating.html).
    chef_configuration: "ChefConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # Whether to use custom cookbooks.
    use_custom_cookbooks: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether to associate the AWS OpsWorks Stacks built-in security groups with
    # the stack's layers.

    # AWS OpsWorks Stacks provides a standard set of built-in security groups,
    # one for each layer, which are associated with layers by default. With
    # `UseOpsworksSecurityGroups` you can instead provide your own custom
    # security groups. `UseOpsworksSecurityGroups` has the following settings:

    #   * True - AWS OpsWorks Stacks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it but you cannot delete the built-in security group.

    #   * False - AWS OpsWorks Stacks does not associate built-in security groups with layers. You must create appropriate Amazon Elastic Compute Cloud (Amazon EC2) security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on creation; custom security groups are required only for those layers that need custom settings.

    # For more information, see [Create a New
    # Stack](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
    # creating.html).
    use_opsworks_security_groups: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains the information required to retrieve an app or cookbook from a
    # repository. For more information, see [Creating
    # Apps](http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-
    # creating.html) or [Custom Recipes and
    # Cookbooks](http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html).
    custom_cookbooks_source: "Source" = dataclasses.field(
        default_factory=dict,
    )

    # A default Amazon EC2 key pair name. The default value is none. If you
    # specify a key pair name, AWS OpsWorks installs the public key on the
    # instance and you can use the private key with an SSH client to log in to
    # the instance. For more information, see [ Using SSH to Communicate with an
    # Instance](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # ssh.html) and [ Managing SSH
    # Access](http://docs.aws.amazon.com/opsworks/latest/userguide/security-ssh-
    # access.html). You can override this setting by specifying a different key
    # pair, or no key pair, when you [ create an
    # instance](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # add.html).
    default_ssh_key_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether to clone the source stack's permissions.
    clone_permissions: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of source stack app IDs to be included in the cloned stack.
    clone_app_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The default root device type. This value is used by default for all
    # instances in the cloned stack, but you can override it when you create an
    # instance. For more information, see [Storage for the Root
    # Device](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-
    # for-the-root-device).
    default_root_device_type: "RootDeviceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The default AWS OpsWorks Stacks agent version. You have the following
    # options:

    #   * Auto-update - Set this parameter to `LATEST`. AWS OpsWorks Stacks automatically installs new agent versions on the stack's instances as soon as they are available.

    #   * Fixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the stack's instances.

    # The default setting is `LATEST`. To specify an agent version, you must use
    # the complete version number, not the abbreviated number shown on the
    # console. For a list of available agent version numbers, call
    # DescribeAgentVersions. AgentVersion cannot be set to Chef 12.2.

    # You can also specify an agent version when you create or update an
    # instance, which overrides the stack's default setting.
    agent_version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CloneStackResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `CloneStack` request.
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
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The cloned stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CloudWatchLogsConfiguration(autoboto.ShapeBase):
    """
    Describes the Amazon CloudWatch logs configuration for a layer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "log_streams",
                "LogStreams",
                autoboto.TypeInfo(typing.List[CloudWatchLogsLogStream]),
            ),
        ]

    # Whether CloudWatch Logs is enabled for a layer.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of configuration options for CloudWatch Logs.
    log_streams: typing.List["CloudWatchLogsLogStream"] = dataclasses.field(
        default_factory=list,
    )


class CloudWatchLogsEncoding(Enum):
    """
    Specifies the encoding of the log file so that the file can be read correctly.
    The default is `utf_8`. Encodings supported by Python `codecs.decode()` can be
    used here.
    """
    ascii = "ascii"
    big5 = "big5"
    big5hkscs = "big5hkscs"
    cp037 = "cp037"
    cp424 = "cp424"
    cp437 = "cp437"
    cp500 = "cp500"
    cp720 = "cp720"
    cp737 = "cp737"
    cp775 = "cp775"
    cp850 = "cp850"
    cp852 = "cp852"
    cp855 = "cp855"
    cp856 = "cp856"
    cp857 = "cp857"
    cp858 = "cp858"
    cp860 = "cp860"
    cp861 = "cp861"
    cp862 = "cp862"
    cp863 = "cp863"
    cp864 = "cp864"
    cp865 = "cp865"
    cp866 = "cp866"
    cp869 = "cp869"
    cp874 = "cp874"
    cp875 = "cp875"
    cp932 = "cp932"
    cp949 = "cp949"
    cp950 = "cp950"
    cp1006 = "cp1006"
    cp1026 = "cp1026"
    cp1140 = "cp1140"
    cp1250 = "cp1250"
    cp1251 = "cp1251"
    cp1252 = "cp1252"
    cp1253 = "cp1253"
    cp1254 = "cp1254"
    cp1255 = "cp1255"
    cp1256 = "cp1256"
    cp1257 = "cp1257"
    cp1258 = "cp1258"
    euc_jp = "euc_jp"
    euc_jis_2004 = "euc_jis_2004"
    euc_jisx0213 = "euc_jisx0213"
    euc_kr = "euc_kr"
    gb2312 = "gb2312"
    gbk = "gbk"
    gb18030 = "gb18030"
    hz = "hz"
    iso2022_jp = "iso2022_jp"
    iso2022_jp_1 = "iso2022_jp_1"
    iso2022_jp_2 = "iso2022_jp_2"
    iso2022_jp_2004 = "iso2022_jp_2004"
    iso2022_jp_3 = "iso2022_jp_3"
    iso2022_jp_ext = "iso2022_jp_ext"
    iso2022_kr = "iso2022_kr"
    latin_1 = "latin_1"
    iso8859_2 = "iso8859_2"
    iso8859_3 = "iso8859_3"
    iso8859_4 = "iso8859_4"
    iso8859_5 = "iso8859_5"
    iso8859_6 = "iso8859_6"
    iso8859_7 = "iso8859_7"
    iso8859_8 = "iso8859_8"
    iso8859_9 = "iso8859_9"
    iso8859_10 = "iso8859_10"
    iso8859_13 = "iso8859_13"
    iso8859_14 = "iso8859_14"
    iso8859_15 = "iso8859_15"
    iso8859_16 = "iso8859_16"
    johab = "johab"
    koi8_r = "koi8_r"
    koi8_u = "koi8_u"
    mac_cyrillic = "mac_cyrillic"
    mac_greek = "mac_greek"
    mac_iceland = "mac_iceland"
    mac_latin2 = "mac_latin2"
    mac_roman = "mac_roman"
    mac_turkish = "mac_turkish"
    ptcp154 = "ptcp154"
    shift_jis = "shift_jis"
    shift_jis_2004 = "shift_jis_2004"
    shift_jisx0213 = "shift_jisx0213"
    utf_32 = "utf_32"
    utf_32_be = "utf_32_be"
    utf_32_le = "utf_32_le"
    utf_16 = "utf_16"
    utf_16_be = "utf_16_be"
    utf_16_le = "utf_16_le"
    utf_7 = "utf_7"
    utf_8 = "utf_8"
    utf_8_sig = "utf_8_sig"


class CloudWatchLogsInitialPosition(Enum):
    """
    Specifies where to start to read data (start_of_file or end_of_file). The
    default is start_of_file. It's only used if there is no state persisted for that
    log stream.
    """
    start_of_file = "start_of_file"
    end_of_file = "end_of_file"


@dataclasses.dataclass
class CloudWatchLogsLogStream(autoboto.ShapeBase):
    """
    Describes the Amazon CloudWatch logs configuration for a layer. For detailed
    information about members of this data type, see the [CloudWatch Logs Agent
    Reference](http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "LogGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "datetime_format",
                "DatetimeFormat",
                autoboto.TypeInfo(str),
            ),
            (
                "time_zone",
                "TimeZone",
                autoboto.TypeInfo(CloudWatchLogsTimeZone),
            ),
            (
                "file",
                "File",
                autoboto.TypeInfo(str),
            ),
            (
                "file_fingerprint_lines",
                "FileFingerprintLines",
                autoboto.TypeInfo(str),
            ),
            (
                "multi_line_start_pattern",
                "MultiLineStartPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "initial_position",
                "InitialPosition",
                autoboto.TypeInfo(CloudWatchLogsInitialPosition),
            ),
            (
                "encoding",
                "Encoding",
                autoboto.TypeInfo(CloudWatchLogsEncoding),
            ),
            (
                "buffer_duration",
                "BufferDuration",
                autoboto.TypeInfo(int),
            ),
            (
                "batch_count",
                "BatchCount",
                autoboto.TypeInfo(int),
            ),
            (
                "batch_size",
                "BatchSize",
                autoboto.TypeInfo(int),
            ),
        ]

    # Specifies the destination log group. A log group is created automatically
    # if it doesn't already exist. Log group names can be between 1 and 512
    # characters long. Allowed characters include a-z, A-Z, 0-9, '_'
    # (underscore), '-' (hyphen), '/' (forward slash), and '.' (period).
    log_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies how the time stamp is extracted from logs. For more information,
    # see the [CloudWatch Logs Agent
    # Reference](http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html).
    datetime_format: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the time zone of log event time stamps.
    time_zone: "CloudWatchLogsTimeZone" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies log files that you want to push to CloudWatch Logs.

    # `File` can point to a specific file or multiple files (by using wild card
    # characters such as `/var/log/system.log*`). Only the latest file is pushed
    # to CloudWatch Logs, based on file modification time. We recommend that you
    # use wild card characters to specify a series of files of the same type,
    # such as `access_log.2014-06-01-01`, `access_log.2014-06-01-02`, and so on
    # by using a pattern like `access_log.*`. Don't use a wildcard to match
    # multiple file types, such as `access_log_80` and `access_log_443`. To
    # specify multiple, different file types, add another log stream entry to the
    # configuration file, so that each log file type is stored in a different log
    # group.

    # Zipped files are not supported.
    file: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the range of lines for identifying a file. The valid values are
    # one number, or two dash-delimited numbers, such as '1', '2-5'. The default
    # value is '1', meaning the first line is used to calculate the fingerprint.
    # Fingerprint lines are not sent to CloudWatch Logs unless all specified
    # lines are available.
    file_fingerprint_lines: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the pattern for identifying the start of a log message.
    multi_line_start_pattern: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies where to start to read data (start_of_file or end_of_file). The
    # default is start_of_file. This setting is only used if there is no state
    # persisted for that log stream.
    initial_position: "CloudWatchLogsInitialPosition" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the encoding of the log file so that the file can be read
    # correctly. The default is `utf_8`. Encodings supported by Python
    # `codecs.decode()` can be used here.
    encoding: "CloudWatchLogsEncoding" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the time duration for the batching of log events. The minimum
    # value is 5000ms and default value is 5000ms.
    buffer_duration: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the max number of log events in a batch, up to 10000. The default
    # value is 1000.
    batch_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the maximum size of log events in a batch, in bytes, up to
    # 1048576 bytes. The default value is 32768 bytes. This size is calculated as
    # the sum of all event messages in UTF-8, plus 26 bytes for each log event.
    batch_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class CloudWatchLogsTimeZone(Enum):
    """
    The preferred time zone for logs streamed to CloudWatch Logs. Valid values are
    `LOCAL` and `UTC`, for Coordinated Universal Time.
    """
    LOCAL = "LOCAL"
    UTC = "UTC"


@dataclasses.dataclass
class Command(autoboto.ShapeBase):
    """
    Describes a command.
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
                "deployment_id",
                "DeploymentId",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "acknowledged_at",
                "AcknowledgedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "completed_at",
                "CompletedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
            (
                "exit_code",
                "ExitCode",
                autoboto.TypeInfo(int),
            ),
            (
                "log_url",
                "LogUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
        ]

    # The command ID.
    command_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the instance where the command was executed.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The command deployment ID.
    deployment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Date and time when the command was run.
    created_at: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Date and time when the command was acknowledged.
    acknowledged_at: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Date when the command completed.
    completed_at: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The command status:

    #   * failed

    #   * successful

    #   * skipped

    #   * pending
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The command exit code.
    exit_code: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The URL of the command log.
    log_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The command type:

    #   * `configure`

    #   * `deploy`

    #   * `execute_recipes`

    #   * `install_dependencies`

    #   * `restart`

    #   * `rollback`

    #   * `setup`

    #   * `start`

    #   * `stop`

    #   * `undeploy`

    #   * `update_custom_cookbooks`

    #   * `update_dependencies`
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAppRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(AppType),
            ),
            (
                "shortname",
                "Shortname",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "data_sources",
                "DataSources",
                autoboto.TypeInfo(typing.List[DataSource]),
            ),
            (
                "app_source",
                "AppSource",
                autoboto.TypeInfo(Source),
            ),
            (
                "domains",
                "Domains",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "enable_ssl",
                "EnableSsl",
                autoboto.TypeInfo(bool),
            ),
            (
                "ssl_configuration",
                "SslConfiguration",
                autoboto.TypeInfo(SslConfiguration),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[AppAttributesKeys, str]),
            ),
            (
                "environment",
                "Environment",
                autoboto.TypeInfo(typing.List[EnvironmentVariable]),
            ),
        ]

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The app name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The app type. Each supported type is associated with a particular layer.
    # For example, PHP applications are associated with a PHP layer. AWS OpsWorks
    # Stacks deploys an application to those instances that are members of the
    # corresponding layer. If your app isn't one of the standard types, or you
    # prefer to implement your own Deploy recipes, specify `other`.
    type: "AppType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The app's short name.
    shortname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A description of the app.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The app's data source.
    data_sources: typing.List["DataSource"] = dataclasses.field(
        default_factory=list,
    )

    # A `Source` object that specifies the app repository.
    app_source: "Source" = dataclasses.field(default_factory=dict, )

    # The app virtual host settings, with multiple domains separated by commas.
    # For example: `'www.example.com, example.com'`
    domains: typing.List[str] = dataclasses.field(default_factory=list, )

    # Whether to enable SSL for the app.
    enable_ssl: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An `SslConfiguration` object with the SSL configuration.
    ssl_configuration: "SslConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # One or more user-defined key/value pairs to be added to the stack
    # attributes.
    attributes: typing.Dict["AppAttributesKeys", str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of `EnvironmentVariable` objects that specify environment
    # variables to be associated with the app. After you deploy the app, these
    # variables are defined on the associated app server instance. For more
    # information, see [ Environment
    # Variables](http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-
    # creating.html#workingapps-creating-environment).

    # There is no specific limit on the number of environment variables. However,
    # the size of the associated data structure - which includes the variables'
    # names, values, and protected flag values - cannot exceed 10 KB (10240
    # Bytes). This limit should accommodate most if not all use cases. Exceeding
    # it will cause an exception with the message, "Environment: is too large
    # (maximum is 10KB)."

    # This parameter is supported only by Chef 11.10 stacks. If you have
    # specified one or more environment variables, you cannot modify the stack's
    # Chef version.
    environment: typing.List["EnvironmentVariable"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateAppResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `CreateApp` request.
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
                "app_id",
                "AppId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The app ID.
    app_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDeploymentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "command",
                "Command",
                autoboto.TypeInfo(DeploymentCommand),
            ),
            (
                "app_id",
                "AppId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_ids",
                "InstanceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "layer_ids",
                "LayerIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "comment",
                "Comment",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_json",
                "CustomJson",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A `DeploymentCommand` object that specifies the deployment command and any
    # associated arguments.
    command: "DeploymentCommand" = dataclasses.field(default_factory=dict, )

    # The app ID. This parameter is required for app deployments, but not for
    # other deployment commands.
    app_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance IDs for the deployment targets.
    instance_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The layer IDs for the deployment targets.
    layer_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # A user-defined comment.
    comment: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A string that contains user-defined, custom JSON. It is used to override
    # the corresponding default stack configuration JSON values. The string
    # should be in the following format:

    # `"{\"key1\": \"value1\", \"key2\": \"value2\",...}"`

    # For more information about custom JSON, see [Use Custom JSON to Modify the
    # Stack Configuration
    # Attributes](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
    # json.html).
    custom_json: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDeploymentResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `CreateDeployment` request.
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
                "deployment_id",
                "DeploymentId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The deployment ID, which can be used with other requests to identify the
    # deployment.
    deployment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_ids",
                "LayerIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "instance_type",
                "InstanceType",
                autoboto.TypeInfo(str),
            ),
            (
                "auto_scaling_type",
                "AutoScalingType",
                autoboto.TypeInfo(AutoScalingType),
            ),
            (
                "hostname",
                "Hostname",
                autoboto.TypeInfo(str),
            ),
            (
                "os",
                "Os",
                autoboto.TypeInfo(str),
            ),
            (
                "ami_id",
                "AmiId",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_key_name",
                "SshKeyName",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "virtualization_type",
                "VirtualizationType",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_id",
                "SubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "architecture",
                "Architecture",
                autoboto.TypeInfo(Architecture),
            ),
            (
                "root_device_type",
                "RootDeviceType",
                autoboto.TypeInfo(RootDeviceType),
            ),
            (
                "block_device_mappings",
                "BlockDeviceMappings",
                autoboto.TypeInfo(typing.List[BlockDeviceMapping]),
            ),
            (
                "install_updates_on_boot",
                "InstallUpdatesOnBoot",
                autoboto.TypeInfo(bool),
            ),
            (
                "ebs_optimized",
                "EbsOptimized",
                autoboto.TypeInfo(bool),
            ),
            (
                "agent_version",
                "AgentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "tenancy",
                "Tenancy",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array that contains the instance's layer IDs.
    layer_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The instance type, such as `t2.micro`. For a list of supported instance
    # types, open the stack in the console, choose **Instances** , and choose
    # **\+ Instance**. The **Size** list contains the currently supported types.
    # For more information, see [Instance Families and
    # Types](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-
    # types.html). The parameter values that you use to specify the various types
    # are in the **API Name** column of the **Available Instance Types** table.
    instance_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # For load-based or time-based instances, the type. Windows stacks can use
    # only time-based instances.
    auto_scaling_type: "AutoScalingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance host name.
    hostname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's operating system, which must be set to one of the following.

    #   * A supported Linux operating system: An Amazon Linux version, such as `Amazon Linux 2017.09`, `Amazon Linux 2017.03`, `Amazon Linux 2016.09`, `Amazon Linux 2016.03`, `Amazon Linux 2015.09`, or `Amazon Linux 2015.03`.

    #   * A supported Ubuntu operating system, such as `Ubuntu 16.04 LTS`, `Ubuntu 14.04 LTS`, or `Ubuntu 12.04 LTS`.

    #   * `CentOS Linux 7`

    #   * `Red Hat Enterprise Linux 7`

    #   * A supported Windows operating system, such as `Microsoft Windows Server 2012 R2 Base`, `Microsoft Windows Server 2012 R2 with SQL Server Express`, `Microsoft Windows Server 2012 R2 with SQL Server Standard`, or `Microsoft Windows Server 2012 R2 with SQL Server Web`.

    #   * A custom AMI: `Custom`.

    # For more information about the supported operating systems, see [AWS
    # OpsWorks Stacks Operating
    # Systems](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # os.html).

    # The default option is the current Amazon Linux version. If you set this
    # parameter to `Custom`, you must use the CreateInstance action's AmiId
    # parameter to specify the custom AMI that you want to use. Block device
    # mappings are not supported if the value is `Custom`. For more information
    # about supported operating systems, see [Operating
    # Systems](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # os.html)For more information about how to use custom AMIs with AWS OpsWorks
    # Stacks, see [Using Custom
    # AMIs](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # custom-ami.html).
    os: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A custom AMI ID to be used to create the instance. The AMI should be based
    # on one of the supported operating systems. For more information, see [Using
    # Custom
    # AMIs](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # custom-ami.html).

    # If you specify a custom AMI, you must set `Os` to `Custom`.
    ami_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's Amazon EC2 key-pair name.
    ssh_key_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance Availability Zone. For more information, see [Regions and
    # Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html).
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance's virtualization type, `paravirtual` or `hvm`.
    virtualization_type: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the instance's subnet. If the stack is running in a VPC, you can
    # use this parameter to override the stack's default subnet ID value and
    # direct AWS OpsWorks Stacks to launch the instance in a different subnet.
    subnet_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance architecture. The default option is `x86_64`. Instance types
    # do not necessarily support both architectures. For a list of the
    # architectures that are supported by the different instance types, see
    # [Instance Families and
    # Types](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-
    # types.html).
    architecture: "Architecture" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance root device type. For more information, see [Storage for the
    # Root
    # Device](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-
    # for-the-root-device).
    root_device_type: "RootDeviceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of `BlockDeviceMapping` objects that specify the instance's block
    # devices. For more information, see [Block Device
    # Mapping](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-
    # mapping-concepts.html). Note that block device mappings are not supported
    # for custom AMIs.
    block_device_mappings: typing.List["BlockDeviceMapping"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )

    # Whether to install operating system and package updates when the instance
    # boots. The default value is `true`. To control when updates are installed,
    # set this value to `false`. You must then update your instances manually by
    # using CreateDeployment to run the `update_dependencies` stack command or by
    # manually running `yum` (Amazon Linux) or `apt-get` (Ubuntu) on the
    # instances.

    # We strongly recommend using the default value of `true` to ensure that your
    # instances have the latest security updates.
    install_updates_on_boot: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether to create an Amazon EBS-optimized instance.
    ebs_optimized: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The default AWS OpsWorks Stacks agent version. You have the following
    # options:

    #   * `INHERIT` \- Use the stack's default agent version setting.

    #   * _version_number_ \- Use the specified agent version. This value overrides the stack's default setting. To update the agent version, edit the instance configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the instance.

    # The default setting is `INHERIT`. To specify an agent version, you must use
    # the complete version number, not the abbreviated number shown on the
    # console. For a list of available agent version numbers, call
    # DescribeAgentVersions. AgentVersion cannot be set to Chef 12.2.
    agent_version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's tenancy option. The default option is no tenancy, or if the
    # instance is running in a VPC, inherit tenancy settings from the VPC. The
    # following are valid values for this parameter: `dedicated`, `default`, or
    # `host`. Because there are costs associated with changes in tenancy options,
    # we recommend that you research tenancy options before choosing them for
    # your instances. For more information about dedicated hosts, see [Dedicated
    # Hosts Overview](http://aws.amazon.com/ec2/dedicated-hosts/) and [Amazon EC2
    # Dedicated Hosts](http://aws.amazon.com/ec2/dedicated-hosts/). For more
    # information about dedicated instances, see [Dedicated
    # Instances](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/dedicated-
    # instance.html) and [Amazon EC2 Dedicated
    # Instances](http://aws.amazon.com/ec2/purchasing-options/dedicated-
    # instances/).
    tenancy: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInstanceResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `CreateInstance` request.
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
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateLayerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(LayerType),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "shortname",
                "Shortname",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[LayerAttributesKeys, str]),
            ),
            (
                "cloud_watch_logs_configuration",
                "CloudWatchLogsConfiguration",
                autoboto.TypeInfo(CloudWatchLogsConfiguration),
            ),
            (
                "custom_instance_profile_arn",
                "CustomInstanceProfileArn",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_json",
                "CustomJson",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_security_group_ids",
                "CustomSecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "packages",
                "Packages",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "volume_configurations",
                "VolumeConfigurations",
                autoboto.TypeInfo(typing.List[VolumeConfiguration]),
            ),
            (
                "enable_auto_healing",
                "EnableAutoHealing",
                autoboto.TypeInfo(bool),
            ),
            (
                "auto_assign_elastic_ips",
                "AutoAssignElasticIps",
                autoboto.TypeInfo(bool),
            ),
            (
                "auto_assign_public_ips",
                "AutoAssignPublicIps",
                autoboto.TypeInfo(bool),
            ),
            (
                "custom_recipes",
                "CustomRecipes",
                autoboto.TypeInfo(Recipes),
            ),
            (
                "install_updates_on_boot",
                "InstallUpdatesOnBoot",
                autoboto.TypeInfo(bool),
            ),
            (
                "use_ebs_optimized_instances",
                "UseEbsOptimizedInstances",
                autoboto.TypeInfo(bool),
            ),
            (
                "lifecycle_event_configuration",
                "LifecycleEventConfiguration",
                autoboto.TypeInfo(LifecycleEventConfiguration),
            ),
        ]

    # The layer stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The layer type. A stack cannot have more than one built-in layer of the
    # same type. It can have any number of custom layers. Built-in layers are not
    # available in Chef 12 stacks.
    type: "LayerType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The layer name, which is used by the console.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # For custom layers only, use this parameter to specify the layer's short
    # name, which is used internally by AWS OpsWorks Stacks and by Chef recipes.
    # The short name is also used as the name for the directory where your app
    # files are installed. It can have a maximum of 200 characters, which are
    # limited to the alphanumeric characters, '-', '_', and '.'.

    # The built-in layers' short names are defined by AWS OpsWorks Stacks. For
    # more information, see the [Layer
    # Reference](http://docs.aws.amazon.com/opsworks/latest/userguide/layers.html).
    shortname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more user-defined key-value pairs to be added to the stack
    # attributes.

    # To create a cluster layer, set the `EcsClusterArn` attribute to the
    # cluster's ARN.
    attributes: typing.Dict["LayerAttributesKeys", str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies CloudWatch Logs configuration options for the layer. For more
    # information, see CloudWatchLogsLogStream.
    cloud_watch_logs_configuration: "CloudWatchLogsConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The ARN of an IAM profile to be used for the layer's EC2 instances. For
    # more information about IAM ARNs, see [Using
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html).
    custom_instance_profile_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A JSON-formatted string containing custom stack configuration and
    # deployment attributes to be installed on the layer's instances. For more
    # information, see [ Using Custom
    # JSON](http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-
    # json-override.html). This feature is supported as of version 1.7.42 of the
    # AWS CLI.
    custom_json: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array containing the layer custom security group IDs.
    custom_security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # An array of `Package` objects that describes the layer packages.
    packages: typing.List[str] = dataclasses.field(default_factory=list, )

    # A `VolumeConfigurations` object that describes the layer's Amazon EBS
    # volumes.
    volume_configurations: typing.List["VolumeConfiguration"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )

    # Whether to disable auto healing for the layer.
    enable_auto_healing: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether to automatically assign an [Elastic IP
    # address](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-
    # addresses-eip.html) to the layer's instances. For more information, see
    # [How to Edit a
    # Layer](http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-
    # basics-edit.html).
    auto_assign_elastic_ips: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # For stacks that are running in a VPC, whether to automatically assign a
    # public IP address to the layer's instances. For more information, see [How
    # to Edit a
    # Layer](http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-
    # basics-edit.html).
    auto_assign_public_ips: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A `LayerCustomRecipes` object that specifies the layer custom recipes.
    custom_recipes: "Recipes" = dataclasses.field(default_factory=dict, )

    # Whether to install operating system and package updates when the instance
    # boots. The default value is `true`. To control when updates are installed,
    # set this value to `false`. You must then update your instances manually by
    # using CreateDeployment to run the `update_dependencies` stack command or by
    # manually running `yum` (Amazon Linux) or `apt-get` (Ubuntu) on the
    # instances.

    # To ensure that your instances have the latest security updates, we strongly
    # recommend using the default value of `true`.
    install_updates_on_boot: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether to use Amazon EBS-optimized instances.
    use_ebs_optimized_instances: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A `LifeCycleEventConfiguration` object that you can use to configure the
    # Shutdown event to specify an execution timeout and enable or disable
    # Elastic Load Balancer connection draining.
    lifecycle_event_configuration: "LifecycleEventConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateLayerResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `CreateLayer` request.
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
                "layer_id",
                "LayerId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The layer ID.
    layer_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStackRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "region",
                "Region",
                autoboto.TypeInfo(str),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "default_instance_profile_arn",
                "DefaultInstanceProfileArn",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[StackAttributesKeys, str]),
            ),
            (
                "default_os",
                "DefaultOs",
                autoboto.TypeInfo(str),
            ),
            (
                "hostname_theme",
                "HostnameTheme",
                autoboto.TypeInfo(str),
            ),
            (
                "default_availability_zone",
                "DefaultAvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "default_subnet_id",
                "DefaultSubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_json",
                "CustomJson",
                autoboto.TypeInfo(str),
            ),
            (
                "configuration_manager",
                "ConfigurationManager",
                autoboto.TypeInfo(StackConfigurationManager),
            ),
            (
                "chef_configuration",
                "ChefConfiguration",
                autoboto.TypeInfo(ChefConfiguration),
            ),
            (
                "use_custom_cookbooks",
                "UseCustomCookbooks",
                autoboto.TypeInfo(bool),
            ),
            (
                "use_opsworks_security_groups",
                "UseOpsworksSecurityGroups",
                autoboto.TypeInfo(bool),
            ),
            (
                "custom_cookbooks_source",
                "CustomCookbooksSource",
                autoboto.TypeInfo(Source),
            ),
            (
                "default_ssh_key_name",
                "DefaultSshKeyName",
                autoboto.TypeInfo(str),
            ),
            (
                "default_root_device_type",
                "DefaultRootDeviceType",
                autoboto.TypeInfo(RootDeviceType),
            ),
            (
                "agent_version",
                "AgentVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stack name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack's AWS region, such as `ap-south-1`. For more information about
    # Amazon regions, see [Regions and
    # Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html).

    # In the AWS CLI, this API maps to the `--stack-region` parameter. If the
    # `--stack-region` parameter and the AWS CLI common parameter `--region` are
    # set to the same value, the stack uses a _regional_ endpoint. If the
    # `--stack-region` parameter is not set, but the AWS CLI `--region` parameter
    # is, this also results in a stack with a _regional_ endpoint. However, if
    # the `--region` parameter is set to `us-east-1`, and the `--stack-region`
    # parameter is set to one of the following, then the stack uses a legacy or
    # _classic_ region: `us-west-1, us-west-2, sa-east-1, eu-central-1, eu-
    # west-1, ap-northeast-1, ap-southeast-1, ap-southeast-2`. In this case, the
    # actual API endpoint of the stack is in `us-east-1`. Only the preceding
    # regions are supported as classic regions in the `us-east-1` API endpoint.
    # Because it is a best practice to choose the regional endpoint that is
    # closest to where you manage AWS, we recommend that you use regional
    # endpoints for new stacks. The AWS CLI common `--region` parameter always
    # specifies a regional API endpoint; it cannot be used to specify a classic
    # AWS OpsWorks Stacks region.
    region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack's AWS Identity and Access Management (IAM) role, which allows AWS
    # OpsWorks Stacks to work with AWS resources on your behalf. You must set
    # this parameter to the Amazon Resource Name (ARN) for an existing IAM role.
    # For more information about IAM ARNs, see [Using
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html).
    service_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of an IAM profile that is the default
    # profile for all of the stack's EC2 instances. For more information about
    # IAM ARNs, see [Using
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html).
    default_instance_profile_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the VPC that the stack is to be launched into. The VPC must be in
    # the stack's region. All instances are launched into this VPC. You cannot
    # change the ID later.

    #   * If your account supports EC2-Classic, the default value is `no VPC`.

    #   * If your account does not support EC2-Classic, the default value is the default VPC for the specified region.

    # If the VPC ID corresponds to a default VPC and you have specified either
    # the `DefaultAvailabilityZone` or the `DefaultSubnetId` parameter only, AWS
    # OpsWorks Stacks infers the value of the other parameter. If you specify
    # neither parameter, AWS OpsWorks Stacks sets these parameters to the first
    # valid Availability Zone for the specified region and the corresponding
    # default VPC subnet ID, respectively.

    # If you specify a nondefault VPC ID, note the following:

    #   * It must belong to a VPC in your account that is in the specified region.

    #   * You must specify a value for `DefaultSubnetId`.

    # For more information about how to use AWS OpsWorks Stacks with a VPC, see
    # [Running a Stack in a
    # VPC](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
    # vpc.html). For more information about default VPC and EC2-Classic, see
    # [Supported
    # Platforms](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-
    # platforms.html).
    vpc_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more user-defined key-value pairs to be added to the stack
    # attributes.
    attributes: typing.Dict["StackAttributesKeys", str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stack's default operating system, which is installed on every instance
    # unless you specify a different operating system when you create the
    # instance. You can specify one of the following.

    #   * A supported Linux operating system: An Amazon Linux version, such as `Amazon Linux 2017.09`, `Amazon Linux 2017.03`, `Amazon Linux 2016.09`, `Amazon Linux 2016.03`, `Amazon Linux 2015.09`, or `Amazon Linux 2015.03`.

    #   * A supported Ubuntu operating system, such as `Ubuntu 16.04 LTS`, `Ubuntu 14.04 LTS`, or `Ubuntu 12.04 LTS`.

    #   * `CentOS Linux 7`

    #   * `Red Hat Enterprise Linux 7`

    #   * A supported Windows operating system, such as `Microsoft Windows Server 2012 R2 Base`, `Microsoft Windows Server 2012 R2 with SQL Server Express`, `Microsoft Windows Server 2012 R2 with SQL Server Standard`, or `Microsoft Windows Server 2012 R2 with SQL Server Web`.

    #   * A custom AMI: `Custom`. You specify the custom AMI you want to use when you create instances. For more information, see [ Using Custom AMIs](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html).

    # The default option is the current Amazon Linux version. For more
    # information about supported operating systems, see [AWS OpsWorks Stacks
    # Operating
    # Systems](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # os.html).
    default_os: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack's host name theme, with spaces replaced by underscores. The theme
    # is used to generate host names for the stack's instances. By default,
    # `HostnameTheme` is set to `Layer_Dependent`, which creates host names by
    # appending integers to the layer's short name. The other themes are:

    #   * `Baked_Goods`

    #   * `Clouds`

    #   * `Europe_Cities`

    #   * `Fruits`

    #   * `Greek_Deities`

    #   * `Legendary_creatures_from_Japan`

    #   * `Planets_and_Moons`

    #   * `Roman_Deities`

    #   * `Scottish_Islands`

    #   * `US_Cities`

    #   * `Wild_Cats`

    # To obtain a generated host name, call `GetHostNameSuggestion`, which
    # returns a host name based on the current theme.
    hostname_theme: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stack's default Availability Zone, which must be in the specified
    # region. For more information, see [Regions and
    # Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html). If you
    # also specify a value for `DefaultSubnetId`, the subnet must be in the same
    # zone. For more information, see the `VpcId` parameter description.
    default_availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stack's default VPC subnet ID. This parameter is required if you
    # specify a value for the `VpcId` parameter. All instances are launched into
    # this subnet unless you specify otherwise when you create the instance. If
    # you also specify a value for `DefaultAvailabilityZone`, the subnet must be
    # in that zone. For information on default values and when this parameter is
    # required, see the `VpcId` parameter description.
    default_subnet_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string that contains user-defined, custom JSON. It can be used to
    # override the corresponding default stack configuration attribute values or
    # to pass data to recipes. The string should be in the following format:

    # `"{\"key1\": \"value1\", \"key2\": \"value2\",...}"`

    # For more information about custom JSON, see [Use Custom JSON to Modify the
    # Stack Configuration
    # Attributes](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
    # json.html).
    custom_json: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The configuration manager. When you create a stack we recommend that you
    # use the configuration manager to specify the Chef version: 12, 11.10, or
    # 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for
    # Linux stacks is currently 12.
    configuration_manager: "StackConfigurationManager" = dataclasses.field(
        default_factory=dict,
    )

    # A `ChefConfiguration` object that specifies whether to enable Berkshelf and
    # the Berkshelf version on Chef 11.10 stacks. For more information, see
    # [Create a New
    # Stack](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
    # creating.html).
    chef_configuration: "ChefConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # Whether the stack uses custom cookbooks.
    use_custom_cookbooks: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether to associate the AWS OpsWorks Stacks built-in security groups with
    # the stack's layers.

    # AWS OpsWorks Stacks provides a standard set of built-in security groups,
    # one for each layer, which are associated with layers by default. With
    # `UseOpsworksSecurityGroups` you can instead provide your own custom
    # security groups. `UseOpsworksSecurityGroups` has the following settings:

    #   * True - AWS OpsWorks Stacks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it, but you cannot delete the built-in security group.

    #   * False - AWS OpsWorks Stacks does not associate built-in security groups with layers. You must create appropriate EC2 security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on creation; custom security groups are required only for those layers that need custom settings.

    # For more information, see [Create a New
    # Stack](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
    # creating.html).
    use_opsworks_security_groups: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains the information required to retrieve an app or cookbook from a
    # repository. For more information, see [Creating
    # Apps](http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-
    # creating.html) or [Custom Recipes and
    # Cookbooks](http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html).
    custom_cookbooks_source: "Source" = dataclasses.field(
        default_factory=dict,
    )

    # A default Amazon EC2 key pair name. The default value is none. If you
    # specify a key pair name, AWS OpsWorks installs the public key on the
    # instance and you can use the private key with an SSH client to log in to
    # the instance. For more information, see [ Using SSH to Communicate with an
    # Instance](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # ssh.html) and [ Managing SSH
    # Access](http://docs.aws.amazon.com/opsworks/latest/userguide/security-ssh-
    # access.html). You can override this setting by specifying a different key
    # pair, or no key pair, when you [ create an
    # instance](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # add.html).
    default_ssh_key_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The default root device type. This value is the default for all instances
    # in the stack, but you can override it when you create an instance. The
    # default option is `instance-store`. For more information, see [Storage for
    # the Root
    # Device](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-
    # for-the-root-device).
    default_root_device_type: "RootDeviceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The default AWS OpsWorks Stacks agent version. You have the following
    # options:

    #   * Auto-update - Set this parameter to `LATEST`. AWS OpsWorks Stacks automatically installs new agent versions on the stack's instances as soon as they are available.

    #   * Fixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the stack's instances.

    # The default setting is the most recent release of the agent. To specify an
    # agent version, you must use the complete version number, not the
    # abbreviated number shown on the console. For a list of available agent
    # version numbers, call DescribeAgentVersions. AgentVersion cannot be set to
    # Chef 12.2.

    # You can also specify an agent version when you create or update an
    # instance, which overrides the stack's default setting.
    agent_version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStackResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `CreateStack` request.
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
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stack ID, which is an opaque string that you use to identify the stack
    # when performing actions such as `DescribeStacks`.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUserProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "iam_user_arn",
                "IamUserArn",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_username",
                "SshUsername",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "SshPublicKey",
                autoboto.TypeInfo(str),
            ),
            (
                "allow_self_management",
                "AllowSelfManagement",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The user's IAM ARN; this can also be a federated user's ARN.
    iam_user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user's SSH user name. The allowable characters are [a-z], [A-Z], [0-9],
    # '-', and '_'. If the specified name includes other punctuation marks, AWS
    # OpsWorks Stacks removes them. For example, `my.name` will be changed to
    # `myname`. If you do not specify an SSH user name, AWS OpsWorks Stacks
    # generates one from the IAM user name.
    ssh_username: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user's public SSH key.
    ssh_public_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether users can specify their own SSH public key through the My Settings
    # page. For more information, see [Setting an IAM User's Public SSH
    # Key](http://docs.aws.amazon.com/opsworks/latest/userguide/security-
    # settingsshkey.html).
    allow_self_management: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateUserProfileResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `CreateUserProfile` request.
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
                "iam_user_arn",
                "IamUserArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The user's IAM ARN.
    iam_user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DataSource(autoboto.ShapeBase):
    """
    Describes an app's data source.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The data source's type, `AutoSelectOpsworksMysqlInstance`,
    # `OpsworksMysqlInstance`, `RdsDbInstance`, or `None`.
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The data source's ARN.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The database name.
    database_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAppRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "app_id",
                "AppId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The app ID.
    app_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "delete_elastic_ip",
                "DeleteElasticIp",
                autoboto.TypeInfo(bool),
            ),
            (
                "delete_volumes",
                "DeleteVolumes",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether to delete the instance Elastic IP address.
    delete_elastic_ip: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether to delete the instance's Amazon EBS volumes.
    delete_volumes: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteLayerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "layer_id",
                "LayerId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The layer ID.
    layer_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteStackRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUserProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "iam_user_arn",
                "IamUserArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user's IAM ARN. This can also be a federated user's ARN.
    iam_user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Deployment(autoboto.ShapeBase):
    """
    Describes a deployment of a stack or app.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_id",
                "DeploymentId",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "app_id",
                "AppId",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "completed_at",
                "CompletedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(int),
            ),
            (
                "iam_user_arn",
                "IamUserArn",
                autoboto.TypeInfo(str),
            ),
            (
                "comment",
                "Comment",
                autoboto.TypeInfo(str),
            ),
            (
                "command",
                "Command",
                autoboto.TypeInfo(DeploymentCommand),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_json",
                "CustomJson",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_ids",
                "InstanceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The deployment ID.
    deployment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The app ID.
    app_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Date when the deployment was created.
    created_at: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Date when the deployment completed.
    completed_at: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The deployment duration.
    duration: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user's IAM ARN.
    iam_user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A user-defined comment.
    comment: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Used to specify a stack or deployment command.
    command: "DeploymentCommand" = dataclasses.field(default_factory=dict, )

    # The deployment status:

    #   * running

    #   * successful

    #   * failed
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A string that contains user-defined custom JSON. It can be used to override
    # the corresponding default stack configuration attribute values for stack or
    # to pass data to recipes. The string should be in the following format:

    # `"{\"key1\": \"value1\", \"key2\": \"value2\",...}"`

    # For more information on custom JSON, see [Use Custom JSON to Modify the
    # Stack Configuration
    # Attributes](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
    # json.html).
    custom_json: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The IDs of the target instances.
    instance_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DeploymentCommand(autoboto.ShapeBase):
    """
    Used to specify a stack or deployment command.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(DeploymentCommandName),
            ),
            (
                "args",
                "Args",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
        ]

    # Specifies the operation. You can specify only one command.

    # For stacks, the following commands are available:

    #   * `execute_recipes`: Execute one or more recipes. To specify the recipes, set an `Args` parameter named `recipes` to the list of recipes to be executed. For example, to execute `phpapp::appsetup`, set `Args` to `{"recipes":["phpapp::appsetup"]}`.

    #   * `install_dependencies`: Install the stack's dependencies.

    #   * `update_custom_cookbooks`: Update the stack's custom cookbooks.

    #   * `update_dependencies`: Update the stack's dependencies.

    # The update_dependencies and install_dependencies commands are supported
    # only for Linux instances. You can run the commands successfully on Windows
    # instances, but they do nothing.

    # For apps, the following commands are available:

    #   * `deploy`: Deploy an app. Ruby on Rails apps have an optional `Args` parameter named `migrate`. Set `Args` to {"migrate":["true"]} to migrate the database. The default setting is {"migrate":["false"]}.

    #   * `rollback` Roll the app back to the previous version. When you update an app, AWS OpsWorks Stacks stores the previous version, up to a maximum of five versions. You can use this command to roll an app back as many as four versions.

    #   * `start`: Start the app's web or application server.

    #   * `stop`: Stop the app's web or application server.

    #   * `restart`: Restart the app's web or application server.

    #   * `undeploy`: Undeploy the app.
    name: "DeploymentCommandName" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The arguments of those commands that take arguments. It should be set to a
    # JSON object with the following format:

    # `{"arg_name1" : ["value1", "value2", ...], "arg_name2" : ["value1",
    # "value2", ...], ...}`

    # The `update_dependencies` command takes two arguments:

    #   * `upgrade_os_to` \- Specifies the desired Amazon Linux version for instances whose OS you want to upgrade, such as `Amazon Linux 2016.09`. You must also set the `allow_reboot` argument to true.

    #   * `allow_reboot` \- Specifies whether to allow AWS OpsWorks Stacks to reboot the instances if necessary, after installing the updates. This argument can be set to either `true` or `false`. The default value is `false`.

    # For example, to upgrade an instance to Amazon Linux 2016.09, set `Args` to
    # the following.

    # ` { "upgrade_os_to":["Amazon Linux 2016.09"], "allow_reboot":["true"] } `
    args: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class DeploymentCommandName(Enum):
    install_dependencies = "install_dependencies"
    update_dependencies = "update_dependencies"
    update_custom_cookbooks = "update_custom_cookbooks"
    execute_recipes = "execute_recipes"
    configure = "configure"
    setup = "setup"
    deploy = "deploy"
    rollback = "rollback"
    start = "start"
    stop = "stop"
    restart = "restart"
    undeploy = "undeploy"


@dataclasses.dataclass
class DeregisterEcsClusterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ecs_cluster_arn",
                "EcsClusterArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The cluster's Amazon Resource Number (ARN).
    ecs_cluster_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeregisterElasticIpRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "elastic_ip",
                "ElasticIp",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Elastic IP address.
    elastic_ip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterRdsDbInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rds_db_instance_arn",
                "RdsDbInstanceArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon RDS instance's ARN.
    rds_db_instance_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeregisterVolumeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_id",
                "VolumeId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The AWS OpsWorks Stacks volume ID, which is the GUID that AWS OpsWorks
    # Stacks assigned to the instance when you registered the volume with the
    # stack, not the Amazon EC2 volume ID.
    volume_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAgentVersionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "configuration_manager",
                "ConfigurationManager",
                autoboto.TypeInfo(StackConfigurationManager),
            ),
        ]

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The configuration manager.
    configuration_manager: "StackConfigurationManager" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeAgentVersionsResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeAgentVersions` request.
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
                "agent_versions",
                "AgentVersions",
                autoboto.TypeInfo(typing.List[AgentVersion]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The agent versions for the specified stack or configuration manager. Note
    # that this value is the complete version number, not the abbreviated number
    # used by the console.
    agent_versions: typing.List["AgentVersion"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeAppsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "app_ids",
                "AppIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The app stack ID. If you use this parameter, `DescribeApps` returns a
    # description of the apps in the specified stack.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of app IDs for the apps to be described. If you use this
    # parameter, `DescribeApps` returns a description of the specified apps.
    # Otherwise, it returns a description of every app.
    app_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeAppsResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeApps` request.
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
                "apps",
                "Apps",
                autoboto.TypeInfo(typing.List[App]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of `App` objects that describe the specified apps.
    apps: typing.List["App"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeCommandsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_id",
                "DeploymentId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "command_ids",
                "CommandIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The deployment ID. If you include this parameter, `DescribeCommands`
    # returns a description of the commands associated with the specified
    # deployment.
    deployment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance ID. If you include this parameter, `DescribeCommands` returns
    # a description of the commands associated with the specified instance.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of command IDs. If you include this parameter, `DescribeCommands`
    # returns a description of the specified commands. Otherwise, it returns a
    # description of every command.
    command_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeCommandsResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeCommands` request.
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
                "commands",
                "Commands",
                autoboto.TypeInfo(typing.List[Command]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of `Command` objects that describe each of the specified commands.
    commands: typing.List["Command"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeDeploymentsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "app_id",
                "AppId",
                autoboto.TypeInfo(str),
            ),
            (
                "deployment_ids",
                "DeploymentIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The stack ID. If you include this parameter, the command returns a
    # description of the commands associated with the specified stack.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The app ID. If you include this parameter, the command returns a
    # description of the commands associated with the specified app.
    app_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of deployment IDs to be described. If you include this parameter,
    # the command returns a description of the specified deployments. Otherwise,
    # it returns a description of every deployment.
    deployment_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeDeploymentsResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeDeployments` request.
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
                "deployments",
                "Deployments",
                autoboto.TypeInfo(typing.List[Deployment]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of `Deployment` objects that describe the deployments.
    deployments: typing.List["Deployment"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeEcsClustersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ecs_cluster_arns",
                "EcsClusterArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "stack_id",
                "StackId",
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

    # A list of ARNs, one for each cluster to be described.
    ecs_cluster_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A stack ID. `DescribeEcsClusters` returns a description of the cluster that
    # is registered with the stack.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the previous paginated request did not return all of the remaining
    # results, the response object's`NextToken` parameter value is set to a
    # token. To retrieve the next set of results, call `DescribeEcsClusters`
    # again and assign that token to the request object's `NextToken` parameter.
    # If there are no remaining results, the previous response object's
    # `NextToken` parameter is set to `null`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # To receive a paginated response, use this parameter to specify the maximum
    # number of results to be returned with a single call. If the number of
    # available results exceeds this maximum, the response includes a `NextToken`
    # value that you can assign to the `NextToken` request parameter to get the
    # next set of results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEcsClustersResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeEcsClusters` request.
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
                "ecs_clusters",
                "EcsClusters",
                autoboto.TypeInfo(typing.List[EcsCluster]),
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

    # A list of `EcsCluster` objects containing the cluster descriptions.
    ecs_clusters: typing.List["EcsCluster"] = dataclasses.field(
        default_factory=list,
    )

    # If a paginated request does not return all of the remaining results, this
    # parameter is set to a token that you can assign to the request object's
    # `NextToken` parameter to retrieve the next set of results. If the previous
    # paginated request returned all of the remaining results, this parameter is
    # set to `null`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeElasticIpsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "ips",
                "Ips",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The instance ID. If you include this parameter, `DescribeElasticIps`
    # returns a description of the Elastic IP addresses associated with the
    # specified instance.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A stack ID. If you include this parameter, `DescribeElasticIps` returns a
    # description of the Elastic IP addresses that are registered with the
    # specified stack.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of Elastic IP addresses to be described. If you include this
    # parameter, `DescribeElasticIps` returns a description of the specified
    # Elastic IP addresses. Otherwise, it returns a description of every Elastic
    # IP address.
    ips: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeElasticIpsResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeElasticIps` request.
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
                "elastic_ips",
                "ElasticIps",
                autoboto.TypeInfo(typing.List[ElasticIp]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An `ElasticIps` object that describes the specified Elastic IP addresses.
    elastic_ips: typing.List["ElasticIp"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeElasticLoadBalancersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_ids",
                "LayerIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A stack ID. The action describes the stack's Elastic Load Balancing
    # instances.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of layer IDs. The action describes the Elastic Load Balancing
    # instances for the specified layers.
    layer_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeElasticLoadBalancersResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeElasticLoadBalancers` request.
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
                "elastic_load_balancers",
                "ElasticLoadBalancers",
                autoboto.TypeInfo(typing.List[ElasticLoadBalancer]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of `ElasticLoadBalancer` objects that describe the specified Elastic
    # Load Balancing instances.
    elastic_load_balancers: typing.List["ElasticLoadBalancer"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )


@dataclasses.dataclass
class DescribeInstancesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_id",
                "LayerId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_ids",
                "InstanceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A stack ID. If you use this parameter, `DescribeInstances` returns
    # descriptions of the instances associated with the specified stack.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A layer ID. If you use this parameter, `DescribeInstances` returns
    # descriptions of the instances associated with the specified layer.
    layer_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of instance IDs to be described. If you use this parameter,
    # `DescribeInstances` returns a description of the specified instances.
    # Otherwise, it returns a description of every instance.
    instance_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeInstancesResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeInstances` request.
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
                "instances",
                "Instances",
                autoboto.TypeInfo(typing.List[Instance]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of `Instance` objects that describe the instances.
    instances: typing.List["Instance"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeLayersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_ids",
                "LayerIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of layer IDs that specify the layers to be described. If you omit
    # this parameter, `DescribeLayers` returns a description of every layer in
    # the specified stack.
    layer_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeLayersResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeLayers` request.
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
                "layers",
                "Layers",
                autoboto.TypeInfo(typing.List[Layer]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of `Layer` objects that describe the layers.
    layers: typing.List["Layer"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeLoadBasedAutoScalingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "layer_ids",
                "LayerIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # An array of layer IDs.
    layer_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeLoadBasedAutoScalingResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeLoadBasedAutoScaling` request.
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
                "load_based_auto_scaling_configurations",
                "LoadBasedAutoScalingConfigurations",
                autoboto.TypeInfo(
                    typing.List[LoadBasedAutoScalingConfiguration]
                ),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of `LoadBasedAutoScalingConfiguration` objects that describe each
    # layer's configuration.
    load_based_auto_scaling_configurations: typing.List[
        "LoadBasedAutoScalingConfiguration"
    ] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeMyUserProfileResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeMyUserProfile` request.
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
                "user_profile",
                "UserProfile",
                autoboto.TypeInfo(SelfUserProfile),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A `UserProfile` object that describes the user's SSH information.
    user_profile: "SelfUserProfile" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeOperatingSystemsResponse(autoboto.OutputShapeBase):
    """
    The response to a `DescribeOperatingSystems` request.
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
                "operating_systems",
                "OperatingSystems",
                autoboto.TypeInfo(typing.List[OperatingSystem]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains information in response to a `DescribeOperatingSystems` request.
    operating_systems: typing.List["OperatingSystem"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribePermissionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "iam_user_arn",
                "IamUserArn",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user's IAM ARN. This can also be a federated user's ARN. For more
    # information about IAM ARNs, see [Using
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html).
    iam_user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePermissionsResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribePermissions` request.
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
                "permissions",
                "Permissions",
                autoboto.TypeInfo(typing.List[Permission]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of `Permission` objects that describe the stack permissions.

    #   * If the request object contains only a stack ID, the array contains a `Permission` object with permissions for each of the stack IAM ARNs.

    #   * If the request object contains only an IAM ARN, the array contains a `Permission` object with permissions for each of the user's stack IDs.

    #   * If the request contains a stack ID and an IAM ARN, the array contains a single `Permission` object with permissions for the specified stack and IAM ARN.
    permissions: typing.List["Permission"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeRaidArraysRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "raid_array_ids",
                "RaidArrayIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The instance ID. If you use this parameter, `DescribeRaidArrays` returns
    # descriptions of the RAID arrays associated with the specified instance.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of RAID array IDs. If you use this parameter, `DescribeRaidArrays`
    # returns descriptions of the specified arrays. Otherwise, it returns a
    # description of every array.
    raid_array_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeRaidArraysResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeRaidArrays` request.
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
                "raid_arrays",
                "RaidArrays",
                autoboto.TypeInfo(typing.List[RaidArray]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A `RaidArrays` object that describes the specified RAID arrays.
    raid_arrays: typing.List["RaidArray"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeRdsDbInstancesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "rds_db_instance_arns",
                "RdsDbInstanceArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the stack with which the instances are registered. The operation
    # returns descriptions of all registered Amazon RDS instances.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array containing the ARNs of the instances to be described.
    rds_db_instance_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeRdsDbInstancesResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeRdsDbInstances` request.
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
                "rds_db_instances",
                "RdsDbInstances",
                autoboto.TypeInfo(typing.List[RdsDbInstance]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An a array of `RdsDbInstance` objects that describe the instances.
    rds_db_instances: typing.List["RdsDbInstance"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeServiceErrorsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "service_error_ids",
                "ServiceErrorIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The stack ID. If you use this parameter, `DescribeServiceErrors` returns
    # descriptions of the errors associated with the specified stack.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance ID. If you use this parameter, `DescribeServiceErrors` returns
    # descriptions of the errors associated with the specified instance.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of service error IDs. If you use this parameter,
    # `DescribeServiceErrors` returns descriptions of the specified errors.
    # Otherwise, it returns a description of every error.
    service_error_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeServiceErrorsResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeServiceErrors` request.
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
                "service_errors",
                "ServiceErrors",
                autoboto.TypeInfo(typing.List[ServiceError]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of `ServiceError` objects that describe the specified service
    # errors.
    service_errors: typing.List["ServiceError"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeStackProvisioningParametersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStackProvisioningParametersResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeStackProvisioningParameters` request.
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
                "agent_installer_url",
                "AgentInstallerUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS OpsWorks Stacks agent installer's URL.
    agent_installer_url: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An embedded object that contains the provisioning parameters.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeStackSummaryRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStackSummaryResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeStackSummary` request.
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
                "stack_summary",
                "StackSummary",
                autoboto.TypeInfo(StackSummary),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A `StackSummary` object that contains the results.
    stack_summary: "StackSummary" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeStacksRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_ids",
                "StackIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # An array of stack IDs that specify the stacks to be described. If you omit
    # this parameter, `DescribeStacks` returns a description of every stack.
    stack_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeStacksResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeStacks` request.
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
                "stacks",
                "Stacks",
                autoboto.TypeInfo(typing.List[Stack]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of `Stack` objects that describe the stacks.
    stacks: typing.List["Stack"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeTimeBasedAutoScalingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_ids",
                "InstanceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # An array of instance IDs.
    instance_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeTimeBasedAutoScalingResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeTimeBasedAutoScaling` request.
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
                "time_based_auto_scaling_configurations",
                "TimeBasedAutoScalingConfigurations",
                autoboto.TypeInfo(
                    typing.List[TimeBasedAutoScalingConfiguration]
                ),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of `TimeBasedAutoScalingConfiguration` objects that describe the
    # configuration for the specified instances.
    time_based_auto_scaling_configurations: typing.List[
        "TimeBasedAutoScalingConfiguration"
    ] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeUserProfilesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "iam_user_arns",
                "IamUserArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # An array of IAM or federated user ARNs that identify the users to be
    # described.
    iam_user_arns: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeUserProfilesResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeUserProfiles` request.
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
                "user_profiles",
                "UserProfiles",
                autoboto.TypeInfo(typing.List[UserProfile]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A `Users` object that describes the specified users.
    user_profiles: typing.List["UserProfile"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeVolumesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "raid_array_id",
                "RaidArrayId",
                autoboto.TypeInfo(str),
            ),
            (
                "volume_ids",
                "VolumeIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The instance ID. If you use this parameter, `DescribeVolumes` returns
    # descriptions of the volumes associated with the specified instance.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A stack ID. The action describes the stack's registered Amazon EBS volumes.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The RAID array ID. If you use this parameter, `DescribeVolumes` returns
    # descriptions of the volumes associated with the specified RAID array.
    raid_array_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Am array of volume IDs. If you use this parameter, `DescribeVolumes`
    # returns descriptions of the specified volumes. Otherwise, it returns a
    # description of every volume.
    volume_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeVolumesResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `DescribeVolumes` request.
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
                "volumes",
                "Volumes",
                autoboto.TypeInfo(typing.List[Volume]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of volume IDs.
    volumes: typing.List["Volume"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DetachElasticLoadBalancerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "elastic_load_balancer_name",
                "ElasticLoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_id",
                "LayerId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Elastic Load Balancing instance's name.
    elastic_load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the layer that the Elastic Load Balancing instance is attached
    # to.
    layer_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateElasticIpRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "elastic_ip",
                "ElasticIp",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Elastic IP address.
    elastic_ip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EbsBlockDevice(autoboto.ShapeBase):
    """
    Describes an Amazon EBS volume. This data type maps directly to the Amazon EC2
    [EbsBlockDevice](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html)
    data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "snapshot_id",
                "SnapshotId",
                autoboto.TypeInfo(str),
            ),
            (
                "iops",
                "Iops",
                autoboto.TypeInfo(int),
            ),
            (
                "volume_size",
                "VolumeSize",
                autoboto.TypeInfo(int),
            ),
            (
                "volume_type",
                "VolumeType",
                autoboto.TypeInfo(VolumeType),
            ),
            (
                "delete_on_termination",
                "DeleteOnTermination",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The snapshot ID.
    snapshot_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of I/O operations per second (IOPS) that the volume supports.
    # For more information, see
    # [EbsBlockDevice](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html).
    iops: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The volume size, in GiB. For more information, see
    # [EbsBlockDevice](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html).
    volume_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The volume type. `gp2` for General Purpose (SSD) volumes, `io1` for
    # Provisioned IOPS (SSD) volumes, `st1` for Throughput Optimized hard disk
    # drives (HDD), `sc1` for Cold HDD,and `standard` for Magnetic volumes.

    # If you specify the `io1` volume type, you must also specify a value for the
    # `Iops` attribute. The maximum ratio of provisioned IOPS to requested volume
    # size (in GiB) is 50:1. AWS uses the default volume size (in GiB) specified
    # in the AMI attributes to set IOPS to 50 x (volume size).
    volume_type: "VolumeType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether the volume is deleted on instance termination.
    delete_on_termination: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EcsCluster(autoboto.ShapeBase):
    """
    Describes a registered Amazon ECS cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ecs_cluster_arn",
                "EcsClusterArn",
                autoboto.TypeInfo(str),
            ),
            (
                "ecs_cluster_name",
                "EcsClusterName",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "registered_at",
                "RegisteredAt",
                autoboto.TypeInfo(str),
            ),
        ]

    # The cluster's ARN.
    ecs_cluster_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The cluster name.
    ecs_cluster_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time and date that the cluster was registered with the stack.
    registered_at: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ElasticIp(autoboto.ShapeBase):
    """
    Describes an Elastic IP address.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip",
                "Ip",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "domain",
                "Domain",
                autoboto.TypeInfo(str),
            ),
            (
                "region",
                "Region",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The IP address.
    ip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The domain.
    domain: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The AWS region. For more information, see [Regions and
    # Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html).
    region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the instance that the address is attached to.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ElasticLoadBalancer(autoboto.ShapeBase):
    """
    Describes an Elastic Load Balancing instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "elastic_load_balancer_name",
                "ElasticLoadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "region",
                "Region",
                autoboto.TypeInfo(str),
            ),
            (
                "dns_name",
                "DnsName",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_id",
                "LayerId",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "ec2_instance_ids",
                "Ec2InstanceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The Elastic Load Balancing instance's name.
    elastic_load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance's AWS region.
    region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's public DNS name.
    dns_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the stack that the instance is associated with.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the layer that the instance is attached to.
    layer_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The VPC ID.
    vpc_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of Availability Zones.
    availability_zones: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list of subnet IDs, if the stack is running in a VPC.
    subnet_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of the EC2 instances that the Elastic Load Balancing instance is
    # managing traffic for.
    ec2_instance_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class EnvironmentVariable(autoboto.ShapeBase):
    """
    Represents an app's environment variable.
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
            (
                "secure",
                "Secure",
                autoboto.TypeInfo(bool),
            ),
        ]

    # (Required) The environment variable's name, which can consist of up to 64
    # characters and must be specified. The name can contain upper- and lowercase
    # letters, numbers, and underscores (_), but it must start with a letter or
    # underscore.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Optional) The environment variable's value, which can be left empty. If
    # you specify a value, it can contain up to 256 characters, which must all be
    # printable.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Optional) Whether the variable's value will be returned by the
    # DescribeApps action. To conceal an environment variable's value, set
    # `Secure` to `true`. `DescribeApps` then returns `*****FILTERED*****`
    # instead of the actual value. The default value for `Secure` is `false`.
    secure: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetHostnameSuggestionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "layer_id",
                "LayerId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The layer ID.
    layer_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetHostnameSuggestionResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `GetHostnameSuggestion` request.
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
                "layer_id",
                "LayerId",
                autoboto.TypeInfo(str),
            ),
            (
                "hostname",
                "Hostname",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The layer ID.
    layer_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The generated host name.
    hostname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GrantAccessRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "valid_for_in_minutes",
                "ValidForInMinutes",
                autoboto.TypeInfo(int),
            ),
        ]

    # The instance's AWS OpsWorks Stacks ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The length of time (in minutes) that the grant is valid. When the grant
    # expires at the end of this period, the user will no longer be able to use
    # the credentials to log in. If the user is logged in at the time, he or she
    # automatically will be logged out.
    valid_for_in_minutes: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GrantAccessResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `GrantAccess` request.
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
                "temporary_credential",
                "TemporaryCredential",
                autoboto.TypeInfo(TemporaryCredential),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A `TemporaryCredential` object that contains the data needed to log in to
    # the instance by RDP clients, such as the Microsoft Remote Desktop
    # Connection.
    temporary_credential: "TemporaryCredential" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class Instance(autoboto.ShapeBase):
    """
    Describes an instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_version",
                "AgentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "ami_id",
                "AmiId",
                autoboto.TypeInfo(str),
            ),
            (
                "architecture",
                "Architecture",
                autoboto.TypeInfo(Architecture),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "auto_scaling_type",
                "AutoScalingType",
                autoboto.TypeInfo(AutoScalingType),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "block_device_mappings",
                "BlockDeviceMappings",
                autoboto.TypeInfo(typing.List[BlockDeviceMapping]),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "ebs_optimized",
                "EbsOptimized",
                autoboto.TypeInfo(bool),
            ),
            (
                "ec2_instance_id",
                "Ec2InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "ecs_cluster_arn",
                "EcsClusterArn",
                autoboto.TypeInfo(str),
            ),
            (
                "ecs_container_instance_arn",
                "EcsContainerInstanceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "elastic_ip",
                "ElasticIp",
                autoboto.TypeInfo(str),
            ),
            (
                "hostname",
                "Hostname",
                autoboto.TypeInfo(str),
            ),
            (
                "infrastructure_class",
                "InfrastructureClass",
                autoboto.TypeInfo(str),
            ),
            (
                "install_updates_on_boot",
                "InstallUpdatesOnBoot",
                autoboto.TypeInfo(bool),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_profile_arn",
                "InstanceProfileArn",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                autoboto.TypeInfo(str),
            ),
            (
                "last_service_error_id",
                "LastServiceErrorId",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_ids",
                "LayerIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "os",
                "Os",
                autoboto.TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                autoboto.TypeInfo(str),
            ),
            (
                "private_dns",
                "PrivateDns",
                autoboto.TypeInfo(str),
            ),
            (
                "private_ip",
                "PrivateIp",
                autoboto.TypeInfo(str),
            ),
            (
                "public_dns",
                "PublicDns",
                autoboto.TypeInfo(str),
            ),
            (
                "public_ip",
                "PublicIp",
                autoboto.TypeInfo(str),
            ),
            (
                "registered_by",
                "RegisteredBy",
                autoboto.TypeInfo(str),
            ),
            (
                "reported_agent_version",
                "ReportedAgentVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "reported_os",
                "ReportedOs",
                autoboto.TypeInfo(ReportedOs),
            ),
            (
                "root_device_type",
                "RootDeviceType",
                autoboto.TypeInfo(RootDeviceType),
            ),
            (
                "root_device_volume_id",
                "RootDeviceVolumeId",
                autoboto.TypeInfo(str),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "ssh_host_dsa_key_fingerprint",
                "SshHostDsaKeyFingerprint",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_host_rsa_key_fingerprint",
                "SshHostRsaKeyFingerprint",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_key_name",
                "SshKeyName",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_id",
                "SubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "tenancy",
                "Tenancy",
                autoboto.TypeInfo(str),
            ),
            (
                "virtualization_type",
                "VirtualizationType",
                autoboto.TypeInfo(VirtualizationType),
            ),
        ]

    # The agent version. This parameter is set to `INHERIT` if the instance
    # inherits the default stack setting or to a a version number for a fixed
    # agent version.
    agent_version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A custom AMI ID to be used to create the instance. For more information,
    # see
    # [Instances](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # custom-ami.html)
    ami_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance architecture: "i386" or "x86_64".
    architecture: "Architecture" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance's Amazon Resource Number (ARN).
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # For load-based or time-based instances, the type.
    auto_scaling_type: "AutoScalingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance Availability Zone. For more information, see [Regions and
    # Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html).
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of `BlockDeviceMapping` objects that specify the instance's block
    # device mappings.
    block_device_mappings: typing.List["BlockDeviceMapping"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )

    # The time that the instance was created.
    created_at: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether this is an Amazon EBS-optimized instance.
    ebs_optimized: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the associated Amazon EC2 instance.
    ec2_instance_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # For container instances, the Amazon ECS cluster's ARN.
    ecs_cluster_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # For container instances, the instance's ARN.
    ecs_container_instance_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance [Elastic IP address
    # ](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-
    # eip.html).
    elastic_ip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance host name.
    hostname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # For registered instances, the infrastructure class: `ec2` or `on-premises`.
    infrastructure_class: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether to install operating system and package updates when the instance
    # boots. The default value is `true`. If this value is set to `false`, you
    # must then update your instances manually by using CreateDeployment to run
    # the `update_dependencies` stack command or by manually running `yum`
    # (Amazon Linux) or `apt-get` (Ubuntu) on the instances.

    # We strongly recommend using the default value of `true`, to ensure that
    # your instances have the latest security updates.
    install_updates_on_boot: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the instance's IAM profile. For more information about IAM ARNs,
    # see [Using
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html).
    instance_profile_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance type, such as `t2.micro`.
    instance_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the last service error. For more information, call
    # DescribeServiceErrors.
    last_service_error_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array containing the instance layer IDs.
    layer_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The instance's operating system.
    os: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's platform.
    platform: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's private DNS name.
    private_dns: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's private IP address.
    private_ip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance public DNS name.
    public_dns: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance public IP address.
    public_ip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # For registered instances, who performed the registration.
    registered_by: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's reported AWS OpsWorks Stacks agent version.
    reported_agent_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # For registered instances, the reported operating system.
    reported_os: "ReportedOs" = dataclasses.field(default_factory=dict, )

    # The instance's root device type. For more information, see [Storage for the
    # Root
    # Device](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-
    # for-the-root-device).
    root_device_type: "RootDeviceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The root device volume ID.
    root_device_volume_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array containing the instance security group IDs.
    security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The SSH key's Deep Security Agent (DSA) fingerprint.
    ssh_host_dsa_key_fingerprint: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The SSH key's RSA fingerprint.
    ssh_host_rsa_key_fingerprint: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance's Amazon EC2 key-pair name.
    ssh_key_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance status:

    #   * `booting`

    #   * `connection_lost`

    #   * `online`

    #   * `pending`

    #   * `rebooting`

    #   * `requested`

    #   * `running_setup`

    #   * `setup_failed`

    #   * `shutting_down`

    #   * `start_failed`

    #   * `stop_failed`

    #   * `stopped`

    #   * `stopping`

    #   * `terminated`

    #   * `terminating`
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's subnet ID; applicable only if the stack is running in a VPC.
    subnet_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's tenancy option, such as `dedicated` or `host`.
    tenancy: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's virtualization type: `paravirtual` or `hvm`.
    virtualization_type: "VirtualizationType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceIdentity(autoboto.ShapeBase):
    """
    Contains a description of an Amazon EC2 instance from the Amazon EC2 metadata
    service. For more information, see [Instance Metadata and User
    Data](http://docs.aws.amazon.com/sdkfornet/latest/apidocs/Index.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document",
                "Document",
                autoboto.TypeInfo(str),
            ),
            (
                "signature",
                "Signature",
                autoboto.TypeInfo(str),
            ),
        ]

    # A JSON document that contains the metadata.
    document: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A signature that can be used to verify the document's accuracy and
    # authenticity.
    signature: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstancesCount(autoboto.ShapeBase):
    """
    Describes how many instances a stack has for each status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assigning",
                "Assigning",
                autoboto.TypeInfo(int),
            ),
            (
                "booting",
                "Booting",
                autoboto.TypeInfo(int),
            ),
            (
                "connection_lost",
                "ConnectionLost",
                autoboto.TypeInfo(int),
            ),
            (
                "deregistering",
                "Deregistering",
                autoboto.TypeInfo(int),
            ),
            (
                "online",
                "Online",
                autoboto.TypeInfo(int),
            ),
            (
                "pending",
                "Pending",
                autoboto.TypeInfo(int),
            ),
            (
                "rebooting",
                "Rebooting",
                autoboto.TypeInfo(int),
            ),
            (
                "registered",
                "Registered",
                autoboto.TypeInfo(int),
            ),
            (
                "registering",
                "Registering",
                autoboto.TypeInfo(int),
            ),
            (
                "requested",
                "Requested",
                autoboto.TypeInfo(int),
            ),
            (
                "running_setup",
                "RunningSetup",
                autoboto.TypeInfo(int),
            ),
            (
                "setup_failed",
                "SetupFailed",
                autoboto.TypeInfo(int),
            ),
            (
                "shutting_down",
                "ShuttingDown",
                autoboto.TypeInfo(int),
            ),
            (
                "start_failed",
                "StartFailed",
                autoboto.TypeInfo(int),
            ),
            (
                "stop_failed",
                "StopFailed",
                autoboto.TypeInfo(int),
            ),
            (
                "stopped",
                "Stopped",
                autoboto.TypeInfo(int),
            ),
            (
                "stopping",
                "Stopping",
                autoboto.TypeInfo(int),
            ),
            (
                "terminated",
                "Terminated",
                autoboto.TypeInfo(int),
            ),
            (
                "terminating",
                "Terminating",
                autoboto.TypeInfo(int),
            ),
            (
                "unassigning",
                "Unassigning",
                autoboto.TypeInfo(int),
            ),
        ]

    # The number of instances in the Assigning state.
    assigning: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances with `booting` status.
    booting: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances with `connection_lost` status.
    connection_lost: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of instances in the Deregistering state.
    deregistering: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances with `online` status.
    online: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances with `pending` status.
    pending: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances with `rebooting` status.
    rebooting: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances in the Registered state.
    registered: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances in the Registering state.
    registering: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances with `requested` status.
    requested: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances with `running_setup` status.
    running_setup: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances with `setup_failed` status.
    setup_failed: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances with `shutting_down` status.
    shutting_down: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances with `start_failed` status.
    start_failed: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances with `stop_failed` status.
    stop_failed: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances with `stopped` status.
    stopped: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances with `stopping` status.
    stopping: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances with `terminated` status.
    terminated: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances with `terminating` status.
    terminating: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of instances in the Unassigning state.
    unassigning: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Layer(autoboto.ShapeBase):
    """
    Describes a layer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_id",
                "LayerId",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(LayerType),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "shortname",
                "Shortname",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[LayerAttributesKeys, str]),
            ),
            (
                "cloud_watch_logs_configuration",
                "CloudWatchLogsConfiguration",
                autoboto.TypeInfo(CloudWatchLogsConfiguration),
            ),
            (
                "custom_instance_profile_arn",
                "CustomInstanceProfileArn",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_json",
                "CustomJson",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_security_group_ids",
                "CustomSecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "default_security_group_names",
                "DefaultSecurityGroupNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "packages",
                "Packages",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "volume_configurations",
                "VolumeConfigurations",
                autoboto.TypeInfo(typing.List[VolumeConfiguration]),
            ),
            (
                "enable_auto_healing",
                "EnableAutoHealing",
                autoboto.TypeInfo(bool),
            ),
            (
                "auto_assign_elastic_ips",
                "AutoAssignElasticIps",
                autoboto.TypeInfo(bool),
            ),
            (
                "auto_assign_public_ips",
                "AutoAssignPublicIps",
                autoboto.TypeInfo(bool),
            ),
            (
                "default_recipes",
                "DefaultRecipes",
                autoboto.TypeInfo(Recipes),
            ),
            (
                "custom_recipes",
                "CustomRecipes",
                autoboto.TypeInfo(Recipes),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "install_updates_on_boot",
                "InstallUpdatesOnBoot",
                autoboto.TypeInfo(bool),
            ),
            (
                "use_ebs_optimized_instances",
                "UseEbsOptimizedInstances",
                autoboto.TypeInfo(bool),
            ),
            (
                "lifecycle_event_configuration",
                "LifecycleEventConfiguration",
                autoboto.TypeInfo(LifecycleEventConfiguration),
            ),
        ]

    # The Amazon Resource Number (ARN) of a layer.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The layer stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The layer ID.
    layer_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The layer type.
    type: "LayerType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The layer name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The layer short name.
    shortname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The layer attributes.

    # For the `HaproxyStatsPassword`, `MysqlRootPassword`, and `GangliaPassword`
    # attributes, AWS OpsWorks Stacks returns `*****FILTERED*****` instead of the
    # actual value

    # For an ECS Cluster layer, AWS OpsWorks Stacks the `EcsClusterArn` attribute
    # is set to the cluster's ARN.
    attributes: typing.Dict["LayerAttributesKeys", str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon CloudWatch Logs configuration settings for the layer.
    cloud_watch_logs_configuration: "CloudWatchLogsConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The ARN of the default IAM profile to be used for the layer's EC2
    # instances. For more information about IAM ARNs, see [Using
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html).
    custom_instance_profile_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A JSON formatted string containing the layer's custom stack configuration
    # and deployment attributes.
    custom_json: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array containing the layer's custom security group IDs.
    custom_security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # An array containing the layer's security group names.
    default_security_group_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # An array of `Package` objects that describe the layer's packages.
    packages: typing.List[str] = dataclasses.field(default_factory=list, )

    # A `VolumeConfigurations` object that describes the layer's Amazon EBS
    # volumes.
    volume_configurations: typing.List["VolumeConfiguration"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )

    # Whether auto healing is disabled for the layer.
    enable_auto_healing: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether to automatically assign an [Elastic IP
    # address](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-
    # addresses-eip.html) to the layer's instances. For more information, see
    # [How to Edit a
    # Layer](http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-
    # basics-edit.html).
    auto_assign_elastic_ips: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # For stacks that are running in a VPC, whether to automatically assign a
    # public IP address to the layer's instances. For more information, see [How
    # to Edit a
    # Layer](http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-
    # basics-edit.html).
    auto_assign_public_ips: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # AWS OpsWorks Stacks supports five lifecycle events: **setup** ,
    # **configuration** , **deploy** , **undeploy** , and **shutdown**. For each
    # layer, AWS OpsWorks Stacks runs a set of standard recipes for each event.
    # In addition, you can provide custom recipes for any or all layers and
    # events. AWS OpsWorks Stacks runs custom event recipes after the standard
    # recipes. `LayerCustomRecipes` specifies the custom recipes for a particular
    # layer to be run in response to each of the five events.

    # To specify a recipe, use the cookbook's directory name in the repository
    # followed by two colons and the recipe name, which is the recipe's file name
    # without the .rb extension. For example: phpapp2::dbsetup specifies the
    # dbsetup.rb recipe in the repository's phpapp2 folder.
    default_recipes: "Recipes" = dataclasses.field(default_factory=dict, )

    # A `LayerCustomRecipes` object that specifies the layer's custom recipes.
    custom_recipes: "Recipes" = dataclasses.field(default_factory=dict, )

    # Date when the layer was created.
    created_at: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether to install operating system and package updates when the instance
    # boots. The default value is `true`. If this value is set to `false`, you
    # must then update your instances manually by using CreateDeployment to run
    # the `update_dependencies` stack command or manually running `yum` (Amazon
    # Linux) or `apt-get` (Ubuntu) on the instances.

    # We strongly recommend using the default value of `true`, to ensure that
    # your instances have the latest security updates.
    install_updates_on_boot: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether the layer uses Amazon EBS-optimized instances.
    use_ebs_optimized_instances: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A `LifeCycleEventConfiguration` object that specifies the Shutdown event
    # configuration.
    lifecycle_event_configuration: "LifecycleEventConfiguration" = dataclasses.field(
        default_factory=dict,
    )


class LayerAttributesKeys(Enum):
    EcsClusterArn = "EcsClusterArn"
    EnableHaproxyStats = "EnableHaproxyStats"
    HaproxyStatsUrl = "HaproxyStatsUrl"
    HaproxyStatsUser = "HaproxyStatsUser"
    HaproxyStatsPassword = "HaproxyStatsPassword"
    HaproxyHealthCheckUrl = "HaproxyHealthCheckUrl"
    HaproxyHealthCheckMethod = "HaproxyHealthCheckMethod"
    MysqlRootPassword = "MysqlRootPassword"
    MysqlRootPasswordUbiquitous = "MysqlRootPasswordUbiquitous"
    GangliaUrl = "GangliaUrl"
    GangliaUser = "GangliaUser"
    GangliaPassword = "GangliaPassword"
    MemcachedMemory = "MemcachedMemory"
    NodejsVersion = "NodejsVersion"
    RubyVersion = "RubyVersion"
    RubygemsVersion = "RubygemsVersion"
    ManageBundler = "ManageBundler"
    BundlerVersion = "BundlerVersion"
    RailsStack = "RailsStack"
    PassengerVersion = "PassengerVersion"
    Jvm = "Jvm"
    JvmVersion = "JvmVersion"
    JvmOptions = "JvmOptions"
    JavaAppServer = "JavaAppServer"
    JavaAppServerVersion = "JavaAppServerVersion"


class LayerType(Enum):
    aws_flow_ruby = "aws-flow-ruby"
    ecs_cluster = "ecs-cluster"
    java_app = "java-app"
    lb = "lb"
    web = "web"
    php_app = "php-app"
    rails_app = "rails-app"
    nodejs_app = "nodejs-app"
    memcached = "memcached"
    db_master = "db-master"
    monitoring_master = "monitoring-master"
    custom = "custom"


@dataclasses.dataclass
class LifecycleEventConfiguration(autoboto.ShapeBase):
    """
    Specifies the lifecycle event configuration
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "shutdown",
                "Shutdown",
                autoboto.TypeInfo(ShutdownEventConfiguration),
            ),
        ]

    # A `ShutdownEventConfiguration` object that specifies the Shutdown event
    # configuration.
    shutdown: "ShutdownEventConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ListTagsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
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

    # The stack or layer's Amazon Resource Number (ARN).
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Do not use. A validation exception occurs if you add a `MaxResults`
    # parameter to a `ListTagsRequest` call.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Do not use. A validation exception occurs if you add a `NextToken`
    # parameter to a `ListTagsRequest` call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `ListTags` request.
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
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.Dict[str, str]),
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

    # A set of key-value pairs that contain tag keys and tag values that are
    # attached to a stack or layer.
    tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If a paginated request does not return all of the remaining results, this
    # parameter is set to a token that you can assign to the request object's
    # `NextToken` parameter to get the next set of results. If the previous
    # paginated request returned all of the remaining results, this parameter is
    # set to `null`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LoadBasedAutoScalingConfiguration(autoboto.ShapeBase):
    """
    Describes a layer's load-based auto scaling configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "layer_id",
                "LayerId",
                autoboto.TypeInfo(str),
            ),
            (
                "enable",
                "Enable",
                autoboto.TypeInfo(bool),
            ),
            (
                "up_scaling",
                "UpScaling",
                autoboto.TypeInfo(AutoScalingThresholds),
            ),
            (
                "down_scaling",
                "DownScaling",
                autoboto.TypeInfo(AutoScalingThresholds),
            ),
        ]

    # The layer ID.
    layer_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether load-based auto scaling is enabled for the layer.
    enable: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An `AutoScalingThresholds` object that describes the upscaling
    # configuration, which defines how and when AWS OpsWorks Stacks increases the
    # number of instances.
    up_scaling: "AutoScalingThresholds" = dataclasses.field(
        default_factory=dict,
    )

    # An `AutoScalingThresholds` object that describes the downscaling
    # configuration, which defines how and when AWS OpsWorks Stacks reduces the
    # number of instances.
    down_scaling: "AutoScalingThresholds" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class OperatingSystem(autoboto.ShapeBase):
    """
    Describes supported operating systems in AWS OpsWorks Stacks.
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
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
            (
                "configuration_managers",
                "ConfigurationManagers",
                autoboto.TypeInfo(
                    typing.List[OperatingSystemConfigurationManager]
                ),
            ),
            (
                "reported_name",
                "ReportedName",
                autoboto.TypeInfo(str),
            ),
            (
                "reported_version",
                "ReportedVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "supported",
                "Supported",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the operating system, such as `Amazon Linux 2017.09`.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of a supported operating system, such as `Amazon Linux 2017.09`.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of a supported operating system, either `Linux` or `Windows`.
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Supported configuration manager name and versions for an AWS OpsWorks
    # Stacks operating system.
    configuration_managers: typing.List["OperatingSystemConfigurationManager"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )

    # A short name for the operating system manufacturer.
    reported_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version of the operating system, including the release and edition, if
    # applicable.
    reported_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates that an operating system is not supported for new instances.
    supported: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OperatingSystemConfigurationManager(autoboto.ShapeBase):
    """
    A block that contains information about the configuration manager (Chef) and the
    versions of the configuration manager that are supported for an operating
    system.
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
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the configuration manager, which is Chef.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The versions of the configuration manager that are supported by an
    # operating system.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Permission(autoboto.ShapeBase):
    """
    Describes stack or user permissions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "iam_user_arn",
                "IamUserArn",
                autoboto.TypeInfo(str),
            ),
            (
                "allow_ssh",
                "AllowSsh",
                autoboto.TypeInfo(bool),
            ),
            (
                "allow_sudo",
                "AllowSudo",
                autoboto.TypeInfo(bool),
            ),
            (
                "level",
                "Level",
                autoboto.TypeInfo(str),
            ),
        ]

    # A stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for an AWS Identity and Access Management
    # (IAM) role. For more information about IAM ARNs, see [Using
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html).
    iam_user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether the user can use SSH.
    allow_ssh: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether the user can use **sudo**.
    allow_sudo: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user's permission level, which must be the following:

    #   * `deny`

    #   * `show`

    #   * `deploy`

    #   * `manage`

    #   * `iam_only`

    # For more information on the permissions associated with these levels, see
    # [Managing User
    # Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
    # security-users.html)
    level: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RaidArray(autoboto.ShapeBase):
    """
    Describes an instance's RAID array.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "raid_array_id",
                "RaidArrayId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "raid_level",
                "RaidLevel",
                autoboto.TypeInfo(int),
            ),
            (
                "number_of_disks",
                "NumberOfDisks",
                autoboto.TypeInfo(int),
            ),
            (
                "size",
                "Size",
                autoboto.TypeInfo(int),
            ),
            (
                "device",
                "Device",
                autoboto.TypeInfo(str),
            ),
            (
                "mount_point",
                "MountPoint",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "volume_type",
                "VolumeType",
                autoboto.TypeInfo(str),
            ),
            (
                "iops",
                "Iops",
                autoboto.TypeInfo(int),
            ),
        ]

    # The array ID.
    raid_array_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The array name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The [RAID level](http://en.wikipedia.org/wiki/Standard_RAID_levels).
    raid_level: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of disks in the array.
    number_of_disks: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The array's size.
    size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The array's Linux device. For example /dev/mdadm0.
    device: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The array's mount point.
    mount_point: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The array's Availability Zone. For more information, see [Regions and
    # Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html).
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When the RAID array was created.
    created_at: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The volume type, standard or PIOPS.
    volume_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # For PIOPS volumes, the IOPS per disk.
    iops: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RdsDbInstance(autoboto.ShapeBase):
    """
    Describes an Amazon RDS instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rds_db_instance_arn",
                "RdsDbInstanceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "db_instance_identifier",
                "DbInstanceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "db_user",
                "DbUser",
                autoboto.TypeInfo(str),
            ),
            (
                "db_password",
                "DbPassword",
                autoboto.TypeInfo(str),
            ),
            (
                "region",
                "Region",
                autoboto.TypeInfo(str),
            ),
            (
                "address",
                "Address",
                autoboto.TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "missing_on_rds",
                "MissingOnRds",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The instance's ARN.
    rds_db_instance_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The DB instance identifier.
    db_instance_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The master user name.
    db_user: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # AWS OpsWorks Stacks returns `*****FILTERED*****` instead of the actual
    # value.
    db_password: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's AWS region.
    region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's address.
    address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's database engine.
    engine: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the stack with which the instance is registered.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Set to `true` if AWS OpsWorks Stacks is unable to discover the Amazon RDS
    # instance. AWS OpsWorks Stacks attempts to discover the instance only once.
    # If this value is set to `true`, you must deregister the instance, and then
    # register it again.
    missing_on_rds: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RebootInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Recipes(autoboto.ShapeBase):
    """
    AWS OpsWorks Stacks supports five lifecycle events: **setup** ,
    **configuration** , **deploy** , **undeploy** , and **shutdown**. For each
    layer, AWS OpsWorks Stacks runs a set of standard recipes for each event. In
    addition, you can provide custom recipes for any or all layers and events. AWS
    OpsWorks Stacks runs custom event recipes after the standard recipes.
    `LayerCustomRecipes` specifies the custom recipes for a particular layer to be
    run in response to each of the five events.

    To specify a recipe, use the cookbook's directory name in the repository
    followed by two colons and the recipe name, which is the recipe's file name
    without the .rb extension. For example: phpapp2::dbsetup specifies the
    dbsetup.rb recipe in the repository's phpapp2 folder.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "setup",
                "Setup",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "configure",
                "Configure",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "deploy",
                "Deploy",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "undeploy",
                "Undeploy",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "shutdown",
                "Shutdown",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # An array of custom recipe names to be run following a `setup` event.
    setup: typing.List[str] = dataclasses.field(default_factory=list, )

    # An array of custom recipe names to be run following a `configure` event.
    configure: typing.List[str] = dataclasses.field(default_factory=list, )

    # An array of custom recipe names to be run following a `deploy` event.
    deploy: typing.List[str] = dataclasses.field(default_factory=list, )

    # An array of custom recipe names to be run following a `undeploy` event.
    undeploy: typing.List[str] = dataclasses.field(default_factory=list, )

    # An array of custom recipe names to be run following a `shutdown` event.
    shutdown: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class RegisterEcsClusterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ecs_cluster_arn",
                "EcsClusterArn",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The cluster's ARN.
    ecs_cluster_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterEcsClusterResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `RegisterEcsCluster` request.
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
                "ecs_cluster_arn",
                "EcsClusterArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The cluster's ARN.
    ecs_cluster_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RegisterElasticIpRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "elastic_ip",
                "ElasticIp",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Elastic IP address.
    elastic_ip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterElasticIpResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `RegisterElasticIp` request.
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
                "elastic_ip",
                "ElasticIp",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Elastic IP address.
    elastic_ip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "hostname",
                "Hostname",
                autoboto.TypeInfo(str),
            ),
            (
                "public_ip",
                "PublicIp",
                autoboto.TypeInfo(str),
            ),
            (
                "private_ip",
                "PrivateIp",
                autoboto.TypeInfo(str),
            ),
            (
                "rsa_public_key",
                "RsaPublicKey",
                autoboto.TypeInfo(str),
            ),
            (
                "rsa_public_key_fingerprint",
                "RsaPublicKeyFingerprint",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_identity",
                "InstanceIdentity",
                autoboto.TypeInfo(InstanceIdentity),
            ),
        ]

    # The ID of the stack that the instance is to be registered with.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's hostname.
    hostname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's public IP address.
    public_ip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's private IP address.
    private_ip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instances public RSA key. This key is used to encrypt communication
    # between the instance and the service.
    rsa_public_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instances public RSA key fingerprint.
    rsa_public_key_fingerprint: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An InstanceIdentity object that contains the instance's identity.
    instance_identity: "InstanceIdentity" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class RegisterInstanceResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `RegisterInstanceResult` request.
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
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The registered instance's AWS OpsWorks Stacks ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterRdsDbInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "rds_db_instance_arn",
                "RdsDbInstanceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "db_user",
                "DbUser",
                autoboto.TypeInfo(str),
            ),
            (
                "db_password",
                "DbPassword",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon RDS instance's ARN.
    rds_db_instance_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The database's master user name.
    db_user: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The database password.
    db_password: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterVolumeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "ec2_volume_id",
                "Ec2VolumeId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon EBS volume ID.
    ec2_volume_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterVolumeResult(autoboto.OutputShapeBase):
    """
    Contains the response to a `RegisterVolume` request.
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
                "volume_id",
                "VolumeId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The volume ID.
    volume_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReportedOs(autoboto.ShapeBase):
    """
    A registered instance's reported operating system.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "family",
                "Family",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The operating system family.
    family: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The operating system name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The operating system version.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    Indicates that a resource was not found.
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

    # The exception message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class RootDeviceType(Enum):
    ebs = "ebs"
    instance_store = "instance-store"


@dataclasses.dataclass
class SelfUserProfile(autoboto.ShapeBase):
    """
    Describes a user's SSH information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "iam_user_arn",
                "IamUserArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_username",
                "SshUsername",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "SshPublicKey",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user's IAM ARN.
    iam_user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user's name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user's SSH user name.
    ssh_username: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user's SSH public key.
    ssh_public_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServiceError(autoboto.ShapeBase):
    """
    Describes an AWS OpsWorks Stacks service error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_error_id",
                "ServiceErrorId",
                autoboto.TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error ID.
    service_error_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The error type.
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A message that describes the error.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When the error occurred.
    created_at: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetLoadBasedAutoScalingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "layer_id",
                "LayerId",
                autoboto.TypeInfo(str),
            ),
            (
                "enable",
                "Enable",
                autoboto.TypeInfo(bool),
            ),
            (
                "up_scaling",
                "UpScaling",
                autoboto.TypeInfo(AutoScalingThresholds),
            ),
            (
                "down_scaling",
                "DownScaling",
                autoboto.TypeInfo(AutoScalingThresholds),
            ),
        ]

    # The layer ID.
    layer_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Enables load-based auto scaling for the layer.
    enable: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An `AutoScalingThresholds` object with the upscaling threshold
    # configuration. If the load exceeds these thresholds for a specified amount
    # of time, AWS OpsWorks Stacks starts a specified number of instances.
    up_scaling: "AutoScalingThresholds" = dataclasses.field(
        default_factory=dict,
    )

    # An `AutoScalingThresholds` object with the downscaling threshold
    # configuration. If the load falls below these thresholds for a specified
    # amount of time, AWS OpsWorks Stacks stops a specified number of instances.
    down_scaling: "AutoScalingThresholds" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SetPermissionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "iam_user_arn",
                "IamUserArn",
                autoboto.TypeInfo(str),
            ),
            (
                "allow_ssh",
                "AllowSsh",
                autoboto.TypeInfo(bool),
            ),
            (
                "allow_sudo",
                "AllowSudo",
                autoboto.TypeInfo(bool),
            ),
            (
                "level",
                "Level",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user's IAM ARN. This can also be a federated user's ARN.
    iam_user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user is allowed to use SSH to communicate with the instance.
    allow_ssh: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user is allowed to use **sudo** to elevate privileges.
    allow_sudo: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user's permission level, which must be set to one of the following
    # strings. You cannot set your own permissions level.

    #   * `deny`

    #   * `show`

    #   * `deploy`

    #   * `manage`

    #   * `iam_only`

    # For more information about the permissions associated with these levels,
    # see [Managing User
    # Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
    # security-users.html).
    level: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetTimeBasedAutoScalingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "auto_scaling_schedule",
                "AutoScalingSchedule",
                autoboto.TypeInfo(WeeklyAutoScalingSchedule),
            ),
        ]

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An `AutoScalingSchedule` with the instance schedule.
    auto_scaling_schedule: "WeeklyAutoScalingSchedule" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ShutdownEventConfiguration(autoboto.ShapeBase):
    """
    The Shutdown event configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution_timeout",
                "ExecutionTimeout",
                autoboto.TypeInfo(int),
            ),
            (
                "delay_until_elb_connections_drained",
                "DelayUntilElbConnectionsDrained",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a
    # Shutdown event before shutting down an instance.
    execution_timeout: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether to enable Elastic Load Balancing connection draining. For more
    # information, see [Connection
    # Draining](http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-
    # drain)
    delay_until_elb_connections_drained: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Source(autoboto.ShapeBase):
    """
    Contains the information required to retrieve an app or cookbook from a
    repository. For more information, see [Creating
    Apps](http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-
    creating.html) or [Custom Recipes and
    Cookbooks](http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(SourceType),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
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
            (
                "ssh_key",
                "SshKey",
                autoboto.TypeInfo(str),
            ),
            (
                "revision",
                "Revision",
                autoboto.TypeInfo(str),
            ),
        ]

    # The repository type.
    type: "SourceType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The source URL. The following is an example of an Amazon S3 source URL:
    # `https://s3.amazonaws.com/opsworks-demo-
    # bucket/opsworks_cookbook_demo.tar.gz`.
    url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This parameter depends on the repository type.

    #   * For Amazon S3 bundles, set `Username` to the appropriate IAM access key ID.

    #   * For HTTP bundles, Git repositories, and Subversion repositories, set `Username` to the user name.
    username: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When included in a request, the parameter depends on the repository type.

    #   * For Amazon S3 bundles, set `Password` to the appropriate IAM secret access key.

    #   * For HTTP bundles and Subversion repositories, set `Password` to the password.

    # For more information on how to safely handle IAM credentials, see
    # <http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-
    # practices.html>.

    # In responses, AWS OpsWorks Stacks returns `*****FILTERED*****` instead of
    # the actual value.
    password: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # In requests, the repository's SSH key.

    # In responses, AWS OpsWorks Stacks returns `*****FILTERED*****` instead of
    # the actual value.
    ssh_key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The application's version. AWS OpsWorks Stacks enables you to easily deploy
    # new versions of an application. One of the simplest approaches is to have
    # branches or revisions in your repository that represent different versions
    # that can potentially be deployed.
    revision: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class SourceType(Enum):
    git = "git"
    svn = "svn"
    archive = "archive"
    s3 = "s3"


@dataclasses.dataclass
class SslConfiguration(autoboto.ShapeBase):
    """
    Describes an app's SSL configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate",
                "Certificate",
                autoboto.TypeInfo(str),
            ),
            (
                "private_key",
                "PrivateKey",
                autoboto.TypeInfo(str),
            ),
            (
                "chain",
                "Chain",
                autoboto.TypeInfo(str),
            ),
        ]

    # The contents of the certificate's domain.crt file.
    certificate: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The private key; the contents of the certificate's domain.kex file.
    private_key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Optional. Can be used to specify an intermediate certificate authority key
    # or client authentication.
    chain: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Stack(autoboto.ShapeBase):
    """
    Describes a stack.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "region",
                "Region",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[StackAttributesKeys, str]),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "default_instance_profile_arn",
                "DefaultInstanceProfileArn",
                autoboto.TypeInfo(str),
            ),
            (
                "default_os",
                "DefaultOs",
                autoboto.TypeInfo(str),
            ),
            (
                "hostname_theme",
                "HostnameTheme",
                autoboto.TypeInfo(str),
            ),
            (
                "default_availability_zone",
                "DefaultAvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "default_subnet_id",
                "DefaultSubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_json",
                "CustomJson",
                autoboto.TypeInfo(str),
            ),
            (
                "configuration_manager",
                "ConfigurationManager",
                autoboto.TypeInfo(StackConfigurationManager),
            ),
            (
                "chef_configuration",
                "ChefConfiguration",
                autoboto.TypeInfo(ChefConfiguration),
            ),
            (
                "use_custom_cookbooks",
                "UseCustomCookbooks",
                autoboto.TypeInfo(bool),
            ),
            (
                "use_opsworks_security_groups",
                "UseOpsworksSecurityGroups",
                autoboto.TypeInfo(bool),
            ),
            (
                "custom_cookbooks_source",
                "CustomCookbooksSource",
                autoboto.TypeInfo(Source),
            ),
            (
                "default_ssh_key_name",
                "DefaultSshKeyName",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "default_root_device_type",
                "DefaultRootDeviceType",
                autoboto.TypeInfo(RootDeviceType),
            ),
            (
                "agent_version",
                "AgentVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack's ARN.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack AWS region, such as "ap-northeast-2". For more information about
    # AWS regions, see [Regions and
    # Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html).
    region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The VPC ID; applicable only if the stack is running in a VPC.
    vpc_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack's attributes.
    attributes: typing.Dict["StackAttributesKeys", str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stack AWS Identity and Access Management (IAM) role.
    service_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of an IAM profile that is the default profile for all of the
    # stack's EC2 instances. For more information about IAM ARNs, see [Using
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html).
    default_instance_profile_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stack's default operating system.
    default_os: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack host name theme, with spaces replaced by underscores.
    hostname_theme: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stack's default Availability Zone. For more information, see [Regions
    # and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html).
    default_availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The default subnet ID; applicable only if the stack is running in a VPC.
    default_subnet_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A JSON object that contains user-defined attributes to be added to the
    # stack configuration and deployment attributes. You can use custom JSON to
    # override the corresponding default stack configuration attribute values or
    # to pass data to recipes. The string should be in the following format:

    # `"{\"key1\": \"value1\", \"key2\": \"value2\",...}"`

    # For more information on custom JSON, see [Use Custom JSON to Modify the
    # Stack Configuration
    # Attributes](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
    # json.html).
    custom_json: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The configuration manager.
    configuration_manager: "StackConfigurationManager" = dataclasses.field(
        default_factory=dict,
    )

    # A `ChefConfiguration` object that specifies whether to enable Berkshelf and
    # the Berkshelf version. For more information, see [Create a New
    # Stack](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
    # creating.html).
    chef_configuration: "ChefConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # Whether the stack uses custom cookbooks.
    use_custom_cookbooks: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether the stack automatically associates the AWS OpsWorks Stacks built-in
    # security groups with the stack's layers.
    use_opsworks_security_groups: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains the information required to retrieve an app or cookbook from a
    # repository. For more information, see [Creating
    # Apps](http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-
    # creating.html) or [Custom Recipes and
    # Cookbooks](http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html).
    custom_cookbooks_source: "Source" = dataclasses.field(
        default_factory=dict,
    )

    # A default Amazon EC2 key pair for the stack's instances. You can override
    # this value when you create or update an instance.
    default_ssh_key_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date when the stack was created.
    created_at: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The default root device type. This value is used by default for all
    # instances in the stack, but you can override it when you create an
    # instance. For more information, see [Storage for the Root
    # Device](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-
    # for-the-root-device).
    default_root_device_type: "RootDeviceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The agent version. This parameter is set to `LATEST` for auto-update. or a
    # version number for a fixed agent version.
    agent_version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class StackAttributesKeys(Enum):
    Color = "Color"


@dataclasses.dataclass
class StackConfigurationManager(autoboto.ShapeBase):
    """
    Describes the configuration manager.
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
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name. This parameter must be set to "Chef".
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Chef version. This parameter must be set to 12, 11.10, or 11.4 for
    # Linux stacks, and to 12.2 for Windows stacks. The default value for Linux
    # stacks is 11.4.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StackSummary(autoboto.ShapeBase):
    """
    Summarizes the number of layers, instances, and apps in a stack.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "layers_count",
                "LayersCount",
                autoboto.TypeInfo(int),
            ),
            (
                "apps_count",
                "AppsCount",
                autoboto.TypeInfo(int),
            ),
            (
                "instances_count",
                "InstancesCount",
                autoboto.TypeInfo(InstancesCount),
            ),
        ]

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack's ARN.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of layers.
    layers_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of apps.
    apps_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An `InstancesCount` object with the number of instances in each status.
    instances_count: "InstancesCount" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class StartInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartStackRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "force",
                "Force",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies whether to force an instance to stop.
    force: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopStackRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagResourceRequest(autoboto.ShapeBase):
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
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The stack or layer's Amazon Resource Number (ARN).
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A map that contains tag keys and tag values that are attached to a stack or
    # layer.

    #   * The key cannot be empty.

    #   * The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /`

    #   * The value can be a maximum 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /`

    #   * Leading and trailing white spaces are trimmed from both the key and value.

    #   * A maximum of 40 tags is allowed for any resource.
    tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TemporaryCredential(autoboto.ShapeBase):
    """
    Contains the data needed by RDP clients such as the Microsoft Remote Desktop
    Connection to log in to the instance.
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
            (
                "valid_for_in_minutes",
                "ValidForInMinutes",
                autoboto.TypeInfo(int),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user name.
    username: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The password.
    password: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The length of time (in minutes) that the grant is valid. When the grant
    # expires, at the end of this period, the user will no longer be able to use
    # the credentials to log in. If they are logged in at the time, they will be
    # automatically logged out.
    valid_for_in_minutes: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance's AWS OpsWorks Stacks ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TimeBasedAutoScalingConfiguration(autoboto.ShapeBase):
    """
    Describes an instance's time-based auto scaling configuration.
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
                "auto_scaling_schedule",
                "AutoScalingSchedule",
                autoboto.TypeInfo(WeeklyAutoScalingSchedule),
            ),
        ]

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A `WeeklyAutoScalingSchedule` object with the instance schedule.
    auto_scaling_schedule: "WeeklyAutoScalingSchedule" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UnassignInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnassignVolumeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_id",
                "VolumeId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The volume ID.
    volume_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UntagResourceRequest(autoboto.ShapeBase):
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

    # The stack or layer's Amazon Resource Number (ARN).
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of the keys of tags to be removed from a stack or layer.
    tag_keys: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UpdateAppRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "app_id",
                "AppId",
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
                "data_sources",
                "DataSources",
                autoboto.TypeInfo(typing.List[DataSource]),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(AppType),
            ),
            (
                "app_source",
                "AppSource",
                autoboto.TypeInfo(Source),
            ),
            (
                "domains",
                "Domains",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "enable_ssl",
                "EnableSsl",
                autoboto.TypeInfo(bool),
            ),
            (
                "ssl_configuration",
                "SslConfiguration",
                autoboto.TypeInfo(SslConfiguration),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[AppAttributesKeys, str]),
            ),
            (
                "environment",
                "Environment",
                autoboto.TypeInfo(typing.List[EnvironmentVariable]),
            ),
        ]

    # The app ID.
    app_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The app name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A description of the app.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The app's data sources.
    data_sources: typing.List["DataSource"] = dataclasses.field(
        default_factory=list,
    )

    # The app type.
    type: "AppType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A `Source` object that specifies the app repository.
    app_source: "Source" = dataclasses.field(default_factory=dict, )

    # The app's virtual host settings, with multiple domains separated by commas.
    # For example: `'www.example.com, example.com'`
    domains: typing.List[str] = dataclasses.field(default_factory=list, )

    # Whether SSL is enabled for the app.
    enable_ssl: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An `SslConfiguration` object with the SSL configuration.
    ssl_configuration: "SslConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # One or more user-defined key/value pairs to be added to the stack
    # attributes.
    attributes: typing.Dict["AppAttributesKeys", str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of `EnvironmentVariable` objects that specify environment
    # variables to be associated with the app. After you deploy the app, these
    # variables are defined on the associated app server instances.For more
    # information, see [ Environment
    # Variables](http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-
    # creating.html#workingapps-creating-environment).

    # There is no specific limit on the number of environment variables. However,
    # the size of the associated data structure - which includes the variables'
    # names, values, and protected flag values - cannot exceed 10 KB (10240
    # Bytes). This limit should accommodate most if not all use cases. Exceeding
    # it will cause an exception with the message, "Environment: is too large
    # (maximum is 10KB)."

    # This parameter is supported only by Chef 11.10 stacks. If you have
    # specified one or more environment variables, you cannot modify the stack's
    # Chef version.
    environment: typing.List["EnvironmentVariable"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateElasticIpRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "elastic_ip",
                "ElasticIp",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The IP address for which you want to update the name.
    elastic_ip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The new name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "layer_ids",
                "LayerIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "instance_type",
                "InstanceType",
                autoboto.TypeInfo(str),
            ),
            (
                "auto_scaling_type",
                "AutoScalingType",
                autoboto.TypeInfo(AutoScalingType),
            ),
            (
                "hostname",
                "Hostname",
                autoboto.TypeInfo(str),
            ),
            (
                "os",
                "Os",
                autoboto.TypeInfo(str),
            ),
            (
                "ami_id",
                "AmiId",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_key_name",
                "SshKeyName",
                autoboto.TypeInfo(str),
            ),
            (
                "architecture",
                "Architecture",
                autoboto.TypeInfo(Architecture),
            ),
            (
                "install_updates_on_boot",
                "InstallUpdatesOnBoot",
                autoboto.TypeInfo(bool),
            ),
            (
                "ebs_optimized",
                "EbsOptimized",
                autoboto.TypeInfo(bool),
            ),
            (
                "agent_version",
                "AgentVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's layer IDs.
    layer_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The instance type, such as `t2.micro`. For a list of supported instance
    # types, open the stack in the console, choose **Instances** , and choose
    # **\+ Instance**. The **Size** list contains the currently supported types.
    # For more information, see [Instance Families and
    # Types](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-
    # types.html). The parameter values that you use to specify the various types
    # are in the **API Name** column of the **Available Instance Types** table.
    instance_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # For load-based or time-based instances, the type. Windows stacks can use
    # only time-based instances.
    auto_scaling_type: "AutoScalingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance host name.
    hostname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's operating system, which must be set to one of the following.
    # You cannot update an instance that is using a custom AMI.

    #   * A supported Linux operating system: An Amazon Linux version, such as `Amazon Linux 2017.09`, `Amazon Linux 2017.03`, `Amazon Linux 2016.09`, `Amazon Linux 2016.03`, `Amazon Linux 2015.09`, or `Amazon Linux 2015.03`.

    #   * A supported Ubuntu operating system, such as `Ubuntu 16.04 LTS`, `Ubuntu 14.04 LTS`, or `Ubuntu 12.04 LTS`.

    #   * `CentOS Linux 7`

    #   * `Red Hat Enterprise Linux 7`

    #   * A supported Windows operating system, such as `Microsoft Windows Server 2012 R2 Base`, `Microsoft Windows Server 2012 R2 with SQL Server Express`, `Microsoft Windows Server 2012 R2 with SQL Server Standard`, or `Microsoft Windows Server 2012 R2 with SQL Server Web`.

    # For more information about supported operating systems, see [AWS OpsWorks
    # Stacks Operating
    # Systems](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # os.html).

    # The default option is the current Amazon Linux version. If you set this
    # parameter to `Custom`, you must use the AmiId parameter to specify the
    # custom AMI that you want to use. For more information about supported
    # operating systems, see [Operating
    # Systems](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # os.html). For more information about how to use custom AMIs with OpsWorks,
    # see [Using Custom
    # AMIs](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # custom-ami.html).

    # You can specify a different Linux operating system for the updated stack,
    # but you cannot change from Linux to Windows or Windows to Linux.
    os: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the AMI that was used to create the instance. The value of this
    # parameter must be the same AMI ID that the instance is already using. You
    # cannot apply a new AMI to an instance by running UpdateInstance.
    # UpdateInstance does not work on instances that are using custom AMIs.
    ami_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance's Amazon EC2 key name.
    ssh_key_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance architecture. Instance types do not necessarily support both
    # architectures. For a list of the architectures that are supported by the
    # different instance types, see [Instance Families and
    # Types](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-
    # types.html).
    architecture: "Architecture" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether to install operating system and package updates when the instance
    # boots. The default value is `true`. To control when updates are installed,
    # set this value to `false`. You must then update your instances manually by
    # using CreateDeployment to run the `update_dependencies` stack command or by
    # manually running `yum` (Amazon Linux) or `apt-get` (Ubuntu) on the
    # instances.

    # We strongly recommend using the default value of `true`, to ensure that
    # your instances have the latest security updates.
    install_updates_on_boot: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This property cannot be updated.
    ebs_optimized: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The default AWS OpsWorks Stacks agent version. You have the following
    # options:

    #   * `INHERIT` \- Use the stack's default agent version setting.

    #   * _version_number_ \- Use the specified agent version. This value overrides the stack's default setting. To update the agent version, you must edit the instance configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the instance.

    # The default setting is `INHERIT`. To specify an agent version, you must use
    # the complete version number, not the abbreviated number shown on the
    # console. For a list of available agent version numbers, call
    # DescribeAgentVersions.

    # AgentVersion cannot be set to Chef 12.2.
    agent_version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateLayerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "layer_id",
                "LayerId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "shortname",
                "Shortname",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[LayerAttributesKeys, str]),
            ),
            (
                "cloud_watch_logs_configuration",
                "CloudWatchLogsConfiguration",
                autoboto.TypeInfo(CloudWatchLogsConfiguration),
            ),
            (
                "custom_instance_profile_arn",
                "CustomInstanceProfileArn",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_json",
                "CustomJson",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_security_group_ids",
                "CustomSecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "packages",
                "Packages",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "volume_configurations",
                "VolumeConfigurations",
                autoboto.TypeInfo(typing.List[VolumeConfiguration]),
            ),
            (
                "enable_auto_healing",
                "EnableAutoHealing",
                autoboto.TypeInfo(bool),
            ),
            (
                "auto_assign_elastic_ips",
                "AutoAssignElasticIps",
                autoboto.TypeInfo(bool),
            ),
            (
                "auto_assign_public_ips",
                "AutoAssignPublicIps",
                autoboto.TypeInfo(bool),
            ),
            (
                "custom_recipes",
                "CustomRecipes",
                autoboto.TypeInfo(Recipes),
            ),
            (
                "install_updates_on_boot",
                "InstallUpdatesOnBoot",
                autoboto.TypeInfo(bool),
            ),
            (
                "use_ebs_optimized_instances",
                "UseEbsOptimizedInstances",
                autoboto.TypeInfo(bool),
            ),
            (
                "lifecycle_event_configuration",
                "LifecycleEventConfiguration",
                autoboto.TypeInfo(LifecycleEventConfiguration),
            ),
        ]

    # The layer ID.
    layer_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The layer name, which is used by the console.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # For custom layers only, use this parameter to specify the layer's short
    # name, which is used internally by AWS OpsWorks Stacks and by Chef. The
    # short name is also used as the name for the directory where your app files
    # are installed. It can have a maximum of 200 characters and must be in the
    # following format: /\A[a-z0-9\\-\\_\\.]+\Z/.

    # The built-in layers' short names are defined by AWS OpsWorks Stacks. For
    # more information, see the [Layer
    # Reference](http://docs.aws.amazon.com/opsworks/latest/userguide/layers.html)
    shortname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more user-defined key/value pairs to be added to the stack
    # attributes.
    attributes: typing.Dict["LayerAttributesKeys", str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies CloudWatch Logs configuration options for the layer. For more
    # information, see CloudWatchLogsLogStream.
    cloud_watch_logs_configuration: "CloudWatchLogsConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The ARN of an IAM profile to be used for all of the layer's EC2 instances.
    # For more information about IAM ARNs, see [Using
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html).
    custom_instance_profile_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A JSON-formatted string containing custom stack configuration and
    # deployment attributes to be installed on the layer's instances. For more
    # information, see [ Using Custom
    # JSON](http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-
    # json-override.html).
    custom_json: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array containing the layer's custom security group IDs.
    custom_security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # An array of `Package` objects that describe the layer's packages.
    packages: typing.List[str] = dataclasses.field(default_factory=list, )

    # A `VolumeConfigurations` object that describes the layer's Amazon EBS
    # volumes.
    volume_configurations: typing.List["VolumeConfiguration"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )

    # Whether to disable auto healing for the layer.
    enable_auto_healing: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether to automatically assign an [Elastic IP
    # address](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-
    # addresses-eip.html) to the layer's instances. For more information, see
    # [How to Edit a
    # Layer](http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-
    # basics-edit.html).
    auto_assign_elastic_ips: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # For stacks that are running in a VPC, whether to automatically assign a
    # public IP address to the layer's instances. For more information, see [How
    # to Edit a
    # Layer](http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-
    # basics-edit.html).
    auto_assign_public_ips: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A `LayerCustomRecipes` object that specifies the layer's custom recipes.
    custom_recipes: "Recipes" = dataclasses.field(default_factory=dict, )

    # Whether to install operating system and package updates when the instance
    # boots. The default value is `true`. To control when updates are installed,
    # set this value to `false`. You must then update your instances manually by
    # using CreateDeployment to run the `update_dependencies` stack command or
    # manually running `yum` (Amazon Linux) or `apt-get` (Ubuntu) on the
    # instances.

    # We strongly recommend using the default value of `true`, to ensure that
    # your instances have the latest security updates.
    install_updates_on_boot: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether to use Amazon EBS-optimized instances.
    use_ebs_optimized_instances: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    lifecycle_event_configuration: "LifecycleEventConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateMyUserProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ssh_public_key",
                "SshPublicKey",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user's SSH public key.
    ssh_public_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateRdsDbInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rds_db_instance_arn",
                "RdsDbInstanceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "db_user",
                "DbUser",
                autoboto.TypeInfo(str),
            ),
            (
                "db_password",
                "DbPassword",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon RDS instance's ARN.
    rds_db_instance_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The master user name.
    db_user: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The database password.
    db_password: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateStackRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_id",
                "StackId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.Dict[StackAttributesKeys, str]),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "default_instance_profile_arn",
                "DefaultInstanceProfileArn",
                autoboto.TypeInfo(str),
            ),
            (
                "default_os",
                "DefaultOs",
                autoboto.TypeInfo(str),
            ),
            (
                "hostname_theme",
                "HostnameTheme",
                autoboto.TypeInfo(str),
            ),
            (
                "default_availability_zone",
                "DefaultAvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "default_subnet_id",
                "DefaultSubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_json",
                "CustomJson",
                autoboto.TypeInfo(str),
            ),
            (
                "configuration_manager",
                "ConfigurationManager",
                autoboto.TypeInfo(StackConfigurationManager),
            ),
            (
                "chef_configuration",
                "ChefConfiguration",
                autoboto.TypeInfo(ChefConfiguration),
            ),
            (
                "use_custom_cookbooks",
                "UseCustomCookbooks",
                autoboto.TypeInfo(bool),
            ),
            (
                "custom_cookbooks_source",
                "CustomCookbooksSource",
                autoboto.TypeInfo(Source),
            ),
            (
                "default_ssh_key_name",
                "DefaultSshKeyName",
                autoboto.TypeInfo(str),
            ),
            (
                "default_root_device_type",
                "DefaultRootDeviceType",
                autoboto.TypeInfo(RootDeviceType),
            ),
            (
                "use_opsworks_security_groups",
                "UseOpsworksSecurityGroups",
                autoboto.TypeInfo(bool),
            ),
            (
                "agent_version",
                "AgentVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The stack ID.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack's new name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more user-defined key-value pairs to be added to the stack
    # attributes.
    attributes: typing.Dict["StackAttributesKeys", str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Do not use this parameter. You cannot update a stack's service role.
    service_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN of an IAM profile that is the default profile for all of the
    # stack's EC2 instances. For more information about IAM ARNs, see [Using
    # Identifiers](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html).
    default_instance_profile_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stack's operating system, which must be set to one of the following:

    #   * A supported Linux operating system: An Amazon Linux version, such as `Amazon Linux 2017.09`, `Amazon Linux 2017.03`, `Amazon Linux 2016.09`, `Amazon Linux 2016.03`, `Amazon Linux 2015.09`, or `Amazon Linux 2015.03`.

    #   * A supported Ubuntu operating system, such as `Ubuntu 16.04 LTS`, `Ubuntu 14.04 LTS`, or `Ubuntu 12.04 LTS`.

    #   * `CentOS Linux 7`

    #   * `Red Hat Enterprise Linux 7`

    #   * A supported Windows operating system, such as `Microsoft Windows Server 2012 R2 Base`, `Microsoft Windows Server 2012 R2 with SQL Server Express`, `Microsoft Windows Server 2012 R2 with SQL Server Standard`, or `Microsoft Windows Server 2012 R2 with SQL Server Web`.

    #   * A custom AMI: `Custom`. You specify the custom AMI you want to use when you create instances. For more information about how to use custom AMIs with OpsWorks, see [Using Custom AMIs](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html).

    # The default option is the stack's current operating system. For more
    # information about supported operating systems, see [AWS OpsWorks Stacks
    # Operating
    # Systems](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # os.html).
    default_os: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The stack's new host name theme, with spaces replaced by underscores. The
    # theme is used to generate host names for the stack's instances. By default,
    # `HostnameTheme` is set to `Layer_Dependent`, which creates host names by
    # appending integers to the layer's short name. The other themes are:

    #   * `Baked_Goods`

    #   * `Clouds`

    #   * `Europe_Cities`

    #   * `Fruits`

    #   * `Greek_Deities`

    #   * `Legendary_creatures_from_Japan`

    #   * `Planets_and_Moons`

    #   * `Roman_Deities`

    #   * `Scottish_Islands`

    #   * `US_Cities`

    #   * `Wild_Cats`

    # To obtain a generated host name, call `GetHostNameSuggestion`, which
    # returns a host name based on the current theme.
    hostname_theme: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stack's default Availability Zone, which must be in the stack's region.
    # For more information, see [Regions and
    # Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html). If you
    # also specify a value for `DefaultSubnetId`, the subnet must be in the same
    # zone. For more information, see CreateStack.
    default_availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The stack's default VPC subnet ID. This parameter is required if you
    # specify a value for the `VpcId` parameter. All instances are launched into
    # this subnet unless you specify otherwise when you create the instance. If
    # you also specify a value for `DefaultAvailabilityZone`, the subnet must be
    # in that zone. For information on default values and when this parameter is
    # required, see the `VpcId` parameter description.
    default_subnet_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string that contains user-defined, custom JSON. It can be used to
    # override the corresponding default stack configuration JSON values or to
    # pass data to recipes. The string should be in the following format:

    # `"{\"key1\": \"value1\", \"key2\": \"value2\",...}"`

    # For more information about custom JSON, see [Use Custom JSON to Modify the
    # Stack Configuration
    # Attributes](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
    # json.html).
    custom_json: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The configuration manager. When you update a stack, we recommend that you
    # use the configuration manager to specify the Chef version: 12, 11.10, or
    # 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for
    # Linux stacks is currently 12.
    configuration_manager: "StackConfigurationManager" = dataclasses.field(
        default_factory=dict,
    )

    # A `ChefConfiguration` object that specifies whether to enable Berkshelf and
    # the Berkshelf version on Chef 11.10 stacks. For more information, see
    # [Create a New
    # Stack](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
    # creating.html).
    chef_configuration: "ChefConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # Whether the stack uses custom cookbooks.
    use_custom_cookbooks: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains the information required to retrieve an app or cookbook from a
    # repository. For more information, see [Creating
    # Apps](http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-
    # creating.html) or [Custom Recipes and
    # Cookbooks](http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html).
    custom_cookbooks_source: "Source" = dataclasses.field(
        default_factory=dict,
    )

    # A default Amazon EC2 key-pair name. The default value is `none`. If you
    # specify a key-pair name, AWS OpsWorks Stacks installs the public key on the
    # instance and you can use the private key with an SSH client to log in to
    # the instance. For more information, see [ Using SSH to Communicate with an
    # Instance](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # ssh.html) and [ Managing SSH
    # Access](http://docs.aws.amazon.com/opsworks/latest/userguide/security-ssh-
    # access.html). You can override this setting by specifying a different key
    # pair, or no key pair, when you [ create an
    # instance](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
    # add.html).
    default_ssh_key_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The default root device type. This value is used by default for all
    # instances in the stack, but you can override it when you create an
    # instance. For more information, see [Storage for the Root
    # Device](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-
    # for-the-root-device).
    default_root_device_type: "RootDeviceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether to associate the AWS OpsWorks Stacks built-in security groups with
    # the stack's layers.

    # AWS OpsWorks Stacks provides a standard set of built-in security groups,
    # one for each layer, which are associated with layers by default.
    # `UseOpsworksSecurityGroups` allows you to provide your own custom security
    # groups instead of using the built-in groups. `UseOpsworksSecurityGroups`
    # has the following settings:

    #   * True - AWS OpsWorks Stacks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it, but you cannot delete the built-in security group.

    #   * False - AWS OpsWorks Stacks does not associate built-in security groups with layers. You must create appropriate EC2 security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on. Custom security groups are required only for those layers that need custom settings.

    # For more information, see [Create a New
    # Stack](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
    # creating.html).
    use_opsworks_security_groups: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The default AWS OpsWorks Stacks agent version. You have the following
    # options:

    #   * Auto-update - Set this parameter to `LATEST`. AWS OpsWorks Stacks automatically installs new agent versions on the stack's instances as soon as they are available.

    #   * Fixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the stack's instances.

    # The default setting is `LATEST`. To specify an agent version, you must use
    # the complete version number, not the abbreviated number shown on the
    # console. For a list of available agent version numbers, call
    # DescribeAgentVersions. AgentVersion cannot be set to Chef 12.2.

    # You can also specify an agent version when you create or update an
    # instance, which overrides the stack's default setting.
    agent_version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateUserProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "iam_user_arn",
                "IamUserArn",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_username",
                "SshUsername",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "SshPublicKey",
                autoboto.TypeInfo(str),
            ),
            (
                "allow_self_management",
                "AllowSelfManagement",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The user IAM ARN. This can also be a federated user's ARN.
    iam_user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user's SSH user name. The allowable characters are [a-z], [A-Z], [0-9],
    # '-', and '_'. If the specified name includes other punctuation marks, AWS
    # OpsWorks Stacks removes them. For example, `my.name` will be changed to
    # `myname`. If you do not specify an SSH user name, AWS OpsWorks Stacks
    # generates one from the IAM user name.
    ssh_username: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user's new SSH public key.
    ssh_public_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether users can specify their own SSH public key through the My Settings
    # page. For more information, see [Managing User
    # Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/security-
    # settingsshkey.html).
    allow_self_management: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateVolumeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_id",
                "VolumeId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "mount_point",
                "MountPoint",
                autoboto.TypeInfo(str),
            ),
        ]

    # The volume ID.
    volume_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The new name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The new mount point.
    mount_point: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UserProfile(autoboto.ShapeBase):
    """
    Describes a user's SSH information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "iam_user_arn",
                "IamUserArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_username",
                "SshUsername",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "SshPublicKey",
                autoboto.TypeInfo(str),
            ),
            (
                "allow_self_management",
                "AllowSelfManagement",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The user's IAM ARN.
    iam_user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user's name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user's SSH user name.
    ssh_username: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user's SSH public key.
    ssh_public_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether users can specify their own SSH public key through the My Settings
    # page. For more information, see [Managing User
    # Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/security-
    # settingsshkey.html).
    allow_self_management: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ValidationException(autoboto.ShapeBase):
    """
    Indicates that a request was not valid.
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

    # The exception message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class VirtualizationType(Enum):
    paravirtual = "paravirtual"
    hvm = "hvm"


@dataclasses.dataclass
class Volume(autoboto.ShapeBase):
    """
    Describes an instance's Amazon EBS volume.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_id",
                "VolumeId",
                autoboto.TypeInfo(str),
            ),
            (
                "ec2_volume_id",
                "Ec2VolumeId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "raid_array_id",
                "RaidArrayId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
            (
                "size",
                "Size",
                autoboto.TypeInfo(int),
            ),
            (
                "device",
                "Device",
                autoboto.TypeInfo(str),
            ),
            (
                "mount_point",
                "MountPoint",
                autoboto.TypeInfo(str),
            ),
            (
                "region",
                "Region",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "volume_type",
                "VolumeType",
                autoboto.TypeInfo(str),
            ),
            (
                "iops",
                "Iops",
                autoboto.TypeInfo(int),
            ),
            (
                "encrypted",
                "Encrypted",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The volume ID.
    volume_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon EC2 volume ID.
    ec2_volume_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The volume name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The RAID array ID.
    raid_array_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance ID.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value returned by
    # [DescribeVolumes](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-
    # query-DescribeVolumes.html).
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The volume size.
    size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The device name.
    device: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The volume mount point. For example, "/mnt/disk1".
    mount_point: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The AWS region. For more information about AWS regions, see [Regions and
    # Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html).
    region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The volume Availability Zone. For more information, see [Regions and
    # Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html).
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The volume type. For more information, see [ Amazon EBS Volume
    # Types](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html).

    #   * `standard` \- Magnetic. Magnetic volumes must have a minimum size of 1 GiB and a maximum size of 1024 GiB.

    #   * `io1` \- Provisioned IOPS (SSD). PIOPS volumes must have a minimum size of 4 GiB and a maximum size of 16384 GiB.

    #   * `gp2` \- General Purpose (SSD). General purpose volumes must have a minimum size of 1 GiB and a maximum size of 16384 GiB.

    #   * `st1` \- Throughput Optimized hard disk drive (HDD). Throughput optimized HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.

    #   * `sc1` \- Cold HDD. Cold HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.
    volume_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # For PIOPS volumes, the IOPS per disk.
    iops: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies whether an Amazon EBS volume is encrypted. For more information,
    # see [Amazon EBS
    # Encryption](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html).
    encrypted: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VolumeConfiguration(autoboto.ShapeBase):
    """
    Describes an Amazon EBS volume configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "mount_point",
                "MountPoint",
                autoboto.TypeInfo(str),
            ),
            (
                "number_of_disks",
                "NumberOfDisks",
                autoboto.TypeInfo(int),
            ),
            (
                "size",
                "Size",
                autoboto.TypeInfo(int),
            ),
            (
                "raid_level",
                "RaidLevel",
                autoboto.TypeInfo(int),
            ),
            (
                "volume_type",
                "VolumeType",
                autoboto.TypeInfo(str),
            ),
            (
                "iops",
                "Iops",
                autoboto.TypeInfo(int),
            ),
            (
                "encrypted",
                "Encrypted",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The volume mount point. For example "/dev/sdh".
    mount_point: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of disks in the volume.
    number_of_disks: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The volume size.
    size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The volume [RAID level](http://en.wikipedia.org/wiki/Standard_RAID_levels).
    raid_level: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The volume type. For more information, see [ Amazon EBS Volume
    # Types](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html).

    #   * `standard` \- Magnetic. Magnetic volumes must have a minimum size of 1 GiB and a maximum size of 1024 GiB.

    #   * `io1` \- Provisioned IOPS (SSD). PIOPS volumes must have a minimum size of 4 GiB and a maximum size of 16384 GiB.

    #   * `gp2` \- General Purpose (SSD). General purpose volumes must have a minimum size of 1 GiB and a maximum size of 16384 GiB.

    #   * `st1` \- Throughput Optimized hard disk drive (HDD). Throughput optimized HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.

    #   * `sc1` \- Cold HDD. Cold HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.
    volume_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # For PIOPS volumes, the IOPS per disk.
    iops: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies whether an Amazon EBS volume is encrypted. For more information,
    # see [Amazon EBS
    # Encryption](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html).
    encrypted: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class VolumeType(Enum):
    gp2 = "gp2"
    io1 = "io1"
    standard = "standard"


@dataclasses.dataclass
class WeeklyAutoScalingSchedule(autoboto.ShapeBase):
    """
    Describes a time-based instance's auto scaling schedule. The schedule consists
    of a set of key-value pairs.

      * The key is the time period (a UTC hour) and must be an integer from 0 - 23.

      * The value indicates whether the instance should be online or offline for the specified period, and must be set to "on" or "off"

    The default setting for all time periods is off, so you use the following
    parameters primarily to specify the online periods. You don't have to explicitly
    specify offline periods unless you want to change an online period to an offline
    period.

    The following example specifies that the instance should be online for four
    hours, from UTC 1200 - 1600. It will be off for the remainder of the day.

    ` { "12":"on", "13":"on", "14":"on", "15":"on" } `
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "monday",
                "Monday",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tuesday",
                "Tuesday",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "wednesday",
                "Wednesday",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "thursday",
                "Thursday",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "friday",
                "Friday",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "saturday",
                "Saturday",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sunday",
                "Sunday",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The schedule for Monday.
    monday: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The schedule for Tuesday.
    tuesday: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The schedule for Wednesday.
    wednesday: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The schedule for Thursday.
    thursday: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The schedule for Friday.
    friday: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The schedule for Saturday.
    saturday: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The schedule for Sunday.
    sunday: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
