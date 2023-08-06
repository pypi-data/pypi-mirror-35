import datetime
import typing
import autoboto
import dataclasses


@dataclasses.dataclass
class AssociateTeamMemberRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_arn",
                "userArn",
                autoboto.TypeInfo(str),
            ),
            (
                "project_role",
                "projectRole",
                autoboto.TypeInfo(str),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                autoboto.TypeInfo(str),
            ),
            (
                "remote_access_allowed",
                "remoteAccessAllowed",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the project to which you will add the IAM user.
    project_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the IAM user you want to add to the AWS
    # CodeStar project.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The AWS CodeStar project role that will apply to this user. This role
    # determines what actions a user can take in an AWS CodeStar project.
    project_role: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A user- or system-generated token that identifies the entity that requested
    # the team member association to the project. This token can be used to
    # repeat the request.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether the team member is allowed to use an SSH public/private key pair to
    # remotely access project resources, for example Amazon EC2 instances.
    remote_access_allowed: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociateTeamMemberResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The user- or system-generated token from the initial request that can be
    # used to repeat the request.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConcurrentModificationException(autoboto.ShapeBase):
    """
    Another modification is being made. That modification must complete before you
    can make your change.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateProjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Reserved for future use.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Reserved for future use.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Reserved for future use.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Reserved for future use.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateProjectResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                autoboto.TypeInfo(str),
            ),
            (
                "project_template_id",
                "projectTemplateId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Reserved for future use.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Reserved for future use.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Reserved for future use.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Reserved for future use.
    project_template_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateUserProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "userArn",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "displayName",
                autoboto.TypeInfo(str),
            ),
            (
                "email_address",
                "emailAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "sshPublicKey",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the user in IAM.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name that will be displayed as the friendly name for the user in AWS
    # CodeStar.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The email address that will be displayed as part of the user's profile in
    # AWS CodeStar.
    email_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The SSH public key associated with the user in AWS CodeStar. If a project
    # owner allows the user remote access to project resources, this public key
    # will be used along with the user's private key for SSH access.
    ssh_public_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateUserProfileResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_arn",
                "userArn",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "displayName",
                autoboto.TypeInfo(str),
            ),
            (
                "email_address",
                "emailAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "sshPublicKey",
                autoboto.TypeInfo(str),
            ),
            (
                "created_timestamp",
                "createdTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_timestamp",
                "lastModifiedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the user in IAM.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name that is displayed as the friendly name for the user in AWS
    # CodeStar.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The email address that is displayed as part of the user's profile in AWS
    # CodeStar.
    email_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The SSH public key associated with the user in AWS CodeStar. This is the
    # public portion of the public/private keypair the user can use to access
    # project resources if a project owner allows the user remote access to those
    # resources.
    ssh_public_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date the user profile was created, in timestamp format.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date the user profile was last modified, in timestamp format.
    last_modified_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteProjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                autoboto.TypeInfo(str),
            ),
            (
                "delete_stack",
                "deleteStack",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the project to be deleted in AWS CodeStar.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A user- or system-generated token that identifies the entity that requested
    # project deletion. This token can be used to repeat the request.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whether to send a delete request for the primary stack in AWS
    # CloudFormation originally used to generate the project and its resources.
    # This option will delete all AWS resources for the project (except for any
    # buckets in Amazon S3) as well as deleting the project itself. Recommended
    # for most use cases.
    delete_stack: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProjectResult(autoboto.OutputShapeBase):
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
                "stackId",
                autoboto.TypeInfo(str),
            ),
            (
                "project_arn",
                "projectArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the primary stack in AWS CloudFormation that will be deleted as
    # part of deleting the project and its resources.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the deleted project.
    project_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUserProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "userArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the user to delete from AWS CodeStar.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUserProfileResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_arn",
                "userArn",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the user deleted from AWS CodeStar.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the project.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProjectResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                autoboto.TypeInfo(str),
            ),
            (
                "created_time_stamp",
                "createdTimeStamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "stack_id",
                "stackId",
                autoboto.TypeInfo(str),
            ),
            (
                "project_template_id",
                "projectTemplateId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The display name for the project.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the project.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the project.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the project, if any.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A user- or system-generated token that identifies the entity that requested
    # project creation.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time the project was created, in timestamp format.
    created_time_stamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the primary stack in AWS CloudFormation used to generate
    # resources for the project.
    stack_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID for the AWS CodeStar project template used to create the project.
    project_template_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeUserProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "userArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the user.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeUserProfileResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_arn",
                "userArn",
                autoboto.TypeInfo(str),
            ),
            (
                "created_timestamp",
                "createdTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_timestamp",
                "lastModifiedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "display_name",
                "displayName",
                autoboto.TypeInfo(str),
            ),
            (
                "email_address",
                "emailAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "sshPublicKey",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the user.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date and time when the user profile was created in AWS CodeStar, in
    # timestamp format.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time when the user profile was last modified, in timestamp
    # format.
    last_modified_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The display name shown for the user in AWS CodeStar projects. For example,
    # this could be set to both first and last name ("Mary Major") or a single
    # name ("Mary"). The display name is also used to generate the initial icon
    # associated with the user in AWS CodeStar projects. If spaces are included
    # in the display name, the first character that appears after the space will
    # be used as the second character in the user initial icon. The initial icon
    # displays a maximum of two characters, so a display name with more than one
    # space (for example "Mary Jane Major") would generate an initial icon using
    # the first character and the first character after the space ("MJ", not
    # "MM").
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The email address for the user. Optional.
    email_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The SSH public key associated with the user. This SSH public key is
    # associated with the user profile, and can be used in conjunction with the
    # associated private key for access to project resources, such as Amazon EC2
    # instances, if a project owner grants remote access to those resources.
    ssh_public_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateTeamMemberRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_arn",
                "userArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS CodeStar project from which you want to remove a team
    # member.
    project_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM user or group whom you want to
    # remove from the project.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateTeamMemberResult(autoboto.OutputShapeBase):
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
class InvalidNextTokenException(autoboto.ShapeBase):
    """
    The next token is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidServiceRoleException(autoboto.ShapeBase):
    """
    The service role is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    A resource limit has been exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListProjectsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The continuation token to be used to return the next set of results, if the
    # results cannot be returned in one response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum amount of data that can be contained in a single set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListProjectsResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "projects",
                "projects",
                autoboto.TypeInfo(typing.List[ProjectSummary]),
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

    # A list of projects.
    projects: typing.List["ProjectSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The continuation token to use when requesting the next set of results, if
    # there are more results to be returned.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourcesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the project.
    project_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The continuation token for the next set of results, if the results cannot
    # be returned in one response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum amount of data that can be contained in a single set of
    # results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourcesResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resources",
                "resources",
                autoboto.TypeInfo(typing.List[Resource]),
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

    # An array of resources associated with the project.
    resources: typing.List["Resource"] = dataclasses.field(
        default_factory=list,
    )

    # The continuation token to use when requesting the next set of results, if
    # there are more results to be returned.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForProjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the project to get tags for.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Reserved for future use.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Reserved for future use.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForProjectResult(autoboto.OutputShapeBase):
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
                "tags",
                autoboto.TypeInfo(typing.Dict[str, str]),
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

    # The tags for the project.
    tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Reserved for future use.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTeamMembersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the project for which you want to list team members.
    project_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The continuation token for the next set of results, if the results cannot
    # be returned in one response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of team members you want returned in a response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTeamMembersResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "team_members",
                "teamMembers",
                autoboto.TypeInfo(typing.List[TeamMember]),
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

    # A list of team member objects for the project.
    team_members: typing.List["TeamMember"] = dataclasses.field(
        default_factory=list,
    )

    # The continuation token to use when requesting the next set of results, if
    # there are more results to be returned.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListUserProfilesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The continuation token for the next set of results, if the results cannot
    # be returned in one response.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to return in a response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListUserProfilesResult(autoboto.OutputShapeBase):
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
                "userProfiles",
                autoboto.TypeInfo(typing.List[UserProfileSummary]),
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

    # All the user profiles configured in AWS CodeStar for an AWS account.
    user_profiles: typing.List["UserProfileSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The continuation token to use when requesting the next set of results, if
    # there are more results to be returned.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProjectAlreadyExistsException(autoboto.ShapeBase):
    """
    An AWS CodeStar project with the same ID already exists in this region for the
    AWS account. AWS CodeStar project IDs must be unique within a region for the AWS
    account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ProjectConfigurationException(autoboto.ShapeBase):
    """
    Project configuration information is required but not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ProjectCreationFailedException(autoboto.ShapeBase):
    """
    The project creation request was valid, but a nonspecific exception or error
    occurred during project creation. The project could not be created in AWS
    CodeStar.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ProjectNotFoundException(autoboto.ShapeBase):
    """
    The specified AWS CodeStar project was not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ProjectSummary(autoboto.ShapeBase):
    """
    Information about the metadata for a project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                autoboto.TypeInfo(str),
            ),
            (
                "project_arn",
                "projectArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the project.
    project_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the project.
    project_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Resource(autoboto.ShapeBase):
    """
    Information about a resource for a project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagProjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The ID of the project you want to add a tag to.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tags you want to add to the project.
    tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TagProjectResult(autoboto.OutputShapeBase):
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
                "tags",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The tags for the project.
    tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TeamMember(autoboto.ShapeBase):
    """
    Information about a team member in a project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "userArn",
                autoboto.TypeInfo(str),
            ),
            (
                "project_role",
                "projectRole",
                autoboto.TypeInfo(str),
            ),
            (
                "remote_access_allowed",
                "remoteAccessAllowed",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The Amazon Resource Name (ARN) of the user in IAM.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The role assigned to the user in the project. Project roles have different
    # levels of access. For more information, see [Working with
    # Teams](http://docs.aws.amazon.com/codestar/latest/userguide/working-with-
    # teams.html) in the _AWS CodeStar User Guide_.
    project_role: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether the user is allowed to remotely access project resources using an
    # SSH public/private key pair.
    remote_access_allowed: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TeamMemberAlreadyAssociatedException(autoboto.ShapeBase):
    """
    The team member is already associated with a role in this project.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TeamMemberNotFoundException(autoboto.ShapeBase):
    """
    The specified team member was not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UntagProjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the project to remove tags from.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tags to remove from the project.
    tags: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UntagProjectResult(autoboto.OutputShapeBase):
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
class UpdateProjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the project you want to update.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the project you want to update.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the project, if any.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateProjectResult(autoboto.OutputShapeBase):
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
class UpdateTeamMemberRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_id",
                "projectId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_arn",
                "userArn",
                autoboto.TypeInfo(str),
            ),
            (
                "project_role",
                "projectRole",
                autoboto.TypeInfo(str),
            ),
            (
                "remote_access_allowed",
                "remoteAccessAllowed",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the project.
    project_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the user for whom you want to change team
    # membership attributes.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The role assigned to the user in the project. Project roles have different
    # levels of access. For more information, see [Working with
    # Teams](http://docs.aws.amazon.com/codestar/latest/userguide/working-with-
    # teams.html) in the _AWS CodeStar User Guide_.
    project_role: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether a team member is allowed to remotely access project resources using
    # the SSH public key associated with the user's profile. Even if this is set
    # to True, the user must associate a public key with their profile before the
    # user can access resources.
    remote_access_allowed: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateTeamMemberResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_arn",
                "userArn",
                autoboto.TypeInfo(str),
            ),
            (
                "project_role",
                "projectRole",
                autoboto.TypeInfo(str),
            ),
            (
                "remote_access_allowed",
                "remoteAccessAllowed",
                autoboto.TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the user whose team membership attributes
    # were updated.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The project role granted to the user.
    project_role: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Whether a team member is allowed to remotely access project resources using
    # the SSH public key associated with the user's profile.
    remote_access_allowed: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateUserProfileRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "userArn",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "displayName",
                autoboto.TypeInfo(str),
            ),
            (
                "email_address",
                "emailAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "sshPublicKey",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name that will be displayed as the friendly name for the user in AWS
    # CodeStar.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name that is displayed as the friendly name for the user in AWS
    # CodeStar.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The email address that is displayed as part of the user's profile in AWS
    # CodeStar.
    email_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The SSH public key associated with the user in AWS CodeStar. If a project
    # owner allows the user remote access to project resources, this public key
    # will be used along with the user's private key for SSH access.
    ssh_public_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateUserProfileResult(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_arn",
                "userArn",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "displayName",
                autoboto.TypeInfo(str),
            ),
            (
                "email_address",
                "emailAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "sshPublicKey",
                autoboto.TypeInfo(str),
            ),
            (
                "created_timestamp",
                "createdTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_timestamp",
                "lastModifiedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the user in IAM.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name that is displayed as the friendly name for the user in AWS
    # CodeStar.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The email address that is displayed as part of the user's profile in AWS
    # CodeStar.
    email_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The SSH public key associated with the user in AWS CodeStar. This is the
    # public portion of the public/private keypair the user can use to access
    # project resources if a project owner allows the user remote access to those
    # resources.
    ssh_public_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date the user profile was created, in timestamp format.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date the user profile was last modified, in timestamp format.
    last_modified_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UserProfileAlreadyExistsException(autoboto.ShapeBase):
    """
    A user profile with that name already exists in this region for the AWS account.
    AWS CodeStar user profile names must be unique within a region for the AWS
    account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UserProfileNotFoundException(autoboto.ShapeBase):
    """
    The user profile was not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UserProfileSummary(autoboto.ShapeBase):
    """
    Information about a user's profile in AWS CodeStar.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_arn",
                "userArn",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "displayName",
                autoboto.TypeInfo(str),
            ),
            (
                "email_address",
                "emailAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "sshPublicKey",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the user in IAM.
    user_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The display name of a user in AWS CodeStar. For example, this could be set
    # to both first and last name ("Mary Major") or a single name ("Mary"). The
    # display name is also used to generate the initial icon associated with the
    # user in AWS CodeStar projects. If spaces are included in the display name,
    # the first character that appears after the space will be used as the second
    # character in the user initial icon. The initial icon displays a maximum of
    # two characters, so a display name with more than one space (for example
    # "Mary Jane Major") would generate an initial icon using the first character
    # and the first character after the space ("MJ", not "MM").
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The email address associated with the user.
    email_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The SSH public key associated with the user in AWS CodeStar. If a project
    # owner allows the user remote access to project resources, this public key
    # will be used along with the user's private key for SSH access.
    ssh_public_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ValidationException(autoboto.ShapeBase):
    """
    The specified input is either not valid, or it could not be validated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []
