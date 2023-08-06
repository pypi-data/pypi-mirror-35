import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


class ErrorCode(Enum):
    InternalServiceException = "InternalServiceException"
    InvalidParameterException = "InvalidParameterException"


@dataclasses.dataclass
class FailureInfo(autoboto.ShapeBase):
    """
    Details of the common errors that all actions return.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status_code",
                "StatusCode",
                autoboto.TypeInfo(int),
            ),
            (
                "error_code",
                "ErrorCode",
                autoboto.TypeInfo(ErrorCode),
            ),
            (
                "error_message",
                "ErrorMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The HTTP status code of the common error.
    status_code: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The code of the common error. Valid values include
    # `InternalServiceException`, `InvalidParameterException`, and any valid
    # error code returned by the AWS service that hosts the resource that you
    # want to tag.
    error_code: "ErrorCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The message of the common error.
    error_message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetResourcesInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pagination_token",
                "PaginationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_filters",
                "TagFilters",
                autoboto.TypeInfo(typing.List[TagFilter]),
            ),
            (
                "resources_per_page",
                "ResourcesPerPage",
                autoboto.TypeInfo(int),
            ),
            (
                "tags_per_page",
                "TagsPerPage",
                autoboto.TypeInfo(int),
            ),
            (
                "resource_type_filters",
                "ResourceTypeFilters",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A string that indicates that additional data is available. Leave this value
    # empty for your initial request. If the response includes a
    # `PaginationToken`, use that string for this value to request an additional
    # page of data.
    pagination_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of tags (keys and values). A request can include up to 50 keys, and
    # each key can include up to 20 values.

    # If you specify multiple filters connected by an AND operator in a single
    # request, the response returns only those resources that are associated with
    # every specified filter.

    # If you specify multiple filters connected by an OR operator in a single
    # request, the response returns all resources that are associated with at
    # least one or possibly more of the specified filters.
    tag_filters: typing.List["TagFilter"] = dataclasses.field(
        default_factory=list,
    )

    # A limit that restricts the number of resources returned by GetResources in
    # paginated output. You can set ResourcesPerPage to a minimum of 1 item and
    # the maximum of 50 items.
    resources_per_page: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A limit that restricts the number of tags (key and value pairs) returned by
    # GetResources in paginated output. A resource with no tags is counted as
    # having one tag (one key and value pair).

    # `GetResources` does not split a resource and its associated tags across
    # pages. If the specified `TagsPerPage` would cause such a break, a
    # `PaginationToken` is returned in place of the affected resource and its
    # tags. Use that token in another request to get the remaining data. For
    # example, if you specify a `TagsPerPage` of `100` and the account has 22
    # resources with 10 tags each (meaning that each resource has 10 key and
    # value pairs), the output will consist of 3 pages, with the first page
    # displaying the first 10 resources, each with its 10 tags, the second page
    # displaying the next 10 resources each with its 10 tags, and the third page
    # displaying the remaining 2 resources, each with its 10 tags.

    # You can set `TagsPerPage` to a minimum of 100 items and the maximum of 500
    # items.
    tags_per_page: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The constraints on the resources that you want returned. The format of each
    # resource type is `service[:resourceType]`. For example, specifying a
    # resource type of `ec2` returns all tagged Amazon EC2 resources (which
    # includes tagged EC2 instances). Specifying a resource type of
    # `ec2:instance` returns only EC2 instances.

    # The string for each service name and resource type is the same as that
    # embedded in a resource's Amazon Resource Name (ARN). Consult the _AWS
    # General Reference_ for the following:

    #   * For a list of service name strings, see [AWS Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces).

    #   * For resource type strings, see [Example ARNs](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arns-syntax).

    #   * For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
    resource_type_filters: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetResourcesOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pagination_token",
                "PaginationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_tag_mapping_list",
                "ResourceTagMappingList",
                autoboto.TypeInfo(typing.List[ResourceTagMapping]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string that indicates that the response contains more data than can be
    # returned in a single response. To receive additional data, specify this
    # string for the `PaginationToken` value in a subsequent request.
    pagination_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of resource ARNs and the tags (keys and values) associated with
    # each.
    resource_tag_mapping_list: typing.List["ResourceTagMapping"
                                          ] = dataclasses.field(
                                              default_factory=list,
                                          )


@dataclasses.dataclass
class GetTagKeysInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pagination_token",
                "PaginationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A string that indicates that additional data is available. Leave this value
    # empty for your initial request. If the response includes a PaginationToken,
    # use that string for this value to request an additional page of data.
    pagination_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetTagKeysOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pagination_token",
                "PaginationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string that indicates that the response contains more data than can be
    # returned in a single response. To receive additional data, specify this
    # string for the `PaginationToken` value in a subsequent request.
    pagination_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of all tag keys in the AWS account.
    tag_keys: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class GetTagValuesInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "pagination_token",
                "PaginationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The key for which you want to list all existing values in the specified
    # region for the AWS account.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A string that indicates that additional data is available. Leave this value
    # empty for your initial request. If the response includes a PaginationToken,
    # use that string for this value to request an additional page of data.
    pagination_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetTagValuesOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pagination_token",
                "PaginationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_values",
                "TagValues",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string that indicates that the response contains more data than can be
    # returned in a single response. To receive additional data, specify this
    # string for the `PaginationToken` value in a subsequent request.
    pagination_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of all tag values for the specified key in the AWS account.
    tag_values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class InternalServiceException(autoboto.ShapeBase):
    """
    The request processing failed because of an unknown error, exception, or
    failure. You can retry the request.
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
    A parameter is missing or a malformed string or invalid or out-of-range value
    was supplied for the request parameter.
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
class PaginationTokenExpiredException(autoboto.ShapeBase):
    """
    A `PaginationToken` is valid for a maximum of 15 minutes. Your request was
    denied because the specified `PaginationToken` has expired.
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
class ResourceTagMapping(autoboto.ShapeBase):
    """
    A list of resource ARNs and the tags (keys and values) that are associated with
    each.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceARN",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # An array of resource ARN(s).
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tags that have been applied to one or more AWS resources.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    """
    The metadata that you apply to AWS resources to help you categorize and organize
    them. Each tag consists of a key and an optional value, both of which you
    define. For more information, see [Tag
    Basics](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-
    basics) in the _Amazon EC2 User Guide for Linux Instances_.
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

    # One part of a key-value pair that make up a tag. A key is a general label
    # that acts like a category for more specific tag values.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The optional part of a key-value pair that make up a tag. A value acts as a
    # descriptor within a tag category (key).
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagFilter(autoboto.ShapeBase):
    """
    A list of tags (keys and values) that are used to specify the associated
    resources.
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

    # One part of a key-value pair that make up a tag. A key is a general label
    # that acts like a category for more specific tag values.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The optional part of a key-value pair that make up a tag. A value acts as a
    # descriptor within a tag category (key).
    values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class TagResourcesInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn_list",
                "ResourceARNList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # A list of ARNs. An ARN (Amazon Resource Name) uniquely identifies a
    # resource. You can specify a minimum of 1 and a maximum of 20 ARNs
    # (resources) to tag. An ARN can be set to a maximum of 1600 characters. For
    # more information, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html) in the _AWS General Reference_.
    resource_arn_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The tags that you want to add to the specified resources. A tag consists of
    # a key and a value that you define.
    tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TagResourcesOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_resources_map",
                "FailedResourcesMap",
                autoboto.TypeInfo(typing.Dict[str, FailureInfo]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Details of resources that could not be tagged. An error code, status code,
    # and error message are returned for each failed item.
    failed_resources_map: typing.Dict[str, "FailureInfo"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ThrottledException(autoboto.ShapeBase):
    """
    The request was denied to limit the frequency of submitted requests.
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
class UntagResourcesInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn_list",
                "ResourceARNList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "tag_keys",
                "TagKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A list of ARNs. An ARN (Amazon Resource Name) uniquely identifies a
    # resource. You can specify a minimum of 1 and a maximum of 20 ARNs
    # (resources) to untag. An ARN can be set to a maximum of 1600 characters.
    # For more information, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html) in the _AWS General Reference_.
    resource_arn_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list of the tag keys that you want to remove from the specified
    # resources.
    tag_keys: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UntagResourcesOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_resources_map",
                "FailedResourcesMap",
                autoboto.TypeInfo(typing.Dict[str, FailureInfo]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Details of resources that could not be untagged. An error code, status
    # code, and error message are returned for each failed item.
    failed_resources_map: typing.Dict[str, "FailureInfo"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
