import datetime
import typing
import autoboto
import dataclasses


@dataclasses.dataclass
class Attribute(autoboto.ShapeBase):
    """

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
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
            (
                "alternate_name_encoding",
                "AlternateNameEncoding",
                autoboto.TypeInfo(str),
            ),
            (
                "alternate_value_encoding",
                "AlternateValueEncoding",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the attribute.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value of the attribute.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    alternate_name_encoding: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    alternate_value_encoding: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttributeDoesNotExist(autoboto.ShapeBase):
    """
    The specified attribute does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchDeleteAttributesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "items",
                "Items",
                autoboto.TypeInfo(typing.List[DeletableItem]),
            ),
        ]

    # The name of the domain in which the attributes are being deleted.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of items on which to perform the operation.
    items: typing.List["DeletableItem"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchPutAttributesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "items",
                "Items",
                autoboto.TypeInfo(typing.List[ReplaceableItem]),
            ),
        ]

    # The name of the domain in which the attributes are being stored.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of items on which to perform the operation.
    items: typing.List["ReplaceableItem"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateDomainRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the domain to create. The name can range between 3 and 255
    # characters and can contain the following characters: a-z, A-Z, 0-9, '_',
    # '-', and '.'.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletableItem(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.List[Attribute]),
            ),
        ]

    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    attributes: typing.List["Attribute"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DeleteAttributesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "item_name",
                "ItemName",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.List[Attribute]),
            ),
            (
                "expected",
                "Expected",
                autoboto.TypeInfo(UpdateCondition),
            ),
        ]

    # The name of the domain in which to perform the operation.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the item. Similar to rows on a spreadsheet, items represent
    # individual objects that contain one or more value-attribute pairs.
    item_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of Attributes. Similar to columns on a spreadsheet, attributes
    # represent categories of data that can be assigned to items.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default_factory=list,
    )

    # The update condition which, if specified, determines whether the specified
    # attributes will be deleted or not. The update condition must be satisfied
    # in order for this request to be processed and the attributes to be deleted.
    expected: "UpdateCondition" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteDomainRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the domain to delete.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DomainMetadataRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the domain for which to display the metadata of.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DomainMetadataResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item_count",
                "ItemCount",
                autoboto.TypeInfo(int),
            ),
            (
                "item_names_size_bytes",
                "ItemNamesSizeBytes",
                autoboto.TypeInfo(int),
            ),
            (
                "attribute_name_count",
                "AttributeNameCount",
                autoboto.TypeInfo(int),
            ),
            (
                "attribute_names_size_bytes",
                "AttributeNamesSizeBytes",
                autoboto.TypeInfo(int),
            ),
            (
                "attribute_value_count",
                "AttributeValueCount",
                autoboto.TypeInfo(int),
            ),
            (
                "attribute_values_size_bytes",
                "AttributeValuesSizeBytes",
                autoboto.TypeInfo(int),
            ),
            (
                "timestamp",
                "Timestamp",
                autoboto.TypeInfo(int),
            ),
        ]

    # The number of all items in the domain.
    item_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The total size of all item names in the domain, in bytes.
    item_names_size_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of unique attribute names in the domain.
    attribute_name_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The total size of all unique attribute names in the domain, in bytes.
    attribute_names_size_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of all attribute name/value pairs in the domain.
    attribute_value_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The total size of all attribute values in the domain, in bytes.
    attribute_values_size_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The data and time when metadata was calculated, in Epoch (UNIX) seconds.
    timestamp: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DuplicateItemName(autoboto.ShapeBase):
    """
    The item name was specified more than once.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAttributesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "item_name",
                "ItemName",
                autoboto.TypeInfo(str),
            ),
            (
                "attribute_names",
                "AttributeNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "consistent_read",
                "ConsistentRead",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the domain in which to perform the operation.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the item.
    item_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The names of the attributes.
    attribute_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Determines whether or not strong consistency should be enforced when data
    # is read from SimpleDB. If `true`, any data previously written to SimpleDB
    # will be returned. Otherwise, results will be consistent eventually, and the
    # client may not see data that was written immediately before your read.
    consistent_read: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetAttributesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.List[Attribute]),
            ),
        ]

    # The list of attributes returned by the operation.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class InvalidNextToken(autoboto.ShapeBase):
    """
    The specified NextToken is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidNumberPredicates(autoboto.ShapeBase):
    """
    Too many predicates exist in the query expression.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidNumberValueTests(autoboto.ShapeBase):
    """
    Too many predicates exist in the query expression.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterValue(autoboto.ShapeBase):
    """
    The value for a parameter is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidQueryExpression(autoboto.ShapeBase):
    """
    The specified query expression syntax is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Item(autoboto.ShapeBase):
    """

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
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.List[Attribute]),
            ),
            (
                "alternate_name_encoding",
                "AlternateNameEncoding",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the item.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of attributes.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default_factory=list,
    )

    alternate_name_encoding: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListDomainsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_number_of_domains",
                "MaxNumberOfDomains",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The maximum number of domain names you want returned. The range is 1 to
    # 100. The default setting is 100.
    max_number_of_domains: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string informing Amazon SimpleDB where to start the next list of domain
    # names.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDomainsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_names",
                "DomainNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of domain names that match the expression.
    domain_names: typing.List[str] = dataclasses.field(default_factory=list, )

    # An opaque token indicating that there are more domains than the specified
    # `MaxNumberOfDomains` still available.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MissingParameter(autoboto.ShapeBase):
    """
    The request must contain the specified missing parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoSuchDomain(autoboto.ShapeBase):
    """
    The specified domain does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NumberDomainAttributesExceeded(autoboto.ShapeBase):
    """
    Too many attributes in this domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NumberDomainBytesExceeded(autoboto.ShapeBase):
    """
    Too many bytes in this domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NumberDomainsExceeded(autoboto.ShapeBase):
    """
    Too many domains exist per this account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NumberItemAttributesExceeded(autoboto.ShapeBase):
    """
    Too many attributes in this item.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NumberSubmittedAttributesExceeded(autoboto.ShapeBase):
    """
    Too many attributes exist in a single call.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NumberSubmittedItemsExceeded(autoboto.ShapeBase):
    """
    Too many items exist in a single call.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutAttributesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "item_name",
                "ItemName",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.List[ReplaceableAttribute]),
            ),
            (
                "expected",
                "Expected",
                autoboto.TypeInfo(UpdateCondition),
            ),
        ]

    # The name of the domain in which to perform the operation.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the item.
    item_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of attributes.
    attributes: typing.List["ReplaceableAttribute"] = dataclasses.field(
        default_factory=list,
    )

    # The update condition which, if specified, determines whether the specified
    # attributes will be updated or not. The update condition must be satisfied
    # in order for this request to be processed and the attributes to be updated.
    expected: "UpdateCondition" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ReplaceableAttribute(autoboto.ShapeBase):
    """

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
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
            (
                "replace",
                "Replace",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the replaceable attribute.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value of the replaceable attribute.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A flag specifying whether or not to replace the attribute/value pair or to
    # add a new attribute/value pair. The default setting is `false`.
    replace: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReplaceableItem(autoboto.ShapeBase):
    """

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
                "attributes",
                "Attributes",
                autoboto.TypeInfo(typing.List[ReplaceableAttribute]),
            ),
        ]

    # The name of the replaceable item.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of attributes for a replaceable item.
    attributes: typing.List["ReplaceableAttribute"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class RequestTimeout(autoboto.ShapeBase):
    """
    A timeout occurred when attempting to query the specified domain with specified
    query expression.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SelectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "select_expression",
                "SelectExpression",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "consistent_read",
                "ConsistentRead",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The expression used to query the domain.
    select_expression: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string informing Amazon SimpleDB where to start the next list of
    # `ItemNames`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Determines whether or not strong consistency should be enforced when data
    # is read from SimpleDB. If `true`, any data previously written to SimpleDB
    # will be returned. Otherwise, results will be consistent eventually, and the
    # client may not see data that was written immediately before your read.
    consistent_read: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SelectResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "items",
                "Items",
                autoboto.TypeInfo(typing.List[Item]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of items that match the select expression.
    items: typing.List["Item"] = dataclasses.field(default_factory=list, )

    # An opaque token indicating that more items than `MaxNumberOfItems` were
    # matched, the response size exceeded 1 megabyte, or the execution time
    # exceeded 5 seconds.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyRequestedAttributes(autoboto.ShapeBase):
    """
    Too many attributes requested.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "box_usage",
                "BoxUsage",
                autoboto.TypeInfo(float),
            ),
        ]

    box_usage: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateCondition(autoboto.ShapeBase):
    """
    Specifies the conditions under which data should be updated. If an update
    condition is specified for a request, the data will only be updated if the
    condition is satisfied. For example, if an attribute with a specific name and
    value exists, or if a specific attribute doesn't exist.
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
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
            (
                "exists",
                "Exists",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the attribute involved in the condition.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value of an attribute. This value can only be specified when the
    # `Exists` parameter is equal to `true`.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A value specifying whether or not the specified attribute must exist with
    # the specified value in order for the update condition to be satisfied.
    # Specify `true` if the attribute must exist for the update condition to be
    # satisfied. Specify `false` if the attribute should not exist in order for
    # the update condition to be satisfied.
    exists: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
