import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AbortDocumentVersionUploadRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the version.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ActivateUserRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_id",
                "UserId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the user.
    user_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ActivateUserResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user",
                "User",
                autoboto.TypeInfo(User),
            ),
        ]

    # The user information.
    user: "User" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class Activity(autoboto.ShapeBase):
    """
    Describes the activity information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(ActivityType),
            ),
            (
                "time_stamp",
                "TimeStamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "organization_id",
                "OrganizationId",
                autoboto.TypeInfo(str),
            ),
            (
                "initiator",
                "Initiator",
                autoboto.TypeInfo(UserMetadata),
            ),
            (
                "participants",
                "Participants",
                autoboto.TypeInfo(Participants),
            ),
            (
                "resource_metadata",
                "ResourceMetadata",
                autoboto.TypeInfo(ResourceMetadata),
            ),
            (
                "original_parent",
                "OriginalParent",
                autoboto.TypeInfo(ResourceMetadata),
            ),
            (
                "comment_metadata",
                "CommentMetadata",
                autoboto.TypeInfo(CommentMetadata),
            ),
        ]

    # The activity type.
    type: "ActivityType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp when the action was performed.
    time_stamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the organization.
    organization_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The user who performed the action.
    initiator: "UserMetadata" = dataclasses.field(default_factory=dict, )

    # The list of users or groups impacted by this action. This is an optional
    # field and is filled for the following sharing activities: DOCUMENT_SHARED,
    # DOCUMENT_SHARED, DOCUMENT_UNSHARED, FOLDER_SHARED, FOLDER_UNSHARED.
    participants: "Participants" = dataclasses.field(default_factory=dict, )

    # The metadata of the resource involved in the user action.
    resource_metadata: "ResourceMetadata" = dataclasses.field(
        default_factory=dict,
    )

    # The original parent of the resource. This is an optional field and is
    # filled for move activities.
    original_parent: "ResourceMetadata" = dataclasses.field(
        default_factory=dict,
    )

    # Metadata of the commenting activity. This is an optional field and is
    # filled for commenting activities.
    comment_metadata: "CommentMetadata" = dataclasses.field(
        default_factory=dict,
    )


class ActivityType(Enum):
    DOCUMENT_CHECKED_IN = "DOCUMENT_CHECKED_IN"
    DOCUMENT_CHECKED_OUT = "DOCUMENT_CHECKED_OUT"
    DOCUMENT_RENAMED = "DOCUMENT_RENAMED"
    DOCUMENT_VERSION_UPLOADED = "DOCUMENT_VERSION_UPLOADED"
    DOCUMENT_VERSION_DELETED = "DOCUMENT_VERSION_DELETED"
    DOCUMENT_RECYCLED = "DOCUMENT_RECYCLED"
    DOCUMENT_RESTORED = "DOCUMENT_RESTORED"
    DOCUMENT_REVERTED = "DOCUMENT_REVERTED"
    DOCUMENT_SHARED = "DOCUMENT_SHARED"
    DOCUMENT_UNSHARED = "DOCUMENT_UNSHARED"
    DOCUMENT_SHARE_PERMISSION_CHANGED = "DOCUMENT_SHARE_PERMISSION_CHANGED"
    DOCUMENT_SHAREABLE_LINK_CREATED = "DOCUMENT_SHAREABLE_LINK_CREATED"
    DOCUMENT_SHAREABLE_LINK_REMOVED = "DOCUMENT_SHAREABLE_LINK_REMOVED"
    DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED = "DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED"
    DOCUMENT_MOVED = "DOCUMENT_MOVED"
    DOCUMENT_COMMENT_ADDED = "DOCUMENT_COMMENT_ADDED"
    DOCUMENT_COMMENT_DELETED = "DOCUMENT_COMMENT_DELETED"
    DOCUMENT_ANNOTATION_ADDED = "DOCUMENT_ANNOTATION_ADDED"
    DOCUMENT_ANNOTATION_DELETED = "DOCUMENT_ANNOTATION_DELETED"
    FOLDER_CREATED = "FOLDER_CREATED"
    FOLDER_DELETED = "FOLDER_DELETED"
    FOLDER_RENAMED = "FOLDER_RENAMED"
    FOLDER_RECYCLED = "FOLDER_RECYCLED"
    FOLDER_RESTORED = "FOLDER_RESTORED"
    FOLDER_SHARED = "FOLDER_SHARED"
    FOLDER_UNSHARED = "FOLDER_UNSHARED"
    FOLDER_SHARE_PERMISSION_CHANGED = "FOLDER_SHARE_PERMISSION_CHANGED"
    FOLDER_SHAREABLE_LINK_CREATED = "FOLDER_SHAREABLE_LINK_CREATED"
    FOLDER_SHAREABLE_LINK_REMOVED = "FOLDER_SHAREABLE_LINK_REMOVED"
    FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED = "FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED"
    FOLDER_MOVED = "FOLDER_MOVED"


@dataclasses.dataclass
class AddResourcePermissionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "principals",
                "Principals",
                autoboto.TypeInfo(typing.List[SharePrincipal]),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "notification_options",
                "NotificationOptions",
                autoboto.TypeInfo(NotificationOptions),
            ),
        ]

    # The ID of the resource.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The users, groups, or organization being granted permission.
    principals: typing.List["SharePrincipal"] = dataclasses.field(
        default_factory=list,
    )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The notification options.
    notification_options: "NotificationOptions" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class AddResourcePermissionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "share_results",
                "ShareResults",
                autoboto.TypeInfo(typing.List[ShareResult]),
            ),
        ]

    # The share results.
    share_results: typing.List["ShareResult"] = dataclasses.field(
        default_factory=list,
    )


class BooleanEnumType(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"


@dataclasses.dataclass
class Comment(autoboto.ShapeBase):
    """
    Describes a comment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment_id",
                "CommentId",
                autoboto.TypeInfo(str),
            ),
            (
                "parent_id",
                "ParentId",
                autoboto.TypeInfo(str),
            ),
            (
                "thread_id",
                "ThreadId",
                autoboto.TypeInfo(str),
            ),
            (
                "text",
                "Text",
                autoboto.TypeInfo(str),
            ),
            (
                "contributor",
                "Contributor",
                autoboto.TypeInfo(User),
            ),
            (
                "created_timestamp",
                "CreatedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(CommentStatusType),
            ),
            (
                "visibility",
                "Visibility",
                autoboto.TypeInfo(CommentVisibilityType),
            ),
            (
                "recipient_id",
                "RecipientId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the comment.
    comment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the parent comment.
    parent_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the root comment in the thread.
    thread_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The text of the comment.
    text: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The details of the user who made the comment.
    contributor: "User" = dataclasses.field(default_factory=dict, )

    # The time that the comment was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the comment.
    status: "CommentStatusType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The visibility of the comment. Options are either PRIVATE, where the
    # comment is visible only to the comment author and document owner and co-
    # owners, or PUBLIC, where the comment is visible to document owners, co-
    # owners, and contributors.
    visibility: "CommentVisibilityType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the comment is a reply to another user's comment, this field contains
    # the user ID of the user being replied to.
    recipient_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CommentMetadata(autoboto.ShapeBase):
    """
    Describes the metadata of a comment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment_id",
                "CommentId",
                autoboto.TypeInfo(str),
            ),
            (
                "contributor",
                "Contributor",
                autoboto.TypeInfo(User),
            ),
            (
                "created_timestamp",
                "CreatedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "comment_status",
                "CommentStatus",
                autoboto.TypeInfo(CommentStatusType),
            ),
            (
                "recipient_id",
                "RecipientId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the comment.
    comment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user who made the comment.
    contributor: "User" = dataclasses.field(default_factory=dict, )

    # The timestamp that the comment was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the comment.
    comment_status: "CommentStatusType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the user being replied to.
    recipient_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class CommentStatusType(Enum):
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    DELETED = "DELETED"


class CommentVisibilityType(Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"


@dataclasses.dataclass
class ConcurrentModificationException(autoboto.ShapeBase):
    """
    The resource hierarchy is changing.
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
class CreateCommentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "text",
                "Text",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "parent_id",
                "ParentId",
                autoboto.TypeInfo(str),
            ),
            (
                "thread_id",
                "ThreadId",
                autoboto.TypeInfo(str),
            ),
            (
                "visibility",
                "Visibility",
                autoboto.TypeInfo(CommentVisibilityType),
            ),
            (
                "notify_collaborators",
                "NotifyCollaborators",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the document version.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The text of the comment.
    text: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the parent comment.
    parent_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the root comment in the thread.
    thread_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The visibility of the comment. Options are either PRIVATE, where the
    # comment is visible only to the comment author and document owner and co-
    # owners, or PUBLIC, where the comment is visible to document owners, co-
    # owners, and contributors.
    visibility: "CommentVisibilityType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Set this parameter to TRUE to send an email out to the document
    # collaborators after the comment is created.
    notify_collaborators: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateCommentResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment",
                "Comment",
                autoboto.TypeInfo(Comment),
            ),
        ]

    # The comment that has been created.
    comment: "Comment" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateCustomMetadataRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_metadata",
                "CustomMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the resource.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Custom metadata in the form of name-value pairs.
    custom_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the version, if the custom metadata is being added to a document
    # version.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCustomMetadataResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateFolderRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parent_folder_id",
                "ParentFolderId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the parent folder.
    parent_folder_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the new folder.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateFolderResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metadata",
                "Metadata",
                autoboto.TypeInfo(FolderMetadata),
            ),
        ]

    # The metadata of the folder.
    metadata: "FolderMetadata" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateLabelsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the resource.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # List of labels to add to the resource.
    labels: typing.List[str] = dataclasses.field(default_factory=list, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateLabelsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateNotificationSubscriptionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint",
                "Endpoint",
                autoboto.TypeInfo(str),
            ),
            (
                "protocol",
                "Protocol",
                autoboto.TypeInfo(SubscriptionProtocolType),
            ),
            (
                "subscription_type",
                "SubscriptionType",
                autoboto.TypeInfo(SubscriptionType),
            ),
        ]

    # The ID of the organization.
    organization_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The endpoint to receive the notifications. If the protocol is HTTPS, the
    # endpoint is a URL that begins with "https://".
    endpoint: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The protocol to use. The supported value is https, which delivers JSON-
    # encoded messages using HTTPS POST.
    protocol: "SubscriptionProtocolType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The notification type.
    subscription_type: "SubscriptionType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateNotificationSubscriptionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription",
                "Subscription",
                autoboto.TypeInfo(Subscription),
            ),
        ]

    # The subscription.
    subscription: "Subscription" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateUserRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "given_name",
                "GivenName",
                autoboto.TypeInfo(str),
            ),
            (
                "surname",
                "Surname",
                autoboto.TypeInfo(str),
            ),
            (
                "password",
                "Password",
                autoboto.TypeInfo(str),
            ),
            (
                "organization_id",
                "OrganizationId",
                autoboto.TypeInfo(str),
            ),
            (
                "email_address",
                "EmailAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "time_zone_id",
                "TimeZoneId",
                autoboto.TypeInfo(str),
            ),
            (
                "storage_rule",
                "StorageRule",
                autoboto.TypeInfo(StorageRuleType),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The login name of the user.
    username: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The given name of the user.
    given_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The surname of the user.
    surname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The password of the user.
    password: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the organization.
    organization_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The email address of the user.
    email_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time zone ID of the user.
    time_zone_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The amount of storage for the user.
    storage_rule: "StorageRuleType" = dataclasses.field(default_factory=dict, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateUserResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user",
                "User",
                autoboto.TypeInfo(User),
            ),
        ]

    # The user information.
    user: "User" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CustomMetadataLimitExceededException(autoboto.ShapeBase):
    """
    The limit has been reached on the number of custom properties for the specified
    resource.
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
class DeactivateUserRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_id",
                "UserId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the user.
    user_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeactivatingLastSystemUserException(autoboto.ShapeBase):
    """
    The last user in the organization is being deactivated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteCommentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "comment_id",
                "CommentId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the document version.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the comment.
    comment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteCustomMetadataRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "keys",
                "Keys",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "delete_all",
                "DeleteAll",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the resource, either a document or folder.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the version, if the custom metadata is being deleted from a
    # document version.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # List of properties to remove.
    keys: typing.List[str] = dataclasses.field(default_factory=list, )

    # Flag to indicate removal of all custom metadata properties from the
    # specified resource.
    delete_all: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteCustomMetadataResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteDocumentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteFolderContentsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "folder_id",
                "FolderId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the folder.
    folder_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteFolderRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "folder_id",
                "FolderId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the folder.
    folder_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteLabelsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "delete_all",
                "DeleteAll",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the resource.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # List of labels to delete from the resource.
    labels: typing.List[str] = dataclasses.field(default_factory=list, )

    # Flag to request removal of all labels from the specified resource.
    delete_all: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLabelsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteNotificationSubscriptionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_id",
                "SubscriptionId",
                autoboto.TypeInfo(str),
            ),
            (
                "organization_id",
                "OrganizationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the subscription.
    subscription_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the organization.
    organization_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteUserRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_id",
                "UserId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the user.
    user_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeActivitiesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
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
                "organization_id",
                "OrganizationId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp that determines the starting time of the activities. The
    # response includes the activities performed after the specified timestamp.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp that determines the end time of the activities. The response
    # includes the activities performed before the specified timestamp.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the organization. This is a mandatory parameter when using
    # administrative API (SigV4) requests.
    organization_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the user who performed the action. The response includes
    # activities pertaining to this user. This is an optional parameter and is
    # only applicable for administrative API (SigV4) requests.
    user_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The marker for the next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeActivitiesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_activities",
                "UserActivities",
                autoboto.TypeInfo(typing.List[Activity]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of activities for the specified user and time period.
    user_activities: typing.List["Activity"] = dataclasses.field(
        default_factory=list,
    )

    # The marker for the next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCommentsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the document version.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of items to return.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The marker for the next set of results. This marker was received from a
    # previous call.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCommentsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comments",
                "Comments",
                autoboto.TypeInfo(typing.List[Comment]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of comments for the specified document version.
    comments: typing.List["Comment"] = dataclasses.field(default_factory=list, )

    # The marker for the next set of results. This marker was received from a
    # previous call.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDocumentVersionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "include",
                "Include",
                autoboto.TypeInfo(str),
            ),
            (
                "fields",
                "Fields",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of versions to return with this call.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A comma-separated list of values. Specify "INITIALIZED" to include
    # incomplete versions.
    include: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specify "SOURCE" to include initialized versions and a URL for the source
    # document.
    fields: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDocumentVersionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_versions",
                "DocumentVersions",
                autoboto.TypeInfo(typing.List[DocumentVersionMetadata]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The document versions.
    document_versions: typing.List["DocumentVersionMetadata"
                                  ] = dataclasses.field(
                                      default_factory=list,
                                  )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFolderContentsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "folder_id",
                "FolderId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "sort",
                "Sort",
                autoboto.TypeInfo(ResourceSortType),
            ),
            (
                "order",
                "Order",
                autoboto.TypeInfo(OrderType),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(FolderContentType),
            ),
            (
                "include",
                "Include",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the folder.
    folder_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The sorting criteria.
    sort: "ResourceSortType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The order for the contents of the folder.
    order: "OrderType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The marker for the next set of results. This marker was received from a
    # previous call.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of items.
    type: "FolderContentType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The contents to include. Specify "INITIALIZED" to include initialized
    # documents.
    include: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFolderContentsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "folders",
                "Folders",
                autoboto.TypeInfo(typing.List[FolderMetadata]),
            ),
            (
                "documents",
                "Documents",
                autoboto.TypeInfo(typing.List[DocumentMetadata]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The subfolders in the specified folder.
    folders: typing.List["FolderMetadata"] = dataclasses.field(
        default_factory=list,
    )

    # The documents in the specified folder.
    documents: typing.List["DocumentMetadata"] = dataclasses.field(
        default_factory=list,
    )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeGroupsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "search_query",
                "SearchQuery",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "organization_id",
                "OrganizationId",
                autoboto.TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # A query to describe groups by group name.
    search_query: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the organization.
    organization_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeGroupsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "groups",
                "Groups",
                autoboto.TypeInfo(typing.List[GroupMetadata]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of groups.
    groups: typing.List["GroupMetadata"] = dataclasses.field(
        default_factory=list,
    )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeNotificationSubscriptionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_id",
                "OrganizationId",
                autoboto.TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the organization.
    organization_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeNotificationSubscriptionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscriptions",
                "Subscriptions",
                autoboto.TypeInfo(typing.List[Subscription]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The subscriptions.
    subscriptions: typing.List["Subscription"] = dataclasses.field(
        default_factory=list,
    )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeResourcePermissionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "principal_id",
                "PrincipalId",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the resource.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the principal to filter permissions by.
    principal_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The marker for the next set of results. (You received this marker from a
    # previous call)
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeResourcePermissionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "principals",
                "Principals",
                autoboto.TypeInfo(typing.List[Principal]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The principals.
    principals: typing.List["Principal"] = dataclasses.field(
        default_factory=list,
    )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRootFoldersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of items to return.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRootFoldersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "folders",
                "Folders",
                autoboto.TypeInfo(typing.List[FolderMetadata]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user's special folders.
    folders: typing.List["FolderMetadata"] = dataclasses.field(
        default_factory=list,
    )

    # The marker for the next set of results.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeUsersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "organization_id",
                "OrganizationId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_ids",
                "UserIds",
                autoboto.TypeInfo(str),
            ),
            (
                "query",
                "Query",
                autoboto.TypeInfo(str),
            ),
            (
                "include",
                "Include",
                autoboto.TypeInfo(UserFilterType),
            ),
            (
                "order",
                "Order",
                autoboto.TypeInfo(OrderType),
            ),
            (
                "sort",
                "Sort",
                autoboto.TypeInfo(UserSortType),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "fields",
                "Fields",
                autoboto.TypeInfo(str),
            ),
        ]

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the organization.
    organization_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The IDs of the users.
    user_ids: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A query to filter users by user name.
    query: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The state of the users. Specify "ALL" to include inactive users.
    include: "UserFilterType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The order for the results.
    order: "OrderType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The sorting criteria.
    sort: "UserSortType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A comma-separated list of values. Specify "STORAGE_METADATA" to include the
    # user storage quota and utilization information.
    fields: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeUsersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "users",
                "Users",
                autoboto.TypeInfo(typing.List[User]),
            ),
            (
                "total_number_of_users",
                "TotalNumberOfUsers",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The users.
    users: typing.List["User"] = dataclasses.field(default_factory=list, )

    # The total number of users included in the results.
    total_number_of_users: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DocumentLockedForCommentsException(autoboto.ShapeBase):
    """
    This exception is thrown when the document is locked for comments and user tries
    to create or delete a comment on that document.
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
class DocumentMetadata(autoboto.ShapeBase):
    """
    Describes the document.
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
                "creator_id",
                "CreatorId",
                autoboto.TypeInfo(str),
            ),
            (
                "parent_folder_id",
                "ParentFolderId",
                autoboto.TypeInfo(str),
            ),
            (
                "created_timestamp",
                "CreatedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "modified_timestamp",
                "ModifiedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "latest_version_metadata",
                "LatestVersionMetadata",
                autoboto.TypeInfo(DocumentVersionMetadata),
            ),
            (
                "resource_state",
                "ResourceState",
                autoboto.TypeInfo(ResourceStateType),
            ),
            (
                "labels",
                "Labels",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the document.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the creator.
    creator_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the parent folder.
    parent_folder_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time when the document was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time when the document was updated.
    modified_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The latest version of the document.
    latest_version_metadata: "DocumentVersionMetadata" = dataclasses.field(
        default_factory=dict,
    )

    # The resource state.
    resource_state: "ResourceStateType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # List of labels on the document.
    labels: typing.List[str] = dataclasses.field(default_factory=list, )


class DocumentSourceType(Enum):
    ORIGINAL = "ORIGINAL"
    WITH_COMMENTS = "WITH_COMMENTS"


class DocumentStatusType(Enum):
    INITIALIZED = "INITIALIZED"
    ACTIVE = "ACTIVE"


class DocumentThumbnailType(Enum):
    SMALL = "SMALL"
    SMALL_HQ = "SMALL_HQ"
    LARGE = "LARGE"


@dataclasses.dataclass
class DocumentVersionMetadata(autoboto.ShapeBase):
    """
    Describes a version of a document.
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
                "content_type",
                "ContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "size",
                "Size",
                autoboto.TypeInfo(int),
            ),
            (
                "signature",
                "Signature",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(DocumentStatusType),
            ),
            (
                "created_timestamp",
                "CreatedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "modified_timestamp",
                "ModifiedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "content_created_timestamp",
                "ContentCreatedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "content_modified_timestamp",
                "ContentModifiedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creator_id",
                "CreatorId",
                autoboto.TypeInfo(str),
            ),
            (
                "thumbnail",
                "Thumbnail",
                autoboto.TypeInfo(typing.Dict[DocumentThumbnailType, str]),
            ),
            (
                "source",
                "Source",
                autoboto.TypeInfo(typing.Dict[DocumentSourceType, str]),
            ),
        ]

    # The ID of the version.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the version.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The content type of the document.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The size of the document, in bytes.
    size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The signature of the document.
    signature: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the document.
    status: "DocumentStatusType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp when the document was first uploaded.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp when the document was last uploaded.
    modified_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp when the content of the document was originally created.
    content_created_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp when the content of the document was modified.
    content_modified_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the creator.
    creator_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The thumbnail of the document.
    thumbnail: typing.Dict["DocumentThumbnailType", str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The source of the document.
    source: typing.Dict["DocumentSourceType", str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class DocumentVersionStatus(Enum):
    ACTIVE = "ACTIVE"


@dataclasses.dataclass
class DraftUploadOutOfSyncException(autoboto.ShapeBase):
    """
    This exception is thrown when a valid checkout ID is not presented on document
    version upload calls for a document that has been checked out from Web client.
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
class EntityAlreadyExistsException(autoboto.ShapeBase):
    """
    The resource already exists.
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
class EntityNotExistsException(autoboto.ShapeBase):
    """
    The resource does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "entity_ids",
                "EntityIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    entity_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class FailedDependencyException(autoboto.ShapeBase):
    """
    The AWS Directory Service cannot reach an on-premises instance. Or a dependency
    under the control of the organization is failing, such as a connected Active
    Directory.
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


class FolderContentType(Enum):
    ALL = "ALL"
    DOCUMENT = "DOCUMENT"
    FOLDER = "FOLDER"


@dataclasses.dataclass
class FolderMetadata(autoboto.ShapeBase):
    """
    Describes a folder.
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
                "creator_id",
                "CreatorId",
                autoboto.TypeInfo(str),
            ),
            (
                "parent_folder_id",
                "ParentFolderId",
                autoboto.TypeInfo(str),
            ),
            (
                "created_timestamp",
                "CreatedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "modified_timestamp",
                "ModifiedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "resource_state",
                "ResourceState",
                autoboto.TypeInfo(ResourceStateType),
            ),
            (
                "signature",
                "Signature",
                autoboto.TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "size",
                "Size",
                autoboto.TypeInfo(int),
            ),
            (
                "latest_version_size",
                "LatestVersionSize",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the folder.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the folder.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the creator.
    creator_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the parent folder.
    parent_folder_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time when the folder was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time when the folder was updated.
    modified_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The resource state of the folder.
    resource_state: "ResourceStateType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The unique identifier created from the subfolders and documents of the
    # folder.
    signature: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # List of labels on the folder.
    labels: typing.List[str] = dataclasses.field(default_factory=list, )

    # The size of the folder metadata.
    size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The size of the latest version of the folder metadata.
    latest_version_size: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetCurrentUserRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetCurrentUserResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user",
                "User",
                autoboto.TypeInfo(User),
            ),
        ]

    # Metadata of the user.
    user: "User" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetDocumentPathRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "fields",
                "Fields",
                autoboto.TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of levels in the hierarchy to return.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A comma-separated list of values. Specify `NAME` to include the names of
    # the parent folders.
    fields: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This value is not supported.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDocumentPathResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                autoboto.TypeInfo(ResourcePath),
            ),
        ]

    # The path information.
    path: "ResourcePath" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetDocumentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "include_custom_metadata",
                "IncludeCustomMetadata",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Set this to `TRUE` to include custom metadata in the response.
    include_custom_metadata: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDocumentResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metadata",
                "Metadata",
                autoboto.TypeInfo(DocumentMetadata),
            ),
            (
                "custom_metadata",
                "CustomMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The metadata details of the document.
    metadata: "DocumentMetadata" = dataclasses.field(default_factory=dict, )

    # The custom metadata on the document.
    custom_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDocumentVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "fields",
                "Fields",
                autoboto.TypeInfo(str),
            ),
            (
                "include_custom_metadata",
                "IncludeCustomMetadata",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version ID of the document.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A comma-separated list of values. Specify "SOURCE" to include a URL for the
    # source document.
    fields: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Set this to TRUE to include custom metadata in the response.
    include_custom_metadata: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDocumentVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metadata",
                "Metadata",
                autoboto.TypeInfo(DocumentVersionMetadata),
            ),
            (
                "custom_metadata",
                "CustomMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The version metadata.
    metadata: "DocumentVersionMetadata" = dataclasses.field(
        default_factory=dict,
    )

    # The custom metadata on the document version.
    custom_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetFolderPathRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "folder_id",
                "FolderId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
            (
                "fields",
                "Fields",
                autoboto.TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the folder.
    folder_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of levels in the hierarchy to return.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A comma-separated list of values. Specify "NAME" to include the names of
    # the parent folders.
    fields: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This value is not supported.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFolderPathResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                autoboto.TypeInfo(ResourcePath),
            ),
        ]

    # The path information.
    path: "ResourcePath" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetFolderRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "folder_id",
                "FolderId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "include_custom_metadata",
                "IncludeCustomMetadata",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the folder.
    folder_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Set to TRUE to include custom metadata in the response.
    include_custom_metadata: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetFolderResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metadata",
                "Metadata",
                autoboto.TypeInfo(FolderMetadata),
            ),
            (
                "custom_metadata",
                "CustomMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The metadata of the folder.
    metadata: "FolderMetadata" = dataclasses.field(default_factory=dict, )

    # The custom metadata on the folder.
    custom_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GroupMetadata(autoboto.ShapeBase):
    """
    Describes the metadata of a user group.
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
        ]

    # The ID of the user group.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the group.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IllegalUserStateException(autoboto.ShapeBase):
    """
    The user is undergoing transfer of ownership.
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
class InitiateDocumentVersionUploadRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parent_folder_id",
                "ParentFolderId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
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
                "content_created_timestamp",
                "ContentCreatedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "content_modified_timestamp",
                "ContentModifiedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "content_type",
                "ContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "document_size_in_bytes",
                "DocumentSizeInBytes",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the parent folder.
    parent_folder_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the document.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The timestamp when the content of the document was originally created.
    content_created_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp when the content of the document was modified.
    content_modified_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The content type of the document.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The size of the document, in bytes.
    document_size_in_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InitiateDocumentVersionUploadResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metadata",
                "Metadata",
                autoboto.TypeInfo(DocumentMetadata),
            ),
            (
                "upload_metadata",
                "UploadMetadata",
                autoboto.TypeInfo(UploadMetadata),
            ),
        ]

    # The document metadata.
    metadata: "DocumentMetadata" = dataclasses.field(default_factory=dict, )

    # The upload metadata.
    upload_metadata: "UploadMetadata" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class InvalidArgumentException(autoboto.ShapeBase):
    """
    The pagination marker or limit fields are not valid.
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
class InvalidOperationException(autoboto.ShapeBase):
    """
    The operation is invalid.
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
class InvalidPasswordException(autoboto.ShapeBase):
    """
    The password is invalid.
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
class LimitExceededException(autoboto.ShapeBase):
    """
    The maximum of 100,000 folders under the parent folder has been exceeded.
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


class LocaleType(Enum):
    en = "en"
    fr = "fr"
    ko = "ko"
    de = "de"
    es = "es"
    ja = "ja"
    ru = "ru"
    zh_CN = "zh_CN"
    zh_TW = "zh_TW"
    pt_BR = "pt_BR"
    default = "default"


@dataclasses.dataclass
class NotificationOptions(autoboto.ShapeBase):
    """
    Set of options which defines notification preferences of given action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "send_email",
                "SendEmail",
                autoboto.TypeInfo(bool),
            ),
            (
                "email_message",
                "EmailMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # Boolean value to indicate an email notification should be sent to the
    # receipients.
    send_email: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Text value to be included in the email body.
    email_message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class OrderType(Enum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


@dataclasses.dataclass
class Participants(autoboto.ShapeBase):
    """
    Describes the users or user groups.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "users",
                "Users",
                autoboto.TypeInfo(typing.List[UserMetadata]),
            ),
            (
                "groups",
                "Groups",
                autoboto.TypeInfo(typing.List[GroupMetadata]),
            ),
        ]

    # The list of users.
    users: typing.List["UserMetadata"] = dataclasses.field(
        default_factory=list,
    )

    # The list of user groups.
    groups: typing.List["GroupMetadata"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class PermissionInfo(autoboto.ShapeBase):
    """
    Describes the permissions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role",
                "Role",
                autoboto.TypeInfo(RoleType),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(RolePermissionType),
            ),
        ]

    # The role of the user.
    role: "RoleType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of permissions.
    type: "RolePermissionType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Principal(autoboto.ShapeBase):
    """
    Describes a resource.
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
                "type",
                "Type",
                autoboto.TypeInfo(PrincipalType),
            ),
            (
                "roles",
                "Roles",
                autoboto.TypeInfo(typing.List[PermissionInfo]),
            ),
        ]

    # The ID of the resource.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of resource.
    type: "PrincipalType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The permission information for the resource.
    roles: typing.List["PermissionInfo"] = dataclasses.field(
        default_factory=list,
    )


