import datetime
import typing
import boto3
import autoboto
from . import shapes


class Client:
    def __init__(self, *args, **kwargs):
        self._boto_client = boto3.client("translate", *args, **kwargs)

    def translate_text(
        self,
        _request: shapes.TranslateTextRequest = None,
        *,
        text: str,
        source_language_code: str,
        target_language_code: str,
    ) -> shapes.TranslateTextResponse:
        """
        Translates input text from the source language to the target language. You can
        translate between English (en) and one of the following languages, or between
        one of the following languages and English.

          * Arabic (ar)

          * Chinese (Simplified) (zh)

          * French (fr)

          * German (de)

          * Portuguese (pt)

          * Spanish (es)

        To have Amazon Translate determine the source language of your text, you can
        specify `auto` in the `SourceLanguageCode` field. If you specify `auto`, Amazon
        Translate will call Amazon Comprehend to determine the source language.
        """
        if _request is None:
            _params = {}
            if text is not autoboto.ShapeBase.NOT_SET:
                _params['text'] = text
            if source_language_code is not autoboto.ShapeBase.NOT_SET:
                _params['source_language_code'] = source_language_code
            if target_language_code is not autoboto.ShapeBase.NOT_SET:
                _params['target_language_code'] = target_language_code
            _request = shapes.TranslateTextRequest(**_params)
        response = self._boto_client.translate_text(**_request.to_boto_dict())

        return shapes.TranslateTextResponse.from_boto_dict(response)
