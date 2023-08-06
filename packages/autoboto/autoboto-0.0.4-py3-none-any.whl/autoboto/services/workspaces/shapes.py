import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AccessDeniedException(autoboto.ShapeBase):
    """
    The user is not authorized to access a resource.
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
class AssociateIpGroupsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                autoboto.TypeInfo(str),
            ),
            (
                "group_ids",
                "GroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the directory.
    directory_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The IDs of one or more IP access control groups.
    group_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class AssociateIpGroupsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AuthorizeIpRulesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_rules",
                "UserRules",
                autoboto.TypeInfo(typing.List[IpRuleItem]),
            ),
        ]

    # The ID of the group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The rules to add to the group.
    user_rules: typing.List["IpRuleItem"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AuthorizeIpRulesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


class Compute(Enum):
    VALUE = "VALUE"
    STANDARD = "STANDARD"
    PERFORMANCE = "PERFORMANCE"
    POWER = "POWER"
    GRAPHICS = "GRAPHICS"


@dataclasses.dataclass
class ComputeType(autoboto.ShapeBase):
    """
    Information about the compute type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(Compute),
            ),
        ]

    # The compute type.
    name: "Compute" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ConnectionState(Enum):
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
    UNKNOWN = "UNKNOWN"


@dataclasses.dataclass
class CreateIpGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_name",
                "GroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "group_desc",
                "GroupDesc",
                autoboto.TypeInfo(str),
            ),
            (
                "user_rules",
                "UserRules",
                autoboto.TypeInfo(typing.List[IpRuleItem]),
            ),
        ]

    # The name of the group.
    group_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the group.
    group_desc: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The rules to add to the group.
    user_rules: typing.List["IpRuleItem"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateIpGroupResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTagsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The ID of the WorkSpace. To find this ID, use DescribeWorkspaces.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tags. Each WorkSpace can have a maximum of 50 tags.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateTagsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateWorkspacesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspaces",
                "Workspaces",
                autoboto.TypeInfo(typing.List[WorkspaceRequest]),
            ),
        ]

    # The WorkSpaces to create. You can specify up to 25 WorkSpaces.
    workspaces: typing.List["WorkspaceRequest"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateWorkspacesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failed_requests",
                "FailedRequests",
                autoboto.TypeInfo(typing.List[FailedCreateWorkspaceRequest]),
            ),
            (
                "pending_requests",
                "PendingRequests",
                autoboto.TypeInfo(typing.List[Workspace]),
            ),
        ]

    # Information about the WorkSpaces that could not be created.
    failed_requests: typing.List["FailedCreateWorkspaceRequest"
                                ] = dataclasses.field(
                                    default_factory=list,
                                )

    # Information about the WorkSpaces that were created.

    # Because this operation is asynchronous, the identifier returned is not
    # immediately available for use with other operations. For example, if you
    # call DescribeWorkspaces before the WorkSpace is created, the information
    # returned can be incomplete.
    pending_requests: typing.List["Workspace"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DefaultWorkspaceCreationProperties(autoboto.ShapeBase):
    """
    Information about defaults used to create a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enable_work_docs",
                "EnableWorkDocs",
                autoboto.TypeInfo(bool),
            ),
            (
                "enable_internet_access",
                "EnableInternetAccess",
                autoboto.TypeInfo(bool),
            ),
            (
                "default_ou",
                "DefaultOu",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_security_group_id",
                "CustomSecurityGroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_enabled_as_local_administrator",
                "UserEnabledAsLocalAdministrator",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Indicates whether the directory is enabled for Amazon WorkDocs.
    enable_work_docs: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The public IP address to attach to all WorkSpaces that are created or
    # rebuilt.
    enable_internet_access: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The organizational unit (OU) in the directory for the WorkSpace machine
    # accounts.
    default_ou: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of any security groups to apply to WorkSpaces when they are
    # created.
    custom_security_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the WorkSpace user is an administrator on the WorkSpace.
    user_enabled_as_local_administrator: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteIpGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the IP access control group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteIpGroupResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteTagsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the WorkSpace. To find this ID, use DescribeWorkspaces.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tag keys.
    tag_keys: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DeleteTagsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeIpGroupsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_ids",
                "GroupIds",
                autoboto.TypeInfo(typing.List[str]),
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

    # The IDs of one or more IP access control groups.
    group_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The token for the next set of results. (You received this token from a
    # previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeIpGroupsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "result",
                "Result",
                autoboto.TypeInfo(typing.List[WorkspacesIpGroup]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the IP access control groups.
    result: typing.List["WorkspacesIpGroup"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use to retrieve the next set of results, or null if there are
    # no more results available. This token is valid for one day and must be used
    # within that time frame.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTagsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the WorkSpace. To find this ID, use DescribeWorkspaces.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTagsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_list",
                "TagList",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The tags.
    tag_list: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeWorkspaceBundlesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_ids",
                "BundleIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The IDs of the bundles. This parameter cannot be combined with any other
    # filter.
    bundle_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The owner of the bundles. This parameter cannot be combined with any other
    # filter.

    # Specify `AMAZON` to describe the bundles provided by AWS or null to
    # describe the bundles that belong to your account.
    owner: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of results. (You received this token from a
    # previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeWorkspaceBundlesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundles",
                "Bundles",
                autoboto.TypeInfo(typing.List[WorkspaceBundle]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the bundles.
    bundles: typing.List["WorkspaceBundle"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use to retrieve the next set of results, or null if there are
    # no more results available. This token is valid for one day and must be used
    # within that time frame.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeWorkspaceDirectoriesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_ids",
                "DirectoryIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifiers of the directories. If the value is null, all directories
    # are retrieved.
    directory_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The token for the next set of results. (You received this token from a
    # previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeWorkspaceDirectoriesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directories",
                "Directories",
                autoboto.TypeInfo(typing.List[WorkspaceDirectory]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the directories.
    directories: typing.List["WorkspaceDirectory"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use to retrieve the next set of results, or null if there are
    # no more results available. This token is valid for one day and must be used
    # within that time frame.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeWorkspacesConnectionStatusRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_ids",
                "WorkspaceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifiers of the WorkSpaces. You can specify up to 25 WorkSpaces.
    workspace_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The token for the next set of results. (You received this token from a
    # previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeWorkspacesConnectionStatusResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspaces_connection_status",
                "WorkspacesConnectionStatus",
                autoboto.TypeInfo(typing.List[WorkspaceConnectionStatus]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the connection status of the WorkSpace.
    workspaces_connection_status: typing.List["WorkspaceConnectionStatus"
                                             ] = dataclasses.field(
                                                 default_factory=list,
                                             )

    # The token to use to retrieve the next set of results, or null if there are
    # no more results available.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeWorkspacesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_ids",
                "WorkspaceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "directory_id",
                "DirectoryId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                autoboto.TypeInfo(str),
            ),
            (
                "bundle_id",
                "BundleId",
                autoboto.TypeInfo(str),
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

    # The IDs of the WorkSpaces. This parameter cannot be combined with any other
    # filter.

    # Because the CreateWorkspaces operation is asynchronous, the identifier it
    # returns is not immediately available. If you immediately call
    # DescribeWorkspaces with this identifier, no information is returned.
    workspace_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The ID of the directory. In addition, you can optionally specify a specific
    # directory user (see `UserName`). This parameter cannot be combined with any
    # other filter.
    directory_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the directory user. You must specify this parameter with
    # `DirectoryId`.
    user_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the bundle. All WorkSpaces that are created from this bundle are
    # retrieved. This parameter cannot be combined with any other filter.
    bundle_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of items to return.
    limit: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token for the next set of results. (You received this token from a
    # previous call.)
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeWorkspacesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspaces",
                "Workspaces",
                autoboto.TypeInfo(typing.List[Workspace]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the WorkSpaces.

    # Because CreateWorkspaces is an asynchronous operation, some of the returned
    # information could be incomplete.
    workspaces: typing.List["Workspace"] = dataclasses.field(
        default_factory=list,
    )

    # The token to use to retrieve the next set of results, or null if there are
    # no more results available. This token is valid for one day and must be used
    # within that time frame.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateIpGroupsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                autoboto.TypeInfo(str),
            ),
            (
                "group_ids",
                "GroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the directory.
    directory_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The IDs of one or more IP access control groups.
    group_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DisassociateIpGroupsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class FailedCreateWorkspaceRequest(autoboto.ShapeBase):
    """
    Information about a WorkSpace that could not be created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_request",
                "WorkspaceRequest",
                autoboto.TypeInfo(WorkspaceRequest),
            ),
            (
                "error_code",
                "ErrorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the WorkSpace.
    workspace_request: "WorkspaceRequest" = dataclasses.field(
        default_factory=dict,
    )

    # The error code.
    error_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The textual error message.
    error_message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FailedWorkspaceChangeRequest(autoboto.ShapeBase):
    """
    Information about a WorkSpace that could not be rebooted (RebootWorkspaces),
    rebuilt (RebuildWorkspaces), terminated (TerminateWorkspaces), started
    (StartWorkspaces), or stopped (StopWorkspaces).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                autoboto.TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier of the WorkSpace.
    workspace_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The error code.
    error_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The textual error message.
    error_message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterValuesException(autoboto.ShapeBase):
    """
    One or more parameter values are not valid.
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

    # The exception error message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidResourceStateException(autoboto.ShapeBase):
    """
    The state of the resource is not valid for this operation.
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
class IpRuleItem(autoboto.ShapeBase):
    """
    Information about a rule for an IP access control group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip_rule",
                "ipRule",
                autoboto.TypeInfo(str),
            ),
            (
                "rule_desc",
                "ruleDesc",
                autoboto.TypeInfo(str),
            ),
        ]

    # The IP address range, in CIDR notation.
    ip_rule: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description.
    rule_desc: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ModificationResourceEnum(Enum):
    ROOT_VOLUME = "ROOT_VOLUME"
    USER_VOLUME = "USER_VOLUME"
    COMPUTE_TYPE = "COMPUTE_TYPE"