class PrincipalType(Enum):
    USER = "USER"
    GROUP = "GROUP"
    INVITE = "INVITE"
    ANONYMOUS = "ANONYMOUS"
    ORGANIZATION = "ORGANIZATION"


@dataclasses.dataclass
class ProhibitedStateException(autoboto.ShapeBase):
    """
    The specified document version is not in the INITIALIZED state.
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
class RemoveAllResourcePermissionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the resource.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveResourcePermissionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "principal_id",
                "PrincipalId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "principal_type",
                "PrincipalType",
                autoboto.TypeInfo(PrincipalType),
            ),
        ]

    # The ID of the resource.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The principal ID of the resource.
    principal_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The principal type of the resource.
    principal_type: "PrincipalType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceAlreadyCheckedOutException(autoboto.ShapeBase):
    """
    The resource is already checked out.
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
class ResourceMetadata(autoboto.ShapeBase):
    """
    Describes the metadata of a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "original_name",
                "OriginalName",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(UserMetadata),
            ),
            (
                "parent_id",
                "ParentId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of resource.
    type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the resource.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The original name of the resource before a rename operation.
    original_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the resource.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version ID of the resource. This is an optional field and is filled for
    # action on document version.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The owner of the resource.
    owner: "UserMetadata" = dataclasses.field(default_factory=dict, )

    # The parent ID of the resource before a rename operation.
    parent_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourcePath(autoboto.ShapeBase):
    """
    Describes the path information of a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "components",
                "Components",
                autoboto.TypeInfo(typing.List[ResourcePathComponent]),
            ),
        ]

    # The components of the resource path.
    components: typing.List["ResourcePathComponent"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ResourcePathComponent(autoboto.ShapeBase):
    """
    Describes the resource path.
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
        ]

    # The ID of the resource path.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the resource path.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ResourceSortType(Enum):
    DATE = "DATE"
    NAME = "NAME"


class ResourceStateType(Enum):
    ACTIVE = "ACTIVE"
    RESTORING = "RESTORING"
    RECYCLING = "RECYCLING"
    RECYCLED = "RECYCLED"


class ResourceType(Enum):
    FOLDER = "FOLDER"
    DOCUMENT = "DOCUMENT"


class RolePermissionType(Enum):
    DIRECT = "DIRECT"
    INHERITED = "INHERITED"


class RoleType(Enum):
    VIEWER = "VIEWER"
    CONTRIBUTOR = "CONTRIBUTOR"
    OWNER = "OWNER"
    COOWNER = "COOWNER"


@dataclasses.dataclass
class ServiceUnavailableException(autoboto.ShapeBase):
    """
    One or more of the dependencies is unavailable.
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
class SharePrincipal(autoboto.ShapeBase):
    """
    Describes the recipient type and ID, if available.
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
                "type",
                "Type",
                autoboto.TypeInfo(PrincipalType),
            ),
            (
                "role",
                "Role",
                autoboto.TypeInfo(RoleType),
            ),
        ]

    # The ID of the recipient.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of the recipient.
    type: "PrincipalType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The role of the recipient.
    role: "RoleType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ShareResult(autoboto.ShapeBase):
    """
    Describes the share results of a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "principal_id",
                "PrincipalId",
                autoboto.TypeInfo(str),
            ),
            (
                "role",
                "Role",
                autoboto.TypeInfo(RoleType),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(ShareStatusType),
            ),
            (
                "share_id",
                "ShareId",
                autoboto.TypeInfo(str),
            ),
            (
                "status_message",
                "StatusMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the principal.
    principal_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The role.
    role: "RoleType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status.
    status: "ShareStatusType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the resource that was shared.
    share_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status message.
    status_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ShareStatusType(Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


@dataclasses.dataclass
class StorageLimitExceededException(autoboto.ShapeBase):
    """
    The storage limit has been exceeded.
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
class StorageLimitWillExceedException(autoboto.ShapeBase):
    """
    The storage limit will be exceeded.
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
class StorageRuleType(autoboto.ShapeBase):
    """
    Describes the storage for a user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "storage_allocated_in_bytes",
                "StorageAllocatedInBytes",
                autoboto.TypeInfo(int),
            ),
            (
                "storage_type",
                "StorageType",
                autoboto.TypeInfo(StorageType),
            ),
        ]

    # The amount of storage allocated, in bytes.
    storage_allocated_in_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of storage.
    storage_type: "StorageType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class StorageType(Enum):
    UNLIMITED = "UNLIMITED"
    QUOTA = "QUOTA"


@dataclasses.dataclass
class Subscription(autoboto.ShapeBase):
    """
    Describes a subscription.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_id",
                "SubscriptionId",
                autoboto.TypeInfo(str),
            ),
            (
                "end_point",
                "EndPoint",
                autoboto.TypeInfo(str),
            ),
            (
                "protocol",
                "Protocol",
                autoboto.TypeInfo(SubscriptionProtocolType),
            ),
        ]

    # The ID of the subscription.
    subscription_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The endpoint of the subscription.
    end_point: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The protocol of the subscription.
    protocol: "SubscriptionProtocolType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class SubscriptionProtocolType(Enum):
    HTTPS = "HTTPS"


class SubscriptionType(Enum):
    ALL = "ALL"


@dataclasses.dataclass
class TooManyLabelsException(autoboto.ShapeBase):
    """
    The limit has been reached on the number of labels for the specified resource.
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
class TooManySubscriptionsException(autoboto.ShapeBase):
    """
    You've reached the limit on the number of subscriptions for the WorkDocs
    instance.
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
class UnauthorizedOperationException(autoboto.ShapeBase):
    """
    The operation is not permitted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UnauthorizedResourceAccessException(autoboto.ShapeBase):
    """
    The caller does not have access to perform the action on the resource.
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
class UpdateDocumentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "parent_folder_id",
                "ParentFolderId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_state",
                "ResourceState",
                autoboto.TypeInfo(ResourceStateType),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the document.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the parent folder.
    parent_folder_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The resource state of the document. Only ACTIVE and RECYCLED are supported.
    resource_state: "ResourceStateType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateDocumentVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_id",
                "DocumentId",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "version_status",
                "VersionStatus",
                autoboto.TypeInfo(DocumentVersionStatus),
            ),
        ]

    # The ID of the document.
    document_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version ID of the document.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the version.
    version_status: "DocumentVersionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateFolderRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "folder_id",
                "FolderId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "parent_folder_id",
                "ParentFolderId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_state",
                "ResourceState",
                autoboto.TypeInfo(ResourceStateType),
            ),
        ]

    # The ID of the folder.
    folder_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the folder.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the parent folder.
    parent_folder_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The resource state of the folder. Only ACTIVE and RECYCLED are accepted
    # values from the API.
    resource_state: "ResourceStateType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateUserRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_id",
                "UserId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_token",
                "AuthenticationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "given_name",
                "GivenName",
                autoboto.TypeInfo(str),
            ),
            (
                "surname",
                "Surname",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(UserType),
            ),
            (
                "storage_rule",
                "StorageRule",
                autoboto.TypeInfo(StorageRuleType),
            ),
            (
                "time_zone_id",
                "TimeZoneId",
                autoboto.TypeInfo(str),
            ),
            (
                "locale",
                "Locale",
                autoboto.TypeInfo(LocaleType),
            ),
            (
                "grant_poweruser_privileges",
                "GrantPoweruserPrivileges",
                autoboto.TypeInfo(BooleanEnumType),
            ),
        ]

    # The ID of the user.
    user_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon WorkDocs authentication token. Do not set this field when using
    # administrative API actions, as in accessing the API using AWS credentials.
    authentication_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The given name of the user.
    given_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The surname of the user.
    surname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of the user.
    type: "UserType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The amount of storage for the user.
    storage_rule: "StorageRuleType" = dataclasses.field(default_factory=dict, )

    # The time zone ID of the user.
    time_zone_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The locale of the user.
    locale: "LocaleType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Boolean value to determine whether the user is granted Poweruser
    # privileges.
    grant_poweruser_privileges: "BooleanEnumType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateUserResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user",
                "User",
                autoboto.TypeInfo(User),
            ),
        ]

    # The user information.
    user: "User" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UploadMetadata(autoboto.ShapeBase):
    """
    Describes the upload.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "upload_url",
                "UploadUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "signed_headers",
                "SignedHeaders",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The URL of the upload.
    upload_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The signed headers.
    signed_headers: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class User(autoboto.ShapeBase):
    """
    Describes a user.
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
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "email_address",
                "EmailAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "given_name",
                "GivenName",
                autoboto.TypeInfo(str),
            ),
            (
                "surname",
                "Surname",
                autoboto.TypeInfo(str),
            ),
            (
                "organization_id",
                "OrganizationId",
                autoboto.TypeInfo(str),
            ),
            (
                "root_folder_id",
                "RootFolderId",
                autoboto.TypeInfo(str),
            ),
            (
                "recycle_bin_folder_id",
                "RecycleBinFolderId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(UserStatusType),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(UserType),
            ),
            (
                "created_timestamp",
                "CreatedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "modified_timestamp",
                "ModifiedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "time_zone_id",
                "TimeZoneId",
                autoboto.TypeInfo(str),
            ),
            (
                "locale",
                "Locale",
                autoboto.TypeInfo(LocaleType),
            ),
            (
                "storage",
                "Storage",
                autoboto.TypeInfo(UserStorageMetadata),
            ),
        ]

    # The ID of the user.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The login name of the user.
    username: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The email address of the user.
    email_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The given name of the user.
    given_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The surname of the user.
    surname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the organization.
    organization_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the root folder.
    root_folder_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the recycle bin folder.
    recycle_bin_folder_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the user.
    status: "UserStatusType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of user.
    type: "UserType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time when the user was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time when the user was modified.
    modified_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time zone ID of the user.
    time_zone_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The locale of the user.
    locale: "LocaleType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The storage for the user.
    storage: "UserStorageMetadata" = dataclasses.field(default_factory=dict, )


