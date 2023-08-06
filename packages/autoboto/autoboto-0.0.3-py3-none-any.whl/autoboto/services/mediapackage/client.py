import datetime
import typing
import boto3
import autoboto
from . import shapes


class Client:
    def __init__(self, *args, **kwargs):
        self._boto_client = boto3.client("mediapackage", *args, **kwargs)

    def create_channel(
        self,
        _request: shapes.CreateChannelRequest = None,
        *,
        id: str,
        description: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.CreateChannelResponse:
        """
        Creates a new Channel.
        """
        if _request is None:
            _params = {}
            if id is not autoboto.ShapeBase._NOT_SET:
                _params['id'] = id
            if description is not autoboto.ShapeBase._NOT_SET:
                _params['description'] = description
            _request = shapes.CreateChannelRequest(**_params)
        response = self._boto_client.create_channel(**_request.to_boto_dict())

        return shapes.CreateChannelResponse.from_boto_dict(response)

    def create_origin_endpoint(
        self,
        _request: shapes.CreateOriginEndpointRequest = None,
        *,
        channel_id: str,
        id: str,
        cmaf_package: shapes.CmafPackageCreateOrUpdateParameters = autoboto.
        ShapeBase._NOT_SET,
        dash_package: shapes.DashPackage = autoboto.ShapeBase._NOT_SET,
        description: str = autoboto.ShapeBase._NOT_SET,
        hls_package: shapes.HlsPackage = autoboto.ShapeBase._NOT_SET,
        manifest_name: str = autoboto.ShapeBase._NOT_SET,
        mss_package: shapes.MssPackage = autoboto.ShapeBase._NOT_SET,
        startover_window_seconds: int = autoboto.ShapeBase._NOT_SET,
        time_delay_seconds: int = autoboto.ShapeBase._NOT_SET,
        whitelist: typing.List[str] = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.CreateOriginEndpointResponse:
        """
        Creates a new OriginEndpoint record.
        """
        if _request is None:
            _params = {}
            if channel_id is not autoboto.ShapeBase._NOT_SET:
                _params['channel_id'] = channel_id
            if id is not autoboto.ShapeBase._NOT_SET:
                _params['id'] = id
            if cmaf_package is not autoboto.ShapeBase._NOT_SET:
                _params['cmaf_package'] = cmaf_package
            if dash_package is not autoboto.ShapeBase._NOT_SET:
                _params['dash_package'] = dash_package
            if description is not autoboto.ShapeBase._NOT_SET:
                _params['description'] = description
            if hls_package is not autoboto.ShapeBase._NOT_SET:
                _params['hls_package'] = hls_package
            if manifest_name is not autoboto.ShapeBase._NOT_SET:
                _params['manifest_name'] = manifest_name
            if mss_package is not autoboto.ShapeBase._NOT_SET:
                _params['mss_package'] = mss_package
            if startover_window_seconds is not autoboto.ShapeBase._NOT_SET:
                _params['startover_window_seconds'] = startover_window_seconds
            if time_delay_seconds is not autoboto.ShapeBase._NOT_SET:
                _params['time_delay_seconds'] = time_delay_seconds
            if whitelist is not autoboto.ShapeBase._NOT_SET:
                _params['whitelist'] = whitelist
            _request = shapes.CreateOriginEndpointRequest(**_params)
        response = self._boto_client.create_origin_endpoint(
            **_request.to_boto_dict()
        )

        return shapes.CreateOriginEndpointResponse.from_boto_dict(response)

    def delete_channel(
        self,
        _request: shapes.DeleteChannelRequest = None,
        *,
        id: str,
    ) -> shapes.DeleteChannelResponse:
        """
        Deletes an existing Channel.
        """
        if _request is None:
            _params = {}
            if id is not autoboto.ShapeBase._NOT_SET:
                _params['id'] = id
            _request = shapes.DeleteChannelRequest(**_params)
        response = self._boto_client.delete_channel(**_request.to_boto_dict())

        return shapes.DeleteChannelResponse.from_boto_dict(response)

    def delete_origin_endpoint(
        self,
        _request: shapes.DeleteOriginEndpointRequest = None,
        *,
        id: str,
    ) -> shapes.DeleteOriginEndpointResponse:
        """
        Deletes an existing OriginEndpoint.
        """
        if _request is None:
            _params = {}
            if id is not autoboto.ShapeBase._NOT_SET:
                _params['id'] = id
            _request = shapes.DeleteOriginEndpointRequest(**_params)
        response = self._boto_client.delete_origin_endpoint(
            **_request.to_boto_dict()
        )

        return shapes.DeleteOriginEndpointResponse.from_boto_dict(response)

    def describe_channel(
        self,
        _request: shapes.DescribeChannelRequest = None,
        *,
        id: str,
    ) -> shapes.DescribeChannelResponse:
        """
        Gets details about a Channel.
        """
        if _request is None:
            _params = {}
            if id is not autoboto.ShapeBase._NOT_SET:
                _params['id'] = id
            _request = shapes.DescribeChannelRequest(**_params)
        response = self._boto_client.describe_channel(**_request.to_boto_dict())

        return shapes.DescribeChannelResponse.from_boto_dict(response)

    def describe_origin_endpoint(
        self,
        _request: shapes.DescribeOriginEndpointRequest = None,
        *,
        id: str,
    ) -> shapes.DescribeOriginEndpointResponse:
        """
        Gets details about an existing OriginEndpoint.
        """
        if _request is None:
            _params = {}
            if id is not autoboto.ShapeBase._NOT_SET:
                _params['id'] = id
            _request = shapes.DescribeOriginEndpointRequest(**_params)
        response = self._boto_client.describe_origin_endpoint(
            **_request.to_boto_dict()
        )

        return shapes.DescribeOriginEndpointResponse.from_boto_dict(response)

    def list_channels(
        self,
        _request: shapes.ListChannelsRequest = None,
        *,
        max_results: int = autoboto.ShapeBase._NOT_SET,
        next_token: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.ListChannelsResponse:
        """
        Returns a collection of Channels.
        """
        if _request is None:
            _params = {}
            if max_results is not autoboto.ShapeBase._NOT_SET:
                _params['max_results'] = max_results
            if next_token is not autoboto.ShapeBase._NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListChannelsRequest(**_params)
        response = self._boto_client.list_channels(**_request.to_boto_dict())

        return shapes.ListChannelsResponse.from_boto_dict(response)

    def list_origin_endpoints(
        self,
        _request: shapes.ListOriginEndpointsRequest = None,
        *,
        channel_id: str = autoboto.ShapeBase._NOT_SET,
        max_results: int = autoboto.ShapeBase._NOT_SET,
        next_token: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.ListOriginEndpointsResponse:
        """
        Returns a collection of OriginEndpoint records.
        """
        if _request is None:
            _params = {}
            if channel_id is not autoboto.ShapeBase._NOT_SET:
                _params['channel_id'] = channel_id
            if max_results is not autoboto.ShapeBase._NOT_SET:
                _params['max_results'] = max_results
            if next_token is not autoboto.ShapeBase._NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListOriginEndpointsRequest(**_params)
        response = self._boto_client.list_origin_endpoints(
            **_request.to_boto_dict()
        )

        return shapes.ListOriginEndpointsResponse.from_boto_dict(response)

    def rotate_channel_credentials(
        self,
        _request: shapes.RotateChannelCredentialsRequest = None,
        *,
        id: str,
    ) -> shapes.RotateChannelCredentialsResponse:
        """
        Changes the Channel ingest username and password.
        """
        if _request is None:
            _params = {}
            if id is not autoboto.ShapeBase._NOT_SET:
                _params['id'] = id
            _request = shapes.RotateChannelCredentialsRequest(**_params)
        response = self._boto_client.rotate_channel_credentials(
            **_request.to_boto_dict()
        )

        return shapes.RotateChannelCredentialsResponse.from_boto_dict(response)

    def update_channel(
        self,
        _request: shapes.UpdateChannelRequest = None,
        *,
        id: str,
        description: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.UpdateChannelResponse:
        """
        Updates an existing Channel.
        """
        if _request is None:
            _params = {}
            if id is not autoboto.ShapeBase._NOT_SET:
                _params['id'] = id
            if description is not autoboto.ShapeBase._NOT_SET:
                _params['description'] = description
            _request = shapes.UpdateChannelRequest(**_params)
        response = self._boto_client.update_channel(**_request.to_boto_dict())

        return shapes.UpdateChannelResponse.from_boto_dict(response)

    def update_origin_endpoint(
        self,
        _request: shapes.UpdateOriginEndpointRequest = None,
        *,
        id: str,
        cmaf_package: shapes.CmafPackageCreateOrUpdateParameters = autoboto.
        ShapeBase._NOT_SET,
        dash_package: shapes.DashPackage = autoboto.ShapeBase._NOT_SET,
        description: str = autoboto.ShapeBase._NOT_SET,
        hls_package: shapes.HlsPackage = autoboto.ShapeBase._NOT_SET,
        manifest_name: str = autoboto.ShapeBase._NOT_SET,
        mss_package: shapes.MssPackage = autoboto.ShapeBase._NOT_SET,
        startover_window_seconds: int = autoboto.ShapeBase._NOT_SET,
        time_delay_seconds: int = autoboto.ShapeBase._NOT_SET,
        whitelist: typing.List[str] = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.UpdateOriginEndpointResponse:
        """
        Updates an existing OriginEndpoint.
        """
        if _request is None:
            _params = {}
            if id is not autoboto.ShapeBase._NOT_SET:
                _params['id'] = id
            if cmaf_package is not autoboto.ShapeBase._NOT_SET:
                _params['cmaf_package'] = cmaf_package
            if dash_package is not autoboto.ShapeBase._NOT_SET:
                _params['dash_package'] = dash_package
            if description is not autoboto.ShapeBase._NOT_SET:
                _params['description'] = description
            if hls_package is not autoboto.ShapeBase._NOT_SET:
                _params['hls_package'] = hls_package
            if manifest_name is not autoboto.ShapeBase._NOT_SET:
                _params['manifest_name'] = manifest_name
            if mss_package is not autoboto.ShapeBase._NOT_SET:
                _params['mss_package'] = mss_package
            if startover_window_seconds is not autoboto.ShapeBase._NOT_SET:
                _params['startover_window_seconds'] = startover_window_seconds
            if time_delay_seconds is not autoboto.ShapeBase._NOT_SET:
                _params['time_delay_seconds'] = time_delay_seconds
            if whitelist is not autoboto.ShapeBase._NOT_SET:
                _params['whitelist'] = whitelist
            _request = shapes.UpdateOriginEndpointRequest(**_params)
        response = self._boto_client.update_origin_endpoint(
            **_request.to_boto_dict()
        )

        return shapes.UpdateOriginEndpointResponse.from_boto_dict(response)
