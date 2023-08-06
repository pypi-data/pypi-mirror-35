import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AcceptInvitationRequest(autoboto.ShapeBase):
    """
    AcceptInvitation request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "invitation_id",
                "InvitationId",
                autoboto.TypeInfo(str),
            ),
            (
                "master_id",
                "MasterId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the detector of the GuardDuty member account.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # This value is used to validate the master account to the member account.
    invitation_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The account ID of the master GuardDuty account whose invitation you're
    # accepting.
    master_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AcceptInvitationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AccessKeyDetails(autoboto.ShapeBase):
    """
    The IAM access key details (IAM user information) of a user that engaged in the
    activity that prompted GuardDuty to generate a finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_key_id",
                "AccessKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "principal_id",
                "PrincipalId",
                autoboto.TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                autoboto.TypeInfo(str),
            ),
            (
                "user_type",
                "UserType",
                autoboto.TypeInfo(str),
            ),
        ]

    # Access key ID of the user.
    access_key_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The principal ID of the user.
    principal_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the user.
    user_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of the user.
    user_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AccountDetail(autoboto.ShapeBase):
    """
    An object containing the member's accountId and email address.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "email",
                "Email",
                autoboto.TypeInfo(str),
            ),
        ]

    # Member account ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Member account's email address.
    email: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Action(autoboto.ShapeBase):
    """
    Information about the activity described in a finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_type",
                "ActionType",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_api_call_action",
                "AwsApiCallAction",
                autoboto.TypeInfo(AwsApiCallAction),
            ),
            (
                "dns_request_action",
                "DnsRequestAction",
                autoboto.TypeInfo(DnsRequestAction),
            ),
            (
                "network_connection_action",
                "NetworkConnectionAction",
                autoboto.TypeInfo(NetworkConnectionAction),
            ),
            (
                "port_probe_action",
                "PortProbeAction",
                autoboto.TypeInfo(PortProbeAction),
            ),
        ]

    # GuardDuty Finding activity type.
    action_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Information about the AWS_API_CALL action described in this finding.
    aws_api_call_action: "AwsApiCallAction" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the DNS_REQUEST action described in this finding.
    dns_request_action: "DnsRequestAction" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the NETWORK_CONNECTION action described in this finding.
    network_connection_action: "NetworkConnectionAction" = dataclasses.field(
        default_factory=dict,
    )

    # Information about the PORT_PROBE action described in this finding.
    port_probe_action: "PortProbeAction" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ArchiveFindingsRequest(autoboto.ShapeBase):
    """
    ArchiveFindings request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "finding_ids",
                "FindingIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the detector that specifies the GuardDuty service whose findings
    # you want to archive.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # IDs of the findings that you want to archive.
    finding_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class ArchiveFindingsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AwsApiCallAction(autoboto.ShapeBase):
    """
    Information about the AWS_API_CALL action described in this finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api",
                "Api",
                autoboto.TypeInfo(str),
            ),
            (
                "caller_type",
                "CallerType",
                autoboto.TypeInfo(str),
            ),
            (
                "domain_details",
                "DomainDetails",
                autoboto.TypeInfo(DomainDetails),
            ),
            (
                "remote_ip_details",
                "RemoteIpDetails",
                autoboto.TypeInfo(RemoteIpDetails),
            ),
            (
                "service_name",
                "ServiceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # AWS API name.
    api: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # AWS API caller type.
    caller_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Domain information for the AWS API call.
    domain_details: "DomainDetails" = dataclasses.field(default_factory=dict, )

    # Remote IP information of the connection.
    remote_ip_details: "RemoteIpDetails" = dataclasses.field(
        default_factory=dict,
    )

    # AWS service name whose API was invoked.
    service_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BadRequestException(autoboto.ShapeBase):
    """
    Error response object.
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
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The error type.
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class City(autoboto.ShapeBase):
    """
    City information of the remote IP address.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "city_name",
                "CityName",
                autoboto.TypeInfo(str),
            ),
        ]

    # City name of the remote IP address.
    city_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Condition(autoboto.ShapeBase):
    """
    Finding attribute (for example, accountId) for which conditions and values must
    be specified when querying findings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "eq",
                "Eq",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "gt",
                "Gt",
                autoboto.TypeInfo(int),
            ),
            (
                "gte",
                "Gte",
                autoboto.TypeInfo(int),
            ),
            (
                "lt",
                "Lt",
                autoboto.TypeInfo(int),
            ),
            (
                "lte",
                "Lte",
                autoboto.TypeInfo(int),
            ),
            (
                "neq",
                "Neq",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # Represents the equal condition to be applied to a single field when
    # querying for findings.
    eq: typing.List[str] = dataclasses.field(default_factory=list, )

    # Represents the greater than condition to be applied to a single field when
    # querying for findings.
    gt: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Represents the greater than equal condition to be applied to a single field
    # when querying for findings.
    gte: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Represents the less than condition to be applied to a single field when
    # querying for findings.
    lt: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Represents the less than equal condition to be applied to a single field
    # when querying for findings.
    lte: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Represents the not equal condition to be applied to a single field when
    # querying for findings.
    neq: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class Country(autoboto.ShapeBase):
    """
    Country information of the remote IP address.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "country_code",
                "CountryCode",
                autoboto.TypeInfo(str),
            ),
            (
                "country_name",
                "CountryName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Country code of the remote IP address.
    country_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Country name of the remote IP address.
    country_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateDetectorRequest(autoboto.ShapeBase):
    """
    CreateDetector request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enable",
                "Enable",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A boolean value that specifies whether the detector is to be enabled.
    enable: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateDetectorResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the created detector.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateFilterRequest(autoboto.ShapeBase):
    """
    CreateFilterRequest request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "action",
                "Action",
                autoboto.TypeInfo(FilterAction),
            ),
            (
                "client_token",
                "ClientToken",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "finding_criteria",
                "FindingCriteria",
                autoboto.TypeInfo(FindingCriteria),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "rank",
                "Rank",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique ID of the detector that you want to update.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the action that is to be applied to the findings that match the
    # filter.
    action: "FilterAction" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The idempotency token for the create request.
    client_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The description of the filter.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Represents the criteria to be used in the filter for querying findings.
    finding_criteria: "FindingCriteria" = dataclasses.field(
        default_factory=dict,
    )

    # The name of the filter.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the position of the filter in the list of current filters. Also
    # specifies the order in which this filter is applied to the findings.
    rank: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateFilterResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the successfully created filter.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateIPSetRequest(autoboto.ShapeBase):
    """
    CreateIPSet request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "activate",
                "Activate",
                autoboto.TypeInfo(bool),
            ),
            (
                "format",
                "Format",
                autoboto.TypeInfo(IpSetFormat),
            ),
            (
                "location",
                "Location",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the detector that you want to update.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A boolean value that indicates whether GuardDuty is to start using the
    # uploaded IPSet.
    activate: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The format of the file that contains the IPSet.
    format: "IpSetFormat" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URI of the file that contains the IPSet. For example (https://s3.us-
    # west-2.amazonaws.com/my-bucket/my-object-key)
    location: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user friendly name to identify the IPSet. This name is displayed in all
    # findings that are triggered by activity that involves IP addresses included
    # in this IPSet.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateIPSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip_set_id",
                "IpSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier for an IP Set
    ip_set_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateMembersRequest(autoboto.ShapeBase):
    """
    CreateMembers request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "account_details",
                "AccountDetails",
                autoboto.TypeInfo(typing.List[AccountDetail]),
            ),
        ]

    # The unique ID of the detector of the GuardDuty account with which you want
    # to associate member accounts.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of account ID and email address pairs of the accounts that you want
    # to associate with the master GuardDuty account.
    account_details: typing.List["AccountDetail"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateMembersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                autoboto.TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateSampleFindingsRequest(autoboto.ShapeBase):
    """
    CreateSampleFindings request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "finding_types",
                "FindingTypes",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the detector to create sample findings for.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Types of sample findings that you want to generate.
    finding_types: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateSampleFindingsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateThreatIntelSetRequest(autoboto.ShapeBase):
    """
    CreateThreatIntelSet request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "activate",
                "Activate",
                autoboto.TypeInfo(bool),
            ),
            (
                "format",
                "Format",
                autoboto.TypeInfo(ThreatIntelSetFormat),
            ),
            (
                "location",
                "Location",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the detector that you want to update.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A boolean value that indicates whether GuardDuty is to start using the
    # uploaded ThreatIntelSet.
    activate: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The format of the file that contains the ThreatIntelSet.
    format: "ThreatIntelSetFormat" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URI of the file that contains the ThreatIntelSet. For example
    # (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key).
    location: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A user-friendly ThreatIntelSet name that is displayed in all finding
    # generated by activity that involves IP addresses included in this
    # ThreatIntelSet.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateThreatIntelSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "threat_intel_set_id",
                "ThreatIntelSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier for an threat intel set
    threat_intel_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeclineInvitationsRequest(autoboto.ShapeBase):
    """
    DeclineInvitations request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_ids",
                "AccountIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A list of account IDs of the AWS accounts that sent invitations to the
    # current member account that you want to decline invitations from.
    account_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DeclineInvitationsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                autoboto.TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DeleteDetectorRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID that specifies the detector that you want to delete.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteDetectorResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteFilterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "filter_name",
                "FilterName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID that specifies the detector where you want to delete a
    # filter.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the filter.
    filter_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteFilterResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteIPSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "ip_set_id",
                "IpSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The detectorID that specifies the GuardDuty service whose IPSet you want to
    # delete.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID that specifies the IPSet that you want to delete.
    ip_set_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteIPSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteInvitationsRequest(autoboto.ShapeBase):
    """
    DeleteInvitations request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_ids",
                "AccountIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A list of account IDs of the AWS accounts that sent invitations to the
    # current member account that you want to delete invitations from.
    account_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DeleteInvitationsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                autoboto.TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DeleteMembersRequest(autoboto.ShapeBase):
    """
    DeleteMembers request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "account_ids",
                "AccountIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The unique ID of the detector of the GuardDuty account whose members you
    # want to delete.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of account IDs of the GuardDuty member accounts that you want to
    # delete.
    account_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DeleteMembersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                autoboto.TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DeleteThreatIntelSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "threat_intel_set_id",
                "ThreatIntelSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The detectorID that specifies the GuardDuty service whose ThreatIntelSet
    # you want to delete.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID that specifies the ThreatIntelSet that you want to delete.
    threat_intel_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteThreatIntelSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


class DetectorStatus(Enum):
    """
    The status of detector.
    """
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class DisassociateFromMasterAccountRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the detector of the GuardDuty member account.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DisassociateFromMasterAccountResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DisassociateMembersRequest(autoboto.ShapeBase):
    """
    DisassociateMembers request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "account_ids",
                "AccountIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The unique ID of the detector of the GuardDuty account whose members you
    # want to disassociate from master.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of account IDs of the GuardDuty member accounts that you want to
    # disassociate from master.
    account_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DisassociateMembersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                autoboto.TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DnsRequestAction(autoboto.ShapeBase):
    """
    Information about the DNS_REQUEST action described in this finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "Domain",
                autoboto.TypeInfo(str),
            ),
        ]

    # Domain information for the DNS request.
    domain: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DomainDetails(autoboto.ShapeBase):
    """
    Domain information for the AWS API call.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ErrorResponse(autoboto.ShapeBase):
    """
    Error response object.
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
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The error type.
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class Feedback(Enum):
    """
    Finding Feedback Value
    """
    USEFUL = "USEFUL"
    NOT_USEFUL = "NOT_USEFUL"


class FilterAction(Enum):
    """
    The action associated with a filter.
    """
    NOOP = "NOOP"
    ARCHIVE = "ARCHIVE"


@dataclasses.dataclass
class Finding(autoboto.ShapeBase):
    """
    Representation of a abnormal or suspicious activity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "region",
                "Region",
                autoboto.TypeInfo(str),
            ),
            (
                "resource",
                "Resource",
                autoboto.TypeInfo(Resource),
            ),
            (
                "schema_version",
                "SchemaVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "severity",
                "Severity",
                autoboto.TypeInfo(float),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
            (
                "updated_at",
                "UpdatedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "confidence",
                "Confidence",
                autoboto.TypeInfo(float),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "partition",
                "Partition",
                autoboto.TypeInfo(str),
            ),
            (
                "service",
                "Service",
                autoboto.TypeInfo(Service),
            ),
            (
                "title",
                "Title",
                autoboto.TypeInfo(str),
            ),
        ]

    # AWS account ID where the activity occurred that prompted GuardDuty to
    # generate a finding.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ARN of a finding described by the action.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time stamp at which a finding was generated.
    created_at: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The identifier that corresponds to a finding described by the action.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The AWS region where the activity occurred that prompted GuardDuty to
    # generate a finding.
    region: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The AWS resource associated with the activity that prompted GuardDuty to
    # generate a finding.
    resource: "Resource" = dataclasses.field(default_factory=dict, )

    # Findings' schema version.
    schema_version: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The severity of a finding.
    severity: float = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of a finding described by the action.
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time stamp at which a finding was last updated.
    updated_at: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The confidence level of a finding.
    confidence: float = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The description of a finding.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The AWS resource partition.
    partition: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Additional information assigned to the generated finding by GuardDuty.
    service: "Service" = dataclasses.field(default_factory=dict, )

    # The title of a finding.
    title: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class FindingCriteria(autoboto.ShapeBase):
    """
    Represents the criteria used for querying findings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "criterion",
                "Criterion",
                autoboto.TypeInfo(typing.Dict[str, Condition]),
            ),
        ]

    # Represents a map of finding properties that match specified conditions and
    # values when querying findings.
    criterion: typing.Dict[str, "Condition"] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class FindingStatisticType(Enum):
    """
    The types of finding statistics.
    """
    COUNT_BY_SEVERITY = "COUNT_BY_SEVERITY"


@dataclasses.dataclass
class FindingStatistics(autoboto.ShapeBase):
    """
    Finding statistics object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "count_by_severity",
                "CountBySeverity",
                autoboto.TypeInfo(typing.Dict[str, int]),
            ),
        ]

    # Represents a map of severity to count statistic for a set of findings
    count_by_severity: typing.Dict[str, int] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GeoLocation(autoboto.ShapeBase):
    """
    Location information of the remote IP address.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lat",
                "Lat",
                autoboto.TypeInfo(float),
            ),
            (
                "lon",
                "Lon",
                autoboto.TypeInfo(float),
            ),
        ]

    # Latitude information of remote IP address.
    lat: float = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Longitude information of remote IP address.
    lon: float = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDetectorRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the detector that you want to retrieve.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDetectorResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "created_at",
                "CreatedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "service_role",
                "ServiceRole",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(DetectorStatus),
            ),
            (
                "updated_at",
                "UpdatedAt",
                autoboto.TypeInfo(str),
            ),
        ]

    # The first time a resource was created. The format will be ISO-8601.
    created_at: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Customer serviceRole name or ARN for accessing customer resources
    service_role: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of detector.
    status: "DetectorStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The first time a resource was created. The format will be ISO-8601.
    updated_at: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetFilterRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "filter_name",
                "FilterName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The detector ID that specifies the GuardDuty service where you want to list
    # the details of the specified filter.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the filter whose details you want to get.
    filter_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetFilterResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(FilterAction),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "finding_criteria",
                "FindingCriteria",
                autoboto.TypeInfo(FindingCriteria),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "rank",
                "Rank",
                autoboto.TypeInfo(int),
            ),
        ]

    # Specifies the action that is to be applied to the findings that match the
    # filter.
    action: "FilterAction" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The description of the filter.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Represents the criteria to be used in the filter for querying findings.
    finding_criteria: "FindingCriteria" = dataclasses.field(
        default_factory=dict,
    )

    # The name of the filter.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the position of the filter in the list of current filters. Also
    # specifies the order in which this filter is applied to the findings.
    rank: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetFindingsRequest(autoboto.ShapeBase):
    """
    GetFindings request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "finding_ids",
                "FindingIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                autoboto.TypeInfo(SortCriteria),
            ),
        ]

    # The ID of the detector that specifies the GuardDuty service whose findings
    # you want to retrieve.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # IDs of the findings that you want to retrieve.
    finding_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # Represents the criteria used for sorting findings.
    sort_criteria: "SortCriteria" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetFindingsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "findings",
                "Findings",
                autoboto.TypeInfo(typing.List[Finding]),
            ),
        ]

    # A list of findings.
    findings: typing.List["Finding"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class GetFindingsStatisticsRequest(autoboto.ShapeBase):
    """
    GetFindingsStatistics request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "finding_criteria",
                "FindingCriteria",
                autoboto.TypeInfo(FindingCriteria),
            ),
            (
                "finding_statistic_types",
                "FindingStatisticTypes",
                autoboto.TypeInfo(typing.List[FindingStatisticType]),
            ),
        ]

    # The ID of the detector that specifies the GuardDuty service whose findings'
    # statistics you want to retrieve.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Represents the criteria used for querying findings.
    finding_criteria: "FindingCriteria" = dataclasses.field(
        default_factory=dict,
    )

    # Types of finding statistics to retrieve.
    finding_statistic_types: typing.List["FindingStatisticType"
                                        ] = dataclasses.field(
                                            default_factory=list,
                                        )


@dataclasses.dataclass
class GetFindingsStatisticsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "finding_statistics",
                "FindingStatistics",
                autoboto.TypeInfo(FindingStatistics),
            ),
        ]

    # Finding statistics object.
    finding_statistics: "FindingStatistics" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetIPSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "ip_set_id",
                "IpSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The detectorID that specifies the GuardDuty service whose IPSet you want to
    # retrieve.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID that specifies the IPSet that you want to describe.
    ip_set_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetIPSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "format",
                "Format",
                autoboto.TypeInfo(IpSetFormat),
            ),
            (
                "location",
                "Location",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(IpSetStatus),
            ),
        ]

    # The format of the file that contains the IPSet.
    format: "IpSetFormat" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URI of the file that contains the IPSet. For example (https://s3.us-
    # west-2.amazonaws.com/my-bucket/my-object-key)
    location: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The user friendly name to identify the IPSet. This name is displayed in all
    # findings that are triggered by activity that involves IP addresses included
    # in this IPSet.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of ipSet file uploaded.
    status: "IpSetStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetInvitationsCountRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetInvitationsCountResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "invitations_count",
                "InvitationsCount",
                autoboto.TypeInfo(int),
            ),
        ]

    # The number of received invitations.
    invitations_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetMasterAccountRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the detector of the GuardDuty member account.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetMasterAccountResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "master",
                "Master",
                autoboto.TypeInfo(Master),
            ),
        ]

    # Contains details about the master account.
    master: "Master" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetMembersRequest(autoboto.ShapeBase):
    """
    GetMembers request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "account_ids",
                "AccountIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The unique ID of the detector of the GuardDuty account whose members you
    # want to retrieve.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of account IDs of the GuardDuty member accounts that you want to
    # describe.
    account_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class GetMembersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "members",
                "Members",
                autoboto.TypeInfo(typing.List[Member]),
            ),
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                autoboto.TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    # A list of member descriptions.
    members: typing.List["Member"] = dataclasses.field(default_factory=list, )

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetThreatIntelSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "threat_intel_set_id",
                "ThreatIntelSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The detectorID that specifies the GuardDuty service whose ThreatIntelSet
    # you want to describe.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID that specifies the ThreatIntelSet that you want to describe.
    threat_intel_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetThreatIntelSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "format",
                "Format",
                autoboto.TypeInfo(ThreatIntelSetFormat),
            ),
            (
                "location",
                "Location",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(ThreatIntelSetStatus),
            ),
        ]

    # The format of the threatIntelSet.
    format: "ThreatIntelSetFormat" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URI of the file that contains the ThreatIntelSet. For example
    # (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key).
    location: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A user-friendly ThreatIntelSet name that is displayed in all finding
    # generated by activity that involves IP addresses included in this
    # ThreatIntelSet.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of threatIntelSet file uploaded.
    status: "ThreatIntelSetStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class IamInstanceProfile(autoboto.ShapeBase):
    """
    The profile information of the EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # AWS EC2 instance profile ARN.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # AWS EC2 instance profile ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InstanceDetails(autoboto.ShapeBase):
    """
    The information about the EC2 instance associated with the activity that
    prompted GuardDuty to generate a finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "availability_zone",
                "AvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "iam_instance_profile",
                "IamInstanceProfile",
                autoboto.TypeInfo(IamInstanceProfile),
            ),
            (
                "image_description",
                "ImageDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "image_id",
                "ImageId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_state",
                "InstanceState",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                autoboto.TypeInfo(str),
            ),
            (
                "launch_time",
                "LaunchTime",
                autoboto.TypeInfo(str),
            ),
            (
                "network_interfaces",
                "NetworkInterfaces",
                autoboto.TypeInfo(typing.List[NetworkInterface]),
            ),
            (
                "platform",
                "Platform",
                autoboto.TypeInfo(str),
            ),
            (
                "product_codes",
                "ProductCodes",
                autoboto.TypeInfo(typing.List[ProductCode]),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The availability zone of the EC2 instance.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The profile information of the EC2 instance.
    iam_instance_profile: "IamInstanceProfile" = dataclasses.field(
        default_factory=dict,
    )

    # The image description of the EC2 instance.
    image_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The image ID of the EC2 instance.
    image_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the EC2 instance.
    instance_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The state of the EC2 instance.
    instance_state: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of the EC2 instance.
    instance_type: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The launch time of the EC2 instance.
    launch_time: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The network interface information of the EC2 instance.
    network_interfaces: typing.List["NetworkInterface"] = dataclasses.field(
        default_factory=list,
    )

    # The platform of the EC2 instance.
    platform: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The product code of the EC2 instance.
    product_codes: typing.List["ProductCode"] = dataclasses.field(
        default_factory=list,
    )

    # The tags of the EC2 instance.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class InternalServerErrorException(autoboto.ShapeBase):
    """
    Error response object.
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
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
        ]

    # The error message.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The error type.
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Invitation(autoboto.ShapeBase):
    """
    Invitation from an AWS account to become the current account's master.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "invitation_id",
                "InvitationId",
                autoboto.TypeInfo(str),
            ),
            (
                "invited_at",
                "InvitedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "relationship_status",
                "RelationshipStatus",
                autoboto.TypeInfo(str),
            ),
        ]

    # Inviter account ID
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # This value is used to validate the inviter account to the member account.
    invitation_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Timestamp at which the invitation was sent
    invited_at: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the relationship between the inviter and invitee accounts.
    relationship_status: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class InviteMembersRequest(autoboto.ShapeBase):
    """
    InviteMembers request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "account_ids",
                "AccountIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "disable_email_notification",
                "DisableEmailNotification",
                autoboto.TypeInfo(bool),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the detector of the GuardDuty account with which you want
    # to invite members.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of account IDs of the accounts that you want to invite to GuardDuty
    # as members.
    account_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # A boolean value that specifies whether you want to disable email
    # notification to the accounts that you’re inviting to GuardDuty as members.
    disable_email_notification: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The invitation message that you want to send to the accounts that you’re
    # inviting to GuardDuty as members.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InviteMembersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                autoboto.TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default_factory=list,
    )


class IpSetFormat(Enum):
    """
    The format of the ipSet.
    """
    TXT = "TXT"
    STIX = "STIX"
    OTX_CSV = "OTX_CSV"
    ALIEN_VAULT = "ALIEN_VAULT"
    PROOF_POINT = "PROOF_POINT"
    FIRE_EYE = "FIRE_EYE"


class IpSetStatus(Enum):
    """
    The status of ipSet file uploaded.
    """
    INACTIVE = "INACTIVE"
    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    DEACTIVATING = "DEACTIVATING"
    ERROR = "ERROR"
    DELETE_PENDING = "DELETE_PENDING"
    DELETED = "DELETED"


@dataclasses.dataclass
class ListDetectorsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # You can use this parameter to indicate the maximum number of detectors that
    # you want in the response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the ListDetectors action. For
    # subsequent calls to the action fill nextToken in the request with the value
    # of nextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListDetectorsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_ids",
                "DetectorIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of detector Ids.
    detector_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the list action. For subsequent
    # calls to the action fill nextToken in the request with the value of
    # NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListFiltersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
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

    # The ID of the detector that specifies the GuardDuty service where you want
    # to list filters.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Indicates the maximum number of items that you want in the response. The
    # maximum value is 50.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Paginates results. Set the value of this parameter to NULL on your first
    # call to the ListFilters operation.For subsequent calls to the operation,
    # fill nextToken in the request with the value of nextToken from the previous
    # response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListFiltersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter_names",
                "FilterNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of filter names
    filter_names: typing.List[str] = dataclasses.field(default_factory=list, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the list action. For subsequent
    # calls to the action fill nextToken in the request with the value of
    # NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListFindingsRequest(autoboto.ShapeBase):
    """
    ListFindings request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "finding_criteria",
                "FindingCriteria",
                autoboto.TypeInfo(FindingCriteria),
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
            (
                "sort_criteria",
                "SortCriteria",
                autoboto.TypeInfo(SortCriteria),
            ),
        ]

    # The ID of the detector that specifies the GuardDuty service whose findings
    # you want to list.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Represents the criteria used for querying findings.
    finding_criteria: "FindingCriteria" = dataclasses.field(
        default_factory=dict,
    )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 50. The maximum value is 50.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the ListFindings action. For
    # subsequent calls to the action fill nextToken in the request with the value
    # of nextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Represents the criteria used for sorting findings.
    sort_criteria: "SortCriteria" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ListFindingsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "finding_ids",
                "FindingIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of the Findings.
    finding_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the list action. For subsequent
    # calls to the action fill nextToken in the request with the value of
    # NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListIPSetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
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

    # The unique ID of the detector that you want to retrieve.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # You can use this parameter to indicate the maximum number of items that you
    # want in the response. The default value is 7. The maximum value is 7.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the ListIPSet action. For
    # subsequent calls to the action fill nextToken in the request with the value
    # of NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListIPSetsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip_set_ids",
                "IpSetIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of the IP set IDs
    ip_set_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the list action. For subsequent
    # calls to the action fill nextToken in the request with the value of
    # NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListInvitationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # You can use this parameter to indicate the maximum number of invitations
    # you want in the response. The default value is 50. The maximum value is 50.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the ListInvitations action.
    # Subsequent calls to the action fill nextToken in the request with the value
    # of NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListInvitationsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "invitations",
                "Invitations",
                autoboto.TypeInfo(typing.List[Invitation]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of invitation descriptions.
    invitations: typing.List["Invitation"] = dataclasses.field(
        default_factory=list,
    )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the list action. For subsequent
    # calls to the action fill nextToken in the request with the value of
    # NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListMembersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
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
            (
                "only_associated",
                "OnlyAssociated",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the detector of the GuardDuty account whose members you
    # want to list.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 1. The maximum value is 50.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the ListMembers action. Subsequent
    # calls to the action fill nextToken in the request with the value of
    # NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies what member accounts the response is to include based on their
    # relationship status with the master account. The default value is TRUE. If
    # onlyAssociated is set to TRUE, the response will include member accounts
    # whose relationship status with the master is set to Enabled, Disabled. If
    # onlyAssociated is set to FALSE, the response will include all existing
    # member accounts.
    only_associated: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListMembersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "members",
                "Members",
                autoboto.TypeInfo(typing.List[Member]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of member descriptions.
    members: typing.List["Member"] = dataclasses.field(default_factory=list, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the list action. For subsequent
    # calls to the action fill nextToken in the request with the value of
    # NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListThreatIntelSetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
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

    # The detectorID that specifies the GuardDuty service whose ThreatIntelSets
    # you want to list.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # You can use this parameter to indicate the maximum number of items that you
    # want in the response. The default value is 7. The maximum value is 7.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Pagination token to start retrieving threat intel sets from.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListThreatIntelSetsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "threat_intel_set_ids",
                "ThreatIntelSetIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the list action. For subsequent
    # calls to the action fill nextToken in the request with the value of
    # NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The list of the threat intel set IDs
    threat_intel_set_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class LocalPortDetails(autoboto.ShapeBase):
    """
    Local port information of the connection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "port",
                "Port",
                autoboto.TypeInfo(int),
            ),
            (
                "port_name",
                "PortName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Port number of the local connection.
    port: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Port name of the local connection.
    port_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Master(autoboto.ShapeBase):
    """
    Contains details about the master account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "invitation_id",
                "InvitationId",
                autoboto.TypeInfo(str),
            ),
            (
                "invited_at",
                "InvitedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "relationship_status",
                "RelationshipStatus",
                autoboto.TypeInfo(str),
            ),
        ]

    # Master account ID
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # This value is used to validate the master account to the member account.
    invitation_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Timestamp at which the invitation was sent
    invited_at: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the relationship between the master and member accounts.
    relationship_status: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Member(autoboto.ShapeBase):
    """
    Contains details about the member account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "email",
                "Email",
                autoboto.TypeInfo(str),
            ),
            (
                "master_id",
                "MasterId",
                autoboto.TypeInfo(str),
            ),
            (
                "relationship_status",
                "RelationshipStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "updated_at",
                "UpdatedAt",
                autoboto.TypeInfo(str),
            ),
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "invited_at",
                "InvitedAt",
                autoboto.TypeInfo(str),
            ),
        ]

    # AWS account ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Member account's email address.
    email: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The master account ID.
    master_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of the relationship between the member and the master.
    relationship_status: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The first time a resource was created. The format will be ISO-8601.
    updated_at: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique identifier for a detector.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Timestamp at which the invitation was sent
    invited_at: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class NetworkConnectionAction(autoboto.ShapeBase):
    """
    Information about the NETWORK_CONNECTION action described in this finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "blocked",
                "Blocked",
                autoboto.TypeInfo(bool),
            ),
            (
                "connection_direction",
                "ConnectionDirection",
                autoboto.TypeInfo(str),
            ),
            (
                "local_port_details",
                "LocalPortDetails",
                autoboto.TypeInfo(LocalPortDetails),
            ),
            (
                "protocol",
                "Protocol",
                autoboto.TypeInfo(str),
            ),
            (
                "remote_ip_details",
                "RemoteIpDetails",
                autoboto.TypeInfo(RemoteIpDetails),
            ),
            (
                "remote_port_details",
                "RemotePortDetails",
                autoboto.TypeInfo(RemotePortDetails),
            ),
        ]

    # Network connection blocked information.
    blocked: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Network connection direction.
    connection_direction: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Local port information of the connection.
    local_port_details: "LocalPortDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Network connection protocol.
    protocol: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Remote IP information of the connection.
    remote_ip_details: "RemoteIpDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Remote port information of the connection.
    remote_port_details: "RemotePortDetails" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class NetworkInterface(autoboto.ShapeBase):
    """
    The network interface information of the EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ipv6_addresses",
                "Ipv6Addresses",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "network_interface_id",
                "NetworkInterfaceId",
                autoboto.TypeInfo(str),
            ),
            (
                "private_dns_name",
                "PrivateDnsName",
                autoboto.TypeInfo(str),
            ),
            (
                "private_ip_address",
                "PrivateIpAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "private_ip_addresses",
                "PrivateIpAddresses",
                autoboto.TypeInfo(typing.List[PrivateIpAddressDetails]),
            ),
            (
                "public_dns_name",
                "PublicDnsName",
                autoboto.TypeInfo(str),
            ),
            (
                "public_ip",
                "PublicIp",
                autoboto.TypeInfo(str),
            ),
            (
                "security_groups",
                "SecurityGroups",
                autoboto.TypeInfo(typing.List[SecurityGroup]),
            ),
            (
                "subnet_id",
                "SubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of EC2 instance IPv6 address information.
    ipv6_addresses: typing.List[str] = dataclasses.field(default_factory=list, )

    # The ID of the network interface
    network_interface_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Private DNS name of the EC2 instance.
    private_dns_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Private IP address of the EC2 instance.
    private_ip_address: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Other private IP address information of the EC2 instance.
    private_ip_addresses: typing.List["PrivateIpAddressDetails"
                                     ] = dataclasses.field(
                                         default_factory=list,
                                     )

    # Public DNS name of the EC2 instance.
    public_dns_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Public IP address of the EC2 instance.
    public_ip: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Security groups associated with the EC2 instance.
    security_groups: typing.List["SecurityGroup"] = dataclasses.field(
        default_factory=list,
    )

    # The subnet ID of the EC2 instance.
    subnet_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The VPC ID of the EC2 instance.
    vpc_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class OrderBy(Enum):
    ASC = "ASC"
    DESC = "DESC"


@dataclasses.dataclass
class Organization(autoboto.ShapeBase):
    """
    ISP Organization information of the remote IP address.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "asn",
                "Asn",
                autoboto.TypeInfo(str),
            ),
            (
                "asn_org",
                "AsnOrg",
                autoboto.TypeInfo(str),
            ),
            (
                "isp",
                "Isp",
                autoboto.TypeInfo(str),
            ),
            (
                "org",
                "Org",
                autoboto.TypeInfo(str),
            ),
        ]

    # Autonomous system number of the internet provider of the remote IP address.
    asn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Organization that registered this ASN.
    asn_org: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # ISP information for the internet provider.
    isp: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Name of the internet provider.
    org: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PortProbeAction(autoboto.ShapeBase):
    """
    Information about the PORT_PROBE action described in this finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "blocked",
                "Blocked",
                autoboto.TypeInfo(bool),
            ),
            (
                "port_probe_details",
                "PortProbeDetails",
                autoboto.TypeInfo(typing.List[PortProbeDetail]),
            ),
        ]

    # Port probe blocked information.
    blocked: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of port probe details objects.
    port_probe_details: typing.List["PortProbeDetail"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class PortProbeDetail(autoboto.ShapeBase):
    """
    Details about the port probe finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "local_port_details",
                "LocalPortDetails",
                autoboto.TypeInfo(LocalPortDetails),
            ),
            (
                "remote_ip_details",
                "RemoteIpDetails",
                autoboto.TypeInfo(RemoteIpDetails),
            ),
        ]

    # Local port information of the connection.
    local_port_details: "LocalPortDetails" = dataclasses.field(
        default_factory=dict,
    )

    # Remote IP information of the connection.
    remote_ip_details: "RemoteIpDetails" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PrivateIpAddressDetails(autoboto.ShapeBase):
    """
    Other private IP address information of the EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "private_dns_name",
                "PrivateDnsName",
                autoboto.TypeInfo(str),
            ),
            (
                "private_ip_address",
                "PrivateIpAddress",
                autoboto.TypeInfo(str),
            ),
        ]

    # Private DNS name of the EC2 instance.
    private_dns_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Private IP address of the EC2 instance.
    private_ip_address: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ProductCode(autoboto.ShapeBase):
    """
    The product code of the EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                autoboto.TypeInfo(str),
            ),
            (
                "product_type",
                "ProductType",
                autoboto.TypeInfo(str),
            ),
        ]

    # Product code information.
    code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Product code type.
    product_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RemoteIpDetails(autoboto.ShapeBase):
    """
    Remote IP information of the connection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "city",
                "City",
                autoboto.TypeInfo(City),
            ),
            (
                "country",
                "Country",
                autoboto.TypeInfo(Country),
            ),
            (
                "geo_location",
                "GeoLocation",
                autoboto.TypeInfo(GeoLocation),
            ),
            (
                "ip_address_v4",
                "IpAddressV4",
                autoboto.TypeInfo(str),
            ),
            (
                "organization",
                "Organization",
                autoboto.TypeInfo(Organization),
            ),
        ]

    # City information of the remote IP address.
    city: "City" = dataclasses.field(default_factory=dict, )

    # Country code of the remote IP address.
    country: "Country" = dataclasses.field(default_factory=dict, )

    # Location information of the remote IP address.
    geo_location: "GeoLocation" = dataclasses.field(default_factory=dict, )

    # IPV4 remote address of the connection.
    ip_address_v4: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # ISP Organization information of the remote IP address.
    organization: "Organization" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class RemotePortDetails(autoboto.ShapeBase):
    """
    Remote port information of the connection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "port",
                "Port",
                autoboto.TypeInfo(int),
            ),
            (
                "port_name",
                "PortName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Port number of the remote connection.
    port: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Port name of the remote connection.
    port_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Resource(autoboto.ShapeBase):
    """
    The AWS resource associated with the activity that prompted GuardDuty to
    generate a finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_key_details",
                "AccessKeyDetails",
                autoboto.TypeInfo(AccessKeyDetails),
            ),
            (
                "instance_details",
                "InstanceDetails",
                autoboto.TypeInfo(InstanceDetails),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(str),
            ),
        ]

    # The IAM access key details (IAM user information) of a user that engaged in
    # the activity that prompted GuardDuty to generate a finding.
    access_key_details: "AccessKeyDetails" = dataclasses.field(
        default_factory=dict,
    )

    # The information about the EC2 instance associated with the activity that
    # prompted GuardDuty to generate a finding.
    instance_details: "InstanceDetails" = dataclasses.field(
        default_factory=dict,
    )

    # The type of the AWS resource.
    resource_type: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SecurityGroup(autoboto.ShapeBase):
    """
    Security groups associated with the EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "group_name",
                "GroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # EC2 instance's security group ID.
    group_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # EC2 instance's security group name.
    group_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Service(autoboto.ShapeBase):
    """
    Additional information assigned to the generated finding by GuardDuty.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(Action),
            ),
            (
                "archived",
                "Archived",
                autoboto.TypeInfo(bool),
            ),
            (
                "count",
                "Count",
                autoboto.TypeInfo(int),
            ),
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "event_first_seen",
                "EventFirstSeen",
                autoboto.TypeInfo(str),
            ),
            (
                "event_last_seen",
                "EventLastSeen",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_role",
                "ResourceRole",
                autoboto.TypeInfo(str),
            ),
            (
                "service_name",
                "ServiceName",
                autoboto.TypeInfo(str),
            ),
            (
                "user_feedback",
                "UserFeedback",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the activity described in a finding.
    action: "Action" = dataclasses.field(default_factory=dict, )

    # Indicates whether this finding is archived.
    archived: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Total count of the occurrences of this finding type.
    count: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Detector ID for the GuardDuty service.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # First seen timestamp of the activity that prompted GuardDuty to generate
    # this finding.
    event_first_seen: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Last seen timestamp of the activity that prompted GuardDuty to generate
    # this finding.
    event_last_seen: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Resource role information for this finding.
    resource_role: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the AWS service (GuardDuty) that generated a finding.
    service_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Feedback left about the finding.
    user_feedback: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SortCriteria(autoboto.ShapeBase):
    """
    Represents the criteria used for sorting findings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_name",
                "AttributeName",
                autoboto.TypeInfo(str),
            ),
            (
                "order_by",
                "OrderBy",
                autoboto.TypeInfo(OrderBy),
            ),
        ]

    # Represents the finding attribute (for example, accountId) by which to sort
    # findings.
    attribute_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Order by which the sorted findings are to be displayed.
    order_by: "OrderBy" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class StartMonitoringMembersRequest(autoboto.ShapeBase):
    """
    StartMonitoringMembers request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "account_ids",
                "AccountIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The unique ID of the detector of the GuardDuty account whom you want to re-
    # enable to monitor members' findings.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of account IDs of the GuardDuty member accounts whose findings you
    # want the master account to monitor.
    account_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class StartMonitoringMembersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                autoboto.TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class StopMonitoringMembersRequest(autoboto.ShapeBase):
    """
    StopMonitoringMembers request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "account_ids",
                "AccountIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The unique ID of the detector of the GuardDuty account that you want to
    # stop from monitor members' findings.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of account IDs of the GuardDuty member accounts whose findings you
    # want the master account to stop monitoring.
    account_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class StopMonitoringMembersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                autoboto.TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    """
    A tag of the EC2 instance.
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

    # EC2 instance tag key.
    key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # EC2 instance tag value.
    value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class ThreatIntelSetFormat(Enum):
    """
    The format of the threatIntelSet.
    """
    TXT = "TXT"
    STIX = "STIX"
    OTX_CSV = "OTX_CSV"
    ALIEN_VAULT = "ALIEN_VAULT"
    PROOF_POINT = "PROOF_POINT"
    FIRE_EYE = "FIRE_EYE"


class ThreatIntelSetStatus(Enum):
    """
    The status of threatIntelSet file uploaded.
    """
    INACTIVE = "INACTIVE"
    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    DEACTIVATING = "DEACTIVATING"
    ERROR = "ERROR"
    DELETE_PENDING = "DELETE_PENDING"
    DELETED = "DELETED"


@dataclasses.dataclass
class UnarchiveFindingsRequest(autoboto.ShapeBase):
    """
    UnarchiveFindings request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "finding_ids",
                "FindingIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the detector that specifies the GuardDuty service whose findings
    # you want to unarchive.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # IDs of the findings that you want to unarchive.
    finding_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UnarchiveFindingsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UnprocessedAccount(autoboto.ShapeBase):
    """
    An object containing the unprocessed account and a result string explaining why
    it was unprocessed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "result",
                "Result",
                autoboto.TypeInfo(str),
            ),
        ]

    # AWS Account ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A reason why the account hasn't been processed.
    result: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateDetectorRequest(autoboto.ShapeBase):
    """
    UpdateDetector request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "enable",
                "Enable",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The unique ID of the detector that you want to update.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Updated boolean value for the detector that specifies whether the detector
    # is enabled.
    enable: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateDetectorResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateFilterRequest(autoboto.ShapeBase):
    """
    UpdateFilterRequest request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "filter_name",
                "FilterName",
                autoboto.TypeInfo(str),
            ),
            (
                "action",
                "Action",
                autoboto.TypeInfo(FilterAction),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "finding_criteria",
                "FindingCriteria",
                autoboto.TypeInfo(FindingCriteria),
            ),
            (
                "rank",
                "Rank",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique ID of the detector that specifies the GuardDuty service where
    # you want to update a filter.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the filter.
    filter_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the action that is to be applied to the findings that match the
    # filter.
    action: "FilterAction" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The description of the filter.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Represents the criteria to be used in the filter for querying findings.
    finding_criteria: "FindingCriteria" = dataclasses.field(
        default_factory=dict,
    )

    # Specifies the position of the filter in the list of current filters. Also
    # specifies the order in which this filter is applied to the findings.
    rank: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateFilterResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the filter.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateFindingsFeedbackRequest(autoboto.ShapeBase):
    """
    UpdateFindingsFeedback request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "comments",
                "Comments",
                autoboto.TypeInfo(str),
            ),
            (
                "feedback",
                "Feedback",
                autoboto.TypeInfo(Feedback),
            ),
            (
                "finding_ids",
                "FindingIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the detector that specifies the GuardDuty service whose findings
    # you want to mark as useful or not useful.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Additional feedback about the GuardDuty findings.
    comments: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Valid values: USEFUL | NOT_USEFUL
    feedback: "Feedback" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # IDs of the findings that you want to mark as useful or not useful.
    finding_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UpdateFindingsFeedbackResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateIPSetRequest(autoboto.ShapeBase):
    """
    UpdateIPSet request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "ip_set_id",
                "IpSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "activate",
                "Activate",
                autoboto.TypeInfo(bool),
            ),
            (
                "location",
                "Location",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The detectorID that specifies the GuardDuty service whose IPSet you want to
    # update.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID that specifies the IPSet that you want to update.
    ip_set_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The updated boolean value that specifies whether the IPSet is active or
    # not.
    activate: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The updated URI of the file that contains the IPSet. For example
    # (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key).
    location: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID that specifies the IPSet that you want to update.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateIPSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateThreatIntelSetRequest(autoboto.ShapeBase):
    """
    UpdateThreatIntelSet request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                autoboto.TypeInfo(str),
            ),
            (
                "threat_intel_set_id",
                "ThreatIntelSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "activate",
                "Activate",
                autoboto.TypeInfo(bool),
            ),
            (
                "location",
                "Location",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The detectorID that specifies the GuardDuty service whose ThreatIntelSet
    # you want to update.
    detector_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID that specifies the ThreatIntelSet that you want to update.
    threat_intel_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The updated boolean value that specifies whether the ThreateIntelSet is
    # active or not.
    activate: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The updated URI of the file that contains the ThreateIntelSet. For example
    # (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key)
    location: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique ID that specifies the ThreatIntelSet that you want to update.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateThreatIntelSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []
