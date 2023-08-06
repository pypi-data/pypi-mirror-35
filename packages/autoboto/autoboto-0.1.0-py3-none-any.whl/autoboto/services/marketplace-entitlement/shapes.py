import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class Entitlement(autoboto.ShapeBase):
    """
    An entitlement represents capacity in a product owned by the customer. For
    example, a customer might own some number of users or seats in an SaaS
    application or some amount of data capacity in a multi-tenant database.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_code",
                "ProductCode",
                autoboto.TypeInfo(str),
            ),
            (
                "dimension",
                "Dimension",
                autoboto.TypeInfo(str),
            ),
            (
                "customer_identifier",
                "CustomerIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(EntitlementValue),
            ),
            (
                "expiration_date",
                "ExpirationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The product code for which the given entitlement applies. Product codes are
    # provided by AWS Marketplace when the product listing is created.
    product_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The dimension for which the given entitlement applies. Dimensions represent
    # categories of capacity in a product and are specified when the product is
    # listed in AWS Marketplace.
    dimension: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The customer identifier is a handle to each unique customer in an
    # application. Customer identifiers are obtained through the ResolveCustomer
    # operation in AWS Marketplace Metering Service.
    customer_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The EntitlementValue represents the amount of capacity that the customer is
    # entitled to for the product.
    value: "EntitlementValue" = dataclasses.field(default_factory=dict, )

    # The expiration date represents the minimum date through which this
    # entitlement is expected to remain valid. For contractual products listed on
    # AWS Marketplace, the expiration date is the date at which the customer will
    # renew or cancel their contract. Customers who are opting to renew their
    # contract will still have entitlements with an expiration date.
    expiration_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EntitlementValue(autoboto.ShapeBase):
    """
    The EntitlementValue represents the amount of capacity that the customer is
    entitled to for the product.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "integer_value",
                "IntegerValue",
                autoboto.TypeInfo(int),
            ),
            (
                "double_value",
                "DoubleValue",
                autoboto.TypeInfo(float),
            ),
            (
                "boolean_value",
                "BooleanValue",
                autoboto.TypeInfo(bool),
            ),
            (
                "string_value",
                "StringValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The IntegerValue field will be populated with an integer value when the
    # entitlement is an integer type. Otherwise, the field will not be set.
    integer_value: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The DoubleValue field will be populated with a double value when the
    # entitlement is a double type. Otherwise, the field will not be set.
    double_value: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The BooleanValue field will be populated with a boolean value when the
    # entitlement is a boolean type. Otherwise, the field will not be set.
    boolean_value: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The StringValue field will be populated with a string value when the
    # entitlement is a string type. Otherwise, the field will not be set.
    string_value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class GetEntitlementFilterName(Enum):
    CUSTOMER_IDENTIFIER = "CUSTOMER_IDENTIFIER"
    DIMENSION = "DIMENSION"


@dataclasses.dataclass
class GetEntitlementsRequest(autoboto.ShapeBase):
    """
    The GetEntitlementsRequest contains parameters for the GetEntitlements
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_code",
                "ProductCode",
                autoboto.TypeInfo(str),
            ),
            (
                "filter",
                "Filter",
                autoboto.TypeInfo(
                    typing.Dict[GetEntitlementFilterName, typing.List[str]]
                ),
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

    # Product code is used to uniquely identify a product in AWS Marketplace. The
    # product code will be provided by AWS Marketplace when the product listing
    # is created.
    product_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filter is used to return entitlements for a specific customer or for a
    # specific dimension. Filters are described as keys mapped to a lists of
    # values. Filtered requests are _unioned_ for each value in the value list,
    # and then _intersected_ for each filter key.
    filter: typing.Dict["GetEntitlementFilterName", typing.List[str]
                       ] = dataclasses.field(
                           default=autoboto.ShapeBase.NOT_SET,
                       )

    # For paginated calls to GetEntitlements, pass the NextToken from the
    # previous GetEntitlementsResult.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to retrieve from the GetEntitlements operation.
    # For pagination, use the NextToken field in subsequent calls to
    # GetEntitlements.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetEntitlementsResult(autoboto.OutputShapeBase):
    """
    The GetEntitlementsRequest contains results from the GetEntitlements operation.
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
                "entitlements",
                "Entitlements",
                autoboto.TypeInfo(typing.List[Entitlement]),
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

    # The set of entitlements found through the GetEntitlements operation. If the
    # result contains an empty set of entitlements, NextToken might still be
    # present and should be used.
    entitlements: typing.List["Entitlement"] = dataclasses.field(
        default_factory=list,
    )

    # For paginated results, use NextToken in subsequent calls to
    # GetEntitlements. If the result contains an empty set of entitlements,
    # NextToken might still be present and should be used.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServiceErrorException(autoboto.ShapeBase):
    """
    An internal error has occurred. Retry your request. If the problem persists,
    post a message with details on the AWS forums.
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
class InvalidParameterException(autoboto.ShapeBase):
    """
    One or more parameters in your request was invalid.
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
    The calls to the GetEntitlements API are throttled.
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
