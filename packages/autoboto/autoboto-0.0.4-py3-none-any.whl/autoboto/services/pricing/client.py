import datetime
import typing
import boto3
import autoboto
from . import shapes


class Client:
    def __init__(self, *args, **kwargs):
        self._boto_client = boto3.client("pricing", *args, **kwargs)

    def describe_services(
        self,
        _request: shapes.DescribeServicesRequest = None,
        *,
        service_code: str = autoboto.ShapeBase.NOT_SET,
        format_version: str = autoboto.ShapeBase.NOT_SET,
        next_token: str = autoboto.ShapeBase.NOT_SET,
        max_results: int = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.DescribeServicesResponse:
        """
        Returns the metadata for one service or a list of the metadata for all services.
        Use this without a service code to get the service codes for all services. Use
        it with a service code, such as `AmazonEC2`, to get information specific to that
        service, such as the attribute names available for that service. For example,
        some of the attribute names available for EC2 are `volumeType`, `maxIopsVolume`,
        `operation`, `locationType`, and `instanceCapacity10xlarge`.
        """
        if _request is None:
            _params = {}
            if service_code is not autoboto.ShapeBase.NOT_SET:
                _params['service_code'] = service_code
            if format_version is not autoboto.ShapeBase.NOT_SET:
                _params['format_version'] = format_version
            if next_token is not autoboto.ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not autoboto.ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeServicesRequest(**_params)
        response = self._boto_client.describe_services(
            **_request.to_boto_dict()
        )

        return shapes.DescribeServicesResponse.from_boto_dict(response)

    def get_attribute_values(
        self,
        _request: shapes.GetAttributeValuesRequest = None,
        *,
        service_code: str,
        attribute_name: str,
        next_token: str = autoboto.ShapeBase.NOT_SET,
        max_results: int = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.GetAttributeValuesResponse:
        """
        Returns a list of attribute values. Attibutes are similar to the details in a
        Price List API offer file. For a list of available attributes, see [Offer File
        Definitions](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/reading-
        an-offer.html#pps-defs) in the [AWS Billing and Cost Management User
        Guide](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-
        is.html).
        """
        if _request is None:
            _params = {}
            if service_code is not autoboto.ShapeBase.NOT_SET:
                _params['service_code'] = service_code
            if attribute_name is not autoboto.ShapeBase.NOT_SET:
                _params['attribute_name'] = attribute_name
            if next_token is not autoboto.ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not autoboto.ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetAttributeValuesRequest(**_params)
        response = self._boto_client.get_attribute_values(
            **_request.to_boto_dict()
        )

        return shapes.GetAttributeValuesResponse.from_boto_dict(response)

    def get_products(
        self,
        _request: shapes.GetProductsRequest = None,
        *,
        service_code: str = autoboto.ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = autoboto.ShapeBase.NOT_SET,
        format_version: str = autoboto.ShapeBase.NOT_SET,
        next_token: str = autoboto.ShapeBase.NOT_SET,
        max_results: int = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.GetProductsResponse:
        """
        Returns a list of all products that match the filter criteria.
        """
        if _request is None:
            _params = {}
            if service_code is not autoboto.ShapeBase.NOT_SET:
                _params['service_code'] = service_code
            if filters is not autoboto.ShapeBase.NOT_SET:
                _params['filters'] = filters
            if format_version is not autoboto.ShapeBase.NOT_SET:
                _params['format_version'] = format_version
            if next_token is not autoboto.ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not autoboto.ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetProductsRequest(**_params)
        response = self._boto_client.get_products(**_request.to_boto_dict())

        return shapes.GetProductsResponse.from_boto_dict(response)
