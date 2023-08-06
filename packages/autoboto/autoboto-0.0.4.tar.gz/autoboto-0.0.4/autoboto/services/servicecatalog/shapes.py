import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AcceptPortfolioShareInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AcceptPortfolioShareOutput(autoboto.OutputShapeBase):
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
class AccessLevelFilter(autoboto.ShapeBase):
    """
    The access level to use to filter results.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(AccessLevelFilterKey),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
        ]

    # The access level.

    #   * `Account` \- Filter results based on the account.

    #   * `Role` \- Filter results based on the federated role of the specified user.

    #   * `User` \- Filter results based on the specified user.
    key: "AccessLevelFilterKey" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The user to which the access level applies. The only supported value is
    # `Self`.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class AccessLevelFilterKey(Enum):
    Account = "Account"
    Role = "Role"
    User = "User"


@dataclasses.dataclass
class AssociatePrincipalWithPortfolioInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                autoboto.TypeInfo(str),
            ),
            (
                "principal_arn",
                "PrincipalARN",
                autoboto.TypeInfo(str),
            ),
            (
                "principal_type",
                "PrincipalType",
                autoboto.TypeInfo(PrincipalType),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the principal (IAM user, role, or group).
    principal_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The principal type. The supported value is `IAM`.
    principal_type: "PrincipalType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociatePrincipalWithPortfolioOutput(autoboto.OutputShapeBase):
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
class AssociateProductWithPortfolioInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "portfolio_id",
                "PortfolioId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "source_portfolio_id",
                "SourcePortfolioId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the source portfolio.
    source_portfolio_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociateProductWithPortfolioOutput(autoboto.OutputShapeBase):
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
class AssociateTagOptionWithResourceInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_option_id",
                "TagOptionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The resource identifier.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The TagOption identifier.
    tag_option_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateTagOptionWithResourceOutput(autoboto.OutputShapeBase):
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


class ChangeAction(Enum):
    ADD = "ADD"
    MODIFY = "MODIFY"
    REMOVE = "REMOVE"


@dataclasses.dataclass
class CloudWatchDashboard(autoboto.ShapeBase):
    """
    Information about a CloudWatch dashboard.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the CloudWatch dashboard.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConstraintDetail(autoboto.ShapeBase):
    """
    Information about a constraint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "constraint_id",
                "ConstraintId",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier of the constraint.
    constraint_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of constraint.

    #   * `LAUNCH`

    #   * `NOTIFICATION`

    #   * `TEMPLATE`
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the constraint.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The owner of the constraint.
    owner: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConstraintSummary(autoboto.ShapeBase):
    """
    Summary information about a constraint.
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
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of constraint.

    #   * `LAUNCH`

    #   * `NOTIFICATION`

    #   * `TEMPLATE`
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the constraint.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class CopyOption(Enum):
    CopyTags = "CopyTags"


@dataclasses.dataclass
class CopyProductInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_product_arn",
                "SourceProductArn",
                autoboto.TypeInfo(str),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "target_product_id",
                "TargetProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "target_product_name",
                "TargetProductName",
                autoboto.TypeInfo(str),
            ),
            (
                "source_provisioning_artifact_identifiers",
                "SourceProvisioningArtifactIdentifiers",
                autoboto.TypeInfo(
                    typing.List[typing.Dict[ProvisioningArtifactPropertyName,
                                            str]]
                ),
            ),
            (
                "copy_options",
                "CopyOptions",
                autoboto.TypeInfo(typing.List[CopyOption]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the source product.
    source_product_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the target product. By default, a new product is created.
    target_product_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A name for the target product. The default is the name of the source
    # product.
    target_product_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifiers of the provisioning artifacts (also known as versions) of
    # the product to copy. By default, all provisioning artifacts are copied.
    source_provisioning_artifact_identifiers: typing.List[
        typing.Dict["ProvisioningArtifactPropertyName", str]
    ] = dataclasses.field(
        default_factory=list,
    )

    # The copy options. If the value is `CopyTags`, the tags from the source
    # product are copied to the target product.
    copy_options: typing.List["CopyOption"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CopyProductOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "copy_product_token",
                "CopyProductToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The token to use to track the progress of the operation.
    copy_product_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class CopyProductStatus(Enum):
    SUCCEEDED = "SUCCEEDED"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"


@dataclasses.dataclass
class CreateConstraintInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                autoboto.TypeInfo(str),
            ),
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The constraint parameters, in JSON format. The syntax depends on the
    # constraint type as follows:

    # LAUNCH

    # Specify the `RoleArn` property as follows:

    # \"RoleArn\" : \"arn:aws:iam::123456789012:role/LaunchRole\"

    # NOTIFICATION

    # Specify the `NotificationArns` property as follows:

    # \"NotificationArns\" : [\"arn:aws:sns:us-east-1:123456789012:Topic\"]

    # TEMPLATE

    # Specify the `Rules` property. For more information, see [Template
    # Constraint
    # Rules](http://docs.aws.amazon.com/servicecatalog/latest/adminguide/reference-
    # template_constraint_rules.html).
    parameters: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of constraint.

    #   * `LAUNCH`

    #   * `NOTIFICATION`

    #   * `TEMPLATE`
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description of the constraint.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateConstraintOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "constraint_detail",
                "ConstraintDetail",
                autoboto.TypeInfo(ConstraintDetail),
            ),
            (
                "constraint_parameters",
                "ConstraintParameters",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(Status),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the constraint.
    constraint_detail: "ConstraintDetail" = dataclasses.field(
        default_factory=dict,
    )

    # The constraint parameters.
    constraint_parameters: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the current request.
    status: "Status" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePortfolioInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_name",
                "ProviderName",
                autoboto.TypeInfo(str),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name to use for display purposes.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the portfolio provider.
    provider_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description of the portfolio.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more tags.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreatePortfolioOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "portfolio_detail",
                "PortfolioDetail",
                autoboto.TypeInfo(PortfolioDetail),
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

    # Information about the portfolio.
    portfolio_detail: "PortfolioDetail" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the tags associated with the portfolio.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreatePortfolioShareInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                autoboto.TypeInfo(str),
            ),
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The AWS account ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePortfolioShareOutput(autoboto.OutputShapeBase):
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
class CreateProductInput(autoboto.ShapeBase):
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
                "product_type",
                "ProductType",
                autoboto.TypeInfo(ProductType),
            ),
            (
                "provisioning_artifact_parameters",
                "ProvisioningArtifactParameters",
                autoboto.TypeInfo(ProvisioningArtifactProperties),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "distributor",
                "Distributor",
                autoboto.TypeInfo(str),
            ),
            (
                "support_description",
                "SupportDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "support_email",
                "SupportEmail",
                autoboto.TypeInfo(str),
            ),
            (
                "support_url",
                "SupportUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the product.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The owner of the product.
    owner: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of product.
    product_type: "ProductType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The configuration of the provisioning artifact.
    provisioning_artifact_parameters: "ProvisioningArtifactProperties" = dataclasses.field(
        default_factory=dict,
    )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description of the product.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The distributor of the product.
    distributor: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The support information about the product.
    support_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The contact email for product support.
    support_email: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The contact URL for product support.
    support_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more tags.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateProductOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "product_view_detail",
                "ProductViewDetail",
                autoboto.TypeInfo(ProductViewDetail),
            ),
            (
                "provisioning_artifact_detail",
                "ProvisioningArtifactDetail",
                autoboto.TypeInfo(ProvisioningArtifactDetail),
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

    # Information about the product view.
    product_view_detail: "ProductViewDetail" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the provisioning artifact.
    provisioning_artifact_detail: "ProvisioningArtifactDetail" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the tags associated with the product.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateProvisionedProductPlanInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "plan_name",
                "PlanName",
                autoboto.TypeInfo(str),
            ),
            (
                "plan_type",
                "PlanType",
                autoboto.TypeInfo(ProvisionedProductPlanType),
            ),
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioned_product_name",
                "ProvisionedProductName",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                autoboto.TypeInfo(str),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "notification_arns",
                "NotificationArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "path_id",
                "PathId",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioning_parameters",
                "ProvisioningParameters",
                autoboto.TypeInfo(typing.List[UpdateProvisioningParameter]),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the plan.
    plan_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The plan type.
    plan_type: "ProvisionedProductPlanType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A user-friendly name for the provisioned product. This value must be unique
    # for the AWS account and cannot be updated after the product is provisioned.
    provisioned_product_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Passed to CloudFormation. The SNS topic ARNs to which to publish stack-
    # related events.
    notification_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The path identifier of the product. This value is optional if the product
    # has a default path, and required if the product has more than one path. To
    # list the paths for a product, use ListLaunchPaths.
    path_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Parameters specified by the administrator that are required for
    # provisioning the product.
    provisioning_parameters: typing.List["UpdateProvisioningParameter"
                                        ] = dataclasses.field(
                                            default_factory=list,
                                        )

    # One or more tags.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateProvisionedProductPlanOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "plan_name",
                "PlanName",
                autoboto.TypeInfo(str),
            ),
            (
                "plan_id",
                "PlanId",
                autoboto.TypeInfo(str),
            ),
            (
                "provision_product_id",
                "ProvisionProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioned_product_name",
                "ProvisionedProductName",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the plan.
    plan_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The plan identifier.
    plan_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The product identifier.
    provision_product_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The user-friendly name of the provisioned product.
    provisioned_product_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateProvisioningArtifactInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(ProvisioningArtifactProperties),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The configuration for the provisioning artifact.
    parameters: "ProvisioningArtifactProperties" = dataclasses.field(
        default_factory=dict,
    )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateProvisioningArtifactOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioning_artifact_detail",
                "ProvisioningArtifactDetail",
                autoboto.TypeInfo(ProvisioningArtifactDetail),
            ),
            (
                "info",
                "Info",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(Status),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the provisioning artifact.
    provisioning_artifact_detail: "ProvisioningArtifactDetail" = dataclasses.field(
        default_factory=dict,
    )

    # The URL of the CloudFormation template in Amazon S3, in JSON format.
    info: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the current request.
    status: "Status" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTagOptionInput(autoboto.ShapeBase):
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

    # The TagOption key.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The TagOption value.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTagOptionOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tag_option_detail",
                "TagOptionDetail",
                autoboto.TypeInfo(TagOptionDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the TagOption.
    tag_option_detail: "TagOptionDetail" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteConstraintInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier of the constraint.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteConstraintOutput(autoboto.OutputShapeBase):
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
class DeletePortfolioInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeletePortfolioOutput(autoboto.OutputShapeBase):
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
class DeletePortfolioShareInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                autoboto.TypeInfo(str),
            ),
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The AWS account ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeletePortfolioShareOutput(autoboto.OutputShapeBase):
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
class DeleteProductInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The product identifier.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteProductOutput(autoboto.OutputShapeBase):
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
class DeleteProvisionedProductPlanInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "plan_id",
                "PlanId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "ignore_errors",
                "IgnoreErrors",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The plan identifier.
    plan_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If set to true, AWS Service Catalog stops managing the specified
    # provisioned product even if it cannot delete the underlying resources.
    ignore_errors: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteProvisionedProductPlanOutput(autoboto.OutputShapeBase):
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
class DeleteProvisioningArtifactInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteProvisioningArtifactOutput(autoboto.OutputShapeBase):
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
class DeleteTagOptionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The TagOption identifier.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTagOptionOutput(autoboto.OutputShapeBase):
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
class DescribeConstraintInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier of the constraint.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeConstraintOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "constraint_detail",
                "ConstraintDetail",
                autoboto.TypeInfo(ConstraintDetail),
            ),
            (
                "constraint_parameters",
                "ConstraintParameters",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(Status),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the constraint.
    constraint_detail: "ConstraintDetail" = dataclasses.field(
        default_factory=dict,
    )

    # The constraint parameters.
    constraint_parameters: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the current request.
    status: "Status" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCopyProductStatusInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "copy_product_token",
                "CopyProductToken",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The token for the copy product operation. This token is returned by
    # CopyProduct.
    copy_product_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeCopyProductStatusOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "copy_product_status",
                "CopyProductStatus",
                autoboto.TypeInfo(CopyProductStatus),
            ),
            (
                "target_product_id",
                "TargetProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "status_detail",
                "StatusDetail",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the copy product operation.
    copy_product_status: "CopyProductStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the copied product.
    target_product_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status message.
    status_detail: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePortfolioInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribePortfolioOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "portfolio_detail",
                "PortfolioDetail",
                autoboto.TypeInfo(PortfolioDetail),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "tag_options",
                "TagOptions",
                autoboto.TypeInfo(typing.List[TagOptionDetail]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the portfolio.
    portfolio_detail: "PortfolioDetail" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the tags associated with the portfolio.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # Information about the TagOptions associated with the portfolio.
    tag_options: typing.List["TagOptionDetail"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeProductAsAdminInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The product identifier.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeProductAsAdminOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "product_view_detail",
                "ProductViewDetail",
                autoboto.TypeInfo(ProductViewDetail),
            ),
            (
                "provisioning_artifact_summaries",
                "ProvisioningArtifactSummaries",
                autoboto.TypeInfo(typing.List[ProvisioningArtifactSummary]),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "tag_options",
                "TagOptions",
                autoboto.TypeInfo(typing.List[TagOptionDetail]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the product view.
    product_view_detail: "ProductViewDetail" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the provisioning artifacts (also known as versions) for
    # the specified product.
    provisioning_artifact_summaries: typing.List["ProvisioningArtifactSummary"
                                                ] = dataclasses.field(
                                                    default_factory=list,
                                                )

    # Information about the tags associated with the product.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # Information about the TagOptions associated with the product.
    tag_options: typing.List["TagOptionDetail"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeProductInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The product identifier.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeProductOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "product_view_summary",
                "ProductViewSummary",
                autoboto.TypeInfo(ProductViewSummary),
            ),
            (
                "provisioning_artifacts",
                "ProvisioningArtifacts",
                autoboto.TypeInfo(typing.List[ProvisioningArtifact]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Summary information about the product view.
    product_view_summary: "ProductViewSummary" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the provisioning artifacts for the specified product.
    provisioning_artifacts: typing.List["ProvisioningArtifact"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )


@dataclasses.dataclass
class DescribeProductViewInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The product view identifier.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeProductViewOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "product_view_summary",
                "ProductViewSummary",
                autoboto.TypeInfo(ProductViewSummary),
            ),
            (
                "provisioning_artifacts",
                "ProvisioningArtifacts",
                autoboto.TypeInfo(typing.List[ProvisioningArtifact]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Summary information about the product.
    product_view_summary: "ProductViewSummary" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the provisioning artifacts for the product.
    provisioning_artifacts: typing.List["ProvisioningArtifact"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )


@dataclasses.dataclass
class DescribeProvisionedProductInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The provisioned product identifier.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeProvisionedProductOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioned_product_detail",
                "ProvisionedProductDetail",
                autoboto.TypeInfo(ProvisionedProductDetail),
            ),
            (
                "cloud_watch_dashboards",
                "CloudWatchDashboards",
                autoboto.TypeInfo(typing.List[CloudWatchDashboard]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the provisioned product.
    provisioned_product_detail: "ProvisionedProductDetail" = dataclasses.field(
        default_factory=dict,
    )

    # Any CloudWatch dashboards that were created when provisioning the product.
    cloud_watch_dashboards: typing.List["CloudWatchDashboard"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )


@dataclasses.dataclass
class DescribeProvisionedProductPlanInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "plan_id",
                "PlanId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The plan identifier.
    plan_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProvisionedProductPlanOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioned_product_plan_details",
                "ProvisionedProductPlanDetails",
                autoboto.TypeInfo(ProvisionedProductPlanDetails),
            ),
            (
                "resource_changes",
                "ResourceChanges",
                autoboto.TypeInfo(typing.List[ResourceChange]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the plan.
    provisioned_product_plan_details: "ProvisionedProductPlanDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the resource changes that will occur when the plan is
    # executed.
    resource_changes: typing.List["ResourceChange"] = dataclasses.field(
        default_factory=list,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeProvisioningArtifactInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                autoboto.TypeInfo(str),
            ),
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "verbose",
                "Verbose",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether a verbose level of detail is enabled.
    verbose: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProvisioningArtifactOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioning_artifact_detail",
                "ProvisioningArtifactDetail",
                autoboto.TypeInfo(ProvisioningArtifactDetail),
            ),
            (
                "info",
                "Info",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(Status),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the provisioning artifact.
    provisioning_artifact_detail: "ProvisioningArtifactDetail" = dataclasses.field(
        default_factory=dict,
    )

    # The URL of the CloudFormation template in Amazon S3.
    info: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the current request.
    status: "Status" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProvisioningParametersInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "path_id",
                "PathId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The path identifier of the product. This value is optional if the product
    # has a default path, and required if the product has more than one path. To
    # list the paths for a product, use ListLaunchPaths.
    path_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProvisioningParametersOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioning_artifact_parameters",
                "ProvisioningArtifactParameters",
                autoboto.TypeInfo(typing.List[ProvisioningArtifactParameter]),
            ),
            (
                "constraint_summaries",
                "ConstraintSummaries",
                autoboto.TypeInfo(typing.List[ConstraintSummary]),
            ),
            (
                "usage_instructions",
                "UsageInstructions",
                autoboto.TypeInfo(typing.List[UsageInstruction]),
            ),
            (
                "tag_options",
                "TagOptions",
                autoboto.TypeInfo(typing.List[TagOptionSummary]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the parameters used to provision the product.
    provisioning_artifact_parameters: typing.List[
        "ProvisioningArtifactParameter"
    ] = dataclasses.field(
        default_factory=list,
    )

    # Information about the constraints used to provision the product.
    constraint_summaries: typing.List["ConstraintSummary"] = dataclasses.field(
        default_factory=list,
    )

    # Any additional metadata specifically related to the provisioning of the
    # product. For example, see the `Version` field of the CloudFormation
    # template.
    usage_instructions: typing.List["UsageInstruction"] = dataclasses.field(
        default_factory=list,
    )

    # Information about the TagOptions associated with the resource.
    tag_options: typing.List["TagOptionSummary"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeRecordInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
        ]

    # The record identifier of the provisioned product. This identifier is
    # returned by the request operation.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRecordOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "record_detail",
                "RecordDetail",
                autoboto.TypeInfo(RecordDetail),
            ),
            (
                "record_outputs",
                "RecordOutputs",
                autoboto.TypeInfo(typing.List[RecordOutput]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the product.
    record_detail: "RecordDetail" = dataclasses.field(default_factory=dict, )

    # Information about the product created as the result of a request. For
    # example, the output for a CloudFormation-backed product that creates an S3
    # bucket would include the S3 bucket URL.
    record_outputs: typing.List["RecordOutput"] = dataclasses.field(
        default_factory=list,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTagOptionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The TagOption identifier.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTagOptionOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tag_option_detail",
                "TagOptionDetail",
                autoboto.TypeInfo(TagOptionDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the TagOption.
    tag_option_detail: "TagOptionDetail" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DisassociatePrincipalFromPortfolioInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                autoboto.TypeInfo(str),
            ),
            (
                "principal_arn",
                "PrincipalARN",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the principal (IAM user, role, or group).
    principal_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociatePrincipalFromPortfolioOutput(autoboto.OutputShapeBase):
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
class DisassociateProductFromPortfolioInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "portfolio_id",
                "PortfolioId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateProductFromPortfolioOutput(autoboto.OutputShapeBase):
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
class DisassociateTagOptionFromResourceInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_option_id",
                "TagOptionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The resource identifier.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The TagOption identifier.
    tag_option_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateTagOptionFromResourceOutput(autoboto.OutputShapeBase):
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
class DuplicateResourceException(autoboto.ShapeBase):
    """
    The specified resource is a duplicate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class EvaluationType(Enum):
    STATIC = "STATIC"
    DYNAMIC = "DYNAMIC"


@dataclasses.dataclass
class ExecuteProvisionedProductPlanInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "plan_id",
                "PlanId",
                autoboto.TypeInfo(str),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The plan identifier.
    plan_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ExecuteProvisionedProductPlanOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "record_detail",
                "RecordDetail",
                autoboto.TypeInfo(RecordDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the result of provisioning the product.
    record_detail: "RecordDetail" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class InvalidParametersException(autoboto.ShapeBase):
    """
    One or more parameters provided to the operation are not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidStateException(autoboto.ShapeBase):
    """
    An attempt was made to modify a resource that is in a state that is not valid.
    Check your resources to ensure that they are in valid states before retrying the
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LaunchPathSummary(autoboto.ShapeBase):
    """
    Summary information about a product path for a user.
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
                "constraint_summaries",
                "ConstraintSummaries",
                autoboto.TypeInfo(typing.List[ConstraintSummary]),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier of the product path.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The constraints on the portfolio-product relationship.
    constraint_summaries: typing.List["ConstraintSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The tags associated with this product path.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # The name of the portfolio to which the user was assigned.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    The current limits of the service would have been exceeded by this operation.
    Decrease your resource use or increase your service limits and retry the
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListAcceptedPortfolioSharesInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "portfolio_share_type",
                "PortfolioShareType",
                autoboto.TypeInfo(PortfolioShareType),
            ),
        ]

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of shared portfolios to list. The default is to list imported
    # portfolios.

    #   * `AWS_SERVICECATALOG` \- List default portfolios

    #   * `IMPORTED` \- List imported portfolios
    portfolio_share_type: "PortfolioShareType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListAcceptedPortfolioSharesOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "portfolio_details",
                "PortfolioDetails",
                autoboto.TypeInfo(typing.List[PortfolioDetail]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the portfolios.
    portfolio_details: typing.List["PortfolioDetail"] = dataclasses.field(
        default_factory=list,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListConstraintsForPortfolioInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListConstraintsForPortfolioOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "constraint_details",
                "ConstraintDetails",
                autoboto.TypeInfo(typing.List[ConstraintDetail]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the constraints.
    constraint_details: typing.List["ConstraintDetail"] = dataclasses.field(
        default_factory=list,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListLaunchPathsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListLaunchPathsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "launch_path_summaries",
                "LaunchPathSummaries",
                autoboto.TypeInfo(typing.List[LaunchPathSummary]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the launch path.
    launch_path_summaries: typing.List["LaunchPathSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListPortfolioAccessInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListPortfolioAccessOutput(autoboto.OutputShapeBase):
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
            (
                "next_page_token",
                "NextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the AWS accounts with access to the portfolio.
    account_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListPortfoliosForProductInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPortfoliosForProductOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "portfolio_details",
                "PortfolioDetails",
                autoboto.TypeInfo(typing.List[PortfolioDetail]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the portfolios.
    portfolio_details: typing.List["PortfolioDetail"] = dataclasses.field(
        default_factory=list,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListPortfoliosInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
        ]

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPortfoliosOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "portfolio_details",
                "PortfolioDetails",
                autoboto.TypeInfo(typing.List[PortfolioDetail]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the portfolios.
    portfolio_details: typing.List["PortfolioDetail"] = dataclasses.field(
        default_factory=list,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListPrincipalsForPortfolioInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPrincipalsForPortfolioOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "principals",
                "Principals",
                autoboto.TypeInfo(typing.List[Principal]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The IAM principals (users or roles) associated with the portfolio.
    principals: typing.List["Principal"] = dataclasses.field(
        default_factory=list,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListProvisionedProductPlansInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "provision_product_id",
                "ProvisionProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
            (
                "access_level_filter",
                "AccessLevelFilter",
                autoboto.TypeInfo(AccessLevelFilter),
            ),
        ]

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The product identifier.
    provision_product_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The access level to use to obtain results. The default is `User`.
    access_level_filter: "AccessLevelFilter" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ListProvisionedProductPlansOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioned_product_plans",
                "ProvisionedProductPlans",
                autoboto.TypeInfo(typing.List[ProvisionedProductPlanSummary]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the plans.
    provisioned_product_plans: typing.List["ProvisionedProductPlanSummary"
                                          ] = dataclasses.field(
                                              default_factory=list,
                                          )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListProvisioningArtifactsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListProvisioningArtifactsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioning_artifact_details",
                "ProvisioningArtifactDetails",
                autoboto.TypeInfo(typing.List[ProvisioningArtifactDetail]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the provisioning artifacts.
    provisioning_artifact_details: typing.List["ProvisioningArtifactDetail"
                                              ] = dataclasses.field(
                                                  default_factory=list,
                                              )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListRecordHistoryInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "access_level_filter",
                "AccessLevelFilter",
                autoboto.TypeInfo(AccessLevelFilter),
            ),
            (
                "search_filter",
                "SearchFilter",
                autoboto.TypeInfo(ListRecordHistorySearchFilter),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The access level to use to obtain results. The default is `User`.
    access_level_filter: "AccessLevelFilter" = dataclasses.field(
        default_factory=dict,
    )

    # The search filter to scope the results.
    search_filter: "ListRecordHistorySearchFilter" = dataclasses.field(
        default_factory=dict,
    )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRecordHistoryOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "record_details",
                "RecordDetails",
                autoboto.TypeInfo(typing.List[RecordDetail]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The records, in reverse chronological order.
    record_details: typing.List["RecordDetail"] = dataclasses.field(
        default_factory=list,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListRecordHistorySearchFilter(autoboto.ShapeBase):
    """
    The search filter to use when listing history records.
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

    # The filter key.

    #   * `product` \- Filter results based on the specified product identifier.

    #   * `provisionedproduct` \- Filter results based on the provisioned product identifier.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The filter value.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourcesForTagOptionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_option_id",
                "TagOptionId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The TagOption identifier.
    tag_option_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The resource type.

    #   * `Portfolio`

    #   * `Product`
    resource_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourcesForTagOptionOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_details",
                "ResourceDetails",
                autoboto.TypeInfo(typing.List[ResourceDetail]),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the resources.
    resource_details: typing.List["ResourceDetail"] = dataclasses.field(
        default_factory=list,
    )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagOptionsFilters(autoboto.ShapeBase):
    """
    Filters to use when listing TagOptions.
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
                "active",
                "Active",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The TagOption key.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The TagOption value.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The active state.
    active: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagOptionsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(ListTagOptionsFilters),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The search filters. If no search filters are specified, the output includes
    # all TagOptions.
    filters: "ListTagOptionsFilters" = dataclasses.field(default_factory=dict, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagOptionsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tag_option_details",
                "TagOptionDetails",
                autoboto.TypeInfo(typing.List[TagOptionDetail]),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the TagOptions.
    tag_option_details: typing.List["TagOptionDetail"] = dataclasses.field(
        default_factory=list,
    )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ParameterConstraints(autoboto.ShapeBase):
    """
    The constraints that the administrator has put on the parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "allowed_values",
                "AllowedValues",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The values that the administrator has allowed for the parameter.
    allowed_values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class PortfolioDetail(autoboto.ShapeBase):
    """
    Information about a portfolio.
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
                "arn",
                "ARN",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "provider_name",
                "ProviderName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN assigned to the portfolio.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name to use for display purposes.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the portfolio.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the portfolio provider.
    provider_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class PortfolioShareType(Enum):
    IMPORTED = "IMPORTED"
    AWS_SERVICECATALOG = "AWS_SERVICECATALOG"


@dataclasses.dataclass
class Principal(autoboto.ShapeBase):
    """
    Information about a principal.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "principal_arn",
                "PrincipalARN",
                autoboto.TypeInfo(str),
            ),
            (
                "principal_type",
                "PrincipalType",
                autoboto.TypeInfo(PrincipalType),
            ),
        ]

    # The ARN of the principal (IAM user, role, or group).
    principal_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The principal type. The supported value is `IAM`.
    principal_type: "PrincipalType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class PrincipalType(Enum):
    IAM = "IAM"


class ProductSource(Enum):
    ACCOUNT = "ACCOUNT"


class ProductType(Enum):
    CLOUD_FORMATION_TEMPLATE = "CLOUD_FORMATION_TEMPLATE"
    MARKETPLACE = "MARKETPLACE"


@dataclasses.dataclass
class ProductViewAggregationValue(autoboto.ShapeBase):
    """
    A single product view aggregation value/count pair, containing metadata about
    each product to which the calling user has access.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
            (
                "approximate_count",
                "ApproximateCount",
                autoboto.TypeInfo(int),
            ),
        ]

    # The value of the product view aggregation.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An approximate count of the products that match the value.
    approximate_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ProductViewDetail(autoboto.ShapeBase):
    """
    Information about a product view.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_view_summary",
                "ProductViewSummary",
                autoboto.TypeInfo(ProductViewSummary),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(Status),
            ),
            (
                "product_arn",
                "ProductARN",
                autoboto.TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # Summary information about the product view.
    product_view_summary: "ProductViewSummary" = dataclasses.field(
        default_factory=dict,
    )

    # The status of the product.

    #   * `AVAILABLE` \- The product is ready for use.

    #   * `CREATING` \- Product creation has started; the product is not ready for use.

    #   * `FAILED` \- An action failed.
    status: "Status" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the product.
    product_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ProductViewFilterBy(Enum):
    FullTextSearch = "FullTextSearch"
    Owner = "Owner"
    ProductType = "ProductType"
    SourceProductId = "SourceProductId"


class ProductViewSortBy(Enum):
    Title = "Title"
    VersionCount = "VersionCount"
    CreationDate = "CreationDate"


@dataclasses.dataclass
class ProductViewSummary(autoboto.ShapeBase):
    """
    Summary information about a product view.
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
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
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
                "short_description",
                "ShortDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(ProductType),
            ),
            (
                "distributor",
                "Distributor",
                autoboto.TypeInfo(str),
            ),
            (
                "has_default_path",
                "HasDefaultPath",
                autoboto.TypeInfo(bool),
            ),
            (
                "support_email",
                "SupportEmail",
                autoboto.TypeInfo(str),
            ),
            (
                "support_description",
                "SupportDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "support_url",
                "SupportUrl",
                autoboto.TypeInfo(str),
            ),
        ]

    # The product view identifier.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the product.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The owner of the product. Contact the product administrator for the
    # significance of this value.
    owner: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Short description of the product.
    short_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The product type. Contact the product administrator for the significance of
    # this value. If this value is `MARKETPLACE`, the product was created by AWS
    # Marketplace.
    type: "ProductType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The distributor of the product. Contact the product administrator for the
    # significance of this value.
    distributor: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether the product has a default path. If the product does not
    # have a default path, call ListLaunchPaths to disambiguate between paths.
    # Otherwise, ListLaunchPaths is not required, and the output of
    # ProductViewSummary can be used directly with
    # DescribeProvisioningParameters.
    has_default_path: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The email contact information to obtain support for this Product.
    support_email: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the support for this Product.
    support_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL information to obtain support for this Product.
    support_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProvisionProductInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioned_product_name",
                "ProvisionedProductName",
                autoboto.TypeInfo(str),
            ),
            (
                "provision_token",
                "ProvisionToken",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "path_id",
                "PathId",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioning_parameters",
                "ProvisioningParameters",
                autoboto.TypeInfo(typing.List[ProvisioningParameter]),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "notification_arns",
                "NotificationArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A user-friendly name for the provisioned product. This value must be unique
    # for the AWS account and cannot be updated after the product is provisioned.
    provisioned_product_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An idempotency token that uniquely identifies the provisioning request.
    provision_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The path identifier of the product. This value is optional if the product
    # has a default path, and required if the product has more than one path. To
    # list the paths for a product, use ListLaunchPaths.
    path_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Parameters specified by the administrator that are required for
    # provisioning the product.
    provisioning_parameters: typing.List["ProvisioningParameter"
                                        ] = dataclasses.field(
                                            default_factory=list,
                                        )

    # One or more tags.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # Passed to CloudFormation. The SNS topic ARNs to which to publish stack-
    # related events.
    notification_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ProvisionProductOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "record_detail",
                "RecordDetail",
                autoboto.TypeInfo(RecordDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the result of provisioning the product.
    record_detail: "RecordDetail" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ProvisionedProductAttribute(autoboto.ShapeBase):
    """
    Information about a provisioned product.
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
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(ProvisionedProductStatus),
            ),
            (
                "status_message",
                "StatusMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                autoboto.TypeInfo(str),
            ),
            (
                "last_record_id",
                "LastRecordId",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "physical_id",
                "PhysicalId",
                autoboto.TypeInfo(str),
            ),
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_arn",
                "UserArn",
                autoboto.TypeInfo(str),
            ),
            (
                "user_arn_session",
                "UserArnSession",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user-friendly name of the provisioned product.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the provisioned product.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of provisioned product. The supported value is `CFN_STACK`.
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of the provisioned product.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The current status of the provisioned product.

    #   * `AVAILABLE` \- Stable state, ready to perform any operation. The most recent operation succeeded and completed.

    #   * `UNDER_CHANGE` \- Transitive state, operations performed might not have valid results. Wait for an `AVAILABLE` status before performing operations.

    #   * `TAINTED` \- Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.

    #   * `ERROR` \- An unexpected error occurred, the provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
    status: "ProvisionedProductStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The current status message of the provisioned product.
    status_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The record identifier of the last request performed on this provisioned
    # product.
    last_record_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # One or more tags.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # The assigned identifier for the resource, such as an EC2 instance ID or an
    # S3 bucket name.
    physical_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the IAM user.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the IAM user in the session. This ARN might contain a session
    # ID.
    user_arn_session: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ProvisionedProductDetail(autoboto.ShapeBase):
    """
    Information about a provisioned product.
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
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(ProvisionedProductStatus),
            ),
            (
                "status_message",
                "StatusMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                autoboto.TypeInfo(str),
            ),
            (
                "last_record_id",
                "LastRecordId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user-friendly name of the provisioned product.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the provisioned product.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of provisioned product. The supported value is `CFN_STACK`.
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of the provisioned product.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The current status of the provisioned product.

    #   * `AVAILABLE` \- Stable state, ready to perform any operation. The most recent operation succeeded and completed.

    #   * `UNDER_CHANGE` \- Transitive state, operations performed might not have valid results. Wait for an `AVAILABLE` status before performing operations.

    #   * `TAINTED` \- Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.

    #   * `ERROR` \- An unexpected error occurred, the provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
    status: "ProvisionedProductStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The current status message of the provisioned product.
    status_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A unique identifier that you provide to ensure idempotency. If multiple
    # requests differ only by the idempotency token, the same response is
    # returned for each repeated request.
    idempotency_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The record identifier of the last request performed on this provisioned
    # product.
    last_record_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ProvisionedProductPlanDetails(autoboto.ShapeBase):
    """
    Information about a plan.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "path_id",
                "PathId",
                autoboto.TypeInfo(str),
            ),
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "plan_name",
                "PlanName",
                autoboto.TypeInfo(str),
            ),
            (
                "plan_id",
                "PlanId",
                autoboto.TypeInfo(str),
            ),
            (
                "provision_product_id",
                "ProvisionProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "provision_product_name",
                "ProvisionProductName",
                autoboto.TypeInfo(str),
            ),
            (
                "plan_type",
                "PlanType",
                autoboto.TypeInfo(ProvisionedProductPlanType),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(ProvisionedProductPlanStatus),
            ),
            (
                "updated_time",
                "UpdatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "notification_arns",
                "NotificationArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "provisioning_parameters",
                "ProvisioningParameters",
                autoboto.TypeInfo(typing.List[UpdateProvisioningParameter]),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "status_message",
                "StatusMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The path identifier of the product. This value is optional if the product
    # has a default path, and required if the product has more than one path. To
    # list the paths for a product, use ListLaunchPaths.
    path_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the plan.
    plan_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The plan identifier.
    plan_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The product identifier.
    provision_product_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The user-friendly name of the provisioned product.
    provision_product_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The plan type.
    plan_type: "ProvisionedProductPlanType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status.
    status: "ProvisionedProductPlanStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time when the plan was last updated.
    updated_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Passed to CloudFormation. The SNS topic ARNs to which to publish stack-
    # related events.
    notification_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Parameters specified by the administrator that are required for
    # provisioning the product.
    provisioning_parameters: typing.List["UpdateProvisioningParameter"
                                        ] = dataclasses.field(
                                            default_factory=list,
                                        )

    # One or more tags.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # The status message.
    status_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ProvisionedProductPlanStatus(Enum):
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_SUCCESS = "CREATE_SUCCESS"
    CREATE_FAILED = "CREATE_FAILED"
    EXECUTE_IN_PROGRESS = "EXECUTE_IN_PROGRESS"
    EXECUTE_SUCCESS = "EXECUTE_SUCCESS"
    EXECUTE_FAILED = "EXECUTE_FAILED"


@dataclasses.dataclass
class ProvisionedProductPlanSummary(autoboto.ShapeBase):
    """
    Summary information about a plan.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "plan_name",
                "PlanName",
                autoboto.TypeInfo(str),
            ),
            (
                "plan_id",
                "PlanId",
                autoboto.TypeInfo(str),
            ),
            (
                "provision_product_id",
                "ProvisionProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "provision_product_name",
                "ProvisionProductName",
                autoboto.TypeInfo(str),
            ),
            (
                "plan_type",
                "PlanType",
                autoboto.TypeInfo(ProvisionedProductPlanType),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the plan.
    plan_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The plan identifier.
    plan_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The product identifier.
    provision_product_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The user-friendly name of the provisioned product.
    provision_product_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The plan type.
    plan_type: "ProvisionedProductPlanType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ProvisionedProductPlanType(Enum):
    CLOUDFORMATION = "CLOUDFORMATION"


class ProvisionedProductStatus(Enum):
    AVAILABLE = "AVAILABLE"
    UNDER_CHANGE = "UNDER_CHANGE"
    TAINTED = "TAINTED"
    ERROR = "ERROR"
    PLAN_IN_PROGRESS = "PLAN_IN_PROGRESS"


class ProvisionedProductViewFilterBy(Enum):
    SearchQuery = "SearchQuery"


@dataclasses.dataclass
class ProvisioningArtifact(autoboto.ShapeBase):
    """
    Information about a provisioning artifact. A provisioning artifact is also known
    as a product version.
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
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The identifier of the provisioning artifact.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the provisioning artifact.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the provisioning artifact.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ProvisioningArtifactDetail(autoboto.ShapeBase):
    """
    Information about a provisioning artifact (also known as a version) for a
    product.
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
                "type",
                "Type",
                autoboto.TypeInfo(ProvisioningArtifactType),
            ),
            (
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "active",
                "Active",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The identifier of the provisioning artifact.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the provisioning artifact.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the provisioning artifact.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of provisioning artifact.

    #   * `CLOUD_FORMATION_TEMPLATE` \- AWS CloudFormation template

    #   * `MARKETPLACE_AMI` \- AWS Marketplace AMI

    #   * `MARKETPLACE_CAR` \- AWS Marketplace Clusters and AWS Resources
    type: "ProvisioningArtifactType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the product version is active.
    active: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProvisioningArtifactParameter(autoboto.ShapeBase):
    """
    Information about a parameter used to provision a product.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_key",
                "ParameterKey",
                autoboto.TypeInfo(str),
            ),
            (
                "default_value",
                "DefaultValue",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_type",
                "ParameterType",
                autoboto.TypeInfo(str),
            ),
            (
                "is_no_echo",
                "IsNoEcho",
                autoboto.TypeInfo(bool),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_constraints",
                "ParameterConstraints",
                autoboto.TypeInfo(ParameterConstraints),
            ),
        ]

    # The parameter key.
    parameter_key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The default value.
    default_value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The parameter type.
    parameter_type: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If this value is true, the value for this parameter is obfuscated from view
    # when the parameter is retrieved. This parameter is used to hide sensitive
    # information.
    is_no_echo: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the parameter.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Constraints that the administrator has put on a parameter.
    parameter_constraints: "ParameterConstraints" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ProvisioningArtifactProperties(autoboto.ShapeBase):
    """
    Information about a provisioning artifact (also known as a version) for a
    product.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "info",
                "Info",
                autoboto.TypeInfo(typing.Dict[str, str]),
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
                "type",
                "Type",
                autoboto.TypeInfo(ProvisioningArtifactType),
            ),
        ]

    # The URL of the CloudFormation template in Amazon S3. Specify the URL in
    # JSON format as follows:

    # `"LoadTemplateFromURL": "https://s3.amazonaws.com/cf-templates-
    # ozkq9d3hgiq2-us-east-1/..."`
    info: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the provisioning artifact (for example, v1 v2beta). No spaces
    # are allowed.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the provisioning artifact, including how it differs from
    # the previous provisioning artifact.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of provisioning artifact.

    #   * `CLOUD_FORMATION_TEMPLATE` \- AWS CloudFormation template

    #   * `MARKETPLACE_AMI` \- AWS Marketplace AMI

    #   * `MARKETPLACE_CAR` \- AWS Marketplace Clusters and AWS Resources
    type: "ProvisioningArtifactType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ProvisioningArtifactPropertyName(Enum):
    Id = "Id"


@dataclasses.dataclass
class ProvisioningArtifactSummary(autoboto.ShapeBase):
    """
    Summary information about a provisioning artifact (also known as a version) for
    a product.
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
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "provisioning_artifact_metadata",
                "ProvisioningArtifactMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The identifier of the provisioning artifact.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the provisioning artifact.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the provisioning artifact.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The metadata for the provisioning artifact. This is used with AWS
    # Marketplace products.
    provisioning_artifact_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ProvisioningArtifactType(Enum):
    CLOUD_FORMATION_TEMPLATE = "CLOUD_FORMATION_TEMPLATE"
    MARKETPLACE_AMI = "MARKETPLACE_AMI"
    MARKETPLACE_CAR = "MARKETPLACE_CAR"


@dataclasses.dataclass
class ProvisioningParameter(autoboto.ShapeBase):
    """
    Information about a parameter used to provision a product.
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

    # The parameter key.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The parameter value.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RecordDetail(autoboto.ShapeBase):
    """
    Information about a request operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "record_id",
                "RecordId",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioned_product_name",
                "ProvisionedProductName",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(RecordStatus),
            ),
            (
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "updated_time",
                "UpdatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "provisioned_product_type",
                "ProvisionedProductType",
                autoboto.TypeInfo(str),
            ),
            (
                "record_type",
                "RecordType",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioned_product_id",
                "ProvisionedProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                autoboto.TypeInfo(str),
            ),
            (
                "path_id",
                "PathId",
                autoboto.TypeInfo(str),
            ),
            (
                "record_errors",
                "RecordErrors",
                autoboto.TypeInfo(typing.List[RecordError]),
            ),
            (
                "record_tags",
                "RecordTags",
                autoboto.TypeInfo(typing.List[RecordTag]),
            ),
        ]

    # The identifier of the record.
    record_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user-friendly name of the provisioned product.
    provisioned_product_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the provisioned product.

    #   * `CREATED` \- The request was created but the operation has not started.

    #   * `IN_PROGRESS` \- The requested operation is in progress.

    #   * `IN_PROGRESS_IN_ERROR` \- The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.

    #   * `SUCCEEDED` \- The requested operation has successfully completed.

    #   * `FAILED` \- The requested operation has unsuccessfully completed. Investigate using the error messages returned.
    status: "RecordStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The UTC time stamp of the creation time.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time when the record was last updated.
    updated_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of provisioned product. The supported value is `CFN_STACK`.
    provisioned_product_type: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The record type.

    #   * `PROVISION_PRODUCT`

    #   * `UPDATE_PROVISIONED_PRODUCT`

    #   * `TERMINATE_PROVISIONED_PRODUCT`
    record_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of the provisioned product.
    provisioned_product_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The path identifier.
    path_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The errors that occurred.
    record_errors: typing.List["RecordError"] = dataclasses.field(
        default_factory=list,
    )

    # One or more tags.
    record_tags: typing.List["RecordTag"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class RecordError(autoboto.ShapeBase):
    """
    The error code and description resulting from an operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The numeric value of the error.
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the error.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RecordOutput(autoboto.OutputShapeBase):
    """
    The output for the product created as the result of a request. For example, the
    output for a CloudFormation-backed product that creates an S3 bucket would
    include the S3 bucket URL.
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
                "output_key",
                "OutputKey",
                autoboto.TypeInfo(str),
            ),
            (
                "output_value",
                "OutputValue",
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

    # The output key.
    output_key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The output value.
    output_value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the output.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class RecordStatus(Enum):
    CREATED = "CREATED"
    IN_PROGRESS = "IN_PROGRESS"
    IN_PROGRESS_IN_ERROR = "IN_PROGRESS_IN_ERROR"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


@dataclasses.dataclass
class RecordTag(autoboto.ShapeBase):
    """
    Information about a tag, which is a key-value pair.
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

    # The key for this tag.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value for this tag.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RejectPortfolioShareInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "portfolio_id",
                "PortfolioId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RejectPortfolioShareOutput(autoboto.OutputShapeBase):
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


class Replacement(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
    CONDITIONAL = "CONDITIONAL"


class RequiresRecreation(Enum):
    NEVER = "NEVER"
    CONDITIONALLY = "CONDITIONALLY"
    ALWAYS = "ALWAYS"


class ResourceAttribute(Enum):
    PROPERTIES = "PROPERTIES"
    METADATA = "METADATA"
    CREATIONPOLICY = "CREATIONPOLICY"
    UPDATEPOLICY = "UPDATEPOLICY"
    DELETIONPOLICY = "DELETIONPOLICY"
    TAGS = "TAGS"


@dataclasses.dataclass
class ResourceChange(autoboto.ShapeBase):
    """
    Information about a resource change that will occur when a plan is executed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(ChangeAction),
            ),
            (
                "logical_resource_id",
                "LogicalResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "physical_resource_id",
                "PhysicalResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "replacement",
                "Replacement",
                autoboto.TypeInfo(Replacement),
            ),
            (
                "scope",
                "Scope",
                autoboto.TypeInfo(typing.List[ResourceAttribute]),
            ),
            (
                "details",
                "Details",
                autoboto.TypeInfo(typing.List[ResourceChangeDetail]),
            ),
        ]

    # The change action.
    action: "ChangeAction" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the resource, as defined in the CloudFormation template.
    logical_resource_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the resource, if it was already created.
    physical_resource_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of resource.
    resource_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the change type is `Modify`, indicates whether the existing resource is
    # deleted and replaced with a new one.
    replacement: "Replacement" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The change scope.
    scope: typing.List["ResourceAttribute"] = dataclasses.field(
        default_factory=list,
    )

    # Information about the resource changes.
    details: typing.List["ResourceChangeDetail"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ResourceChangeDetail(autoboto.ShapeBase):
    """
    Information about a change to a resource attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target",
                "Target",
                autoboto.TypeInfo(ResourceTargetDefinition),
            ),
            (
                "evaluation",
                "Evaluation",
                autoboto.TypeInfo(EvaluationType),
            ),
            (
                "causing_entity",
                "CausingEntity",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the resource attribute to be modified.
    target: "ResourceTargetDefinition" = dataclasses.field(
        default_factory=dict,
    )

    # For static evaluations, the value of the resource attribute will change and
    # the new value is known. For dynamic evaluations, the value might change,
    # and any new value will be determined when the plan is updated.
    evaluation: "EvaluationType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the entity that caused the change.
    causing_entity: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceDetail(autoboto.ShapeBase):
    """
    Information about a resource.
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
                "arn",
                "ARN",
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
                "created_time",
                "CreatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The identifier of the resource.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN of the resource.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the resource.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the resource.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The creation time of the resource.
    created_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceInUseException(autoboto.ShapeBase):
    """
    A resource that is currently in use. Ensure that the resource is not in use and
    retry the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    The specified resource was not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResourceTargetDefinition(autoboto.ShapeBase):
    """
    Information about a change to a resource attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute",
                "Attribute",
                autoboto.TypeInfo(ResourceAttribute),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "requires_recreation",
                "RequiresRecreation",
                autoboto.TypeInfo(RequiresRecreation),
            ),
        ]

    # The attribute to be changed.
    attribute: "ResourceAttribute" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the attribute is `Properties`, the value is the name of the property.
    # Otherwise, the value is null.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the attribute is `Properties`, indicates whether a change to this
    # property causes the resource to be re-created.
    requires_recreation: "RequiresRecreation" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ScanProvisionedProductsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "access_level_filter",
                "AccessLevelFilter",
                autoboto.TypeInfo(AccessLevelFilter),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The access level to use to obtain results. The default is `User`.
    access_level_filter: "AccessLevelFilter" = dataclasses.field(
        default_factory=dict,
    )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ScanProvisionedProductsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioned_products",
                "ProvisionedProducts",
                autoboto.TypeInfo(typing.List[ProvisionedProductDetail]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the provisioned products.
    provisioned_products: typing.List["ProvisionedProductDetail"
                                     ] = dataclasses.field(
                                         default_factory=list,
                                     )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SearchProductsAsAdminInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "portfolio_id",
                "PortfolioId",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(
                    typing.Dict[ProductViewFilterBy, typing.List[str]]
                ),
            ),
            (
                "sort_by",
                "SortBy",
                autoboto.TypeInfo(ProductViewSortBy),
            ),
            (
                "sort_order",
                "SortOrder",
                autoboto.TypeInfo(SortOrder),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "product_source",
                "ProductSource",
                autoboto.TypeInfo(ProductSource),
            ),
        ]

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The portfolio identifier.
    portfolio_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The search filters. If no search filters are specified, the output includes
    # all products to which the administrator has access.
    filters: typing.Dict["ProductViewFilterBy", typing.List[str]
                        ] = dataclasses.field(
                            default=autoboto.ShapeBase.NOT_SET,
                        )

    # The sort field. If no value is specified, the results are not sorted.
    sort_by: "ProductViewSortBy" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The sort order. If no value is specified, the results are not sorted.
    sort_order: "SortOrder" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Access level of the source of the product.
    product_source: "ProductSource" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SearchProductsAsAdminOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "product_view_details",
                "ProductViewDetails",
                autoboto.TypeInfo(typing.List[ProductViewDetail]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the product views.
    product_view_details: typing.List["ProductViewDetail"] = dataclasses.field(
        default_factory=list,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SearchProductsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(
                    typing.Dict[ProductViewFilterBy, typing.List[str]]
                ),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "sort_by",
                "SortBy",
                autoboto.TypeInfo(ProductViewSortBy),
            ),
            (
                "sort_order",
                "SortOrder",
                autoboto.TypeInfo(SortOrder),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The search filters. If no search filters are specified, the output includes
    # all products to which the caller has access.
    filters: typing.Dict["ProductViewFilterBy", typing.List[str]
                        ] = dataclasses.field(
                            default=autoboto.ShapeBase.NOT_SET,
                        )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The sort field. If no value is specified, the results are not sorted.
    sort_by: "ProductViewSortBy" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The sort order. If no value is specified, the results are not sorted.
    sort_order: "SortOrder" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchProductsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "product_view_summaries",
                "ProductViewSummaries",
                autoboto.TypeInfo(typing.List[ProductViewSummary]),
            ),
            (
                "product_view_aggregations",
                "ProductViewAggregations",
                autoboto.TypeInfo(
                    typing.Dict[str, typing.List[ProductViewAggregationValue]]
                ),
            ),
            (
                "next_page_token",
                "NextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the product views.
    product_view_summaries: typing.List["ProductViewSummary"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )

    # The product view aggregations.
    product_view_aggregations: typing.Dict[
        str, typing.List["ProductViewAggregationValue"]
    ] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SearchProvisionedProductsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "access_level_filter",
                "AccessLevelFilter",
                autoboto.TypeInfo(AccessLevelFilter),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(
                    typing.Dict[ProvisionedProductViewFilterBy, typing.List[str]
                               ]
                ),
            ),
            (
                "sort_by",
                "SortBy",
                autoboto.TypeInfo(str),
            ),
            (
                "sort_order",
                "SortOrder",
                autoboto.TypeInfo(SortOrder),
            ),
            (
                "page_size",
                "PageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "page_token",
                "PageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The access level to use to obtain results. The default is `User`.
    access_level_filter: "AccessLevelFilter" = dataclasses.field(
        default_factory=dict,
    )

    # The search filters.

    # When the key is `SearchQuery`, the searchable fields are `arn`,
    # `createdTime`, `id`, `lastRecordId`, `idempotencyToken`, `name`,
    # `physicalId`, `productId`, `provisioningArtifact`, `type`, `status`,
    # `tags`, `userArn`, and `userArnSession`.

    # Example: `"SearchQuery":["status:AVAILABLE"]`
    filters: typing.Dict["ProvisionedProductViewFilterBy", typing.List[str]
                        ] = dataclasses.field(
                            default=autoboto.ShapeBase.NOT_SET,
                        )

    # The sort field. If no value is specified, the results are not sorted. The
    # valid values are `arn`, `id`, `name`, and `lastRecordId`.
    sort_by: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The sort order. If no value is specified, the results are not sorted.
    sort_order: "SortOrder" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of items to return with this call.
    page_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The page token for the next set of results. To retrieve the first set of
    # results, use null.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchProvisionedProductsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioned_products",
                "ProvisionedProducts",
                autoboto.TypeInfo(typing.List[ProvisionedProductAttribute]),
            ),
            (
                "total_results_count",
                "TotalResultsCount",
                autoboto.TypeInfo(int),
            ),
            (
                "next_page_token",
                "NextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the provisioned products.
    provisioned_products: typing.List["ProvisionedProductAttribute"
                                     ] = dataclasses.field(
                                         default_factory=list,
                                     )

    # The number of provisioned products found.
    total_results_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The page token to use to retrieve the next set of results. If there are no
    # additional results, this value is null.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class SortOrder(Enum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class Status(Enum):
    AVAILABLE = "AVAILABLE"
    CREATING = "CREATING"
    FAILED = "FAILED"


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    """
    Information about a tag. A tag is a key-value pair. Tags are propagated to the
    resources created when provisioning a product.
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

    # The value for this key.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagOptionDetail(autoboto.ShapeBase):
    """
    Information about a TagOption.
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
                "active",
                "Active",
                autoboto.TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The TagOption key.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The TagOption value.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The TagOption active state.
    active: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The TagOption identifier.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagOptionNotMigratedException(autoboto.ShapeBase):
    """
    An operation requiring TagOptions failed because the TagOptions migration
    process has not been performed for this account. Please use the AWS console to
    perform the migration process before retrying the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TagOptionSummary(autoboto.ShapeBase):
    """
    Summary information about a TagOption.
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

    # The TagOption key.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The TagOption value.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class TerminateProvisionedProductInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "terminate_token",
                "TerminateToken",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioned_product_name",
                "ProvisionedProductName",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioned_product_id",
                "ProvisionedProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "ignore_errors",
                "IgnoreErrors",
                autoboto.TypeInfo(bool),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
        ]

    # An idempotency token that uniquely identifies the termination request. This
    # token is only valid during the termination process. After the provisioned
    # product is terminated, subsequent requests to terminate the same
    # provisioned product always return **ResourceNotFound**.
    terminate_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the provisioned product. You cannot specify both
    # `ProvisionedProductName` and `ProvisionedProductId`.
    provisioned_product_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the provisioned product. You cannot specify both
    # `ProvisionedProductName` and `ProvisionedProductId`.
    provisioned_product_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If set to true, AWS Service Catalog stops managing the specified
    # provisioned product even if it cannot delete the underlying resources.
    ignore_errors: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TerminateProvisionedProductOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "record_detail",
                "RecordDetail",
                autoboto.TypeInfo(RecordDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the result of this request.
    record_detail: "RecordDetail" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateConstraintInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier of the constraint.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated description of the constraint.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateConstraintOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "constraint_detail",
                "ConstraintDetail",
                autoboto.TypeInfo(ConstraintDetail),
            ),
            (
                "constraint_parameters",
                "ConstraintParameters",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(Status),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the constraint.
    constraint_detail: "ConstraintDetail" = dataclasses.field(
        default_factory=dict,
    )

    # The constraint parameters.
    constraint_parameters: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the current request.
    status: "Status" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePortfolioInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "provider_name",
                "ProviderName",
                autoboto.TypeInfo(str),
            ),
            (
                "add_tags",
                "AddTags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "remove_tags",
                "RemoveTags",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The portfolio identifier.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name to use for display purposes.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated description of the portfolio.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated name of the portfolio provider.
    provider_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tags to add.
    add_tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # The tags to remove.
    remove_tags: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UpdatePortfolioOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "portfolio_detail",
                "PortfolioDetail",
                autoboto.TypeInfo(PortfolioDetail),
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

    # Information about the portfolio.
    portfolio_detail: "PortfolioDetail" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the tags associated with the portfolio.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UpdateProductInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
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
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "distributor",
                "Distributor",
                autoboto.TypeInfo(str),
            ),
            (
                "support_description",
                "SupportDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "support_email",
                "SupportEmail",
                autoboto.TypeInfo(str),
            ),
            (
                "support_url",
                "SupportUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "add_tags",
                "AddTags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "remove_tags",
                "RemoveTags",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The product identifier.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated product name.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated owner of the product.
    owner: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated description of the product.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated distributor of the product.
    distributor: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated support description for the product.
    support_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated support email for the product.
    support_email: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated support URL for the product.
    support_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tags to add to the product.
    add_tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # The tags to remove from the product.
    remove_tags: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UpdateProductOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "product_view_detail",
                "ProductViewDetail",
                autoboto.TypeInfo(ProductViewDetail),
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

    # Information about the product view.
    product_view_detail: "ProductViewDetail" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the tags associated with the product.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UpdateProvisionedProductInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "update_token",
                "UpdateToken",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioned_product_name",
                "ProvisionedProductName",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioned_product_id",
                "ProvisionedProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                autoboto.TypeInfo(str),
            ),
            (
                "path_id",
                "PathId",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioning_parameters",
                "ProvisioningParameters",
                autoboto.TypeInfo(typing.List[UpdateProvisioningParameter]),
            ),
        ]

    # The idempotency token that uniquely identifies the provisioning update
    # request.
    update_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated name of the provisioned product. You cannot specify both
    # `ProvisionedProductName` and `ProvisionedProductId`.
    provisioned_product_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the provisioned product. You cannot specify both
    # `ProvisionedProductName` and `ProvisionedProductId`.
    provisioned_product_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the provisioned product.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The new path identifier. This value is optional if the product has a
    # default path, and required if the product has more than one path.
    path_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The new parameters.
    provisioning_parameters: typing.List["UpdateProvisioningParameter"
                                        ] = dataclasses.field(
                                            default_factory=list,
                                        )


@dataclasses.dataclass
class UpdateProvisionedProductOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "record_detail",
                "RecordDetail",
                autoboto.TypeInfo(RecordDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the result of the request.
    record_detail: "RecordDetail" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateProvisioningArtifactInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_id",
                "ProductId",
                autoboto.TypeInfo(str),
            ),
            (
                "provisioning_artifact_id",
                "ProvisioningArtifactId",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_language",
                "AcceptLanguage",
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
                "active",
                "Active",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The product identifier.
    product_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of the provisioning artifact.
    provisioning_artifact_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language code.

    #   * `en` \- English (default)

    #   * `jp` \- Japanese

    #   * `zh` \- Chinese
    accept_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The updated name of the provisioning artifact.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated description of the provisioning artifact.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether the product version is active.
    active: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateProvisioningArtifactOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "provisioning_artifact_detail",
                "ProvisioningArtifactDetail",
                autoboto.TypeInfo(ProvisioningArtifactDetail),
            ),
            (
                "info",
                "Info",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(Status),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the provisioning artifact.
    provisioning_artifact_detail: "ProvisioningArtifactDetail" = dataclasses.field(
        default_factory=dict,
    )

    # The URL of the CloudFormation template in Amazon S3.
    info: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the current request.
    status: "Status" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateProvisioningParameter(autoboto.ShapeBase):
    """
    The parameter key-value pair used to update a provisioned product.
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
                "use_previous_value",
                "UsePreviousValue",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The parameter key.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The parameter value.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If set to true, `Value` is ignored and the previous parameter value is
    # kept.
    use_previous_value: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateTagOptionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
            (
                "active",
                "Active",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The TagOption identifier.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated value.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The updated active state.
    active: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateTagOptionOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tag_option_detail",
                "TagOptionDetail",
                autoboto.TypeInfo(TagOptionDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Information about the TagOption.
    tag_option_detail: "TagOptionDetail" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UsageInstruction(autoboto.ShapeBase):
    """
    Additional information provided by the administrator.
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
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
        ]

    # The usage instruction type for the value.
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The usage instruction value for this type.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
