import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AcceptQualificationRequestRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "qualification_request_id",
                "QualificationRequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "integer_value",
                "IntegerValue",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the Qualification request, as returned by the
    # `GetQualificationRequests` operation.
    qualification_request_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The value of the Qualification. You can omit this value if you are using
    # the presence or absence of the Qualification as the basis for a HIT
    # requirement.
    integer_value: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AcceptQualificationRequestResponse(autoboto.OutputShapeBase):
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
class ApproveAssignmentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assignment_id",
                "AssignmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "requester_feedback",
                "RequesterFeedback",
                autoboto.TypeInfo(str),
            ),
            (
                "override_rejection",
                "OverrideRejection",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the assignment. The assignment must correspond to a HIT created
    # by the Requester.
    assignment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A message for the Worker, which the Worker can see in the Status section of
    # the web site.
    requester_feedback: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A flag indicating that an assignment should be approved even if it was
    # previously rejected. Defaults to `False`.
    override_rejection: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ApproveAssignmentResponse(autoboto.OutputShapeBase):
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
class Assignment(autoboto.ShapeBase):
    """
    The Assignment data structure represents a single assignment of a HIT to a
    Worker. The assignment tracks the Worker's efforts to complete the HIT, and
    contains the results for later retrieval.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assignment_id",
                "AssignmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "worker_id",
                "WorkerId",
                autoboto.TypeInfo(str),
            ),
            (
                "hit_id",
                "HITId",
                autoboto.TypeInfo(str),
            ),
            (
                "assignment_status",
                "AssignmentStatus",
                autoboto.TypeInfo(AssignmentStatus),
            ),
            (
                "auto_approval_time",
                "AutoApprovalTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "accept_time",
                "AcceptTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "submit_time",
                "SubmitTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "approval_time",
                "ApprovalTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "rejection_time",
                "RejectionTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "deadline",
                "Deadline",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "answer",
                "Answer",
                autoboto.TypeInfo(str),
            ),
            (
                "requester_feedback",
                "RequesterFeedback",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier for the assignment.
    assignment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the Worker who accepted the HIT.
    worker_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the HIT.
    hit_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the assignment.
    assignment_status: "AssignmentStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If results have been submitted, AutoApprovalTime is the date and time the
    # results of the assignment results are considered Approved automatically if
    # they have not already been explicitly approved or rejected by the
    # Requester. This value is derived from the auto-approval delay specified by
    # the Requester in the HIT. This value is omitted from the assignment if the
    # Worker has not yet submitted results.
    auto_approval_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time the Worker accepted the assignment.
    accept_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the Worker has submitted results, SubmitTime is the date and time the
    # assignment was submitted. This value is omitted from the assignment if the
    # Worker has not yet submitted results.
    submit_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the Worker has submitted results and the Requester has approved the
    # results, ApprovalTime is the date and time the Requester approved the
    # results. This value is omitted from the assignment if the Requester has not
    # yet approved the results.
    approval_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the Worker has submitted results and the Requester has rejected the
    # results, RejectionTime is the date and time the Requester rejected the
    # results.
    rejection_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time of the deadline for the assignment. This value is derived
    # from the deadline specification for the HIT and the date and time the
    # Worker accepted the HIT.
    deadline: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Worker's answers submitted for the HIT contained in a
    # QuestionFormAnswers document, if the Worker provides an answer. If the
    # Worker does not provide any answers, Answer may contain a
    # QuestionFormAnswers document, or Answer may be empty.
    answer: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The feedback string included with the call to the ApproveAssignment
    # operation or the RejectAssignment operation, if the Requester approved or
    # rejected the assignment and specified feedback.
    requester_feedback: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class AssignmentStatus(Enum):
    Submitted = "Submitted"
    Approved = "Approved"
    Rejected = "Rejected"


@dataclasses.dataclass
class AssociateQualificationWithWorkerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "qualification_type_id",
                "QualificationTypeId",
                autoboto.TypeInfo(str),
            ),
            (
                "worker_id",
                "WorkerId",
                autoboto.TypeInfo(str),
            ),
            (
                "integer_value",
                "IntegerValue",
                autoboto.TypeInfo(int),
            ),
            (
                "send_notification",
                "SendNotification",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the Qualification type to use for the assigned Qualification.
    qualification_type_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the Worker to whom the Qualification is being assigned. Worker
    # IDs are included with submitted HIT assignments and Qualification requests.
    worker_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value of the Qualification to assign.
    integer_value: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies whether to send a notification email message to the Worker saying
    # that the qualification was assigned to the Worker. Note: this is true by
    # default.
    send_notification: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociateQualificationWithWorkerResponse(autoboto.OutputShapeBase):
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
class BonusPayment(autoboto.ShapeBase):
    """
    An object representing a Bonus payment paid to a Worker.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "worker_id",
                "WorkerId",
                autoboto.TypeInfo(str),
            ),
            (
                "bonus_amount",
                "BonusAmount",
                autoboto.TypeInfo(str),
            ),
            (
                "assignment_id",
                "AssignmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "reason",
                "Reason",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_time",
                "GrantTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ID of the Worker to whom the bonus was paid.
    worker_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A string representing a currency amount.
    bonus_amount: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the assignment associated with this bonus payment.
    assignment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Reason text given when the bonus was granted, if any.
    reason: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date and time of when the bonus was granted.
    grant_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class Comparator(Enum):
    LessThan = "LessThan"
    LessThanOrEqualTo = "LessThanOrEqualTo"
    GreaterThan = "GreaterThan"
    GreaterThanOrEqualTo = "GreaterThanOrEqualTo"
    EqualTo = "EqualTo"
    NotEqualTo = "NotEqualTo"
    Exists = "Exists"
    DoesNotExist = "DoesNotExist"
    In = "In"
    NotIn = "NotIn"


@dataclasses.dataclass
class CreateAdditionalAssignmentsForHITRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hit_id",
                "HITId",
                autoboto.TypeInfo(str),
            ),
            (
                "number_of_additional_assignments",
                "NumberOfAdditionalAssignments",
                autoboto.TypeInfo(int),
            ),
            (
                "unique_request_token",
                "UniqueRequestToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the HIT to extend.
    hit_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of additional assignments to request for this HIT.
    number_of_additional_assignments: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A unique identifier for this request, which allows you to retry the call on
    # error without extending the HIT multiple times. This is useful in cases
    # such as network timeouts where it is unclear whether or not the call
    # succeeded on the server. If the extend HIT already exists in the system
    # from a previous call using the same `UniqueRequestToken`, subsequent calls
    # will return an error with a message containing the request ID.
    unique_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateAdditionalAssignmentsForHITResponse(autoboto.OutputShapeBase):
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
class CreateHITRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lifetime_in_seconds",
                "LifetimeInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "assignment_duration_in_seconds",
                "AssignmentDurationInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "reward",
                "Reward",
                autoboto.TypeInfo(str),
            ),
            (
                "title",
                "Title",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "max_assignments",
                "MaxAssignments",
                autoboto.TypeInfo(int),
            ),
            (
                "auto_approval_delay_in_seconds",
                "AutoApprovalDelayInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "keywords",
                "Keywords",
                autoboto.TypeInfo(str),
            ),
            (
                "question",
                "Question",
                autoboto.TypeInfo(str),
            ),
            (
                "requester_annotation",
                "RequesterAnnotation",
                autoboto.TypeInfo(str),
            ),
            (
                "qualification_requirements",
                "QualificationRequirements",
                autoboto.TypeInfo(typing.List[QualificationRequirement]),
            ),
            (
                "unique_request_token",
                "UniqueRequestToken",
                autoboto.TypeInfo(str),
            ),
            (
                "assignment_review_policy",
                "AssignmentReviewPolicy",
                autoboto.TypeInfo(ReviewPolicy),
            ),
            (
                "hit_review_policy",
                "HITReviewPolicy",
                autoboto.TypeInfo(ReviewPolicy),
            ),
            (
                "hit_layout_id",
                "HITLayoutId",
                autoboto.TypeInfo(str),
            ),
            (
                "hit_layout_parameters",
                "HITLayoutParameters",
                autoboto.TypeInfo(typing.List[HITLayoutParameter]),
            ),
        ]

    # An amount of time, in seconds, after which the HIT is no longer available
    # for users to accept. After the lifetime of the HIT elapses, the HIT no
    # longer appears in HIT searches, even if not all of the assignments for the
    # HIT have been accepted.
    lifetime_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The amount of time, in seconds, that a Worker has to complete the HIT after
    # accepting it. If a Worker does not complete the assignment within the
    # specified duration, the assignment is considered abandoned. If the HIT is
    # still active (that is, its lifetime has not elapsed), the assignment
    # becomes available for other users to find and accept.
    assignment_duration_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The amount of money the Requester will pay a Worker for successfully
    # completing the HIT.
    reward: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The title of the HIT. A title should be short and descriptive about the
    # kind of task the HIT contains. On the Amazon Mechanical Turk web site, the
    # HIT title appears in search results, and everywhere the HIT is mentioned.
    title: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A general description of the HIT. A description includes detailed
    # information about the kind of task the HIT contains. On the Amazon
    # Mechanical Turk web site, the HIT description appears in the expanded view
    # of search results, and in the HIT and assignment screens. A good
    # description gives the user enough information to evaluate the HIT before
    # accepting it.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of times the HIT can be accepted and completed before the HIT
    # becomes unavailable.
    max_assignments: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of seconds after an assignment for the HIT has been submitted,
    # after which the assignment is considered Approved automatically unless the
    # Requester explicitly rejects it.
    auto_approval_delay_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # One or more words or phrases that describe the HIT, separated by commas.
    # These words are used in searches to find HITs.
    keywords: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The data the person completing the HIT uses to produce the results.

    # Constraints: Must be a QuestionForm data structure, an ExternalQuestion
    # data structure, or an HTMLQuestion data structure. The XML question data
    # must not be larger than 64 kilobytes (65,535 bytes) in size, including
    # whitespace.

    # Either a Question parameter or a HITLayoutId parameter must be provided.
    question: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An arbitrary data field. The RequesterAnnotation parameter lets your
    # application attach arbitrary data to the HIT for tracking purposes. For
    # example, this parameter could be an identifier internal to the Requester's
    # application that corresponds with the HIT.

    # The RequesterAnnotation parameter for a HIT is only visible to the
    # Requester who created the HIT. It is not shown to the Worker, or any other
    # Requester.

    # The RequesterAnnotation parameter may be different for each HIT you submit.
    # It does not affect how your HITs are grouped.
    requester_annotation: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Conditions that a Worker's Qualifications must meet in order to accept the
    # HIT. A HIT can have between zero and ten Qualification requirements. All
    # requirements must be met in order for a Worker to accept the HIT.
    # Additionally, other actions can be restricted using the `ActionsGuarded`
    # field on each `QualificationRequirement` structure.
    qualification_requirements: typing.List["QualificationRequirement"
                                           ] = dataclasses.field(
                                               default_factory=list,
                                           )

    # A unique identifier for this request which allows you to retry the call on
    # error without creating duplicate HITs. This is useful in cases such as
    # network timeouts where it is unclear whether or not the call succeeded on
    # the server. If the HIT already exists in the system from a previous call
    # using the same UniqueRequestToken, subsequent calls will return a
    # AWS.MechanicalTurk.HitAlreadyExists error with a message containing the
    # HITId.

    # Note: It is your responsibility to ensure uniqueness of the token. The
    # unique token expires after 24 hours. Subsequent calls using the same
    # UniqueRequestToken made after the 24 hour limit could create duplicate
    # HITs.
    unique_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Assignment-level Review Policy applies to the assignments under the
    # HIT. You can specify for Mechanical Turk to take various actions based on
    # the policy.
    assignment_review_policy: "ReviewPolicy" = dataclasses.field(
        default_factory=dict,
    )

    # The HIT-level Review Policy applies to the HIT. You can specify for
    # Mechanical Turk to take various actions based on the policy.
    hit_review_policy: "ReviewPolicy" = dataclasses.field(
        default_factory=dict,
    )

    # The HITLayoutId allows you to use a pre-existing HIT design with
    # placeholder values and create an additional HIT by providing those values
    # as HITLayoutParameters.

    # Constraints: Either a Question parameter or a HITLayoutId parameter must be
    # provided.
    hit_layout_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the HITLayoutId is provided, any placeholder values must be filled in
    # with values using the HITLayoutParameter structure. For more information,
    # see HITLayout.
    hit_layout_parameters: typing.List["HITLayoutParameter"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )


@dataclasses.dataclass
class CreateHITResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hit",
                "HIT",
                autoboto.TypeInfo(HIT),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains the newly created HIT data. For a description of the HIT data
    # structure as it appears in responses, see the HIT Data Structure
    # documentation.
    hit: "HIT" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateHITTypeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assignment_duration_in_seconds",
                "AssignmentDurationInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "reward",
                "Reward",
                autoboto.TypeInfo(str),
            ),
            (
                "title",
                "Title",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "auto_approval_delay_in_seconds",
                "AutoApprovalDelayInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "keywords",
                "Keywords",
                autoboto.TypeInfo(str),
            ),
            (
                "qualification_requirements",
                "QualificationRequirements",
                autoboto.TypeInfo(typing.List[QualificationRequirement]),
            ),
        ]

    # The amount of time, in seconds, that a Worker has to complete the HIT after
    # accepting it. If a Worker does not complete the assignment within the
    # specified duration, the assignment is considered abandoned. If the HIT is
    # still active (that is, its lifetime has not elapsed), the assignment
    # becomes available for other users to find and accept.
    assignment_duration_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The amount of money the Requester will pay a Worker for successfully
    # completing the HIT.
    reward: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The title of the HIT. A title should be short and descriptive about the
    # kind of task the HIT contains. On the Amazon Mechanical Turk web site, the
    # HIT title appears in search results, and everywhere the HIT is mentioned.
    title: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A general description of the HIT. A description includes detailed
    # information about the kind of task the HIT contains. On the Amazon
    # Mechanical Turk web site, the HIT description appears in the expanded view
    # of search results, and in the HIT and assignment screens. A good
    # description gives the user enough information to evaluate the HIT before
    # accepting it.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of seconds after an assignment for the HIT has been submitted,
    # after which the assignment is considered Approved automatically unless the
    # Requester explicitly rejects it.
    auto_approval_delay_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # One or more words or phrases that describe the HIT, separated by commas.
    # These words are used in searches to find HITs.
    keywords: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Conditions that a Worker's Qualifications must meet in order to accept the
    # HIT. A HIT can have between zero and ten Qualification requirements. All
    # requirements must be met in order for a Worker to accept the HIT.
    # Additionally, other actions can be restricted using the `ActionsGuarded`
    # field on each `QualificationRequirement` structure.
    qualification_requirements: typing.List["QualificationRequirement"
                                           ] = dataclasses.field(
                                               default_factory=list,
                                           )


@dataclasses.dataclass
class CreateHITTypeResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hit_type_id",
                "HITTypeId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the newly registered HIT type.
    hit_type_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateHITWithHITTypeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hit_type_id",
                "HITTypeId",
                autoboto.TypeInfo(str),
            ),
            (
                "lifetime_in_seconds",
                "LifetimeInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "max_assignments",
                "MaxAssignments",
                autoboto.TypeInfo(int),
            ),
            (
                "question",
                "Question",
                autoboto.TypeInfo(str),
            ),
            (
                "requester_annotation",
                "RequesterAnnotation",
                autoboto.TypeInfo(str),
            ),
            (
                "unique_request_token",
                "UniqueRequestToken",
                autoboto.TypeInfo(str),
            ),
            (
                "assignment_review_policy",
                "AssignmentReviewPolicy",
                autoboto.TypeInfo(ReviewPolicy),
            ),
            (
                "hit_review_policy",
                "HITReviewPolicy",
                autoboto.TypeInfo(ReviewPolicy),
            ),
            (
                "hit_layout_id",
                "HITLayoutId",
                autoboto.TypeInfo(str),
            ),
            (
                "hit_layout_parameters",
                "HITLayoutParameters",
                autoboto.TypeInfo(typing.List[HITLayoutParameter]),
            ),
        ]

    # The HIT type ID you want to create this HIT with.
    hit_type_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An amount of time, in seconds, after which the HIT is no longer available
    # for users to accept. After the lifetime of the HIT elapses, the HIT no
    # longer appears in HIT searches, even if not all of the assignments for the
    # HIT have been accepted.
    lifetime_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of times the HIT can be accepted and completed before the HIT
    # becomes unavailable.
    max_assignments: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The data the person completing the HIT uses to produce the results.

    # Constraints: Must be a QuestionForm data structure, an ExternalQuestion
    # data structure, or an HTMLQuestion data structure. The XML question data
    # must not be larger than 64 kilobytes (65,535 bytes) in size, including
    # whitespace.

    # Either a Question parameter or a HITLayoutId parameter must be provided.
    question: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An arbitrary data field. The RequesterAnnotation parameter lets your
    # application attach arbitrary data to the HIT for tracking purposes. For
    # example, this parameter could be an identifier internal to the Requester's
    # application that corresponds with the HIT.

    # The RequesterAnnotation parameter for a HIT is only visible to the
    # Requester who created the HIT. It is not shown to the Worker, or any other
    # Requester.

    # The RequesterAnnotation parameter may be different for each HIT you submit.
    # It does not affect how your HITs are grouped.
    requester_annotation: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A unique identifier for this request which allows you to retry the call on
    # error without creating duplicate HITs. This is useful in cases such as
    # network timeouts where it is unclear whether or not the call succeeded on
    # the server. If the HIT already exists in the system from a previous call
    # using the same UniqueRequestToken, subsequent calls will return a
    # AWS.MechanicalTurk.HitAlreadyExists error with a message containing the
    # HITId.

    # Note: It is your responsibility to ensure uniqueness of the token. The
    # unique token expires after 24 hours. Subsequent calls using the same
    # UniqueRequestToken made after the 24 hour limit could create duplicate
    # HITs.
    unique_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Assignment-level Review Policy applies to the assignments under the
    # HIT. You can specify for Mechanical Turk to take various actions based on
    # the policy.
    assignment_review_policy: "ReviewPolicy" = dataclasses.field(
        default_factory=dict,
    )

    # The HIT-level Review Policy applies to the HIT. You can specify for
    # Mechanical Turk to take various actions based on the policy.
    hit_review_policy: "ReviewPolicy" = dataclasses.field(
        default_factory=dict,
    )

    # The HITLayoutId allows you to use a pre-existing HIT design with
    # placeholder values and create an additional HIT by providing those values
    # as HITLayoutParameters.

    # Constraints: Either a Question parameter or a HITLayoutId parameter must be
    # provided.
    hit_layout_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the HITLayoutId is provided, any placeholder values must be filled in
    # with values using the HITLayoutParameter structure. For more information,
    # see HITLayout.
    hit_layout_parameters: typing.List["HITLayoutParameter"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )


@dataclasses.dataclass
class CreateHITWithHITTypeResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hit",
                "HIT",
                autoboto.TypeInfo(HIT),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains the newly created HIT data. For a description of the HIT data
    # structure as it appears in responses, see the HIT Data Structure
    # documentation.
    hit: "HIT" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateQualificationTypeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "qualification_type_status",
                "QualificationTypeStatus",
                autoboto.TypeInfo(QualificationTypeStatus),
            ),
            (
                "keywords",
                "Keywords",
                autoboto.TypeInfo(str),
            ),
            (
                "retry_delay_in_seconds",
                "RetryDelayInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "test",
                "Test",
                autoboto.TypeInfo(str),
            ),
            (
                "answer_key",
                "AnswerKey",
                autoboto.TypeInfo(str),
            ),
            (
                "test_duration_in_seconds",
                "TestDurationInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "auto_granted",
                "AutoGranted",
                autoboto.TypeInfo(bool),
            ),
            (
                "auto_granted_value",
                "AutoGrantedValue",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name you give to the Qualification type. The type name is used to
    # represent the Qualification to Workers, and to find the type using a
    # Qualification type search. It must be unique across all of your
    # Qualification types.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A long description for the Qualification type. On the Amazon Mechanical
    # Turk website, the long description is displayed when a Worker examines a
    # Qualification type.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The initial status of the Qualification type.

    # Constraints: Valid values are: Active | Inactive
    qualification_type_status: "QualificationTypeStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # One or more words or phrases that describe the Qualification type,
    # separated by commas. The keywords of a type make the type easier to find
    # during a search.
    keywords: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of seconds that a Worker must wait after requesting a
    # Qualification of the Qualification type before the worker can retry the
    # Qualification request.

    # Constraints: None. If not specified, retries are disabled and Workers can
    # request a Qualification of this type only once, even if the Worker has not
    # been granted the Qualification. It is not possible to disable retries for a
    # Qualification type after it has been created with retries enabled. If you
    # want to disable retries, you must delete existing retry-enabled
    # Qualification type and then create a new Qualification type with retries
    # disabled.
    retry_delay_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The questions for the Qualification test a Worker must answer correctly to
    # obtain a Qualification of this type. If this parameter is specified,
    # `TestDurationInSeconds` must also be specified.

    # Constraints: Must not be longer than 65535 bytes. Must be a QuestionForm
    # data structure. This parameter cannot be specified if AutoGranted is true.

    # Constraints: None. If not specified, the Worker may request the
    # Qualification without answering any questions.
    test: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The answers to the Qualification test specified in the Test parameter, in
    # the form of an AnswerKey data structure.

    # Constraints: Must not be longer than 65535 bytes.

    # Constraints: None. If not specified, you must process Qualification
    # requests manually.
    answer_key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of seconds the Worker has to complete the Qualification test,
    # starting from the time the Worker requests the Qualification.
    test_duration_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether requests for the Qualification type are granted
    # immediately, without prompting the Worker with a Qualification test.

    # Constraints: If the Test parameter is specified, this parameter cannot be
    # true.
    auto_granted: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Qualification value to use for automatically granted Qualifications.
    # This parameter is used only if the AutoGranted parameter is true.
    auto_granted_value: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateQualificationTypeResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "qualification_type",
                "QualificationType",
                autoboto.TypeInfo(QualificationType),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The created Qualification type, returned as a QualificationType data
    # structure.
    qualification_type: "QualificationType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateWorkerBlockRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "worker_id",
                "WorkerId",
                autoboto.TypeInfo(str),
            ),
            (
                "reason",
                "Reason",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Worker to block.
    worker_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A message explaining the reason for blocking the Worker. This parameter
    # enables you to keep track of your Workers. The Worker does not see this
    # message.
    reason: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateWorkerBlockResponse(autoboto.OutputShapeBase):
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
class DeleteHITRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hit_id",
                "HITId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the HIT to be deleted.
    hit_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteHITResponse(autoboto.OutputShapeBase):
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
class DeleteQualificationTypeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "qualification_type_id",
                "QualificationTypeId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the QualificationType to dispose.
    qualification_type_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteQualificationTypeResponse(autoboto.OutputShapeBase):
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
class DeleteWorkerBlockRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "worker_id",
                "WorkerId",
                autoboto.TypeInfo(str),
            ),
            (
                "reason",
                "Reason",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Worker to unblock.
    worker_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A message that explains the reason for unblocking the Worker. The Worker
    # does not see this message.
    reason: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteWorkerBlockResponse(autoboto.OutputShapeBase):
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
class DisassociateQualificationFromWorkerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "worker_id",
                "WorkerId",
                autoboto.TypeInfo(str),
            ),
            (
                "qualification_type_id",
                "QualificationTypeId",
                autoboto.TypeInfo(str),
            ),
            (
                "reason",
                "Reason",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Worker who possesses the Qualification to be revoked.
    worker_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the Qualification type of the Qualification to be revoked.
    qualification_type_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A text message that explains why the Qualification was revoked. The user
    # who had the Qualification sees this message.
    reason: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateQualificationFromWorkerResponse(autoboto.OutputShapeBase):
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


class EventType(Enum):
    AssignmentAccepted = "AssignmentAccepted"
    AssignmentAbandoned = "AssignmentAbandoned"
    AssignmentReturned = "AssignmentReturned"
    AssignmentSubmitted = "AssignmentSubmitted"
    AssignmentRejected = "AssignmentRejected"
    AssignmentApproved = "AssignmentApproved"
    HITCreated = "HITCreated"
    HITExpired = "HITExpired"
    HITReviewable = "HITReviewable"
    HITExtended = "HITExtended"
    HITDisposed = "HITDisposed"
    Ping = "Ping"


@dataclasses.dataclass
class GetAccountBalanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetAccountBalanceResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "available_balance",
                "AvailableBalance",
                autoboto.TypeInfo(str),
            ),
            (
                "on_hold_balance",
                "OnHoldBalance",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string representing a currency amount.
    available_balance: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string representing a currency amount.
    on_hold_balance: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetAssignmentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assignment_id",
                "AssignmentId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Assignment to be retrieved.
    assignment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAssignmentResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assignment",
                "Assignment",
                autoboto.TypeInfo(Assignment),
            ),
            (
                "hit",
                "HIT",
                autoboto.TypeInfo(HIT),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The assignment. The response includes one Assignment element.
    assignment: "Assignment" = dataclasses.field(default_factory=dict, )

    # The HIT associated with this assignment. The response includes one HIT
    # element.
    hit: "HIT" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetFileUploadURLRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assignment_id",
                "AssignmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "question_identifier",
                "QuestionIdentifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the assignment that contains the question with a
    # FileUploadAnswer.
    assignment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier of the question with a FileUploadAnswer, as specified in the
    # QuestionForm of the HIT.
    question_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetFileUploadURLResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "file_upload_url",
                "FileUploadURL",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A temporary URL for the file that the Worker uploaded for the answer.
    file_upload_url: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetHITRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hit_id",
                "HITId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the HIT to be retrieved.
    hit_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetHITResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hit",
                "HIT",
                autoboto.TypeInfo(HIT),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains the requested HIT data.
    hit: "HIT" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetQualificationScoreRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "qualification_type_id",
                "QualificationTypeId",
                autoboto.TypeInfo(str),
            ),
            (
                "worker_id",
                "WorkerId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the QualificationType.
    qualification_type_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the Worker whose Qualification is being updated.
    worker_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetQualificationScoreResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "qualification",
                "Qualification",
                autoboto.TypeInfo(Qualification),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Qualification data structure of the Qualification assigned to a user,
    # including the Qualification type and the value (score).
    qualification: "Qualification" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetQualificationTypeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "qualification_type_id",
                "QualificationTypeId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the QualificationType.
    qualification_type_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetQualificationTypeResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "qualification_type",
                "QualificationType",
                autoboto.TypeInfo(QualificationType),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The returned Qualification Type
    qualification_type: "QualificationType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class HIT(autoboto.ShapeBase):
    """
    The HIT data structure represents a single HIT, including all the information
    necessary for a Worker to accept and complete the HIT.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hit_id",
                "HITId",
                autoboto.TypeInfo(str),
            ),
            (
                "hit_type_id",
                "HITTypeId",
                autoboto.TypeInfo(str),
            ),
            (
                "hit_group_id",
                "HITGroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "hit_layout_id",
                "HITLayoutId",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "title",
                "Title",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "question",
                "Question",
                autoboto.TypeInfo(str),
            ),
            (
                "keywords",
                "Keywords",
                autoboto.TypeInfo(str),
            ),
            (
                "hit_status",
                "HITStatus",
                autoboto.TypeInfo(HITStatus),
            ),
            (
                "max_assignments",
                "MaxAssignments",
                autoboto.TypeInfo(int),
            ),
            (
                "reward",
                "Reward",
                autoboto.TypeInfo(str),
            ),
            (
                "auto_approval_delay_in_seconds",
                "AutoApprovalDelayInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "expiration",
                "Expiration",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "assignment_duration_in_seconds",
                "AssignmentDurationInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "requester_annotation",
                "RequesterAnnotation",
                autoboto.TypeInfo(str),
            ),
            (
                "qualification_requirements",
                "QualificationRequirements",
                autoboto.TypeInfo(typing.List[QualificationRequirement]),
            ),
            (
                "hit_review_status",
                "HITReviewStatus",
                autoboto.TypeInfo(HITReviewStatus),
            ),
            (
                "number_of_assignments_pending",
                "NumberOfAssignmentsPending",
                autoboto.TypeInfo(int),
            ),
            (
                "number_of_assignments_available",
                "NumberOfAssignmentsAvailable",
                autoboto.TypeInfo(int),
            ),
            (
                "number_of_assignments_completed",
                "NumberOfAssignmentsCompleted",
                autoboto.TypeInfo(int),
            ),
        ]

    # A unique identifier for the HIT.
    hit_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the HIT type of this HIT
    hit_type_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the HIT Group of this HIT.
    hit_group_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the HIT Layout of this HIT.
    hit_layout_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date and time the HIT was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The title of the HIT.
    title: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A general description of the HIT.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The data the Worker completing the HIT uses produce the results. This is
    # either either a QuestionForm, HTMLQuestion or an ExternalQuestion data
    # structure.
    question: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more words or phrases that describe the HIT, separated by commas.
    # Search terms similar to the keywords of a HIT are more likely to have the
    # HIT in the search results.
    keywords: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the HIT and its assignments. Valid Values are Assignable |
    # Unassignable | Reviewable | Reviewing | Disposed.
    hit_status: "HITStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of times the HIT can be accepted and completed before the HIT
    # becomes unavailable.
    max_assignments: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string representing a currency amount.
    reward: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The amount of time, in seconds, after the Worker submits an assignment for
    # the HIT that the results are automatically approved by Amazon Mechanical
    # Turk. This is the amount of time the Requester has to reject an assignment
    # submitted by a Worker before the assignment is auto-approved and the Worker
    # is paid.
    auto_approval_delay_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time the HIT expires.
    expiration: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The length of time, in seconds, that a Worker has to complete the HIT after
    # accepting it.
    assignment_duration_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An arbitrary data field the Requester who created the HIT can use. This
    # field is visible only to the creator of the HIT.
    requester_annotation: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Conditions that a Worker's Qualifications must meet in order to accept the
    # HIT. A HIT can have between zero and ten Qualification requirements. All
    # requirements must be met in order for a Worker to accept the HIT.
    # Additionally, other actions can be restricted using the `ActionsGuarded`
    # field on each `QualificationRequirement` structure.
    qualification_requirements: typing.List["QualificationRequirement"
                                           ] = dataclasses.field(
                                               default_factory=list,
                                           )

    # Indicates the review status of the HIT. Valid Values are NotReviewed |
    # MarkedForReview | ReviewedAppropriate | ReviewedInappropriate.
    hit_review_status: "HITReviewStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of assignments for this HIT that are being previewed or have
    # been accepted by Workers, but have not yet been submitted, returned, or
    # abandoned.
    number_of_assignments_pending: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of assignments for this HIT that are available for Workers to
    # accept.
    number_of_assignments_available: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of assignments for this HIT that have been approved or rejected.
    number_of_assignments_completed: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class HITAccessActions(Enum):
    Accept = "Accept"
    PreviewAndAccept = "PreviewAndAccept"
    DiscoverPreviewAndAccept = "DiscoverPreviewAndAccept"


@dataclasses.dataclass
class HITLayoutParameter(autoboto.ShapeBase):
    """
    The HITLayoutParameter data structure defines parameter values used with a
    HITLayout. A HITLayout is a reusable Amazon Mechanical Turk project template
    used to provide Human Intelligence Task (HIT) question data for CreateHIT.
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
        ]

    # The name of the parameter in the HITLayout.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value substituted for the parameter referenced in the HITLayout.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class HITReviewStatus(Enum):
    NotReviewed = "NotReviewed"
    MarkedForReview = "MarkedForReview"
    ReviewedAppropriate = "ReviewedAppropriate"
    ReviewedInappropriate = "ReviewedInappropriate"


class HITStatus(Enum):
    Assignable = "Assignable"
    Unassignable = "Unassignable"
    Reviewable = "Reviewable"
    Reviewing = "Reviewing"
    Disposed = "Disposed"


@dataclasses.dataclass
class ListAssignmentsForHITRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hit_id",
                "HITId",
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
            (
                "assignment_statuses",
                "AssignmentStatuses",
                autoboto.TypeInfo(typing.List[AssignmentStatus]),
            ),
        ]

    # The ID of the HIT.
    hit_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Pagination token
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the assignments to return: Submitted | Approved | Rejected
    assignment_statuses: typing.List["AssignmentStatus"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListAssignmentsForHITResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "num_results",
                "NumResults",
                autoboto.TypeInfo(int),
            ),
            (
                "assignments",
                "Assignments",
                autoboto.TypeInfo(typing.List[Assignment]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the previous response was incomplete (because there is more data to
    # retrieve), Amazon Mechanical Turk returns a pagination token in the
    # response. You can use this pagination token to retrieve the next set of
    # results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of assignments on the page in the filtered results list,
    # equivalent to the number of assignments returned by this call.
    num_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The collection of Assignment data structures returned by this call.
    assignments: typing.List["Assignment"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListBonusPaymentsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hit_id",
                "HITId",
                autoboto.TypeInfo(str),
            ),
            (
                "assignment_id",
                "AssignmentId",
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

    # The ID of the HIT associated with the bonus payments to retrieve. If not
    # specified, all bonus payments for all assignments for the given HIT are
    # returned. Either the HITId parameter or the AssignmentId parameter must be
    # specified
    hit_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the assignment associated with the bonus payments to retrieve. If
    # specified, only bonus payments for the given assignment are returned.
    # Either the HITId parameter or the AssignmentId parameter must be specified
    assignment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Pagination token
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBonusPaymentsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "num_results",
                "NumResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "bonus_payments",
                "BonusPayments",
                autoboto.TypeInfo(typing.List[BonusPayment]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of bonus payments on this page in the filtered results list,
    # equivalent to the number of bonus payments being returned by this call.
    num_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the previous response was incomplete (because there is more data to
    # retrieve), Amazon Mechanical Turk returns a pagination token in the
    # response. You can use this pagination token to retrieve the next set of
    # results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A successful request to the ListBonusPayments operation returns a list of
    # BonusPayment objects.
    bonus_payments: typing.List["BonusPayment"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListHITsForQualificationTypeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "qualification_type_id",
                "QualificationTypeId",
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

    # The ID of the Qualification type to use when querying HITs.
    qualification_type_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Pagination Token
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Limit the number of results returned.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListHITsForQualificationTypeResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "num_results",
                "NumResults",
                autoboto.TypeInfo(int),
            ),
            (
                "_hits",
                "HITs",
                autoboto.TypeInfo(typing.List[HIT]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the previous response was incomplete (because there is more data to
    # retrieve), Amazon Mechanical Turk returns a pagination token in the
    # response. You can use this pagination token to retrieve the next set of
    # results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of HITs on this page in the filtered results list, equivalent to
    # the number of HITs being returned by this call.
    num_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of HIT elements returned by the query.
    _hits: typing.List["HIT"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class ListHITsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # Pagination token
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListHITsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "num_results",
                "NumResults",
                autoboto.TypeInfo(int),
            ),
            (
                "_hits",
                "HITs",
                autoboto.TypeInfo(typing.List[HIT]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the previous response was incomplete (because there is more data to
    # retrieve), Amazon Mechanical Turk returns a pagination token in the
    # response. You can use this pagination token to retrieve the next set of
    # results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of HITs on this page in the filtered results list, equivalent to
    # the number of HITs being returned by this call.
    num_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of HIT elements returned by the query.
    _hits: typing.List["HIT"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class ListQualificationRequestsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "qualification_type_id",
                "QualificationTypeId",
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

    # The ID of the QualificationType.
    qualification_type_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the previous response was incomplete (because there is more data to
    # retrieve), Amazon Mechanical Turk returns a pagination token in the
    # response. You can use this pagination token to retrieve the next set of
    # results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to return in a single call.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListQualificationRequestsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "num_results",
                "NumResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "qualification_requests",
                "QualificationRequests",
                autoboto.TypeInfo(typing.List[QualificationRequest]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of Qualification requests on this page in the filtered results
    # list, equivalent to the number of Qualification requests being returned by
    # this call.
    num_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the previous response was incomplete (because there is more data to
    # retrieve), Amazon Mechanical Turk returns a pagination token in the
    # response. You can use this pagination token to retrieve the next set of
    # results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Qualification request. The response includes one QualificationRequest
    # element for each Qualification request returned by the query.
    qualification_requests: typing.List["QualificationRequest"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )


@dataclasses.dataclass
class ListQualificationTypesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "must_be_requestable",
                "MustBeRequestable",
                autoboto.TypeInfo(bool),
            ),
            (
                "query",
                "Query",
                autoboto.TypeInfo(str),
            ),
            (
                "must_be_owned_by_caller",
                "MustBeOwnedByCaller",
                autoboto.TypeInfo(bool),
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

    # Specifies that only Qualification types that a user can request through the
    # Amazon Mechanical Turk web site, such as by taking a Qualification test,
    # are returned as results of the search. Some Qualification types, such as
    # those assigned automatically by the system, cannot be requested directly by
    # users. If false, all Qualification types, including those managed by the
    # system, are considered. Valid values are True | False.
    must_be_requestable: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A text query against all of the searchable attributes of Qualification
    # types.
    query: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies that only Qualification types that the Requester created are
    # returned. If false, the operation returns all Qualification types.
    must_be_owned_by_caller: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the previous response was incomplete (because there is more data to
    # retrieve), Amazon Mechanical Turk returns a pagination token in the
    # response. You can use this pagination token to retrieve the next set of
    # results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to return in a single call.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListQualificationTypesResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "num_results",
                "NumResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "qualification_types",
                "QualificationTypes",
                autoboto.TypeInfo(typing.List[QualificationType]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of Qualification types on this page in the filtered results
    # list, equivalent to the number of types this operation returns.
    num_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the previous response was incomplete (because there is more data to
    # retrieve), Amazon Mechanical Turk returns a pagination token in the
    # response. You can use this pagination token to retrieve the next set of
    # results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of QualificationType elements returned by the query.
    qualification_types: typing.List["QualificationType"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListReviewPolicyResultsForHITRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hit_id",
                "HITId",
                autoboto.TypeInfo(str),
            ),
            (
                "policy_levels",
                "PolicyLevels",
                autoboto.TypeInfo(typing.List[ReviewPolicyLevel]),
            ),
            (
                "retrieve_actions",
                "RetrieveActions",
                autoboto.TypeInfo(bool),
            ),
            (
                "retrieve_results",
                "RetrieveResults",
                autoboto.TypeInfo(bool),
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

    # The unique identifier of the HIT to retrieve review results for.
    hit_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Policy Level(s) to retrieve review results for - HIT or Assignment. If
    # omitted, the default behavior is to retrieve all data for both policy
    # levels. For a list of all the described policies, see Review Policies.
    policy_levels: typing.List["ReviewPolicyLevel"] = dataclasses.field(
        default_factory=list,
    )

    # Specify if the operation should retrieve a list of the actions taken
    # executing the Review Policies and their outcomes.
    retrieve_actions: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specify if the operation should retrieve a list of the results computed by
    # the Review Policies.
    retrieve_results: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Pagination token
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Limit the number of results returned.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListReviewPolicyResultsForHITResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hit_id",
                "HITId",
                autoboto.TypeInfo(str),
            ),
            (
                "assignment_review_policy",
                "AssignmentReviewPolicy",
                autoboto.TypeInfo(ReviewPolicy),
            ),
            (
                "hit_review_policy",
                "HITReviewPolicy",
                autoboto.TypeInfo(ReviewPolicy),
            ),
            (
                "assignment_review_report",
                "AssignmentReviewReport",
                autoboto.TypeInfo(ReviewReport),
            ),
            (
                "hit_review_report",
                "HITReviewReport",
                autoboto.TypeInfo(ReviewReport),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The HITId of the HIT for which results have been returned.
    hit_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the Assignment-level Review Policy. This contains only the
    # PolicyName element.
    assignment_review_policy: "ReviewPolicy" = dataclasses.field(
        default_factory=dict,
    )

    # The name of the HIT-level Review Policy. This contains only the PolicyName
    # element.
    hit_review_policy: "ReviewPolicy" = dataclasses.field(
        default_factory=dict,
    )

    # Contains both ReviewResult and ReviewAction elements for an Assignment.
    assignment_review_report: "ReviewReport" = dataclasses.field(
        default_factory=dict,
    )

    # Contains both ReviewResult and ReviewAction elements for a particular HIT.
    hit_review_report: "ReviewReport" = dataclasses.field(
        default_factory=dict,
    )

    # If the previous response was incomplete (because there is more data to
    # retrieve), Amazon Mechanical Turk returns a pagination token in the
    # response. You can use this pagination token to retrieve the next set of
    # results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListReviewableHITsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hit_type_id",
                "HITTypeId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(ReviewableHITStatus),
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

    # The ID of the HIT type of the HITs to consider for the query. If not
    # specified, all HITs for the Reviewer are considered
    hit_type_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Can be either `Reviewable` or `Reviewing`. Reviewable is the default value.
    status: "ReviewableHITStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Pagination Token
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Limit the number of results returned.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListReviewableHITsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "num_results",
                "NumResults",
                autoboto.TypeInfo(int),
            ),
            (
                "_hits",
                "HITs",
                autoboto.TypeInfo(typing.List[HIT]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the previous response was incomplete (because there is more data to
    # retrieve), Amazon Mechanical Turk returns a pagination token in the
    # response. You can use this pagination token to retrieve the next set of
    # results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of HITs on this page in the filtered results list, equivalent to
    # the number of HITs being returned by this call.
    num_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of HIT elements returned by the query.
    _hits: typing.List["HIT"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class ListWorkerBlocksRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # Pagination token
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListWorkerBlocksResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "num_results",
                "NumResults",
                autoboto.TypeInfo(int),
            ),
            (
                "worker_blocks",
                "WorkerBlocks",
                autoboto.TypeInfo(typing.List[WorkerBlock]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the previous response was incomplete (because there is more data to
    # retrieve), Amazon Mechanical Turk returns a pagination token in the
    # response. You can use this pagination token to retrieve the next set of
    # results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of assignments on the page in the filtered results list,
    # equivalent to the number of assignments returned by this call.
    num_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of WorkerBlocks, containing the collection of Worker IDs and
    # reasons for blocking.
    worker_blocks: typing.List["WorkerBlock"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListWorkersWithQualificationTypeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "qualification_type_id",
                "QualificationTypeId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(QualificationStatus),
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

    # The ID of the Qualification type of the Qualifications to return.
    qualification_type_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the Qualifications to return. Can be `Granted | Revoked`.
    status: "QualificationStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Pagination Token
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Limit the number of results returned.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListWorkersWithQualificationTypeResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "num_results",
                "NumResults",
                autoboto.TypeInfo(int),
            ),
            (
                "qualifications",
                "Qualifications",
                autoboto.TypeInfo(typing.List[Qualification]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the previous response was incomplete (because there is more data to
    # retrieve), Amazon Mechanical Turk returns a pagination token in the
    # response. You can use this pagination token to retrieve the next set of
    # results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of Qualifications on this page in the filtered results list,
    # equivalent to the number of Qualifications being returned by this call.
    num_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of Qualification elements returned by this call.
    qualifications: typing.List["Qualification"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Locale(autoboto.ShapeBase):
    """
    The Locale data structure represents a geographical region or location.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "country",
                "Country",
                autoboto.TypeInfo(str),
            ),
            (
                "subdivision",
                "Subdivision",
                autoboto.TypeInfo(str),
            ),
        ]

    # The country of the locale. Must be a valid ISO 3166 country code. For
    # example, the code US refers to the United States of America.
    country: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The state or subdivision of the locale. A valid ISO 3166-2 subdivision
    # code. For example, the code WA refers to the state of Washington.
    subdivision: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotificationSpecification(autoboto.ShapeBase):
    """
    The NotificationSpecification data structure describes a HIT event notification
    for a HIT type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination",
                "Destination",
                autoboto.TypeInfo(str),
            ),
            (
                "transport",
                "Transport",
                autoboto.TypeInfo(NotificationTransport),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(str),
            ),
            (
                "event_types",
                "EventTypes",
                autoboto.TypeInfo(typing.List[EventType]),
            ),
        ]

    # The target for notification messages. The Destination’s format is
    # determined by the specified Transport:

    #   * When Transport is Email, the Destination is your email address.

    #   * When Transport is SQS, the Destination is your queue URL.

    #   * When Transport is SNS, the Destination is the ARN of your topic.
    destination: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The method Amazon Mechanical Turk uses to send the notification. Valid
    # Values: Email | SQS | SNS.
    transport: "NotificationTransport" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The version of the Notification API to use. Valid value is 2006-05-05.
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of events that should cause notifications to be sent. Valid
    # Values: AssignmentAccepted | AssignmentAbandoned | AssignmentReturned |
    # AssignmentSubmitted | AssignmentRejected | AssignmentApproved | HITCreated
    # | HITExtended | HITDisposed | HITReviewable | HITExpired | Ping. The Ping
    # event is only valid for the SendTestEventNotification operation.
    event_types: typing.List["EventType"] = dataclasses.field(
        default_factory=list,
    )


class NotificationTransport(Enum):
    Email = "Email"
    SQS = "SQS"
    SNS = "SNS"


class NotifyWorkersFailureCode(Enum):
    SoftFailure = "SoftFailure"
    HardFailure = "HardFailure"


@dataclasses.dataclass
class NotifyWorkersFailureStatus(autoboto.ShapeBase):
    """
    When MTurk encounters an issue with notifying the Workers you specified, it
    returns back this object with failure details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notify_workers_failure_code",
                "NotifyWorkersFailureCode",
                autoboto.TypeInfo(NotifyWorkersFailureCode),
            ),
            (
                "notify_workers_failure_message",
                "NotifyWorkersFailureMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "worker_id",
                "WorkerId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Encoded value for the failure type.
    notify_workers_failure_code: "NotifyWorkersFailureCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A message detailing the reason the Worker could not be notified.
    notify_workers_failure_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the Worker.
    worker_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotifyWorkersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subject",
                "Subject",
                autoboto.TypeInfo(str),
            ),
            (
                "message_text",
                "MessageText",
                autoboto.TypeInfo(str),
            ),
            (
                "worker_ids",
                "WorkerIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The subject line of the email message to send. Can include up to 200
    # characters.
    subject: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The text of the email message to send. Can include up to 4,096 characters
    message_text: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of Worker IDs you wish to notify. You can notify upto 100 Workers at
    # a time.
    worker_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class NotifyWorkersResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "notify_workers_failure_statuses",
                "NotifyWorkersFailureStatuses",
                autoboto.TypeInfo(typing.List[NotifyWorkersFailureStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When MTurk sends notifications to the list of Workers, it returns back any
    # failures it encounters in this list of NotifyWorkersFailureStatus objects.
    notify_workers_failure_statuses: typing.List["NotifyWorkersFailureStatus"
                                                ] = dataclasses.field(
                                                    default_factory=list,
                                                )


@dataclasses.dataclass
class ParameterMapEntry(autoboto.ShapeBase):
    """
    This data structure is the data type for the AnswerKey parameter of the
    ScoreMyKnownAnswers/2011-09-01 Review Policy.
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

    # The QuestionID from the HIT that is used to identify which question
    # requires Mechanical Turk to score as part of the
    # ScoreMyKnownAnswers/2011-09-01 Review Policy.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of answers to the question specified in the MapEntry Key element.
    # The Worker must match all values in order for the answer to be scored
    # correctly.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class PolicyParameter(autoboto.ShapeBase):
    """
    Name of the parameter from the Review policy.
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
            (
                "map_entries",
                "MapEntries",
                autoboto.TypeInfo(typing.List[ParameterMapEntry]),
            ),
        ]

    # Name of the parameter from the list of Review Polices.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of values of the Parameter
    values: typing.List[str] = dataclasses.field(default_factory=list, )

    # List of ParameterMapEntry objects.
    map_entries: typing.List["ParameterMapEntry"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Qualification(autoboto.ShapeBase):
    """
    The Qualification data structure represents a Qualification assigned to a user,
    including the Qualification type and the value (score).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "qualification_type_id",
                "QualificationTypeId",
                autoboto.TypeInfo(str),
            ),
            (
                "worker_id",
                "WorkerId",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_time",
                "GrantTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "integer_value",
                "IntegerValue",
                autoboto.TypeInfo(int),
            ),
            (
                "locale_value",
                "LocaleValue",
                autoboto.TypeInfo(Locale),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(QualificationStatus),
            ),
        ]

    # The ID of the Qualification type for the Qualification.
    qualification_type_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the Worker who possesses the Qualification.
    worker_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date and time the Qualification was granted to the Worker. If the
    # Worker's Qualification was revoked, and then re-granted based on a new
    # Qualification request, GrantTime is the date and time of the last call to
    # the AcceptQualificationRequest operation.
    grant_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The value (score) of the Qualification, if the Qualification has an integer
    # value.
    integer_value: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Locale data structure represents a geographical region or location.
    locale_value: "Locale" = dataclasses.field(default_factory=dict, )

    # The status of the Qualification. Valid values are Granted | Revoked.
    status: "QualificationStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class QualificationRequest(autoboto.ShapeBase):
    """
    The QualificationRequest data structure represents a request a Worker has made
    for a Qualification.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "qualification_request_id",
                "QualificationRequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "qualification_type_id",
                "QualificationTypeId",
                autoboto.TypeInfo(str),
            ),
            (
                "worker_id",
                "WorkerId",
                autoboto.TypeInfo(str),
            ),
            (
                "test",
                "Test",
                autoboto.TypeInfo(str),
            ),
            (
                "answer",
                "Answer",
                autoboto.TypeInfo(str),
            ),
            (
                "submit_time",
                "SubmitTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The ID of the Qualification request, a unique identifier generated when the
    # request was submitted.
    qualification_request_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the Qualification type the Worker is requesting, as returned by
    # the CreateQualificationType operation.
    qualification_type_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the Worker requesting the Qualification.
    worker_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The contents of the Qualification test that was presented to the Worker, if
    # the type has a test and the Worker has submitted answers. This value is
    # identical to the QuestionForm associated with the Qualification type at the
    # time the Worker requests the Qualification.
    test: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Worker's answers for the Qualification type's test contained in a
    # QuestionFormAnswers document, if the type has a test and the Worker has
    # submitted answers. If the Worker does not provide any answers, Answer may
    # be empty.
    answer: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date and time the Qualification request had a status of Submitted. This
    # is either the time the Worker submitted answers for a Qualification test,
    # or the time the Worker requested the Qualification if the Qualification
    # type does not have a test.
    submit_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class QualificationRequirement(autoboto.ShapeBase):
    """
    The QualificationRequirement data structure describes a Qualification that a
    Worker must have before the Worker is allowed to accept a HIT. A requirement may
    optionally state that a Worker must have the Qualification in order to preview
    the HIT, or see the HIT in search results.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "qualification_type_id",
                "QualificationTypeId",
                autoboto.TypeInfo(str),
            ),
            (
                "comparator",
                "Comparator",
                autoboto.TypeInfo(Comparator),
            ),
            (
                "integer_values",
                "IntegerValues",
                autoboto.TypeInfo(typing.List[int]),
            ),
            (
                "locale_values",
                "LocaleValues",
                autoboto.TypeInfo(typing.List[Locale]),
            ),
            (
                "required_to_preview",
                "RequiredToPreview",
                autoboto.TypeInfo(bool),
            ),
            (
                "actions_guarded",
                "ActionsGuarded",
                autoboto.TypeInfo(HITAccessActions),
            ),
        ]

    # The ID of the Qualification type for the requirement.
    qualification_type_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The kind of comparison to make against a Qualification's value. You can
    # compare a Qualification's value to an IntegerValue to see if it is
    # LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or
    # NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if
    # it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the
    # value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a
    # Qualification requirement can also test if a Qualification Exists or
    # DoesNotExist in the user's profile, regardless of its value.
    comparator: "Comparator" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The integer value to compare against the Qualification's value.
    # IntegerValue must not be present if Comparator is Exists or DoesNotExist.
    # IntegerValue can only be used if the Qualification type has an integer
    # value; it cannot be used with the Worker_Locale QualificationType ID. When
    # performing a set comparison by using the In or the NotIn comparator, you
    # can use up to 15 IntegerValue elements in a QualificationRequirement data
    # structure.
    integer_values: typing.List[int] = dataclasses.field(default_factory=list, )

    # The locale value to compare against the Qualification's value. The local
    # value must be a valid ISO 3166 country code or supports ISO 3166-2
    # subdivisions. LocaleValue can only be used with a Worker_Locale
    # QualificationType ID. LocaleValue can only be used with the EqualTo,
    # NotEqualTo, In, and NotIn comparators. You must only use a single
    # LocaleValue element when using the EqualTo or NotEqualTo comparators. When
    # performing a set comparison by using the In or the NotIn comparator, you
    # can use up to 30 LocaleValue elements in a QualificationRequirement data
    # structure.
    locale_values: typing.List["Locale"] = dataclasses.field(
        default_factory=list,
    )

    # DEPRECATED: Use the `ActionsGuarded` field instead. If RequiredToPreview is
    # true, the question data for the HIT will not be shown when a Worker whose
    # Qualifications do not meet this requirement tries to preview the HIT. That
    # is, a Worker's Qualifications must meet all of the requirements for which
    # RequiredToPreview is true in order to preview the HIT. If a Worker meets
    # all of the requirements where RequiredToPreview is true (or if there are no
    # such requirements), but does not meet all of the requirements for the HIT,
    # the Worker will be allowed to preview the HIT's question data, but will not
    # be allowed to accept and complete the HIT. The default is false. This
    # should not be used in combination with the `ActionsGuarded` field.
    required_to_preview: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Setting this attribute prevents Workers whose Qualifications do not meet
    # this QualificationRequirement from taking the specified action. Valid
    # arguments include "Accept" (Worker cannot accept the HIT, but can preview
    # the HIT and see it in their search results), "PreviewAndAccept" (Worker
    # cannot accept or preview the HIT, but can see the HIT in their search
    # results), and "DiscoverPreviewAndAccept" (Worker cannot accept, preview, or
    # see the HIT in their search results). It's possible for you to create a HIT
    # with multiple QualificationRequirements (which can have different values
    # for the ActionGuarded attribute). In this case, the Worker is only
    # permitted to perform an action when they have met all
    # QualificationRequirements guarding the action. The actions in the order of
    # least restrictive to most restrictive are Discover, Preview and Accept. For
    # example, if a Worker meets all QualificationRequirements that are set to
    # DiscoverPreviewAndAccept, but do not meet all requirements that are set
    # with PreviewAndAccept, then the Worker will be able to Discover, i.e. see
    # the HIT in their search result, but will not be able to Preview or Accept
    # the HIT. ActionsGuarded should not be used in combination with the
    # `RequiredToPreview` field.
    actions_guarded: "HITAccessActions" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class QualificationStatus(Enum):
    Granted = "Granted"
    Revoked = "Revoked"


@dataclasses.dataclass
class QualificationType(autoboto.ShapeBase):
    """
    The QualificationType data structure represents a Qualification type, a
    description of a property of a Worker that must match the requirements of a HIT
    for the Worker to be able to accept the HIT. The type also describes how a
    Worker can obtain a Qualification of that type, such as through a Qualification
    test.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "qualification_type_id",
                "QualificationTypeId",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "keywords",
                "Keywords",
                autoboto.TypeInfo(str),
            ),
            (
                "qualification_type_status",
                "QualificationTypeStatus",
                autoboto.TypeInfo(QualificationTypeStatus),
            ),
            (
                "test",
                "Test",
                autoboto.TypeInfo(str),
            ),
            (
                "test_duration_in_seconds",
                "TestDurationInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "answer_key",
                "AnswerKey",
                autoboto.TypeInfo(str),
            ),
            (
                "retry_delay_in_seconds",
                "RetryDelayInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "is_requestable",
                "IsRequestable",
                autoboto.TypeInfo(bool),
            ),
            (
                "auto_granted",
                "AutoGranted",
                autoboto.TypeInfo(bool),
            ),
            (
                "auto_granted_value",
                "AutoGrantedValue",
                autoboto.TypeInfo(int),
            ),
        ]

    # A unique identifier for the Qualification type. A Qualification type is
    # given a Qualification type ID when you call the CreateQualificationType
    # operation.
    qualification_type_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time the Qualification type was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the Qualification type. The type name is used to identify the
    # type, and to find the type using a Qualification type search.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A long description for the Qualification type.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more words or phrases that describe theQualification type, separated
    # by commas. The Keywords make the type easier to find using a search.
    keywords: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the Qualification type. A Qualification type's status
    # determines if users can apply to receive a Qualification of this type, and
    # if HITs can be created with requirements based on this type. Valid values
    # are Active | Inactive.
    qualification_type_status: "QualificationTypeStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The questions for a Qualification test associated with this Qualification
    # type that a user can take to obtain a Qualification of this type. This
    # parameter must be specified if AnswerKey is present. A Qualification type
    # cannot have both a specified Test parameter and an AutoGranted value of
    # true.
    test: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The amount of time, in seconds, given to a Worker to complete the
    # Qualification test, beginning from the time the Worker requests the
    # Qualification.
    test_duration_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The answers to the Qualification test specified in the Test parameter.
    answer_key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The amount of time, in seconds, Workers must wait after taking the
    # Qualification test before they can take it again. Workers can take a
    # Qualification test multiple times if they were not granted the
    # Qualification from a previous attempt, or if the test offers a gradient
    # score and they want a better score. If not specified, retries are disabled
    # and Workers can request a Qualification only once.
    retry_delay_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether the Qualification type is one that a user can request
    # through the Amazon Mechanical Turk web site, such as by taking a
    # Qualification test. This value is False for Qualifications assigned
    # automatically by the system. Valid values are True | False.
    is_requestable: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies that requests for the Qualification type are granted immediately,
    # without prompting the Worker with a Qualification test. Valid values are
    # True | False.
    auto_granted: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Qualification integer value to use for automatically granted
    # Qualifications, if AutoGranted is true. This is 1 by default.
    auto_granted_value: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class QualificationTypeStatus(Enum):
    Active = "Active"
    Inactive = "Inactive"


@dataclasses.dataclass
class RejectAssignmentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assignment_id",
                "AssignmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "requester_feedback",
                "RequesterFeedback",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the assignment. The assignment must correspond to a HIT created
    # by the Requester.
    assignment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A message for the Worker, which the Worker can see in the Status section of
    # the web site.
    requester_feedback: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RejectAssignmentResponse(autoboto.OutputShapeBase):
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
class RejectQualificationRequestRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "qualification_request_id",
                "QualificationRequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "reason",
                "Reason",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Qualification request, as returned by the
    # `ListQualificationRequests` operation.
    qualification_request_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A text message explaining why the request was rejected, to be shown to the
    # Worker who made the request.
    reason: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RejectQualificationRequestResponse(autoboto.OutputShapeBase):
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
class RequestError(autoboto.ShapeBase):
    """
    Your request is invalid.
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
                "turk_error_code",
                "TurkErrorCode",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    turk_error_code: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReviewActionDetail(autoboto.ShapeBase):
    """
    Both the AssignmentReviewReport and the HITReviewReport elements contains the
    ReviewActionDetail data structure. This structure is returned multiple times for
    each action specified in the Review Policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_id",
                "ActionId",
                autoboto.TypeInfo(str),
            ),
            (
                "action_name",
                "ActionName",
                autoboto.TypeInfo(str),
            ),
            (
                "target_id",
                "TargetId",
                autoboto.TypeInfo(str),
            ),
            (
                "target_type",
                "TargetType",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(ReviewActionStatus),
            ),
            (
                "complete_time",
                "CompleteTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "result",
                "Result",
                autoboto.TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier for the action.
    action_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The nature of the action itself. The Review Policy is responsible for
    # examining the HIT and Assignments, emitting results, and deciding which
    # other actions will be necessary.
    action_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The specific HITId or AssignmentID targeted by the action.
    target_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of object in TargetId.
    target_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The current disposition of the action: INTENDED, SUCCEEDED, FAILED, or
    # CANCELLED.
    status: "ReviewActionStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date when the action was completed.
    complete_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A description of the outcome of the review.
    result: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Present only when the Results have a FAILED Status.
    error_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ReviewActionStatus(Enum):
    Intended = "Intended"
    Succeeded = "Succeeded"
    Failed = "Failed"
    Cancelled = "Cancelled"


@dataclasses.dataclass
class ReviewPolicy(autoboto.ShapeBase):
    """
    HIT Review Policy data structures represent HIT review policies, which you
    specify when you create a HIT.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "PolicyName",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.List[PolicyParameter]),
            ),
        ]

    # Name of a Review Policy: SimplePlurality/2011-09-01 or
    # ScoreMyKnownAnswers/2011-09-01
    policy_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Name of the parameter from the Review policy.
    parameters: typing.List["PolicyParameter"] = dataclasses.field(
        default_factory=list,
    )


class ReviewPolicyLevel(Enum):
    Assignment = "Assignment"
    HIT = "HIT"


@dataclasses.dataclass
class ReviewReport(autoboto.ShapeBase):
    """
    Contains both ReviewResult and ReviewAction elements for a particular HIT.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "review_results",
                "ReviewResults",
                autoboto.TypeInfo(typing.List[ReviewResultDetail]),
            ),
            (
                "review_actions",
                "ReviewActions",
                autoboto.TypeInfo(typing.List[ReviewActionDetail]),
            ),
        ]

    # A list of ReviewResults objects for each action specified in the Review
    # Policy.
    review_results: typing.List["ReviewResultDetail"] = dataclasses.field(
        default_factory=list,
    )

    # A list of ReviewAction objects for each action specified in the Review
    # Policy.
    review_actions: typing.List["ReviewActionDetail"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ReviewResultDetail(autoboto.ShapeBase):
    """
    This data structure is returned multiple times for each result specified in the
    Review Policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_id",
                "ActionId",
                autoboto.TypeInfo(str),
            ),
            (
                "subject_id",
                "SubjectId",
                autoboto.TypeInfo(str),
            ),
            (
                "subject_type",
                "SubjectType",
                autoboto.TypeInfo(str),
            ),
            (
                "question_id",
                "QuestionId",
                autoboto.TypeInfo(str),
            ),
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

    # A unique identifier of the Review action result.
    action_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The HITID or AssignmentId about which this result was taken. Note that HIT-
    # level Review Policies will often emit results about both the HIT itself and
    # its Assignments, while Assignment-level review policies generally only emit
    # results about the Assignment itself.
    subject_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of the object from the SubjectId field.
    subject_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the QuestionId the result is describing. Depending on whether the
    # TargetType is a HIT or Assignment this results could specify multiple
    # values. If TargetType is HIT and QuestionId is absent, then the result
    # describes results of the HIT, including the HIT agreement score. If
    # ObjectType is Assignment and QuestionId is absent, then the result
    # describes the Worker's performance on the HIT.
    question_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Key identifies the particular piece of reviewed information.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The values of Key provided by the review policies you have selected.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ReviewableHITStatus(Enum):
    Reviewable = "Reviewable"
    Reviewing = "Reviewing"


@dataclasses.dataclass
class SendBonusRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "worker_id",
                "WorkerId",
                autoboto.TypeInfo(str),
            ),
            (
                "bonus_amount",
                "BonusAmount",
                autoboto.TypeInfo(str),
            ),
            (
                "assignment_id",
                "AssignmentId",
                autoboto.TypeInfo(str),
            ),
            (
                "reason",
                "Reason",
                autoboto.TypeInfo(str),
            ),
            (
                "unique_request_token",
                "UniqueRequestToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Worker being paid the bonus.
    worker_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Bonus amount is a US Dollar amount specified using a string (for
    # example, "5" represents $5.00 USD and "101.42" represents $101.42 USD). Do
    # not include currency symbols or currency codes.
    bonus_amount: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the assignment for which this bonus is paid.
    assignment_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A message that explains the reason for the bonus payment. The Worker
    # receiving the bonus can see this message.
    reason: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A unique identifier for this request, which allows you to retry the call on
    # error without granting multiple bonuses. This is useful in cases such as
    # network timeouts where it is unclear whether or not the call succeeded on
    # the server. If the bonus already exists in the system from a previous call
    # using the same UniqueRequestToken, subsequent calls will return an error
    # with a message containing the request ID.
    unique_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SendBonusResponse(autoboto.OutputShapeBase):
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
class SendTestEventNotificationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notification",
                "Notification",
                autoboto.TypeInfo(NotificationSpecification),
            ),
            (
                "test_event_type",
                "TestEventType",
                autoboto.TypeInfo(EventType),
            ),
        ]

    # The notification specification to test. This value is identical to the
    # value you would provide to the UpdateNotificationSettings operation when
    # you establish the notification specification for a HIT type.
    notification: "NotificationSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # The event to simulate to test the notification specification. This event is
    # included in the test message even if the notification specification does
    # not include the event type. The notification specification does not filter
    # out the test event.
    test_event_type: "EventType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SendTestEventNotificationResponse(autoboto.OutputShapeBase):
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
class ServiceFault(autoboto.ShapeBase):
    """
    Amazon Mechanical Turk is temporarily unable to process your request. Try your
    call again.
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
                "turk_error_code",
                "TurkErrorCode",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    turk_error_code: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateExpirationForHITRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hit_id",
                "HITId",
                autoboto.TypeInfo(str),
            ),
            (
                "expire_at",
                "ExpireAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The HIT to update.
    hit_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date and time at which you want the HIT to expire
    expire_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateExpirationForHITResponse(autoboto.OutputShapeBase):
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
class UpdateHITReviewStatusRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hit_id",
                "HITId",
                autoboto.TypeInfo(str),
            ),
            (
                "revert",
                "Revert",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the HIT to update.
    hit_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies how to update the HIT status. Default is `False`.

    #   * Setting this to false will only transition a HIT from `Reviewable` to `Reviewing`

    #   * Setting this to true will only transition a HIT from `Reviewing` to `Reviewable`
    revert: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateHITReviewStatusResponse(autoboto.OutputShapeBase):
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
class UpdateHITTypeOfHITRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hit_id",
                "HITId",
                autoboto.TypeInfo(str),
            ),
            (
                "hit_type_id",
                "HITTypeId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The HIT to update.
    hit_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the new HIT type.
    hit_type_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateHITTypeOfHITResponse(autoboto.OutputShapeBase):
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
class UpdateNotificationSettingsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hit_type_id",
                "HITTypeId",
                autoboto.TypeInfo(str),
            ),
            (
                "notification",
                "Notification",
                autoboto.TypeInfo(NotificationSpecification),
            ),
            (
                "active",
                "Active",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the HIT type whose notification specification is being updated.
    hit_type_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The notification specification for the HIT type.
    notification: "NotificationSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # Specifies whether notifications are sent for HITs of this HIT type,
    # according to the notification specification. You must specify either the
    # Notification parameter or the Active parameter for the call to
    # UpdateNotificationSettings to succeed.
    active: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateNotificationSettingsResponse(autoboto.OutputShapeBase):
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
class UpdateQualificationTypeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "qualification_type_id",
                "QualificationTypeId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "qualification_type_status",
                "QualificationTypeStatus",
                autoboto.TypeInfo(QualificationTypeStatus),
            ),
            (
                "test",
                "Test",
                autoboto.TypeInfo(str),
            ),
            (
                "answer_key",
                "AnswerKey",
                autoboto.TypeInfo(str),
            ),
            (
                "test_duration_in_seconds",
                "TestDurationInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "retry_delay_in_seconds",
                "RetryDelayInSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "auto_granted",
                "AutoGranted",
                autoboto.TypeInfo(bool),
            ),
            (
                "auto_granted_value",
                "AutoGrantedValue",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the Qualification type to update.
    qualification_type_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The new description of the Qualification type.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The new status of the Qualification type - Active | Inactive
    qualification_type_status: "QualificationTypeStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The questions for the Qualification test a Worker must answer correctly to
    # obtain a Qualification of this type. If this parameter is specified,
    # `TestDurationInSeconds` must also be specified.

    # Constraints: Must not be longer than 65535 bytes. Must be a QuestionForm
    # data structure. This parameter cannot be specified if AutoGranted is true.

    # Constraints: None. If not specified, the Worker may request the
    # Qualification without answering any questions.
    test: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The answers to the Qualification test specified in the Test parameter, in
    # the form of an AnswerKey data structure.
    answer_key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of seconds the Worker has to complete the Qualification test,
    # starting from the time the Worker requests the Qualification.
    test_duration_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The amount of time, in seconds, that Workers must wait after requesting a
    # Qualification of the specified Qualification type before they can retry the
    # Qualification request. It is not possible to disable retries for a
    # Qualification type after it has been created with retries enabled. If you
    # want to disable retries, you must dispose of the existing retry-enabled
    # Qualification type using DisposeQualificationType and then create a new
    # Qualification type with retries disabled using CreateQualificationType.
    retry_delay_in_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether requests for the Qualification type are granted
    # immediately, without prompting the Worker with a Qualification test.

    # Constraints: If the Test parameter is specified, this parameter cannot be
    # true.
    auto_granted: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Qualification value to use for automatically granted Qualifications.
    # This parameter is used only if the AutoGranted parameter is true.
    auto_granted_value: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateQualificationTypeResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "qualification_type",
                "QualificationType",
                autoboto.TypeInfo(QualificationType),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains a QualificationType data structure.
    qualification_type: "QualificationType" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class WorkerBlock(autoboto.ShapeBase):
    """
    The WorkerBlock data structure represents a Worker who has been blocked. It has
    two elements: the WorkerId and the Reason for the block.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "worker_id",
                "WorkerId",
                autoboto.TypeInfo(str),
            ),
            (
                "reason",
                "Reason",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Worker who accepted the HIT.
    worker_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A message explaining the reason the Worker was blocked.
    reason: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
