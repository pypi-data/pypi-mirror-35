import datetime
import typing
import autoboto
import dataclasses


@dataclasses.dataclass
class DetectedLanguageLowConfidenceException(autoboto.ShapeBase):
    """
    The confidence that Amazon Comprehend accurately detected the source language is
    low. If a low confidence level is acceptable for your application, you can use
    the language in the exception to call Amazon Translate again. For more
    information, see the
    [DetectDominantLanguage](https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectDominantLanguage.html)
    operation in the _Amazon Comprehend Developer Guide_.
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
                "detected_language_code",
                "DetectedLanguageCode",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Auto detected language code from Comprehend.
    detected_language_code: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalServerException(autoboto.ShapeBase):
    """
    An internal server error occurred. Retry your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRequestException(autoboto.ShapeBase):
    """
    The request is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceUnavailableException(autoboto.ShapeBase):
    """
    Amazon Translate is unavailable. Retry your request later.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TextSizeLimitExceededException(autoboto.ShapeBase):
    """
    The size of the input text exceeds the length constraint for the `Text` field.
    Try again with a shorter text.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyRequestsException(autoboto.ShapeBase):
    """
    The number of requests exceeds the limit. Resubmit your request later.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TranslateTextRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "text",
                "Text",
                autoboto.TypeInfo(str),
            ),
            (
                "source_language_code",
                "SourceLanguageCode",
                autoboto.TypeInfo(str),
            ),
            (
                "target_language_code",
                "TargetLanguageCode",
                autoboto.TypeInfo(str),
            ),
        ]

    # The text to translate.
    text: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One of the supported language codes for the source text. If the
    # `TargetLanguageCode` is not "en", the `SourceLanguageCode` must be "en".

    # To have Amazon Translate determine the source language of your text, you
    # can specify `auto` in the `SourceLanguageCode` field. If you specify
    # `auto`, Amazon Translate will call Amazon Comprehend to determine the
    # source language.
    source_language_code: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # One of the supported language codes for the target text. If the
    # `SourceLanguageCode` is not "en", the `TargetLanguageCode` must be "en".
    target_language_code: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TranslateTextResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "translated_text",
                "TranslatedText",
                autoboto.TypeInfo(str),
            ),
            (
                "source_language_code",
                "SourceLanguageCode",
                autoboto.TypeInfo(str),
            ),
            (
                "target_language_code",
                "TargetLanguageCode",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The text translated into the target language.
    translated_text: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language code for the language of the input text.
    source_language_code: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language code for the language of the translated text.
    target_language_code: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UnsupportedLanguagePairException(autoboto.ShapeBase):
    """
    Amazon Translate cannot translate input text in the source language into this
    target language. For more information, see how-to-error-msg.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