class UserFilterType(Enum):
    ALL = "ALL"
    ACTIVE_PENDING = "ACTIVE_PENDING"


@dataclasses.dataclass
class UserMetadata(autoboto.ShapeBase):
    """
    Describes the metadata of the user.
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
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
            (
                "given_name",
                "GivenName",
                autoboto.TypeInfo(str),
            ),
            (
                "surname",
                "Surname",
                autoboto.TypeInfo(str),
            ),
            (
                "email_address",
                "EmailAddress",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the user.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the user.
    username: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The given name of the user before a rename operation.
    given_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The surname of the user.
    surname: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The email address of the user.
    email_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class UserSortType(Enum):
    USER_NAME = "USER_NAME"
    FULL_NAME = "FULL_NAME"
    STORAGE_LIMIT = "STORAGE_LIMIT"
    USER_STATUS = "USER_STATUS"
    STORAGE_USED = "STORAGE_USED"


class UserStatusType(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    PENDING = "PENDING"


@dataclasses.dataclass
class UserStorageMetadata(autoboto.ShapeBase):
    """
    Describes the storage for a user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "storage_utilized_in_bytes",
                "StorageUtilizedInBytes",
                autoboto.TypeInfo(int),
            ),
            (
                "storage_rule",
                "StorageRule",
                autoboto.TypeInfo(StorageRuleType),
            ),
        ]

    # The amount of storage used, in bytes.
    storage_utilized_in_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The storage for a user.
    storage_rule: "StorageRuleType" = dataclasses.field(default_factory=dict, )


class UserType(Enum):
    USER = "USER"
    ADMIN = "ADMIN"
    POWERUSER = "POWERUSER"
    MINIMALUSER = "MINIMALUSER"
    WORKSPACESUSER = "WORKSPACESUSER"
