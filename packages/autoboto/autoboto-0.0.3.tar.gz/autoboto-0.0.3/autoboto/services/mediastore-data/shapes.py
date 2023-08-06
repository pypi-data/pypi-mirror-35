import datetime
import typing
import autoboto
from enum import Enum
import botocore.response
import dataclasses


@dataclasses.dataclass
class ContainerNotFoundException(autoboto.ShapeBase):
    """
    The specified container was not found for the specified account.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteObjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                autoboto.TypeInfo(str),
            ),
        ]

    # The path (including the file name) where the object is stored in the
    # container. Format: <folder name>/<folder name>/<file name>
    path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteObjectResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeObjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                autoboto.TypeInfo(str),
            ),
        ]

    # The path (including the file name) where the object is stored in the
    # container. Format: <folder name>/<folder name>/<file name>
    path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeObjectResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "e_tag",
                "ETag",
                autoboto.TypeInfo(str),
            ),
            (
                "content_type",
                "ContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "content_length",
                "ContentLength",
                autoboto.TypeInfo(int),
            ),
            (
                "cache_control",
                "CacheControl",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ETag that represents a unique instance of the object.
    e_tag: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The content type of the object.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The length of the object in bytes.
    content_length: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An optional `CacheControl` header that allows the caller to control the
    # object's cache behavior. Headers can be passed in as specified in the HTTP
    # at <https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>.

    # Headers with a custom user-defined value are also accepted.
    cache_control: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time that the object was last modified.
    last_modified: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetObjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                autoboto.TypeInfo(str),
            ),
            (
                "range",
                "Range",
                autoboto.TypeInfo(str),
            ),
        ]

    # The path (including the file name) where the object is stored in the
    # container. Format: <folder name>/<folder name>/<file name>

    # For example, to upload the file `mlaw.avi` to the folder path
    # `premium\canada` in the container `movies`, enter the path
    # `premium/canada/mlaw.avi`.

    # Do not include the container name in this path.

    # If the path includes any folders that don't exist yet, the service creates
    # them. For example, suppose you have an existing `premium/usa` subfolder. If
    # you specify `premium/canada`, the service creates a `canada` subfolder in
    # the `premium` folder. You then have two subfolders, `usa` and `canada`, in
    # the `premium` folder.

    # There is no correlation between the path to the source and the path
    # (folders) in the container in AWS Elemental MediaStore.

    # For more information about folders and how they exist in a container, see
    # the [AWS Elemental MediaStore User
    # Guide](http://docs.aws.amazon.com/mediastore/latest/ug/).

    # The file name is the name that is assigned to the file that you upload. The
    # file can have the same name inside and outside of AWS Elemental MediaStore,
    # or it can have the same name. The file name can include or omit an
    # extension.
    path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The range bytes of an object to retrieve. For more information about the
    # `Range` header, go to
    # <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35>.
    range: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetObjectResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status_code",
                "StatusCode",
                autoboto.TypeInfo(int),
            ),
            (
                "body",
                "Body",
                autoboto.TypeInfo(typing.Any),
            ),
            (
                "cache_control",
                "CacheControl",
                autoboto.TypeInfo(str),
            ),
            (
                "content_range",
                "ContentRange",
                autoboto.TypeInfo(str),
            ),
            (
                "content_length",
                "ContentLength",
                autoboto.TypeInfo(int),
            ),
            (
                "content_type",
                "ContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "e_tag",
                "ETag",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The HTML status code of the request. Status codes ranging from 200 to 299
    # indicate success. All other status codes indicate the type of error that
    # occurred.
    status_code: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The bytes of the object.
    body: typing.Any = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An optional `CacheControl` header that allows the caller to control the
    # object's cache behavior. Headers can be passed in as specified in the HTTP
    # spec at <https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>.

    # Headers with a custom user-defined value are also accepted.
    cache_control: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The range of bytes to retrieve.
    content_range: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The length of the object in bytes.
    content_length: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The content type of the object.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ETag that represents a unique instance of the object.
    e_tag: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date and time that the object was last modified.
    last_modified: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class InternalServerError(autoboto.ShapeBase):
    """
    The service is temporarily unavailable.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Item(autoboto.ShapeBase):
    """
    A metadata entry for a folder or object.
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
                "type",
                "Type",
                autoboto.TypeInfo(ItemType),
            ),
            (
                "e_tag",
                "ETag",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "content_type",
                "ContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "content_length",
                "ContentLength",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the item.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The item type (folder or object).
    type: "ItemType" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ETag that represents a unique instance of the item.
    e_tag: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date and time that the item was last modified.
    last_modified: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The content type of the item.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The length of the item in bytes.
    content_length: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class ItemType(Enum):
    OBJECT = "OBJECT"
    FOLDER = "FOLDER"


@dataclasses.dataclass
class ListItemsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
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

    # The path in the container from which to retrieve items. Format: <folder
    # name>/<folder name>/<file name>
    path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum results to return. The service might return fewer results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The `NextToken` received in the `ListItemsResponse` for the same container
    # and path. Tokens expire after 15 minutes.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListItemsResponse(autoboto.ShapeBase):
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

    # Metadata entries for the folders and objects at the requested path.
    items: typing.List["Item"] = dataclasses.field(default_factory=list, )

    # The `NextToken` used to request the next page of results using `ListItems`.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ObjectNotFoundException(autoboto.ShapeBase):
    """
    Could not perform an operation on an object that does not exist.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class PayloadBlob(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class PutObjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body",
                "Body",
                autoboto.TypeInfo(typing.Any),
            ),
            (
                "path",
                "Path",
                autoboto.TypeInfo(str),
            ),
            (
                "content_type",
                "ContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "cache_control",
                "CacheControl",
                autoboto.TypeInfo(str),
            ),
            (
                "storage_class",
                "StorageClass",
                autoboto.TypeInfo(StorageClass),
            ),
        ]

    # The bytes to be stored.
    body: typing.Any = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The path (including the file name) where the object is stored in the
    # container. Format: <folder name>/<folder name>/<file name>

    # For example, to upload the file `mlaw.avi` to the folder path
    # `premium\canada` in the container `movies`, enter the path
    # `premium/canada/mlaw.avi`.

    # Do not include the container name in this path.

    # If the path includes any folders that don't exist yet, the service creates
    # them. For example, suppose you have an existing `premium/usa` subfolder. If
    # you specify `premium/canada`, the service creates a `canada` subfolder in
    # the `premium` folder. You then have two subfolders, `usa` and `canada`, in
    # the `premium` folder.

    # There is no correlation between the path to the source and the path
    # (folders) in the container in AWS Elemental MediaStore.

    # For more information about folders and how they exist in a container, see
    # the [AWS Elemental MediaStore User
    # Guide](http://docs.aws.amazon.com/mediastore/latest/ug/).

    # The file name is the name that is assigned to the file that you upload. The
    # file can have the same name inside and outside of AWS Elemental MediaStore,
    # or it can have the same name. The file name can include or omit an
    # extension.
    path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The content type of the object.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An optional `CacheControl` header that allows the caller to control the
    # object's cache behavior. Headers can be passed in as specified in the HTTP
    # at <https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>.

    # Headers with a custom user-defined value are also accepted.
    cache_control: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates the storage class of a `Put` request. Defaults to high-
    # performance temporal storage class, and objects are persisted into durable
    # storage shortly after being received.
    storage_class: "StorageClass" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PutObjectResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "content_sha256",
                "ContentSHA256",
                autoboto.TypeInfo(str),
            ),
            (
                "e_tag",
                "ETag",
                autoboto.TypeInfo(str),
            ),
            (
                "storage_class",
                "StorageClass",
                autoboto.TypeInfo(StorageClass),
            ),
        ]

    # The SHA256 digest of the object that is persisted.
    content_sha256: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Unique identifier of the object in the container.
    e_tag: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The storage class where the object was persisted. Should be “Temporal”.
    storage_class: "StorageClass" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RequestedRangeNotSatisfiableException(autoboto.ShapeBase):
    """
    The requested content range is not valid.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class StorageClass(Enum):
    TEMPORAL = "TEMPORAL"
