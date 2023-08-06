import datetime
import typing
import autoboto
import botocore.response
from enum import Enum
import dataclasses


class AudioStream(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class DeleteLexiconInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the lexicon to delete. Must be an existing lexicon in the
    # region.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteLexiconOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeVoicesInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "language_code",
                "LanguageCode",
                autoboto.TypeInfo(LanguageCode),
            ),
            (
                "include_additional_language_codes",
                "IncludeAdditionalLanguageCodes",
                autoboto.TypeInfo(bool),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The language identification tag (ISO 639 code for the language name-ISO
    # 3166 country code) for filtering the list of voices returned. If you don't
    # specify this optional parameter, all available voices are returned.
    language_code: "LanguageCode" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Boolean value indicating whether to return any bilingual voices that use
    # the specified language as an additional language. For instance, if you
    # request all languages that use US English (es-US), and there is an Italian
    # voice that speaks both Italian (it-IT) and US English, that voice will be
    # included if you specify `yes` but not if you specify `no`.
    include_additional_language_codes: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An opaque pagination token returned from the previous `DescribeVoices`
    # operation. If present, this indicates where to continue the listing.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeVoicesOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "voices",
                "Voices",
                autoboto.TypeInfo(typing.List[Voice]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of voices with their properties.
    voices: typing.List["Voice"] = dataclasses.field(default_factory=list, )

    # The pagination token to use in the next request to continue the listing of
    # voices. `NextToken` is returned only if the response is truncated.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class Gender(Enum):
    Female = "Female"
    Male = "Male"


@dataclasses.dataclass
class GetLexiconInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the lexicon.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetLexiconOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lexicon",
                "Lexicon",
                autoboto.TypeInfo(Lexicon),
            ),
            (
                "lexicon_attributes",
                "LexiconAttributes",
                autoboto.TypeInfo(LexiconAttributes),
            ),
        ]

    # Lexicon object that provides name and the string content of the lexicon.
    lexicon: "Lexicon" = dataclasses.field(default_factory=dict, )

    # Metadata of the lexicon, including phonetic alphabetic used, language code,
    # lexicon ARN, number of lexemes defined in the lexicon, and size of lexicon
    # in bytes.
    lexicon_attributes: "LexiconAttributes" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetSpeechSynthesisTaskInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "TaskId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Polly generated identifier for a speech synthesis task.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetSpeechSynthesisTaskOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "synthesis_task",
                "SynthesisTask",
                autoboto.TypeInfo(SynthesisTask),
            ),
        ]

    # SynthesisTask object that provides information from the requested task,
    # including output format, creation time, task status, and so on.
    synthesis_task: "SynthesisTask" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class InvalidLexiconException(autoboto.ShapeBase):
    """
    Amazon Polly can't find the specified lexicon. Verify that the lexicon's name is
    spelled correctly, and then try again.
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
class InvalidNextTokenException(autoboto.ShapeBase):
    """
    The NextToken is invalid. Verify that it's spelled correctly, and then try
    again.
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
class InvalidS3BucketException(autoboto.ShapeBase):
    """
    The provided Amazon S3 bucket name is invalid. Please check your input with S3
    bucket naming requirements and try again.
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
class InvalidS3KeyException(autoboto.ShapeBase):
    """
    The provided Amazon S3 key prefix is invalid. Please provide a valid S3 object
    key name.
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
class InvalidSampleRateException(autoboto.ShapeBase):
    """
    The specified sample rate is not valid.
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
class InvalidSnsTopicArnException(autoboto.ShapeBase):
    """
    The provided SNS topic ARN is invalid. Please provide a valid SNS topic ARN and
    try again.
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
class InvalidSsmlException(autoboto.ShapeBase):
    """
    The SSML you provided is invalid. Verify the SSML syntax, spelling of tags and
    values, and then try again.
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
class InvalidTaskIdException(autoboto.ShapeBase):
    """
    The provided Task ID is not valid. Please provide a valid Task ID and try again.
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


class LanguageCode(Enum):
    cy_GB = "cy-GB"
    da_DK = "da-DK"
    de_DE = "de-DE"
    en_AU = "en-AU"
    en_GB = "en-GB"
    en_GB_WLS = "en-GB-WLS"
    en_IN = "en-IN"
    en_US = "en-US"
    es_ES = "es-ES"
    es_US = "es-US"
    fr_CA = "fr-CA"
    fr_FR = "fr-FR"
    is_IS = "is-IS"
    it_IT = "it-IT"
    ja_JP = "ja-JP"
    hi_IN = "hi-IN"
    ko_KR = "ko-KR"
    nb_NO = "nb-NO"
    nl_NL = "nl-NL"
    pl_PL = "pl-PL"
    pt_BR = "pt-BR"
    pt_PT = "pt-PT"
    ro_RO = "ro-RO"
    ru_RU = "ru-RU"
    sv_SE = "sv-SE"
    tr_TR = "tr-TR"


@dataclasses.dataclass
class LanguageNotSupportedException(autoboto.ShapeBase):
    """
    The language specified is not currently supported by Amazon Polly in this
    capacity.
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
class Lexicon(autoboto.ShapeBase):
    """
    Provides lexicon name and lexicon content in string format. For more
    information, see [Pronunciation Lexicon Specification (PLS) Version
    1.0](https://www.w3.org/TR/pronunciation-lexicon/).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "content",
                "Content",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # Lexicon content in string format. The content of a lexicon must be in PLS
    # format.
    content: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Name of the lexicon.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LexiconAttributes(autoboto.ShapeBase):
    """
    Contains metadata describing the lexicon such as the number of lexemes, language
    code, and so on. For more information, see [Managing
    Lexicons](http://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alphabet",
                "Alphabet",
                autoboto.TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                autoboto.TypeInfo(LanguageCode),
            ),
            (
                "last_modified",
                "LastModified",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "lexicon_arn",
                "LexiconArn",
                autoboto.TypeInfo(str),
            ),
            (
                "lexemes_count",
                "LexemesCount",
                autoboto.TypeInfo(int),
            ),
            (
                "size",
                "Size",
                autoboto.TypeInfo(int),
            ),
        ]

    # Phonetic alphabet used in the lexicon. Valid values are `ipa` and
    # `x-sampa`.
    alphabet: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Language code that the lexicon applies to. A lexicon with a language code
    # such as "en" would be applied to all English languages (en-GB, en-US, en-
    # AUS, en-WLS, and so on.
    language_code: "LanguageCode" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Date lexicon was last modified (a timestamp value).
    last_modified: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Amazon Resource Name (ARN) of the lexicon.
    lexicon_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Number of lexemes in the lexicon.
    lexemes_count: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Total size of the lexicon, in characters.
    size: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LexiconDescription(autoboto.ShapeBase):
    """
    Describes the content of the lexicon.
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
                "attributes",
                "Attributes",
                autoboto.TypeInfo(LexiconAttributes),
            ),
        ]

    # Name of the lexicon.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Provides lexicon metadata.
    attributes: "LexiconAttributes" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class LexiconNotFoundException(autoboto.ShapeBase):
    """
    Amazon Polly can't find the specified lexicon. This could be caused by a lexicon
    that is missing, its name is misspelled or specifying a lexicon that is in a
    different region.

    Verify that the lexicon exists, is in the region (see ListLexicons) and that you
    spelled its name is spelled correctly. Then try again.
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
class LexiconSizeExceededException(autoboto.ShapeBase):
    """
    The maximum size of the specified lexicon would be exceeded by this operation.
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
class ListLexiconsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An opaque pagination token returned from previous `ListLexicons` operation.
    # If present, indicates where to continue the list of lexicons.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListLexiconsOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lexicons",
                "Lexicons",
                autoboto.TypeInfo(typing.List[LexiconDescription]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of lexicon names and attributes.
    lexicons: typing.List["LexiconDescription"] = dataclasses.field(
        default_factory=list,
    )

    # The pagination token to use in the next request to continue the listing of
    # lexicons. `NextToken` is returned only if the response is truncated.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListSpeechSynthesisTasksInput(autoboto.ShapeBase):
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
            (
                "status",
                "Status",
                autoboto.TypeInfo(TaskStatus),
            ),
        ]

    # Maximum number of speech synthesis tasks returned in a List operation.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The pagination token to use in the next request to continue the listing of
    # speech synthesis tasks.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Status of the speech synthesis tasks returned in a List operation
    status: "TaskStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListSpeechSynthesisTasksOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "synthesis_tasks",
                "SynthesisTasks",
                autoboto.TypeInfo(typing.List[SynthesisTask]),
            ),
        ]

    # An opaque pagination token returned from the previous List operation in
    # this request. If present, this indicates where to continue the listing.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # List of SynthesisTask objects that provides information from the specified
    # task in the list request, including output format, creation time, task
    # status, and so on.
    synthesis_tasks: typing.List["SynthesisTask"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class MarksNotSupportedForFormatException(autoboto.ShapeBase):
    """
    Speech marks are not supported for the `OutputFormat` selected. Speech marks are
    only available for content in `json` format.
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
class MaxLexemeLengthExceededException(autoboto.ShapeBase):
    """
    The maximum size of the lexeme would be exceeded by this operation.
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
class MaxLexiconsNumberExceededException(autoboto.ShapeBase):
    """
    The maximum number of lexicons would be exceeded by this operation.
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


class OutputFormat(Enum):
    json = "json"
    mp3 = "mp3"
    ogg_vorbis = "ogg_vorbis"
    pcm = "pcm"


@dataclasses.dataclass
class PutLexiconInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "content",
                "Content",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the lexicon. The name must follow the regular express format
    # [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive alphanumeric
    # string up to 20 characters long.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Content of the PLS lexicon as string data.
    content: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PutLexiconOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ServiceFailureException(autoboto.ShapeBase):
    """
    An unknown condition has caused a service failure.
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


class SpeechMarkType(Enum):
    sentence = "sentence"
    ssml = "ssml"
    viseme = "viseme"
    word = "word"


@dataclasses.dataclass
class SsmlMarksNotSupportedForTextTypeException(autoboto.ShapeBase):
    """
    SSML speech marks are not supported for plain text-type input.
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
class StartSpeechSynthesisTaskInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_format",
                "OutputFormat",
                autoboto.TypeInfo(OutputFormat),
            ),
            (
                "output_s3_bucket_name",
                "OutputS3BucketName",
                autoboto.TypeInfo(str),
            ),
            (
                "text",
                "Text",
                autoboto.TypeInfo(str),
            ),
            (
                "voice_id",
                "VoiceId",
                autoboto.TypeInfo(VoiceId),
            ),
            (
                "lexicon_names",
                "LexiconNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "output_s3_key_prefix",
                "OutputS3KeyPrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "sample_rate",
                "SampleRate",
                autoboto.TypeInfo(str),
            ),
            (
                "sns_topic_arn",
                "SnsTopicArn",
                autoboto.TypeInfo(str),
            ),
            (
                "speech_mark_types",
                "SpeechMarkTypes",
                autoboto.TypeInfo(typing.List[SpeechMarkType]),
            ),
            (
                "text_type",
                "TextType",
                autoboto.TypeInfo(TextType),
            ),
            (
                "language_code",
                "LanguageCode",
                autoboto.TypeInfo(LanguageCode),
            ),
        ]

    # The format in which the returned output will be encoded. For audio stream,
    # this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.
    output_format: "OutputFormat" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Amazon S3 bucket name to which the output file will be saved.
    output_s3_bucket_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The input text to synthesize. If you specify ssml as the TextType, follow
    # the SSML format for the input text.
    text: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Voice ID to use for the synthesis.
    voice_id: "VoiceId" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # List of one or more pronunciation lexicon names you want the service to
    # apply during synthesis. Lexicons are applied only if the language of the
    # lexicon is the same as the language of the voice.
    lexicon_names: typing.List[str] = dataclasses.field(default_factory=list, )

    # The Amazon S3 key prefix for the output speech file.
    output_s3_key_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The audio frequency specified in Hz.

    # The valid values for mp3 and ogg_vorbis are "8000", "16000", and "22050".
    # The default value is "22050".

    # Valid values for pcm are "8000" and "16000" The default value is "16000".
    sample_rate: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # ARN for the SNS topic optionally used for providing status notification for
    # a speech synthesis task.
    sns_topic_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of speech marks returned for the input text.
    speech_mark_types: typing.List["SpeechMarkType"] = dataclasses.field(
        default_factory=list,
    )

    # Specifies whether the input text is plain text or SSML. The default value
    # is plain text.
    text_type: "TextType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Optional language code for the Speech Synthesis request. This is only
    # necessary if using a bilingual voice, such as Aditi, which can be used for
    # either Indian English (en-IN) or Hindi (hi-IN).

    # If a bilingual voice is used and no language code is specified, Amazon
    # Polly will use the default language of the bilingual voice. The default
    # language for any voice is the one returned by the
    # [DescribeVoices](https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html)
    # operation for the `LanguageCode` parameter. For example, if no language
    # code is specified, Aditi will use Indian English rather than Hindi.
    language_code: "LanguageCode" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class StartSpeechSynthesisTaskOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "synthesis_task",
                "SynthesisTask",
                autoboto.TypeInfo(SynthesisTask),
            ),
        ]

    # SynthesisTask object that provides information and attributes about a newly
    # submitted speech synthesis task.
    synthesis_task: "SynthesisTask" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class SynthesisTask(autoboto.ShapeBase):
    """
    SynthesisTask object that provides information about a speech synthesis task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "TaskId",
                autoboto.TypeInfo(str),
            ),
            (
                "task_status",
                "TaskStatus",
                autoboto.TypeInfo(TaskStatus),
            ),
            (
                "task_status_reason",
                "TaskStatusReason",
                autoboto.TypeInfo(str),
            ),
            (
                "output_uri",
                "OutputUri",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "request_characters",
                "RequestCharacters",
                autoboto.TypeInfo(int),
            ),
            (
                "sns_topic_arn",
                "SnsTopicArn",
                autoboto.TypeInfo(str),
            ),
            (
                "lexicon_names",
                "LexiconNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "output_format",
                "OutputFormat",
                autoboto.TypeInfo(OutputFormat),
            ),
            (
                "sample_rate",
                "SampleRate",
                autoboto.TypeInfo(str),
            ),
            (
                "speech_mark_types",
                "SpeechMarkTypes",
                autoboto.TypeInfo(typing.List[SpeechMarkType]),
            ),
            (
                "text_type",
                "TextType",
                autoboto.TypeInfo(TextType),
            ),
            (
                "voice_id",
                "VoiceId",
                autoboto.TypeInfo(VoiceId),
            ),
            (
                "language_code",
                "LanguageCode",
                autoboto.TypeInfo(LanguageCode),
            ),
        ]

    # The Amazon Polly generated identifier for a speech synthesis task.
    task_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Current status of the individual speech synthesis task.
    task_status: "TaskStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Reason for the current status of a specific speech synthesis task,
    # including errors if the task has failed.
    task_status_reason: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Pathway for the output speech file.
    output_uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Timestamp for the time the synthesis task was started.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Number of billable characters synthesized.
    request_characters: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # ARN for the SNS topic optionally used for providing status notification for
    # a speech synthesis task.
    sns_topic_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # List of one or more pronunciation lexicon names you want the service to
    # apply during synthesis. Lexicons are applied only if the language of the
    # lexicon is the same as the language of the voice.
    lexicon_names: typing.List[str] = dataclasses.field(default_factory=list, )

    # The format in which the returned output will be encoded. For audio stream,
    # this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.
    output_format: "OutputFormat" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The audio frequency specified in Hz.

    # The valid values for mp3 and ogg_vorbis are "8000", "16000", and "22050".
    # The default value is "22050".

    # Valid values for pcm are "8000" and "16000" The default value is "16000".
    sample_rate: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of speech marks returned for the input text.
    speech_mark_types: typing.List["SpeechMarkType"] = dataclasses.field(
        default_factory=list,
    )

    # Specifies whether the input text is plain text or SSML. The default value
    # is plain text.
    text_type: "TextType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Voice ID to use for the synthesis.
    voice_id: "VoiceId" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Optional language code for a synthesis task. This is only necessary if
    # using a bilingual voice, such as Aditi, which can be used for either Indian
    # English (en-IN) or Hindi (hi-IN).

    # If a bilingual voice is used and no language code is specified, Amazon
    # Polly will use the default language of the bilingual voice. The default
    # language for any voice is the one returned by the
    # [DescribeVoices](https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html)
    # operation for the `LanguageCode` parameter. For example, if no language
    # code is specified, Aditi will use Indian English rather than Hindi.
    language_code: "LanguageCode" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SynthesisTaskNotFoundException(autoboto.ShapeBase):
    """
    The Speech Synthesis task with requested Task ID cannot be found.
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
class SynthesizeSpeechInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_format",
                "OutputFormat",
                autoboto.TypeInfo(OutputFormat),
            ),
            (
                "text",
                "Text",
                autoboto.TypeInfo(str),
            ),
            (
                "voice_id",
                "VoiceId",
                autoboto.TypeInfo(VoiceId),
            ),
            (
                "lexicon_names",
                "LexiconNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "sample_rate",
                "SampleRate",
                autoboto.TypeInfo(str),
            ),
            (
                "speech_mark_types",
                "SpeechMarkTypes",
                autoboto.TypeInfo(typing.List[SpeechMarkType]),
            ),
            (
                "text_type",
                "TextType",
                autoboto.TypeInfo(TextType),
            ),
            (
                "language_code",
                "LanguageCode",
                autoboto.TypeInfo(LanguageCode),
            ),
        ]

    # The format in which the returned output will be encoded. For audio stream,
    # this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.
    output_format: "OutputFormat" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Input text to synthesize. If you specify `ssml` as the `TextType`, follow
    # the SSML format for the input text.
    text: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Voice ID to use for the synthesis. You can get a list of available voice
    # IDs by calling the
    # [DescribeVoices](http://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html)
    # operation.
    voice_id: "VoiceId" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # List of one or more pronunciation lexicon names you want the service to
    # apply during synthesis. Lexicons are applied only if the language of the
    # lexicon is the same as the language of the voice. For information about
    # storing lexicons, see
    # [PutLexicon](http://docs.aws.amazon.com/polly/latest/dg/API_PutLexicon.html).
    lexicon_names: typing.List[str] = dataclasses.field(default_factory=list, )

    # The audio frequency specified in Hz.

    # The valid values for `mp3` and `ogg_vorbis` are "8000", "16000", and
    # "22050". The default value is "22050".

    # Valid values for `pcm` are "8000" and "16000" The default value is "16000".
    sample_rate: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of speech marks returned for the input text.
    speech_mark_types: typing.List["SpeechMarkType"] = dataclasses.field(
        default_factory=list,
    )

    # Specifies whether the input text is plain text or SSML. The default value
    # is plain text. For more information, see [Using
    # SSML](http://docs.aws.amazon.com/polly/latest/dg/ssml.html).
    text_type: "TextType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Optional language code for the Synthesize Speech request. This is only
    # necessary if using a bilingual voice, such as Aditi, which can be used for
    # either Indian English (en-IN) or Hindi (hi-IN).

    # If a bilingual voice is used and no language code is specified, Amazon
    # Polly will use the default language of the bilingual voice. The default
    # language for any voice is the one returned by the
    # [DescribeVoices](https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html)
    # operation for the `LanguageCode` parameter. For example, if no language
    # code is specified, Aditi will use Indian English rather than Hindi.
    language_code: "LanguageCode" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SynthesizeSpeechOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_stream",
                "AudioStream",
                autoboto.TypeInfo(typing.Any),
            ),
            (
                "content_type",
                "ContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "request_characters",
                "RequestCharacters",
                autoboto.TypeInfo(int),
            ),
        ]

    # Stream containing the synthesized speech.
    audio_stream: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies the type audio stream. This should reflect the `OutputFormat`
    # parameter in your request.

    #   * If you request `mp3` as the `OutputFormat`, the `ContentType` returned is audio/mpeg.

    #   * If you request `ogg_vorbis` as the `OutputFormat`, the `ContentType` returned is audio/ogg.

    #   * If you request `pcm` as the `OutputFormat`, the `ContentType` returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format.

    #   * If you request `json` as the `OutputFormat`, the `ContentType` returned is audio/json.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Number of characters synthesized.
    request_characters: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class TaskStatus(Enum):
    scheduled = "scheduled"
    inProgress = "inProgress"
    completed = "completed"
    failed = "failed"


@dataclasses.dataclass
class TextLengthExceededException(autoboto.ShapeBase):
    """
    The value of the "Text" parameter is longer than the accepted limits. For the
    `SynthesizeSpeech` API, the limit for input text is a maximum of 6000 characters
    total, of which no more than 3000 can be billed characters. For the
    `StartSpeechSynthesisTask` API, the maximum is 200,000 characters, of which no
    more than 100,000 can be billed characters. SSML tags are not counted as billed
    characters.
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


