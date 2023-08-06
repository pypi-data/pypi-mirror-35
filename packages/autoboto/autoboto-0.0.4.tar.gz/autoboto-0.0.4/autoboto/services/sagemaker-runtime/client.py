import datetime
import typing
import boto3
import autoboto
from . import shapes


class Client:
    def __init__(self, *args, **kwargs):
        self._boto_client = boto3.client("sagemaker-runtime", *args, **kwargs)

    def invoke_endpoint(
        self,
        _request: shapes.InvokeEndpointInput = None,
        *,
        endpoint_name: str,
        body: typing.Any,
        content_type: str = autoboto.ShapeBase.NOT_SET,
        accept: str = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.InvokeEndpointOutput:
        """
        After you deploy a model into production using Amazon SageMaker hosting
        services, your client applications use this API to get inferences from the model
        hosted at the specified endpoint.

        For an overview of Amazon SageMaker, see [How It
        Works](http://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html)

        Amazon SageMaker strips all POST headers except those supported by the API.
        Amazon SageMaker might add additional headers. You should not rely on the
        behavior of headers outside those enumerated in the request syntax.
        """
        if _request is None:
            _params = {}
            if endpoint_name is not autoboto.ShapeBase.NOT_SET:
                _params['endpoint_name'] = endpoint_name
            if body is not autoboto.ShapeBase.NOT_SET:
                _params['body'] = body
            if content_type is not autoboto.ShapeBase.NOT_SET:
                _params['content_type'] = content_type
            if accept is not autoboto.ShapeBase.NOT_SET:
                _params['accept'] = accept
            _request = shapes.InvokeEndpointInput(**_params)
        response = self._boto_client.invoke_endpoint(**_request.to_boto_dict())

        return shapes.InvokeEndpointOutput.from_boto_dict(response)
