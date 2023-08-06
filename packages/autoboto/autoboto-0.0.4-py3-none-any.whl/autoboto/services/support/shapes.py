import datetime
import typing
import autoboto
import botocore.response
import dataclasses


@dataclasses.dataclass
class AddAttachmentsToSetRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attachments",
                "attachments",
                autoboto.TypeInfo(typing.List[Attachment]),
            ),
            (
                "attachment_set_id",
                "attachmentSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # One or more attachments to add to the set. The limit is 3 attachments per
    # set, and the size limit is 5 MB per attachment.
    attachments: typing.List["Attachment"] = dataclasses.field(
        default_factory=list,
    )

    # The ID of the attachment set. If an `attachmentSetId` is not specified, a
    # new attachment set is created, and the ID of the set is returned in the
    # response. If an `attachmentSetId` is specified, the attachments are added
    # to the specified set, if it exists.
    attachment_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddAttachmentsToSetResponse(autoboto.ShapeBase):
    """
    The ID and expiry time of the attachment set returned by the AddAttachmentsToSet
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attachment_set_id",
                "attachmentSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "expiry_time",
                "expiryTime",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the attachment set. If an `attachmentSetId` was not specified, a
    # new attachment set is created, and the ID of the set is returned in the
    # response. If an `attachmentSetId` was specified, the attachments are added
    # to the specified set, if it exists.
    attachment_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time and date when the attachment set expires.
    expiry_time: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddCommunicationToCaseRequest(autoboto.ShapeBase):
    """
    To be written.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "communication_body",
                "communicationBody",
                autoboto.TypeInfo(str),
            ),
            (
                "case_id",
                "caseId",
                autoboto.TypeInfo(str),
            ),
            (
                "cc_email_addresses",
                "ccEmailAddresses",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "attachment_set_id",
                "attachmentSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The body of an email communication to add to the support case.
    communication_body: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS Support case ID requested or returned in the call. The case ID is
    # an alphanumeric string formatted as shown in this example: case-
    # _12345678910-2013-c4c1d2bf33c5cf47_
    case_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The email addresses in the CC line of an email to be added to the support
    # case.
    cc_email_addresses: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The ID of a set of one or more attachments for the communication to add to
    # the case. Create the set by calling AddAttachmentsToSet
    attachment_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddCommunicationToCaseResponse(autoboto.ShapeBase):
    """
    The result of the AddCommunicationToCase operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "result",
                "result",
                autoboto.TypeInfo(bool),
            ),
        ]

    # True if AddCommunicationToCase succeeds. Otherwise, returns an error.
    result: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Attachment(autoboto.ShapeBase):
    """
    An attachment to a case communication. The attachment consists of the file name
    and the content of the file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_name",
                "fileName",
                autoboto.TypeInfo(str),
            ),
            (
                "data",
                "data",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # The name of the attachment file.
    file_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The content of the attachment file.
    data: typing.Any = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachmentDetails(autoboto.ShapeBase):
    """
    The file name and ID of an attachment to a case communication. You can use the
    ID to retrieve the attachment with the DescribeAttachment operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attachment_id",
                "attachmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "file_name",
                "fileName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the attachment.
    attachment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The file name of the attachment.
    file_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachmentIdNotFound(autoboto.ShapeBase):
    """
    An attachment with the specified ID could not be found.
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

    # An attachment with the specified ID could not be found.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachmentLimitExceeded(autoboto.ShapeBase):
    """
    The limit for the number of attachment sets created in a short period of time
    has been exceeded.
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

    # The limit for the number of attachment sets created in a short period of
    # time has been exceeded.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachmentSetExpired(autoboto.ShapeBase):
    """
    The expiration time of the attachment set has passed. The set expires 1 hour
    after it is created.
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

    # The expiration time of the attachment set has passed. The set expires 1
    # hour after it is created.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachmentSetIdNotFound(autoboto.ShapeBase):
    """
    An attachment set with the specified ID could not be found.
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

    # An attachment set with the specified ID could not be found.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachmentSetSizeLimitExceeded(autoboto.ShapeBase):
    """
    A limit for the size of an attachment set has been exceeded. The limits are 3
    attachments and 5 MB per attachment.
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

    # A limit for the size of an attachment set has been exceeded. The limits are
    # 3 attachments and 5 MB per attachment.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CaseCreationLimitExceeded(autoboto.ShapeBase):
    """
    The case creation limit for the account has been exceeded.
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

    # An error message that indicates that you have exceeded the number of cases
    # you can have open.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CaseDetails(autoboto.ShapeBase):
    """
    A JSON-formatted object that contains the metadata for a support case. It is
    contained the response from a DescribeCases request. **CaseDetails** contains
    the following fields:

      * **caseId.** The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case- _12345678910-2013-c4c1d2bf33c5cf47_.

      * **categoryCode.** The category of problem for the AWS Support case. Corresponds to the CategoryCode values returned by a call to DescribeServices.

      * **displayId.** The identifier for the case on pages in the AWS Support Center.

      * **language.** The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ("en") and Japanese ("ja"). Language parameters must be passed explicitly for operations that take them.

      * **recentCommunications.** One or more Communication objects. Fields of these objects are `attachments`, `body`, `caseId`, `submittedBy`, and `timeCreated`.

      * **nextToken.** A resumption point for pagination.

      * **serviceCode.** The identifier for the AWS service that corresponds to the service code defined in the call to DescribeServices.

      * **severityCode.** The severity code assigned to the case. Contains one of the values returned by the call to DescribeSeverityLevels.

      * **status.** The status of the case in the AWS Support Center.

      * **subject.** The subject line of the case.

      * **submittedBy.** The email address of the account that submitted the case.

      * **timeCreated.** The time the case was created, in ISO-8601 format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "case_id",
                "caseId",
                autoboto.TypeInfo(str),
            ),
            (
                "display_id",
                "displayId",
                autoboto.TypeInfo(str),
            ),
            (
                "subject",
                "subject",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(str),
            ),
            (
                "service_code",
                "serviceCode",
                autoboto.TypeInfo(str),
            ),
            (
                "category_code",
                "categoryCode",
                autoboto.TypeInfo(str),
            ),
            (
                "severity_code",
                "severityCode",
                autoboto.TypeInfo(str),
            ),
            (
                "submitted_by",
                "submittedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "time_created",
                "timeCreated",
                autoboto.TypeInfo(str),
            ),
            (
                "recent_communications",
                "recentCommunications",
                autoboto.TypeInfo(RecentCaseCommunications),
            ),
            (
                "cc_email_addresses",
                "ccEmailAddresses",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "language",
                "language",
                autoboto.TypeInfo(str),
            ),
        ]

    # The AWS Support case ID requested or returned in the call. The case ID is
    # an alphanumeric string formatted as shown in this example: case-
    # _12345678910-2013-c4c1d2bf33c5cf47_
    case_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID displayed for the case in the AWS Support Center. This is a numeric
    # string.
    display_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The subject line for the case in the AWS Support Center.
    subject: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the case.
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The code for the AWS service returned by the call to DescribeServices.
    service_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The category of problem for the AWS Support case.
    category_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The code for the severity level returned by the call to
    # DescribeSeverityLevels.
    severity_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The email address of the account that submitted the case.
    submitted_by: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time that the case was case created in the AWS Support Center.
    time_created: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The five most recent communications between you and AWS Support Center,
    # including the IDs of any attachments to the communications. Also includes a
    # `nextToken` that you can use to retrieve earlier communications.
    recent_communications: "RecentCaseCommunications" = dataclasses.field(
        default_factory=dict,
    )

    # The email addresses that receive copies of communication about the case.
    cc_email_addresses: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The ISO 639-1 code for the language in which AWS provides support. AWS
    # Support currently supports English ("en") and Japanese ("ja"). Language
    # parameters must be passed explicitly for operations that take them.
    language: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CaseIdNotFound(autoboto.ShapeBase):
    """
    The requested `caseId` could not be located.
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

    # The requested `CaseId` could not be located.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Category(autoboto.ShapeBase):
    """
    A JSON-formatted name/value pair that represents the category name and category
    code of the problem, selected from the DescribeServices response for each AWS
    service.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The category code for the support case.
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The category name for the support case.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Communication(autoboto.ShapeBase):
    """
    A communication associated with an AWS Support case. The communication consists
    of the case ID, the message body, attachment information, the account email
    address, and the date and time of the communication.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "case_id",
                "caseId",
                autoboto.TypeInfo(str),
            ),
            (
                "body",
                "body",
                autoboto.TypeInfo(str),
            ),
            (
                "submitted_by",
                "submittedBy",
                autoboto.TypeInfo(str),
            ),
            (
                "time_created",
                "timeCreated",
                autoboto.TypeInfo(str),
            ),
            (
                "attachment_set",
                "attachmentSet",
                autoboto.TypeInfo(typing.List[AttachmentDetails]),
            ),
        ]

    # The AWS Support case ID requested or returned in the call. The case ID is
    # an alphanumeric string formatted as shown in this example: case-
    # _12345678910-2013-c4c1d2bf33c5cf47_
    case_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The text of the communication between the customer and AWS Support.
    body: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The email address of the account that submitted the AWS Support case.
    submitted_by: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time the communication was created.
    time_created: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Information about the attachments to the case communication.
    attachment_set: typing.List["AttachmentDetails"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateCaseRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subject",
                "subject",
                autoboto.TypeInfo(str),
            ),
            (
                "communication_body",
                "communicationBody",
                autoboto.TypeInfo(str),
            ),
            (
                "service_code",
                "serviceCode",
                autoboto.TypeInfo(str),
            ),
            (
                "severity_code",
                "severityCode",
                autoboto.TypeInfo(str),
            ),
            (
                "category_code",
                "categoryCode",
                autoboto.TypeInfo(str),
            ),
            (
                "cc_email_addresses",
                "ccEmailAddresses",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "language",
                "language",
                autoboto.TypeInfo(str),
            ),
            (
                "issue_type",
                "issueType",
                autoboto.TypeInfo(str),
            ),
            (
                "attachment_set_id",
                "attachmentSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The title of the AWS Support case.
    subject: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The communication body text when you create an AWS Support case by calling
    # CreateCase.
    communication_body: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The code for the AWS service returned by the call to DescribeServices.
    service_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The code for the severity level returned by the call to
    # DescribeSeverityLevels.

    # The availability of severity levels depends on each customer's support
    # subscription. In other words, your subscription may not necessarily require
    # the urgent level of response time.
    severity_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The category of problem for the AWS Support case.
    category_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of email addresses that AWS Support copies on case correspondence.
    cc_email_addresses: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The ISO 639-1 code for the language in which AWS provides support. AWS
    # Support currently supports English ("en") and Japanese ("ja"). Language
    # parameters must be passed explicitly for operations that take them.
    language: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of issue for the case. You can specify either "customer-service"
    # or "technical." If you do not indicate a value, the default is "technical."
    issue_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of a set of one or more attachments for the case. Create the set by
    # using AddAttachmentsToSet.
    attachment_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateCaseResponse(autoboto.ShapeBase):
    """
    The AWS Support case ID returned by a successful completion of the CreateCase
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "case_id",
                "caseId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The AWS Support case ID requested or returned in the call. The case ID is
    # an alphanumeric string formatted as shown in this example: case-
    # _12345678910-2013-c4c1d2bf33c5cf47_
    case_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class Data(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class DescribeAttachmentLimitExceeded(autoboto.ShapeBase):
    """
    The limit for the number of DescribeAttachment requests in a short period of
    time has been exceeded.
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

    # The limit for the number of DescribeAttachment requests in a short period
    # of time has been exceeded.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAttachmentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attachment_id",
                "attachmentId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the attachment to return. Attachment IDs are returned by the
    # DescribeCommunications operation.
    attachment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAttachmentResponse(autoboto.ShapeBase):
    """
    The content and file name of the attachment returned by the DescribeAttachment
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attachment",
                "attachment",
                autoboto.TypeInfo(Attachment),
            ),
        ]

    # The attachment content and file name.
    attachment: "Attachment" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeCasesRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "case_id_list",
                "caseIdList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "display_id",
                "displayId",
                autoboto.TypeInfo(str),
            ),
            (
                "after_time",
                "afterTime",
                autoboto.TypeInfo(str),
            ),
            (
                "before_time",
                "beforeTime",
                autoboto.TypeInfo(str),
            ),
            (
                "include_resolved_cases",
                "includeResolvedCases",
                autoboto.TypeInfo(bool),
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
            (
                "language",
                "language",
                autoboto.TypeInfo(str),
            ),
            (
                "include_communications",
                "includeCommunications",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A list of ID numbers of the support cases you want returned. The maximum
    # number of cases is 100.
    case_id_list: typing.List[str] = dataclasses.field(default_factory=list, )

    # The ID displayed for a case in the AWS Support Center user interface.
    display_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The start date for a filtered date search on support case communications.
    # Case communications are available for 12 months after creation.
    after_time: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The end date for a filtered date search on support case communications.
    # Case communications are available for 12 months after creation.
    before_time: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies whether resolved support cases should be included in the
    # DescribeCases results. The default is _false_.
    include_resolved_cases: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A resumption point for pagination.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to return before paginating.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ISO 639-1 code for the language in which AWS provides support. AWS
    # Support currently supports English ("en") and Japanese ("ja"). Language
    # parameters must be passed explicitly for operations that take them.
    language: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies whether communications should be included in the DescribeCases
    # results. The default is _true_.
    include_communications: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeCasesResponse(autoboto.ShapeBase):
    """
    Returns an array of CaseDetails objects and a `nextToken` that defines a point
    for pagination in the result set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cases",
                "cases",
                autoboto.TypeInfo(typing.List[CaseDetails]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The details for the cases that match the request.
    cases: typing.List["CaseDetails"] = dataclasses.field(
        default_factory=list,
    )

    # A resumption point for pagination.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCommunicationsRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "case_id",
                "caseId",
                autoboto.TypeInfo(str),
            ),
            (
                "before_time",
                "beforeTime",
                autoboto.TypeInfo(str),
            ),
            (
                "after_time",
                "afterTime",
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

    # The AWS Support case ID requested or returned in the call. The case ID is
    # an alphanumeric string formatted as shown in this example: case-
    # _12345678910-2013-c4c1d2bf33c5cf47_
    case_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The end date for a filtered date search on support case communications.
    # Case communications are available for 12 months after creation.
    before_time: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The start date for a filtered date search on support case communications.
    # Case communications are available for 12 months after creation.
    after_time: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A resumption point for pagination.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to return before paginating.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCommunicationsResponse(autoboto.ShapeBase):
    """
    The communications returned by the DescribeCommunications operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "communications",
                "communications",
                autoboto.TypeInfo(typing.List[Communication]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The communications for the case.
    communications: typing.List["Communication"] = dataclasses.field(
        default_factory=list,
    )

    # A resumption point for pagination.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeServicesRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_code_list",
                "serviceCodeList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "language",
                "language",
                autoboto.TypeInfo(str),
            ),
        ]

    # A JSON-formatted list of service codes available for AWS services.
    service_code_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The ISO 639-1 code for the language in which AWS provides support. AWS
    # Support currently supports English ("en") and Japanese ("ja"). Language
    # parameters must be passed explicitly for operations that take them.
    language: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeServicesResponse(autoboto.ShapeBase):
    """
    The list of AWS services returned by the DescribeServices operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "services",
                "services",
                autoboto.TypeInfo(typing.List[Service]),
            ),
        ]

    # A JSON-formatted list of AWS services.
    services: typing.List["Service"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeSeverityLevelsRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "language",
                "language",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ISO 639-1 code for the language in which AWS provides support. AWS
    # Support currently supports English ("en") and Japanese ("ja"). Language
    # parameters must be passed explicitly for operations that take them.
    language: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSeverityLevelsResponse(autoboto.ShapeBase):
    """
    The list of severity levels returned by the DescribeSeverityLevels operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "severity_levels",
                "severityLevels",
                autoboto.TypeInfo(typing.List[SeverityLevel]),
            ),
        ]

    # The available severity levels for the support case. Available severity
    # levels are defined by your service level agreement with AWS.
    severity_levels: typing.List["SeverityLevel"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeTrustedAdvisorCheckRefreshStatusesRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "check_ids",
                "checkIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The IDs of the Trusted Advisor checks to get the status of. **Note:**
    # Specifying the check ID of a check that is automatically refreshed causes
    # an `InvalidParameterValue` error.
    check_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeTrustedAdvisorCheckRefreshStatusesResponse(autoboto.ShapeBase):
    """
    The statuses of the Trusted Advisor checks returned by the
    DescribeTrustedAdvisorCheckRefreshStatuses operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "statuses",
                "statuses",
                autoboto.TypeInfo(
                    typing.List[TrustedAdvisorCheckRefreshStatus]
                ),
            ),
        ]

    # The refresh status of the specified Trusted Advisor checks.
    statuses: typing.List["TrustedAdvisorCheckRefreshStatus"
                         ] = dataclasses.field(
                             default_factory=list,
                         )


@dataclasses.dataclass
class DescribeTrustedAdvisorCheckResultRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "check_id",
                "checkId",
                autoboto.TypeInfo(str),
            ),
            (
                "language",
                "language",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier for the Trusted Advisor check.
    check_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ISO 639-1 code for the language in which AWS provides support. AWS
    # Support currently supports English ("en") and Japanese ("ja"). Language
    # parameters must be passed explicitly for operations that take them.
    language: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTrustedAdvisorCheckResultResponse(autoboto.ShapeBase):
    """
    The result of the Trusted Advisor check returned by the
    DescribeTrustedAdvisorCheckResult operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "result",
                "result",
                autoboto.TypeInfo(TrustedAdvisorCheckResult),
            ),
        ]

    # The detailed results of the Trusted Advisor check.
    result: "TrustedAdvisorCheckResult" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeTrustedAdvisorCheckSummariesRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "check_ids",
                "checkIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The IDs of the Trusted Advisor checks.
    check_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeTrustedAdvisorCheckSummariesResponse(autoboto.ShapeBase):
    """
    The summaries of the Trusted Advisor checks returned by the
    DescribeTrustedAdvisorCheckSummaries operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "summaries",
                "summaries",
                autoboto.TypeInfo(typing.List[TrustedAdvisorCheckSummary]),
            ),
        ]

    # The summary information for the requested Trusted Advisor checks.
    summaries: typing.List["TrustedAdvisorCheckSummary"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeTrustedAdvisorChecksRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "language",
                "language",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ISO 639-1 code for the language in which AWS provides support. AWS
    # Support currently supports English ("en") and Japanese ("ja"). Language
    # parameters must be passed explicitly for operations that take them.
    language: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTrustedAdvisorChecksResponse(autoboto.ShapeBase):
    """
    Information about the Trusted Advisor checks returned by the
    DescribeTrustedAdvisorChecks operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "checks",
                "checks",
                autoboto.TypeInfo(typing.List[TrustedAdvisorCheckDescription]),
            ),
        ]

    # Information about all available Trusted Advisor checks.
    checks: typing.List["TrustedAdvisorCheckDescription"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class InternalServerError(autoboto.ShapeBase):
    """
    An internal server error occurred.
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

    # An internal server error occurred.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RecentCaseCommunications(autoboto.ShapeBase):
    """
    The five most recent communications associated with the case.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "communications",
                "communications",
                autoboto.TypeInfo(typing.List[Communication]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The five most recent communications associated with the case.
    communications: typing.List["Communication"] = dataclasses.field(
        default_factory=list,
    )

    # A resumption point for pagination.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RefreshTrustedAdvisorCheckRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "check_id",
                "checkId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier for the Trusted Advisor check to refresh. **Note:**
    # Specifying the check ID of a check that is automatically refreshed causes
    # an `InvalidParameterValue` error.
    check_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RefreshTrustedAdvisorCheckResponse(autoboto.ShapeBase):
    """
    The current refresh status of a Trusted Advisor check.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "status",
                autoboto.TypeInfo(TrustedAdvisorCheckRefreshStatus),
            ),
        ]

    # The current refresh status for a check, including the amount of time until
    # the check is eligible for refresh.
    status: "TrustedAdvisorCheckRefreshStatus" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ResolveCaseRequest(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "case_id",
                "caseId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The AWS Support case ID requested or returned in the call. The case ID is
    # an alphanumeric string formatted as shown in this example: case-
    # _12345678910-2013-c4c1d2bf33c5cf47_
    case_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResolveCaseResponse(autoboto.ShapeBase):
    """
    The status of the case returned by the ResolveCase operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "initial_case_status",
                "initialCaseStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "final_case_status",
                "finalCaseStatus",
                autoboto.TypeInfo(str),
            ),
        ]

    # The status of the case when the ResolveCase request was sent.
    initial_case_status: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the case after the ResolveCase request was processed.
    final_case_status: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Service(autoboto.ShapeBase):
    """
    Information about an AWS service returned by the DescribeServices operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "categories",
                "categories",
                autoboto.TypeInfo(typing.List[Category]),
            ),
        ]

    # The code for an AWS service returned by the DescribeServices response. The
    # `name` element contains the corresponding friendly name.
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The friendly name for an AWS service. The `code` element contains the
    # corresponding code.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of categories that describe the type of support issue a case
    # describes. Categories consist of a category name and a category code.
    # Category names and codes are passed to AWS Support when you call
    # CreateCase.
    categories: typing.List["Category"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class SeverityLevel(autoboto.ShapeBase):
    """
    A code and name pair that represent a severity level that can be applied to a
    support case.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
        ]

    # One of four values: "low," "medium," "high," and "urgent". These values
    # correspond to response times returned to the caller in
    # `severityLevel.name`.
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the severity level that corresponds to the severity level code.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TrustedAdvisorCategorySpecificSummary(autoboto.ShapeBase):
    """
    The container for summary information that relates to the category of the
    Trusted Advisor check.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cost_optimizing",
                "costOptimizing",
                autoboto.TypeInfo(TrustedAdvisorCostOptimizingSummary),
            ),
        ]

    # The summary information about cost savings for a Trusted Advisor check that
    # is in the Cost Optimizing category.
    cost_optimizing: "TrustedAdvisorCostOptimizingSummary" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class TrustedAdvisorCheckDescription(autoboto.ShapeBase):
    """
    The description and metadata for a Trusted Advisor check.
    """

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
            (
                "category",
                "category",
                autoboto.TypeInfo(str),
            ),
            (
                "metadata",
                "metadata",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The unique identifier for the Trusted Advisor check.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The display name for the Trusted Advisor check.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The description of the Trusted Advisor check, which includes the alert
    # criteria and recommended actions (contains HTML markup).
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The category of the Trusted Advisor check.
    category: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The column headings for the data returned by the Trusted Advisor check. The
    # order of the headings corresponds to the order of the data in the
    # **Metadata** element of the TrustedAdvisorResourceDetail for the check.
    # **Metadata** contains all the data that is shown in the Excel download,
    # even in those cases where the UI shows just summary data.
    metadata: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class TrustedAdvisorCheckRefreshStatus(autoboto.ShapeBase):
    """
    The refresh status of a Trusted Advisor check.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "check_id",
                "checkId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(str),
            ),
            (
                "millis_until_next_refreshable",
                "millisUntilNextRefreshable",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique identifier for the Trusted Advisor check.
    check_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the Trusted Advisor check for which a refresh has been
    # requested: "none", "enqueued", "processing", "success", or "abandoned".
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The amount of time, in milliseconds, until the Trusted Advisor check is
    # eligible for refresh.
    millis_until_next_refreshable: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TrustedAdvisorCheckResult(autoboto.ShapeBase):
    """
    The results of a Trusted Advisor check returned by
    DescribeTrustedAdvisorCheckResult.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "check_id",
                "checkId",
                autoboto.TypeInfo(str),
            ),
            (
                "timestamp",
                "timestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(str),
            ),
            (
                "resources_summary",
                "resourcesSummary",
                autoboto.TypeInfo(TrustedAdvisorResourcesSummary),
            ),
            (
                "category_specific_summary",
                "categorySpecificSummary",
                autoboto.TypeInfo(TrustedAdvisorCategorySpecificSummary),
            ),
            (
                "flagged_resources",
                "flaggedResources",
                autoboto.TypeInfo(typing.List[TrustedAdvisorResourceDetail]),
            ),
        ]

    # The unique identifier for the Trusted Advisor check.
    check_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time of the last refresh of the check.
    timestamp: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The alert status of the check: "ok" (green), "warning" (yellow), "error"
    # (red), or "not_available".
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Details about AWS resources that were analyzed in a call to Trusted Advisor
    # DescribeTrustedAdvisorCheckSummaries.
    resources_summary: "TrustedAdvisorResourcesSummary" = dataclasses.field(
        default_factory=dict,
    )

    # Summary information that relates to the category of the check. Cost
    # Optimizing is the only category that is currently supported.
    category_specific_summary: "TrustedAdvisorCategorySpecificSummary" = dataclasses.field(
        default_factory=dict,
    )

    # The details about each resource listed in the check result.
    flagged_resources: typing.List["TrustedAdvisorResourceDetail"
                                  ] = dataclasses.field(
                                      default_factory=list,
                                  )


@dataclasses.dataclass
class TrustedAdvisorCheckSummary(autoboto.ShapeBase):
    """
    A summary of a Trusted Advisor check result, including the alert status, last
    refresh, and number of resources examined.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "check_id",
                "checkId",
                autoboto.TypeInfo(str),
            ),
            (
                "timestamp",
                "timestamp",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(str),
            ),
            (
                "resources_summary",
                "resourcesSummary",
                autoboto.TypeInfo(TrustedAdvisorResourcesSummary),
            ),
            (
                "category_specific_summary",
                "categorySpecificSummary",
                autoboto.TypeInfo(TrustedAdvisorCategorySpecificSummary),
            ),
            (
                "has_flagged_resources",
                "hasFlaggedResources",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The unique identifier for the Trusted Advisor check.
    check_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time of the last refresh of the check.
    timestamp: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The alert status of the check: "ok" (green), "warning" (yellow), "error"
    # (red), or "not_available".
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Details about AWS resources that were analyzed in a call to Trusted Advisor
    # DescribeTrustedAdvisorCheckSummaries.
    resources_summary: "TrustedAdvisorResourcesSummary" = dataclasses.field(
        default_factory=dict,
    )

    # Summary information that relates to the category of the check. Cost
    # Optimizing is the only category that is currently supported.
    category_specific_summary: "TrustedAdvisorCategorySpecificSummary" = dataclasses.field(
        default_factory=dict,
    )

    # Specifies whether the Trusted Advisor check has flagged resources.
    has_flagged_resources: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TrustedAdvisorCostOptimizingSummary(autoboto.ShapeBase):
    """
    The estimated cost savings that might be realized if the recommended actions are
    taken.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "estimated_monthly_savings",
                "estimatedMonthlySavings",
                autoboto.TypeInfo(float),
            ),
            (
                "estimated_percent_monthly_savings",
                "estimatedPercentMonthlySavings",
                autoboto.TypeInfo(float),
            ),
        ]

    # The estimated monthly savings that might be realized if the recommended
    # actions are taken.
    estimated_monthly_savings: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The estimated percentage of savings that might be realized if the
    # recommended actions are taken.
    estimated_percent_monthly_savings: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TrustedAdvisorResourceDetail(autoboto.ShapeBase):
    """
    Contains information about a resource identified by a Trusted Advisor check.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "status",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "metadata",
                "metadata",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "region",
                "region",
                autoboto.TypeInfo(str),
            ),
            (
                "is_suppressed",
                "isSuppressed",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The status code for the resource identified in the Trusted Advisor check.
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The unique identifier for the identified resource.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Additional information about the identified resource. The exact metadata
    # and its order can be obtained by inspecting the
    # TrustedAdvisorCheckDescription object returned by the call to
    # DescribeTrustedAdvisorChecks. **Metadata** contains all the data that is
    # shown in the Excel download, even in those cases where the UI shows just
    # summary data.
    metadata: typing.List[str] = dataclasses.field(default_factory=list, )

    # The AWS region in which the identified resource is located.
    region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies whether the AWS resource was ignored by Trusted Advisor because
    # it was marked as suppressed by the user.
    is_suppressed: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TrustedAdvisorResourcesSummary(autoboto.ShapeBase):
    """
    Details about AWS resources that were analyzed in a call to Trusted Advisor
    DescribeTrustedAdvisorCheckSummaries.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resources_processed",
                "resourcesProcessed",
                autoboto.TypeInfo(int),
            ),
            (
                "resources_flagged",
                "resourcesFlagged",
                autoboto.TypeInfo(int),
            ),
            (
                "resources_ignored",
                "resourcesIgnored",
                autoboto.TypeInfo(int),
            ),
            (
                "resources_suppressed",
                "resourcesSuppressed",
                autoboto.TypeInfo(int),
            ),
        ]

    # The number of AWS resources that were analyzed by the Trusted Advisor
    # check.
    resources_processed: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of AWS resources that were flagged (listed) by the Trusted
    # Advisor check.
    resources_flagged: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of AWS resources ignored by Trusted Advisor because information
    # was unavailable.
    resources_ignored: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of AWS resources ignored by Trusted Advisor because they were
    # marked as suppressed by the user.
    resources_suppressed: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
