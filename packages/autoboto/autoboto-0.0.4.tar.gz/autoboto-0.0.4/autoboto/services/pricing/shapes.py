import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AttributeValue(autoboto.ShapeBase):
    """
    The values of a given attribute, such as `Throughput Optimized HDD` or
    `Provisioned IOPS` for the `Amazon EC2` `volumeType` attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
        ]

    # The specific value of an `attributeName`.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeServicesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_code",
                "ServiceCode",
                autoboto.TypeInfo(str),
            ),
            (
                "format_version",
                "FormatVersion",
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

    # The code for the service whose information you want to retrieve, such as
    # `AmazonEC2`. You can use the `ServiceCode` to filter the results in a
    # `GetProducts` call. To retrieve a list of all services, leave this blank.
    service_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The format version that you want the response to be in.

    # Valid values are: `aws_v1`
    format_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The pagination token that indicates the next set of results that you want
    # to retrieve.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results that you want returned in the response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeServicesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "services",
                "Services",
                autoboto.TypeInfo(typing.List[Service]),
            ),
            (
                "format_version",
                "FormatVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The service metadata for the service or services in the response.
    services: typing.List["Service"] = dataclasses.field(default_factory=list, )

    # The format version of the response. For example, `aws_v1`.
    format_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The pagination token for the next set of retreivable results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExpiredNextTokenException(autoboto.ShapeBase):
    """
    The pagination token expired. Try again without a pagination token.
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
class Filter(autoboto.ShapeBase):
    """
    The constraints that you want all returned products to match.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(FilterType),
            ),
            (
                "field",
                "Field",
                autoboto.TypeInfo(str),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of filter that you want to use.

    # Valid values are: `TERM_MATCH`. `TERM_MATCH` returns only products that
    # match both the given filter field and the given value.
    type: "FilterType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The product metadata field that you want to filter on. You can filter by
    # just the service code to see all products for a specific service, filter by
    # just the attribute name to see a specific attribute for multiple services,
    # or use both a service code and an attribute name to retrieve only products
    # that match both fields.

    # Valid values include: `ServiceCode`, and all attribute names

    # For example, you can filter by the `AmazonEC2` service code and the
    # `volumeType` attribute name to get the prices for only Amazon EC2 volumes.
    field: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The service code or attribute value that you want to filter by. If you are
    # filtering by service code this is the actual service code, such as
    # `AmazonEC2`. If you are filtering by attribute name, this is the attribute
    # value that you want the returned products to match, such as a `Provisioned
    # IOPS` volume.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class FilterType(Enum):
    TERM_MATCH = "TERM_MATCH"


@dataclasses.dataclass
class GetAttributeValuesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_code",
                "ServiceCode",
                autoboto.TypeInfo(str),
            ),
            (
                "attribute_name",
                "AttributeName",
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

    # The service code for the service whose attributes you want to retrieve. For
    # example, if you want the retrieve an EC2 attribute, use `AmazonEC2`.
    service_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the attribute that you want to retrieve the values for, such as
    # `volumeType`.
    attribute_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The pagination token that indicates the next set of results that you want
    # to retrieve.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to return in response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAttributeValuesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_values",
                "AttributeValues",
                autoboto.TypeInfo(typing.List[AttributeValue]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of values for an attribute. For example, `Throughput Optimized
    # HDD` and `Provisioned IOPS` are two available values for the `AmazonEC2`
    # `volumeType`.
    attribute_values: typing.List["AttributeValue"] = dataclasses.field(
        default_factory=list,
    )

    # The pagination token that indicates the next set of results to retrieve.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetProductsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_code",
                "ServiceCode",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "format_version",
                "FormatVersion",
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

    # The code for the service whose products you want to retrieve.
    service_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of filters that limit the returned products. only products that
    # match all filters are returned.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The format version that you want the response to be in.

    # Valid values are: `aws_v1`
    format_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The pagination token that indicates the next set of results that you want
    # to retrieve.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to return in the response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetProductsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "format_version",
                "FormatVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "price_list",
                "PriceList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The format version of the response. For example, aws_v1.
    format_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The list of products that match your filters. The list contains both the
    # product metadata and the price information.
    price_list: typing.List[str] = dataclasses.field(default_factory=list, )

    # The pagination token that indicates the next set of results to retrieve.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalErrorException(autoboto.ShapeBase):
    """
    An error on the server occurred during the processing of your request. Try again
    later.
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
class InvalidNextTokenException(autoboto.ShapeBase):
    """
    The pagination token is invalid. Try again without a pagination token.
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
class InvalidParameterException(autoboto.ShapeBase):
    """
    One or more parameters had an invalid value.
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
class NotFoundException(autoboto.ShapeBase):
    """
    The requested resource can't be found.
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
class Service(autoboto.ShapeBase):
    """
    The metadata for a service, such as the service code and available attribute
    names.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_code",
                "ServiceCode",
                autoboto.TypeInfo(str),
            ),
            (
                "attribute_names",
                "AttributeNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The code for the AWS service.
    service_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The attributes that are available for this service.
    attribute_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )
