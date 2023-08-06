import datetime
import typing
import autoboto
import botocore.response
from enum import Enum
import dataclasses


@dataclasses.dataclass
class ActivatedRule(autoboto.ShapeBase):
    """
    The `ActivatedRule` object in an UpdateWebACL request specifies a `Rule` that
    you want to insert or delete, the priority of the `Rule` in the `WebACL`, and
    the action that you want AWS WAF to take when a web request matches the `Rule`
    (`ALLOW`, `BLOCK`, or `COUNT`).

    To specify whether to insert or delete a `Rule`, use the `Action` parameter in
    the WebACLUpdate data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "priority",
                "Priority",
                autoboto.TypeInfo(int),
            ),
            (
                "rule_id",
                "RuleId",
                autoboto.TypeInfo(str),
            ),
            (
                "action",
                "Action",
                autoboto.TypeInfo(WafAction),
            ),
            (
                "override_action",
                "OverrideAction",
                autoboto.TypeInfo(WafOverrideAction),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(WafRuleType),
            ),
        ]

    # Specifies the order in which the `Rules` in a `WebACL` are evaluated. Rules
    # with a lower value for `Priority` are evaluated before `Rules` with a
    # higher value. The value must be a unique integer. If you add multiple
    # `Rules` to a `WebACL`, the values don't need to be consecutive.
    priority: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The `RuleId` for a `Rule`. You use `RuleId` to get more information about a
    # `Rule` (see GetRule), update a `Rule` (see UpdateRule), insert a `Rule`
    # into a `WebACL` or delete a one from a `WebACL` (see UpdateWebACL), or
    # delete a `Rule` from AWS WAF (see DeleteRule).

    # `RuleId` is returned by CreateRule and by ListRules.
    rule_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the action that CloudFront or AWS WAF takes when a web request
    # matches the conditions in the `Rule`. Valid values for `Action` include the
    # following:

    #   * `ALLOW`: CloudFront responds with the requested object.

    #   * `BLOCK`: CloudFront responds with an HTTP 403 (Forbidden) status code.

    #   * `COUNT`: AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.

    # `ActivatedRule|OverrideAction` applies only when updating or adding a
    # `RuleGroup` to a `WebACL`. In this case you do not use
    # `ActivatedRule|Action`. For all other update requests,
    # `ActivatedRule|Action` is used instead of `ActivatedRule|OverrideAction`.
    action: "WafAction" = dataclasses.field(default_factory=dict, )

    # Use the `OverrideAction` to test your `RuleGroup`.

    # Any rule in a `RuleGroup` can potentially block a request. If you set the
    # `OverrideAction` to `None`, the `RuleGroup` will block a request if any
    # individual rule in the `RuleGroup` matches the request and is configured to
    # block that request. However if you first want to test the `RuleGroup`, set
    # the `OverrideAction` to `Count`. The `RuleGroup` will then override any
    # block action specified by individual rules contained within the group.
    # Instead of blocking matching requests, those requests will be counted. You
    # can view a record of counted requests using GetSampledRequests.

    # `ActivatedRule|OverrideAction` applies only when updating or adding a
    # `RuleGroup` to a `WebACL`. In this case you do not use
    # `ActivatedRule|Action`. For all other update requests,
    # `ActivatedRule|Action` is used instead of `ActivatedRule|OverrideAction`.
    override_action: "WafOverrideAction" = dataclasses.field(
        default_factory=dict,
    )

    # The rule type, either `REGULAR`, as defined by Rule, `RATE_BASED`, as
    # defined by RateBasedRule, or `GROUP`, as defined by RuleGroup. The default
    # is REGULAR. Although this field is optional, be aware that if you try to
    # add a RATE_BASED rule to a web ACL without setting the type, the
    # UpdateWebACL request will fail because the request tries to add a REGULAR
    # rule with the specified ID, which does not exist.
    type: "WafRuleType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ByteMatchSet(autoboto.ShapeBase):
    """
    In a GetByteMatchSet request, `ByteMatchSet` is a complex type that contains the
    `ByteMatchSetId` and `Name` of a `ByteMatchSet`, and the values that you
    specified when you updated the `ByteMatchSet`.

    A complex type that contains `ByteMatchTuple` objects, which specify the parts
    of web requests that you want AWS WAF to inspect and the values that you want
    AWS WAF to search for. If a `ByteMatchSet` contains more than one
    `ByteMatchTuple` object, a request needs to match the settings in only one
    `ByteMatchTuple` to be considered a match.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "byte_match_set_id",
                "ByteMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "byte_match_tuples",
                "ByteMatchTuples",
                autoboto.TypeInfo(typing.List[ByteMatchTuple]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ByteMatchSetId` for a `ByteMatchSet`. You use `ByteMatchSetId` to get
    # information about a `ByteMatchSet` (see GetByteMatchSet), update a
    # `ByteMatchSet` (see UpdateByteMatchSet), insert a `ByteMatchSet` into a
    # `Rule` or delete one from a `Rule` (see UpdateRule), and delete a
    # `ByteMatchSet` from AWS WAF (see DeleteByteMatchSet).

    # `ByteMatchSetId` is returned by CreateByteMatchSet and by
    # ListByteMatchSets.
    byte_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the bytes (typically a string that corresponds with ASCII
    # characters) that you want AWS WAF to search for in web requests, the
    # location in requests that you want AWS WAF to search, and other settings.
    byte_match_tuples: typing.List["ByteMatchTuple"] = dataclasses.field(
        default_factory=list,
    )

    # A friendly name or description of the ByteMatchSet. You can't change `Name`
    # after you create a `ByteMatchSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ByteMatchSetSummary(autoboto.ShapeBase):
    """
    Returned by ListByteMatchSets. Each `ByteMatchSetSummary` object includes the
    `Name` and `ByteMatchSetId` for one ByteMatchSet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "byte_match_set_id",
                "ByteMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ByteMatchSetId` for a `ByteMatchSet`. You use `ByteMatchSetId` to get
    # information about a `ByteMatchSet`, update a `ByteMatchSet`, remove a
    # `ByteMatchSet` from a `Rule`, and delete a `ByteMatchSet` from AWS WAF.

    # `ByteMatchSetId` is returned by CreateByteMatchSet and by
    # ListByteMatchSets.
    byte_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A friendly name or description of the ByteMatchSet. You can't change `Name`
    # after you create a `ByteMatchSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ByteMatchSetUpdate(autoboto.ShapeBase):
    """
    In an UpdateByteMatchSet request, `ByteMatchSetUpdate` specifies whether to
    insert or delete a ByteMatchTuple and includes the settings for the
    `ByteMatchTuple`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(ChangeAction),
            ),
            (
                "byte_match_tuple",
                "ByteMatchTuple",
                autoboto.TypeInfo(ByteMatchTuple),
            ),
        ]

    # Specifies whether to insert or delete a ByteMatchTuple.
    action: "ChangeAction" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the part of a web request that you want AWS WAF to
    # inspect and the value that you want AWS WAF to search for. If you specify
    # `DELETE` for the value of `Action`, the `ByteMatchTuple` values must
    # exactly match the values in the `ByteMatchTuple` that you want to delete
    # from the `ByteMatchSet`.
    byte_match_tuple: "ByteMatchTuple" = dataclasses.field(
        default_factory=dict,
    )


class ByteMatchTargetString(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class ByteMatchTuple(autoboto.ShapeBase):
    """
    The bytes (typically a string that corresponds with ASCII characters) that you
    want AWS WAF to search for in web requests, the location in requests that you
    want AWS WAF to search, and other settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_to_match",
                "FieldToMatch",
                autoboto.TypeInfo(FieldToMatch),
            ),
            (
                "target_string",
                "TargetString",
                autoboto.TypeInfo(typing.Any),
            ),
            (
                "text_transformation",
                "TextTransformation",
                autoboto.TypeInfo(TextTransformation),
            ),
            (
                "positional_constraint",
                "PositionalConstraint",
                autoboto.TypeInfo(PositionalConstraint),
            ),
        ]

    # The part of a web request that you want AWS WAF to search, such as a
    # specified header or a query string. For more information, see FieldToMatch.
    field_to_match: "FieldToMatch" = dataclasses.field(default_factory=dict, )

    # The value that you want AWS WAF to search for. AWS WAF searches for the
    # specified string in the part of web requests that you specified in
    # `FieldToMatch`. The maximum length of the value is 50 bytes.

    # Valid values depend on the values that you specified for `FieldToMatch`:

    #   * `HEADER`: The value that you want AWS WAF to search for in the request header that you specified in FieldToMatch, for example, the value of the `User-Agent` or `Referer` header.

    #   * `METHOD`: The HTTP method, which indicates the type of operation specified in the request. CloudFront supports the following methods: `DELETE`, `GET`, `HEAD`, `OPTIONS`, `PATCH`, `POST`, and `PUT`.

    #   * `QUERY_STRING`: The value that you want AWS WAF to search for in the query string, which is the part of a URL that appears after a `?` character.

    #   * `URI`: The value that you want AWS WAF to search for in the part of a URL that identifies a resource, for example, `/images/daily-ad.jpg`.

    #   * `BODY`: The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first `8192` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet.

    # If `TargetString` includes alphabetic characters A-Z and a-z, note that the
    # value is case sensitive.

    # **If you're using the AWS WAF API**

    # Specify a base64-encoded version of the value. The maximum length of the
    # value before you base64-encode it is 50 bytes.

    # For example, suppose the value of `Type` is `HEADER` and the value of
    # `Data` is `User-Agent`. If you want to search the `User-Agent` header for
    # the value `BadBot`, you base64-encode `BadBot` using MIME base64 encoding
    # and include the resulting value, `QmFkQm90`, in the value of
    # `TargetString`.

    # **If you're using the AWS CLI or one of the AWS SDKs**

    # The value that you want AWS WAF to search for. The SDK automatically base64
    # encodes the value.
    target_string: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Text transformations eliminate some of the unusual formatting that
    # attackers use in web requests in an effort to bypass AWS WAF. If you
    # specify a transformation, AWS WAF performs the transformation on
    # `TargetString` before inspecting a request for a match.

    # **CMD_LINE**

    # When you're concerned that attackers are injecting an operating system
    # commandline command and using unusual formatting to disguise some or all of
    # the command, use this option to perform the following transformations:

    #   * Delete the following characters: \ " ' ^

    #   * Delete spaces before the following characters: / (

    #   * Replace the following characters with a space: , ;

    #   * Replace multiple spaces with one space

    #   * Convert uppercase letters (A-Z) to lowercase (a-z)

    # **COMPRESS_WHITE_SPACE**

    # Use this option to replace the following characters with a space character
    # (decimal 32):

    #   * \f, formfeed, decimal 12

    #   * \t, tab, decimal 9

    #   * \n, newline, decimal 10

    #   * \r, carriage return, decimal 13

    #   * \v, vertical tab, decimal 11

    #   * non-breaking space, decimal 160

    # `COMPRESS_WHITE_SPACE` also replaces multiple spaces with one space.

    # **HTML_ENTITY_DECODE**

    # Use this option to replace HTML-encoded characters with unencoded
    # characters. `HTML_ENTITY_DECODE` performs the following operations:

    #   * Replaces `(ampersand)quot;` with `"`

    #   * Replaces `(ampersand)nbsp;` with a non-breaking space, decimal 160

    #   * Replaces `(ampersand)lt;` with a "less than" symbol

    #   * Replaces `(ampersand)gt;` with `>`

    #   * Replaces characters that are represented in hexadecimal format, `(ampersand)#xhhhh;`, with the corresponding characters

    #   * Replaces characters that are represented in decimal format, `(ampersand)#nnnn;`, with the corresponding characters

    # **LOWERCASE**

    # Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

    # **URL_DECODE**

    # Use this option to decode a URL-encoded value.

    # **NONE**

    # Specify `NONE` if you don't want to perform any text transformations.
    text_transformation: "TextTransformation" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Within the portion of a web request that you want to search (for example,
    # in the query string, if any), specify where you want AWS WAF to search.
    # Valid values include the following:

    # **CONTAINS**

    # The specified part of the web request must include the value of
    # `TargetString`, but the location doesn't matter.

    # **CONTAINS_WORD**

    # The specified part of the web request must include the value of
    # `TargetString`, and `TargetString` must contain only alphanumeric
    # characters or underscore (A-Z, a-z, 0-9, or _). In addition, `TargetString`
    # must be a word, which means one of the following:

    #   * `TargetString` exactly matches the value of the specified part of the web request, such as the value of a header.

    #   * `TargetString` is at the beginning of the specified part of the web request and is followed by a character other than an alphanumeric character or underscore (_), for example, `BadBot;`.

    #   * `TargetString` is at the end of the specified part of the web request and is preceded by a character other than an alphanumeric character or underscore (_), for example, `;BadBot`.

    #   * `TargetString` is in the middle of the specified part of the web request and is preceded and followed by characters other than alphanumeric characters or underscore (_), for example, `-BadBot;`.

    # **EXACTLY**

    # The value of the specified part of the web request must exactly match the
    # value of `TargetString`.

    # **STARTS_WITH**

    # The value of `TargetString` must appear at the beginning of the specified
    # part of the web request.

    # **ENDS_WITH**

    # The value of `TargetString` must appear at the end of the specified part of
    # the web request.
    positional_constraint: "PositionalConstraint" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class ChangeAction(Enum):
    INSERT = "INSERT"
    DELETE = "DELETE"


class ChangeTokenStatus(Enum):
    PROVISIONED = "PROVISIONED"
    PENDING = "PENDING"
    INSYNC = "INSYNC"


class ComparisonOperator(Enum):
    EQ = "EQ"
    NE = "NE"
    LE = "LE"
    LT = "LT"
    GE = "GE"
    GT = "GT"


@dataclasses.dataclass
class CreateByteMatchSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A friendly name or description of the ByteMatchSet. You can't change `Name`
    # after you create a `ByteMatchSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateByteMatchSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "byte_match_set",
                "ByteMatchSet",
                autoboto.TypeInfo(ByteMatchSet),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A ByteMatchSet that contains no `ByteMatchTuple` objects.
    byte_match_set: "ByteMatchSet" = dataclasses.field(default_factory=dict, )

    # The `ChangeToken` that you used to submit the `CreateByteMatchSet` request.
    # You can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateGeoMatchSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A friendly name or description of the GeoMatchSet. You can't change `Name`
    # after you create the `GeoMatchSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateGeoMatchSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "geo_match_set",
                "GeoMatchSet",
                autoboto.TypeInfo(GeoMatchSet),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The GeoMatchSet returned in the `CreateGeoMatchSet` response. The
    # `GeoMatchSet` contains no `GeoMatchConstraints`.
    geo_match_set: "GeoMatchSet" = dataclasses.field(default_factory=dict, )

    # The `ChangeToken` that you used to submit the `CreateGeoMatchSet` request.
    # You can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateIPSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A friendly name or description of the IPSet. You can't change `Name` after
    # you create the `IPSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateIPSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip_set",
                "IPSet",
                autoboto.TypeInfo(IPSet),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The IPSet returned in the `CreateIPSet` response.
    ip_set: "IPSet" = dataclasses.field(default_factory=dict, )

    # The `ChangeToken` that you used to submit the `CreateIPSet` request. You
    # can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateRateBasedRuleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_name",
                "MetricName",
                autoboto.TypeInfo(str),
            ),
            (
                "rate_key",
                "RateKey",
                autoboto.TypeInfo(RateKey),
            ),
            (
                "rate_limit",
                "RateLimit",
                autoboto.TypeInfo(int),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A friendly name or description of the RateBasedRule. You can't change the
    # name of a `RateBasedRule` after you create it.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A friendly name or description for the metrics for this `RateBasedRule`.
    # The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name
    # can't contain whitespace. You can't change the name of the metric after you
    # create the `RateBasedRule`.
    metric_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The field that AWS WAF uses to determine if requests are likely arriving
    # from a single source and thus subject to rate monitoring. The only valid
    # value for `RateKey` is `IP`. `IP` indicates that requests that arrive from
    # the same IP address are subject to the `RateLimit` that is specified in the
    # `RateBasedRule`.
    rate_key: "RateKey" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of requests, which have an identical value in the field
    # that is specified by `RateKey`, allowed in a five-minute period. If the
    # number of requests exceeds the `RateLimit` and the other predicates
    # specified in the rule are also met, AWS WAF triggers the action that is
    # specified for this rule.
    rate_limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The `ChangeToken` that you used to submit the `CreateRateBasedRule`
    # request. You can also use this value to query the status of the request.
    # For more information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateRateBasedRuleResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule",
                "Rule",
                autoboto.TypeInfo(RateBasedRule),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The RateBasedRule that is returned in the `CreateRateBasedRule` response.
    rule: "RateBasedRule" = dataclasses.field(default_factory=dict, )

    # The `ChangeToken` that you used to submit the `CreateRateBasedRule`
    # request. You can also use this value to query the status of the request.
    # For more information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateRegexMatchSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A friendly name or description of the RegexMatchSet. You can't change
    # `Name` after you create a `RegexMatchSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateRegexMatchSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "regex_match_set",
                "RegexMatchSet",
                autoboto.TypeInfo(RegexMatchSet),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A RegexMatchSet that contains no `RegexMatchTuple` objects.
    regex_match_set: "RegexMatchSet" = dataclasses.field(default_factory=dict, )

    # The `ChangeToken` that you used to submit the `CreateRegexMatchSet`
    # request. You can also use this value to query the status of the request.
    # For more information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateRegexPatternSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A friendly name or description of the RegexPatternSet. You can't change
    # `Name` after you create a `RegexPatternSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateRegexPatternSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "regex_pattern_set",
                "RegexPatternSet",
                autoboto.TypeInfo(RegexPatternSet),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A RegexPatternSet that contains no objects.
    regex_pattern_set: "RegexPatternSet" = dataclasses.field(
        default_factory=dict,
    )

    # The `ChangeToken` that you used to submit the `CreateRegexPatternSet`
    # request. You can also use this value to query the status of the request.
    # For more information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateRuleGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_name",
                "MetricName",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A friendly name or description of the RuleGroup. You can't change `Name`
    # after you create a `RuleGroup`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A friendly name or description for the metrics for this `RuleGroup`. The
    # name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name
    # can't contain whitespace. You can't change the name of the metric after you
    # create the `RuleGroup`.
    metric_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateRuleGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_group",
                "RuleGroup",
                autoboto.TypeInfo(RuleGroup),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An empty RuleGroup.
    rule_group: "RuleGroup" = dataclasses.field(default_factory=dict, )

    # The `ChangeToken` that you used to submit the `CreateRuleGroup` request.
    # You can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateRuleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_name",
                "MetricName",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A friendly name or description of the Rule. You can't change the name of a
    # `Rule` after you create it.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A friendly name or description for the metrics for this `Rule`. The name
    # can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't
    # contain whitespace. You can't change the name of the metric after you
    # create the `Rule`.
    metric_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateRuleResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule",
                "Rule",
                autoboto.TypeInfo(Rule),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Rule returned in the `CreateRule` response.
    rule: "Rule" = dataclasses.field(default_factory=dict, )

    # The `ChangeToken` that you used to submit the `CreateRule` request. You can
    # also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateSizeConstraintSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A friendly name or description of the SizeConstraintSet. You can't change
    # `Name` after you create a `SizeConstraintSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateSizeConstraintSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "size_constraint_set",
                "SizeConstraintSet",
                autoboto.TypeInfo(SizeConstraintSet),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A SizeConstraintSet that contains no `SizeConstraint` objects.
    size_constraint_set: "SizeConstraintSet" = dataclasses.field(
        default_factory=dict,
    )

    # The `ChangeToken` that you used to submit the `CreateSizeConstraintSet`
    # request. You can also use this value to query the status of the request.
    # For more information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateSqlInjectionMatchSetRequest(autoboto.ShapeBase):
    """
    A request to create a SqlInjectionMatchSet.
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
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A friendly name or description for the SqlInjectionMatchSet that you're
    # creating. You can't change `Name` after you create the
    # `SqlInjectionMatchSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateSqlInjectionMatchSetResponse(autoboto.ShapeBase):
    """
    The response to a `CreateSqlInjectionMatchSet` request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sql_injection_match_set",
                "SqlInjectionMatchSet",
                autoboto.TypeInfo(SqlInjectionMatchSet),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A SqlInjectionMatchSet.
    sql_injection_match_set: "SqlInjectionMatchSet" = dataclasses.field(
        default_factory=dict,
    )

    # The `ChangeToken` that you used to submit the `CreateSqlInjectionMatchSet`
    # request. You can also use this value to query the status of the request.
    # For more information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateWebACLRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_name",
                "MetricName",
                autoboto.TypeInfo(str),
            ),
            (
                "default_action",
                "DefaultAction",
                autoboto.TypeInfo(WafAction),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A friendly name or description of the WebACL. You can't change `Name` after
    # you create the `WebACL`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A friendly name or description for the metrics for this `WebACL`. The name
    # can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't
    # contain whitespace. You can't change `MetricName` after you create the
    # `WebACL`.
    metric_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The action that you want AWS WAF to take when a request doesn't match the
    # criteria specified in any of the `Rule` objects that are associated with
    # the `WebACL`.
    default_action: "WafAction" = dataclasses.field(default_factory=dict, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateWebACLResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "web_acl",
                "WebACL",
                autoboto.TypeInfo(WebACL),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The WebACL returned in the `CreateWebACL` response.
    web_acl: "WebACL" = dataclasses.field(default_factory=dict, )

    # The `ChangeToken` that you used to submit the `CreateWebACL` request. You
    # can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateXssMatchSetRequest(autoboto.ShapeBase):
    """
    A request to create an XssMatchSet.
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
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A friendly name or description for the XssMatchSet that you're creating.
    # You can't change `Name` after you create the `XssMatchSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateXssMatchSetResponse(autoboto.ShapeBase):
    """
    The response to a `CreateXssMatchSet` request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "xss_match_set",
                "XssMatchSet",
                autoboto.TypeInfo(XssMatchSet),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An XssMatchSet.
    xss_match_set: "XssMatchSet" = dataclasses.field(default_factory=dict, )

    # The `ChangeToken` that you used to submit the `CreateXssMatchSet` request.
    # You can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteByteMatchSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "byte_match_set_id",
                "ByteMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ByteMatchSetId` of the ByteMatchSet that you want to delete.
    # `ByteMatchSetId` is returned by CreateByteMatchSet and by
    # ListByteMatchSets.
    byte_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteByteMatchSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `DeleteByteMatchSet` request.
    # You can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteGeoMatchSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "geo_match_set_id",
                "GeoMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `GeoMatchSetID` of the GeoMatchSet that you want to delete.
    # `GeoMatchSetId` is returned by CreateGeoMatchSet and by ListGeoMatchSets.
    geo_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteGeoMatchSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `DeleteGeoMatchSet` request.
    # You can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteIPSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip_set_id",
                "IPSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `IPSetId` of the IPSet that you want to delete. `IPSetId` is returned
    # by CreateIPSet and by ListIPSets.
    ip_set_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteIPSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `DeleteIPSet` request. You
    # can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeletePermissionPolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the RuleGroup from which you want to
    # delete the policy.

    # The user making the request must be the owner of the RuleGroup.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeletePermissionPolicyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteRateBasedRuleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_id",
                "RuleId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `RuleId` of the RateBasedRule that you want to delete. `RuleId` is
    # returned by CreateRateBasedRule and by ListRateBasedRules.
    rule_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteRateBasedRuleResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `DeleteRateBasedRule`
    # request. You can also use this value to query the status of the request.
    # For more information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteRegexMatchSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "regex_match_set_id",
                "RegexMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `RegexMatchSetId` of the RegexMatchSet that you want to delete.
    # `RegexMatchSetId` is returned by CreateRegexMatchSet and by
    # ListRegexMatchSets.
    regex_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteRegexMatchSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `DeleteRegexMatchSet`
    # request. You can also use this value to query the status of the request.
    # For more information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteRegexPatternSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "regex_pattern_set_id",
                "RegexPatternSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `RegexPatternSetId` of the RegexPatternSet that you want to delete.
    # `RegexPatternSetId` is returned by CreateRegexPatternSet and by
    # ListRegexPatternSets.
    regex_pattern_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteRegexPatternSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `DeleteRegexPatternSet`
    # request. You can also use this value to query the status of the request.
    # For more information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteRuleGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_group_id",
                "RuleGroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `RuleGroupId` of the RuleGroup that you want to delete. `RuleGroupId`
    # is returned by CreateRuleGroup and by ListRuleGroups.
    rule_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteRuleGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `DeleteRuleGroup` request.
    # You can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteRuleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_id",
                "RuleId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `RuleId` of the Rule that you want to delete. `RuleId` is returned by
    # CreateRule and by ListRules.
    rule_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteRuleResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `DeleteRule` request. You can
    # also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteSizeConstraintSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "size_constraint_set_id",
                "SizeConstraintSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `SizeConstraintSetId` of the SizeConstraintSet that you want to delete.
    # `SizeConstraintSetId` is returned by CreateSizeConstraintSet and by
    # ListSizeConstraintSets.
    size_constraint_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteSizeConstraintSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `DeleteSizeConstraintSet`
    # request. You can also use this value to query the status of the request.
    # For more information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteSqlInjectionMatchSetRequest(autoboto.ShapeBase):
    """
    A request to delete a SqlInjectionMatchSet from AWS WAF.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sql_injection_match_set_id",
                "SqlInjectionMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `SqlInjectionMatchSetId` of the SqlInjectionMatchSet that you want to
    # delete. `SqlInjectionMatchSetId` is returned by CreateSqlInjectionMatchSet
    # and by ListSqlInjectionMatchSets.
    sql_injection_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteSqlInjectionMatchSetResponse(autoboto.ShapeBase):
    """
    The response to a request to delete a SqlInjectionMatchSet from AWS WAF.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `DeleteSqlInjectionMatchSet`
    # request. You can also use this value to query the status of the request.
    # For more information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteWebACLRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "web_acl_id",
                "WebACLId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `WebACLId` of the WebACL that you want to delete. `WebACLId` is
    # returned by CreateWebACL and by ListWebACLs.
    web_acl_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteWebACLResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `DeleteWebACL` request. You
    # can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteXssMatchSetRequest(autoboto.ShapeBase):
    """
    A request to delete an XssMatchSet from AWS WAF.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "xss_match_set_id",
                "XssMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `XssMatchSetId` of the XssMatchSet that you want to delete.
    # `XssMatchSetId` is returned by CreateXssMatchSet and by ListXssMatchSets.
    xss_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteXssMatchSetResponse(autoboto.ShapeBase):
    """
    The response to a request to delete an XssMatchSet from AWS WAF.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `DeleteXssMatchSet` request.
    # You can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class FieldToMatch(autoboto.ShapeBase):
    """
    Specifies where in a web request to look for `TargetString`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(MatchFieldType),
            ),
            (
                "data",
                "Data",
                autoboto.TypeInfo(str),
            ),
        ]

    # The part of the web request that you want AWS WAF to search for a specified
    # string. Parts of a request that you can search include the following:

    #   * `HEADER`: A specified request header, for example, the value of the `User-Agent` or `Referer` header. If you choose `HEADER` for the type, specify the name of the header in `Data`.

    #   * `METHOD`: The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: `DELETE`, `GET`, `HEAD`, `OPTIONS`, `PATCH`, `POST`, and `PUT`.

    #   * `QUERY_STRING`: A query string, which is the part of a URL that appears after a `?` character, if any.

    #   * `URI`: The part of a web request that identifies a resource, for example, `/images/daily-ad.jpg`.

    #   * `BODY`: The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first `8192` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see CreateSizeConstraintSet.
    type: "MatchFieldType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # When the value of `Type` is `HEADER`, enter the name of the header that you
    # want AWS WAF to search, for example, `User-Agent` or `Referer`. If the
    # value of `Type` is any other value, omit `Data`.

    # The name of the header is not case sensitive.
    data: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GeoMatchConstraint(autoboto.ShapeBase):
    """
    The country from which web requests originate that you want AWS WAF to search
    for.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(GeoMatchConstraintType),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(GeoMatchConstraintValue),
            ),
        ]

    # The type of geographical area you want AWS WAF to search for. Currently
    # `Country` is the only valid value.
    type: "GeoMatchConstraintType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The country that you want AWS WAF to search for.
    value: "GeoMatchConstraintValue" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class GeoMatchConstraintType(Enum):
    Country = "Country"


class GeoMatchConstraintValue(Enum):
    AF = "AF"
    AX = "AX"
    AL = "AL"
    DZ = "DZ"
    AS = "AS"
    AD = "AD"
    AO = "AO"
    AI = "AI"
    AQ = "AQ"
    AG = "AG"
    AR = "AR"
    AM = "AM"
    AW = "AW"
    AU = "AU"
    AT = "AT"
    AZ = "AZ"
    BS = "BS"
    BH = "BH"
    BD = "BD"
    BB = "BB"
    BY = "BY"
    BE = "BE"
    BZ = "BZ"
    BJ = "BJ"
    BM = "BM"
    BT = "BT"
    BO = "BO"
    BQ = "BQ"
    BA = "BA"
    BW = "BW"
    BV = "BV"
    BR = "BR"
    IO = "IO"
    BN = "BN"
    BG = "BG"
    BF = "BF"
    BI = "BI"
    KH = "KH"
    CM = "CM"
    CA = "CA"
    CV = "CV"
    KY = "KY"
    CF = "CF"
    TD = "TD"
    CL = "CL"
    CN = "CN"
    CX = "CX"
    CC = "CC"
    CO = "CO"
    KM = "KM"
    CG = "CG"
    CD = "CD"
    CK = "CK"
    CR = "CR"
    CI = "CI"
    HR = "HR"
    CU = "CU"
    CW = "CW"
    CY = "CY"
    CZ = "CZ"
    DK = "DK"
    DJ = "DJ"
    DM = "DM"
    DO = "DO"
    EC = "EC"
    EG = "EG"
    SV = "SV"
    GQ = "GQ"
    ER = "ER"
    EE = "EE"
    ET = "ET"
    FK = "FK"
    FO = "FO"
    FJ = "FJ"
    FI = "FI"
    FR = "FR"
    GF = "GF"
    PF = "PF"
    TF = "TF"
    GA = "GA"
    GM = "GM"
    GE = "GE"
    DE = "DE"
    GH = "GH"
    GI = "GI"
    GR = "GR"
    GL = "GL"
    GD = "GD"
    GP = "GP"
    GU = "GU"
    GT = "GT"
    GG = "GG"
    GN = "GN"
    GW = "GW"
    GY = "GY"
    HT = "HT"
    HM = "HM"
    VA = "VA"
    HN = "HN"
    HK = "HK"
    HU = "HU"
    IS = "IS"
    IN = "IN"
    ID = "ID"
    IR = "IR"
    IQ = "IQ"
    IE = "IE"
    IM = "IM"
    IL = "IL"
    IT = "IT"
    JM = "JM"
    JP = "JP"
    JE = "JE"
    JO = "JO"
    KZ = "KZ"
    KE = "KE"
    KI = "KI"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KG = "KG"
    LA = "LA"
    LV = "LV"
    LB = "LB"
    LS = "LS"
    LR = "LR"
    LY = "LY"
    LI = "LI"
    LT = "LT"
    LU = "LU"
    MO = "MO"
    MK = "MK"
    MG = "MG"
    MW = "MW"
    MY = "MY"
    MV = "MV"
    ML = "ML"
    MT = "MT"
    MH = "MH"
    MQ = "MQ"
    MR = "MR"
    MU = "MU"
    YT = "YT"
    MX = "MX"
    FM = "FM"
    MD = "MD"
    MC = "MC"
    MN = "MN"
    ME = "ME"
    MS = "MS"
    MA = "MA"
    MZ = "MZ"
    MM = "MM"
    NA = "NA"
    NR = "NR"
    NP = "NP"
    NL = "NL"
    NC = "NC"
    NZ = "NZ"
    NI = "NI"
    NE = "NE"
    NG = "NG"
    NU = "NU"
    NF = "NF"
    MP = "MP"
    NO = "NO"
    OM = "OM"
    PK = "PK"
    PW = "PW"
    PS = "PS"
    PA = "PA"
    PG = "PG"
    PY = "PY"
    PE = "PE"
    PH = "PH"
    PN = "PN"
    PL = "PL"
    PT = "PT"
    PR = "PR"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RU = "RU"
    RW = "RW"
    BL = "BL"
    SH = "SH"
    KN = "KN"
    LC = "LC"
    MF = "MF"
    PM = "PM"
    VC = "VC"
    WS = "WS"
    SM = "SM"
    ST = "ST"
    SA = "SA"
    SN = "SN"
    RS = "RS"
    SC = "SC"
    SL = "SL"
    SG = "SG"
    SX = "SX"
    SK = "SK"
    SI = "SI"
    SB = "SB"
    SO = "SO"
    ZA = "ZA"
    GS = "GS"
    SS = "SS"
    ES = "ES"
    LK = "LK"
    SD = "SD"
    SR = "SR"
    SJ = "SJ"
    SZ = "SZ"
    SE = "SE"
    CH = "CH"
    SY = "SY"
    TW = "TW"
    TJ = "TJ"
    TZ = "TZ"
    TH = "TH"
    TL = "TL"
    TG = "TG"
    TK = "TK"
    TO = "TO"
    TT = "TT"
    TN = "TN"
    TR = "TR"
    TM = "TM"
    TC = "TC"
    TV = "TV"
    UG = "UG"
    UA = "UA"
    AE = "AE"
    GB = "GB"
    US = "US"
    UM = "UM"
    UY = "UY"
    UZ = "UZ"
    VU = "VU"
    VE = "VE"
    VN = "VN"
    VG = "VG"
    VI = "VI"
    WF = "WF"
    EH = "EH"
    YE = "YE"
    ZM = "ZM"
    ZW = "ZW"


@dataclasses.dataclass
class GeoMatchSet(autoboto.ShapeBase):
    """
    Contains one or more countries that AWS WAF will search for.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "geo_match_set_id",
                "GeoMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "geo_match_constraints",
                "GeoMatchConstraints",
                autoboto.TypeInfo(typing.List[GeoMatchConstraint]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `GeoMatchSetId` for an `GeoMatchSet`. You use `GeoMatchSetId` to get
    # information about a `GeoMatchSet` (see GeoMatchSet), update a `GeoMatchSet`
    # (see UpdateGeoMatchSet), insert a `GeoMatchSet` into a `Rule` or delete one
    # from a `Rule` (see UpdateRule), and delete a `GeoMatchSet` from AWS WAF
    # (see DeleteGeoMatchSet).

    # `GeoMatchSetId` is returned by CreateGeoMatchSet and by ListGeoMatchSets.
    geo_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An array of GeoMatchConstraint objects, which contain the country that you
    # want AWS WAF to search for.
    geo_match_constraints: typing.List["GeoMatchConstraint"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )

    # A friendly name or description of the GeoMatchSet. You can't change the
    # name of an `GeoMatchSet` after you create it.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GeoMatchSetSummary(autoboto.ShapeBase):
    """
    Contains the identifier and the name of the `GeoMatchSet`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "geo_match_set_id",
                "GeoMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `GeoMatchSetId` for an GeoMatchSet. You can use `GeoMatchSetId` in a
    # GetGeoMatchSet request to get detailed information about an GeoMatchSet.
    geo_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A friendly name or description of the GeoMatchSet. You can't change the
    # name of an `GeoMatchSet` after you create it.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GeoMatchSetUpdate(autoboto.ShapeBase):
    """
    Specifies the type of update to perform to an GeoMatchSet with
    UpdateGeoMatchSet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(ChangeAction),
            ),
            (
                "geo_match_constraint",
                "GeoMatchConstraint",
                autoboto.TypeInfo(GeoMatchConstraint),
            ),
        ]

    # Specifies whether to insert or delete a country with UpdateGeoMatchSet.
    action: "ChangeAction" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The country from which web requests originate that you want AWS WAF to
    # search for.
    geo_match_constraint: "GeoMatchConstraint" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetByteMatchSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "byte_match_set_id",
                "ByteMatchSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ByteMatchSetId` of the ByteMatchSet that you want to get.
    # `ByteMatchSetId` is returned by CreateByteMatchSet and by
    # ListByteMatchSets.
    byte_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetByteMatchSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "byte_match_set",
                "ByteMatchSet",
                autoboto.TypeInfo(ByteMatchSet),
            ),
        ]

    # Information about the ByteMatchSet that you specified in the
    # `GetByteMatchSet` request. For more information, see the following topics:

    #   * ByteMatchSet: Contains `ByteMatchSetId`, `ByteMatchTuples`, and `Name`

    #   * `ByteMatchTuples`: Contains an array of ByteMatchTuple objects. Each `ByteMatchTuple` object contains FieldToMatch, `PositionalConstraint`, `TargetString`, and `TextTransformation`

    #   * FieldToMatch: Contains `Data` and `Type`
    byte_match_set: "ByteMatchSet" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetChangeTokenRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetChangeTokenResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used in the request. Use this value in a
    # `GetChangeTokenStatus` request to get the current status of the request.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetChangeTokenStatusRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The change token for which you want to get the status. This change token
    # was previously returned in the `GetChangeToken` response.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetChangeTokenStatusResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token_status",
                "ChangeTokenStatus",
                autoboto.TypeInfo(ChangeTokenStatus),
            ),
        ]

    # The status of the change token.
    change_token_status: "ChangeTokenStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetGeoMatchSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "geo_match_set_id",
                "GeoMatchSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `GeoMatchSetId` of the GeoMatchSet that you want to get.
    # `GeoMatchSetId` is returned by CreateGeoMatchSet and by ListGeoMatchSets.
    geo_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetGeoMatchSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "geo_match_set",
                "GeoMatchSet",
                autoboto.TypeInfo(GeoMatchSet),
            ),
        ]

    # Information about the GeoMatchSet that you specified in the
    # `GetGeoMatchSet` request. This includes the `Type`, which for a
    # `GeoMatchContraint` is always `Country`, as well as the `Value`, which is
    # the identifier for a specific country.
    geo_match_set: "GeoMatchSet" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetIPSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip_set_id",
                "IPSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `IPSetId` of the IPSet that you want to get. `IPSetId` is returned by
    # CreateIPSet and by ListIPSets.
    ip_set_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetIPSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip_set",
                "IPSet",
                autoboto.TypeInfo(IPSet),
            ),
        ]

    # Information about the IPSet that you specified in the `GetIPSet` request.
    # For more information, see the following topics:

    #   * IPSet: Contains `IPSetDescriptors`, `IPSetId`, and `Name`

    #   * `IPSetDescriptors`: Contains an array of IPSetDescriptor objects. Each `IPSetDescriptor` object contains `Type` and `Value`
    ip_set: "IPSet" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetPermissionPolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the RuleGroup for which you want to get
    # the policy.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetPermissionPolicyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy",
                "Policy",
                autoboto.TypeInfo(str),
            ),
        ]

    # The IAM policy attached to the specified RuleGroup.
    policy: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetRateBasedRuleManagedKeysRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_id",
                "RuleId",
                autoboto.TypeInfo(str),
            ),
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `RuleId` of the RateBasedRule for which you want to get a list of
    # `ManagedKeys`. `RuleId` is returned by CreateRateBasedRule and by
    # ListRateBasedRules.
    rule_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A null value and not currently used. Do not include this in your request.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetRateBasedRuleManagedKeysResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "managed_keys",
                "ManagedKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of IP addresses that currently are blocked by the specified
    # RateBasedRule.
    managed_keys: typing.List[str] = dataclasses.field(default_factory=list, )

    # A null value and not currently used.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetRateBasedRuleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_id",
                "RuleId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `RuleId` of the RateBasedRule that you want to get. `RuleId` is
    # returned by CreateRateBasedRule and by ListRateBasedRules.
    rule_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetRateBasedRuleResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule",
                "Rule",
                autoboto.TypeInfo(RateBasedRule),
            ),
        ]

    # Information about the RateBasedRule that you specified in the
    # `GetRateBasedRule` request.
    rule: "RateBasedRule" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetRegexMatchSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "regex_match_set_id",
                "RegexMatchSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `RegexMatchSetId` of the RegexMatchSet that you want to get.
    # `RegexMatchSetId` is returned by CreateRegexMatchSet and by
    # ListRegexMatchSets.
    regex_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetRegexMatchSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "regex_match_set",
                "RegexMatchSet",
                autoboto.TypeInfo(RegexMatchSet),
            ),
        ]

    # Information about the RegexMatchSet that you specified in the
    # `GetRegexMatchSet` request. For more information, see RegexMatchTuple.
    regex_match_set: "RegexMatchSet" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetRegexPatternSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "regex_pattern_set_id",
                "RegexPatternSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `RegexPatternSetId` of the RegexPatternSet that you want to get.
    # `RegexPatternSetId` is returned by CreateRegexPatternSet and by
    # ListRegexPatternSets.
    regex_pattern_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetRegexPatternSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "regex_pattern_set",
                "RegexPatternSet",
                autoboto.TypeInfo(RegexPatternSet),
            ),
        ]

    # Information about the RegexPatternSet that you specified in the
    # `GetRegexPatternSet` request, including the identifier of the pattern set
    # and the regular expression patterns you want AWS WAF to search for.
    regex_pattern_set: "RegexPatternSet" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetRuleGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_group_id",
                "RuleGroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `RuleGroupId` of the RuleGroup that you want to get. `RuleGroupId` is
    # returned by CreateRuleGroup and by ListRuleGroups.
    rule_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetRuleGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_group",
                "RuleGroup",
                autoboto.TypeInfo(RuleGroup),
            ),
        ]

    # Information about the RuleGroup that you specified in the `GetRuleGroup`
    # request.
    rule_group: "RuleGroup" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetRuleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_id",
                "RuleId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `RuleId` of the Rule that you want to get. `RuleId` is returned by
    # CreateRule and by ListRules.
    rule_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetRuleResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule",
                "Rule",
                autoboto.TypeInfo(Rule),
            ),
        ]

    # Information about the Rule that you specified in the `GetRule` request. For
    # more information, see the following topics:

    #   * Rule: Contains `MetricName`, `Name`, an array of `Predicate` objects, and `RuleId`

    #   * Predicate: Each `Predicate` object contains `DataId`, `Negated`, and `Type`
    rule: "Rule" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetSampledRequestsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "web_acl_id",
                "WebAclId",
                autoboto.TypeInfo(str),
            ),
            (
                "rule_id",
                "RuleId",
                autoboto.TypeInfo(str),
            ),
            (
                "time_window",
                "TimeWindow",
                autoboto.TypeInfo(TimeWindow),
            ),
            (
                "max_items",
                "MaxItems",
                autoboto.TypeInfo(int),
            ),
        ]

    # The `WebACLId` of the `WebACL` for which you want `GetSampledRequests` to
    # return a sample of requests.
    web_acl_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # `RuleId` is one of three values:

    #   * The `RuleId` of the `Rule` or the `RuleGroupId` of the `RuleGroup` for which you want `GetSampledRequests` to return a sample of requests.

    #   * `Default_Action`, which causes `GetSampledRequests` to return a sample of the requests that didn't match any of the rules in the specified `WebACL`.
    rule_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The start date and time and the end date and time of the range for which
    # you want `GetSampledRequests` to return a sample of requests. Specify the
    # date and time in the following format: `"2016-09-27T14:50Z"`. You can
    # specify any time range in the previous three hours.
    time_window: "TimeWindow" = dataclasses.field(default_factory=dict, )

    # The number of requests that you want AWS WAF to return from among the first
    # 5,000 requests that your AWS resource received during the time range. If
    # your resource received fewer requests than the value of `MaxItems`,
    # `GetSampledRequests` returns information about all of them.
    max_items: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetSampledRequestsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sampled_requests",
                "SampledRequests",
                autoboto.TypeInfo(typing.List[SampledHTTPRequest]),
            ),
            (
                "population_size",
                "PopulationSize",
                autoboto.TypeInfo(int),
            ),
            (
                "time_window",
                "TimeWindow",
                autoboto.TypeInfo(TimeWindow),
            ),
        ]

    # A complex type that contains detailed information about each of the
    # requests in the sample.
    sampled_requests: typing.List["SampledHTTPRequest"] = dataclasses.field(
        default_factory=list,
    )

    # The total number of requests from which `GetSampledRequests` got a sample
    # of `MaxItems` requests. If `PopulationSize` is less than `MaxItems`, the
    # sample includes every request that your AWS resource received during the
    # specified time range.
    population_size: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Usually, `TimeWindow` is the time range that you specified in the
    # `GetSampledRequests` request. However, if your AWS resource received more
    # than 5,000 requests during the time range that you specified in the
    # request, `GetSampledRequests` returns the time range for the first 5,000
    # requests.
    time_window: "TimeWindow" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetSizeConstraintSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "size_constraint_set_id",
                "SizeConstraintSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `SizeConstraintSetId` of the SizeConstraintSet that you want to get.
    # `SizeConstraintSetId` is returned by CreateSizeConstraintSet and by
    # ListSizeConstraintSets.
    size_constraint_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetSizeConstraintSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "size_constraint_set",
                "SizeConstraintSet",
                autoboto.TypeInfo(SizeConstraintSet),
            ),
        ]

    # Information about the SizeConstraintSet that you specified in the
    # `GetSizeConstraintSet` request. For more information, see the following
    # topics:

    #   * SizeConstraintSet: Contains `SizeConstraintSetId`, `SizeConstraints`, and `Name`

    #   * `SizeConstraints`: Contains an array of SizeConstraint objects. Each `SizeConstraint` object contains FieldToMatch, `TextTransformation`, `ComparisonOperator`, and `Size`

    #   * FieldToMatch: Contains `Data` and `Type`
    size_constraint_set: "SizeConstraintSet" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetSqlInjectionMatchSetRequest(autoboto.ShapeBase):
    """
    A request to get a SqlInjectionMatchSet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sql_injection_match_set_id",
                "SqlInjectionMatchSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `SqlInjectionMatchSetId` of the SqlInjectionMatchSet that you want to
    # get. `SqlInjectionMatchSetId` is returned by CreateSqlInjectionMatchSet and
    # by ListSqlInjectionMatchSets.
    sql_injection_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetSqlInjectionMatchSetResponse(autoboto.ShapeBase):
    """
    The response to a GetSqlInjectionMatchSet request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sql_injection_match_set",
                "SqlInjectionMatchSet",
                autoboto.TypeInfo(SqlInjectionMatchSet),
            ),
        ]

    # Information about the SqlInjectionMatchSet that you specified in the
    # `GetSqlInjectionMatchSet` request. For more information, see the following
    # topics:

    #   * SqlInjectionMatchSet: Contains `Name`, `SqlInjectionMatchSetId`, and an array of `SqlInjectionMatchTuple` objects

    #   * SqlInjectionMatchTuple: Each `SqlInjectionMatchTuple` object contains `FieldToMatch` and `TextTransformation`

    #   * FieldToMatch: Contains `Data` and `Type`
    sql_injection_match_set: "SqlInjectionMatchSet" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetWebACLRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "web_acl_id",
                "WebACLId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `WebACLId` of the WebACL that you want to get. `WebACLId` is returned
    # by CreateWebACL and by ListWebACLs.
    web_acl_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetWebACLResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "web_acl",
                "WebACL",
                autoboto.TypeInfo(WebACL),
            ),
        ]

    # Information about the WebACL that you specified in the `GetWebACL` request.
    # For more information, see the following topics:

    #   * WebACL: Contains `DefaultAction`, `MetricName`, `Name`, an array of `Rule` objects, and `WebACLId`

    #   * `DefaultAction` (Data type is WafAction): Contains `Type`

    #   * `Rules`: Contains an array of `ActivatedRule` objects, which contain `Action`, `Priority`, and `RuleId`

    #   * `Action`: Contains `Type`
    web_acl: "WebACL" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetXssMatchSetRequest(autoboto.ShapeBase):
    """
    A request to get an XssMatchSet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "xss_match_set_id",
                "XssMatchSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `XssMatchSetId` of the XssMatchSet that you want to get.
    # `XssMatchSetId` is returned by CreateXssMatchSet and by ListXssMatchSets.
    xss_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetXssMatchSetResponse(autoboto.ShapeBase):
    """
    The response to a GetXssMatchSet request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "xss_match_set",
                "XssMatchSet",
                autoboto.TypeInfo(XssMatchSet),
            ),
        ]

    # Information about the XssMatchSet that you specified in the
    # `GetXssMatchSet` request. For more information, see the following topics:

    #   * XssMatchSet: Contains `Name`, `XssMatchSetId`, and an array of `XssMatchTuple` objects

    #   * XssMatchTuple: Each `XssMatchTuple` object contains `FieldToMatch` and `TextTransformation`

    #   * FieldToMatch: Contains `Data` and `Type`
    xss_match_set: "XssMatchSet" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class HTTPHeader(autoboto.ShapeBase):
    """
    The response from a GetSampledRequests request includes an `HTTPHeader` complex
    type that appears as `Headers` in the response syntax. `HTTPHeader` contains the
    names and values of all of the headers that appear in one of the web requests
    that were returned by `GetSampledRequests`.
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

    # The name of one of the headers in the sampled web request.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value of one of the headers in the sampled web request.
    value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class HTTPRequest(autoboto.ShapeBase):
    """
    The response from a GetSampledRequests request includes an `HTTPRequest` complex
    type that appears as `Request` in the response syntax. `HTTPRequest` contains
    information about one of the web requests that were returned by
    `GetSampledRequests`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_ip",
                "ClientIP",
                autoboto.TypeInfo(str),
            ),
            (
                "country",
                "Country",
                autoboto.TypeInfo(str),
            ),
            (
                "uri",
                "URI",
                autoboto.TypeInfo(str),
            ),
            (
                "method",
                "Method",
                autoboto.TypeInfo(str),
            ),
            (
                "http_version",
                "HTTPVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "headers",
                "Headers",
                autoboto.TypeInfo(typing.List[HTTPHeader]),
            ),
        ]

    # The IP address that the request originated from. If the `WebACL` is
    # associated with a CloudFront distribution, this is the value of one of the
    # following fields in CloudFront access logs:

    #   * `c-ip`, if the viewer did not use an HTTP proxy or a load balancer to send the request

    #   * `x-forwarded-for`, if the viewer did use an HTTP proxy or a load balancer to send the request
    client_ip: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The two-letter country code for the country that the request originated
    # from. For a current list of country codes, see the Wikipedia entry [ISO
    # 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The part of a web request that identifies the resource, for example,
    # `/images/daily-ad.jpg`.
    uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The HTTP method specified in the sampled web request. CloudFront supports
    # the following methods: `DELETE`, `GET`, `HEAD`, `OPTIONS`, `PATCH`, `POST`,
    # and `PUT`.
    method: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The HTTP version specified in the sampled web request, for example,
    # `HTTP/1.1`.
    http_version: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A complex type that contains two values for each header in the sampled web
    # request: the name of the header and the value of the header.
    headers: typing.List["HTTPHeader"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class IPSet(autoboto.ShapeBase):
    """
    Contains one or more IP addresses or blocks of IP addresses specified in
    Classless Inter-Domain Routing (CIDR) notation. AWS WAF supports /8, /16, /24,
    and /32 IP address ranges for IPv4, and /24, /32, /48, /56, /64 and /128 for
    IPv6.

    To specify an individual IP address, you specify the four-part IP address
    followed by a `/32`, for example, 192.0.2.0/31. To block a range of IP
    addresses, you can specify a `/128`, `/64`, `/56`, `/48`, `/32`, `/24`, `/16`,
    or `/8` CIDR. For more information about CIDR notation, see the Wikipedia entry
    [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-
    Domain_Routing).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip_set_id",
                "IPSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "ip_set_descriptors",
                "IPSetDescriptors",
                autoboto.TypeInfo(typing.List[IPSetDescriptor]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `IPSetId` for an `IPSet`. You use `IPSetId` to get information about an
    # `IPSet` (see GetIPSet), update an `IPSet` (see UpdateIPSet), insert an
    # `IPSet` into a `Rule` or delete one from a `Rule` (see UpdateRule), and
    # delete an `IPSet` from AWS WAF (see DeleteIPSet).

    # `IPSetId` is returned by CreateIPSet and by ListIPSets.
    ip_set_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The IP address type (`IPV4` or `IPV6`) and the IP address range (in CIDR
    # notation) that web requests originate from. If the `WebACL` is associated
    # with a CloudFront distribution and the viewer did not use an HTTP proxy or
    # a load balancer to send the request, this is the value of the c-ip field in
    # the CloudFront access logs.
    ip_set_descriptors: typing.List["IPSetDescriptor"] = dataclasses.field(
        default_factory=list,
    )

    # A friendly name or description of the IPSet. You can't change the name of
    # an `IPSet` after you create it.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class IPSetDescriptor(autoboto.ShapeBase):
    """
    Specifies the IP address type (`IPV4` or `IPV6`) and the IP address range (in
    CIDR format) that web requests originate from.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(IPSetDescriptorType),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
        ]

    # Specify `IPV4` or `IPV6`.
    type: "IPSetDescriptorType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specify an IPv4 address by using CIDR notation. For example:

    #   * To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify `192.0.2.44/32`.

    #   * To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify `192.0.2.0/24`.

    # For more information about CIDR notation, see the Wikipedia entry
    # [Classless Inter-Domain
    # Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).

    # Specify an IPv6 address by using CIDR notation. For example:

    #   * To configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify `1111:0000:0000:0000:0000:0000:0000:0111/128`.

    #   * To configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify `1111:0000:0000:0000:0000:0000:0000:0000/64`.
    value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class IPSetDescriptorType(Enum):
    IPV4 = "IPV4"
    IPV6 = "IPV6"


@dataclasses.dataclass
class IPSetSummary(autoboto.ShapeBase):
    """
    Contains the identifier and the name of the `IPSet`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip_set_id",
                "IPSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `IPSetId` for an IPSet. You can use `IPSetId` in a GetIPSet request to
    # get detailed information about an IPSet.
    ip_set_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A friendly name or description of the IPSet. You can't change the name of
    # an `IPSet` after you create it.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class IPSetUpdate(autoboto.ShapeBase):
    """
    Specifies the type of update to perform to an IPSet with UpdateIPSet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(ChangeAction),
            ),
            (
                "ip_set_descriptor",
                "IPSetDescriptor",
                autoboto.TypeInfo(IPSetDescriptor),
            ),
        ]

    # Specifies whether to insert or delete an IP address with UpdateIPSet.
    action: "ChangeAction" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IP address type (`IPV4` or `IPV6`) and the IP address range (in CIDR
    # notation) that web requests originate from.
    ip_set_descriptor: "IPSetDescriptor" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ListActivatedRulesInRuleGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_group_id",
                "RuleGroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # The `RuleGroupId` of the RuleGroup for which you want to get a list of
    # ActivatedRule objects.
    rule_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If you specify a value for `Limit` and you have more `ActivatedRules` than
    # the value of `Limit`, AWS WAF returns a `NextMarker` value in the response
    # that allows you to list another group of `ActivatedRules`. For the second
    # and subsequent `ListActivatedRulesInRuleGroup` requests, specify the value
    # of `NextMarker` from the previous response to get information about another
    # batch of `ActivatedRules`.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the number of `ActivatedRules` that you want AWS WAF to return
    # for this request. If you have more `ActivatedRules` than the number that
    # you specify for `Limit`, the response includes a `NextMarker` value that
    # you can use to get another batch of `ActivatedRules`.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListActivatedRulesInRuleGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "activated_rules",
                "ActivatedRules",
                autoboto.TypeInfo(typing.List[ActivatedRule]),
            ),
        ]

    # If you have more `ActivatedRules` than the number that you specified for
    # `Limit` in the request, the response includes a `NextMarker` value. To list
    # more `ActivatedRules`, submit another `ListActivatedRulesInRuleGroup`
    # request, and specify the `NextMarker` value from the response in the
    # `NextMarker` value in the next request.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of `ActivatedRules` objects.
    activated_rules: typing.List["ActivatedRule"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListByteMatchSetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # If you specify a value for `Limit` and you have more `ByteMatchSets` than
    # the value of `Limit`, AWS WAF returns a `NextMarker` value in the response
    # that allows you to list another group of `ByteMatchSets`. For the second
    # and subsequent `ListByteMatchSets` requests, specify the value of
    # `NextMarker` from the previous response to get information about another
    # batch of `ByteMatchSets`.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the number of `ByteMatchSet` objects that you want AWS WAF to
    # return for this request. If you have more `ByteMatchSets` objects than the
    # number you specify for `Limit`, the response includes a `NextMarker` value
    # that you can use to get another batch of `ByteMatchSet` objects.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListByteMatchSetsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "byte_match_sets",
                "ByteMatchSets",
                autoboto.TypeInfo(typing.List[ByteMatchSetSummary]),
            ),
        ]

    # If you have more `ByteMatchSet` objects than the number that you specified
    # for `Limit` in the request, the response includes a `NextMarker` value. To
    # list more `ByteMatchSet` objects, submit another `ListByteMatchSets`
    # request, and specify the `NextMarker` value from the response in the
    # `NextMarker` value in the next request.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of ByteMatchSetSummary objects.
    byte_match_sets: typing.List["ByteMatchSetSummary"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListGeoMatchSetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # If you specify a value for `Limit` and you have more `GeoMatchSet`s than
    # the value of `Limit`, AWS WAF returns a `NextMarker` value in the response
    # that allows you to list another group of `GeoMatchSet` objects. For the
    # second and subsequent `ListGeoMatchSets` requests, specify the value of
    # `NextMarker` from the previous response to get information about another
    # batch of `GeoMatchSet` objects.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the number of `GeoMatchSet` objects that you want AWS WAF to
    # return for this request. If you have more `GeoMatchSet` objects than the
    # number you specify for `Limit`, the response includes a `NextMarker` value
    # that you can use to get another batch of `GeoMatchSet` objects.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListGeoMatchSetsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "geo_match_sets",
                "GeoMatchSets",
                autoboto.TypeInfo(typing.List[GeoMatchSetSummary]),
            ),
        ]

    # If you have more `GeoMatchSet` objects than the number that you specified
    # for `Limit` in the request, the response includes a `NextMarker` value. To
    # list more `GeoMatchSet` objects, submit another `ListGeoMatchSets` request,
    # and specify the `NextMarker` value from the response in the `NextMarker`
    # value in the next request.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of GeoMatchSetSummary objects.
    geo_match_sets: typing.List["GeoMatchSetSummary"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListIPSetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # If you specify a value for `Limit` and you have more `IPSets` than the
    # value of `Limit`, AWS WAF returns a `NextMarker` value in the response that
    # allows you to list another group of `IPSets`. For the second and subsequent
    # `ListIPSets` requests, specify the value of `NextMarker` from the previous
    # response to get information about another batch of `IPSets`.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the number of `IPSet` objects that you want AWS WAF to return for
    # this request. If you have more `IPSet` objects than the number you specify
    # for `Limit`, the response includes a `NextMarker` value that you can use to
    # get another batch of `IPSet` objects.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListIPSetsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "ip_sets",
                "IPSets",
                autoboto.TypeInfo(typing.List[IPSetSummary]),
            ),
        ]

    # If you have more `IPSet` objects than the number that you specified for
    # `Limit` in the request, the response includes a `NextMarker` value. To list
    # more `IPSet` objects, submit another `ListIPSets` request, and specify the
    # `NextMarker` value from the response in the `NextMarker` value in the next
    # request.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of IPSetSummary objects.
    ip_sets: typing.List["IPSetSummary"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListRateBasedRulesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # If you specify a value for `Limit` and you have more `Rules` than the value
    # of `Limit`, AWS WAF returns a `NextMarker` value in the response that
    # allows you to list another group of `Rules`. For the second and subsequent
    # `ListRateBasedRules` requests, specify the value of `NextMarker` from the
    # previous response to get information about another batch of `Rules`.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the number of `Rules` that you want AWS WAF to return for this
    # request. If you have more `Rules` than the number that you specify for
    # `Limit`, the response includes a `NextMarker` value that you can use to get
    # another batch of `Rules`.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListRateBasedRulesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "rules",
                "Rules",
                autoboto.TypeInfo(typing.List[RuleSummary]),
            ),
        ]

    # If you have more `Rules` than the number that you specified for `Limit` in
    # the request, the response includes a `NextMarker` value. To list more
    # `Rules`, submit another `ListRateBasedRules` request, and specify the
    # `NextMarker` value from the response in the `NextMarker` value in the next
    # request.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of RuleSummary objects.
    rules: typing.List["RuleSummary"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListRegexMatchSetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # If you specify a value for `Limit` and you have more `RegexMatchSet`
    # objects than the value of `Limit`, AWS WAF returns a `NextMarker` value in
    # the response that allows you to list another group of `ByteMatchSets`. For
    # the second and subsequent `ListRegexMatchSets` requests, specify the value
    # of `NextMarker` from the previous response to get information about another
    # batch of `RegexMatchSet` objects.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the number of `RegexMatchSet` objects that you want AWS WAF to
    # return for this request. If you have more `RegexMatchSet` objects than the
    # number you specify for `Limit`, the response includes a `NextMarker` value
    # that you can use to get another batch of `RegexMatchSet` objects.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListRegexMatchSetsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "regex_match_sets",
                "RegexMatchSets",
                autoboto.TypeInfo(typing.List[RegexMatchSetSummary]),
            ),
        ]

    # If you have more `RegexMatchSet` objects than the number that you specified
    # for `Limit` in the request, the response includes a `NextMarker` value. To
    # list more `RegexMatchSet` objects, submit another `ListRegexMatchSets`
    # request, and specify the `NextMarker` value from the response in the
    # `NextMarker` value in the next request.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of RegexMatchSetSummary objects.
    regex_match_sets: typing.List["RegexMatchSetSummary"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListRegexPatternSetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # If you specify a value for `Limit` and you have more `RegexPatternSet`
    # objects than the value of `Limit`, AWS WAF returns a `NextMarker` value in
    # the response that allows you to list another group of `RegexPatternSet`
    # objects. For the second and subsequent `ListRegexPatternSets` requests,
    # specify the value of `NextMarker` from the previous response to get
    # information about another batch of `RegexPatternSet` objects.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the number of `RegexPatternSet` objects that you want AWS WAF to
    # return for this request. If you have more `RegexPatternSet` objects than
    # the number you specify for `Limit`, the response includes a `NextMarker`
    # value that you can use to get another batch of `RegexPatternSet` objects.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListRegexPatternSetsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "regex_pattern_sets",
                "RegexPatternSets",
                autoboto.TypeInfo(typing.List[RegexPatternSetSummary]),
            ),
        ]

    # If you have more `RegexPatternSet` objects than the number that you
    # specified for `Limit` in the request, the response includes a `NextMarker`
    # value. To list more `RegexPatternSet` objects, submit another
    # `ListRegexPatternSets` request, and specify the `NextMarker` value from the
    # response in the `NextMarker` value in the next request.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of RegexPatternSetSummary objects.
    regex_pattern_sets: typing.List["RegexPatternSetSummary"
                                   ] = dataclasses.field(
                                       default_factory=list,
                                   )


@dataclasses.dataclass
class ListRuleGroupsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # If you specify a value for `Limit` and you have more `RuleGroups` than the
    # value of `Limit`, AWS WAF returns a `NextMarker` value in the response that
    # allows you to list another group of `RuleGroups`. For the second and
    # subsequent `ListRuleGroups` requests, specify the value of `NextMarker`
    # from the previous response to get information about another batch of
    # `RuleGroups`.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the number of `RuleGroups` that you want AWS WAF to return for
    # this request. If you have more `RuleGroups` than the number that you
    # specify for `Limit`, the response includes a `NextMarker` value that you
    # can use to get another batch of `RuleGroups`.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListRuleGroupsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "rule_groups",
                "RuleGroups",
                autoboto.TypeInfo(typing.List[RuleGroupSummary]),
            ),
        ]

    # If you have more `RuleGroups` than the number that you specified for
    # `Limit` in the request, the response includes a `NextMarker` value. To list
    # more `RuleGroups`, submit another `ListRuleGroups` request, and specify the
    # `NextMarker` value from the response in the `NextMarker` value in the next
    # request.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of RuleGroup objects.
    rule_groups: typing.List["RuleGroupSummary"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListRulesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # If you specify a value for `Limit` and you have more `Rules` than the value
    # of `Limit`, AWS WAF returns a `NextMarker` value in the response that
    # allows you to list another group of `Rules`. For the second and subsequent
    # `ListRules` requests, specify the value of `NextMarker` from the previous
    # response to get information about another batch of `Rules`.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the number of `Rules` that you want AWS WAF to return for this
    # request. If you have more `Rules` than the number that you specify for
    # `Limit`, the response includes a `NextMarker` value that you can use to get
    # another batch of `Rules`.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListRulesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "rules",
                "Rules",
                autoboto.TypeInfo(typing.List[RuleSummary]),
            ),
        ]

    # If you have more `Rules` than the number that you specified for `Limit` in
    # the request, the response includes a `NextMarker` value. To list more
    # `Rules`, submit another `ListRules` request, and specify the `NextMarker`
    # value from the response in the `NextMarker` value in the next request.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of RuleSummary objects.
    rules: typing.List["RuleSummary"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListSizeConstraintSetsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # If you specify a value for `Limit` and you have more `SizeConstraintSets`
    # than the value of `Limit`, AWS WAF returns a `NextMarker` value in the
    # response that allows you to list another group of `SizeConstraintSets`. For
    # the second and subsequent `ListSizeConstraintSets` requests, specify the
    # value of `NextMarker` from the previous response to get information about
    # another batch of `SizeConstraintSets`.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the number of `SizeConstraintSet` objects that you want AWS WAF
    # to return for this request. If you have more `SizeConstraintSets` objects
    # than the number you specify for `Limit`, the response includes a
    # `NextMarker` value that you can use to get another batch of
    # `SizeConstraintSet` objects.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListSizeConstraintSetsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "size_constraint_sets",
                "SizeConstraintSets",
                autoboto.TypeInfo(typing.List[SizeConstraintSetSummary]),
            ),
        ]

    # If you have more `SizeConstraintSet` objects than the number that you
    # specified for `Limit` in the request, the response includes a `NextMarker`
    # value. To list more `SizeConstraintSet` objects, submit another
    # `ListSizeConstraintSets` request, and specify the `NextMarker` value from
    # the response in the `NextMarker` value in the next request.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of SizeConstraintSetSummary objects.
    size_constraint_sets: typing.List["SizeConstraintSetSummary"
                                     ] = dataclasses.field(
                                         default_factory=list,
                                     )


@dataclasses.dataclass
class ListSqlInjectionMatchSetsRequest(autoboto.ShapeBase):
    """
    A request to list the SqlInjectionMatchSet objects created by the current AWS
    account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # If you specify a value for `Limit` and you have more SqlInjectionMatchSet
    # objects than the value of `Limit`, AWS WAF returns a `NextMarker` value in
    # the response that allows you to list another group of
    # `SqlInjectionMatchSets`. For the second and subsequent
    # `ListSqlInjectionMatchSets` requests, specify the value of `NextMarker`
    # from the previous response to get information about another batch of
    # `SqlInjectionMatchSets`.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the number of SqlInjectionMatchSet objects that you want AWS WAF
    # to return for this request. If you have more `SqlInjectionMatchSet` objects
    # than the number you specify for `Limit`, the response includes a
    # `NextMarker` value that you can use to get another batch of `Rules`.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListSqlInjectionMatchSetsResponse(autoboto.ShapeBase):
    """
    The response to a ListSqlInjectionMatchSets request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "sql_injection_match_sets",
                "SqlInjectionMatchSets",
                autoboto.TypeInfo(typing.List[SqlInjectionMatchSetSummary]),
            ),
        ]

    # If you have more SqlInjectionMatchSet objects than the number that you
    # specified for `Limit` in the request, the response includes a `NextMarker`
    # value. To list more `SqlInjectionMatchSet` objects, submit another
    # `ListSqlInjectionMatchSets` request, and specify the `NextMarker` value
    # from the response in the `NextMarker` value in the next request.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of SqlInjectionMatchSetSummary objects.
    sql_injection_match_sets: typing.List["SqlInjectionMatchSetSummary"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )


@dataclasses.dataclass
class ListSubscribedRuleGroupsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # If you specify a value for `Limit` and you have more
    # `ByteMatchSets`subscribed rule groups than the value of `Limit`, AWS WAF
    # returns a `NextMarker` value in the response that allows you to list
    # another group of subscribed rule groups. For the second and subsequent
    # `ListSubscribedRuleGroupsRequest` requests, specify the value of
    # `NextMarker` from the previous response to get information about another
    # batch of subscribed rule groups.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the number of subscribed rule groups that you want AWS WAF to
    # return for this request. If you have more objects than the number you
    # specify for `Limit`, the response includes a `NextMarker` value that you
    # can use to get another batch of objects.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListSubscribedRuleGroupsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "rule_groups",
                "RuleGroups",
                autoboto.TypeInfo(typing.List[SubscribedRuleGroupSummary]),
            ),
        ]

    # If you have more objects than the number that you specified for `Limit` in
    # the request, the response includes a `NextMarker` value. To list more
    # objects, submit another `ListSubscribedRuleGroups` request, and specify the
    # `NextMarker` value from the response in the `NextMarker` value in the next
    # request.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of RuleGroup objects.
    rule_groups: typing.List["SubscribedRuleGroupSummary"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListWebACLsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # If you specify a value for `Limit` and you have more `WebACL` objects than
    # the number that you specify for `Limit`, AWS WAF returns a `NextMarker`
    # value in the response that allows you to list another group of `WebACL`
    # objects. For the second and subsequent `ListWebACLs` requests, specify the
    # value of `NextMarker` from the previous response to get information about
    # another batch of `WebACL` objects.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the number of `WebACL` objects that you want AWS WAF to return
    # for this request. If you have more `WebACL` objects than the number that
    # you specify for `Limit`, the response includes a `NextMarker` value that
    # you can use to get another batch of `WebACL` objects.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListWebACLsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "web_acls",
                "WebACLs",
                autoboto.TypeInfo(typing.List[WebACLSummary]),
            ),
        ]

    # If you have more `WebACL` objects than the number that you specified for
    # `Limit` in the request, the response includes a `NextMarker` value. To list
    # more `WebACL` objects, submit another `ListWebACLs` request, and specify
    # the `NextMarker` value from the response in the `NextMarker` value in the
    # next request.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of WebACLSummary objects.
    web_acls: typing.List["WebACLSummary"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListXssMatchSetsRequest(autoboto.ShapeBase):
    """
    A request to list the XssMatchSet objects created by the current AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(int),
            ),
        ]

    # If you specify a value for `Limit` and you have more XssMatchSet objects
    # than the value of `Limit`, AWS WAF returns a `NextMarker` value in the
    # response that allows you to list another group of `XssMatchSets`. For the
    # second and subsequent `ListXssMatchSets` requests, specify the value of
    # `NextMarker` from the previous response to get information about another
    # batch of `XssMatchSets`.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the number of XssMatchSet objects that you want AWS WAF to return
    # for this request. If you have more `XssMatchSet` objects than the number
    # you specify for `Limit`, the response includes a `NextMarker` value that
    # you can use to get another batch of `Rules`.
    limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListXssMatchSetsResponse(autoboto.ShapeBase):
    """
    The response to a ListXssMatchSets request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "xss_match_sets",
                "XssMatchSets",
                autoboto.TypeInfo(typing.List[XssMatchSetSummary]),
            ),
        ]

    # If you have more XssMatchSet objects than the number that you specified for
    # `Limit` in the request, the response includes a `NextMarker` value. To list
    # more `XssMatchSet` objects, submit another `ListXssMatchSets` request, and
    # specify the `NextMarker` value from the response in the `NextMarker` value
    # in the next request.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of XssMatchSetSummary objects.
    xss_match_sets: typing.List["XssMatchSetSummary"] = dataclasses.field(
        default_factory=list,
    )


class MatchFieldType(Enum):
    URI = "URI"
    QUERY_STRING = "QUERY_STRING"
    HEADER = "HEADER"
    METHOD = "METHOD"
    BODY = "BODY"


class ParameterExceptionField(Enum):
    CHANGE_ACTION = "CHANGE_ACTION"
    WAF_ACTION = "WAF_ACTION"
    WAF_OVERRIDE_ACTION = "WAF_OVERRIDE_ACTION"
    PREDICATE_TYPE = "PREDICATE_TYPE"
    IPSET_TYPE = "IPSET_TYPE"
    BYTE_MATCH_FIELD_TYPE = "BYTE_MATCH_FIELD_TYPE"
    SQL_INJECTION_MATCH_FIELD_TYPE = "SQL_INJECTION_MATCH_FIELD_TYPE"
    BYTE_MATCH_TEXT_TRANSFORMATION = "BYTE_MATCH_TEXT_TRANSFORMATION"
    BYTE_MATCH_POSITIONAL_CONSTRAINT = "BYTE_MATCH_POSITIONAL_CONSTRAINT"
    SIZE_CONSTRAINT_COMPARISON_OPERATOR = "SIZE_CONSTRAINT_COMPARISON_OPERATOR"
    GEO_MATCH_LOCATION_TYPE = "GEO_MATCH_LOCATION_TYPE"
    GEO_MATCH_LOCATION_VALUE = "GEO_MATCH_LOCATION_VALUE"
    RATE_KEY = "RATE_KEY"
    RULE_TYPE = "RULE_TYPE"
    NEXT_MARKER = "NEXT_MARKER"


class ParameterExceptionReason(Enum):
    INVALID_OPTION = "INVALID_OPTION"
    ILLEGAL_COMBINATION = "ILLEGAL_COMBINATION"


class PositionalConstraint(Enum):
    EXACTLY = "EXACTLY"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    CONTAINS = "CONTAINS"
    CONTAINS_WORD = "CONTAINS_WORD"


@dataclasses.dataclass
class Predicate(autoboto.ShapeBase):
    """
    Specifies the ByteMatchSet, IPSet, SqlInjectionMatchSet, XssMatchSet,
    RegexMatchSet, GeoMatchSet, and SizeConstraintSet objects that you want to add
    to a `Rule` and, for each object, indicates whether you want to negate the
    settings, for example, requests that do NOT originate from the IP address
    192.0.2.44.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "negated",
                "Negated",
                autoboto.TypeInfo(bool),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(PredicateType),
            ),
            (
                "data_id",
                "DataId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Set `Negated` to `False` if you want AWS WAF to allow, block, or count
    # requests based on the settings in the specified ByteMatchSet, IPSet,
    # SqlInjectionMatchSet, XssMatchSet, RegexMatchSet, GeoMatchSet, or
    # SizeConstraintSet. For example, if an `IPSet` includes the IP address
    # `192.0.2.44`, AWS WAF will allow or block requests based on that IP
    # address.

    # Set `Negated` to `True` if you want AWS WAF to allow or block a request
    # based on the negation of the settings in the ByteMatchSet, IPSet,
    # SqlInjectionMatchSet, XssMatchSet, RegexMatchSet, GeoMatchSet, or
    # SizeConstraintSet. For example, if an `IPSet` includes the IP address
    # `192.0.2.44`, AWS WAF will allow, block, or count requests based on all IP
    # addresses _except_ `192.0.2.44`.
    negated: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of predicate in a `Rule`, such as `ByteMatchSet` or `IPSet`.
    type: "PredicateType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A unique identifier for a predicate in a `Rule`, such as `ByteMatchSetId`
    # or `IPSetId`. The ID is returned by the corresponding `Create` or `List`
    # command.
    data_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class PredicateType(Enum):
    IPMatch = "IPMatch"
    ByteMatch = "ByteMatch"
    SqlInjectionMatch = "SqlInjectionMatch"
    GeoMatch = "GeoMatch"
    SizeConstraint = "SizeConstraint"
    XssMatch = "XssMatch"
    RegexMatch = "RegexMatch"


@dataclasses.dataclass
class PutPermissionPolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "policy",
                "Policy",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the RuleGroup to which you want to attach
    # the policy.
    resource_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The policy to attach to the specified RuleGroup.
    policy: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PutPermissionPolicyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RateBasedRule(autoboto.ShapeBase):
    """
    A `RateBasedRule` is identical to a regular Rule, with one addition: a
    `RateBasedRule` counts the number of requests that arrive from a specified IP
    address every five minutes. For example, based on recent requests that you've
    seen from an attacker, you might create a `RateBasedRule` that includes the
    following conditions:

      * The requests come from 192.0.2.44.

      * They contain the value `BadBot` in the `User-Agent` header.

    In the rule, you also define the rate limit as 15,000.

    Requests that meet both of these conditions and exceed 15,000 requests every
    five minutes trigger the rule's action (block or count), which is defined in the
    web ACL.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_id",
                "RuleId",
                autoboto.TypeInfo(str),
            ),
            (
                "match_predicates",
                "MatchPredicates",
                autoboto.TypeInfo(typing.List[Predicate]),
            ),
            (
                "rate_key",
                "RateKey",
                autoboto.TypeInfo(RateKey),
            ),
            (
                "rate_limit",
                "RateLimit",
                autoboto.TypeInfo(int),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_name",
                "MetricName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier for a `RateBasedRule`. You use `RuleId` to get more
    # information about a `RateBasedRule` (see GetRateBasedRule), update a
    # `RateBasedRule` (see UpdateRateBasedRule), insert a `RateBasedRule` into a
    # `WebACL` or delete one from a `WebACL` (see UpdateWebACL), or delete a
    # `RateBasedRule` from AWS WAF (see DeleteRateBasedRule).
    rule_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The `Predicates` object contains one `Predicate` element for each
    # ByteMatchSet, IPSet, or SqlInjectionMatchSet object that you want to
    # include in a `RateBasedRule`.
    match_predicates: typing.List["Predicate"] = dataclasses.field(
        default_factory=list,
    )

    # The field that AWS WAF uses to determine if requests are likely arriving
    # from single source and thus subject to rate monitoring. The only valid
    # value for `RateKey` is `IP`. `IP` indicates that requests arriving from the
    # same IP address are subject to the `RateLimit` that is specified in the
    # `RateBasedRule`.
    rate_key: "RateKey" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum number of requests, which have an identical value in the field
    # specified by the `RateKey`, allowed in a five-minute period. If the number
    # of requests exceeds the `RateLimit` and the other predicates specified in
    # the rule are also met, AWS WAF triggers the action that is specified for
    # this rule.
    rate_limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A friendly name or description for a `RateBasedRule`. You can't change the
    # name of a `RateBasedRule` after you create it.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A friendly name or description for the metrics for a `RateBasedRule`. The
    # name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name
    # can't contain whitespace. You can't change the name of the metric after you
    # create the `RateBasedRule`.
    metric_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class RateKey(Enum):
    IP = "IP"


@dataclasses.dataclass
class RegexMatchSet(autoboto.ShapeBase):
    """
    In a GetRegexMatchSet request, `RegexMatchSet` is a complex type that contains
    the `RegexMatchSetId` and `Name` of a `RegexMatchSet`, and the values that you
    specified when you updated the `RegexMatchSet`.

    The values are contained in a `RegexMatchTuple` object, which specify the parts
    of web requests that you want AWS WAF to inspect and the values that you want
    AWS WAF to search for. If a `RegexMatchSet` contains more than one
    `RegexMatchTuple` object, a request needs to match the settings in only one
    `ByteMatchTuple` to be considered a match.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "regex_match_set_id",
                "RegexMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "regex_match_tuples",
                "RegexMatchTuples",
                autoboto.TypeInfo(typing.List[RegexMatchTuple]),
            ),
        ]

    # The `RegexMatchSetId` for a `RegexMatchSet`. You use `RegexMatchSetId` to
    # get information about a `RegexMatchSet` (see GetRegexMatchSet), update a
    # `RegexMatchSet` (see UpdateRegexMatchSet), insert a `RegexMatchSet` into a
    # `Rule` or delete one from a `Rule` (see UpdateRule), and delete a
    # `RegexMatchSet` from AWS WAF (see DeleteRegexMatchSet).

    # `RegexMatchSetId` is returned by CreateRegexMatchSet and by
    # ListRegexMatchSets.
    regex_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A friendly name or description of the RegexMatchSet. You can't change
    # `Name` after you create a `RegexMatchSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Contains an array of RegexMatchTuple objects. Each `RegexMatchTuple` object
    # contains:

    #   * The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the `User-Agent` header.

    #   * The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see RegexPatternSet.

    #   * Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.
    regex_match_tuples: typing.List["RegexMatchTuple"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class RegexMatchSetSummary(autoboto.ShapeBase):
    """
    Returned by ListRegexMatchSets. Each `RegexMatchSetSummary` object includes the
    `Name` and `RegexMatchSetId` for one RegexMatchSet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "regex_match_set_id",
                "RegexMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `RegexMatchSetId` for a `RegexMatchSet`. You use `RegexMatchSetId` to
    # get information about a `RegexMatchSet`, update a `RegexMatchSet`, remove a
    # `RegexMatchSet` from a `Rule`, and delete a `RegexMatchSet` from AWS WAF.

    # `RegexMatchSetId` is returned by CreateRegexMatchSet and by
    # ListRegexMatchSets.
    regex_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A friendly name or description of the RegexMatchSet. You can't change
    # `Name` after you create a `RegexMatchSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RegexMatchSetUpdate(autoboto.ShapeBase):
    """
    In an UpdateRegexMatchSet request, `RegexMatchSetUpdate` specifies whether to
    insert or delete a RegexMatchTuple and includes the settings for the
    `RegexMatchTuple`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(ChangeAction),
            ),
            (
                "regex_match_tuple",
                "RegexMatchTuple",
                autoboto.TypeInfo(RegexMatchTuple),
            ),
        ]

    # Specifies whether to insert or delete a RegexMatchTuple.
    action: "ChangeAction" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about the part of a web request that you want AWS WAF to
    # inspect and the identifier of the regular expression (regex) pattern that
    # you want AWS WAF to search for. If you specify `DELETE` for the value of
    # `Action`, the `RegexMatchTuple` values must exactly match the values in the
    # `RegexMatchTuple` that you want to delete from the `RegexMatchSet`.
    regex_match_tuple: "RegexMatchTuple" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class RegexMatchTuple(autoboto.ShapeBase):
    """
    The regular expression pattern that you want AWS WAF to search for in web
    requests, the location in requests that you want AWS WAF to search, and other
    settings. Each `RegexMatchTuple` object contains:

      * The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the `User-Agent` header. 

      * The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see RegexPatternSet. 

      * Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_to_match",
                "FieldToMatch",
                autoboto.TypeInfo(FieldToMatch),
            ),
            (
                "text_transformation",
                "TextTransformation",
                autoboto.TypeInfo(TextTransformation),
            ),
            (
                "regex_pattern_set_id",
                "RegexPatternSetId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Specifies where in a web request to look for the `RegexPatternSet`.
    field_to_match: "FieldToMatch" = dataclasses.field(default_factory=dict, )

    # Text transformations eliminate some of the unusual formatting that
    # attackers use in web requests in an effort to bypass AWS WAF. If you
    # specify a transformation, AWS WAF performs the transformation on
    # `RegexPatternSet` before inspecting a request for a match.

    # **CMD_LINE**

    # When you're concerned that attackers are injecting an operating system
    # commandline command and using unusual formatting to disguise some or all of
    # the command, use this option to perform the following transformations:

    #   * Delete the following characters: \ " ' ^

    #   * Delete spaces before the following characters: / (

    #   * Replace the following characters with a space: , ;

    #   * Replace multiple spaces with one space

    #   * Convert uppercase letters (A-Z) to lowercase (a-z)

    # **COMPRESS_WHITE_SPACE**

    # Use this option to replace the following characters with a space character
    # (decimal 32):

    #   * \f, formfeed, decimal 12

    #   * \t, tab, decimal 9

    #   * \n, newline, decimal 10

    #   * \r, carriage return, decimal 13

    #   * \v, vertical tab, decimal 11

    #   * non-breaking space, decimal 160

    # `COMPRESS_WHITE_SPACE` also replaces multiple spaces with one space.

    # **HTML_ENTITY_DECODE**

    # Use this option to replace HTML-encoded characters with unencoded
    # characters. `HTML_ENTITY_DECODE` performs the following operations:

    #   * Replaces `(ampersand)quot;` with `"`

    #   * Replaces `(ampersand)nbsp;` with a non-breaking space, decimal 160

    #   * Replaces `(ampersand)lt;` with a "less than" symbol

    #   * Replaces `(ampersand)gt;` with `>`

    #   * Replaces characters that are represented in hexadecimal format, `(ampersand)#xhhhh;`, with the corresponding characters

    #   * Replaces characters that are represented in decimal format, `(ampersand)#nnnn;`, with the corresponding characters

    # **LOWERCASE**

    # Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

    # **URL_DECODE**

    # Use this option to decode a URL-encoded value.

    # **NONE**

    # Specify `NONE` if you don't want to perform any text transformations.
    text_transformation: "TextTransformation" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The `RegexPatternSetId` for a `RegexPatternSet`. You use
    # `RegexPatternSetId` to get information about a `RegexPatternSet` (see
    # GetRegexPatternSet), update a `RegexPatternSet` (see
    # UpdateRegexPatternSet), insert a `RegexPatternSet` into a `RegexMatchSet`
    # or delete one from a `RegexMatchSet` (see UpdateRegexMatchSet), and delete
    # an `RegexPatternSet` from AWS WAF (see DeleteRegexPatternSet).

    # `RegexPatternSetId` is returned by CreateRegexPatternSet and by
    # ListRegexPatternSets.
    regex_pattern_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class RegexPatternSet(autoboto.ShapeBase):
    """
    The `RegexPatternSet` specifies the regular expression (regex) pattern that you
    want AWS WAF to search for, such as `B[a@]dB[o0]t`. You can then configure AWS
    WAF to reject those requests.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "regex_pattern_set_id",
                "RegexPatternSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "regex_pattern_strings",
                "RegexPatternStrings",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier for the `RegexPatternSet`. You use `RegexPatternSetId` to
    # get information about a `RegexPatternSet`, update a `RegexPatternSet`,
    # remove a `RegexPatternSet` from a `RegexMatchSet`, and delete a
    # `RegexPatternSet` from AWS WAF.

    # `RegexMatchSetId` is returned by CreateRegexPatternSet and by
    # ListRegexPatternSets.
    regex_pattern_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the regular expression (regex) patterns that you want AWS WAF to
    # search for, such as `B[a@]dB[o0]t`.
    regex_pattern_strings: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A friendly name or description of the RegexPatternSet. You can't change
    # `Name` after you create a `RegexPatternSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RegexPatternSetSummary(autoboto.ShapeBase):
    """
    Returned by ListRegexPatternSets. Each `RegexPatternSetSummary` object includes
    the `Name` and `RegexPatternSetId` for one RegexPatternSet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "regex_pattern_set_id",
                "RegexPatternSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `RegexPatternSetId` for a `RegexPatternSet`. You use
    # `RegexPatternSetId` to get information about a `RegexPatternSet`, update a
    # `RegexPatternSet`, remove a `RegexPatternSet` from a `RegexMatchSet`, and
    # delete a `RegexPatternSet` from AWS WAF.

    # `RegexPatternSetId` is returned by CreateRegexPatternSet and by
    # ListRegexPatternSets.
    regex_pattern_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A friendly name or description of the RegexPatternSet. You can't change
    # `Name` after you create a `RegexPatternSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RegexPatternSetUpdate(autoboto.ShapeBase):
    """
    In an UpdateRegexPatternSet request, `RegexPatternSetUpdate` specifies whether
    to insert or delete a `RegexPatternString` and includes the settings for the
    `RegexPatternString`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(ChangeAction),
            ),
            (
                "regex_pattern_string",
                "RegexPatternString",
                autoboto.TypeInfo(str),
            ),
        ]

    # Specifies whether to insert or delete a `RegexPatternString`.
    action: "ChangeAction" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the regular expression (regex) pattern that you want AWS WAF to
    # search for, such as `B[a@]dB[o0]t`.
    regex_pattern_string: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Rule(autoboto.ShapeBase):
    """
    A combination of ByteMatchSet, IPSet, and/or SqlInjectionMatchSet objects that
    identify the web requests that you want to allow, block, or count. For example,
    you might create a `Rule` that includes the following predicates:

      * An `IPSet` that causes AWS WAF to search for web requests that originate from the IP address `192.0.2.44`

      * A `ByteMatchSet` that causes AWS WAF to search for web requests for which the value of the `User-Agent` header is `BadBot`.

    To match the settings in this `Rule`, a request must originate from `192.0.2.44`
    AND include a `User-Agent` header for which the value is `BadBot`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_id",
                "RuleId",
                autoboto.TypeInfo(str),
            ),
            (
                "predicates",
                "Predicates",
                autoboto.TypeInfo(typing.List[Predicate]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_name",
                "MetricName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier for a `Rule`. You use `RuleId` to get more information
    # about a `Rule` (see GetRule), update a `Rule` (see UpdateRule), insert a
    # `Rule` into a `WebACL` or delete a one from a `WebACL` (see UpdateWebACL),
    # or delete a `Rule` from AWS WAF (see DeleteRule).

    # `RuleId` is returned by CreateRule and by ListRules.
    rule_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The `Predicates` object contains one `Predicate` element for each
    # ByteMatchSet, IPSet, or SqlInjectionMatchSet object that you want to
    # include in a `Rule`.
    predicates: typing.List["Predicate"] = dataclasses.field(
        default_factory=list,
    )

    # The friendly name or description for the `Rule`. You can't change the name
    # of a `Rule` after you create it.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A friendly name or description for the metrics for this `Rule`. The name
    # can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't
    # contain whitespace. You can't change `MetricName` after you create the
    # `Rule`.
    metric_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RuleGroup(autoboto.ShapeBase):
    """
    A collection of predefined rules that you can add to a web ACL.

    Rule groups are subject to the following limits:

      * Three rule groups per account. You can request an increase to this limit by contacting customer support.

      * One rule group per web ACL.

      * Ten rules per rule group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_group_id",
                "RuleGroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_name",
                "MetricName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier for a `RuleGroup`. You use `RuleGroupId` to get more
    # information about a `RuleGroup` (see GetRuleGroup), update a `RuleGroup`
    # (see UpdateRuleGroup), insert a `RuleGroup` into a `WebACL` or delete a one
    # from a `WebACL` (see UpdateWebACL), or delete a `RuleGroup` from AWS WAF
    # (see DeleteRuleGroup).

    # `RuleGroupId` is returned by CreateRuleGroup and by ListRuleGroups.
    rule_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The friendly name or description for the `RuleGroup`. You can't change the
    # name of a `RuleGroup` after you create it.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A friendly name or description for the metrics for this `RuleGroup`. The
    # name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name
    # can't contain whitespace. You can't change the name of the metric after you
    # create the `RuleGroup`.
    metric_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RuleGroupSummary(autoboto.ShapeBase):
    """
    Contains the identifier and the friendly name or description of the `RuleGroup`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_group_id",
                "RuleGroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier for a `RuleGroup`. You use `RuleGroupId` to get more
    # information about a `RuleGroup` (see GetRuleGroup), update a `RuleGroup`
    # (see UpdateRuleGroup), insert a `RuleGroup` into a `WebACL` or delete one
    # from a `WebACL` (see UpdateWebACL), or delete a `RuleGroup` from AWS WAF
    # (see DeleteRuleGroup).

    # `RuleGroupId` is returned by CreateRuleGroup and by ListRuleGroups.
    rule_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A friendly name or description of the RuleGroup. You can't change the name
    # of a `RuleGroup` after you create it.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RuleGroupUpdate(autoboto.ShapeBase):
    """
    Specifies an `ActivatedRule` and indicates whether you want to add it to a
    `RuleGroup` or delete it from a `RuleGroup`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(ChangeAction),
            ),
            (
                "activated_rule",
                "ActivatedRule",
                autoboto.TypeInfo(ActivatedRule),
            ),
        ]

    # Specify `INSERT` to add an `ActivatedRule` to a `RuleGroup`. Use `DELETE`
    # to remove an `ActivatedRule` from a `RuleGroup`.
    action: "ChangeAction" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The `ActivatedRule` object specifies a `Rule` that you want to insert or
    # delete, the priority of the `Rule` in the `WebACL`, and the action that you
    # want AWS WAF to take when a web request matches the `Rule` (`ALLOW`,
    # `BLOCK`, or `COUNT`).
    activated_rule: "ActivatedRule" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class RuleSummary(autoboto.ShapeBase):
    """
    Contains the identifier and the friendly name or description of the `Rule`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_id",
                "RuleId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier for a `Rule`. You use `RuleId` to get more information
    # about a `Rule` (see GetRule), update a `Rule` (see UpdateRule), insert a
    # `Rule` into a `WebACL` or delete one from a `WebACL` (see UpdateWebACL), or
    # delete a `Rule` from AWS WAF (see DeleteRule).

    # `RuleId` is returned by CreateRule and by ListRules.
    rule_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A friendly name or description of the Rule. You can't change the name of a
    # `Rule` after you create it.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class RuleUpdate(autoboto.ShapeBase):
    """
    Specifies a `Predicate` (such as an `IPSet`) and indicates whether you want to
    add it to a `Rule` or delete it from a `Rule`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(ChangeAction),
            ),
            (
                "predicate",
                "Predicate",
                autoboto.TypeInfo(Predicate),
            ),
        ]

    # Specify `INSERT` to add a `Predicate` to a `Rule`. Use `DELETE` to remove a
    # `Predicate` from a `Rule`.
    action: "ChangeAction" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the `Predicate` (such as an `IPSet`) that you want to add to a
    # `Rule`.
    predicate: "Predicate" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class SampledHTTPRequest(autoboto.ShapeBase):
    """
    The response from a GetSampledRequests request includes a `SampledHTTPRequests`
    complex type that appears as `SampledRequests` in the response syntax.
    `SampledHTTPRequests` contains one `SampledHTTPRequest` object for each web
    request that is returned by `GetSampledRequests`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "request",
                "Request",
                autoboto.TypeInfo(HTTPRequest),
            ),
            (
                "weight",
                "Weight",
                autoboto.TypeInfo(int),
            ),
            (
                "timestamp",
                "Timestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "action",
                "Action",
                autoboto.TypeInfo(str),
            ),
            (
                "rule_within_rule_group",
                "RuleWithinRuleGroup",
                autoboto.TypeInfo(str),
            ),
        ]

    # A complex type that contains detailed information about the request.
    request: "HTTPRequest" = dataclasses.field(default_factory=dict, )

    # A value that indicates how one result in the response relates
    # proportionally to other results in the response. A result that has a weight
    # of `2` represents roughly twice as many CloudFront web requests as a result
    # that has a weight of `1`.
    weight: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time at which AWS WAF received the request from your AWS resource, in
    # Unix time format (in seconds).
    timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The action for the `Rule` that the request matched: `ALLOW`, `BLOCK`, or
    # `COUNT`.
    action: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # This value is returned if the `GetSampledRequests` request specifies the ID
    # of a `RuleGroup` rather than the ID of an individual rule.
    # `RuleWithinRuleGroup` is the rule within the specified `RuleGroup` that
    # matched the request listed in the response.
    rule_within_rule_group: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SizeConstraint(autoboto.ShapeBase):
    """
    Specifies a constraint on the size of a part of the web request. AWS WAF uses
    the `Size`, `ComparisonOperator`, and `FieldToMatch` to build an expression in
    the form of "`Size` `ComparisonOperator` size in bytes of `FieldToMatch`". If
    that expression is true, the `SizeConstraint` is considered to match.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_to_match",
                "FieldToMatch",
                autoboto.TypeInfo(FieldToMatch),
            ),
            (
                "text_transformation",
                "TextTransformation",
                autoboto.TypeInfo(TextTransformation),
            ),
            (
                "comparison_operator",
                "ComparisonOperator",
                autoboto.TypeInfo(ComparisonOperator),
            ),
            (
                "size",
                "Size",
                autoboto.TypeInfo(int),
            ),
        ]

    # Specifies where in a web request to look for the size constraint.
    field_to_match: "FieldToMatch" = dataclasses.field(default_factory=dict, )

    # Text transformations eliminate some of the unusual formatting that
    # attackers use in web requests in an effort to bypass AWS WAF. If you
    # specify a transformation, AWS WAF performs the transformation on
    # `FieldToMatch` before inspecting a request for a match.

    # Note that if you choose `BODY` for the value of `Type`, you must choose
    # `NONE` for `TextTransformation` because CloudFront forwards only the first
    # 8192 bytes for inspection.

    # **NONE**

    # Specify `NONE` if you don't want to perform any text transformations.

    # **CMD_LINE**

    # When you're concerned that attackers are injecting an operating system
    # command line command and using unusual formatting to disguise some or all
    # of the command, use this option to perform the following transformations:

    #   * Delete the following characters: \ " ' ^

    #   * Delete spaces before the following characters: / (

    #   * Replace the following characters with a space: , ;

    #   * Replace multiple spaces with one space

    #   * Convert uppercase letters (A-Z) to lowercase (a-z)

    # **COMPRESS_WHITE_SPACE**

    # Use this option to replace the following characters with a space character
    # (decimal 32):

    #   * \f, formfeed, decimal 12

    #   * \t, tab, decimal 9

    #   * \n, newline, decimal 10

    #   * \r, carriage return, decimal 13

    #   * \v, vertical tab, decimal 11

    #   * non-breaking space, decimal 160

    # `COMPRESS_WHITE_SPACE` also replaces multiple spaces with one space.

    # **HTML_ENTITY_DECODE**

    # Use this option to replace HTML-encoded characters with unencoded
    # characters. `HTML_ENTITY_DECODE` performs the following operations:

    #   * Replaces `(ampersand)quot;` with `"`

    #   * Replaces `(ampersand)nbsp;` with a non-breaking space, decimal 160

    #   * Replaces `(ampersand)lt;` with a "less than" symbol

    #   * Replaces `(ampersand)gt;` with `>`

    #   * Replaces characters that are represented in hexadecimal format, `(ampersand)#xhhhh;`, with the corresponding characters

    #   * Replaces characters that are represented in decimal format, `(ampersand)#nnnn;`, with the corresponding characters

    # **LOWERCASE**

    # Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

    # **URL_DECODE**

    # Use this option to decode a URL-encoded value.
    text_transformation: "TextTransformation" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of comparison you want AWS WAF to perform. AWS WAF uses this in
    # combination with the provided `Size` and `FieldToMatch` to build an
    # expression in the form of "`Size` `ComparisonOperator` size in bytes of
    # `FieldToMatch`". If that expression is true, the `SizeConstraint` is
    # considered to match.

    # **EQ** : Used to test if the `Size` is equal to the size of the
    # `FieldToMatch`

    # **NE** : Used to test if the `Size` is not equal to the size of the
    # `FieldToMatch`

    # **LE** : Used to test if the `Size` is less than or equal to the size of
    # the `FieldToMatch`

    # **LT** : Used to test if the `Size` is strictly less than the size of the
    # `FieldToMatch`

    # **GE** : Used to test if the `Size` is greater than or equal to the size of
    # the `FieldToMatch`

    # **GT** : Used to test if the `Size` is strictly greater than the size of
    # the `FieldToMatch`
    comparison_operator: "ComparisonOperator" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The size in bytes that you want AWS WAF to compare against the size of the
    # specified `FieldToMatch`. AWS WAF uses this in combination with
    # `ComparisonOperator` and `FieldToMatch` to build an expression in the form
    # of "`Size` `ComparisonOperator` size in bytes of `FieldToMatch`". If that
    # expression is true, the `SizeConstraint` is considered to match.

    # Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).

    # If you specify `URI` for the value of `Type`, the / in the URI counts as
    # one character. For example, the URI `/logo.jpg` is nine characters long.
    size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SizeConstraintSet(autoboto.ShapeBase):
    """
    A complex type that contains `SizeConstraint` objects, which specify the parts
    of web requests that you want AWS WAF to inspect the size of. If a
    `SizeConstraintSet` contains more than one `SizeConstraint` object, a request
    only needs to match one constraint to be considered a match.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "size_constraint_set_id",
                "SizeConstraintSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "size_constraints",
                "SizeConstraints",
                autoboto.TypeInfo(typing.List[SizeConstraint]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier for a `SizeConstraintSet`. You use
    # `SizeConstraintSetId` to get information about a `SizeConstraintSet` (see
    # GetSizeConstraintSet), update a `SizeConstraintSet` (see
    # UpdateSizeConstraintSet), insert a `SizeConstraintSet` into a `Rule` or
    # delete one from a `Rule` (see UpdateRule), and delete a `SizeConstraintSet`
    # from AWS WAF (see DeleteSizeConstraintSet).

    # `SizeConstraintSetId` is returned by CreateSizeConstraintSet and by
    # ListSizeConstraintSets.
    size_constraint_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the parts of web requests that you want to inspect the size of.
    size_constraints: typing.List["SizeConstraint"] = dataclasses.field(
        default_factory=list,
    )

    # The name, if any, of the `SizeConstraintSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SizeConstraintSetSummary(autoboto.ShapeBase):
    """
    The `Id` and `Name` of a `SizeConstraintSet`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "size_constraint_set_id",
                "SizeConstraintSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier for a `SizeConstraintSet`. You use
    # `SizeConstraintSetId` to get information about a `SizeConstraintSet` (see
    # GetSizeConstraintSet), update a `SizeConstraintSet` (see
    # UpdateSizeConstraintSet), insert a `SizeConstraintSet` into a `Rule` or
    # delete one from a `Rule` (see UpdateRule), and delete a `SizeConstraintSet`
    # from AWS WAF (see DeleteSizeConstraintSet).

    # `SizeConstraintSetId` is returned by CreateSizeConstraintSet and by
    # ListSizeConstraintSets.
    size_constraint_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the `SizeConstraintSet`, if any.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SizeConstraintSetUpdate(autoboto.ShapeBase):
    """
    Specifies the part of a web request that you want to inspect the size of and
    indicates whether you want to add the specification to a SizeConstraintSet or
    delete it from a `SizeConstraintSet`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(ChangeAction),
            ),
            (
                "size_constraint",
                "SizeConstraint",
                autoboto.TypeInfo(SizeConstraint),
            ),
        ]

    # Specify `INSERT` to add a SizeConstraintSetUpdate to a SizeConstraintSet.
    # Use `DELETE` to remove a `SizeConstraintSetUpdate` from a
    # `SizeConstraintSet`.
    action: "ChangeAction" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies a constraint on the size of a part of the web request. AWS WAF
    # uses the `Size`, `ComparisonOperator`, and `FieldToMatch` to build an
    # expression in the form of "`Size` `ComparisonOperator` size in bytes of
    # `FieldToMatch`". If that expression is true, the `SizeConstraint` is
    # considered to match.
    size_constraint: "SizeConstraint" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SqlInjectionMatchSet(autoboto.ShapeBase):
    """
    A complex type that contains `SqlInjectionMatchTuple` objects, which specify the
    parts of web requests that you want AWS WAF to inspect for snippets of malicious
    SQL code and, if you want AWS WAF to inspect a header, the name of the header.
    If a `SqlInjectionMatchSet` contains more than one `SqlInjectionMatchTuple`
    object, a request needs to include snippets of SQL code in only one of the
    specified parts of the request to be considered a match.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sql_injection_match_set_id",
                "SqlInjectionMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "sql_injection_match_tuples",
                "SqlInjectionMatchTuples",
                autoboto.TypeInfo(typing.List[SqlInjectionMatchTuple]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier for a `SqlInjectionMatchSet`. You use
    # `SqlInjectionMatchSetId` to get information about a `SqlInjectionMatchSet`
    # (see GetSqlInjectionMatchSet), update a `SqlInjectionMatchSet` (see
    # UpdateSqlInjectionMatchSet), insert a `SqlInjectionMatchSet` into a `Rule`
    # or delete one from a `Rule` (see UpdateRule), and delete a
    # `SqlInjectionMatchSet` from AWS WAF (see DeleteSqlInjectionMatchSet).

    # `SqlInjectionMatchSetId` is returned by CreateSqlInjectionMatchSet and by
    # ListSqlInjectionMatchSets.
    sql_injection_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the parts of web requests that you want to inspect for snippets
    # of malicious SQL code.
    sql_injection_match_tuples: typing.List["SqlInjectionMatchTuple"
                                           ] = dataclasses.field(
                                               default_factory=list,
                                           )

    # The name, if any, of the `SqlInjectionMatchSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SqlInjectionMatchSetSummary(autoboto.ShapeBase):
    """
    The `Id` and `Name` of a `SqlInjectionMatchSet`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sql_injection_match_set_id",
                "SqlInjectionMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier for a `SqlInjectionMatchSet`. You use
    # `SqlInjectionMatchSetId` to get information about a `SqlInjectionMatchSet`
    # (see GetSqlInjectionMatchSet), update a `SqlInjectionMatchSet` (see
    # UpdateSqlInjectionMatchSet), insert a `SqlInjectionMatchSet` into a `Rule`
    # or delete one from a `Rule` (see UpdateRule), and delete a
    # `SqlInjectionMatchSet` from AWS WAF (see DeleteSqlInjectionMatchSet).

    # `SqlInjectionMatchSetId` is returned by CreateSqlInjectionMatchSet and by
    # ListSqlInjectionMatchSets.
    sql_injection_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the `SqlInjectionMatchSet`, if any, specified by `Id`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SqlInjectionMatchSetUpdate(autoboto.ShapeBase):
    """
    Specifies the part of a web request that you want to inspect for snippets of
    malicious SQL code and indicates whether you want to add the specification to a
    SqlInjectionMatchSet or delete it from a `SqlInjectionMatchSet`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(ChangeAction),
            ),
            (
                "sql_injection_match_tuple",
                "SqlInjectionMatchTuple",
                autoboto.TypeInfo(SqlInjectionMatchTuple),
            ),
        ]

    # Specify `INSERT` to add a SqlInjectionMatchSetUpdate to a
    # SqlInjectionMatchSet. Use `DELETE` to remove a `SqlInjectionMatchSetUpdate`
    # from a `SqlInjectionMatchSet`.
    action: "ChangeAction" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the part of a web request that you want AWS WAF to inspect for
    # snippets of malicious SQL code and, if you want AWS WAF to inspect a
    # header, the name of the header.
    sql_injection_match_tuple: "SqlInjectionMatchTuple" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SqlInjectionMatchTuple(autoboto.ShapeBase):
    """
    Specifies the part of a web request that you want AWS WAF to inspect for
    snippets of malicious SQL code and, if you want AWS WAF to inspect a header, the
    name of the header.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_to_match",
                "FieldToMatch",
                autoboto.TypeInfo(FieldToMatch),
            ),
            (
                "text_transformation",
                "TextTransformation",
                autoboto.TypeInfo(TextTransformation),
            ),
        ]

    # Specifies where in a web request to look for snippets of malicious SQL
    # code.
    field_to_match: "FieldToMatch" = dataclasses.field(default_factory=dict, )

    # Text transformations eliminate some of the unusual formatting that
    # attackers use in web requests in an effort to bypass AWS WAF. If you
    # specify a transformation, AWS WAF performs the transformation on
    # `FieldToMatch` before inspecting a request for a match.

    # **CMD_LINE**

    # When you're concerned that attackers are injecting an operating system
    # commandline command and using unusual formatting to disguise some or all of
    # the command, use this option to perform the following transformations:

    #   * Delete the following characters: \ " ' ^

    #   * Delete spaces before the following characters: / (

    #   * Replace the following characters with a space: , ;

    #   * Replace multiple spaces with one space

    #   * Convert uppercase letters (A-Z) to lowercase (a-z)

    # **COMPRESS_WHITE_SPACE**

    # Use this option to replace the following characters with a space character
    # (decimal 32):

    #   * \f, formfeed, decimal 12

    #   * \t, tab, decimal 9

    #   * \n, newline, decimal 10

    #   * \r, carriage return, decimal 13

    #   * \v, vertical tab, decimal 11

    #   * non-breaking space, decimal 160

    # `COMPRESS_WHITE_SPACE` also replaces multiple spaces with one space.

    # **HTML_ENTITY_DECODE**

    # Use this option to replace HTML-encoded characters with unencoded
    # characters. `HTML_ENTITY_DECODE` performs the following operations:

    #   * Replaces `(ampersand)quot;` with `"`

    #   * Replaces `(ampersand)nbsp;` with a non-breaking space, decimal 160

    #   * Replaces `(ampersand)lt;` with a "less than" symbol

    #   * Replaces `(ampersand)gt;` with `>`

    #   * Replaces characters that are represented in hexadecimal format, `(ampersand)#xhhhh;`, with the corresponding characters

    #   * Replaces characters that are represented in decimal format, `(ampersand)#nnnn;`, with the corresponding characters

    # **LOWERCASE**

    # Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

    # **URL_DECODE**

    # Use this option to decode a URL-encoded value.

    # **NONE**

    # Specify `NONE` if you don't want to perform any text transformations.
    text_transformation: "TextTransformation" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SubscribedRuleGroupSummary(autoboto.ShapeBase):
    """
    A summary of the rule groups you are subscribed to.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_group_id",
                "RuleGroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_name",
                "MetricName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier for a `RuleGroup`.
    rule_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A friendly name or description of the `RuleGroup`. You can't change the
    # name of a `RuleGroup` after you create it.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A friendly name or description for the metrics for this `RuleGroup`. The
    # name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name
    # can't contain whitespace. You can't change the name of the metric after you
    # create the `RuleGroup`.
    metric_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class TextTransformation(Enum):
    NONE = "NONE"
    COMPRESS_WHITE_SPACE = "COMPRESS_WHITE_SPACE"
    HTML_ENTITY_DECODE = "HTML_ENTITY_DECODE"
    LOWERCASE = "LOWERCASE"
    CMD_LINE = "CMD_LINE"
    URL_DECODE = "URL_DECODE"


@dataclasses.dataclass
class TimeWindow(autoboto.ShapeBase):
    """
    In a GetSampledRequests request, the `StartTime` and `EndTime` objects specify
    the time range for which you want AWS WAF to return a sample of web requests.

    In a GetSampledRequests response, the `StartTime` and `EndTime` objects specify
    the time range for which AWS WAF actually returned a sample of web requests. AWS
    WAF gets the specified number of requests from among the first 5,000 requests
    that your AWS resource receives during the specified time period. If your
    resource receives more than 5,000 requests during that period, AWS WAF stops
    sampling after the 5,000th request. In that case, `EndTime` is the time that AWS
    WAF received the 5,000th request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
        ]

    # The beginning of the time range from which you want `GetSampledRequests` to
    # return a sample of the requests that your AWS resource received. Specify
    # the date and time in the following format: `"2016-09-27T14:50Z"`. You can
    # specify any time range in the previous three hours.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The end of the time range from which you want `GetSampledRequests` to
    # return a sample of the requests that your AWS resource received. Specify
    # the date and time in the following format: `"2016-09-27T14:50Z"`. You can
    # specify any time range in the previous three hours.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateByteMatchSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "byte_match_set_id",
                "ByteMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
            (
                "updates",
                "Updates",
                autoboto.TypeInfo(typing.List[ByteMatchSetUpdate]),
            ),
        ]

    # The `ByteMatchSetId` of the ByteMatchSet that you want to update.
    # `ByteMatchSetId` is returned by CreateByteMatchSet and by
    # ListByteMatchSets.
    byte_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of `ByteMatchSetUpdate` objects that you want to insert into or
    # delete from a ByteMatchSet. For more information, see the applicable data
    # types:

    #   * ByteMatchSetUpdate: Contains `Action` and `ByteMatchTuple`

    #   * ByteMatchTuple: Contains `FieldToMatch`, `PositionalConstraint`, `TargetString`, and `TextTransformation`

    #   * FieldToMatch: Contains `Data` and `Type`
    updates: typing.List["ByteMatchSetUpdate"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateByteMatchSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `UpdateByteMatchSet` request.
    # You can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateGeoMatchSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "geo_match_set_id",
                "GeoMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
            (
                "updates",
                "Updates",
                autoboto.TypeInfo(typing.List[GeoMatchSetUpdate]),
            ),
        ]

    # The `GeoMatchSetId` of the GeoMatchSet that you want to update.
    # `GeoMatchSetId` is returned by CreateGeoMatchSet and by ListGeoMatchSets.
    geo_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of `GeoMatchSetUpdate` objects that you want to insert into or
    # delete from an GeoMatchSet. For more information, see the applicable data
    # types:

    #   * GeoMatchSetUpdate: Contains `Action` and `GeoMatchConstraint`

    #   * GeoMatchConstraint: Contains `Type` and `Value`

    # You can have only one `Type` and `Value` per `GeoMatchConstraint`. To add
    # multiple countries, include multiple `GeoMatchSetUpdate` objects in your
    # request.
    updates: typing.List["GeoMatchSetUpdate"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateGeoMatchSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `UpdateGeoMatchSet` request.
    # You can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateIPSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip_set_id",
                "IPSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
            (
                "updates",
                "Updates",
                autoboto.TypeInfo(typing.List[IPSetUpdate]),
            ),
        ]

    # The `IPSetId` of the IPSet that you want to update. `IPSetId` is returned
    # by CreateIPSet and by ListIPSets.
    ip_set_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of `IPSetUpdate` objects that you want to insert into or delete
    # from an IPSet. For more information, see the applicable data types:

    #   * IPSetUpdate: Contains `Action` and `IPSetDescriptor`

    #   * IPSetDescriptor: Contains `Type` and `Value`
    updates: typing.List["IPSetUpdate"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateIPSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `UpdateIPSet` request. You
    # can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateRateBasedRuleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_id",
                "RuleId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
            (
                "updates",
                "Updates",
                autoboto.TypeInfo(typing.List[RuleUpdate]),
            ),
            (
                "rate_limit",
                "RateLimit",
                autoboto.TypeInfo(int),
            ),
        ]

    # The `RuleId` of the `RateBasedRule` that you want to update. `RuleId` is
    # returned by `CreateRateBasedRule` and by ListRateBasedRules.
    rule_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of `RuleUpdate` objects that you want to insert into or delete
    # from a RateBasedRule.
    updates: typing.List["RuleUpdate"] = dataclasses.field(
        default_factory=list,
    )

    # The maximum number of requests, which have an identical value in the field
    # specified by the `RateKey`, allowed in a five-minute period. If the number
    # of requests exceeds the `RateLimit` and the other predicates specified in
    # the rule are also met, AWS WAF triggers the action that is specified for
    # this rule.
    rate_limit: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateRateBasedRuleResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `UpdateRateBasedRule`
    # request. You can also use this value to query the status of the request.
    # For more information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateRegexMatchSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "regex_match_set_id",
                "RegexMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "updates",
                "Updates",
                autoboto.TypeInfo(typing.List[RegexMatchSetUpdate]),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `RegexMatchSetId` of the RegexMatchSet that you want to update.
    # `RegexMatchSetId` is returned by CreateRegexMatchSet and by
    # ListRegexMatchSets.
    regex_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An array of `RegexMatchSetUpdate` objects that you want to insert into or
    # delete from a RegexMatchSet. For more information, see RegexMatchTuple.
    updates: typing.List["RegexMatchSetUpdate"] = dataclasses.field(
        default_factory=list,
    )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateRegexMatchSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `UpdateRegexMatchSet`
    # request. You can also use this value to query the status of the request.
    # For more information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateRegexPatternSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "regex_pattern_set_id",
                "RegexPatternSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "updates",
                "Updates",
                autoboto.TypeInfo(typing.List[RegexPatternSetUpdate]),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `RegexPatternSetId` of the RegexPatternSet that you want to update.
    # `RegexPatternSetId` is returned by CreateRegexPatternSet and by
    # ListRegexPatternSets.
    regex_pattern_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An array of `RegexPatternSetUpdate` objects that you want to insert into or
    # delete from a RegexPatternSet.
    updates: typing.List["RegexPatternSetUpdate"] = dataclasses.field(
        default_factory=list,
    )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateRegexPatternSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `UpdateRegexPatternSet`
    # request. You can also use this value to query the status of the request.
    # For more information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateRuleGroupRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_group_id",
                "RuleGroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "updates",
                "Updates",
                autoboto.TypeInfo(typing.List[RuleGroupUpdate]),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `RuleGroupId` of the RuleGroup that you want to update. `RuleGroupId`
    # is returned by CreateRuleGroup and by ListRuleGroups.
    rule_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An array of `RuleGroupUpdate` objects that you want to insert into or
    # delete from a RuleGroup.

    # You can only insert `REGULAR` rules into a rule group.

    # `ActivatedRule|OverrideAction` applies only when updating or adding a
    # `RuleGroup` to a `WebACL`. In this case you do not use
    # `ActivatedRule|Action`. For all other update requests,
    # `ActivatedRule|Action` is used instead of `ActivatedRule|OverrideAction`.
    updates: typing.List["RuleGroupUpdate"] = dataclasses.field(
        default_factory=list,
    )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateRuleGroupResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `UpdateRuleGroup` request.
    # You can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateRuleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_id",
                "RuleId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
            (
                "updates",
                "Updates",
                autoboto.TypeInfo(typing.List[RuleUpdate]),
            ),
        ]

    # The `RuleId` of the `Rule` that you want to update. `RuleId` is returned by
    # `CreateRule` and by ListRules.
    rule_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of `RuleUpdate` objects that you want to insert into or delete
    # from a Rule. For more information, see the applicable data types:

    #   * RuleUpdate: Contains `Action` and `Predicate`

    #   * Predicate: Contains `DataId`, `Negated`, and `Type`

    #   * FieldToMatch: Contains `Data` and `Type`
    updates: typing.List["RuleUpdate"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateRuleResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `UpdateRule` request. You can
    # also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateSizeConstraintSetRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "size_constraint_set_id",
                "SizeConstraintSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
            (
                "updates",
                "Updates",
                autoboto.TypeInfo(typing.List[SizeConstraintSetUpdate]),
            ),
        ]

    # The `SizeConstraintSetId` of the SizeConstraintSet that you want to update.
    # `SizeConstraintSetId` is returned by CreateSizeConstraintSet and by
    # ListSizeConstraintSets.
    size_constraint_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of `SizeConstraintSetUpdate` objects that you want to insert into
    # or delete from a SizeConstraintSet. For more information, see the
    # applicable data types:

    #   * SizeConstraintSetUpdate: Contains `Action` and `SizeConstraint`

    #   * SizeConstraint: Contains `FieldToMatch`, `TextTransformation`, `ComparisonOperator`, and `Size`

    #   * FieldToMatch: Contains `Data` and `Type`
    updates: typing.List["SizeConstraintSetUpdate"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateSizeConstraintSetResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `UpdateSizeConstraintSet`
    # request. You can also use this value to query the status of the request.
    # For more information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateSqlInjectionMatchSetRequest(autoboto.ShapeBase):
    """
    A request to update a SqlInjectionMatchSet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sql_injection_match_set_id",
                "SqlInjectionMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
            (
                "updates",
                "Updates",
                autoboto.TypeInfo(typing.List[SqlInjectionMatchSetUpdate]),
            ),
        ]

    # The `SqlInjectionMatchSetId` of the `SqlInjectionMatchSet` that you want to
    # update. `SqlInjectionMatchSetId` is returned by CreateSqlInjectionMatchSet
    # and by ListSqlInjectionMatchSets.
    sql_injection_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of `SqlInjectionMatchSetUpdate` objects that you want to insert
    # into or delete from a SqlInjectionMatchSet. For more information, see the
    # applicable data types:

    #   * SqlInjectionMatchSetUpdate: Contains `Action` and `SqlInjectionMatchTuple`

    #   * SqlInjectionMatchTuple: Contains `FieldToMatch` and `TextTransformation`

    #   * FieldToMatch: Contains `Data` and `Type`
    updates: typing.List["SqlInjectionMatchSetUpdate"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateSqlInjectionMatchSetResponse(autoboto.ShapeBase):
    """
    The response to an UpdateSqlInjectionMatchSets request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `UpdateSqlInjectionMatchSet`
    # request. You can also use this value to query the status of the request.
    # For more information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateWebACLRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "web_acl_id",
                "WebACLId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
            (
                "updates",
                "Updates",
                autoboto.TypeInfo(typing.List[WebACLUpdate]),
            ),
            (
                "default_action",
                "DefaultAction",
                autoboto.TypeInfo(WafAction),
            ),
        ]

    # The `WebACLId` of the WebACL that you want to update. `WebACLId` is
    # returned by CreateWebACL and by ListWebACLs.
    web_acl_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of updates to make to the WebACL.

    # An array of `WebACLUpdate` objects that you want to insert into or delete
    # from a WebACL. For more information, see the applicable data types:

    #   * WebACLUpdate: Contains `Action` and `ActivatedRule`

    #   * ActivatedRule: Contains `Action`, `OverrideAction`, `Priority`, `RuleId`, and `Type`. `ActivatedRule|OverrideAction` applies only when updating or adding a `RuleGroup` to a `WebACL`. In this case you do not use `ActivatedRule|Action`. For all other update requests, `ActivatedRule|Action` is used instead of `ActivatedRule|OverrideAction`.

    #   * WafAction: Contains `Type`
    updates: typing.List["WebACLUpdate"] = dataclasses.field(
        default_factory=list,
    )

    # A default action for the web ACL, either ALLOW or BLOCK. AWS WAF performs
    # the default action if a request doesn't match the criteria in any of the
    # rules in a web ACL.
    default_action: "WafAction" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateWebACLResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `UpdateWebACL` request. You
    # can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateXssMatchSetRequest(autoboto.ShapeBase):
    """
    A request to update an XssMatchSet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "xss_match_set_id",
                "XssMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
            (
                "updates",
                "Updates",
                autoboto.TypeInfo(typing.List[XssMatchSetUpdate]),
            ),
        ]

    # The `XssMatchSetId` of the `XssMatchSet` that you want to update.
    # `XssMatchSetId` is returned by CreateXssMatchSet and by ListXssMatchSets.
    xss_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The value returned by the most recent call to GetChangeToken.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An array of `XssMatchSetUpdate` objects that you want to insert into or
    # delete from a XssMatchSet. For more information, see the applicable data
    # types:

    #   * XssMatchSetUpdate: Contains `Action` and `XssMatchTuple`

    #   * XssMatchTuple: Contains `FieldToMatch` and `TextTransformation`

    #   * FieldToMatch: Contains `Data` and `Type`
    updates: typing.List["XssMatchSetUpdate"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateXssMatchSetResponse(autoboto.ShapeBase):
    """
    The response to an UpdateXssMatchSets request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "change_token",
                "ChangeToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ChangeToken` that you used to submit the `UpdateXssMatchSet` request.
    # You can also use this value to query the status of the request. For more
    # information, see GetChangeTokenStatus.
    change_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WAFDisallowedNameException(autoboto.ShapeBase):
    """
    The name specified is invalid.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WAFInternalErrorException(autoboto.ShapeBase):
    """
    The operation failed because of a system problem, even though the request was
    valid. Retry your request.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WAFInvalidAccountException(autoboto.ShapeBase):
    """
    The operation failed because you tried to create, update, or delete an object by
    using an invalid account identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class WAFInvalidOperationException(autoboto.ShapeBase):
    """
    The operation failed because there was nothing to do. For example:

      * You tried to remove a `Rule` from a `WebACL`, but the `Rule` isn't in the specified `WebACL`.

      * You tried to remove an IP address from an `IPSet`, but the IP address isn't in the specified `IPSet`.

      * You tried to remove a `ByteMatchTuple` from a `ByteMatchSet`, but the `ByteMatchTuple` isn't in the specified `WebACL`.

      * You tried to add a `Rule` to a `WebACL`, but the `Rule` already exists in the specified `WebACL`.

      * You tried to add an IP address to an `IPSet`, but the IP address already exists in the specified `IPSet`.

      * You tried to add a `ByteMatchTuple` to a `ByteMatchSet`, but the `ByteMatchTuple` already exists in the specified `WebACL`.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WAFInvalidParameterException(autoboto.ShapeBase):
    """
    The operation failed because AWS WAF didn't recognize a parameter in the
    request. For example:

      * You specified an invalid parameter name.

      * You specified an invalid value.

      * You tried to update an object (`ByteMatchSet`, `IPSet`, `Rule`, or `WebACL`) using an action other than `INSERT` or `DELETE`.

      * You tried to create a `WebACL` with a `DefaultAction` `Type` other than `ALLOW`, `BLOCK`, or `COUNT`.

      * You tried to create a `RateBasedRule` with a `RateKey` value other than `IP`.

      * You tried to update a `WebACL` with a `WafAction` `Type` other than `ALLOW`, `BLOCK`, or `COUNT`.

      * You tried to update a `ByteMatchSet` with a `FieldToMatch` `Type` other than HEADER, METHOD, QUERY_STRING, URI, or BODY.

      * You tried to update a `ByteMatchSet` with a `Field` of `HEADER` but no value for `Data`.

      * Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field",
                "field",
                autoboto.TypeInfo(ParameterExceptionField),
            ),
            (
                "parameter",
                "parameter",
                autoboto.TypeInfo(str),
            ),
            (
                "reason",
                "reason",
                autoboto.TypeInfo(ParameterExceptionReason),
            ),
        ]

    field: "ParameterExceptionField" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
    parameter: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
    reason: "ParameterExceptionReason" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class WAFInvalidPermissionPolicyException(autoboto.ShapeBase):
    """
    The operation failed because the specified policy is not in the proper format.

    The policy is subject to the following restrictions:

      * You can attach only one policy with each `PutPermissionPolicy` request.

      * The policy must include an `Effect`, `Action` and `Principal`. 

      * `Effect` must specify `Allow`.

      * The `Action` in the policy must be `waf:UpdateWebACL` or `waf-regional:UpdateWebACL`. Any extra or wildcard actions in the policy will be rejected.

      * The policy cannot include a `Resource` parameter.

      * The ARN in the request must be a valid WAF RuleGroup ARN and the RuleGroup must exist in the same region.

      * The user making the request must be the owner of the RuleGroup.

      * Your policy must be composed using IAM Policy version 2012-10-17.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WAFInvalidRegexPatternException(autoboto.ShapeBase):
    """
    The regular expression (regex) you specified in `RegexPatternString` is invalid.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WAFLimitsExceededException(autoboto.ShapeBase):
    """
    The operation exceeds a resource limit, for example, the maximum number of
    `WebACL` objects that you can create for an AWS account. For more information,
    see [Limits](http://docs.aws.amazon.com/waf/latest/developerguide/limits.html)
    in the _AWS WAF Developer Guide_.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WAFNonEmptyEntityException(autoboto.ShapeBase):
    """
    The operation failed because you tried to delete an object that isn't empty. For
    example:

      * You tried to delete a `WebACL` that still contains one or more `Rule` objects.

      * You tried to delete a `Rule` that still contains one or more `ByteMatchSet` objects or other predicates.

      * You tried to delete a `ByteMatchSet` that contains one or more `ByteMatchTuple` objects.

      * You tried to delete an `IPSet` that references one or more IP addresses.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WAFNonexistentContainerException(autoboto.ShapeBase):
    """
    The operation failed because you tried to add an object to or delete an object
    from another object that doesn't exist. For example:

      * You tried to add a `Rule` to or delete a `Rule` from a `WebACL` that doesn't exist.

      * You tried to add a `ByteMatchSet` to or delete a `ByteMatchSet` from a `Rule` that doesn't exist.

      * You tried to add an IP address to or delete an IP address from an `IPSet` that doesn't exist.

      * You tried to add a `ByteMatchTuple` to or delete a `ByteMatchTuple` from a `ByteMatchSet` that doesn't exist.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WAFNonexistentItemException(autoboto.ShapeBase):
    """
    The operation failed because the referenced object doesn't exist.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WAFReferencedItemException(autoboto.ShapeBase):
    """
    The operation failed because you tried to delete an object that is still in use.
    For example:

      * You tried to delete a `ByteMatchSet` that is still referenced by a `Rule`.

      * You tried to delete a `Rule` that is still referenced by a `WebACL`.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WAFStaleDataException(autoboto.ShapeBase):
    """
    The operation failed because you tried to create, update, or delete an object by
    using a change token that has already been used.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WAFSubscriptionNotFoundException(autoboto.ShapeBase):
    """
    The specified subscription does not exist.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WafAction(autoboto.ShapeBase):
    """
    For the action that is associated with a rule in a `WebACL`, specifies the
    action that you want AWS WAF to perform when a web request matches all of the
    conditions in a rule. For the default action in a `WebACL`, specifies the action
    that you want AWS WAF to take when a web request doesn't match all of the
    conditions in any of the rules in a `WebACL`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(WafActionType),
            ),
        ]

    # Specifies how you want AWS WAF to respond to requests that match the
    # settings in a `Rule`. Valid settings include the following:

    #   * `ALLOW`: AWS WAF allows requests

    #   * `BLOCK`: AWS WAF blocks requests

    #   * `COUNT`: AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify `COUNT` for the default action for a `WebACL`.
    type: "WafActionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class WafActionType(Enum):
    BLOCK = "BLOCK"
    ALLOW = "ALLOW"
    COUNT = "COUNT"


@dataclasses.dataclass
class WafOverrideAction(autoboto.ShapeBase):
    """
    The action to take if any rule within the `RuleGroup` matches a request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(WafOverrideActionType),
            ),
        ]

    # `COUNT` overrides the action specified by the individual rule within a
    # `RuleGroup` . If set to `NONE`, the rule's action will take place.
    type: "WafOverrideActionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class WafOverrideActionType(Enum):
    NONE = "NONE"
    COUNT = "COUNT"


class WafRuleType(Enum):
    REGULAR = "REGULAR"
    RATE_BASED = "RATE_BASED"
    GROUP = "GROUP"


@dataclasses.dataclass
class WebACL(autoboto.ShapeBase):
    """
    Contains the `Rules` that identify the requests that you want to allow, block,
    or count. In a `WebACL`, you also specify a default action (`ALLOW` or `BLOCK`),
    and the action for each `Rule` that you add to a `WebACL`, for example, block
    requests from specified IP addresses or block requests from specified referrers.
    You also associate the `WebACL` with a CloudFront distribution to identify the
    requests that you want AWS WAF to filter. If you add more than one `Rule` to a
    `WebACL`, a request needs to match only one of the specifications to be allowed,
    blocked, or counted. For more information, see UpdateWebACL.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "web_acl_id",
                "WebACLId",
                autoboto.TypeInfo(str),
            ),
            (
                "default_action",
                "DefaultAction",
                autoboto.TypeInfo(WafAction),
            ),
            (
                "rules",
                "Rules",
                autoboto.TypeInfo(typing.List[ActivatedRule]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_name",
                "MetricName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier for a `WebACL`. You use `WebACLId` to get information
    # about a `WebACL` (see GetWebACL), update a `WebACL` (see UpdateWebACL), and
    # delete a `WebACL` from AWS WAF (see DeleteWebACL).

    # `WebACLId` is returned by CreateWebACL and by ListWebACLs.
    web_acl_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The action to perform if none of the `Rules` contained in the `WebACL`
    # match. The action is specified by the WafAction object.
    default_action: "WafAction" = dataclasses.field(default_factory=dict, )

    # An array that contains the action for each `Rule` in a `WebACL`, the
    # priority of the `Rule`, and the ID of the `Rule`.
    rules: typing.List["ActivatedRule"] = dataclasses.field(
        default_factory=list,
    )

    # A friendly name or description of the `WebACL`. You can't change the name
    # of a `WebACL` after you create it.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A friendly name or description for the metrics for this `WebACL`. The name
    # can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't
    # contain whitespace. You can't change `MetricName` after you create the
    # `WebACL`.
    metric_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WebACLSummary(autoboto.ShapeBase):
    """
    Contains the identifier and the name or description of the WebACL.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "web_acl_id",
                "WebACLId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier for a `WebACL`. You use `WebACLId` to get information
    # about a `WebACL` (see GetWebACL), update a `WebACL` (see UpdateWebACL), and
    # delete a `WebACL` from AWS WAF (see DeleteWebACL).

    # `WebACLId` is returned by CreateWebACL and by ListWebACLs.
    web_acl_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A friendly name or description of the WebACL. You can't change the name of
    # a `WebACL` after you create it.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class WebACLUpdate(autoboto.ShapeBase):
    """
    Specifies whether to insert a `Rule` into or delete a `Rule` from a `WebACL`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(ChangeAction),
            ),
            (
                "activated_rule",
                "ActivatedRule",
                autoboto.TypeInfo(ActivatedRule),
            ),
        ]

    # Specifies whether to insert a `Rule` into or delete a `Rule` from a
    # `WebACL`.
    action: "ChangeAction" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The `ActivatedRule` object in an UpdateWebACL request specifies a `Rule`
    # that you want to insert or delete, the priority of the `Rule` in the
    # `WebACL`, and the action that you want AWS WAF to take when a web request
    # matches the `Rule` (`ALLOW`, `BLOCK`, or `COUNT`).
    activated_rule: "ActivatedRule" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class XssMatchSet(autoboto.ShapeBase):
    """
    A complex type that contains `XssMatchTuple` objects, which specify the parts of
    web requests that you want AWS WAF to inspect for cross-site scripting attacks
    and, if you want AWS WAF to inspect a header, the name of the header. If a
    `XssMatchSet` contains more than one `XssMatchTuple` object, a request needs to
    include cross-site scripting attacks in only one of the specified parts of the
    request to be considered a match.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "xss_match_set_id",
                "XssMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "xss_match_tuples",
                "XssMatchTuples",
                autoboto.TypeInfo(typing.List[XssMatchTuple]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier for an `XssMatchSet`. You use `XssMatchSetId` to get
    # information about an `XssMatchSet` (see GetXssMatchSet), update an
    # `XssMatchSet` (see UpdateXssMatchSet), insert an `XssMatchSet` into a
    # `Rule` or delete one from a `Rule` (see UpdateRule), and delete an
    # `XssMatchSet` from AWS WAF (see DeleteXssMatchSet).

    # `XssMatchSetId` is returned by CreateXssMatchSet and by ListXssMatchSets.
    xss_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the parts of web requests that you want to inspect for cross-site
    # scripting attacks.
    xss_match_tuples: typing.List["XssMatchTuple"] = dataclasses.field(
        default_factory=list,
    )

    # The name, if any, of the `XssMatchSet`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class XssMatchSetSummary(autoboto.ShapeBase):
    """
    The `Id` and `Name` of an `XssMatchSet`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "xss_match_set_id",
                "XssMatchSetId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier for an `XssMatchSet`. You use `XssMatchSetId` to get
    # information about a `XssMatchSet` (see GetXssMatchSet), update an
    # `XssMatchSet` (see UpdateXssMatchSet), insert an `XssMatchSet` into a
    # `Rule` or delete one from a `Rule` (see UpdateRule), and delete an
    # `XssMatchSet` from AWS WAF (see DeleteXssMatchSet).

    # `XssMatchSetId` is returned by CreateXssMatchSet and by ListXssMatchSets.
    xss_match_set_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the `XssMatchSet`, if any, specified by `Id`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class XssMatchSetUpdate(autoboto.ShapeBase):
    """
    Specifies the part of a web request that you want to inspect for cross-site
    scripting attacks and indicates whether you want to add the specification to an
    XssMatchSet or delete it from an `XssMatchSet`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(ChangeAction),
            ),
            (
                "xss_match_tuple",
                "XssMatchTuple",
                autoboto.TypeInfo(XssMatchTuple),
            ),
        ]

    # Specify `INSERT` to add a XssMatchSetUpdate to an XssMatchSet. Use `DELETE`
    # to remove a `XssMatchSetUpdate` from an `XssMatchSet`.
    action: "ChangeAction" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the part of a web request that you want AWS WAF to inspect for
    # cross-site scripting attacks and, if you want AWS WAF to inspect a header,
    # the name of the header.
    xss_match_tuple: "XssMatchTuple" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class XssMatchTuple(autoboto.ShapeBase):
    """
    Specifies the part of a web request that you want AWS WAF to inspect for cross-
    site scripting attacks and, if you want AWS WAF to inspect a header, the name of
    the header.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_to_match",
                "FieldToMatch",
                autoboto.TypeInfo(FieldToMatch),
            ),
            (
                "text_transformation",
                "TextTransformation",
                autoboto.TypeInfo(TextTransformation),
            ),
        ]

    # Specifies where in a web request to look for cross-site scripting attacks.
    field_to_match: "FieldToMatch" = dataclasses.field(default_factory=dict, )

    # Text transformations eliminate some of the unusual formatting that
    # attackers use in web requests in an effort to bypass AWS WAF. If you
    # specify a transformation, AWS WAF performs the transformation on
    # `FieldToMatch` before inspecting a request for a match.

    # **CMD_LINE**

    # When you're concerned that attackers are injecting an operating system
    # commandline command and using unusual formatting to disguise some or all of
    # the command, use this option to perform the following transformations:

    #   * Delete the following characters: \ " ' ^

    #   * Delete spaces before the following characters: / (

    #   * Replace the following characters with a space: , ;

    #   * Replace multiple spaces with one space

    #   * Convert uppercase letters (A-Z) to lowercase (a-z)

    # **COMPRESS_WHITE_SPACE**

    # Use this option to replace the following characters with a space character
    # (decimal 32):

    #   * \f, formfeed, decimal 12

    #   * \t, tab, decimal 9

    #   * \n, newline, decimal 10

    #   * \r, carriage return, decimal 13

    #   * \v, vertical tab, decimal 11

    #   * non-breaking space, decimal 160

    # `COMPRESS_WHITE_SPACE` also replaces multiple spaces with one space.

    # **HTML_ENTITY_DECODE**

    # Use this option to replace HTML-encoded characters with unencoded
    # characters. `HTML_ENTITY_DECODE` performs the following operations:

    #   * Replaces `(ampersand)quot;` with `"`

    #   * Replaces `(ampersand)nbsp;` with a non-breaking space, decimal 160

    #   * Replaces `(ampersand)lt;` with a "less than" symbol

    #   * Replaces `(ampersand)gt;` with `>`

    #   * Replaces characters that are represented in hexadecimal format, `(ampersand)#xhhhh;`, with the corresponding characters

    #   * Replaces characters that are represented in decimal format, `(ampersand)#nnnn;`, with the corresponding characters

    # **LOWERCASE**

    # Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

    # **URL_DECODE**

    # Use this option to decode a URL-encoded value.

    # **NONE**

    # Specify `NONE` if you don't want to perform any text transformations.
    text_transformation: "TextTransformation" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