class TextType(Enum):
    ssml = "ssml"
    text = "text"


@dataclasses.dataclass
class UnsupportedPlsAlphabetException(autoboto.ShapeBase):
    """
    The alphabet specified by the lexicon is not a supported alphabet. Valid values
    are `x-sampa` and `ipa`.
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
class UnsupportedPlsLanguageException(autoboto.ShapeBase):
    """
    The language specified in the lexicon is unsupported. For a list of supported
    languages, see [Lexicon
    Attributes](http://docs.aws.amazon.com/polly/latest/dg/API_LexiconAttributes.html).
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
class Voice(autoboto.ShapeBase):
    """
    Description of the voice.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gender",
                "Gender",
                autoboto.TypeInfo(Gender),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(VoiceId),
            ),
            (
                "language_code",
                "LanguageCode",
                autoboto.TypeInfo(LanguageCode),
            ),
            (
                "language_name",
                "LanguageName",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "additional_language_codes",
                "AdditionalLanguageCodes",
                autoboto.TypeInfo(typing.List[LanguageCode]),
            ),
        ]

    # Gender of the voice.
    gender: "Gender" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Amazon Polly assigned voice ID. This is the ID that you specify when
    # calling the `SynthesizeSpeech` operation.
    id: "VoiceId" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Language code of the voice.
    language_code: "LanguageCode" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Human readable name of the language in English.
    language_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Name of the voice (for example, Salli, Kendra, etc.). This provides a human
    # readable voice name that you might display in your application.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Additional codes for languages available for the specified voice in
    # addition to its default language.

    # For example, the default language for Aditi is Indian English (en-IN)
    # because it was first used for that language. Since Aditi is bilingual and
    # fluent in both Indian English and Hindi, this parameter would show the code
    # `hi-IN`.
    additional_language_codes: typing.List["LanguageCode"] = dataclasses.field(
        default_factory=list,
    )


class VoiceId(Enum):
    Geraint = "Geraint"
    Gwyneth = "Gwyneth"
    Mads = "Mads"
    Naja = "Naja"
    Hans = "Hans"
    Marlene = "Marlene"
    Nicole = "Nicole"
    Russell = "Russell"
    Amy = "Amy"
    Brian = "Brian"
    Emma = "Emma"
    Raveena = "Raveena"
    Ivy = "Ivy"
    Joanna = "Joanna"
    Joey = "Joey"
    Justin = "Justin"
    Kendra = "Kendra"
    Kimberly = "Kimberly"
    Matthew = "Matthew"
    Salli = "Salli"
    Conchita = "Conchita"
    Enrique = "Enrique"
    Miguel = "Miguel"
    Penelope = "Penelope"
    Chantal = "Chantal"
    Celine = "Celine"
    Lea = "Lea"
    Mathieu = "Mathieu"
    Dora = "Dora"
    Karl = "Karl"
    Carla = "Carla"
    Giorgio = "Giorgio"
    Mizuki = "Mizuki"
    Liv = "Liv"
    Lotte = "Lotte"
    Ruben = "Ruben"
    Ewa = "Ewa"
    Jacek = "Jacek"
    Jan = "Jan"
    Maja = "Maja"
    Ricardo = "Ricardo"
    Vitoria = "Vitoria"
    Cristiano = "Cristiano"
    Ines = "Ines"
    Carmen = "Carmen"
    Maxim = "Maxim"
    Tatyana = "Tatyana"
    Astrid = "Astrid"
    Filiz = "Filiz"
    Vicki = "Vicki"
    Takumi = "Takumi"
    Seoyeon = "Seoyeon"
    Aditi = "Aditi"
