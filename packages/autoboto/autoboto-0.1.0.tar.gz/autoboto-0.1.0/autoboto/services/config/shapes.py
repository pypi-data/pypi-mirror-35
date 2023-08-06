import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AccountAggregationSource(autoboto.ShapeBase):
    """
    A collection of accounts and regions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_ids",
                "AccountIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "all_aws_regions",
                "AllAwsRegions",
                autoboto.TypeInfo(bool),
            ),
            (
                "aws_regions",
                "AwsRegions",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The 12-digit account ID of the account being aggregated.
    account_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # If true, aggregate existing AWS Config regions and future regions.
    all_aws_regions: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The source regions being aggregated.
    aws_regions: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class AggregateComplianceByConfigRule(autoboto.ShapeBase):
    """
    Indicates whether an AWS Config rule is compliant based on account ID, region,
    compliance, and rule name.

    A rule is compliant if all of the resources that the rule evaluated comply with
    it. It is noncompliant if any of these resources do not comply.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "config_rule_name",
                "ConfigRuleName",
                autoboto.TypeInfo(str),
            ),
            (
                "compliance",
                "Compliance",
                autoboto.TypeInfo(Compliance),
            ),
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_region",
                "AwsRegion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the AWS Config rule.
    config_rule_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether an AWS resource or AWS Config rule is compliant and
    # provides the number of contributors that affect the compliance.
    compliance: "Compliance" = dataclasses.field(default_factory=dict, )

    # The 12-digit account ID of the source account.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The source region from where the data is aggregated.
    aws_region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AggregateComplianceCount(autoboto.ShapeBase):
    """
    Returns the number of compliant and noncompliant rules for one or more accounts
    and regions in an aggregator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "compliance_summary",
                "ComplianceSummary",
                autoboto.TypeInfo(ComplianceSummary),
            ),
        ]

    # The 12-digit account ID or region based on the GroupByKey value.
    group_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of compliant and noncompliant AWS Config rules.
    compliance_summary: "ComplianceSummary" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class AggregateEvaluationResult(autoboto.ShapeBase):
    """
    The details of an AWS Config evaluation for an account ID and region in an
    aggregator. Provides the AWS resource that was evaluated, the compliance of the
    resource, related time stamps, and supplementary information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "evaluation_result_identifier",
                "EvaluationResultIdentifier",
                autoboto.TypeInfo(EvaluationResultIdentifier),
            ),
            (
                "compliance_type",
                "ComplianceType",
                autoboto.TypeInfo(ComplianceType),
            ),
            (
                "result_recorded_time",
                "ResultRecordedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "config_rule_invoked_time",
                "ConfigRuleInvokedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "annotation",
                "Annotation",
                autoboto.TypeInfo(str),
            ),
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_region",
                "AwsRegion",
                autoboto.TypeInfo(str),
            ),
        ]

    # Uniquely identifies the evaluation result.
    evaluation_result_identifier: "EvaluationResultIdentifier" = dataclasses.field(
        default_factory=dict,
    )

    # The resource compliance status.

    # For the `AggregationEvaluationResult` data type, AWS Config supports only
    # the `COMPLIANT` and `NON_COMPLIANT`. AWS Config does not support the
    # `NOT_APPLICABLE` and `INSUFFICIENT_DATA` value.
    compliance_type: "ComplianceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time when AWS Config recorded the aggregate evaluation result.
    result_recorded_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time when the AWS Config rule evaluated the AWS resource.
    config_rule_invoked_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Supplementary information about how the agrregate evaluation determined the
    # compliance.
    annotation: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The 12-digit account ID of the source account.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The source region from where the data is aggregated.
    aws_region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AggregatedSourceStatus(autoboto.ShapeBase):
    """
    The current sync status between the source and the aggregator account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_id",
                "SourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "source_type",
                "SourceType",
                autoboto.TypeInfo(AggregatedSourceType),
            ),
            (
                "aws_region",
                "AwsRegion",
                autoboto.TypeInfo(str),
            ),
            (
                "last_update_status",
                "LastUpdateStatus",
                autoboto.TypeInfo(AggregatedSourceStatusType),
            ),
            (
                "last_update_time",
                "LastUpdateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_error_code",
                "LastErrorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "last_error_message",
                "LastErrorMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The source account ID or an organization.
    source_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The source account or an organization.
    source_type: "AggregatedSourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The region authorized to collect aggregated data.
    aws_region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filters the last updated status type.

    #   * Valid value FAILED indicates errors while moving data.

    #   * Valid value SUCCEEDED indicates the data was successfully moved.

    #   * Valid value OUTDATED indicates the data is not the most recent.
    last_update_status: "AggregatedSourceStatusType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time of the last update.
    last_update_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The error code that AWS Config returned when the source account aggregation
    # last failed.
    last_error_code: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The message indicating that the source account aggregation failed due to an
    # error.
    last_error_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class AggregatedSourceStatusType(Enum):
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    OUTDATED = "OUTDATED"


class AggregatedSourceType(Enum):
    ACCOUNT = "ACCOUNT"
    ORGANIZATION = "ORGANIZATION"


@dataclasses.dataclass
class AggregationAuthorization(autoboto.ShapeBase):
    """
    An object that represents the authorizations granted to aggregator accounts and
    regions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "aggregation_authorization_arn",
                "AggregationAuthorizationArn",
                autoboto.TypeInfo(str),
            ),
            (
                "authorized_account_id",
                "AuthorizedAccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "authorized_aws_region",
                "AuthorizedAwsRegion",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Resource Name (ARN) of the aggregation object.
    aggregation_authorization_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The 12-digit account ID of the account authorized to aggregate data.
    authorized_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The region authorized to collect aggregated data.
    authorized_aws_region: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time stamp when the aggregation authorization was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BaseConfigurationItem(autoboto.ShapeBase):
    """
    The detailed configuration of a specified resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "version",
                "version",
                autoboto.TypeInfo(str),
            ),
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "configuration_item_capture_time",
                "configurationItemCaptureTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "configuration_item_status",
                "configurationItemStatus",
                autoboto.TypeInfo(ConfigurationItemStatus),
            ),
            (
                "configuration_state_id",
                "configurationStateId",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "resource_id",
                "resourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_name",
                "resourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_region",
                "awsRegion",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zone",
                "availabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_creation_time",
                "resourceCreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "configuration",
                "configuration",
                autoboto.TypeInfo(str),
            ),
            (
                "supplementary_configuration",
                "supplementaryConfiguration",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The version number of the resource configuration.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The 12 digit AWS account ID associated with the resource.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time when the configuration recording was initiated.
    configuration_item_capture_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The configuration item status.
    configuration_item_status: "ConfigurationItemStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An identifier that indicates the ordering of the configuration items of a
    # resource.
    configuration_state_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the resource.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of AWS resource.
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the resource (for example., sg-xxxxxx).
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The custom name of the resource, if available.
    resource_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The region where the resource resides.
    aws_region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Availability Zone associated with the resource.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time stamp when the resource was created.
    resource_creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description of the resource configuration.
    configuration: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Configuration attributes that AWS Config returns for certain resource types
    # to supplement the information returned for the configuration parameter.
    supplementary_configuration: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetResourceConfigRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_keys",
                "resourceKeys",
                autoboto.TypeInfo(typing.List[ResourceKey]),
            ),
        ]

    # A list of resource keys to be processed with the current request. Each
    # element in the list consists of the resource type and resource ID.
    resource_keys: typing.List["ResourceKey"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchGetResourceConfigResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "base_configuration_items",
                "baseConfigurationItems",
                autoboto.TypeInfo(typing.List[BaseConfigurationItem]),
            ),
            (
                "unprocessed_resource_keys",
                "unprocessedResourceKeys",
                autoboto.TypeInfo(typing.List[ResourceKey]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list that contains the current configuration of one or more resources.
    base_configuration_items: typing.List["BaseConfigurationItem"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )

    # A list of resource keys that were not processed with the current response.
    # The unprocessesResourceKeys value is in the same form as ResourceKeys, so
    # the value can be directly provided to a subsequent BatchGetResourceConfig
    # operation. If there are no unprocessed resource keys, the response contains
    # an empty unprocessedResourceKeys list.
    unprocessed_resource_keys: typing.List["ResourceKey"] = dataclasses.field(
        default_factory=list,
    )


class ChronologicalOrder(Enum):
    Reverse = "Reverse"
    Forward = "Forward"


@dataclasses.dataclass
class Compliance(autoboto.ShapeBase):
    """
    Indicates whether an AWS resource or AWS Config rule is compliant and provides
    the number of contributors that affect the compliance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compliance_type",
                "ComplianceType",
                autoboto.TypeInfo(ComplianceType),
            ),
            (
                "compliance_contributor_count",
                "ComplianceContributorCount",
                autoboto.TypeInfo(ComplianceContributorCount),
            ),
        ]

    # Indicates whether an AWS resource or AWS Config rule is compliant.

    # A resource is compliant if it complies with all of the AWS Config rules
    # that evaluate it. A resource is noncompliant if it does not comply with one
    # or more of these rules.

    # A rule is compliant if all of the resources that the rule evaluates comply
    # with it. A rule is noncompliant if any of these resources do not comply.

    # AWS Config returns the `INSUFFICIENT_DATA` value when no evaluation results
    # are available for the AWS resource or AWS Config rule.

    # For the `Compliance` data type, AWS Config supports only `COMPLIANT`,
    # `NON_COMPLIANT`, and `INSUFFICIENT_DATA` values. AWS Config does not
    # support the `NOT_APPLICABLE` value for the `Compliance` data type.
    compliance_type: "ComplianceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of AWS resources or AWS Config rules that cause a result of
    # `NON_COMPLIANT`, up to a maximum number.
    compliance_contributor_count: "ComplianceContributorCount" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ComplianceByConfigRule(autoboto.ShapeBase):
    """
    Indicates whether an AWS Config rule is compliant. A rule is compliant if all of
    the resources that the rule evaluated comply with it. A rule is noncompliant if
    any of these resources do not comply.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "config_rule_name",
                "ConfigRuleName",
                autoboto.TypeInfo(str),
            ),
            (
                "compliance",
                "Compliance",
                autoboto.TypeInfo(Compliance),
            ),
        ]

    # The name of the AWS Config rule.
    config_rule_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the AWS Config rule is compliant.
    compliance: "Compliance" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ComplianceByResource(autoboto.ShapeBase):
    """
    Indicates whether an AWS resource that is evaluated according to one or more AWS
    Config rules is compliant. A resource is compliant if it complies with all of
    the rules that evaluate it. A resource is noncompliant if it does not comply
    with one or more of these rules.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "compliance",
                "Compliance",
                autoboto.TypeInfo(Compliance),
            ),
        ]

    # The type of the AWS resource that was evaluated.
    resource_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the AWS resource that was evaluated.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether the AWS resource complies with all of the AWS Config
    # rules that evaluated it.
    compliance: "Compliance" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ComplianceContributorCount(autoboto.ShapeBase):
    """
    The number of AWS resources or AWS Config rules responsible for the current
    compliance of the item, up to a maximum number.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "capped_count",
                "CappedCount",
                autoboto.TypeInfo(int),
            ),
            (
                "cap_exceeded",
                "CapExceeded",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The number of AWS resources or AWS Config rules responsible for the current
    # compliance of the item.
    capped_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether the maximum count is reached.
    cap_exceeded: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ComplianceSummary(autoboto.ShapeBase):
    """
    The number of AWS Config rules or AWS resources that are compliant and
    noncompliant.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compliant_resource_count",
                "CompliantResourceCount",
                autoboto.TypeInfo(ComplianceContributorCount),
            ),
            (
                "non_compliant_resource_count",
                "NonCompliantResourceCount",
                autoboto.TypeInfo(ComplianceContributorCount),
            ),
            (
                "compliance_summary_timestamp",
                "ComplianceSummaryTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The number of AWS Config rules or AWS resources that are compliant, up to a
    # maximum of 25 for rules and 100 for resources.
    compliant_resource_count: "ComplianceContributorCount" = dataclasses.field(
        default_factory=dict,
    )

    # The number of AWS Config rules or AWS resources that are noncompliant, up
    # to a maximum of 25 for rules and 100 for resources.
    non_compliant_resource_count: "ComplianceContributorCount" = dataclasses.field(
        default_factory=dict,
    )

    # The time that AWS Config created the compliance summary.
    compliance_summary_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ComplianceSummaryByResourceType(autoboto.ShapeBase):
    """
    The number of AWS resources of a specific type that are compliant or
    noncompliant, up to a maximum of 100 for each.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "compliance_summary",
                "ComplianceSummary",
                autoboto.TypeInfo(ComplianceSummary),
            ),
        ]

    # The type of AWS resource.
    resource_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of AWS resources that are compliant or noncompliant, up to a
    # maximum of 100 for each.
    compliance_summary: "ComplianceSummary" = dataclasses.field(
        default_factory=dict,
    )


class ComplianceType(Enum):
    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON_COMPLIANT"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"


@dataclasses.dataclass
class ConfigExportDeliveryInfo(autoboto.ShapeBase):
    """
    Provides status of the delivery of the snapshot or the configuration history to
    the specified Amazon S3 bucket. Also provides the status of notifications about
    the Amazon S3 delivery to the specified Amazon SNS topic.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "last_status",
                "lastStatus",
                autoboto.TypeInfo(DeliveryStatus),
            ),
            (
                "last_error_code",
                "lastErrorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "last_error_message",
                "lastErrorMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "last_attempt_time",
                "lastAttemptTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_successful_time",
                "lastSuccessfulTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "next_delivery_time",
                "nextDeliveryTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # Status of the last attempted delivery.
    last_status: "DeliveryStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The error code from the last attempted delivery.
    last_error_code: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The error message from the last attempted delivery.
    last_error_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time of the last attempted delivery.
    last_attempt_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time of the last successful delivery.
    last_successful_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time that the next delivery occurs.
    next_delivery_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConfigRule(autoboto.ShapeBase):
    """
    An AWS Config rule represents an AWS Lambda function that you create for a
    custom rule or a predefined function for an AWS managed rule. The function
    evaluates configuration items to assess whether your AWS resources comply with
    your desired configurations. This function can run when AWS Config detects a
    configuration change to an AWS resource and at a periodic frequency that you
    choose (for example, every 24 hours).

    You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers
    evaluations for your resources when AWS Config delivers the configuration
    snapshot. For more information, see ConfigSnapshotDeliveryProperties.

    For more information about developing and using AWS Config rules, see
    [Evaluating AWS Resource Configurations with AWS
    Config](http://docs.aws.amazon.com/config/latest/developerguide/evaluate-
    config.html) in the _AWS Config Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source",
                "Source",
                autoboto.TypeInfo(Source),
            ),
            (
                "config_rule_name",
                "ConfigRuleName",
                autoboto.TypeInfo(str),
            ),
            (
                "config_rule_arn",
                "ConfigRuleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "config_rule_id",
                "ConfigRuleId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "scope",
                "Scope",
                autoboto.TypeInfo(Scope),
            ),
            (
                "input_parameters",
                "InputParameters",
                autoboto.TypeInfo(str),
            ),
            (
                "maximum_execution_frequency",
                "MaximumExecutionFrequency",
                autoboto.TypeInfo(MaximumExecutionFrequency),
            ),
            (
                "config_rule_state",
                "ConfigRuleState",
                autoboto.TypeInfo(ConfigRuleState),
            ),
        ]

    # Provides the rule owner (AWS or customer), the rule identifier, and the
    # notifications that cause the function to evaluate your AWS resources.
    source: "Source" = dataclasses.field(default_factory=dict, )

    # The name that you assign to the AWS Config rule. The name is required if
    # you are adding a new rule.
    config_rule_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the AWS Config rule.
    config_rule_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the AWS Config rule.
    config_rule_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description that you provide for the AWS Config rule.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Defines which resources can trigger an evaluation for the rule. The scope
    # can include one or more resource types, a combination of one resource type
    # and one resource ID, or a combination of a tag key and value. Specify a
    # scope to constrain the resources that can trigger an evaluation for the
    # rule. If you do not specify a scope, evaluations are triggered when any
    # resource in the recording group changes.
    scope: "Scope" = dataclasses.field(default_factory=dict, )

    # A string, in JSON format, that is passed to the AWS Config rule Lambda
    # function.
    input_parameters: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum frequency with which AWS Config runs evaluations for a rule.
    # You can specify a value for `MaximumExecutionFrequency` when:

    #   * You are using an AWS managed rule that is triggered at a periodic frequency.

    #   * Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see ConfigSnapshotDeliveryProperties.

    # By default, rules with a periodic trigger are evaluated every 24 hours. To
    # change the frequency, specify a valid value for the
    # `MaximumExecutionFrequency` parameter.
    maximum_execution_frequency: "MaximumExecutionFrequency" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the AWS Config rule is active or is currently being
    # deleted by AWS Config. It can also indicate the evaluation status for the
    # AWS Config rule.

    # AWS Config sets the state of the rule to `EVALUATING` temporarily after you
    # use the `StartConfigRulesEvaluation` request to evaluate your resources
    # against the AWS Config rule.

    # AWS Config sets the state of the rule to `DELETING_RESULTS` temporarily
    # after you use the `DeleteEvaluationResults` request to delete the current
    # evaluation results for the AWS Config rule.

    # AWS Config temporarily sets the state of a rule to `DELETING` after you use
    # the `DeleteConfigRule` request to delete the rule. After AWS Config deletes
    # the rule, the rule and all of its evaluations are erased and are no longer
    # available.
    config_rule_state: "ConfigRuleState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConfigRuleComplianceFilters(autoboto.ShapeBase):
    """
    Filters the compliance results based on account ID, region, compliance type, and
    rule name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "config_rule_name",
                "ConfigRuleName",
                autoboto.TypeInfo(str),
            ),
            (
                "compliance_type",
                "ComplianceType",
                autoboto.TypeInfo(ComplianceType),
            ),
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_region",
                "AwsRegion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the AWS Config rule.
    config_rule_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The rule compliance status.

    # For the `ConfigRuleComplianceFilters` data type, AWS Config supports only
    # `COMPLIANT` and `NON_COMPLIANT`. AWS Config does not support the
    # `NOT_APPLICABLE` and the `INSUFFICIENT_DATA` values.
    compliance_type: "ComplianceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The 12-digit account ID of the source account.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The source region where the data is aggregated.
    aws_region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConfigRuleComplianceSummaryFilters(autoboto.ShapeBase):
    """
    Filters the results based on the account IDs and regions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_region",
                "AwsRegion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The 12-digit account ID of the source account.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The source region where the data is aggregated.
    aws_region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ConfigRuleComplianceSummaryGroupKey(Enum):
    ACCOUNT_ID = "ACCOUNT_ID"
    AWS_REGION = "AWS_REGION"


@dataclasses.dataclass
class ConfigRuleEvaluationStatus(autoboto.ShapeBase):
    """
    Status information for your AWS managed Config rules. The status includes
    information such as the last time the rule ran, the last time it failed, and the
    related error for the last failure.

    This action does not return status information about custom AWS Config rules.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "config_rule_name",
                "ConfigRuleName",
                autoboto.TypeInfo(str),
            ),
            (
                "config_rule_arn",
                "ConfigRuleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "config_rule_id",
                "ConfigRuleId",
                autoboto.TypeInfo(str),
            ),
            (
                "last_successful_invocation_time",
                "LastSuccessfulInvocationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_failed_invocation_time",
                "LastFailedInvocationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_successful_evaluation_time",
                "LastSuccessfulEvaluationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_failed_evaluation_time",
                "LastFailedEvaluationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "first_activated_time",
                "FirstActivatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_error_code",
                "LastErrorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "last_error_message",
                "LastErrorMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "first_evaluation_started",
                "FirstEvaluationStarted",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the AWS Config rule.
    config_rule_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the AWS Config rule.
    config_rule_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the AWS Config rule.
    config_rule_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time that AWS Config last successfully invoked the AWS Config rule to
    # evaluate your AWS resources.
    last_successful_invocation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time that AWS Config last failed to invoke the AWS Config rule to
    # evaluate your AWS resources.
    last_failed_invocation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time that AWS Config last successfully evaluated your AWS resources
    # against the rule.
    last_successful_evaluation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time that AWS Config last failed to evaluate your AWS resources against
    # the rule.
    last_failed_evaluation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time that you first activated the AWS Config rule.
    first_activated_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The error code that AWS Config returned when the rule last failed.
    last_error_code: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The error message that AWS Config returned when the rule last failed.
    last_error_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether AWS Config has evaluated your resources against the rule
    # at least once.

    #   * `true` \- AWS Config has evaluated your AWS resources against the rule at least once.

    #   * `false` \- AWS Config has not once finished evaluating your AWS resources against the rule.
    first_evaluation_started: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ConfigRuleState(Enum):
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETING_RESULTS = "DELETING_RESULTS"
    EVALUATING = "EVALUATING"


@dataclasses.dataclass
class ConfigSnapshotDeliveryProperties(autoboto.ShapeBase):
    """
    Provides options for how often AWS Config delivers configuration snapshots to
    the Amazon S3 bucket in your delivery channel.

    If you want to create a rule that triggers evaluations for your resources when
    AWS Config delivers the configuration snapshot, see the following:

    The frequency for a rule that triggers evaluations for your resources when AWS
    Config delivers the configuration snapshot is set by one of two values,
    depending on which is less frequent:

      * The value for the `deliveryFrequency` parameter within the delivery channel configuration, which sets how often AWS Config delivers configuration snapshots. This value also sets how often AWS Config invokes evaluations for AWS Config rules.

      * The value for the `MaximumExecutionFrequency` parameter, which sets the maximum frequency with which AWS Config invokes evaluations for the rule. For more information, see ConfigRule.

    If the `deliveryFrequency` value is less frequent than the
    `MaximumExecutionFrequency` value for a rule, AWS Config invokes the rule only
    as often as the `deliveryFrequency` value.

      1. For example, you want your rule to run evaluations when AWS Config delivers the configuration snapshot.

      2. You specify the `MaximumExecutionFrequency` value for `Six_Hours`. 

      3. You then specify the delivery channel `deliveryFrequency` value for `TwentyFour_Hours`.

      4. Because the value for `deliveryFrequency` is less frequent than `MaximumExecutionFrequency`, AWS Config invokes evaluations for the rule every 24 hours. 

    You should set the `MaximumExecutionFrequency` value to be at least as frequent
    as the `deliveryFrequency` value. You can view the `deliveryFrequency` value by
    using the `DescribeDeliveryChannnels` action.

    To update the `deliveryFrequency` with which AWS Config delivers your
    configuration snapshots, use the `PutDeliveryChannel` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_frequency",
                "deliveryFrequency",
                autoboto.TypeInfo(MaximumExecutionFrequency),
            ),
        ]

    # The frequency with which AWS Config delivers configuration snapshots.
    delivery_frequency: "MaximumExecutionFrequency" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConfigStreamDeliveryInfo(autoboto.ShapeBase):
    """
    A list that contains the status of the delivery of the configuration stream
    notification to the Amazon SNS topic.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "last_status",
                "lastStatus",
                autoboto.TypeInfo(DeliveryStatus),
            ),
            (
                "last_error_code",
                "lastErrorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "last_error_message",
                "lastErrorMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "last_status_change_time",
                "lastStatusChangeTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # Status of the last attempted delivery.

    # **Note** Providing an SNS topic on a
    # [DeliveryChannel](http://docs.aws.amazon.com/config/latest/APIReference/API_DeliveryChannel.html)
    # for AWS Config is optional. If the SNS delivery is turned off, the last
    # status will be **Not_Applicable**.
    last_status: "DeliveryStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The error code from the last attempted delivery.
    last_error_code: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The error message from the last attempted delivery.
    last_error_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time from the last status change.
    last_status_change_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConfigurationAggregator(autoboto.ShapeBase):
    """
    The details about the configuration aggregator, including information about
    source accounts, regions, and metadata of the aggregator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_aggregator_name",
                "ConfigurationAggregatorName",
                autoboto.TypeInfo(str),
            ),
            (
                "configuration_aggregator_arn",
                "ConfigurationAggregatorArn",
                autoboto.TypeInfo(str),
            ),
            (
                "account_aggregation_sources",
                "AccountAggregationSources",
                autoboto.TypeInfo(typing.List[AccountAggregationSource]),
            ),
            (
                "organization_aggregation_source",
                "OrganizationAggregationSource",
                autoboto.TypeInfo(OrganizationAggregationSource),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_time",
                "LastUpdatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the aggregator.
    configuration_aggregator_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the aggregator.
    configuration_aggregator_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides a list of source accounts and regions to be aggregated.
    account_aggregation_sources: typing.List["AccountAggregationSource"
                                            ] = dataclasses.field(
                                                default_factory=list,
                                            )

    # Provides an organization and list of regions to be aggregated.
    organization_aggregation_source: "OrganizationAggregationSource" = dataclasses.field(
        default_factory=dict,
    )

    # The time stamp when the configuration aggregator was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time of the last update.
    last_updated_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConfigurationItem(autoboto.ShapeBase):
    """
    A list that contains detailed configurations of a specified resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "version",
                "version",
                autoboto.TypeInfo(str),
            ),
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "configuration_item_capture_time",
                "configurationItemCaptureTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "configuration_item_status",
                "configurationItemStatus",
                autoboto.TypeInfo(ConfigurationItemStatus),
            ),
            (
                "configuration_state_id",
                "configurationStateId",
                autoboto.TypeInfo(str),
            ),
            (
                "configuration_item_md5_hash",
                "configurationItemMD5Hash",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "resource_id",
                "resourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_name",
                "resourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_region",
                "awsRegion",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zone",
                "availabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_creation_time",
                "resourceCreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "related_events",
                "relatedEvents",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "relationships",
                "relationships",
                autoboto.TypeInfo(typing.List[Relationship]),
            ),
            (
                "configuration",
                "configuration",
                autoboto.TypeInfo(str),
            ),
            (
                "supplementary_configuration",
                "supplementaryConfiguration",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The version number of the resource configuration.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The 12-digit AWS account ID associated with the resource.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time when the configuration recording was initiated.
    configuration_item_capture_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The configuration item status.
    configuration_item_status: "ConfigurationItemStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An identifier that indicates the ordering of the configuration items of a
    # resource.
    configuration_state_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique MD5 hash that represents the configuration item's state.

    # You can use MD5 hash to compare the states of two or more configuration
    # items that are associated with the same resource.
    configuration_item_md5_hash: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the resource.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of AWS resource.
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the resource (for example, `sg-xxxxxx`).
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The custom name of the resource, if available.
    resource_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The region where the resource resides.
    aws_region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Availability Zone associated with the resource.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time stamp when the resource was created.
    resource_creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A mapping of key value tags associated with the resource.
    tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of CloudTrail event IDs.

    # A populated field indicates that the current configuration was initiated by
    # the events recorded in the CloudTrail log. For more information about
    # CloudTrail, see [What Is AWS
    # CloudTrail](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html).

    # An empty field indicates that the current configuration was not initiated
    # by any event.
    related_events: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of related AWS resources.
    relationships: typing.List["Relationship"] = dataclasses.field(
        default_factory=list,
    )

    # The description of the resource configuration.
    configuration: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Configuration attributes that AWS Config returns for certain resource types
    # to supplement the information returned for the `configuration` parameter.
    supplementary_configuration: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ConfigurationItemStatus(Enum):
    OK = "OK"
    ResourceDiscovered = "ResourceDiscovered"
    ResourceNotRecorded = "ResourceNotRecorded"
    ResourceDeleted = "ResourceDeleted"
    ResourceDeletedNotRecorded = "ResourceDeletedNotRecorded"


@dataclasses.dataclass
class ConfigurationRecorder(autoboto.ShapeBase):
    """
    An object that represents the recording of configuration changes of an AWS
    resource.
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
                "roleARN",
                autoboto.TypeInfo(str),
            ),
            (
                "recording_group",
                "recordingGroup",
                autoboto.TypeInfo(RecordingGroup),
            ),
        ]

    # The name of the recorder. By default, AWS Config automatically assigns the
    # name "default" when creating the configuration recorder. You cannot change
    # the assigned name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon Resource Name (ARN) of the IAM role used to describe the AWS
    # resources associated with the account.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the types of AWS resources for which AWS Config records
    # configuration changes.
    recording_group: "RecordingGroup" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ConfigurationRecorderStatus(autoboto.ShapeBase):
    """
    The current status of the configuration recorder.
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
                "last_start_time",
                "lastStartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_stop_time",
                "lastStopTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "recording",
                "recording",
                autoboto.TypeInfo(bool),
            ),
            (
                "last_status",
                "lastStatus",
                autoboto.TypeInfo(RecorderStatus),
            ),
            (
                "last_error_code",
                "lastErrorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "last_error_message",
                "lastErrorMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "last_status_change_time",
                "lastStatusChangeTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the configuration recorder.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time the recorder was last started.
    last_start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time the recorder was last stopped.
    last_stop_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether or not the recorder is currently recording.
    recording: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The last (previous) status of the recorder.
    last_status: "RecorderStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The error code indicating that the recording failed.
    last_error_code: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The message indicating that the recording failed due to an error.
    last_error_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time when the status was last changed.
    last_status_change_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteAggregationAuthorizationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorized_account_id",
                "AuthorizedAccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "authorized_aws_region",
                "AuthorizedAwsRegion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The 12-digit account ID of the account authorized to aggregate data.
    authorized_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The region authorized to collect aggregated data.
    authorized_aws_region: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteConfigRuleRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "config_rule_name",
                "ConfigRuleName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the AWS Config rule that you want to delete.
    config_rule_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteConfigurationAggregatorRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_aggregator_name",
                "ConfigurationAggregatorName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the configuration aggregator.
    configuration_aggregator_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteConfigurationRecorderRequest(autoboto.ShapeBase):
    """
    The request object for the `DeleteConfigurationRecorder` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_recorder_name",
                "ConfigurationRecorderName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the configuration recorder to be deleted. You can retrieve the
    # name of your configuration recorder by using the
    # `DescribeConfigurationRecorders` action.
    configuration_recorder_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDeliveryChannelRequest(autoboto.ShapeBase):
    """
    The input for the DeleteDeliveryChannel action. The action accepts the following
    data, in JSON format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_channel_name",
                "DeliveryChannelName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the delivery channel to delete.
    delivery_channel_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteEvaluationResultsRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "config_rule_name",
                "ConfigRuleName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the AWS Config rule for which you want to delete the evaluation
    # results.
    config_rule_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteEvaluationResultsResponse(autoboto.OutputShapeBase):
    """
    The output when you delete the evaluation results for the specified AWS Config
    rule.
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
class DeletePendingAggregationRequestRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "requester_account_id",
                "RequesterAccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "requester_aws_region",
                "RequesterAwsRegion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The 12-digit account ID of the account requesting to aggregate data.
    requester_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The region requesting to aggregate data.
    requester_aws_region: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteRetentionConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "retention_configuration_name",
                "RetentionConfigurationName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the retention configuration to delete.
    retention_configuration_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeliverConfigSnapshotRequest(autoboto.ShapeBase):
    """
    The input for the DeliverConfigSnapshot action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_channel_name",
                "deliveryChannelName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the delivery channel through which the snapshot is delivered.
    delivery_channel_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeliverConfigSnapshotResponse(autoboto.OutputShapeBase):
    """
    The output for the DeliverConfigSnapshot action, in JSON format.
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
                "config_snapshot_id",
                "configSnapshotId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the snapshot that is being created.
    config_snapshot_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeliveryChannel(autoboto.ShapeBase):
    """
    The channel through which AWS Config delivers notifications and updated
    configuration states.
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
                "s3_bucket_name",
                "s3BucketName",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_key_prefix",
                "s3KeyPrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "sns_topic_arn",
                "snsTopicARN",
                autoboto.TypeInfo(str),
            ),
            (
                "config_snapshot_delivery_properties",
                "configSnapshotDeliveryProperties",
                autoboto.TypeInfo(ConfigSnapshotDeliveryProperties),
            ),
        ]

    # The name of the delivery channel. By default, AWS Config assigns the name
    # "default" when creating the delivery channel. To change the delivery
    # channel name, you must use the DeleteDeliveryChannel action to delete your
    # current delivery channel, and then you must use the PutDeliveryChannel
    # command to create a delivery channel that has the desired name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the Amazon S3 bucket to which AWS Config delivers configuration
    # snapshots and configuration history files.

    # If you specify a bucket that belongs to another AWS account, that bucket
    # must have policies that grant access permissions to AWS Config. For more
    # information, see [Permissions for the Amazon S3
    # Bucket](http://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-
    # policy.html) in the AWS Config Developer Guide.
    s3_bucket_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The prefix for the specified Amazon S3 bucket.
    s3_key_prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config
    # sends notifications about configuration changes.

    # If you choose a topic from another account, the topic must have policies
    # that grant access permissions to AWS Config. For more information, see
    # [Permissions for the Amazon SNS
    # Topic](http://docs.aws.amazon.com/config/latest/developerguide/sns-topic-
    # policy.html) in the AWS Config Developer Guide.
    sns_topic_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The options for how often AWS Config delivers configuration snapshots to
    # the Amazon S3 bucket.
    config_snapshot_delivery_properties: "ConfigSnapshotDeliveryProperties" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeliveryChannelStatus(autoboto.ShapeBase):
    """
    The status of a specified delivery channel.

    Valid values: `Success` | `Failure`
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
                "config_snapshot_delivery_info",
                "configSnapshotDeliveryInfo",
                autoboto.TypeInfo(ConfigExportDeliveryInfo),
            ),
            (
                "config_history_delivery_info",
                "configHistoryDeliveryInfo",
                autoboto.TypeInfo(ConfigExportDeliveryInfo),
            ),
            (
                "config_stream_delivery_info",
                "configStreamDeliveryInfo",
                autoboto.TypeInfo(ConfigStreamDeliveryInfo),
            ),
        ]

    # The name of the delivery channel.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list containing the status of the delivery of the snapshot to the
    # specified Amazon S3 bucket.
    config_snapshot_delivery_info: "ConfigExportDeliveryInfo" = dataclasses.field(
        default_factory=dict,
    )

    # A list that contains the status of the delivery of the configuration
    # history to the specified Amazon S3 bucket.
    config_history_delivery_info: "ConfigExportDeliveryInfo" = dataclasses.field(
        default_factory=dict,
    )

    # A list containing the status of the delivery of the configuration stream
    # notification to the specified Amazon SNS topic.
    config_stream_delivery_info: "ConfigStreamDeliveryInfo" = dataclasses.field(
        default_factory=dict,
    )


class DeliveryStatus(Enum):
    Success = "Success"
    Failure = "Failure"
    Not_Applicable = "Not_Applicable"


@dataclasses.dataclass
class DescribeAggregateComplianceByConfigRulesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_aggregator_name",
                "ConfigurationAggregatorName",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(ConfigRuleComplianceFilters),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the configuration aggregator.
    configuration_aggregator_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Filters the results by ConfigRuleComplianceFilters object.
    filters: "ConfigRuleComplianceFilters" = dataclasses.field(
        default_factory=dict,
    )

    # The maximum number of evaluation results returned on each page. The default
    # is maximum. If you specify 0, AWS Config uses the default.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The nextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAggregateComplianceByConfigRulesResponse(
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
                "aggregate_compliance_by_config_rules",
                "AggregateComplianceByConfigRules",
                autoboto.TypeInfo(typing.List[AggregateComplianceByConfigRule]),
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

    # Returns a list of AggregateComplianceByConfigRule object.
    aggregate_compliance_by_config_rules: typing.List[
        "AggregateComplianceByConfigRule"
    ] = dataclasses.field(
        default_factory=list,
    )

    # The nextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAggregationAuthorizationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The maximum number of AggregationAuthorizations returned on each page. The
    # default is maximum. If you specify 0, AWS Config uses the default.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The nextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAggregationAuthorizationsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "aggregation_authorizations",
                "AggregationAuthorizations",
                autoboto.TypeInfo(typing.List[AggregationAuthorization]),
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

    # Returns a list of authorizations granted to various aggregator accounts and
    # regions.
    aggregation_authorizations: typing.List["AggregationAuthorization"
                                           ] = dataclasses.field(
                                               default_factory=list,
                                           )

    # The nextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeComplianceByConfigRuleRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "config_rule_names",
                "ConfigRuleNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "compliance_types",
                "ComplianceTypes",
                autoboto.TypeInfo(typing.List[ComplianceType]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Specify one or more AWS Config rule names to filter the results by rule.
    config_rule_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Filters the results by compliance.

    # The allowed values are `COMPLIANT`, `NON_COMPLIANT`, and
    # `INSUFFICIENT_DATA`.
    compliance_types: typing.List["ComplianceType"] = dataclasses.field(
        default_factory=list,
    )

    # The `nextToken` string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeComplianceByConfigRuleResponse(autoboto.OutputShapeBase):
    """

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
                "compliance_by_config_rules",
                "ComplianceByConfigRules",
                autoboto.TypeInfo(typing.List[ComplianceByConfigRule]),
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

    # Indicates whether each of the specified AWS Config rules is compliant.
    compliance_by_config_rules: typing.List["ComplianceByConfigRule"
                                           ] = dataclasses.field(
                                               default_factory=list,
                                           )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeComplianceByResourceRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "compliance_types",
                "ComplianceTypes",
                autoboto.TypeInfo(typing.List[ComplianceType]),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The types of AWS resources for which you want compliance information (for
    # example, `AWS::EC2::Instance`). For this action, you can specify that the
    # resource type is an AWS account by specifying `AWS::::Account`.
    resource_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the AWS resource for which you want compliance information. You
    # can specify only one resource ID. If you specify a resource ID, you must
    # also specify a type for `ResourceType`.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filters the results by compliance.

    # The allowed values are `COMPLIANT` and `NON_COMPLIANT`.
    compliance_types: typing.List["ComplianceType"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of evaluation results returned on each page. The default
    # is 10. You cannot specify a number greater than 100. If you specify 0, AWS
    # Config uses the default.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The `nextToken` string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeComplianceByResourceResponse(autoboto.OutputShapeBase):
    """

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
                "compliance_by_resources",
                "ComplianceByResources",
                autoboto.TypeInfo(typing.List[ComplianceByResource]),
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

    # Indicates whether the specified AWS resource complies with all of the AWS
    # Config rules that evaluate it.
    compliance_by_resources: typing.List["ComplianceByResource"
                                        ] = dataclasses.field(
                                            default_factory=list,
                                        )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConfigRuleEvaluationStatusRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "config_rule_names",
                "ConfigRuleNames",
                autoboto.TypeInfo(typing.List[str]),
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

    # The name of the AWS managed Config rules for which you want status
    # information. If you do not specify any names, AWS Config returns status
    # information for all AWS managed Config rules that you use.
    config_rule_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The `nextToken` string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of rule evaluation results that you want returned.

    # This parameter is required if the rule limit for your account is more than
    # the default of 50 rules.

    # For information about requesting a rule limit increase, see [AWS Config
    # Limits](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_config)
    # in the _AWS General Reference Guide_.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConfigRuleEvaluationStatusResponse(autoboto.OutputShapeBase):
    """

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
                "config_rules_evaluation_status",
                "ConfigRulesEvaluationStatus",
                autoboto.TypeInfo(typing.List[ConfigRuleEvaluationStatus]),
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

    # Status information about your AWS managed Config rules.
    config_rules_evaluation_status: typing.List["ConfigRuleEvaluationStatus"
                                               ] = dataclasses.field(
                                                   default_factory=list,
                                               )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConfigRulesRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "config_rule_names",
                "ConfigRuleNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The names of the AWS Config rules for which you want details. If you do not
    # specify any names, AWS Config returns details for all your rules.
    config_rule_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The `nextToken` string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConfigRulesResponse(autoboto.OutputShapeBase):
    """

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
                "config_rules",
                "ConfigRules",
                autoboto.TypeInfo(typing.List[ConfigRule]),
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

    # The details about your AWS Config rules.
    config_rules: typing.List["ConfigRule"] = dataclasses.field(
        default_factory=list,
    )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConfigurationAggregatorSourcesStatusRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_aggregator_name",
                "ConfigurationAggregatorName",
                autoboto.TypeInfo(str),
            ),
            (
                "update_status",
                "UpdateStatus",
                autoboto.TypeInfo(typing.List[AggregatedSourceStatusType]),
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

    # The name of the configuration aggregator.
    configuration_aggregator_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Filters the status type.

    #   * Valid value FAILED indicates errors while moving data.

    #   * Valid value SUCCEEDED indicates the data was successfully moved.

    #   * Valid value OUTDATED indicates the data is not the most recent.
    update_status: typing.List["AggregatedSourceStatusType"
                              ] = dataclasses.field(
                                  default_factory=list,
                              )

    # The nextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of AggregatorSourceStatus returned on each page. The
    # default is maximum. If you specify 0, AWS Config uses the default.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConfigurationAggregatorSourcesStatusResponse(
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
                "aggregated_source_status_list",
                "AggregatedSourceStatusList",
                autoboto.TypeInfo(typing.List[AggregatedSourceStatus]),
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

    # Returns an AggregatedSourceStatus object.
    aggregated_source_status_list: typing.List["AggregatedSourceStatus"
                                              ] = dataclasses.field(
                                                  default_factory=list,
                                              )

    # The nextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConfigurationAggregatorsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_aggregator_names",
                "ConfigurationAggregatorNames",
                autoboto.TypeInfo(typing.List[str]),
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

    # The name of the configuration aggregators.
    configuration_aggregator_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The nextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of configuration aggregators returned on each page. The
    # default is maximum. If you specify 0, AWS Config uses the default.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConfigurationAggregatorsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "configuration_aggregators",
                "ConfigurationAggregators",
                autoboto.TypeInfo(typing.List[ConfigurationAggregator]),
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

    # Returns a ConfigurationAggregators object.
    configuration_aggregators: typing.List["ConfigurationAggregator"
                                          ] = dataclasses.field(
                                              default_factory=list,
                                          )

    # The nextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConfigurationRecorderStatusRequest(autoboto.ShapeBase):
    """
    The input for the DescribeConfigurationRecorderStatus action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_recorder_names",
                "ConfigurationRecorderNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name(s) of the configuration recorder. If the name is not specified,
    # the action returns the current status of all the configuration recorders
    # associated with the account.
    configuration_recorder_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeConfigurationRecorderStatusResponse(autoboto.OutputShapeBase):
    """
    The output for the DescribeConfigurationRecorderStatus action, in JSON format.
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
                "configuration_recorders_status",
                "ConfigurationRecordersStatus",
                autoboto.TypeInfo(typing.List[ConfigurationRecorderStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list that contains status of the specified recorders.
    configuration_recorders_status: typing.List["ConfigurationRecorderStatus"
                                               ] = dataclasses.field(
                                                   default_factory=list,
                                               )


@dataclasses.dataclass
class DescribeConfigurationRecordersRequest(autoboto.ShapeBase):
    """
    The input for the DescribeConfigurationRecorders action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_recorder_names",
                "ConfigurationRecorderNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A list of configuration recorder names.
    configuration_recorder_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeConfigurationRecordersResponse(autoboto.OutputShapeBase):
    """
    The output for the DescribeConfigurationRecorders action.
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
                "configuration_recorders",
                "ConfigurationRecorders",
                autoboto.TypeInfo(typing.List[ConfigurationRecorder]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list that contains the descriptions of the specified configuration
    # recorders.
    configuration_recorders: typing.List["ConfigurationRecorder"
                                        ] = dataclasses.field(
                                            default_factory=list,
                                        )


@dataclasses.dataclass
class DescribeDeliveryChannelStatusRequest(autoboto.ShapeBase):
    """
    The input for the DeliveryChannelStatus action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_channel_names",
                "DeliveryChannelNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A list of delivery channel names.
    delivery_channel_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeDeliveryChannelStatusResponse(autoboto.OutputShapeBase):
    """
    The output for the DescribeDeliveryChannelStatus action.
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
                "delivery_channels_status",
                "DeliveryChannelsStatus",
                autoboto.TypeInfo(typing.List[DeliveryChannelStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list that contains the status of a specified delivery channel.
    delivery_channels_status: typing.List["DeliveryChannelStatus"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )


@dataclasses.dataclass
class DescribeDeliveryChannelsRequest(autoboto.ShapeBase):
    """
    The input for the DescribeDeliveryChannels action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_channel_names",
                "DeliveryChannelNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A list of delivery channel names.
    delivery_channel_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeDeliveryChannelsResponse(autoboto.OutputShapeBase):
    """
    The output for the DescribeDeliveryChannels action.
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
                "delivery_channels",
                "DeliveryChannels",
                autoboto.TypeInfo(typing.List[DeliveryChannel]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list that contains the descriptions of the specified delivery channel.
    delivery_channels: typing.List["DeliveryChannel"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribePendingAggregationRequestsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The maximum number of evaluation results returned on each page. The default
    # is maximum. If you specify 0, AWS Config uses the default.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The nextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePendingAggregationRequestsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pending_aggregation_requests",
                "PendingAggregationRequests",
                autoboto.TypeInfo(typing.List[PendingAggregationRequest]),
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

    # Returns a PendingAggregationRequests object.
    pending_aggregation_requests: typing.List["PendingAggregationRequest"
                                             ] = dataclasses.field(
                                                 default_factory=list,
                                             )

    # The nextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRetentionConfigurationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "retention_configuration_names",
                "RetentionConfigurationNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of names of retention configurations for which you want details. If
    # you do not specify a name, AWS Config returns details for all the retention
    # configurations for that account.

    # Currently, AWS Config supports only one retention configuration per region
    # in your account.
    retention_configuration_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The `nextToken` string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRetentionConfigurationsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "retention_configurations",
                "RetentionConfigurations",
                autoboto.TypeInfo(typing.List[RetentionConfiguration]),
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

    # Returns a retention configuration object.
    retention_configurations: typing.List["RetentionConfiguration"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )

    # The `nextToken` string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Evaluation(autoboto.ShapeBase):
    """
    Identifies an AWS resource and indicates whether it complies with the AWS Config
    rule that it was evaluated against.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compliance_resource_type",
                "ComplianceResourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "compliance_resource_id",
                "ComplianceResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "compliance_type",
                "ComplianceType",
                autoboto.TypeInfo(ComplianceType),
            ),
            (
                "ordering_timestamp",
                "OrderingTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "annotation",
                "Annotation",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of AWS resource that was evaluated.
    compliance_resource_type: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the AWS resource that was evaluated.
    compliance_resource_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the AWS resource complies with the AWS Config rule that
    # it was evaluated against.

    # For the `Evaluation` data type, AWS Config supports only the `COMPLIANT`,
    # `NON_COMPLIANT`, and `NOT_APPLICABLE` values. AWS Config does not support
    # the `INSUFFICIENT_DATA` value for this data type.

    # Similarly, AWS Config does not accept `INSUFFICIENT_DATA` as the value for
    # `ComplianceType` from a `PutEvaluations` request. For example, an AWS
    # Lambda function for a custom AWS Config rule cannot pass an
    # `INSUFFICIENT_DATA` value to AWS Config.
    compliance_type: "ComplianceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time of the event in AWS Config that triggered the evaluation. For
    # event-based evaluations, the time indicates when AWS Config created the
    # configuration item that triggered the evaluation. For periodic evaluations,
    # the time indicates when AWS Config triggered the evaluation at the
    # frequency that you specified (for example, every 24 hours).
    ordering_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Supplementary information about how the evaluation determined the
    # compliance.
    annotation: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EvaluationResult(autoboto.ShapeBase):
    """
    The details of an AWS Config evaluation. Provides the AWS resource that was
    evaluated, the compliance of the resource, related time stamps, and
    supplementary information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "evaluation_result_identifier",
                "EvaluationResultIdentifier",
                autoboto.TypeInfo(EvaluationResultIdentifier),
            ),
            (
                "compliance_type",
                "ComplianceType",
                autoboto.TypeInfo(ComplianceType),
            ),
            (
                "result_recorded_time",
                "ResultRecordedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "config_rule_invoked_time",
                "ConfigRuleInvokedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "annotation",
                "Annotation",
                autoboto.TypeInfo(str),
            ),
            (
                "result_token",
                "ResultToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Uniquely identifies the evaluation result.
    evaluation_result_identifier: "EvaluationResultIdentifier" = dataclasses.field(
        default_factory=dict,
    )

    # Indicates whether the AWS resource complies with the AWS Config rule that
    # evaluated it.

    # For the `EvaluationResult` data type, AWS Config supports only the
    # `COMPLIANT`, `NON_COMPLIANT`, and `NOT_APPLICABLE` values. AWS Config does
    # not support the `INSUFFICIENT_DATA` value for the `EvaluationResult` data
    # type.
    compliance_type: "ComplianceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time when AWS Config recorded the evaluation result.
    result_recorded_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time when the AWS Config rule evaluated the AWS resource.
    config_rule_invoked_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Supplementary information about how the evaluation determined the
    # compliance.
    annotation: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An encrypted token that associates an evaluation with an AWS Config rule.
    # The token identifies the rule, the AWS resource being evaluated, and the
    # event that triggered the evaluation.
    result_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EvaluationResultIdentifier(autoboto.ShapeBase):
    """
    Uniquely identifies an evaluation result.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "evaluation_result_qualifier",
                "EvaluationResultQualifier",
                autoboto.TypeInfo(EvaluationResultQualifier),
            ),
            (
                "ordering_timestamp",
                "OrderingTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # Identifies an AWS Config rule used to evaluate an AWS resource, and
    # provides the type and ID of the evaluated resource.
    evaluation_result_qualifier: "EvaluationResultQualifier" = dataclasses.field(
        default_factory=dict,
    )

    # The time of the event that triggered the evaluation of your AWS resources.
    # The time can indicate when AWS Config delivered a configuration item change
    # notification, or it can indicate when AWS Config delivered the
    # configuration snapshot, depending on which event triggered the evaluation.
    ordering_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EvaluationResultQualifier(autoboto.ShapeBase):
    """
    Identifies an AWS Config rule that evaluated an AWS resource, and provides the
    type and ID of the resource that the rule evaluated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "config_rule_name",
                "ConfigRuleName",
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
        ]

    # The name of the AWS Config rule that was used in the evaluation.
    config_rule_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of AWS resource that was evaluated.
    resource_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the evaluated AWS resource.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class EventSource(Enum):
    aws_config = "aws.config"


@dataclasses.dataclass
class GetAggregateComplianceDetailsByConfigRuleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_aggregator_name",
                "ConfigurationAggregatorName",
                autoboto.TypeInfo(str),
            ),
            (
                "config_rule_name",
                "ConfigRuleName",
                autoboto.TypeInfo(str),
            ),
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_region",
                "AwsRegion",
                autoboto.TypeInfo(str),
            ),
            (
                "compliance_type",
                "ComplianceType",
                autoboto.TypeInfo(ComplianceType),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the configuration aggregator.
    configuration_aggregator_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the AWS Config rule for which you want compliance information.
    config_rule_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The 12-digit account ID of the source account.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The source region from where the data is aggregated.
    aws_region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The resource compliance status.

    # For the `GetAggregateComplianceDetailsByConfigRuleRequest` data type, AWS
    # Config supports only the `COMPLIANT` and `NON_COMPLIANT`. AWS Config does
    # not support the `NOT_APPLICABLE` and `INSUFFICIENT_DATA` values.
    compliance_type: "ComplianceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of evaluation results returned on each page. The default
    # is 50. You cannot specify a number greater than 100. If you specify 0, AWS
    # Config uses the default.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The nextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAggregateComplianceDetailsByConfigRuleResponse(
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
                "aggregate_evaluation_results",
                "AggregateEvaluationResults",
                autoboto.TypeInfo(typing.List[AggregateEvaluationResult]),
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

    # Returns an AggregateEvaluationResults object.
    aggregate_evaluation_results: typing.List["AggregateEvaluationResult"
                                             ] = dataclasses.field(
                                                 default_factory=list,
                                             )

    # The nextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAggregateConfigRuleComplianceSummaryRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_aggregator_name",
                "ConfigurationAggregatorName",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(ConfigRuleComplianceSummaryFilters),
            ),
            (
                "group_by_key",
                "GroupByKey",
                autoboto.TypeInfo(ConfigRuleComplianceSummaryGroupKey),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the configuration aggregator.
    configuration_aggregator_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Filters the results based on the ConfigRuleComplianceSummaryFilters object.
    filters: "ConfigRuleComplianceSummaryFilters" = dataclasses.field(
        default_factory=dict,
    )

    # Groups the result based on ACCOUNT_ID or AWS_REGION.
    group_by_key: "ConfigRuleComplianceSummaryGroupKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of evaluation results returned on each page. The default
    # is 1000. You cannot specify a number greater than 1000. If you specify 0,
    # AWS Config uses the default.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The nextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAggregateConfigRuleComplianceSummaryResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "group_by_key",
                "GroupByKey",
                autoboto.TypeInfo(str),
            ),
            (
                "aggregate_compliance_counts",
                "AggregateComplianceCounts",
                autoboto.TypeInfo(typing.List[AggregateComplianceCount]),
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

    # Groups the result based on ACCOUNT_ID or AWS_REGION.
    group_by_key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Returns a list of AggregateComplianceCounts object.
    aggregate_compliance_counts: typing.List["AggregateComplianceCount"
                                            ] = dataclasses.field(
                                                default_factory=list,
                                            )

    # The nextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetComplianceDetailsByConfigRuleRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "config_rule_name",
                "ConfigRuleName",
                autoboto.TypeInfo(str),
            ),
            (
                "compliance_types",
                "ComplianceTypes",
                autoboto.TypeInfo(typing.List[ComplianceType]),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the AWS Config rule for which you want compliance information.
    config_rule_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Filters the results by compliance.

    # The allowed values are `COMPLIANT`, `NON_COMPLIANT`, and `NOT_APPLICABLE`.
    compliance_types: typing.List["ComplianceType"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of evaluation results returned on each page. The default
    # is 10. You cannot specify a number greater than 100. If you specify 0, AWS
    # Config uses the default.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The `nextToken` string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetComplianceDetailsByConfigRuleResponse(autoboto.OutputShapeBase):
    """

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
                "evaluation_results",
                "EvaluationResults",
                autoboto.TypeInfo(typing.List[EvaluationResult]),
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

    # Indicates whether the AWS resource complies with the specified AWS Config
    # rule.
    evaluation_results: typing.List["EvaluationResult"] = dataclasses.field(
        default_factory=list,
    )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetComplianceDetailsByResourceRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "compliance_types",
                "ComplianceTypes",
                autoboto.TypeInfo(typing.List[ComplianceType]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of the AWS resource for which you want compliance information.
    resource_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the AWS resource for which you want compliance information.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filters the results by compliance.

    # The allowed values are `COMPLIANT`, `NON_COMPLIANT`, and `NOT_APPLICABLE`.
    compliance_types: typing.List["ComplianceType"] = dataclasses.field(
        default_factory=list,
    )

    # The `nextToken` string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetComplianceDetailsByResourceResponse(autoboto.OutputShapeBase):
    """

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
                "evaluation_results",
                "EvaluationResults",
                autoboto.TypeInfo(typing.List[EvaluationResult]),
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

    # Indicates whether the specified AWS resource complies each AWS Config rule.
    evaluation_results: typing.List["EvaluationResult"] = dataclasses.field(
        default_factory=list,
    )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetComplianceSummaryByConfigRuleResponse(autoboto.OutputShapeBase):
    """

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
                "compliance_summary",
                "ComplianceSummary",
                autoboto.TypeInfo(ComplianceSummary),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of AWS Config rules that are compliant and the number that are
    # noncompliant, up to a maximum of 25 for each.
    compliance_summary: "ComplianceSummary" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetComplianceSummaryByResourceTypeRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_types",
                "ResourceTypes",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # Specify one or more resource types to get the number of resources that are
    # compliant and the number that are noncompliant for each resource type.

    # For this request, you can specify an AWS resource type such as
    # `AWS::EC2::Instance`. You can specify that the resource type is an AWS
    # account by specifying `AWS::::Account`.
    resource_types: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class GetComplianceSummaryByResourceTypeResponse(autoboto.OutputShapeBase):
    """

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
                "compliance_summaries_by_resource_type",
                "ComplianceSummariesByResourceType",
                autoboto.TypeInfo(typing.List[ComplianceSummaryByResourceType]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of resources that are compliant and the number that are
    # noncompliant. If one or more resource types were provided with the request,
    # the numbers are returned for each resource type. The maximum number
    # returned is 100.
    compliance_summaries_by_resource_type: typing.List[
        "ComplianceSummaryByResourceType"
    ] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetDiscoveredResourceCountsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_types",
                "resourceTypes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The comma-separated list that specifies the resource types that you want
    # AWS Config to return (for example, `"AWS::EC2::Instance"`,
    # `"AWS::IAM::User"`).

    # If a value for `resourceTypes` is not specified, AWS Config returns all
    # resource types that AWS Config is recording in the region for your account.

    # If the configuration recorder is turned off, AWS Config returns an empty
    # list of ResourceCount objects. If the configuration recorder is not
    # recording a specific resource type (for example, S3 buckets), that resource
    # type is not returned in the list of ResourceCount objects.
    resource_types: typing.List[str] = dataclasses.field(default_factory=list, )

    # The maximum number of ResourceCount objects returned on each page. The
    # default is 100. You cannot specify a number greater than 100. If you
    # specify 0, AWS Config uses the default.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The `nextToken` string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDiscoveredResourceCountsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "total_discovered_resources",
                "totalDiscoveredResources",
                autoboto.TypeInfo(int),
            ),
            (
                "resource_counts",
                "resourceCounts",
                autoboto.TypeInfo(typing.List[ResourceCount]),
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

    # The total number of resources that AWS Config is recording in the region
    # for your account. If you specify resource types in the request, AWS Config
    # returns only the total number of resources for those resource types.

    # **Example**

    #   1. AWS Config is recording three resource types in the US East (Ohio) Region for your account: 25 EC2 instances, 20 IAM users, and 15 S3 buckets, for a total of 60 resources.

    #   2. You make a call to the `GetDiscoveredResourceCounts` action and specify the resource type, `"AWS::EC2::Instances"`, in the request.

    #   3. AWS Config returns 25 for `totalDiscoveredResources`.
    total_discovered_resources: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The list of `ResourceCount` objects. Each object is listed in descending
    # order by the number of resources.
    resource_counts: typing.List["ResourceCount"] = dataclasses.field(
        default_factory=list,
    )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetResourceConfigHistoryRequest(autoboto.ShapeBase):
    """
    The input for the GetResourceConfigHistory action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "resource_id",
                "resourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "later_time",
                "laterTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "earlier_time",
                "earlierTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "chronological_order",
                "chronologicalOrder",
                autoboto.TypeInfo(ChronologicalOrder),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The resource type.
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the resource (for example., `sg-xxxxxx`).
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time stamp that indicates a later time. If not specified, current time
    # is taken.
    later_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time stamp that indicates an earlier time. If not specified, the action
    # returns paginated results that contain configuration items that start when
    # the first configuration item was recorded.
    earlier_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The chronological order for configuration items listed. By default, the
    # results are listed in reverse chronological order.
    chronological_order: "ChronologicalOrder" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of configuration items returned on each page. The
    # default is 10. You cannot specify a number greater than 100. If you specify
    # 0, AWS Config uses the default.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The `nextToken` string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetResourceConfigHistoryResponse(autoboto.OutputShapeBase):
    """
    The output for the GetResourceConfigHistory action.
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
                "configuration_items",
                "configurationItems",
                autoboto.TypeInfo(typing.List[ConfigurationItem]),
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

    # A list that contains the configuration history of one or more resources.
    configuration_items: typing.List["ConfigurationItem"] = dataclasses.field(
        default_factory=list,
    )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InsufficientDeliveryPolicyException(autoboto.ShapeBase):
    """
    Your Amazon S3 bucket policy does not permit AWS Config to write to it.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InsufficientPermissionsException(autoboto.ShapeBase):
    """
    Indicates one of the following errors:

      * The rule cannot be created because the IAM role assigned to AWS Config lacks permissions to perform the config:Put* action.

      * The AWS Lambda function cannot be invoked. Check the function ARN, and check the function's permissions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidConfigurationRecorderNameException(autoboto.ShapeBase):
    """
    You have provided a configuration recorder name that is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDeliveryChannelNameException(autoboto.ShapeBase):
    """
    The specified delivery channel name is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidLimitException(autoboto.ShapeBase):
    """
    The specified limit is outside the allowable range.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidNextTokenException(autoboto.ShapeBase):
    """
    The specified next token is invalid. Specify the `nextToken` string that was
    returned in the previous response to get the next page of results.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidParameterValueException(autoboto.ShapeBase):
    """
    One or more of the specified parameters are invalid. Verify that your parameters
    are valid and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRecordingGroupException(autoboto.ShapeBase):
    """
    AWS Config throws an exception if the recording group does not contain a valid
    list of resource types. Invalid values might also be incorrectly formatted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidResultTokenException(autoboto.ShapeBase):
    """
    The specified `ResultToken` is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRoleException(autoboto.ShapeBase):
    """
    You have provided a null or empty role ARN.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidS3KeyPrefixException(autoboto.ShapeBase):
    """
    The specified Amazon S3 key prefix is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSNSTopicARNException(autoboto.ShapeBase):
    """
    The specified Amazon SNS topic does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTimeRangeException(autoboto.ShapeBase):
    """
    The specified time range is not valid. The earlier time is not chronologically
    before the later time.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LastDeliveryChannelDeleteFailedException(autoboto.ShapeBase):
    """
    You cannot delete the delivery channel you specified because the configuration
    recorder is running.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    This exception is thrown if an evaluation is in progress or if you call the
    StartConfigRulesEvaluation API more than once per minute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListDiscoveredResourcesRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "resource_ids",
                "resourceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "resource_name",
                "resourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(int),
            ),
            (
                "include_deleted_resources",
                "includeDeletedResources",
                autoboto.TypeInfo(bool),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of resources that you want AWS Config to list in the response.
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The IDs of only those resources that you want AWS Config to list in the
    # response. If you do not specify this parameter, AWS Config lists all
    # resources of the specified type that it has discovered.
    resource_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The custom name of only those resources that you want AWS Config to list in
    # the response. If you do not specify this parameter, AWS Config lists all
    # resources of the specified type that it has discovered.
    resource_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of resource identifiers returned on each page. The
    # default is 100. You cannot specify a number greater than 100. If you
    # specify 0, AWS Config uses the default.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies whether AWS Config includes deleted resources in the results. By
    # default, deleted resources are not included.
    include_deleted_resources: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The `nextToken` string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDiscoveredResourcesResponse(autoboto.OutputShapeBase):
    """

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
                "resource_identifiers",
                "resourceIdentifiers",
                autoboto.TypeInfo(typing.List[ResourceIdentifier]),
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

    # The details that identify a resource that is discovered by AWS Config,
    # including the resource type, ID, and (if available) the custom resource
    # name.
    resource_identifiers: typing.List["ResourceIdentifier"] = dataclasses.field(
        default_factory=list,
    )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaxNumberOfConfigRulesExceededException(autoboto.ShapeBase):
    """
    Failed to add the AWS Config rule because the account already contains the
    maximum number of 50 rules. Consider deleting any deactivated rules before you
    add new rules.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class MaxNumberOfConfigurationRecordersExceededException(autoboto.ShapeBase):
    """
    You have reached the limit of the number of recorders you can create.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class MaxNumberOfDeliveryChannelsExceededException(autoboto.ShapeBase):
    """
    You have reached the limit of the number of delivery channels you can create.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class MaxNumberOfRetentionConfigurationsExceededException(autoboto.ShapeBase):
    """
    Failed to add the retention configuration because a retention configuration with
    that name already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class MaximumExecutionFrequency(Enum):
    One_Hour = "One_Hour"
    Three_Hours = "Three_Hours"
    Six_Hours = "Six_Hours"
    Twelve_Hours = "Twelve_Hours"
    TwentyFour_Hours = "TwentyFour_Hours"


class MessageType(Enum):
    ConfigurationItemChangeNotification = "ConfigurationItemChangeNotification"
    ConfigurationSnapshotDeliveryCompleted = "ConfigurationSnapshotDeliveryCompleted"
    ScheduledNotification = "ScheduledNotification"
    OversizedConfigurationItemChangeNotification = "OversizedConfigurationItemChangeNotification"


@dataclasses.dataclass
class NoAvailableConfigurationRecorderException(autoboto.ShapeBase):
    """
    There are no configuration recorders available to provide the role needed to
    describe your resources. Create a configuration recorder.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NoAvailableDeliveryChannelException(autoboto.ShapeBase):
    """
    There is no delivery channel available to record configurations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NoAvailableOrganizationException(autoboto.ShapeBase):
    """
    Organization does is no longer available.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NoRunningConfigurationRecorderException(autoboto.ShapeBase):
    """
    There is no configuration recorder running.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NoSuchBucketException(autoboto.ShapeBase):
    """
    The specified Amazon S3 bucket does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NoSuchConfigRuleException(autoboto.ShapeBase):
    """
    One or more AWS Config rules in the request are invalid. Verify that the rule
    names are correct and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NoSuchConfigurationAggregatorException(autoboto.ShapeBase):
    """
    You have specified a configuration aggregator that does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NoSuchConfigurationRecorderException(autoboto.ShapeBase):
    """
    You have specified a configuration recorder that does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NoSuchDeliveryChannelException(autoboto.ShapeBase):
    """
    You have specified a delivery channel that does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NoSuchRetentionConfigurationException(autoboto.ShapeBase):
    """
    You have specified a retention configuration that does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class OrganizationAccessDeniedException(autoboto.ShapeBase):
    """
    No permission to call the EnableAWSServiceAccess API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class OrganizationAggregationSource(autoboto.ShapeBase):
    """
    This object contains regions to setup the aggregator and an IAM role to retrieve
    organization details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_regions",
                "AwsRegions",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "all_aws_regions",
                "AllAwsRegions",
                autoboto.TypeInfo(bool),
            ),
        ]

    # ARN of the IAM role used to retreive AWS Organization details associated
    # with the aggregator account.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The source regions being aggregated.
    aws_regions: typing.List[str] = dataclasses.field(default_factory=list, )

    # If true, aggregate existing AWS Config regions and future regions.
    all_aws_regions: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OrganizationAllFeaturesNotEnabledException(autoboto.ShapeBase):
    """
    The configuration aggregator cannot be created because organization does not
    have all features enabled.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class Owner(Enum):
    CUSTOM_LAMBDA = "CUSTOM_LAMBDA"
    AWS = "AWS"


@dataclasses.dataclass
class PendingAggregationRequest(autoboto.ShapeBase):
    """
    An object that represents the account ID and region of an aggregator account
    that is requesting authorization but is not yet authorized.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "requester_account_id",
                "RequesterAccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "requester_aws_region",
                "RequesterAwsRegion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The 12-digit account ID of the account requesting to aggregate data.
    requester_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The region requesting to aggregate data.
    requester_aws_region: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutAggregationAuthorizationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authorized_account_id",
                "AuthorizedAccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "authorized_aws_region",
                "AuthorizedAwsRegion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The 12-digit account ID of the account authorized to aggregate data.
    authorized_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The region authorized to collect aggregated data.
    authorized_aws_region: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutAggregationAuthorizationResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "aggregation_authorization",
                "AggregationAuthorization",
                autoboto.TypeInfo(AggregationAuthorization),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Returns an AggregationAuthorization object.
    aggregation_authorization: "AggregationAuthorization" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutConfigRuleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "config_rule",
                "ConfigRule",
                autoboto.TypeInfo(ConfigRule),
            ),
        ]

    # The rule that you want to add to your account.
    config_rule: "ConfigRule" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PutConfigurationAggregatorRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_aggregator_name",
                "ConfigurationAggregatorName",
                autoboto.TypeInfo(str),
            ),
            (
                "account_aggregation_sources",
                "AccountAggregationSources",
                autoboto.TypeInfo(typing.List[AccountAggregationSource]),
            ),
            (
                "organization_aggregation_source",
                "OrganizationAggregationSource",
                autoboto.TypeInfo(OrganizationAggregationSource),
            ),
        ]

    # The name of the configuration aggregator.
    configuration_aggregator_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of AccountAggregationSource object.
    account_aggregation_sources: typing.List["AccountAggregationSource"
                                            ] = dataclasses.field(
                                                default_factory=list,
                                            )

    # An OrganizationAggregationSource object.
    organization_aggregation_source: "OrganizationAggregationSource" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutConfigurationAggregatorResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "configuration_aggregator",
                "ConfigurationAggregator",
                autoboto.TypeInfo(ConfigurationAggregator),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Returns a ConfigurationAggregator object.
    configuration_aggregator: "ConfigurationAggregator" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutConfigurationRecorderRequest(autoboto.ShapeBase):
    """
    The input for the PutConfigurationRecorder action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_recorder",
                "ConfigurationRecorder",
                autoboto.TypeInfo(ConfigurationRecorder),
            ),
        ]

    # The configuration recorder object that records each configuration change
    # made to the resources.
    configuration_recorder: "ConfigurationRecorder" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutDeliveryChannelRequest(autoboto.ShapeBase):
    """
    The input for the PutDeliveryChannel action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_channel",
                "DeliveryChannel",
                autoboto.TypeInfo(DeliveryChannel),
            ),
        ]

    # The configuration delivery channel object that delivers the configuration
    # information to an Amazon S3 bucket and to an Amazon SNS topic.
    delivery_channel: "DeliveryChannel" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutEvaluationsRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "result_token",
                "ResultToken",
                autoboto.TypeInfo(str),
            ),
            (
                "evaluations",
                "Evaluations",
                autoboto.TypeInfo(typing.List[Evaluation]),
            ),
            (
                "test_mode",
                "TestMode",
                autoboto.TypeInfo(bool),
            ),
        ]

    # An encrypted token that associates an evaluation with an AWS Config rule.
    # Identifies the rule and the event that triggered the evaluation.
    result_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The assessments that the AWS Lambda function performs. Each evaluation
    # identifies an AWS resource and indicates whether it complies with the AWS
    # Config rule that invokes the AWS Lambda function.
    evaluations: typing.List["Evaluation"] = dataclasses.field(
        default_factory=list,
    )

    # Use this parameter to specify a test run for `PutEvaluations`. You can
    # verify whether your AWS Lambda function will deliver evaluation results to
    # AWS Config. No updates occur to your existing evaluations, and evaluation
    # results are not sent to AWS Config.

    # When `TestMode` is `true`, `PutEvaluations` doesn't require a valid value
    # for the `ResultToken` parameter, but the value cannot be null.
    test_mode: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutEvaluationsResponse(autoboto.OutputShapeBase):
    """

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
                "failed_evaluations",
                "FailedEvaluations",
                autoboto.TypeInfo(typing.List[Evaluation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Requests that failed because of a client or server error.
    failed_evaluations: typing.List["Evaluation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class PutRetentionConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "retention_period_in_days",
                "RetentionPeriodInDays",
                autoboto.TypeInfo(int),
            ),
        ]

    # Number of days AWS Config stores your historical information.

    # Currently, only applicable to the configuration item history.
    retention_period_in_days: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutRetentionConfigurationResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "retention_configuration",
                "RetentionConfiguration",
                autoboto.TypeInfo(RetentionConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Returns a retention configuration object.
    retention_configuration: "RetentionConfiguration" = dataclasses.field(
        default_factory=dict,
    )


class RecorderStatus(Enum):
    Pending = "Pending"
    Success = "Success"
    Failure = "Failure"


@dataclasses.dataclass
class RecordingGroup(autoboto.ShapeBase):
    """
    Specifies the types of AWS resource for which AWS Config records configuration
    changes.

    In the recording group, you specify whether all supported types or specific
    types of resources are recorded.

    By default, AWS Config records configuration changes for all supported types of
    regional resources that AWS Config discovers in the region in which it is
    running. Regional resources are tied to a region and can be used only in that
    region. Examples of regional resources are EC2 instances and EBS volumes.

    You can also have AWS Config record configuration changes for supported types of
    global resources (for example, IAM resources). Global resources are not tied to
    an individual region and can be used in all regions.

    The configuration details for any global resource are the same in all regions.
    If you customize AWS Config in multiple regions to record global resources, it
    will create multiple configuration items each time a global resource changes:
    one configuration item for each region. These configuration items will contain
    identical data. To prevent duplicate configuration items, you should consider
    customizing AWS Config in only one region to record global resources, unless you
    want the configuration items to be available in multiple regions.

    If you don't want AWS Config to record all resources, you can specify which
    types of resources it will record with the `resourceTypes` parameter.

    For a list of supported resource types, see [Supported Resource
    Types](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-
    reference.html#supported-resources).

    For more information, see [Selecting Which Resources AWS Config
    Records](http://docs.aws.amazon.com/config/latest/developerguide/select-
    resources.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "all_supported",
                "allSupported",
                autoboto.TypeInfo(bool),
            ),
            (
                "include_global_resource_types",
                "includeGlobalResourceTypes",
                autoboto.TypeInfo(bool),
            ),
            (
                "resource_types",
                "resourceTypes",
                autoboto.TypeInfo(typing.List[ResourceType]),
            ),
        ]

    # Specifies whether AWS Config records configuration changes for every
    # supported type of regional resource.

    # If you set this option to `true`, when AWS Config adds support for a new
    # type of regional resource, it starts recording resources of that type
    # automatically.

    # If you set this option to `true`, you cannot enumerate a list of
    # `resourceTypes`.
    all_supported: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether AWS Config includes all supported types of global
    # resources (for example, IAM resources) with the resources that it records.

    # Before you can set this option to `true`, you must set the `allSupported`
    # option to `true`.

    # If you set this option to `true`, when AWS Config adds support for a new
    # type of global resource, it starts recording resources of that type
    # automatically.

    # The configuration details for any global resource are the same in all
    # regions. To prevent duplicate configuration items, you should consider
    # customizing AWS Config in only one region to record global resources.
    include_global_resource_types: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A comma-separated list that specifies the types of AWS resources for which
    # AWS Config records configuration changes (for example, `AWS::EC2::Instance`
    # or `AWS::CloudTrail::Trail`).

    # Before you can set this option to `true`, you must set the `allSupported`
    # option to `false`.

    # If you set this option to `true`, when AWS Config adds support for a new
    # type of resource, it will not record resources of that type unless you
    # manually add that type to your recording group.

    # For a list of valid `resourceTypes` values, see the **resourceType Value**
    # column in [Supported AWS Resource
    # Types](http://docs.aws.amazon.com/config/latest/developerguide/resource-
    # config-reference.html#supported-resources).
    resource_types: typing.List["ResourceType"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Relationship(autoboto.ShapeBase):
    """
    The relationship of the related resource to the main resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "resource_id",
                "resourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_name",
                "resourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "relationship_name",
                "relationshipName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The resource type of the related resource.
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the related resource (for example, `sg-xxxxxx`).
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The custom name of the related resource, if available.
    resource_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of relationship with the related resource.
    relationship_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceCount(autoboto.ShapeBase):
    """
    An object that contains the resource type and the number of resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "count",
                "count",
                autoboto.TypeInfo(int),
            ),
        ]

    # The resource type (for example, `"AWS::EC2::Instance"`).
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of resources.
    count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceIdentifier(autoboto.ShapeBase):
    """
    The details that identify a resource that is discovered by AWS Config, including
    the resource type, ID, and (if available) the custom resource name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "resource_id",
                "resourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_name",
                "resourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_deletion_time",
                "resourceDeletionTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The type of resource.
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the resource (for example, `sg-xxxxxx`).
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The custom name of the resource (if available).
    resource_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time that the resource was deleted.
    resource_deletion_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceInUseException(autoboto.ShapeBase):
    """
    The rule is currently being deleted or the rule is deleting your evaluation
    results. Try your request again later.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResourceKey(autoboto.ShapeBase):
    """
    The details that identify a resource within AWS Config, including the resource
    type and resource ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "resource_id",
                "resourceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The resource type.
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the resource (for example., sg-xxxxxx).
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotDiscoveredException(autoboto.ShapeBase):
    """
    You have specified a resource that is either unknown or has not been discovered.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class ResourceType(Enum):
    AWS__EC2__CustomerGateway = "AWS::EC2::CustomerGateway"
    AWS__EC2__EIP = "AWS::EC2::EIP"
    AWS__EC2__Host = "AWS::EC2::Host"
    AWS__EC2__Instance = "AWS::EC2::Instance"
    AWS__EC2__InternetGateway = "AWS::EC2::InternetGateway"
    AWS__EC2__NetworkAcl = "AWS::EC2::NetworkAcl"
    AWS__EC2__NetworkInterface = "AWS::EC2::NetworkInterface"
    AWS__EC2__RouteTable = "AWS::EC2::RouteTable"
    AWS__EC2__SecurityGroup = "AWS::EC2::SecurityGroup"
    AWS__EC2__Subnet = "AWS::EC2::Subnet"
    AWS__CloudTrail__Trail = "AWS::CloudTrail::Trail"
    AWS__EC2__Volume = "AWS::EC2::Volume"
    AWS__EC2__VPC = "AWS::EC2::VPC"
    AWS__EC2__VPNConnection = "AWS::EC2::VPNConnection"
    AWS__EC2__VPNGateway = "AWS::EC2::VPNGateway"
    AWS__IAM__Group = "AWS::IAM::Group"
    AWS__IAM__Policy = "AWS::IAM::Policy"
    AWS__IAM__Role = "AWS::IAM::Role"
    AWS__IAM__User = "AWS::IAM::User"
    AWS__ACM__Certificate = "AWS::ACM::Certificate"
    AWS__RDS__DBInstance = "AWS::RDS::DBInstance"
    AWS__RDS__DBSubnetGroup = "AWS::RDS::DBSubnetGroup"
    AWS__RDS__DBSecurityGroup = "AWS::RDS::DBSecurityGroup"
    AWS__RDS__DBSnapshot = "AWS::RDS::DBSnapshot"
    AWS__RDS__EventSubscription = "AWS::RDS::EventSubscription"
    AWS__ElasticLoadBalancingV2__LoadBalancer = "AWS::ElasticLoadBalancingV2::LoadBalancer"
    AWS__S3__Bucket = "AWS::S3::Bucket"
    AWS__SSM__ManagedInstanceInventory = "AWS::SSM::ManagedInstanceInventory"
    AWS__Redshift__Cluster = "AWS::Redshift::Cluster"
    AWS__Redshift__ClusterSnapshot = "AWS::Redshift::ClusterSnapshot"
    AWS__Redshift__ClusterParameterGroup = "AWS::Redshift::ClusterParameterGroup"
    AWS__Redshift__ClusterSecurityGroup = "AWS::Redshift::ClusterSecurityGroup"
    AWS__Redshift__ClusterSubnetGroup = "AWS::Redshift::ClusterSubnetGroup"
    AWS__Redshift__EventSubscription = "AWS::Redshift::EventSubscription"
    AWS__CloudWatch__Alarm = "AWS::CloudWatch::Alarm"
    AWS__CloudFormation__Stack = "AWS::CloudFormation::Stack"
    AWS__DynamoDB__Table = "AWS::DynamoDB::Table"
    AWS__AutoScaling__AutoScalingGroup = "AWS::AutoScaling::AutoScalingGroup"
    AWS__AutoScaling__LaunchConfiguration = "AWS::AutoScaling::LaunchConfiguration"
    AWS__AutoScaling__ScalingPolicy = "AWS::AutoScaling::ScalingPolicy"
    AWS__AutoScaling__ScheduledAction = "AWS::AutoScaling::ScheduledAction"
    AWS__CodeBuild__Project = "AWS::CodeBuild::Project"
    AWS__WAF__RateBasedRule = "AWS::WAF::RateBasedRule"
    AWS__WAF__Rule = "AWS::WAF::Rule"
    AWS__WAF__WebACL = "AWS::WAF::WebACL"
    AWS__WAFRegional__RateBasedRule = "AWS::WAFRegional::RateBasedRule"
    AWS__WAFRegional__Rule = "AWS::WAFRegional::Rule"
    AWS__WAFRegional__WebACL = "AWS::WAFRegional::WebACL"
    AWS__CloudFront__Distribution = "AWS::CloudFront::Distribution"
    AWS__CloudFront__StreamingDistribution = "AWS::CloudFront::StreamingDistribution"
    AWS__WAF__RuleGroup = "AWS::WAF::RuleGroup"
    AWS__WAFRegional__RuleGroup = "AWS::WAFRegional::RuleGroup"
    AWS__Lambda__Function = "AWS::Lambda::Function"
    AWS__ElasticBeanstalk__Application = "AWS::ElasticBeanstalk::Application"
    AWS__ElasticBeanstalk__ApplicationVersion = "AWS::ElasticBeanstalk::ApplicationVersion"
    AWS__ElasticBeanstalk__Environment = "AWS::ElasticBeanstalk::Environment"
    AWS__ElasticLoadBalancing__LoadBalancer = "AWS::ElasticLoadBalancing::LoadBalancer"
    AWS__XRay__EncryptionConfig = "AWS::XRay::EncryptionConfig"


@dataclasses.dataclass
class RetentionConfiguration(autoboto.ShapeBase):
    """
    An object with the name of the retention configuration and the retention period
    in days. The object stores the configuration for data retention in AWS Config.
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
                "retention_period_in_days",
                "RetentionPeriodInDays",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the retention configuration object.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Number of days AWS Config stores your historical information.

    # Currently, only applicable to the configuration item history.
    retention_period_in_days: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Scope(autoboto.ShapeBase):
    """
    Defines which resources trigger an evaluation for an AWS Config rule. The scope
    can include one or more resource types, a combination of a tag key and value, or
    a combination of one resource type and one resource ID. Specify a scope to
    constrain which resources trigger an evaluation for a rule. Otherwise,
    evaluations for the rule are triggered when any resource in your recording group
    changes in configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compliance_resource_types",
                "ComplianceResourceTypes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "tag_key",
                "TagKey",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_value",
                "TagValue",
                autoboto.TypeInfo(str),
            ),
            (
                "compliance_resource_id",
                "ComplianceResourceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The resource types of only those AWS resources that you want to trigger an
    # evaluation for the rule. You can only specify one type if you also specify
    # a resource ID for `ComplianceResourceId`.
    compliance_resource_types: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The tag key that is applied to only those AWS resources that you want to
    # trigger an evaluation for the rule.
    tag_key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tag value applied to only those AWS resources that you want to trigger
    # an evaluation for the rule. If you specify a value for `TagValue`, you must
    # also specify a value for `TagKey`.
    tag_value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the only AWS resource that you want to trigger an evaluation for
    # the rule. If you specify a resource ID, you must specify one resource type
    # for `ComplianceResourceTypes`.
    compliance_resource_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Source(autoboto.ShapeBase):
    """
    Provides the AWS Config rule owner (AWS or customer), the rule identifier, and
    the events that trigger the evaluation of your AWS resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(Owner),
            ),
            (
                "source_identifier",
                "SourceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "source_details",
                "SourceDetails",
                autoboto.TypeInfo(typing.List[SourceDetail]),
            ),
        ]

    # Indicates whether AWS or the customer owns and manages the AWS Config rule.
    owner: "Owner" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # For AWS Config managed rules, a predefined identifier from a list. For
    # example, `IAM_PASSWORD_POLICY` is a managed rule. To reference a managed
    # rule, see [Using AWS Managed Config
    # Rules](http://docs.aws.amazon.com/config/latest/developerguide/evaluate-
    # config_use-managed-rules.html).

    # For custom rules, the identifier is the Amazon Resource Name (ARN) of the
    # rule's AWS Lambda function, such as `arn:aws:lambda:us-
    # east-2:123456789012:function:custom_rule_name`.
    source_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides the source and type of the event that causes AWS Config to
    # evaluate your AWS resources.
    source_details: typing.List["SourceDetail"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class SourceDetail(autoboto.ShapeBase):
    """
    Provides the source and the message types that trigger AWS Config to evaluate
    your AWS resources against a rule. It also provides the frequency with which you
    want AWS Config to run evaluations for the rule if the trigger type is periodic.
    You can specify the parameter values for `SourceDetail` only for custom rules.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_source",
                "EventSource",
                autoboto.TypeInfo(EventSource),
            ),
            (
                "message_type",
                "MessageType",
                autoboto.TypeInfo(MessageType),
            ),
            (
                "maximum_execution_frequency",
                "MaximumExecutionFrequency",
                autoboto.TypeInfo(MaximumExecutionFrequency),
            ),
        ]

    # The source of the event, such as an AWS service, that triggers AWS Config
    # to evaluate your AWS resources.
    event_source: "EventSource" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of notification that triggers AWS Config to run an evaluation for
    # a rule. You can specify the following notification types:

    #   * `ConfigurationItemChangeNotification` \- Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change.

    #   * `OversizedConfigurationItemChangeNotification` \- Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.

    #   * `ScheduledNotification` \- Triggers a periodic evaluation at the frequency specified for `MaximumExecutionFrequency`.

    #   * `ConfigurationSnapshotDeliveryCompleted` \- Triggers a periodic evaluation when AWS Config delivers a configuration snapshot.

    # If you want your custom rule to be triggered by configuration changes,
    # specify two SourceDetail objects, one for
    # `ConfigurationItemChangeNotification` and one for
    # `OversizedConfigurationItemChangeNotification`.
    message_type: "MessageType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The frequency at which you want AWS Config to run evaluations for a custom
    # rule with a periodic trigger. If you specify a value for
    # `MaximumExecutionFrequency`, then `MessageType` must use the
    # `ScheduledNotification` value.

    # By default, rules with a periodic trigger are evaluated every 24 hours. To
    # change the frequency, specify a valid value for the
    # `MaximumExecutionFrequency` parameter.

    # Based on the valid value you choose, AWS Config runs evaluations once for
    # each valid value. For example, if you choose `Three_Hours`, AWS Config runs
    # evaluations once every three hours. In this case, `Three_Hours` is the
    # frequency of this rule.
    maximum_execution_frequency: "MaximumExecutionFrequency" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartConfigRulesEvaluationRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "config_rule_names",
                "ConfigRuleNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The list of names of AWS Config rules that you want to run evaluations for.
    config_rule_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class StartConfigRulesEvaluationResponse(autoboto.OutputShapeBase):
    """
    The output when you start the evaluation for the specified AWS Config rule.
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
class StartConfigurationRecorderRequest(autoboto.ShapeBase):
    """
    The input for the StartConfigurationRecorder action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_recorder_name",
                "ConfigurationRecorderName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the recorder object that records each configuration change made
    # to the resources.
    configuration_recorder_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopConfigurationRecorderRequest(autoboto.ShapeBase):
    """
    The input for the StopConfigurationRecorder action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_recorder_name",
                "ConfigurationRecorderName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the recorder object that records each configuration change made
    # to the resources.
    configuration_recorder_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ValidationException(autoboto.ShapeBase):
    """
    The requested action is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []
