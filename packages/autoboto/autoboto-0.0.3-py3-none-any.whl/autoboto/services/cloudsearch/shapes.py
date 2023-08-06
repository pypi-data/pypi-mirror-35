import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AccessPoliciesStatus(autoboto.ShapeBase):
    """
    The configured access rules for the domain's document and search endpoints, and
    the current status of those rules.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(OptionStatus),
            ),
        ]

    # Access rules for a domain's document or search service endpoints. For more
    # information, see [Configuring Access for a Search
    # Domain](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
    # access.html) in the _Amazon CloudSearch Developer Guide_. The maximum size
    # of a policy document is 100 KB.
    options: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of domain configuration option.
    status: "OptionStatus" = dataclasses.field(default_factory=dict, )


class AlgorithmicStemming(Enum):
    none = "none"
    minimal = "minimal"
    light = "light"
    full = "full"


@dataclasses.dataclass
class AnalysisOptions(autoboto.ShapeBase):
    """
    Synonyms, stopwords, and stemming options for an analysis scheme. Includes
    tokenization dictionary for Japanese.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "synonyms",
                "Synonyms",
                autoboto.TypeInfo(str),
            ),
            (
                "stopwords",
                "Stopwords",
                autoboto.TypeInfo(str),
            ),
            (
                "stemming_dictionary",
                "StemmingDictionary",
                autoboto.TypeInfo(str),
            ),
            (
                "japanese_tokenization_dictionary",
                "JapaneseTokenizationDictionary",
                autoboto.TypeInfo(str),
            ),
            (
                "algorithmic_stemming",
                "AlgorithmicStemming",
                autoboto.TypeInfo(AlgorithmicStemming),
            ),
        ]

    # A JSON object that defines synonym groups and aliases. A synonym group is
    # an array of arrays, where each sub-array is a group of terms where each
    # term in the group is considered a synonym of every other term in the group.
    # The aliases value is an object that contains a collection of string:value
    # pairs where the string specifies a term and the array of values specifies
    # each of the aliases for that term. An alias is considered a synonym of the
    # specified term, but the term is not considered a synonym of the alias. For
    # more information about specifying synonyms, see
    # [Synonyms](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
    # analysis-schemes.html#synonyms) in the _Amazon CloudSearch Developer
    # Guide_.
    synonyms: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A JSON array of terms to ignore during indexing and searching. For example,
    # `["a", "an", "the", "of"]`. The stopwords dictionary must explicitly list
    # each word you want to ignore. Wildcards and regular expressions are not
    # supported.
    stopwords: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A JSON object that contains a collection of string:value pairs that each
    # map a term to its stem. For example, `{"term1": "stem1", "term2": "stem2",
    # "term3": "stem3"}`. The stemming dictionary is applied in addition to any
    # algorithmic stemming. This enables you to override the results of the
    # algorithmic stemming to correct specific cases of overstemming or
    # understemming. The maximum size of a stemming dictionary is 500 KB.
    stemming_dictionary: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A JSON array that contains a collection of terms, tokens, readings and part
    # of speech for Japanese Tokenizaiton. The Japanese tokenization dictionary
    # enables you to override the default tokenization for selected terms. This
    # is only valid for Japanese language fields.
    japanese_tokenization_dictionary: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The level of algorithmic stemming to perform: `none`, `minimal`, `light`,
    # or `full`. The available levels vary depending on the language. For more
    # information, see [Language Specific Text Processing
    # Settings](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-
    # processing.html#text-processing-settings) in the _Amazon CloudSearch
    # Developer Guide_
    algorithmic_stemming: "AlgorithmicStemming" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class AnalysisScheme(autoboto.ShapeBase):
    """
    Configuration information for an analysis scheme. Each analysis scheme has a
    unique name and specifies the language of the text to be processed. The
    following options can be configured for an analysis scheme: `Synonyms`,
    `Stopwords`, `StemmingDictionary`, `JapaneseTokenizationDictionary` and
    `AlgorithmicStemming`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "analysis_scheme_name",
                "AnalysisSchemeName",
                autoboto.TypeInfo(str),
            ),
            (
                "analysis_scheme_language",
                "AnalysisSchemeLanguage",
                autoboto.TypeInfo(AnalysisSchemeLanguage),
            ),
            (
                "analysis_options",
                "AnalysisOptions",
                autoboto.TypeInfo(AnalysisOptions),
            ),
        ]

    # Names must begin with a letter and can contain the following characters:
    # a-z (lowercase), 0-9, and _ (underscore).
    analysis_scheme_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An [IETF RFC 4646](http://tools.ietf.org/html/rfc4646) language code or
    # `mul` for multiple languages.
    analysis_scheme_language: "AnalysisSchemeLanguage" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Synonyms, stopwords, and stemming options for an analysis scheme. Includes
    # tokenization dictionary for Japanese.
    analysis_options: "AnalysisOptions" = dataclasses.field(
        default_factory=dict,
    )


class AnalysisSchemeLanguage(Enum):
    """
    An [IETF RFC 4646](http://tools.ietf.org/html/rfc4646) language code or `mul`
    for multiple languages.
    """
    ar = "ar"
    bg = "bg"
    ca = "ca"
    cs = "cs"
    da = "da"
    de = "de"
    el = "el"
    en = "en"
    es = "es"
    eu = "eu"
    fa = "fa"
    fi = "fi"
    fr = "fr"
    ga = "ga"
    gl = "gl"
    he = "he"
    hi = "hi"
    hu = "hu"
    hy = "hy"
    id = "id"
    it = "it"
    ja = "ja"
    ko = "ko"
    lv = "lv"
    mul = "mul"
    nl = "nl"
    no = "no"
    pt = "pt"
    ro = "ro"
    ru = "ru"
    sv = "sv"
    th = "th"
    tr = "tr"
    zh_Hans = "zh-Hans"
    zh_Hant = "zh-Hant"


@dataclasses.dataclass
class AnalysisSchemeStatus(autoboto.ShapeBase):
    """
    The status and configuration of an `AnalysisScheme`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                autoboto.TypeInfo(AnalysisScheme),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(OptionStatus),
            ),
        ]

    # Configuration information for an analysis scheme. Each analysis scheme has
    # a unique name and specifies the language of the text to be processed. The
    # following options can be configured for an analysis scheme: `Synonyms`,
    # `Stopwords`, `StemmingDictionary`, `JapaneseTokenizationDictionary` and
    # `AlgorithmicStemming`.
    options: "AnalysisScheme" = dataclasses.field(default_factory=dict, )

    # The status of domain configuration option.
    status: "OptionStatus" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class AvailabilityOptionsStatus(autoboto.ShapeBase):
    """
    The status and configuration of the domain's availability options.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                autoboto.TypeInfo(bool),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(OptionStatus),
            ),
        ]

    # The availability options configured for the domain.
    options: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status of domain configuration option.
    status: "OptionStatus" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class BaseException(autoboto.ShapeBase):
    """
    An error occurred while processing the request.
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
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # A machine-parsable string error or warning code.
    code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A human-readable string error or warning message.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BuildSuggestersRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `BuildSuggester` operation. Specifies the
    name of the domain you want to update.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A string that represents the name of a domain. Domain names are unique
    # across the domains owned by an account within an AWS region. Domain names
    # start with a letter or number and can contain the following characters: a-z
    # (lowercase), 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BuildSuggestersResponse(autoboto.ShapeBase):
    """
    The result of a `BuildSuggester` request. Contains a list of the fields used for
    suggestions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_names",
                "FieldNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A list of field names.
    field_names: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateDomainRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `CreateDomain` operation. Specifies a name
    for the new search domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A name for the domain you are creating. Allowed characters are a-z (lower-
    # case letters), 0-9, and hyphen (-). Domain names must start with a letter
    # or number and be at least 3 and no more than 28 characters long.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateDomainResponse(autoboto.ShapeBase):
    """
    The result of a `CreateDomainRequest`. Contains the status of a newly created
    domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_status",
                "DomainStatus",
                autoboto.TypeInfo(DomainStatus),
            ),
        ]

    # The current status of the search domain.
    domain_status: "DomainStatus" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DateArrayOptions(autoboto.ShapeBase):
    """
    Options for a field that contains an array of dates. Present if `IndexFieldType`
    specifies the field is of type `date-array`. All options are enabled by default.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "default_value",
                "DefaultValue",
                autoboto.TypeInfo(str),
            ),
            (
                "source_fields",
                "SourceFields",
                autoboto.TypeInfo(str),
            ),
            (
                "facet_enabled",
                "FacetEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "search_enabled",
                "SearchEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "return_enabled",
                "ReturnEnabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A value to use for the field if the field isn't specified for a document.
    default_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of source fields to map to the field.
    source_fields: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether facet information can be returned for the field.
    facet_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field are searchable.
    search_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field can be returned in the search results.
    return_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DateOptions(autoboto.ShapeBase):
    """
    Options for a date field. Dates and times are specified in UTC (Coordinated
    Universal Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if
    `IndexFieldType` specifies the field is of type `date`. All options are enabled
    by default.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "default_value",
                "DefaultValue",
                autoboto.TypeInfo(str),
            ),
            (
                "source_field",
                "SourceField",
                autoboto.TypeInfo(str),
            ),
            (
                "facet_enabled",
                "FacetEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "search_enabled",
                "SearchEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "return_enabled",
                "ReturnEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "sort_enabled",
                "SortEnabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A value to use for the field if the field isn't specified for a document.
    default_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A string that represents the name of an index field. CloudSearch supports
    # regular index fields as well as dynamic fields. A dynamic field's name
    # defines a pattern that begins or ends with a wildcard. Any document fields
    # that don't map to a regular index field but do match a dynamic field's
    # pattern are configured with the dynamic field's indexing options.

    # Regular field names begin with a letter and can contain the following
    # characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names
    # must begin or end with a wildcard (*). The wildcard can also be the only
    # character in a dynamic field name. Multiple wildcards, and wildcards
    # embedded within a string are not supported.

    # The name `score` is reserved and cannot be used as a field name. To
    # reference a document's ID, you can use the name `_id`.
    source_field: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Whether facet information can be returned for the field.
    facet_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field are searchable.
    search_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field can be returned in the search results.
    return_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the field can be used to sort the search results.
    sort_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DefineAnalysisSchemeRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DefineAnalysisScheme` operation. Specifies
    the name of the domain you want to update and the analysis scheme configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "analysis_scheme",
                "AnalysisScheme",
                autoboto.TypeInfo(AnalysisScheme),
            ),
        ]

    # A string that represents the name of a domain. Domain names are unique
    # across the domains owned by an account within an AWS region. Domain names
    # start with a letter or number and can contain the following characters: a-z
    # (lowercase), 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Configuration information for an analysis scheme. Each analysis scheme has
    # a unique name and specifies the language of the text to be processed. The
    # following options can be configured for an analysis scheme: `Synonyms`,
    # `Stopwords`, `StemmingDictionary`, `JapaneseTokenizationDictionary` and
    # `AlgorithmicStemming`.
    analysis_scheme: "AnalysisScheme" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DefineAnalysisSchemeResponse(autoboto.ShapeBase):
    """
    The result of a `DefineAnalysisScheme` request. Contains the status of the
    newly-configured analysis scheme.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "analysis_scheme",
                "AnalysisScheme",
                autoboto.TypeInfo(AnalysisSchemeStatus),
            ),
        ]

    # The status and configuration of an `AnalysisScheme`.
    analysis_scheme: "AnalysisSchemeStatus" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DefineExpressionRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DefineExpression` operation. Specifies the
    name of the domain you want to update and the expression you want to configure.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "expression",
                "Expression",
                autoboto.TypeInfo(Expression),
            ),
        ]

    # A string that represents the name of a domain. Domain names are unique
    # across the domains owned by an account within an AWS region. Domain names
    # start with a letter or number and can contain the following characters: a-z
    # (lowercase), 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A named expression that can be evaluated at search time. Can be used to
    # sort the search results, define other expressions, or return computed
    # information in the search results.
    expression: "Expression" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DefineExpressionResponse(autoboto.ShapeBase):
    """
    The result of a `DefineExpression` request. Contains the status of the newly-
    configured expression.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "expression",
                "Expression",
                autoboto.TypeInfo(ExpressionStatus),
            ),
        ]

    # The value of an `Expression` and its current status.
    expression: "ExpressionStatus" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DefineIndexFieldRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DefineIndexField` operation. Specifies the
    name of the domain you want to update and the index field configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "index_field",
                "IndexField",
                autoboto.TypeInfo(IndexField),
            ),
        ]

    # A string that represents the name of a domain. Domain names are unique
    # across the domains owned by an account within an AWS region. Domain names
    # start with a letter or number and can contain the following characters: a-z
    # (lowercase), 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The index field and field options you want to configure.
    index_field: "IndexField" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DefineIndexFieldResponse(autoboto.ShapeBase):
    """
    The result of a `DefineIndexField` request. Contains the status of the newly-
    configured index field.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_field",
                "IndexField",
                autoboto.TypeInfo(IndexFieldStatus),
            ),
        ]

    # The value of an `IndexField` and its current status.
    index_field: "IndexFieldStatus" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DefineSuggesterRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DefineSuggester` operation. Specifies the
    name of the domain you want to update and the suggester configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "suggester",
                "Suggester",
                autoboto.TypeInfo(Suggester),
            ),
        ]

    # A string that represents the name of a domain. Domain names are unique
    # across the domains owned by an account within an AWS region. Domain names
    # start with a letter or number and can contain the following characters: a-z
    # (lowercase), 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Configuration information for a search suggester. Each suggester has a
    # unique name and specifies the text field you want to use for suggestions.
    # The following options can be configured for a suggester: `FuzzyMatching`,
    # `SortExpression`.
    suggester: "Suggester" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DefineSuggesterResponse(autoboto.ShapeBase):
    """
    The result of a `DefineSuggester` request. Contains the status of the newly-
    configured suggester.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "suggester",
                "Suggester",
                autoboto.TypeInfo(SuggesterStatus),
            ),
        ]

    # The value of a `Suggester` and its current status.
    suggester: "SuggesterStatus" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteAnalysisSchemeRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DeleteAnalysisScheme` operation. Specifies
    the name of the domain you want to update and the analysis scheme you want to
    delete.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "analysis_scheme_name",
                "AnalysisSchemeName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A string that represents the name of a domain. Domain names are unique
    # across the domains owned by an account within an AWS region. Domain names
    # start with a letter or number and can contain the following characters: a-z
    # (lowercase), 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the analysis scheme you want to delete.
    analysis_scheme_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteAnalysisSchemeResponse(autoboto.ShapeBase):
    """
    The result of a `DeleteAnalysisScheme` request. Contains the status of the
    deleted analysis scheme.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "analysis_scheme",
                "AnalysisScheme",
                autoboto.TypeInfo(AnalysisSchemeStatus),
            ),
        ]

    # The status of the analysis scheme being deleted.
    analysis_scheme: "AnalysisSchemeStatus" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteDomainRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DeleteDomain` operation. Specifies the name
    of the domain you want to delete.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the domain you want to permanently delete.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteDomainResponse(autoboto.ShapeBase):
    """
    The result of a `DeleteDomain` request. Contains the status of a newly deleted
    domain, or no status if the domain has already been completely deleted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_status",
                "DomainStatus",
                autoboto.TypeInfo(DomainStatus),
            ),
        ]

    # The current status of the search domain.
    domain_status: "DomainStatus" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteExpressionRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DeleteExpression` operation. Specifies the
    name of the domain you want to update and the name of the expression you want to
    delete.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "expression_name",
                "ExpressionName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A string that represents the name of a domain. Domain names are unique
    # across the domains owned by an account within an AWS region. Domain names
    # start with a letter or number and can contain the following characters: a-z
    # (lowercase), 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the `Expression` to delete.
    expression_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteExpressionResponse(autoboto.ShapeBase):
    """
    The result of a `DeleteExpression` request. Specifies the expression being
    deleted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "expression",
                "Expression",
                autoboto.TypeInfo(ExpressionStatus),
            ),
        ]

    # The status of the expression being deleted.
    expression: "ExpressionStatus" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteIndexFieldRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DeleteIndexField` operation. Specifies the
    name of the domain you want to update and the name of the index field you want
    to delete.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "index_field_name",
                "IndexFieldName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A string that represents the name of a domain. Domain names are unique
    # across the domains owned by an account within an AWS region. Domain names
    # start with a letter or number and can contain the following characters: a-z
    # (lowercase), 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the index field your want to remove from the domain's indexing
    # options.
    index_field_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteIndexFieldResponse(autoboto.ShapeBase):
    """
    The result of a `DeleteIndexField` request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_field",
                "IndexField",
                autoboto.TypeInfo(IndexFieldStatus),
            ),
        ]

    # The status of the index field being deleted.
    index_field: "IndexFieldStatus" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteSuggesterRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DeleteSuggester` operation. Specifies the
    name of the domain you want to update and name of the suggester you want to
    delete.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "suggester_name",
                "SuggesterName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A string that represents the name of a domain. Domain names are unique
    # across the domains owned by an account within an AWS region. Domain names
    # start with a letter or number and can contain the following characters: a-z
    # (lowercase), 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the name of the suggester you want to delete.
    suggester_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteSuggesterResponse(autoboto.ShapeBase):
    """
    The result of a `DeleteSuggester` request. Contains the status of the deleted
    suggester.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "suggester",
                "Suggester",
                autoboto.TypeInfo(SuggesterStatus),
            ),
        ]

    # The status of the suggester being deleted.
    suggester: "SuggesterStatus" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeAnalysisSchemesRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DescribeAnalysisSchemes` operation.
    Specifies the name of the domain you want to describe. To limit the response to
    particular analysis schemes, specify the names of the analysis schemes you want
    to describe. To show the active configuration and exclude any pending changes,
    set the `Deployed` option to `true`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "analysis_scheme_names",
                "AnalysisSchemeNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "deployed",
                "Deployed",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the domain you want to describe.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The analysis schemes you want to describe.
    analysis_scheme_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Whether to display the deployed configuration (`true`) or include any
    # pending changes (`false`). Defaults to `false`.
    deployed: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeAnalysisSchemesResponse(autoboto.ShapeBase):
    """
    The result of a `DescribeAnalysisSchemes` request. Contains the analysis schemes
    configured for the domain specified in the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "analysis_schemes",
                "AnalysisSchemes",
                autoboto.TypeInfo(typing.List[AnalysisSchemeStatus]),
            ),
        ]

    # The analysis scheme descriptions.
    analysis_schemes: typing.List["AnalysisSchemeStatus"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeAvailabilityOptionsRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DescribeAvailabilityOptions` operation.
    Specifies the name of the domain you want to describe. To show the active
    configuration and exclude any pending changes, set the Deployed option to
    `true`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "deployed",
                "Deployed",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the domain you want to describe.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Whether to display the deployed configuration (`true`) or include any
    # pending changes (`false`). Defaults to `false`.
    deployed: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeAvailabilityOptionsResponse(autoboto.ShapeBase):
    """
    The result of a `DescribeAvailabilityOptions` request. Indicates whether or not
    the Multi-AZ option is enabled for the domain specified in the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "availability_options",
                "AvailabilityOptions",
                autoboto.TypeInfo(AvailabilityOptionsStatus),
            ),
        ]

    # The availability options configured for the domain. Indicates whether
    # Multi-AZ is enabled for the domain.
    availability_options: "AvailabilityOptionsStatus" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeDomainsRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DescribeDomains` operation. By default
    shows the status of all domains. To restrict the response to particular domains,
    specify the names of the domains you want to describe.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_names",
                "DomainNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The names of the domains you want to include in the response.
    domain_names: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeDomainsResponse(autoboto.ShapeBase):
    """
    The result of a `DescribeDomains` request. Contains the status of the domains
    specified in the request or all domains owned by the account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_status_list",
                "DomainStatusList",
                autoboto.TypeInfo(typing.List[DomainStatus]),
            ),
        ]

    # A list that contains the status of each requested domain.
    domain_status_list: typing.List["DomainStatus"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeExpressionsRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DescribeDomains` operation. Specifies the
    name of the domain you want to describe. To restrict the response to particular
    expressions, specify the names of the expressions you want to describe. To show
    the active configuration and exclude any pending changes, set the `Deployed`
    option to `true`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "expression_names",
                "ExpressionNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "deployed",
                "Deployed",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the domain you want to describe.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Limits the `DescribeExpressions` response to the specified expressions. If
    # not specified, all expressions are shown.
    expression_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Whether to display the deployed configuration (`true`) or include any
    # pending changes (`false`). Defaults to `false`.
    deployed: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeExpressionsResponse(autoboto.ShapeBase):
    """
    The result of a `DescribeExpressions` request. Contains the expressions
    configured for the domain specified in the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "expressions",
                "Expressions",
                autoboto.TypeInfo(typing.List[ExpressionStatus]),
            ),
        ]

    # The expressions configured for the domain.
    expressions: typing.List["ExpressionStatus"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeIndexFieldsRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DescribeIndexFields` operation. Specifies
    the name of the domain you want to describe. To restrict the response to
    particular index fields, specify the names of the index fields you want to
    describe. To show the active configuration and exclude any pending changes, set
    the `Deployed` option to `true`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "field_names",
                "FieldNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "deployed",
                "Deployed",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the domain you want to describe.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of the index fields you want to describe. If not specified,
    # information is returned for all configured index fields.
    field_names: typing.List[str] = dataclasses.field(default_factory=list, )

    # Whether to display the deployed configuration (`true`) or include any
    # pending changes (`false`). Defaults to `false`.
    deployed: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeIndexFieldsResponse(autoboto.ShapeBase):
    """
    The result of a `DescribeIndexFields` request. Contains the index fields
    configured for the domain specified in the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_fields",
                "IndexFields",
                autoboto.TypeInfo(typing.List[IndexFieldStatus]),
            ),
        ]

    # The index fields configured for the domain.
    index_fields: typing.List["IndexFieldStatus"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeScalingParametersRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DescribeScalingParameters` operation.
    Specifies the name of the domain you want to describe.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A string that represents the name of a domain. Domain names are unique
    # across the domains owned by an account within an AWS region. Domain names
    # start with a letter or number and can contain the following characters: a-z
    # (lowercase), 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeScalingParametersResponse(autoboto.ShapeBase):
    """
    The result of a `DescribeScalingParameters` request. Contains the scaling
    parameters configured for the domain specified in the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scaling_parameters",
                "ScalingParameters",
                autoboto.TypeInfo(ScalingParametersStatus),
            ),
        ]

    # The status and configuration of a search domain's scaling parameters.
    scaling_parameters: "ScalingParametersStatus" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeServiceAccessPoliciesRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DescribeServiceAccessPolicies` operation.
    Specifies the name of the domain you want to describe. To show the active
    configuration and exclude any pending changes, set the `Deployed` option to
    `true`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "deployed",
                "Deployed",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the domain you want to describe.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Whether to display the deployed configuration (`true`) or include any
    # pending changes (`false`). Defaults to `false`.
    deployed: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeServiceAccessPoliciesResponse(autoboto.ShapeBase):
    """
    The result of a `DescribeServiceAccessPolicies` request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_policies",
                "AccessPolicies",
                autoboto.TypeInfo(AccessPoliciesStatus),
            ),
        ]

    # The access rules configured for the domain specified in the request.
    access_policies: "AccessPoliciesStatus" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeSuggestersRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `DescribeSuggester` operation. Specifies the
    name of the domain you want to describe. To restrict the response to particular
    suggesters, specify the names of the suggesters you want to describe. To show
    the active configuration and exclude any pending changes, set the `Deployed`
    option to `true`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "suggester_names",
                "SuggesterNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "deployed",
                "Deployed",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the domain you want to describe.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The suggesters you want to describe.
    suggester_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Whether to display the deployed configuration (`true`) or include any
    # pending changes (`false`). Defaults to `false`.
    deployed: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeSuggestersResponse(autoboto.ShapeBase):
    """
    The result of a `DescribeSuggesters` request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "suggesters",
                "Suggesters",
                autoboto.TypeInfo(typing.List[SuggesterStatus]),
            ),
        ]

    # The suggesters configured for the domain specified in the request.
    suggesters: typing.List["SuggesterStatus"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DisabledOperationException(autoboto.ShapeBase):
    """
    The request was rejected because it attempted an operation which is not enabled.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DocumentSuggesterOptions(autoboto.ShapeBase):
    """
    Options for a search suggester.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_field",
                "SourceField",
                autoboto.TypeInfo(str),
            ),
            (
                "fuzzy_matching",
                "FuzzyMatching",
                autoboto.TypeInfo(SuggesterFuzzyMatching),
            ),
            (
                "sort_expression",
                "SortExpression",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the index field you want to use for suggestions.
    source_field: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The level of fuzziness allowed when suggesting matches for a string:
    # `none`, `low`, or `high`. With none, the specified string is treated as an
    # exact prefix. With low, suggestions must differ from the specified string
    # by no more than one character. With high, suggestions can differ by up to
    # two characters. The default is none.
    fuzzy_matching: "SuggesterFuzzyMatching" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An expression that computes a score for each suggestion to control how they
    # are sorted. The scores are rounded to the nearest integer, with a floor of
    # 0 and a ceiling of 2^31-1. A document's relevance score is not computed for
    # suggestions, so sort expressions cannot reference the `_score` value. To
    # sort suggestions using a numeric field or existing expression, simply
    # specify the name of the field or expression. If no expression is configured
    # for the suggester, the suggestions are sorted with the closest matches
    # listed first.
    sort_expression: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DomainStatus(autoboto.ShapeBase):
    """
    The current status of the search domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_id",
                "DomainId",
                autoboto.TypeInfo(str),
            ),
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "requires_index_documents",
                "RequiresIndexDocuments",
                autoboto.TypeInfo(bool),
            ),
            (
                "arn",
                "ARN",
                autoboto.TypeInfo(str),
            ),
            (
                "created",
                "Created",
                autoboto.TypeInfo(bool),
            ),
            (
                "deleted",
                "Deleted",
                autoboto.TypeInfo(bool),
            ),
            (
                "doc_service",
                "DocService",
                autoboto.TypeInfo(ServiceEndpoint),
            ),
            (
                "search_service",
                "SearchService",
                autoboto.TypeInfo(ServiceEndpoint),
            ),
            (
                "processing",
                "Processing",
                autoboto.TypeInfo(bool),
            ),
            (
                "search_instance_type",
                "SearchInstanceType",
                autoboto.TypeInfo(str),
            ),
            (
                "search_partition_count",
                "SearchPartitionCount",
                autoboto.TypeInfo(int),
            ),
            (
                "search_instance_count",
                "SearchInstanceCount",
                autoboto.TypeInfo(int),
            ),
            (
                "limits",
                "Limits",
                autoboto.TypeInfo(Limits),
            ),
        ]

    # An internally generated unique identifier for a domain.
    domain_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A string that represents the name of a domain. Domain names are unique
    # across the domains owned by an account within an AWS region. Domain names
    # start with a letter or number and can contain the following characters: a-z
    # (lowercase), 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # True if IndexDocuments needs to be called to activate the current domain
    # configuration.
    requires_index_documents: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the search domain. See [Identifiers for
    # IAM
    # Entities](http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html)
    # in _Using AWS Identity and Access Management_ for more information.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # True if the search domain is created. It can take several minutes to
    # initialize a domain when CreateDomain is called. Newly created search
    # domains are returned from DescribeDomains with a false value for Created
    # until domain creation is complete.
    created: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # True if the search domain has been deleted. The system must clean up
    # resources dedicated to the search domain when DeleteDomain is called. Newly
    # deleted search domains are returned from DescribeDomains with a true value
    # for IsDeleted for several minutes until resource cleanup is complete.
    deleted: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The service endpoint for updating documents in a search domain.
    doc_service: "ServiceEndpoint" = dataclasses.field(default_factory=dict, )

    # The service endpoint for requesting search results from a search domain.
    search_service: "ServiceEndpoint" = dataclasses.field(
        default_factory=dict,
    )

    # True if processing is being done to activate the current domain
    # configuration.
    processing: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The instance type that is being used to process search requests.
    search_instance_type: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of partitions across which the search index is spread.
    search_partition_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of search instances that are available to process search
    # requests.
    search_instance_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
    limits: "Limits" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DoubleArrayOptions(autoboto.ShapeBase):
    """
    Options for a field that contains an array of double-precision 64-bit floating
    point values. Present if `IndexFieldType` specifies the field is of type
    `double-array`. All options are enabled by default.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "default_value",
                "DefaultValue",
                autoboto.TypeInfo(float),
            ),
            (
                "source_fields",
                "SourceFields",
                autoboto.TypeInfo(str),
            ),
            (
                "facet_enabled",
                "FacetEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "search_enabled",
                "SearchEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "return_enabled",
                "ReturnEnabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A value to use for the field if the field isn't specified for a document.
    default_value: float = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of source fields to map to the field.
    source_fields: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether facet information can be returned for the field.
    facet_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field are searchable.
    search_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field can be returned in the search results.
    return_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DoubleOptions(autoboto.ShapeBase):
    """
    Options for a double-precision 64-bit floating point field. Present if
    `IndexFieldType` specifies the field is of type `double`. All options are
    enabled by default.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "default_value",
                "DefaultValue",
                autoboto.TypeInfo(float),
            ),
            (
                "source_field",
                "SourceField",
                autoboto.TypeInfo(str),
            ),
            (
                "facet_enabled",
                "FacetEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "search_enabled",
                "SearchEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "return_enabled",
                "ReturnEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "sort_enabled",
                "SortEnabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A value to use for the field if the field isn't specified for a document.
    # This can be important if you are using the field in an expression and that
    # field is not present in every document.
    default_value: float = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the source field to map to the field.
    source_field: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Whether facet information can be returned for the field.
    facet_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field are searchable.
    search_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field can be returned in the search results.
    return_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the field can be used to sort the search results.
    sort_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Expression(autoboto.ShapeBase):
    """
    A named expression that can be evaluated at search time. Can be used to sort the
    search results, define other expressions, or return computed information in the
    search results.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "expression_name",
                "ExpressionName",
                autoboto.TypeInfo(str),
            ),
            (
                "expression_value",
                "ExpressionValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # Names must begin with a letter and can contain the following characters:
    # a-z (lowercase), 0-9, and _ (underscore).
    expression_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The expression to evaluate for sorting while processing a search request.
    # The `Expression` syntax is based on JavaScript expressions. For more
    # information, see [Configuring
    # Expressions](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
    # expressions.html) in the _Amazon CloudSearch Developer Guide_.
    expression_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ExpressionStatus(autoboto.ShapeBase):
    """
    The value of an `Expression` and its current status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                autoboto.TypeInfo(Expression),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(OptionStatus),
            ),
        ]

    # The expression that is evaluated for sorting while processing a search
    # request.
    options: "Expression" = dataclasses.field(default_factory=dict, )

    # The status of domain configuration option.
    status: "OptionStatus" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class IndexDocumentsRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `IndexDocuments` operation. Specifies the
    name of the domain you want to re-index.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A string that represents the name of a domain. Domain names are unique
    # across the domains owned by an account within an AWS region. Domain names
    # start with a letter or number and can contain the following characters: a-z
    # (lowercase), 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class IndexDocumentsResponse(autoboto.ShapeBase):
    """
    The result of an `IndexDocuments` request. Contains the status of the indexing
    operation, including the fields being indexed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_names",
                "FieldNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The names of the fields that are currently being indexed.
    field_names: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class IndexField(autoboto.ShapeBase):
    """
    Configuration information for a field in the index, including its name, type,
    and options. The supported options depend on the `IndexFieldType`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_field_name",
                "IndexFieldName",
                autoboto.TypeInfo(str),
            ),
            (
                "index_field_type",
                "IndexFieldType",
                autoboto.TypeInfo(IndexFieldType),
            ),
            (
                "int_options",
                "IntOptions",
                autoboto.TypeInfo(IntOptions),
            ),
            (
                "double_options",
                "DoubleOptions",
                autoboto.TypeInfo(DoubleOptions),
            ),
            (
                "literal_options",
                "LiteralOptions",
                autoboto.TypeInfo(LiteralOptions),
            ),
            (
                "text_options",
                "TextOptions",
                autoboto.TypeInfo(TextOptions),
            ),
            (
                "date_options",
                "DateOptions",
                autoboto.TypeInfo(DateOptions),
            ),
            (
                "lat_lon_options",
                "LatLonOptions",
                autoboto.TypeInfo(LatLonOptions),
            ),
            (
                "int_array_options",
                "IntArrayOptions",
                autoboto.TypeInfo(IntArrayOptions),
            ),
            (
                "double_array_options",
                "DoubleArrayOptions",
                autoboto.TypeInfo(DoubleArrayOptions),
            ),
            (
                "literal_array_options",
                "LiteralArrayOptions",
                autoboto.TypeInfo(LiteralArrayOptions),
            ),
            (
                "text_array_options",
                "TextArrayOptions",
                autoboto.TypeInfo(TextArrayOptions),
            ),
            (
                "date_array_options",
                "DateArrayOptions",
                autoboto.TypeInfo(DateArrayOptions),
            ),
        ]

    # A string that represents the name of an index field. CloudSearch supports
    # regular index fields as well as dynamic fields. A dynamic field's name
    # defines a pattern that begins or ends with a wildcard. Any document fields
    # that don't map to a regular index field but do match a dynamic field's
    # pattern are configured with the dynamic field's indexing options.

    # Regular field names begin with a letter and can contain the following
    # characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names
    # must begin or end with a wildcard (*). The wildcard can also be the only
    # character in a dynamic field name. Multiple wildcards, and wildcards
    # embedded within a string are not supported.

    # The name `score` is reserved and cannot be used as a field name. To
    # reference a document's ID, you can use the name `_id`.
    index_field_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of field. The valid options for a field depend on the field type.
    # For more information about the supported field types, see [Configuring
    # Index
    # Fields](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
    # index-fields.html) in the _Amazon CloudSearch Developer Guide_.
    index_field_type: "IndexFieldType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Options for a 64-bit signed integer field. Present if `IndexFieldType`
    # specifies the field is of type `int`. All options are enabled by default.
    int_options: "IntOptions" = dataclasses.field(default_factory=dict, )

    # Options for a double-precision 64-bit floating point field. Present if
    # `IndexFieldType` specifies the field is of type `double`. All options are
    # enabled by default.
    double_options: "DoubleOptions" = dataclasses.field(default_factory=dict, )

    # Options for literal field. Present if `IndexFieldType` specifies the field
    # is of type `literal`. All options are enabled by default.
    literal_options: "LiteralOptions" = dataclasses.field(
        default_factory=dict,
    )

    # Options for text field. Present if `IndexFieldType` specifies the field is
    # of type `text`. A `text` field is always searchable. All options are
    # enabled by default.
    text_options: "TextOptions" = dataclasses.field(default_factory=dict, )

    # Options for a date field. Dates and times are specified in UTC (Coordinated
    # Universal Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if
    # `IndexFieldType` specifies the field is of type `date`. All options are
    # enabled by default.
    date_options: "DateOptions" = dataclasses.field(default_factory=dict, )

    # Options for a latlon field. A latlon field contains a location stored as a
    # latitude and longitude value pair. Present if `IndexFieldType` specifies
    # the field is of type `latlon`. All options are enabled by default.
    lat_lon_options: "LatLonOptions" = dataclasses.field(default_factory=dict, )

    # Options for a field that contains an array of 64-bit signed integers.
    # Present if `IndexFieldType` specifies the field is of type `int-array`. All
    # options are enabled by default.
    int_array_options: "IntArrayOptions" = dataclasses.field(
        default_factory=dict,
    )

    # Options for a field that contains an array of double-precision 64-bit
    # floating point values. Present if `IndexFieldType` specifies the field is
    # of type `double-array`. All options are enabled by default.
    double_array_options: "DoubleArrayOptions" = dataclasses.field(
        default_factory=dict,
    )

    # Options for a field that contains an array of literal strings. Present if
    # `IndexFieldType` specifies the field is of type `literal-array`. All
    # options are enabled by default.
    literal_array_options: "LiteralArrayOptions" = dataclasses.field(
        default_factory=dict,
    )

    # Options for a field that contains an array of text strings. Present if
    # `IndexFieldType` specifies the field is of type `text-array`. A `text-
    # array` field is always searchable. All options are enabled by default.
    text_array_options: "TextArrayOptions" = dataclasses.field(
        default_factory=dict,
    )

    # Options for a field that contains an array of dates. Present if
    # `IndexFieldType` specifies the field is of type `date-array`. All options
    # are enabled by default.
    date_array_options: "DateArrayOptions" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class IndexFieldStatus(autoboto.ShapeBase):
    """
    The value of an `IndexField` and its current status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                autoboto.TypeInfo(IndexField),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(OptionStatus),
            ),
        ]

    # Configuration information for a field in the index, including its name,
    # type, and options. The supported options depend on the `IndexFieldType`.
    options: "IndexField" = dataclasses.field(default_factory=dict, )

    # The status of domain configuration option.
    status: "OptionStatus" = dataclasses.field(default_factory=dict, )


class IndexFieldType(Enum):
    """
    The type of field. The valid options for a field depend on the field type. For
    more information about the supported field types, see [Configuring Index
    Fields](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-
    index-fields.html) in the _Amazon CloudSearch Developer Guide_.
    """
    int = "int"
    double = "double"
    literal = "literal"
    text = "text"
    date = "date"
    latlon = "latlon"
    int_array = "int-array"
    double_array = "double-array"
    literal_array = "literal-array"
    text_array = "text-array"
    date_array = "date-array"


@dataclasses.dataclass
class IntArrayOptions(autoboto.ShapeBase):
    """
    Options for a field that contains an array of 64-bit signed integers. Present if
    `IndexFieldType` specifies the field is of type `int-array`. All options are
    enabled by default.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "default_value",
                "DefaultValue",
                autoboto.TypeInfo(int),
            ),
            (
                "source_fields",
                "SourceFields",
                autoboto.TypeInfo(str),
            ),
            (
                "facet_enabled",
                "FacetEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "search_enabled",
                "SearchEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "return_enabled",
                "ReturnEnabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A value to use for the field if the field isn't specified for a document.
    default_value: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of source fields to map to the field.
    source_fields: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether facet information can be returned for the field.
    facet_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field are searchable.
    search_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field can be returned in the search results.
    return_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class IntOptions(autoboto.ShapeBase):
    """
    Options for a 64-bit signed integer field. Present if `IndexFieldType` specifies
    the field is of type `int`. All options are enabled by default.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "default_value",
                "DefaultValue",
                autoboto.TypeInfo(int),
            ),
            (
                "source_field",
                "SourceField",
                autoboto.TypeInfo(str),
            ),
            (
                "facet_enabled",
                "FacetEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "search_enabled",
                "SearchEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "return_enabled",
                "ReturnEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "sort_enabled",
                "SortEnabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A value to use for the field if the field isn't specified for a document.
    # This can be important if you are using the field in an expression and that
    # field is not present in every document.
    default_value: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the source field to map to the field.
    source_field: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Whether facet information can be returned for the field.
    facet_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field are searchable.
    search_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field can be returned in the search results.
    return_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the field can be used to sort the search results.
    sort_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class InternalException(autoboto.ShapeBase):
    """
    An internal error occurred while processing the request. If this problem
    persists, report an issue from the [Service Health
    Dashboard](http://status.aws.amazon.com/).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTypeException(autoboto.ShapeBase):
    """
    The request was rejected because it specified an invalid type definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LatLonOptions(autoboto.ShapeBase):
    """
    Options for a latlon field. A latlon field contains a location stored as a
    latitude and longitude value pair. Present if `IndexFieldType` specifies the
    field is of type `latlon`. All options are enabled by default.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "default_value",
                "DefaultValue",
                autoboto.TypeInfo(str),
            ),
            (
                "source_field",
                "SourceField",
                autoboto.TypeInfo(str),
            ),
            (
                "facet_enabled",
                "FacetEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "search_enabled",
                "SearchEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "return_enabled",
                "ReturnEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "sort_enabled",
                "SortEnabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A value to use for the field if the field isn't specified for a document.
    default_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A string that represents the name of an index field. CloudSearch supports
    # regular index fields as well as dynamic fields. A dynamic field's name
    # defines a pattern that begins or ends with a wildcard. Any document fields
    # that don't map to a regular index field but do match a dynamic field's
    # pattern are configured with the dynamic field's indexing options.

    # Regular field names begin with a letter and can contain the following
    # characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names
    # must begin or end with a wildcard (*). The wildcard can also be the only
    # character in a dynamic field name. Multiple wildcards, and wildcards
    # embedded within a string are not supported.

    # The name `score` is reserved and cannot be used as a field name. To
    # reference a document's ID, you can use the name `_id`.
    source_field: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Whether facet information can be returned for the field.
    facet_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field are searchable.
    search_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field can be returned in the search results.
    return_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the field can be used to sort the search results.
    sort_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    The request was rejected because a resource limit has already been met.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Limits(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "maximum_replication_count",
                "MaximumReplicationCount",
                autoboto.TypeInfo(int),
            ),
            (
                "maximum_partition_count",
                "MaximumPartitionCount",
                autoboto.TypeInfo(int),
            ),
        ]

    maximum_replication_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
    maximum_partition_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListDomainNamesResponse(autoboto.ShapeBase):
    """
    The result of a `ListDomainNames` request. Contains a list of the domains owned
    by an account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_names",
                "DomainNames",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The names of the search domains owned by an account.
    domain_names: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class LiteralArrayOptions(autoboto.ShapeBase):
    """
    Options for a field that contains an array of literal strings. Present if
    `IndexFieldType` specifies the field is of type `literal-array`. All options are
    enabled by default.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "default_value",
                "DefaultValue",
                autoboto.TypeInfo(str),
            ),
            (
                "source_fields",
                "SourceFields",
                autoboto.TypeInfo(str),
            ),
            (
                "facet_enabled",
                "FacetEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "search_enabled",
                "SearchEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "return_enabled",
                "ReturnEnabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A value to use for the field if the field isn't specified for a document.
    default_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of source fields to map to the field.
    source_fields: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether facet information can be returned for the field.
    facet_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field are searchable.
    search_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field can be returned in the search results.
    return_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class LiteralOptions(autoboto.ShapeBase):
    """
    Options for literal field. Present if `IndexFieldType` specifies the field is of
    type `literal`. All options are enabled by default.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "default_value",
                "DefaultValue",
                autoboto.TypeInfo(str),
            ),
            (
                "source_field",
                "SourceField",
                autoboto.TypeInfo(str),
            ),
            (
                "facet_enabled",
                "FacetEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "search_enabled",
                "SearchEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "return_enabled",
                "ReturnEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "sort_enabled",
                "SortEnabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A value to use for the field if the field isn't specified for a document.
    default_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A string that represents the name of an index field. CloudSearch supports
    # regular index fields as well as dynamic fields. A dynamic field's name
    # defines a pattern that begins or ends with a wildcard. Any document fields
    # that don't map to a regular index field but do match a dynamic field's
    # pattern are configured with the dynamic field's indexing options.

    # Regular field names begin with a letter and can contain the following
    # characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names
    # must begin or end with a wildcard (*). The wildcard can also be the only
    # character in a dynamic field name. Multiple wildcards, and wildcards
    # embedded within a string are not supported.

    # The name `score` is reserved and cannot be used as a field name. To
    # reference a document's ID, you can use the name `_id`.
    source_field: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Whether facet information can be returned for the field.
    facet_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field are searchable.
    search_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field can be returned in the search results.
    return_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the field can be used to sort the search results.
    sort_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class OptionState(Enum):
    """
    The state of processing a change to an option. One of:

      * RequiresIndexDocuments: The option's latest value will not be deployed until IndexDocuments has been called and indexing is complete.
      * Processing: The option's latest value is in the process of being activated.
      * Active: The option's latest value is fully deployed. 
      * FailedToValidate: The option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    """
    RequiresIndexDocuments = "RequiresIndexDocuments"
    Processing = "Processing"
    Active = "Active"
    FailedToValidate = "FailedToValidate"


@dataclasses.dataclass
class OptionStatus(autoboto.ShapeBase):
    """
    The status of domain configuration option.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "update_date",
                "UpdateDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(OptionState),
            ),
            (
                "update_version",
                "UpdateVersion",
                autoboto.TypeInfo(int),
            ),
            (
                "pending_deletion",
                "PendingDeletion",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A timestamp for when this option was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A timestamp for when this option was last updated.
    update_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The state of processing a change to an option. Possible values:

    #   * `RequiresIndexDocuments`: the option's latest value will not be deployed until IndexDocuments has been called and indexing is complete.
    #   * `Processing`: the option's latest value is in the process of being activated.
    #   * `Active`: the option's latest value is completely deployed.
    #   * `FailedToValidate`: the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    state: "OptionState" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A unique integer that indicates when this option was last updated.
    update_version: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates that the option will be deleted once processing is complete.
    pending_deletion: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class PartitionInstanceType(Enum):
    """
    The instance type (such as `search.m1.small`) on which an index partition is
    hosted.
    """
    search_m1_small = "search.m1.small"
    search_m1_large = "search.m1.large"
    search_m2_xlarge = "search.m2.xlarge"
    search_m2_2xlarge = "search.m2.2xlarge"
    search_m3_medium = "search.m3.medium"
    search_m3_large = "search.m3.large"
    search_m3_xlarge = "search.m3.xlarge"
    search_m3_2xlarge = "search.m3.2xlarge"


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    The request was rejected because it attempted to reference a resource that does
    not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ScalingParameters(autoboto.ShapeBase):
    """
    The desired instance type and desired number of replicas of each index
    partition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "desired_instance_type",
                "DesiredInstanceType",
                autoboto.TypeInfo(PartitionInstanceType),
            ),
            (
                "desired_replication_count",
                "DesiredReplicationCount",
                autoboto.TypeInfo(int),
            ),
            (
                "desired_partition_count",
                "DesiredPartitionCount",
                autoboto.TypeInfo(int),
            ),
        ]

    # The instance type that you want to preconfigure for your domain. For
    # example, `search.m1.small`.
    desired_instance_type: "PartitionInstanceType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of replicas you want to preconfigure for each index partition.
    desired_replication_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of partitions you want to preconfigure for your domain. Only
    # valid when you select `m2.2xlarge` as the desired instance type.
    desired_partition_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ScalingParametersStatus(autoboto.ShapeBase):
    """
    The status and configuration of a search domain's scaling parameters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                autoboto.TypeInfo(ScalingParameters),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(OptionStatus),
            ),
        ]

    # The desired instance type and desired number of replicas of each index
    # partition.
    options: "ScalingParameters" = dataclasses.field(default_factory=dict, )

    # The status of domain configuration option.
    status: "OptionStatus" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ServiceEndpoint(autoboto.ShapeBase):
    """
    The endpoint to which service requests can be submitted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint",
                "Endpoint",
                autoboto.TypeInfo(str),
            ),
        ]

    # The endpoint to which service requests can be submitted. For example,
    # `search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-
    # west-1.cloudsearch.amazonaws.com` or `doc-imdb-movies-
    # oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com`.
    endpoint: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Suggester(autoboto.ShapeBase):
    """
    Configuration information for a search suggester. Each suggester has a unique
    name and specifies the text field you want to use for suggestions. The following
    options can be configured for a suggester: `FuzzyMatching`, `SortExpression`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "suggester_name",
                "SuggesterName",
                autoboto.TypeInfo(str),
            ),
            (
                "document_suggester_options",
                "DocumentSuggesterOptions",
                autoboto.TypeInfo(DocumentSuggesterOptions),
            ),
        ]

    # Names must begin with a letter and can contain the following characters:
    # a-z (lowercase), 0-9, and _ (underscore).
    suggester_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Options for a search suggester.
    document_suggester_options: "DocumentSuggesterOptions" = dataclasses.field(
        default_factory=dict,
    )


class SuggesterFuzzyMatching(Enum):
    none = "none"
    low = "low"
    high = "high"


@dataclasses.dataclass
class SuggesterStatus(autoboto.ShapeBase):
    """
    The value of a `Suggester` and its current status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "options",
                "Options",
                autoboto.TypeInfo(Suggester),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(OptionStatus),
            ),
        ]

    # Configuration information for a search suggester. Each suggester has a
    # unique name and specifies the text field you want to use for suggestions.
    # The following options can be configured for a suggester: `FuzzyMatching`,
    # `SortExpression`.
    options: "Suggester" = dataclasses.field(default_factory=dict, )

    # The status of domain configuration option.
    status: "OptionStatus" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class TextArrayOptions(autoboto.ShapeBase):
    """
    Options for a field that contains an array of text strings. Present if
    `IndexFieldType` specifies the field is of type `text-array`. A `text-array`
    field is always searchable. All options are enabled by default.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "default_value",
                "DefaultValue",
                autoboto.TypeInfo(str),
            ),
            (
                "source_fields",
                "SourceFields",
                autoboto.TypeInfo(str),
            ),
            (
                "return_enabled",
                "ReturnEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "highlight_enabled",
                "HighlightEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "analysis_scheme",
                "AnalysisScheme",
                autoboto.TypeInfo(str),
            ),
        ]

    # A value to use for the field if the field isn't specified for a document.
    default_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of source fields to map to the field.
    source_fields: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the contents of the field can be returned in the search results.
    return_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether highlights can be returned for the field.
    highlight_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of an analysis scheme for a `text-array` field.
    analysis_scheme: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class TextOptions(autoboto.ShapeBase):
    """
    Options for text field. Present if `IndexFieldType` specifies the field is of
    type `text`. A `text` field is always searchable. All options are enabled by
    default.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "default_value",
                "DefaultValue",
                autoboto.TypeInfo(str),
            ),
            (
                "source_field",
                "SourceField",
                autoboto.TypeInfo(str),
            ),
            (
                "return_enabled",
                "ReturnEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "sort_enabled",
                "SortEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "highlight_enabled",
                "HighlightEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "analysis_scheme",
                "AnalysisScheme",
                autoboto.TypeInfo(str),
            ),
        ]

    # A value to use for the field if the field isn't specified for a document.
    default_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A string that represents the name of an index field. CloudSearch supports
    # regular index fields as well as dynamic fields. A dynamic field's name
    # defines a pattern that begins or ends with a wildcard. Any document fields
    # that don't map to a regular index field but do match a dynamic field's
    # pattern are configured with the dynamic field's indexing options.

    # Regular field names begin with a letter and can contain the following
    # characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names
    # must begin or end with a wildcard (*). The wildcard can also be the only
    # character in a dynamic field name. Multiple wildcards, and wildcards
    # embedded within a string are not supported.

    # The name `score` is reserved and cannot be used as a field name. To
    # reference a document's ID, you can use the name `_id`.
    source_field: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Whether the contents of the field can be returned in the search results.
    return_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether the field can be used to sort the search results.
    sort_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether highlights can be returned for the field.
    highlight_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of an analysis scheme for a `text` field.
    analysis_scheme: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateAvailabilityOptionsRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `UpdateAvailabilityOptions` operation.
    Specifies the name of the domain you want to update and the Multi-AZ
    availability option.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "multi_az",
                "MultiAZ",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A string that represents the name of a domain. Domain names are unique
    # across the domains owned by an account within an AWS region. Domain names
    # start with a letter or number and can contain the following characters: a-z
    # (lowercase), 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # You expand an existing search domain to a second Availability Zone by
    # setting the Multi-AZ option to true. Similarly, you can turn off the Multi-
    # AZ option to downgrade the domain to a single Availability Zone by setting
    # the Multi-AZ option to `false`.
    multi_az: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateAvailabilityOptionsResponse(autoboto.ShapeBase):
    """
    The result of a `UpdateAvailabilityOptions` request. Contains the status of the
    domain's availability options.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "availability_options",
                "AvailabilityOptions",
                autoboto.TypeInfo(AvailabilityOptionsStatus),
            ),
        ]

    # The newly-configured availability options. Indicates whether Multi-AZ is
    # enabled for the domain.
    availability_options: "AvailabilityOptionsStatus" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateScalingParametersRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `UpdateScalingParameters` operation.
    Specifies the name of the domain you want to update and the scaling parameters
    you want to configure.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "scaling_parameters",
                "ScalingParameters",
                autoboto.TypeInfo(ScalingParameters),
            ),
        ]

    # A string that represents the name of a domain. Domain names are unique
    # across the domains owned by an account within an AWS region. Domain names
    # start with a letter or number and can contain the following characters: a-z
    # (lowercase), 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The desired instance type and desired number of replicas of each index
    # partition.
    scaling_parameters: "ScalingParameters" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateScalingParametersResponse(autoboto.ShapeBase):
    """
    The result of a `UpdateScalingParameters` request. Contains the status of the
    newly-configured scaling parameters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scaling_parameters",
                "ScalingParameters",
                autoboto.TypeInfo(ScalingParametersStatus),
            ),
        ]

    # The status and configuration of a search domain's scaling parameters.
    scaling_parameters: "ScalingParametersStatus" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateServiceAccessPoliciesRequest(autoboto.ShapeBase):
    """
    Container for the parameters to the `UpdateServiceAccessPolicies` operation.
    Specifies the name of the domain you want to update and the access rules you
    want to configure.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "access_policies",
                "AccessPolicies",
                autoboto.TypeInfo(str),
            ),
        ]

    # A string that represents the name of a domain. Domain names are unique
    # across the domains owned by an account within an AWS region. Domain names
    # start with a letter or number and can contain the following characters: a-z
    # (lowercase), 0-9, and - (hyphen).
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The access rules you want to configure. These rules replace any existing
    # rules.
    access_policies: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateServiceAccessPoliciesResponse(autoboto.ShapeBase):
    """
    The result of an `UpdateServiceAccessPolicies` request. Contains the new access
    policies.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_policies",
                "AccessPolicies",
                autoboto.TypeInfo(AccessPoliciesStatus),
            ),
        ]

    # The access rules configured for the domain.
    access_policies: "AccessPoliciesStatus" = dataclasses.field(
        default_factory=dict,
    )