@dataclasses.dataclass
class ModificationState(autoboto.ShapeBase):
    """
    Information about a WorkSpace modification.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource",
                "Resource",
                autoboto.TypeInfo(ModificationResourceEnum),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(ModificationStateEnum),
            ),
        ]

    # The resource.
    resource: "ModificationResourceEnum" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The modification state.
    state: "ModificationStateEnum" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ModificationStateEnum(Enum):
    UPDATE_INITIATED = "UPDATE_INITIATED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"


@dataclasses.dataclass
class ModifyWorkspacePropertiesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                autoboto.TypeInfo(str),
            ),
            (
                "workspace_properties",
                "WorkspaceProperties",
                autoboto.TypeInfo(WorkspaceProperties),
            ),
        ]

    # The ID of the WorkSpace.
    workspace_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The properties of the WorkSpace.
    workspace_properties: "WorkspaceProperties" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ModifyWorkspacePropertiesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ModifyWorkspaceStateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                autoboto.TypeInfo(str),
            ),
            (
                "workspace_state",
                "WorkspaceState",
                autoboto.TypeInfo(TargetWorkspaceState),
            ),
        ]

    # The ID of the WorkSpace.
    workspace_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The WorkSpace state.
    workspace_state: "TargetWorkspaceState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyWorkspaceStateResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class OperationInProgressException(autoboto.ShapeBase):
    """
    The properties of this WorkSpace are currently being modified. Try again in a
    moment.
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
class OperationNotSupportedException(autoboto.ShapeBase):
    """
    This operation is not supported.
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
class RebootRequest(autoboto.ShapeBase):
    """
    Information used to reboot a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the WorkSpace.
    workspace_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RebootWorkspacesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reboot_workspace_requests",
                "RebootWorkspaceRequests",
                autoboto.TypeInfo(typing.List[RebootRequest]),
            ),
        ]

    # The WorkSpaces to reboot. You can specify up to 25 WorkSpaces.
    reboot_workspace_requests: typing.List["RebootRequest"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class RebootWorkspacesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failed_requests",
                "FailedRequests",
                autoboto.TypeInfo(typing.List[FailedWorkspaceChangeRequest]),
            ),
        ]

    # Information about the WorkSpaces that could not be rebooted.
    failed_requests: typing.List["FailedWorkspaceChangeRequest"
                                ] = dataclasses.field(
                                    default_factory=list,
                                )


@dataclasses.dataclass
class RebuildRequest(autoboto.ShapeBase):
    """
    Information used to rebuild a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the WorkSpace.
    workspace_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RebuildWorkspacesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rebuild_workspace_requests",
                "RebuildWorkspaceRequests",
                autoboto.TypeInfo(typing.List[RebuildRequest]),
            ),
        ]

    # The WorkSpace to rebuild. You can specify a single WorkSpace.
    rebuild_workspace_requests: typing.List["RebuildRequest"
                                           ] = dataclasses.field(
                                               default_factory=list,
                                           )


@dataclasses.dataclass
class RebuildWorkspacesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failed_requests",
                "FailedRequests",
                autoboto.TypeInfo(typing.List[FailedWorkspaceChangeRequest]),
            ),
        ]

    # Information about the WorkSpace if it could not be rebuilt.
    failed_requests: typing.List["FailedWorkspaceChangeRequest"
                                ] = dataclasses.field(
                                    default_factory=list,
                                )


@dataclasses.dataclass
class ResourceAlreadyExistsException(autoboto.ShapeBase):
    """
    The specified resource already exists.
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
class ResourceAssociatedException(autoboto.ShapeBase):
    """
    The resource is associated with a directory.
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
class ResourceCreationFailedException(autoboto.ShapeBase):
    """
    The resource could not be created.
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
class ResourceLimitExceededException(autoboto.ShapeBase):
    """
    Your resource limits have been exceeded.
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

    # The exception error message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    The resource could not be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The resource could not be found.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the resource that could not be found.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceUnavailableException(autoboto.ShapeBase):
    """
    The specified resource is not available.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The exception error message.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of the resource that is not available.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RevokeIpRulesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_rules",
                "UserRules",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The rules to remove from the group.
    user_rules: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class RevokeIpRulesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RootStorage(autoboto.ShapeBase):
    """
    Information about the root volume for a WorkSpace bundle.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "capacity",
                "Capacity",
                autoboto.TypeInfo(str),
            ),
        ]

    # The size of the root volume.
    capacity: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class RunningMode(Enum):
    AUTO_STOP = "AUTO_STOP"
    ALWAYS_ON = "ALWAYS_ON"


@dataclasses.dataclass
class StartRequest(autoboto.ShapeBase):
    """
    Information used to start a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the WorkSpace.
    workspace_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartWorkspacesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start_workspace_requests",
                "StartWorkspaceRequests",
                autoboto.TypeInfo(typing.List[StartRequest]),
            ),
        ]

    # The WorkSpaces to start. You can specify up to 25 WorkSpaces.
    start_workspace_requests: typing.List["StartRequest"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class StartWorkspacesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failed_requests",
                "FailedRequests",
                autoboto.TypeInfo(typing.List[FailedWorkspaceChangeRequest]),
            ),
        ]

    # Information about the WorkSpaces that could not be started.
    failed_requests: typing.List["FailedWorkspaceChangeRequest"
                                ] = dataclasses.field(
                                    default_factory=list,
                                )


@dataclasses.dataclass
class StopRequest(autoboto.ShapeBase):
    """
    Information used to stop a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the WorkSpace.
    workspace_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopWorkspacesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stop_workspace_requests",
                "StopWorkspaceRequests",
                autoboto.TypeInfo(typing.List[StopRequest]),
            ),
        ]

    # The WorkSpaces to stop. You can specify up to 25 WorkSpaces.
    stop_workspace_requests: typing.List["StopRequest"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class StopWorkspacesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failed_requests",
                "FailedRequests",
                autoboto.TypeInfo(typing.List[FailedWorkspaceChangeRequest]),
            ),
        ]

    # Information about the WorkSpaces that could not be stopped.
    failed_requests: typing.List["FailedWorkspaceChangeRequest"
                                ] = dataclasses.field(
                                    default_factory=list,
                                )


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    """
    Information about a tag.
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

    # The key of the tag.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value of the tag.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class TargetWorkspaceState(Enum):
    AVAILABLE = "AVAILABLE"
    ADMIN_MAINTENANCE = "ADMIN_MAINTENANCE"


@dataclasses.dataclass
class TerminateRequest(autoboto.ShapeBase):
    """
    Information used to terminate a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the WorkSpace.
    workspace_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TerminateWorkspacesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "terminate_workspace_requests",
                "TerminateWorkspaceRequests",
                autoboto.TypeInfo(typing.List[TerminateRequest]),
            ),
        ]

    # The WorkSpaces to terminate. You can specify up to 25 WorkSpaces.
    terminate_workspace_requests: typing.List["TerminateRequest"
                                             ] = dataclasses.field(
                                                 default_factory=list,
                                             )


@dataclasses.dataclass
class TerminateWorkspacesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failed_requests",
                "FailedRequests",
                autoboto.TypeInfo(typing.List[FailedWorkspaceChangeRequest]),
            ),
        ]

    # Information about the WorkSpaces that could not be terminated.
    failed_requests: typing.List["FailedWorkspaceChangeRequest"
                                ] = dataclasses.field(
                                    default_factory=list,
                                )


@dataclasses.dataclass
class UnsupportedWorkspaceConfigurationException(autoboto.ShapeBase):
    """
    The configuration of this WorkSpace is not supported for this operation. For
    more information, see the [Amazon WorkSpaces Administration
    Guide](http://docs.aws.amazon.com/workspaces/latest/adminguide/).
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
class UpdateRulesOfIpGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_rules",
                "UserRules",
                autoboto.TypeInfo(typing.List[IpRuleItem]),
            ),
        ]

    # The ID of the group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more rules.
    user_rules: typing.List["IpRuleItem"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateRulesOfIpGroupResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UserStorage(autoboto.ShapeBase):
    """
    Information about the user storage for a WorkSpace bundle.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "capacity",
                "Capacity",
                autoboto.TypeInfo(str),
            ),
        ]

    # The size of the user storage.
    capacity: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Workspace(autoboto.ShapeBase):
    """
    Information about a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                autoboto.TypeInfo(str),
            ),
            (
                "directory_id",
                "DirectoryId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                autoboto.TypeInfo(str),
            ),
            (
                "ip_address",
                "IpAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(WorkspaceState),
            ),
            (
                "bundle_id",
                "BundleId",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_id",
                "SubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "computer_name",
                "ComputerName",
                autoboto.TypeInfo(str),
            ),
            (
                "volume_encryption_key",
                "VolumeEncryptionKey",
                autoboto.TypeInfo(str),
            ),
            (
                "user_volume_encryption_enabled",
                "UserVolumeEncryptionEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "root_volume_encryption_enabled",
                "RootVolumeEncryptionEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "workspace_properties",
                "WorkspaceProperties",
                autoboto.TypeInfo(WorkspaceProperties),
            ),
            (
                "modification_states",
                "ModificationStates",
                autoboto.TypeInfo(typing.List[ModificationState]),
            ),
        ]

    # The identifier of the WorkSpace.
    workspace_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of the AWS Directory Service directory for the WorkSpace.
    directory_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user for the WorkSpace.
    user_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The IP address of the WorkSpace.
    ip_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The operational state of the WorkSpace.
    state: "WorkspaceState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the bundle used to create the WorkSpace.
    bundle_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of the subnet for the WorkSpace.
    subnet_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the WorkSpace could not be created, contains a textual error message
    # that describes the failure.
    error_message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the WorkSpace could not be created, contains the error code.
    error_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the WorkSpace, as seen by the operating system.
    computer_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The KMS key used to encrypt data stored on your WorkSpace.
    volume_encryption_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the data stored on the user volume is encrypted.
    user_volume_encryption_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the data stored on the root volume is encrypted.
    root_volume_encryption_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The properties of the WorkSpace.
    workspace_properties: "WorkspaceProperties" = dataclasses.field(
        default_factory=dict,
    )

    # The modification states of the WorkSpace.
    modification_states: typing.List["ModificationState"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class WorkspaceBundle(autoboto.ShapeBase):
    """
    Information about a WorkSpace bundle.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_id",
                "BundleId",
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
                "root_storage",
                "RootStorage",
                autoboto.TypeInfo(RootStorage),
            ),
            (
                "user_storage",
                "UserStorage",
                autoboto.TypeInfo(UserStorage),
            ),
            (
                "compute_type",
                "ComputeType",
                autoboto.TypeInfo(ComputeType),
            ),
        ]

    # The bundle identifier.
    bundle_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the bundle.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The owner of the bundle. This is the account identifier of the owner, or
    # `AMAZON` if the bundle is provided by AWS.
    owner: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A description.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The size of the root volume.
    root_storage: "RootStorage" = dataclasses.field(default_factory=dict, )

    # The size of the user storage.
    user_storage: "UserStorage" = dataclasses.field(default_factory=dict, )

    # The compute type. For more information, see [Amazon WorkSpaces
    # Bundles](http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles).
    compute_type: "ComputeType" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class WorkspaceConnectionStatus(autoboto.ShapeBase):
    """
    Describes the connection status of a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "workspace_id",
                "WorkspaceId",
                autoboto.TypeInfo(str),
            ),
            (
                "connection_state",
                "ConnectionState",
                autoboto.TypeInfo(ConnectionState),
            ),
            (
                "connection_state_check_timestamp",
                "ConnectionStateCheckTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_known_user_connection_timestamp",
                "LastKnownUserConnectionTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ID of the WorkSpace.
    workspace_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The connection state of the WorkSpace. The connection state is unknown if
    # the WorkSpace is stopped.
    connection_state: "ConnectionState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp of the connection state check.
    connection_state_check_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp of the last known user connection.
    last_known_user_connection_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class WorkspaceDirectory(autoboto.ShapeBase):
    """
    Information about an AWS Directory Service directory for use with Amazon
    WorkSpaces.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                autoboto.TypeInfo(str),
            ),
            (
                "alias",
                "Alias",
                autoboto.TypeInfo(str),
            ),
            (
                "directory_name",
                "DirectoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "registration_code",
                "RegistrationCode",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "dns_ip_addresses",
                "DnsIpAddresses",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "customer_user_name",
                "CustomerUserName",
                autoboto.TypeInfo(str),
            ),
            (
                "iam_role_id",
                "IamRoleId",
                autoboto.TypeInfo(str),
            ),
            (
                "directory_type",
                "DirectoryType",
                autoboto.TypeInfo(WorkspaceDirectoryType),
            ),
            (
                "workspace_security_group_id",
                "WorkspaceSecurityGroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(WorkspaceDirectoryState),
            ),
            (
                "workspace_creation_properties",
                "WorkspaceCreationProperties",
                autoboto.TypeInfo(DefaultWorkspaceCreationProperties),
            ),
            (
                "ip_group_ids",
                "ipGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The directory identifier.
    directory_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The directory alias.
    alias: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the directory.
    directory_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The registration code for the directory. This is the code that users enter
    # in their Amazon WorkSpaces client application to connect to the directory.
    registration_code: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifiers of the subnets used with the directory.
    subnet_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The IP addresses of the DNS servers for the directory.
    dns_ip_addresses: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The user name for the service account.
    customer_user_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the IAM role. This is the role that allows Amazon
    # WorkSpaces to make calls to other services, such as Amazon EC2, on your
    # behalf.
    iam_role_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The directory type.
    directory_type: "WorkspaceDirectoryType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the security group that is assigned to new WorkSpaces.
    workspace_security_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The state of the directory's registration with Amazon WorkSpaces
    state: "WorkspaceDirectoryState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The default creation properties for all WorkSpaces in the directory.
    workspace_creation_properties: "DefaultWorkspaceCreationProperties" = dataclasses.field(
        default_factory=dict,
    )

    # The identifiers of the IP access control groups associated with the
    # directory.
    ip_group_ids: typing.List[str] = dataclasses.field(default_factory=list, )


class WorkspaceDirectoryState(Enum):
    REGISTERING = "REGISTERING"
    REGISTERED = "REGISTERED"
    DEREGISTERING = "DEREGISTERING"
    DEREGISTERED = "DEREGISTERED"
    ERROR = "ERROR"


class WorkspaceDirectoryType(Enum):
    SIMPLE_AD = "SIMPLE_AD"
    AD_CONNECTOR = "AD_CONNECTOR"


@dataclasses.dataclass
class WorkspaceProperties(autoboto.ShapeBase):
    """
    Information about a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "running_mode",
                "RunningMode",
                autoboto.TypeInfo(RunningMode),
            ),
            (
                "running_mode_auto_stop_timeout_in_minutes",
                "RunningModeAutoStopTimeoutInMinutes",
                autoboto.TypeInfo(int),
            ),
            (
                "root_volume_size_gib",
                "RootVolumeSizeGib",
                autoboto.TypeInfo(int),
            ),
            (
                "user_volume_size_gib",
                "UserVolumeSizeGib",
                autoboto.TypeInfo(int),
            ),
            (
                "compute_type_name",
                "ComputeTypeName",
                autoboto.TypeInfo(Compute),
            ),
        ]

    # The running mode. For more information, see [Manage the WorkSpace Running
    # Mode](http://docs.aws.amazon.com/workspaces/latest/adminguide/running-
    # mode.html).
    running_mode: "RunningMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time after a user logs off when WorkSpaces are automatically stopped.
    # Configured in 60 minute intervals.
    running_mode_auto_stop_timeout_in_minutes: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The size of the root volume.
    root_volume_size_gib: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The size of the user storage.
    user_volume_size_gib: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The compute type. For more information, see [Amazon WorkSpaces
    # Bundles](http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles).
    compute_type_name: "Compute" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class WorkspaceRequest(autoboto.ShapeBase):
    """
    Information used to create a WorkSpace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                autoboto.TypeInfo(str),
            ),
            (
                "bundle_id",
                "BundleId",
                autoboto.TypeInfo(str),
            ),
            (
                "volume_encryption_key",
                "VolumeEncryptionKey",
                autoboto.TypeInfo(str),
            ),
            (
                "user_volume_encryption_enabled",
                "UserVolumeEncryptionEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "root_volume_encryption_enabled",
                "RootVolumeEncryptionEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "workspace_properties",
                "WorkspaceProperties",
                autoboto.TypeInfo(WorkspaceProperties),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The identifier of the AWS Directory Service directory for the WorkSpace.
    # You can use DescribeWorkspaceDirectories to list the available directories.
    directory_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The username of the user for the WorkSpace. This username must exist in the
    # AWS Directory Service directory for the WorkSpace.
    user_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of the bundle for the WorkSpace. You can use
    # DescribeWorkspaceBundles to list the available bundles.
    bundle_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The KMS key used to encrypt data stored on your WorkSpace.
    volume_encryption_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the data stored on the user volume is encrypted.
    user_volume_encryption_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the data stored on the root volume is encrypted.
    root_volume_encryption_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The WorkSpace properties.
    workspace_properties: "WorkspaceProperties" = dataclasses.field(
        default_factory=dict,
    )

    # The tags for the WorkSpace.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


class WorkspaceState(Enum):
    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    IMPAIRED = "IMPAIRED"
    UNHEALTHY = "UNHEALTHY"
    REBOOTING = "REBOOTING"
    STARTING = "STARTING"
    REBUILDING = "REBUILDING"
    MAINTENANCE = "MAINTENANCE"
    ADMIN_MAINTENANCE = "ADMIN_MAINTENANCE"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"
    SUSPENDED = "SUSPENDED"
    UPDATING = "UPDATING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    ERROR = "ERROR"


@dataclasses.dataclass
class WorkspacesIpGroup(autoboto.ShapeBase):
    """
    Information about an IP access control group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "groupId",
                autoboto.TypeInfo(str),
            ),
            (
                "group_name",
                "groupName",
                autoboto.TypeInfo(str),
            ),
            (
                "group_desc",
                "groupDesc",
                autoboto.TypeInfo(str),
            ),
            (
                "user_rules",
                "userRules",
                autoboto.TypeInfo(typing.List[IpRuleItem]),
            ),
        ]

    # The ID of the group.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the group.
    group_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the group.
    group_desc: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The rules.
    user_rules: typing.List["IpRuleItem"] = dataclasses.field(
        default_factory=list,
    )
