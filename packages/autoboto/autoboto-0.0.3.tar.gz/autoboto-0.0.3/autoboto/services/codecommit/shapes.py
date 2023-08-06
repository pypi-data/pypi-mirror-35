import datetime
import typing
import autoboto
from enum import Enum
import botocore.response
import dataclasses


@dataclasses.dataclass
class ActorDoesNotExistException(autoboto.ShapeBase):
    """
    The specified Amazon Resource Name (ARN) does not exist in the AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AuthorDoesNotExistException(autoboto.ShapeBase):
    """
    The specified Amazon Resource Name (ARN) does not exist in the AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BatchGetRepositoriesInput(autoboto.ShapeBase):
    """
    Represents the input of a batch get repositories operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_names",
                "repositoryNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The names of the repositories to get information about.
    repository_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchGetRepositoriesOutput(autoboto.ShapeBase):
    """
    Represents the output of a batch get repositories operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repositories",
                "repositories",
                autoboto.TypeInfo(typing.List[RepositoryMetadata]),
            ),
            (
                "repositories_not_found",
                "repositoriesNotFound",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A list of repositories returned by the batch get repositories operation.
    repositories: typing.List["RepositoryMetadata"] = dataclasses.field(
        default_factory=list,
    )

    # Returns a list of repository names for which information could not be
    # found.
    repositories_not_found: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BeforeCommitIdAndAfterCommitIdAreSameException(autoboto.ShapeBase):
    """
    The before commit ID and the after commit ID are the same, which is not valid.
    The before commit ID and the after commit ID must be different commit IDs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BlobIdDoesNotExistException(autoboto.ShapeBase):
    """
    The specified blob does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BlobIdRequiredException(autoboto.ShapeBase):
    """
    A blob ID is required but was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BlobMetadata(autoboto.ShapeBase):
    """
    Returns information about a specific Git blob object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "blob_id",
                "blobId",
                autoboto.TypeInfo(str),
            ),
            (
                "path",
                "path",
                autoboto.TypeInfo(str),
            ),
            (
                "mode",
                "mode",
                autoboto.TypeInfo(str),
            ),
        ]

    # The full ID of the blob.
    blob_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The path to the blob and any associated file name, if any.
    path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The file mode permissions of the blob. File mode permission codes include:

    #   * `100644` indicates read/write

    #   * `100755` indicates read/write/execute

    #   * `160000` indicates a submodule

    #   * `120000` indicates a symlink
    mode: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BranchDoesNotExistException(autoboto.ShapeBase):
    """
    The specified branch does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BranchInfo(autoboto.ShapeBase):
    """
    Returns information about a branch.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "branch_name",
                "branchName",
                autoboto.TypeInfo(str),
            ),
            (
                "commit_id",
                "commitId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the branch.
    branch_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the last commit made to the branch.
    commit_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BranchNameExistsException(autoboto.ShapeBase):
    """
    The specified branch name already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BranchNameIsTagNameException(autoboto.ShapeBase):
    """
    The specified branch name is not valid because it is a tag name. Type the name
    of a current branch in the repository. For a list of valid branch names, use
    ListBranches.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BranchNameRequiredException(autoboto.ShapeBase):
    """
    A branch name is required but was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class ChangeTypeEnum(Enum):
    A = "A"
    M = "M"
    D = "D"


@dataclasses.dataclass
class ClientRequestTokenRequiredException(autoboto.ShapeBase):
    """
    A client request token is required. A client request token is an unique, client-
    generated idempotency token that when provided in a request, ensures the request
    cannot be repeated with a changed parameter. If a request is received with the
    same parameters and a token is included, the request will return information
    about the initial request that used that token.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Comment(autoboto.ShapeBase):
    """
    Returns information about a specific comment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment_id",
                "commentId",
                autoboto.TypeInfo(str),
            ),
            (
                "content",
                "content",
                autoboto.TypeInfo(str),
            ),
            (
                "in_reply_to",
                "inReplyTo",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_date",
                "lastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "author_arn",
                "authorArn",
                autoboto.TypeInfo(str),
            ),
            (
                "deleted",
                "deleted",
                autoboto.TypeInfo(bool),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The system-generated comment ID.
    comment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The content of the comment.
    content: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the comment for which this comment is a reply, if any.
    in_reply_to: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date and time the comment was created, in timestamp format.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time the comment was most recently modified, in timestamp
    # format.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the person who posted the comment.
    author_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A Boolean value indicating whether the comment has been deleted.
    deleted: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A unique, client-generated idempotency token that when provided in a
    # request, ensures the request cannot be repeated with a changed parameter.
    # If a request is received with the same parameters and a token is included,
    # the request will return information about the initial request that used
    # that token.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CommentContentRequiredException(autoboto.ShapeBase):
    """
    The comment is empty. You must provide some content for a comment. The content
    cannot be null.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommentContentSizeLimitExceededException(autoboto.ShapeBase):
    """
    The comment is too large. Comments are limited to 1,000 characters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommentDeletedException(autoboto.ShapeBase):
    """
    This comment has already been deleted. You cannot edit or delete a deleted
    comment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommentDoesNotExistException(autoboto.ShapeBase):
    """
    No comment exists with the provided ID. Verify that you have provided the
    correct ID, and then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommentIdRequiredException(autoboto.ShapeBase):
    """
    The comment ID is missing or null. A comment ID is required.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommentNotCreatedByCallerException(autoboto.ShapeBase):
    """
    You cannot modify or delete this comment. Only comment authors can modify or
    delete their comments.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommentsForComparedCommit(autoboto.ShapeBase):
    """
    Returns information about comments on the comparison between two commits.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "before_commit_id",
                "beforeCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "before_blob_id",
                "beforeBlobId",
                autoboto.TypeInfo(str),
            ),
            (
                "after_blob_id",
                "afterBlobId",
                autoboto.TypeInfo(str),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(Location),
            ),
            (
                "comments",
                "comments",
                autoboto.TypeInfo(typing.List[Comment]),
            ),
        ]

    # The name of the repository that contains the compared commits.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full commit ID of the commit used to establish the 'before' of the
    # comparison.
    before_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full commit ID of the commit used to establish the 'after' of the
    # comparison.
    after_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full blob ID of the commit used to establish the 'before' of the
    # comparison.
    before_blob_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full blob ID of the commit used to establish the 'after' of the
    # comparison.
    after_blob_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Location information about the comment on the comparison, including the
    # file name, line number, and whether the version of the file where the
    # comment was made is 'BEFORE' or 'AFTER'.
    location: "Location" = dataclasses.field(default_factory=dict, )

    # An array of comment objects. Each comment object contains information about
    # a comment on the comparison between commits.
    comments: typing.List["Comment"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CommentsForPullRequest(autoboto.ShapeBase):
    """
    Returns information about comments on a pull request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "before_commit_id",
                "beforeCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "before_blob_id",
                "beforeBlobId",
                autoboto.TypeInfo(str),
            ),
            (
                "after_blob_id",
                "afterBlobId",
                autoboto.TypeInfo(str),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(Location),
            ),
            (
                "comments",
                "comments",
                autoboto.TypeInfo(typing.List[Comment]),
            ),
        ]

    # The system-generated ID of the pull request.
    pull_request_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the repository that contains the pull request.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full commit ID of the commit that was the tip of the destination branch
    # when the pull request was created. This commit will be superceded by the
    # after commit in the source branch when and if you merge the source branch
    # into the destination branch.
    before_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # he full commit ID of the commit that was the tip of the source branch at
    # the time the comment was made.
    after_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full blob ID of the file on which you want to comment on the
    # destination commit.
    before_blob_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full blob ID of the file on which you want to comment on the source
    # commit.
    after_blob_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Location information about the comment on the pull request, including the
    # file name, line number, and whether the version of the file where the
    # comment was made is 'BEFORE' (destination branch) or 'AFTER' (source
    # branch).
    location: "Location" = dataclasses.field(default_factory=dict, )

    # An array of comment objects. Each comment object contains information about
    # a comment on the pull request.
    comments: typing.List["Comment"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class Commit(autoboto.ShapeBase):
    """
    Returns information about a specific commit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "commit_id",
                "commitId",
                autoboto.TypeInfo(str),
            ),
            (
                "tree_id",
                "treeId",
                autoboto.TypeInfo(str),
            ),
            (
                "parents",
                "parents",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "author",
                "author",
                autoboto.TypeInfo(UserInfo),
            ),
            (
                "committer",
                "committer",
                autoboto.TypeInfo(UserInfo),
            ),
            (
                "additional_data",
                "additionalData",
                autoboto.TypeInfo(str),
            ),
        ]

    # The full SHA of the specified commit.
    commit_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Tree information for the specified commit.
    tree_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of parent commits for the specified commit. Each parent commit ID is
    # the full commit ID.
    parents: typing.List[str] = dataclasses.field(default_factory=list, )

    # The commit message associated with the specified commit.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information about the author of the specified commit. Information includes
    # the date in timestamp format with GMT offset, the name of the author, and
    # the email address for the author, as configured in Git.
    author: "UserInfo" = dataclasses.field(default_factory=dict, )

    # Information about the person who committed the specified commit, also known
    # as the committer. Information includes the date in timestamp format with
    # GMT offset, the name of the committer, and the email address for the
    # committer, as configured in Git.

    # For more information about the difference between an author and a committer
    # in Git, see [Viewing the Commit History](http://git-
    # scm.com/book/ch2-3.html) in Pro Git by Scott Chacon and Ben Straub.
    committer: "UserInfo" = dataclasses.field(default_factory=dict, )

    # Any additional data associated with the specified commit.
    additional_data: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CommitDoesNotExistException(autoboto.ShapeBase):
    """
    The specified commit does not exist or no commit was specified, and the
    specified repository has no default branch.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommitIdDoesNotExistException(autoboto.ShapeBase):
    """
    The specified commit ID does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommitIdRequiredException(autoboto.ShapeBase):
    """
    A commit ID was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommitMessageLengthExceededException(autoboto.ShapeBase):
    """
    The commit message is too long. Provide a shorter string.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CommitRequiredException(autoboto.ShapeBase):
    """
    A commit was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateBranchInput(autoboto.ShapeBase):
    """
    Represents the input of a create branch operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "branch_name",
                "branchName",
                autoboto.TypeInfo(str),
            ),
            (
                "commit_id",
                "commitId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository in which you want to create the new branch.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the new branch to create.
    branch_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the commit to point the new branch to.
    commit_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreatePullRequestInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "title",
                "title",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "targets",
                autoboto.TypeInfo(typing.List[Target]),
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

    # The title of the pull request. This title will be used to identify the pull
    # request to other users in the repository.
    title: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The targets for the pull request, including the source of the code to be
    # reviewed (the source branch), and the destination where the creator of the
    # pull request intends the code to be merged after the pull request is closed
    # (the destination branch).
    targets: typing.List["Target"] = dataclasses.field(default_factory=list, )

    # A description of the pull request.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A unique, client-generated idempotency token that when provided in a
    # request, ensures the request cannot be repeated with a changed parameter.
    # If a request is received with the same parameters and a token is included,
    # the request will return information about the initial request that used
    # that token.

    # The AWS SDKs prepopulate client request tokens. If using an AWS SDK, you do
    # not have to generate an idempotency token, as this will be done for you.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreatePullRequestOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request",
                "pullRequest",
                autoboto.TypeInfo(PullRequest),
            ),
        ]

    # Information about the newly created pull request.
    pull_request: "PullRequest" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateRepositoryInput(autoboto.ShapeBase):
    """
    Represents the input of a create repository operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_description",
                "repositoryDescription",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the new repository to be created.

    # The repository name must be unique across the calling AWS account. In
    # addition, repository names are limited to 100 alphanumeric, dash, and
    # underscore characters, and cannot include certain characters. For a full
    # description of the limits on repository names, see
    # [Limits](http://docs.aws.amazon.com/codecommit/latest/userguide/limits.html)
    # in the AWS CodeCommit User Guide. The suffix ".git" is prohibited.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A comment or description about the new repository.

    # The description field for a repository accepts all HTML characters and all
    # valid Unicode characters. Applications that do not HTML-encode the
    # description and display it in a web page could expose users to potentially
    # malicious code. Make sure that you HTML-encode the description field in any
    # application that uses this API to display the repository description on a
    # web page.
    repository_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateRepositoryOutput(autoboto.ShapeBase):
    """
    Represents the output of a create repository operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_metadata",
                "repositoryMetadata",
                autoboto.TypeInfo(RepositoryMetadata),
            ),
        ]

    # Information about the newly created repository.
    repository_metadata: "RepositoryMetadata" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DefaultBranchCannotBeDeletedException(autoboto.ShapeBase):
    """
    The specified branch is the default branch for the repository, and cannot be
    deleted. To delete this branch, you must first set another branch as the default
    branch.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteBranchInput(autoboto.ShapeBase):
    """
    Represents the input of a delete branch operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "branch_name",
                "branchName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository that contains the branch to be deleted.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the branch to delete.
    branch_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteBranchOutput(autoboto.ShapeBase):
    """
    Represents the output of a delete branch operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deleted_branch",
                "deletedBranch",
                autoboto.TypeInfo(BranchInfo),
            ),
        ]

    # Information about the branch deleted by the operation, including the branch
    # name and the commit ID that was the tip of the branch.
    deleted_branch: "BranchInfo" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteCommentContentInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment_id",
                "commentId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique, system-generated ID of the comment. To get this ID, use
    # GetCommentsForComparedCommit or GetCommentsForPullRequest.
    comment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteCommentContentOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment",
                "comment",
                autoboto.TypeInfo(Comment),
            ),
        ]

    # Information about the comment you just deleted.
    comment: "Comment" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteRepositoryInput(autoboto.ShapeBase):
    """
    Represents the input of a delete repository operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository to delete.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteRepositoryOutput(autoboto.ShapeBase):
    """
    Represents the output of a delete repository operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_id",
                "repositoryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the repository that was deleted.
    repository_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribePullRequestEventsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "pull_request_event_type",
                "pullRequestEventType",
                autoboto.TypeInfo(PullRequestEventType),
            ),
            (
                "actor_arn",
                "actorArn",
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

    # The system-generated ID of the pull request. To get this ID, use
    # ListPullRequests.
    pull_request_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Optional. The pull request event type about which you want to return
    # information.
    pull_request_event_type: "PullRequestEventType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the user whose actions resulted in the
    # event. Examples include updating the pull request with additional commits
    # or changing the status of a pull request.
    actor_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An enumeration token that when provided in a request, returns the next
    # batch of the results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A non-negative integer used to limit the number of returned results. The
    # default is 100 events, which is also the maximum number of events that can
    # be returned in a result.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribePullRequestEventsOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_events",
                "pullRequestEvents",
                autoboto.TypeInfo(typing.List[PullRequestEvent]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the pull request events.
    pull_request_events: typing.List["PullRequestEvent"] = dataclasses.field(
        default_factory=list,
    )

    # An enumeration token that can be used in a request to return the next batch
    # of the results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Difference(autoboto.ShapeBase):
    """
    Returns information about a set of differences for a commit specifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "before_blob",
                "beforeBlob",
                autoboto.TypeInfo(BlobMetadata),
            ),
            (
                "after_blob",
                "afterBlob",
                autoboto.TypeInfo(BlobMetadata),
            ),
            (
                "change_type",
                "changeType",
                autoboto.TypeInfo(ChangeTypeEnum),
            ),
        ]

    # Information about a `beforeBlob` data type object, including the ID, the
    # file mode permission code, and the path.
    before_blob: "BlobMetadata" = dataclasses.field(default_factory=dict, )

    # Information about an `afterBlob` data type object, including the ID, the
    # file mode permission code, and the path.
    after_blob: "BlobMetadata" = dataclasses.field(default_factory=dict, )

    # Whether the change type of the difference is an addition (A), deletion (D),
    # or modification (M).
    change_type: "ChangeTypeEnum" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DirectoryNameConflictsWithFileNameException(autoboto.ShapeBase):
    """
    A file cannot be added to the repository because the specified path name has the
    same name as a file that already exists in this repository. Either provide a
    different name for the file, or specify a different path for the file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EncryptionIntegrityChecksFailedException(autoboto.ShapeBase):
    """
    An encryption integrity check failed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EncryptionKeyAccessDeniedException(autoboto.ShapeBase):
    """
    An encryption key could not be accessed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EncryptionKeyDisabledException(autoboto.ShapeBase):
    """
    The encryption key is disabled.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EncryptionKeyNotFoundException(autoboto.ShapeBase):
    """
    No encryption key was found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EncryptionKeyUnavailableException(autoboto.ShapeBase):
    """
    The encryption key is not available.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class FileContent(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class FileContentRequiredException(autoboto.ShapeBase):
    """
    The file cannot be added because it is empty. Empty files cannot be added to the
    repository with this API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class FileContentSizeLimitExceededException(autoboto.ShapeBase):
    """
    The file cannot be added because it is too large. The maximum file size that can
    be added using PutFile is 6 MB. For files larger than 6 MB but smaller than 2
    GB, add them using a Git client.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class FileModeTypeEnum(Enum):
    EXECUTABLE = "EXECUTABLE"
    NORMAL = "NORMAL"
    SYMLINK = "SYMLINK"


@dataclasses.dataclass
class FileNameConflictsWithDirectoryNameException(autoboto.ShapeBase):
    """
    A file cannot be added to the repository because the specified file name has the
    same name as a directory in this repository. Either provide another name for the
    file, or add the file in a directory that does not match the file name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class FileTooLargeException(autoboto.ShapeBase):
    """
    The specified file exceeds the file size limit for AWS CodeCommit. For more
    information about limits in AWS CodeCommit, see [AWS CodeCommit User
    Guide](http://docs.aws.amazon.com/codecommit/latest/userguide/limits.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetBlobInput(autoboto.ShapeBase):
    """
    Represents the input of a get blob operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "blob_id",
                "blobId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository that contains the blob.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the blob, which is its SHA-1 pointer.
    blob_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetBlobOutput(autoboto.ShapeBase):
    """
    Represents the output of a get blob operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "content",
                "content",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # The content of the blob, usually a file.
    content: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetBranchInput(autoboto.ShapeBase):
    """
    Represents the input of a get branch operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "branch_name",
                "branchName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository that contains the branch for which you want to
    # retrieve information.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the branch for which you want to retrieve information.
    branch_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetBranchOutput(autoboto.ShapeBase):
    """
    Represents the output of a get branch operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "branch",
                "branch",
                autoboto.TypeInfo(BranchInfo),
            ),
        ]

    # The name of the branch.
    branch: "BranchInfo" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetCommentInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment_id",
                "commentId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique, system-generated ID of the comment. To get this ID, use
    # GetCommentsForComparedCommit or GetCommentsForPullRequest.
    comment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCommentOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment",
                "comment",
                autoboto.TypeInfo(Comment),
            ),
        ]

    # The contents of the comment.
    comment: "Comment" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetCommentsForComparedCommitInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "before_commit_id",
                "beforeCommitId",
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

    # The name of the repository where you want to compare commits.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # To establish the directionality of the comparison, the full commit ID of
    # the 'after' commit.
    after_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # To establish the directionality of the comparison, the full commit ID of
    # the 'before' commit.
    before_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An enumeration token that when provided in a request, returns the next
    # batch of the results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A non-negative integer used to limit the number of returned results. The
    # default is 100 comments, and is configurable up to 500.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCommentsForComparedCommitOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comments_for_compared_commit_data",
                "commentsForComparedCommitData",
                autoboto.TypeInfo(typing.List[CommentsForComparedCommit]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of comment objects on the compared commit.
    comments_for_compared_commit_data: typing.List["CommentsForComparedCommit"
                                                  ] = dataclasses.field(
                                                      default_factory=list,
                                                  )

    # An enumeration token that can be used in a request to return the next batch
    # of the results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCommentsForPullRequestInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "before_commit_id",
                "beforeCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
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

    # The system-generated ID of the pull request. To get this ID, use
    # ListPullRequests.
    pull_request_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the repository that contains the pull request.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full commit ID of the commit in the destination branch that was the tip
    # of the branch at the time the pull request was created.
    before_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full commit ID of the commit in the source branch that was the tip of
    # the branch at the time the comment was made.
    after_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An enumeration token that when provided in a request, returns the next
    # batch of the results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A non-negative integer used to limit the number of returned results. The
    # default is 100 comments. You can return up to 500 comments with a single
    # request.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCommentsForPullRequestOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comments_for_pull_request_data",
                "commentsForPullRequestData",
                autoboto.TypeInfo(typing.List[CommentsForPullRequest]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of comment objects on the pull request.
    comments_for_pull_request_data: typing.List["CommentsForPullRequest"
                                               ] = dataclasses.field(
                                                   default_factory=list,
                                               )

    # An enumeration token that can be used in a request to return the next batch
    # of the results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCommitInput(autoboto.ShapeBase):
    """
    Represents the input of a get commit operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "commit_id",
                "commitId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository to which the commit was made.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The commit ID. Commit IDs are the full SHA of the commit.
    commit_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCommitOutput(autoboto.ShapeBase):
    """
    Represents the output of a get commit operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "commit",
                "commit",
                autoboto.TypeInfo(Commit),
            ),
        ]

    # A commit data type object that contains information about the specified
    # commit.
    commit: "Commit" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetDifferencesInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "after_commit_specifier",
                "afterCommitSpecifier",
                autoboto.TypeInfo(str),
            ),
            (
                "before_commit_specifier",
                "beforeCommitSpecifier",
                autoboto.TypeInfo(str),
            ),
            (
                "before_path",
                "beforePath",
                autoboto.TypeInfo(str),
            ),
            (
                "after_path",
                "afterPath",
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

    # The name of the repository where you want to get differences.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The branch, tag, HEAD, or other fully qualified reference used to identify
    # a commit.
    after_commit_specifier: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The branch, tag, HEAD, or other fully qualified reference used to identify
    # a commit. For example, the full commit ID. Optional. If not specified, all
    # changes prior to the `afterCommitSpecifier` value will be shown. If you do
    # not use `beforeCommitSpecifier` in your request, consider limiting the
    # results with `maxResults`.
    before_commit_specifier: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The file path in which to check for differences. Limits the results to this
    # path. Can also be used to specify the previous name of a directory or
    # folder. If `beforePath` and `afterPath` are not specified, differences will
    # be shown for all paths.
    before_path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The file path in which to check differences. Limits the results to this
    # path. Can also be used to specify the changed name of a directory or
    # folder, if it has changed. If not specified, differences will be shown for
    # all paths.
    after_path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A non-negative integer used to limit the number of returned results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An enumeration token that when provided in a request, returns the next
    # batch of the results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDifferencesOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "differences",
                "differences",
                autoboto.TypeInfo(typing.List[Difference]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A differences data type object that contains information about the
    # differences, including whether the difference is added, modified, or
    # deleted (A, D, M).
    differences: typing.List["Difference"] = dataclasses.field(
        default_factory=list,
    )

    # An enumeration token that can be used in a request to return the next batch
    # of the results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetMergeConflictsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "destination_commit_specifier",
                "destinationCommitSpecifier",
                autoboto.TypeInfo(str),
            ),
            (
                "source_commit_specifier",
                "sourceCommitSpecifier",
                autoboto.TypeInfo(str),
            ),
            (
                "merge_option",
                "mergeOption",
                autoboto.TypeInfo(MergeOptionTypeEnum),
            ),
        ]

    # The name of the repository where the pull request was created.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The branch, tag, HEAD, or other fully qualified reference used to identify
    # a commit. For example, a branch name or a full commit ID.
    destination_commit_specifier: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The branch, tag, HEAD, or other fully qualified reference used to identify
    # a commit. For example, a branch name or a full commit ID.
    source_commit_specifier: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The merge option or strategy you want to use to merge the code. The only
    # valid value is FAST_FORWARD_MERGE.
    merge_option: "MergeOptionTypeEnum" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetMergeConflictsOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "mergeable",
                "mergeable",
                autoboto.TypeInfo(bool),
            ),
            (
                "destination_commit_id",
                "destinationCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "source_commit_id",
                "sourceCommitId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A Boolean value that indicates whether the code is mergable by the
    # specified merge option.
    mergeable: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The commit ID of the destination commit specifier that was used in the
    # merge evaluation.
    destination_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The commit ID of the source commit specifier that was used in the merge
    # evaluation.
    source_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetPullRequestInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The system-generated ID of the pull request. To get this ID, use
    # ListPullRequests.
    pull_request_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetPullRequestOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request",
                "pullRequest",
                autoboto.TypeInfo(PullRequest),
            ),
        ]

    # Information about the specified pull request.
    pull_request: "PullRequest" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetRepositoryInput(autoboto.ShapeBase):
    """
    Represents the input of a get repository operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository to get information about.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetRepositoryOutput(autoboto.ShapeBase):
    """
    Represents the output of a get repository operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_metadata",
                "repositoryMetadata",
                autoboto.TypeInfo(RepositoryMetadata),
            ),
        ]

    # Information about the repository.
    repository_metadata: "RepositoryMetadata" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetRepositoryTriggersInput(autoboto.ShapeBase):
    """
    Represents the input of a get repository triggers operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository for which the trigger is configured.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetRepositoryTriggersOutput(autoboto.ShapeBase):
    """
    Represents the output of a get repository triggers operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_id",
                "configurationId",
                autoboto.TypeInfo(str),
            ),
            (
                "triggers",
                "triggers",
                autoboto.TypeInfo(typing.List[RepositoryTrigger]),
            ),
        ]

    # The system-generated unique ID for the trigger.
    configuration_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The JSON block of configuration information for each trigger.
    triggers: typing.List["RepositoryTrigger"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class IdempotencyParameterMismatchException(autoboto.ShapeBase):
    """
    The client request token is not valid. Either the token is not in a valid
    format, or the token has been used in a previous request and cannot be re-used.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidActorArnException(autoboto.ShapeBase):
    """
    The Amazon Resource Name (ARN) is not valid. Make sure that you have provided
    the full ARN for the user who initiated the change for the pull request, and
    then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidAuthorArnException(autoboto.ShapeBase):
    """
    The Amazon Resource Name (ARN) is not valid. Make sure that you have provided
    the full ARN for the author of the pull request, and then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidBlobIdException(autoboto.ShapeBase):
    """
    The specified blob is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidBranchNameException(autoboto.ShapeBase):
    """
    The specified reference name is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidClientRequestTokenException(autoboto.ShapeBase):
    """
    The client request token is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidCommentIdException(autoboto.ShapeBase):
    """
    The comment ID is not in a valid format. Make sure that you have provided the
    full comment ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidCommitException(autoboto.ShapeBase):
    """
    The specified commit is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidCommitIdException(autoboto.ShapeBase):
    """
    The specified commit ID is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidContinuationTokenException(autoboto.ShapeBase):
    """
    The specified continuation token is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDescriptionException(autoboto.ShapeBase):
    """
    The pull request description is not valid. Descriptions are limited to 1,000
    characters in length.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDestinationCommitSpecifierException(autoboto.ShapeBase):
    """
    The destination commit specifier is not valid. You must provide a valid branch
    name, tag, or full commit ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidEmailException(autoboto.ShapeBase):
    """
    The specified email address either contains one or more characters that are not
    allowed, or it exceeds the maximum number of characters allowed for an email
    address.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidFileLocationException(autoboto.ShapeBase):
    """
    The location of the file is not valid. Make sure that you include the extension
    of the file as well as the file name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidFileModeException(autoboto.ShapeBase):
    """
    The specified file mode permission is not valid. For a list of valid file mode
    permissions, see PutFile.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidFilePositionException(autoboto.ShapeBase):
    """
    The position is not valid. Make sure that the line number exists in the version
    of the file you want to comment on.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidMaxResultsException(autoboto.ShapeBase):
    """
    The specified number of maximum results is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidMergeOptionException(autoboto.ShapeBase):
    """
    The specified merge option is not valid. The only valid value is
    FAST_FORWARD_MERGE.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidOrderException(autoboto.ShapeBase):
    """
    The specified sort order is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidParentCommitIdException(autoboto.ShapeBase):
    """
    The parent commit ID is not valid. The commit ID cannot be empty, and must match
    the head commit ID for the branch of the repository where you want to add or
    update a file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidPathException(autoboto.ShapeBase):
    """
    The specified path is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidPullRequestEventTypeException(autoboto.ShapeBase):
    """
    The pull request event type is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidPullRequestIdException(autoboto.ShapeBase):
    """
    The pull request ID is not valid. Make sure that you have provided the full ID
    and that the pull request is in the specified repository, and then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidPullRequestStatusException(autoboto.ShapeBase):
    """
    The pull request status is not valid. The only valid values are `OPEN` and
    `CLOSED`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidPullRequestStatusUpdateException(autoboto.ShapeBase):
    """
    The pull request status update is not valid. The only valid update is from
    `OPEN` to `CLOSED`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidReferenceNameException(autoboto.ShapeBase):
    """
    The specified reference name format is not valid. Reference names must conform
    to the Git references format, for example refs/heads/master. For more
    information, see [Git Internals - Git References](https://git-
    scm.com/book/en/v2/Git-Internals-Git-References) or consult your Git
    documentation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRelativeFileVersionEnumException(autoboto.ShapeBase):
    """
    Either the enum is not in a valid format, or the specified file version enum is
    not valid in respect to the current file version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRepositoryDescriptionException(autoboto.ShapeBase):
    """
    The specified repository description is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRepositoryNameException(autoboto.ShapeBase):
    """
    At least one specified repository name is not valid.

    This exception only occurs when a specified repository name is not valid. Other
    exceptions occur when a required repository parameter is missing, or when a
    specified repository does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRepositoryTriggerBranchNameException(autoboto.ShapeBase):
    """
    One or more branch names specified for the trigger is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRepositoryTriggerCustomDataException(autoboto.ShapeBase):
    """
    The custom data provided for the trigger is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRepositoryTriggerDestinationArnException(autoboto.ShapeBase):
    """
    The Amazon Resource Name (ARN) for the trigger is not valid for the specified
    destination. The most common reason for this error is that the ARN does not meet
    the requirements for the service type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRepositoryTriggerEventsException(autoboto.ShapeBase):
    """
    One or more events specified for the trigger is not valid. Check to make sure
    that all events specified match the requirements for allowed events.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRepositoryTriggerNameException(autoboto.ShapeBase):
    """
    The name of the trigger is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRepositoryTriggerRegionException(autoboto.ShapeBase):
    """
    The region for the trigger target does not match the region for the repository.
    Triggers must be created in the same region as the target for the trigger.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSortByException(autoboto.ShapeBase):
    """
    The specified sort by value is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSourceCommitSpecifierException(autoboto.ShapeBase):
    """
    The source commit specifier is not valid. You must provide a valid branch name,
    tag, or full commit ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTargetException(autoboto.ShapeBase):
    """
    The target for the pull request is not valid. A target must contain the full
    values for the repository name, source branch, and destination branch for the
    pull request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTargetsException(autoboto.ShapeBase):
    """
    The targets for the pull request is not valid or not in a valid format. Targets
    are a list of target objects. Each target object must contain the full values
    for the repository name, source branch, and destination branch for a pull
    request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTitleException(autoboto.ShapeBase):
    """
    The title of the pull request is not valid. Pull request titles cannot exceed
    100 characters in length.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListBranchesInput(autoboto.ShapeBase):
    """
    Represents the input of a list branches operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository that contains the branches.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An enumeration token that allows the operation to batch the results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListBranchesOutput(autoboto.ShapeBase):
    """
    Represents the output of a list branches operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "branches",
                "branches",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of branch names.
    branches: typing.List[str] = dataclasses.field(default_factory=list, )

    # An enumeration token that returns the batch of the results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListPullRequestsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "author_arn",
                "authorArn",
                autoboto.TypeInfo(str),
            ),
            (
                "pull_request_status",
                "pullRequestStatus",
                autoboto.TypeInfo(PullRequestStatusEnum),
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

    # The name of the repository for which you want to list pull requests.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Optional. The Amazon Resource Name (ARN) of the user who created the pull
    # request. If used, this filters the results to pull requests created by that
    # user.
    author_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Optional. The status of the pull request. If used, this refines the results
    # to the pull requests that match the specified status.
    pull_request_status: "PullRequestStatusEnum" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An enumeration token that when provided in a request, returns the next
    # batch of the results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A non-negative integer used to limit the number of returned results.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListPullRequestsOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_ids",
                "pullRequestIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The system-generated IDs of the pull requests.
    pull_request_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # An enumeration token that when provided in a request, returns the next
    # batch of the results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListRepositoriesInput(autoboto.ShapeBase):
    """
    Represents the input of a list repositories operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "sort_by",
                "sortBy",
                autoboto.TypeInfo(SortByEnum),
            ),
            (
                "order",
                "order",
                autoboto.TypeInfo(OrderEnum),
            ),
        ]

    # An enumeration token that allows the operation to batch the results of the
    # operation. Batch sizes are 1,000 for list repository operations. When the
    # client sends the token back to AWS CodeCommit, another page of 1,000
    # records is retrieved.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The criteria used to sort the results of a list repositories operation.
    sort_by: "SortByEnum" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The order in which to sort the results of a list repositories operation.
    order: "OrderEnum" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListRepositoriesOutput(autoboto.ShapeBase):
    """
    Represents the output of a list repositories operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repositories",
                "repositories",
                autoboto.TypeInfo(typing.List[RepositoryNameIdPair]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Lists the repositories called by the list repositories operation.
    repositories: typing.List["RepositoryNameIdPair"] = dataclasses.field(
        default_factory=list,
    )

    # An enumeration token that allows the operation to batch the results of the
    # operation. Batch sizes are 1,000 for list repository operations. When the
    # client sends the token back to AWS CodeCommit, another page of 1,000
    # records is retrieved.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Location(autoboto.ShapeBase):
    """
    Returns information about the location of a change or comment in the comparison
    between two commits or a pull request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_path",
                "filePath",
                autoboto.TypeInfo(str),
            ),
            (
                "file_position",
                "filePosition",
                autoboto.TypeInfo(int),
            ),
            (
                "relative_file_version",
                "relativeFileVersion",
                autoboto.TypeInfo(RelativeFileVersionEnum),
            ),
        ]

    # The name of the file being compared, including its extension and
    # subdirectory, if any.
    file_path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The position of a change within a compared file, in line number format.
    file_position: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # In a comparison of commits or a pull request, whether the change is in the
    # 'before' or 'after' of that comparison.
    relative_file_version: "RelativeFileVersionEnum" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ManualMergeRequiredException(autoboto.ShapeBase):
    """
    The pull request cannot be merged automatically into the destination branch. You
    must manually merge the branches and resolve any conflicts.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class MaximumBranchesExceededException(autoboto.ShapeBase):
    """
    The number of branches for the trigger was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class MaximumOpenPullRequestsExceededException(autoboto.ShapeBase):
    """
    You cannot create the pull request because the repository has too many open pull
    requests. The maximum number of open pull requests for a repository is 1,000.
    Close one or more open pull requests, and then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class MaximumRepositoryNamesExceededException(autoboto.ShapeBase):
    """
    The maximum number of allowed repository names was exceeded. Currently, this
    number is 25.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class MaximumRepositoryTriggersExceededException(autoboto.ShapeBase):
    """
    The number of triggers allowed for the repository was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class MergeMetadata(autoboto.ShapeBase):
    """
    Returns information about a merge or potential merge between a source reference
    and a destination reference in a pull request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "is_merged",
                "isMerged",
                autoboto.TypeInfo(bool),
            ),
            (
                "merged_by",
                "mergedBy",
                autoboto.TypeInfo(str),
            ),
        ]

    # A Boolean value indicating whether the merge has been made.
    is_merged: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Resource Name (ARN) of the user who merged the branches.
    merged_by: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class MergeOptionRequiredException(autoboto.ShapeBase):
    """
    A merge option or stategy is required, and none was provided.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class MergeOptionTypeEnum(Enum):
    FAST_FORWARD_MERGE = "FAST_FORWARD_MERGE"


@dataclasses.dataclass
class MergePullRequestByFastForwardInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "source_commit_id",
                "sourceCommitId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The system-generated ID of the pull request. To get this ID, use
    # ListPullRequests.
    pull_request_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the repository where the pull request was created.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full commit ID of the original or updated commit in the pull request
    # source branch. Pass this value if you want an exception thrown if the
    # current commit ID of the tip of the source branch does not match this
    # commit ID.
    source_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class MergePullRequestByFastForwardOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request",
                "pullRequest",
                autoboto.TypeInfo(PullRequest),
            ),
        ]

    # Information about the specified pull request, including information about
    # the merge.
    pull_request: "PullRequest" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class MultipleRepositoriesInPullRequestException(autoboto.ShapeBase):
    """
    You cannot include more than one repository in a pull request. Make sure you
    have specified only one repository name in your request, and then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NameLengthExceededException(autoboto.ShapeBase):
    """
    The file name is not valid because it has exceeded the character limit for file
    names. File names, including the path to the file, cannot exceed the character
    limit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class OrderEnum(Enum):
    ascending = "ascending"
    descending = "descending"


@dataclasses.dataclass
class ParentCommitDoesNotExistException(autoboto.ShapeBase):
    """
    The parent commit ID is not valid. The specified parent commit ID does not exist
    in the specified branch of the repository.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ParentCommitIdOutdatedException(autoboto.ShapeBase):
    """
    The file could not be added because the provided parent commit ID is not the
    current tip of the specified branch. To view the full commit ID of the current
    head of the branch, use GetBranch.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ParentCommitIdRequiredException(autoboto.ShapeBase):
    """
    A parent commit ID is required. To view the full commit ID of a branch in a
    repository, use GetBranch or a Git command (for example, git pull or git log).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PathDoesNotExistException(autoboto.ShapeBase):
    """
    The specified path does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PathRequiredException(autoboto.ShapeBase):
    """
    The filePath for a location cannot be empty or null.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PostCommentForComparedCommitInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "content",
                "content",
                autoboto.TypeInfo(str),
            ),
            (
                "before_commit_id",
                "beforeCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(Location),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository where you want to post a comment on the
    # comparison between commits.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # To establish the directionality of the comparison, the full commit ID of
    # the 'after' commit.
    after_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The content of the comment you want to make.
    content: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # To establish the directionality of the comparison, the full commit ID of
    # the 'before' commit.
    before_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The location of the comparison where you want to comment.
    location: "Location" = dataclasses.field(default_factory=dict, )

    # A unique, client-generated idempotency token that when provided in a
    # request, ensures the request cannot be repeated with a changed parameter.
    # If a request is received with the same parameters and a token is included,
    # the request will return information about the initial request that used
    # that token.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PostCommentForComparedCommitOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "before_commit_id",
                "beforeCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "before_blob_id",
                "beforeBlobId",
                autoboto.TypeInfo(str),
            ),
            (
                "after_blob_id",
                "afterBlobId",
                autoboto.TypeInfo(str),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(Location),
            ),
            (
                "comment",
                "comment",
                autoboto.TypeInfo(Comment),
            ),
        ]

    # The name of the repository where you posted a comment on the comparison
    # between commits.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # In the directionality you established, the full commit ID of the 'before'
    # commit.
    before_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # In the directionality you established, the full commit ID of the 'after'
    # commit.
    after_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # In the directionality you established, the blob ID of the 'before' blob.
    before_blob_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # In the directionality you established, the blob ID of the 'after' blob.
    after_blob_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The location of the comment in the comparison between the two commits.
    location: "Location" = dataclasses.field(default_factory=dict, )

    # The content of the comment you posted.
    comment: "Comment" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PostCommentForPullRequestInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "before_commit_id",
                "beforeCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "content",
                "content",
                autoboto.TypeInfo(str),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(Location),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The system-generated ID of the pull request. To get this ID, use
    # ListPullRequests.
    pull_request_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the repository where you want to post a comment on a pull
    # request.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full commit ID of the commit in the destination branch that was the tip
    # of the branch at the time the pull request was created.
    before_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full commit ID of the commit in the source branch that is the current
    # tip of the branch for the pull request when you post the comment.
    after_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The content of your comment on the change.
    content: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The location of the change where you want to post your comment. If no
    # location is provided, the comment will be posted as a general comment on
    # the pull request difference between the before commit ID and the after
    # commit ID.
    location: "Location" = dataclasses.field(default_factory=dict, )

    # A unique, client-generated idempotency token that when provided in a
    # request, ensures the request cannot be repeated with a changed parameter.
    # If a request is received with the same parameters and a token is included,
    # the request will return information about the initial request that used
    # that token.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PostCommentForPullRequestOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "pull_request_id",
                "pullRequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "before_commit_id",
                "beforeCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "before_blob_id",
                "beforeBlobId",
                autoboto.TypeInfo(str),
            ),
            (
                "after_blob_id",
                "afterBlobId",
                autoboto.TypeInfo(str),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(Location),
            ),
            (
                "comment",
                "comment",
                autoboto.TypeInfo(Comment),
            ),
        ]

    # The name of the repository where you posted a comment on a pull request.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The system-generated ID of the pull request.
    pull_request_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full commit ID of the commit in the source branch used to create the
    # pull request, or in the case of an updated pull request, the full commit ID
    # of the commit used to update the pull request.
    before_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full commit ID of the commit in the destination branch where the pull
    # request will be merged.
    after_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # In the directionality of the pull request, the blob ID of the 'before'
    # blob.
    before_blob_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # In the directionality of the pull request, the blob ID of the 'after' blob.
    after_blob_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The location of the change where you posted your comment.
    location: "Location" = dataclasses.field(default_factory=dict, )

    # The content of the comment you posted.
    comment: "Comment" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PostCommentReplyInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "in_reply_to",
                "inReplyTo",
                autoboto.TypeInfo(str),
            ),
            (
                "content",
                "content",
                autoboto.TypeInfo(str),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The system-generated ID of the comment to which you want to reply. To get
    # this ID, use GetCommentsForComparedCommit or GetCommentsForPullRequest.
    in_reply_to: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The contents of your reply to a comment.
    content: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A unique, client-generated idempotency token that when provided in a
    # request, ensures the request cannot be repeated with a changed parameter.
    # If a request is received with the same parameters and a token is included,
    # the request will return information about the initial request that used
    # that token.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PostCommentReplyOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment",
                "comment",
                autoboto.TypeInfo(Comment),
            ),
        ]

    # Information about the reply to a comment.
    comment: "Comment" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PullRequest(autoboto.ShapeBase):
    """
    Returns information about a pull request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "title",
                "title",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "last_activity_date",
                "lastActivityDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "pull_request_status",
                "pullRequestStatus",
                autoboto.TypeInfo(PullRequestStatusEnum),
            ),
            (
                "author_arn",
                "authorArn",
                autoboto.TypeInfo(str),
            ),
            (
                "pull_request_targets",
                "pullRequestTargets",
                autoboto.TypeInfo(typing.List[PullRequestTarget]),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The system-generated ID of the pull request.
    pull_request_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The user-defined title of the pull request. This title is displayed in the
    # list of pull requests to other users of the repository.
    title: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user-defined description of the pull request. This description can be
    # used to clarify what should be reviewed and other details of the request.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The day and time of the last user or system activity on the pull request,
    # in timestamp format.
    last_activity_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time the pull request was originally created, in timestamp
    # format.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the pull request. Pull request status can only change from
    # `OPEN` to `CLOSED`.
    pull_request_status: "PullRequestStatusEnum" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the user who created the pull request.
    author_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The targets of the pull request, including the source branch and
    # destination branch for the pull request.
    pull_request_targets: typing.List["PullRequestTarget"] = dataclasses.field(
        default_factory=list,
    )

    # A unique, client-generated idempotency token that when provided in a
    # request, ensures the request cannot be repeated with a changed parameter.
    # If a request is received with the same parameters and a token is included,
    # the request will return information about the initial request that used
    # that token.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PullRequestAlreadyClosedException(autoboto.ShapeBase):
    """
    The pull request status cannot be updated because it is already closed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PullRequestDoesNotExistException(autoboto.ShapeBase):
    """
    The pull request ID could not be found. Make sure that you have specified the
    correct repository name and pull request ID, and then try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PullRequestEvent(autoboto.ShapeBase):
    """
    Returns information about a pull request event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "event_date",
                "eventDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "pull_request_event_type",
                "pullRequestEventType",
                autoboto.TypeInfo(PullRequestEventType),
            ),
            (
                "actor_arn",
                "actorArn",
                autoboto.TypeInfo(str),
            ),
            (
                "pull_request_status_changed_event_metadata",
                "pullRequestStatusChangedEventMetadata",
                autoboto.TypeInfo(PullRequestStatusChangedEventMetadata),
            ),
            (
                "pull_request_source_reference_updated_event_metadata",
                "pullRequestSourceReferenceUpdatedEventMetadata",
                autoboto.
                TypeInfo(PullRequestSourceReferenceUpdatedEventMetadata),
            ),
            (
                "pull_request_merged_state_changed_event_metadata",
                "pullRequestMergedStateChangedEventMetadata",
                autoboto.TypeInfo(PullRequestMergedStateChangedEventMetadata),
            ),
        ]

    # The system-generated ID of the pull request.
    pull_request_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The day and time of the pull request event, in timestamp format.
    event_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of the pull request event, for example a status change event
    # (PULL_REQUEST_STATUS_CHANGED) or update event
    # (PULL_REQUEST_SOURCE_REFERENCE_UPDATED).
    pull_request_event_type: "PullRequestEventType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the user whose actions resulted in the
    # event. Examples include updating the pull request with additional commits
    # or changing the status of a pull request.
    actor_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information about the change in status for the pull request event.
    pull_request_status_changed_event_metadata: "PullRequestStatusChangedEventMetadata" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the updated source branch for the pull request event.
    pull_request_source_reference_updated_event_metadata: "PullRequestSourceReferenceUpdatedEventMetadata" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the change in mergability state for the pull request
    # event.
    pull_request_merged_state_changed_event_metadata: "PullRequestMergedStateChangedEventMetadata" = dataclasses.field(
        default_factory=dict,
    )


class PullRequestEventType(Enum):
    PULL_REQUEST_CREATED = "PULL_REQUEST_CREATED"
    PULL_REQUEST_STATUS_CHANGED = "PULL_REQUEST_STATUS_CHANGED"
    PULL_REQUEST_SOURCE_REFERENCE_UPDATED = "PULL_REQUEST_SOURCE_REFERENCE_UPDATED"
    PULL_REQUEST_MERGE_STATE_CHANGED = "PULL_REQUEST_MERGE_STATE_CHANGED"


@dataclasses.dataclass
class PullRequestIdRequiredException(autoboto.ShapeBase):
    """
    A pull request ID is required, but none was provided.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PullRequestMergedStateChangedEventMetadata(autoboto.ShapeBase):
    """
    Returns information about the change in the merge state for a pull request
    event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "destination_reference",
                "destinationReference",
                autoboto.TypeInfo(str),
            ),
            (
                "merge_metadata",
                "mergeMetadata",
                autoboto.TypeInfo(MergeMetadata),
            ),
        ]

    # The name of the repository where the pull request was created.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the branch that the pull request will be merged into.
    destination_reference: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the merge state change event.
    merge_metadata: "MergeMetadata" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PullRequestSourceReferenceUpdatedEventMetadata(autoboto.ShapeBase):
    """
    Information about an update to the source branch of a pull request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "before_commit_id",
                "beforeCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "after_commit_id",
                "afterCommitId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository where the pull request was updated.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full commit ID of the commit in the destination branch that was the tip
    # of the branch at the time the pull request was updated.
    before_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full commit ID of the commit in the source branch that was the tip of
    # the branch at the time the pull request was updated.
    after_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PullRequestStatusChangedEventMetadata(autoboto.ShapeBase):
    """
    Information about a change to the status of a pull request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_status",
                "pullRequestStatus",
                autoboto.TypeInfo(PullRequestStatusEnum),
            ),
        ]

    # The changed status of the pull request.
    pull_request_status: "PullRequestStatusEnum" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class PullRequestStatusEnum(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"


@dataclasses.dataclass
class PullRequestStatusRequiredException(autoboto.ShapeBase):
    """
    A pull request status is required, but none was provided.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PullRequestTarget(autoboto.ShapeBase):
    """
    Returns information about a pull request target.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "source_reference",
                "sourceReference",
                autoboto.TypeInfo(str),
            ),
            (
                "destination_reference",
                "destinationReference",
                autoboto.TypeInfo(str),
            ),
            (
                "destination_commit",
                "destinationCommit",
                autoboto.TypeInfo(str),
            ),
            (
                "source_commit",
                "sourceCommit",
                autoboto.TypeInfo(str),
            ),
            (
                "merge_metadata",
                "mergeMetadata",
                autoboto.TypeInfo(MergeMetadata),
            ),
        ]

    # The name of the repository that contains the pull request source and
    # destination branches.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The branch of the repository that contains the changes for the pull
    # request. Also known as the source branch.
    source_reference: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The branch of the repository where the pull request changes will be merged
    # into. Also known as the destination branch.
    destination_reference: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full commit ID that is the tip of the destination branch. This is the
    # commit where the pull request was or will be merged.
    destination_commit: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full commit ID of the tip of the source branch used to create the pull
    # request. If the pull request branch is updated by a push while the pull
    # request is open, the commit ID will change to reflect the new tip of the
    # branch.
    source_commit: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Returns metadata about the state of the merge, including whether the merge
    # has been made.
    merge_metadata: "MergeMetadata" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PutFileInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "branch_name",
                "branchName",
                autoboto.TypeInfo(str),
            ),
            (
                "file_content",
                "fileContent",
                autoboto.TypeInfo(typing.Any),
            ),
            (
                "file_path",
                "filePath",
                autoboto.TypeInfo(str),
            ),
            (
                "file_mode",
                "fileMode",
                autoboto.TypeInfo(FileModeTypeEnum),
            ),
            (
                "parent_commit_id",
                "parentCommitId",
                autoboto.TypeInfo(str),
            ),
            (
                "commit_message",
                "commitMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "email",
                "email",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository where you want to add or update the file.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the branch where you want to add or update the file.
    branch_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The content of the file, in binary object format.
    file_content: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the file you want to add or update, including the relative path
    # to the file in the repository.

    # If the path does not currently exist in the repository, the path will be
    # created as part of adding the file.
    file_path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The file mode permissions of the blob. Valid file mode permissions are
    # listed below.
    file_mode: "FileModeTypeEnum" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The full commit ID of the head commit in the branch where you want to add
    # or update the file. If the commit ID does not match the ID of the head
    # commit at the time of the operation, an error will occur, and the file will
    # not be added or updated.
    parent_commit_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A message about why this file was added or updated. While optional, adding
    # a message is strongly encouraged in order to provide a more useful commit
    # history for your repository.
    commit_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the person adding or updating the file. While optional, adding
    # a name is strongly encouraged in order to provide a more useful commit
    # history for your repository.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An email address for the person adding or updating the file.
    email: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PutFileOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "commit_id",
                "commitId",
                autoboto.TypeInfo(str),
            ),
            (
                "blob_id",
                "blobId",
                autoboto.TypeInfo(str),
            ),
            (
                "tree_id",
                "treeId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The full SHA of the commit that contains this file change.
    commit_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the blob, which is its SHA-1 pointer.
    blob_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Tree information for the commit that contains this file change.
    tree_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PutRepositoryTriggersInput(autoboto.ShapeBase):
    """
    Represents the input ofa put repository triggers operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "triggers",
                "triggers",
                autoboto.TypeInfo(typing.List[RepositoryTrigger]),
            ),
        ]

    # The name of the repository where you want to create or update the trigger.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The JSON block of configuration information for each trigger.
    triggers: typing.List["RepositoryTrigger"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class PutRepositoryTriggersOutput(autoboto.ShapeBase):
    """
    Represents the output of a put repository triggers operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_id",
                "configurationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The system-generated unique ID for the create or update operation.
    configuration_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ReferenceDoesNotExistException(autoboto.ShapeBase):
    """
    The specified reference does not exist. You must provide a full commit ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReferenceNameRequiredException(autoboto.ShapeBase):
    """
    A reference name is required, but none was provided.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReferenceTypeNotSupportedException(autoboto.ShapeBase):
    """
    The specified reference is not a supported type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class RelativeFileVersionEnum(Enum):
    BEFORE = "BEFORE"
    AFTER = "AFTER"


@dataclasses.dataclass
class RepositoryDoesNotExistException(autoboto.ShapeBase):
    """
    The specified repository does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryLimitExceededException(autoboto.ShapeBase):
    """
    A repository resource limit was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryMetadata(autoboto.ShapeBase):
    """
    Information about a repository.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_id",
                "repositoryId",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_description",
                "repositoryDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "default_branch",
                "defaultBranch",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified_date",
                "lastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "creation_date",
                "creationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "clone_url_http",
                "cloneUrlHttp",
                autoboto.TypeInfo(str),
            ),
            (
                "clone_url_ssh",
                "cloneUrlSsh",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS account associated with the repository.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the repository.
    repository_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The repository's name.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A comment or description about the repository.
    repository_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The repository's default branch name.
    default_branch: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time the repository was last modified, in timestamp format.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time the repository was created, in timestamp format.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URL to use for cloning the repository over HTTPS.
    clone_url_http: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URL to use for cloning the repository over SSH.
    clone_url_ssh: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the repository.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RepositoryNameExistsException(autoboto.ShapeBase):
    """
    The specified repository name already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryNameIdPair(autoboto.ShapeBase):
    """
    Information about a repository name and ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_id",
                "repositoryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name associated with the repository.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID associated with the repository.
    repository_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RepositoryNameRequiredException(autoboto.ShapeBase):
    """
    A repository name is required but was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryNamesRequiredException(autoboto.ShapeBase):
    """
    A repository names object is required but was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryNotAssociatedWithPullRequestException(autoboto.ShapeBase):
    """
    The repository does not contain any pull requests with that pull request ID.
    Check to make sure you have provided the correct repository name for the pull
    request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryTrigger(autoboto.ShapeBase):
    """
    Information about a trigger for a repository.
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
                "destination_arn",
                "destinationArn",
                autoboto.TypeInfo(str),
            ),
            (
                "events",
                "events",
                autoboto.TypeInfo(typing.List[RepositoryTriggerEventEnum]),
            ),
            (
                "custom_data",
                "customData",
                autoboto.TypeInfo(str),
            ),
            (
                "branches",
                "branches",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the trigger.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of the resource that is the target for a trigger. For example, the
    # ARN of a topic in Amazon Simple Notification Service (SNS).
    destination_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The repository events that will cause the trigger to run actions in another
    # service, such as sending a notification through Amazon Simple Notification
    # Service (SNS).

    # The valid value "all" cannot be used with any other values.
    events: typing.List["RepositoryTriggerEventEnum"] = dataclasses.field(
        default_factory=list,
    )

    # Any custom data associated with the trigger that will be included in the
    # information sent to the target of the trigger.
    custom_data: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The branches that will be included in the trigger configuration. If you
    # specify an empty array, the trigger will apply to all branches.

    # While no content is required in the array, you must include the array
    # itself.
    branches: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class RepositoryTriggerBranchNameListRequiredException(autoboto.ShapeBase):
    """
    At least one branch name is required but was not specified in the trigger
    configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryTriggerDestinationArnRequiredException(autoboto.ShapeBase):
    """
    A destination ARN for the target service for the trigger is required but was not
    specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class RepositoryTriggerEventEnum(Enum):
    all = "all"
    updateReference = "updateReference"
    createReference = "createReference"
    deleteReference = "deleteReference"


@dataclasses.dataclass
class RepositoryTriggerEventsListRequiredException(autoboto.ShapeBase):
    """
    At least one event for the trigger is required but was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryTriggerExecutionFailure(autoboto.ShapeBase):
    """
    A trigger failed to run.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trigger",
                "trigger",
                autoboto.TypeInfo(str),
            ),
            (
                "failure_message",
                "failureMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the trigger that did not run.
    trigger: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Additional message information about the trigger that did not run.
    failure_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RepositoryTriggerNameRequiredException(autoboto.ShapeBase):
    """
    A name for the trigger is required but was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RepositoryTriggersListRequiredException(autoboto.ShapeBase):
    """
    The list of triggers for the repository is required but was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SameFileContentException(autoboto.ShapeBase):
    """
    The file was not added or updated because the content of the file is exactly the
    same as the content of that file in the repository and branch that you
    specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class SortByEnum(Enum):
    repositoryName = "repositoryName"
    lastModifiedDate = "lastModifiedDate"


@dataclasses.dataclass
class SourceAndDestinationAreSameException(autoboto.ShapeBase):
    """
    The source branch and the destination branch for the pull request are the same.
    You must specify different branches for the source and destination.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Target(autoboto.ShapeBase):
    """
    Returns information about a target for a pull request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "source_reference",
                "sourceReference",
                autoboto.TypeInfo(str),
            ),
            (
                "destination_reference",
                "destinationReference",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository that contains the pull request.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The branch of the repository that contains the changes for the pull
    # request. Also known as the source branch.
    source_reference: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The branch of the repository where the pull request changes will be merged
    # into. Also known as the destination branch.
    destination_reference: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class TargetRequiredException(autoboto.ShapeBase):
    """
    A pull request target is required. It cannot be empty or null. A pull request
    target must contain the full values for the repository name, source branch, and
    destination branch for the pull request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TargetsRequiredException(autoboto.ShapeBase):
    """
    An array of target objects is required. It cannot be empty or null.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TestRepositoryTriggersInput(autoboto.ShapeBase):
    """
    Represents the input of a test repository triggers operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "triggers",
                "triggers",
                autoboto.TypeInfo(typing.List[RepositoryTrigger]),
            ),
        ]

    # The name of the repository in which to test the triggers.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The list of triggers to test.
    triggers: typing.List["RepositoryTrigger"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class TestRepositoryTriggersOutput(autoboto.ShapeBase):
    """
    Represents the output of a test repository triggers operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "successful_executions",
                "successfulExecutions",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "failed_executions",
                "failedExecutions",
                autoboto.TypeInfo(
                    typing.List[RepositoryTriggerExecutionFailure]
                ),
            ),
        ]

    # The list of triggers that were successfully tested. This list provides the
    # names of the triggers that were successfully tested, separated by commas.
    successful_executions: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The list of triggers that were not able to be tested. This list provides
    # the names of the triggers that could not be tested, separated by commas.
    failed_executions: typing.List["RepositoryTriggerExecutionFailure"
                                  ] = dataclasses.field(
                                      default_factory=list,
                                  )


@dataclasses.dataclass
class TipOfSourceReferenceIsDifferentException(autoboto.ShapeBase):
    """
    The tip of the source branch in the destination repository does not match the
    tip of the source branch specified in your request. The pull request might have
    been updated. Make sure that you have the latest changes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TipsDivergenceExceededException(autoboto.ShapeBase):
    """
    The divergence between the tips of the provided commit specifiers is too great
    to determine whether there might be any merge conflicts. Locally compare the
    specifiers using `git diff` or a diff tool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TitleRequiredException(autoboto.ShapeBase):
    """
    A pull request title is required. It cannot be empty or null.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateCommentInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment_id",
                "commentId",
                autoboto.TypeInfo(str),
            ),
            (
                "content",
                "content",
                autoboto.TypeInfo(str),
            ),
        ]

    # The system-generated ID of the comment you want to update. To get this ID,
    # use GetCommentsForComparedCommit or GetCommentsForPullRequest.
    comment_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The updated content with which you want to replace the existing content of
    # the comment.
    content: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateCommentOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment",
                "comment",
                autoboto.TypeInfo(Comment),
            ),
        ]

    # Information about the updated comment.
    comment: "Comment" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateDefaultBranchInput(autoboto.ShapeBase):
    """
    Represents the input of an update default branch operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "default_branch_name",
                "defaultBranchName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository to set or change the default branch for.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the branch to set as the default.
    default_branch_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdatePullRequestDescriptionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The system-generated ID of the pull request. To get this ID, use
    # ListPullRequests.
    pull_request_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The updated content of the description for the pull request. This content
    # will replace the existing description.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdatePullRequestDescriptionOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request",
                "pullRequest",
                autoboto.TypeInfo(PullRequest),
            ),
        ]

    # Information about the updated pull request.
    pull_request: "PullRequest" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdatePullRequestStatusInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "pull_request_status",
                "pullRequestStatus",
                autoboto.TypeInfo(PullRequestStatusEnum),
            ),
        ]

    # The system-generated ID of the pull request. To get this ID, use
    # ListPullRequests.
    pull_request_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the pull request. The only valid operations are to update the
    # status from `OPEN` to `OPEN`, `OPEN` to `CLOSED` or from from `CLOSED` to
    # `CLOSED`.
    pull_request_status: "PullRequestStatusEnum" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdatePullRequestStatusOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request",
                "pullRequest",
                autoboto.TypeInfo(PullRequest),
            ),
        ]

    # Information about the pull request.
    pull_request: "PullRequest" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdatePullRequestTitleInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request_id",
                "pullRequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "title",
                "title",
                autoboto.TypeInfo(str),
            ),
        ]

    # The system-generated ID of the pull request. To get this ID, use
    # ListPullRequests.
    pull_request_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The updated title of the pull request. This will replace the existing
    # title.
    title: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdatePullRequestTitleOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pull_request",
                "pullRequest",
                autoboto.TypeInfo(PullRequest),
            ),
        ]

    # Information about the updated pull request.
    pull_request: "PullRequest" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateRepositoryDescriptionInput(autoboto.ShapeBase):
    """
    Represents the input of an update repository description operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_name",
                "repositoryName",
                autoboto.TypeInfo(str),
            ),
            (
                "repository_description",
                "repositoryDescription",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the repository to set or change the comment or description for.
    repository_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The new comment or description for the specified repository. Repository
    # descriptions are limited to 1,000 characters.
    repository_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateRepositoryNameInput(autoboto.ShapeBase):
    """
    Represents the input of an update repository description operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "old_name",
                "oldName",
                autoboto.TypeInfo(str),
            ),
            (
                "new_name",
                "newName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The existing name of the repository.
    old_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new name for the repository.
    new_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UserInfo(autoboto.ShapeBase):
    """
    Information about the user who made a specified commit.
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
                "email",
                "email",
                autoboto.TypeInfo(str),
            ),
            (
                "date",
                "date",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the user who made the specified commit.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The email address associated with the user who made the commit, if any.
    email: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date when the specified commit was commited, in timestamp format with
    # GMT offset.
    date: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class blob(botocore.response.StreamingBody):
    pass
