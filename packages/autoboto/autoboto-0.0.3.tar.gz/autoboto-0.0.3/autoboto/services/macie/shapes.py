import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AccessDeniedException(autoboto.ShapeBase):
    """
    You do not have required permissions to access the requested resource.
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
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Resource type that caused the exception
    resource_type: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AssociateMemberAccountRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "member_account_id",
                "memberAccountId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the AWS account that you want to associate with Amazon Macie as a
    # member account.
    member_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AssociateS3ResourcesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_resources",
                "s3Resources",
                autoboto.TypeInfo(typing.List[S3ResourceClassification]),
            ),
            (
                "member_account_id",
                "memberAccountId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The S3 resources that you want to associate with Amazon Macie for
    # monitoring and data classification.
    s3_resources: typing.List["S3ResourceClassification"] = dataclasses.field(
        default_factory=list,
    )

    # The ID of the Amazon Macie member account whose resources you want to
    # associate with Macie.
    member_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AssociateS3ResourcesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failed_s3_resources",
                "failedS3Resources",
                autoboto.TypeInfo(typing.List[FailedS3Resource]),
            ),
        ]

    # S3 resources that couldn't be associated with Amazon Macie. An error code
    # and an error message are provided for each failed item.
    failed_s3_resources: typing.List["FailedS3Resource"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ClassificationType(autoboto.ShapeBase):
    """
    The classification type that Amazon Macie applies to the associated S3
    resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "one_time",
                "oneTime",
                autoboto.TypeInfo(S3OneTimeClassificationType),
            ),
            (
                "continuous",
                "continuous",
                autoboto.TypeInfo(S3ContinuousClassificationType),
            ),
        ]

    # A one-time classification of all of the existing objects in a specified S3
    # bucket.
    one_time: "S3OneTimeClassificationType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A continuous classification of the objects that are added to a specified S3
    # bucket. Amazon Macie begins performing continuous classification after a
    # bucket is successfully associated with Amazon Macie.
    continuous: "S3ContinuousClassificationType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ClassificationTypeUpdate(autoboto.ShapeBase):
    """
    The classification type that Amazon Macie applies to the associated S3
    resources. At least one of the classification types (oneTime or continuous) must
    be specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "one_time",
                "oneTime",
                autoboto.TypeInfo(S3OneTimeClassificationType),
            ),
            (
                "continuous",
                "continuous",
                autoboto.TypeInfo(S3ContinuousClassificationType),
            ),
        ]

    # A one-time classification of all of the existing objects in a specified S3
    # bucket.
    one_time: "S3OneTimeClassificationType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A continuous classification of the objects that are added to a specified S3
    # bucket. Amazon Macie begins performing continuous classification after a
    # bucket is successfully associated with Amazon Macie.
    continuous: "S3ContinuousClassificationType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DisassociateMemberAccountRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "member_account_id",
                "memberAccountId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the member account that you want to remove from Amazon Macie.
    member_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DisassociateS3ResourcesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "associated_s3_resources",
                "associatedS3Resources",
                autoboto.TypeInfo(typing.List[S3Resource]),
            ),
            (
                "member_account_id",
                "memberAccountId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The S3 resources (buckets or prefixes) that you want to remove from being
    # monitored and classified by Amazon Macie.
    associated_s3_resources: typing.List["S3Resource"] = dataclasses.field(
        default_factory=list,
    )

    # The ID of the Amazon Macie member account whose resources you want to
    # remove from being monitored by Amazon Macie.
    member_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DisassociateS3ResourcesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failed_s3_resources",
                "failedS3Resources",
                autoboto.TypeInfo(typing.List[FailedS3Resource]),
            ),
        ]

    # S3 resources that couldn't be removed from being monitored and classified
    # by Amazon Macie. An error code and an error message are provided for each
    # failed item.
    failed_s3_resources: typing.List["FailedS3Resource"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class FailedS3Resource(autoboto.ShapeBase):
    """
    Includes details about the failed S3 resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failed_item",
                "failedItem",
                autoboto.TypeInfo(S3Resource),
            ),
            (
                "error_code",
                "errorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "error_message",
                "errorMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The failed S3 resources.
    failed_item: "S3Resource" = dataclasses.field(default_factory=dict, )

    # The status code of a failed item.
    error_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The error message of a failed item.
    error_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class InternalException(autoboto.ShapeBase):
    """
    Internal server error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "errorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    # Error code for the exception
    error_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidInputException(autoboto.ShapeBase):
    """
    The request was rejected because an invalid or out-of-range value was supplied
    for an input parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "errorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "field_name",
                "fieldName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Error code for the exception
    error_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Field that has invalid input
    field_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    The request was rejected because it attempted to create resources beyond the
    current AWS account limits. The error code describes the limit exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "errorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(str),
            ),
        ]

    # Error code for the exception
    error_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Resource type that caused the exception
    resource_type: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListMemberAccountsRequest(autoboto.ShapeBase):
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

    # Use this parameter when paginating results. Set the value of this parameter
    # to null on your first call to the ListMemberAccounts action. Subsequent
    # calls to the action fill nextToken in the request with the value of
    # nextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Use this parameter to indicate the maximum number of items that you want in
    # the response. The default value is 250.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListMemberAccountsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "member_accounts",
                "memberAccounts",
                autoboto.TypeInfo(typing.List[MemberAccount]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of the Amazon Macie member accounts returned by the action. The
    # current master account is also included in this list.
    member_accounts: typing.List["MemberAccount"] = dataclasses.field(
        default_factory=list,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # nextToken parameter in a subsequent pagination request. If there is no more
    # data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListS3ResourcesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "member_account_id",
                "memberAccountId",
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

    # The Amazon Macie member account ID whose associated S3 resources you want
    # to list.
    member_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Use this parameter when paginating results. Set its value to null on your
    # first call to the ListS3Resources action. Subsequent calls to the action
    # fill nextToken in the request with the value of nextToken from the previous
    # response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Use this parameter to indicate the maximum number of items that you want in
    # the response. The default value is 250.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListS3ResourcesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_resources",
                "s3Resources",
                autoboto.TypeInfo(typing.List[S3ResourceClassification]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of the associated S3 resources returned by the action.
    s3_resources: typing.List["S3ResourceClassification"] = dataclasses.field(
        default_factory=list,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # nextToken parameter in a subsequent pagination request. If there is no more
    # data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class MemberAccount(autoboto.ShapeBase):
    """
    Contains information about the Amazon Macie member account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The AWS account ID of the Amazon Macie member account.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class S3ContinuousClassificationType(Enum):
    FULL = "FULL"


class S3OneTimeClassificationType(Enum):
    FULL = "FULL"
    NONE = "NONE"


@dataclasses.dataclass
class S3Resource(autoboto.ShapeBase):
    """
    Contains information about the S3 resource. This data type is used as a request
    parameter in the DisassociateS3Resources action and can be used as a response
    parameter in the AssociateS3Resources and UpdateS3Resources actions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket_name",
                "bucketName",
                autoboto.TypeInfo(str),
            ),
            (
                "prefix",
                "prefix",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the S3 bucket.
    bucket_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The prefix of the S3 bucket.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class S3ResourceClassification(autoboto.ShapeBase):
    """
    The S3 resources that you want to associate with Amazon Macie for monitoring and
    data classification. This data type is used as a request parameter in the
    AssociateS3Resources action and a response parameter in the ListS3Resources
    action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket_name",
                "bucketName",
                autoboto.TypeInfo(str),
            ),
            (
                "classification_type",
                "classificationType",
                autoboto.TypeInfo(ClassificationType),
            ),
            (
                "prefix",
                "prefix",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the S3 bucket that you want to associate with Amazon Macie.
    bucket_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The classification type that you want to specify for the resource
    # associated with Amazon Macie.
    classification_type: "ClassificationType" = dataclasses.field(
        default_factory=dict,
    )

    # The prefix of the S3 bucket that you want to associate with Amazon Macie.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class S3ResourceClassificationUpdate(autoboto.ShapeBase):
    """
    The S3 resources whose classification types you want to update. This data type
    is used as a request parameter in the UpdateS3Resources action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket_name",
                "bucketName",
                autoboto.TypeInfo(str),
            ),
            (
                "classification_type_update",
                "classificationTypeUpdate",
                autoboto.TypeInfo(ClassificationTypeUpdate),
            ),
            (
                "prefix",
                "prefix",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the S3 bucket whose classification types you want to update.
    bucket_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The classification type that you want to update for the resource associated
    # with Amazon Macie.
    classification_type_update: "ClassificationTypeUpdate" = dataclasses.field(
        default_factory=dict,
    )

    # The prefix of the S3 bucket whose classification types you want to update.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateS3ResourcesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_resources_update",
                "s3ResourcesUpdate",
                autoboto.TypeInfo(typing.List[S3ResourceClassificationUpdate]),
            ),
            (
                "member_account_id",
                "memberAccountId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The S3 resources whose classification types you want to update.
    s3_resources_update: typing.List["S3ResourceClassificationUpdate"
                                    ] = dataclasses.field(
                                        default_factory=list,
                                    )

    # The AWS ID of the Amazon Macie member account whose S3 resources'
    # classification types you want to update.
    member_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateS3ResourcesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failed_s3_resources",
                "failedS3Resources",
                autoboto.TypeInfo(typing.List[FailedS3Resource]),
            ),
        ]

    # The S3 resources whose classification types can't be updated. An error code
    # and an error message are provided for each failed item.
    failed_s3_resources: typing.List["FailedS3Resource"] = dataclasses.field(
        default_factory=list,
    )
