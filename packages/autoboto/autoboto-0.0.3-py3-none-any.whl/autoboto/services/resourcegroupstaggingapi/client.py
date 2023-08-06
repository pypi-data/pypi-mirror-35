import datetime
import typing
import boto3
import autoboto
from . import shapes


class Client:
    def __init__(self, *args, **kwargs):
        self._boto_client = boto3.client(
            "resourcegroupstaggingapi", *args, **kwargs
        )

    def get_resources(
        self,
        _request: shapes.GetResourcesInput = None,
        *,
        pagination_token: str = autoboto.ShapeBase._NOT_SET,
        tag_filters: typing.List[shapes.TagFilter
                                ] = autoboto.ShapeBase._NOT_SET,
        resources_per_page: int = autoboto.ShapeBase._NOT_SET,
        tags_per_page: int = autoboto.ShapeBase._NOT_SET,
        resource_type_filters: typing.List[str] = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.GetResourcesOutput:
        """
        Returns all the tagged resources that are associated with the specified tags
        (keys and values) located in the specified region for the AWS account. The tags
        and the resource types that you specify in the request are known as _filters_.
        The response includes all tags that are associated with the requested resources.
        If no filter is provided, this action returns a paginated resource list with the
        associated tags.
        """
        if _request is None:
            _params = {}
            if pagination_token is not autoboto.ShapeBase._NOT_SET:
                _params['pagination_token'] = pagination_token
            if tag_filters is not autoboto.ShapeBase._NOT_SET:
                _params['tag_filters'] = tag_filters
            if resources_per_page is not autoboto.ShapeBase._NOT_SET:
                _params['resources_per_page'] = resources_per_page
            if tags_per_page is not autoboto.ShapeBase._NOT_SET:
                _params['tags_per_page'] = tags_per_page
            if resource_type_filters is not autoboto.ShapeBase._NOT_SET:
                _params['resource_type_filters'] = resource_type_filters
            _request = shapes.GetResourcesInput(**_params)
        response = self._boto_client.get_resources(**_request.to_boto_dict())

        return shapes.GetResourcesOutput.from_boto_dict(response)

    def get_tag_keys(
        self,
        _request: shapes.GetTagKeysInput = None,
        *,
        pagination_token: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.GetTagKeysOutput:
        """
        Returns all tag keys in the specified region for the AWS account.
        """
        if _request is None:
            _params = {}
            if pagination_token is not autoboto.ShapeBase._NOT_SET:
                _params['pagination_token'] = pagination_token
            _request = shapes.GetTagKeysInput(**_params)
        response = self._boto_client.get_tag_keys(**_request.to_boto_dict())

        return shapes.GetTagKeysOutput.from_boto_dict(response)

    def get_tag_values(
        self,
        _request: shapes.GetTagValuesInput = None,
        *,
        key: str,
        pagination_token: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.GetTagValuesOutput:
        """
        Returns all tag values for the specified key in the specified region for the AWS
        account.
        """
        if _request is None:
            _params = {}
            if key is not autoboto.ShapeBase._NOT_SET:
                _params['key'] = key
            if pagination_token is not autoboto.ShapeBase._NOT_SET:
                _params['pagination_token'] = pagination_token
            _request = shapes.GetTagValuesInput(**_params)
        response = self._boto_client.get_tag_values(**_request.to_boto_dict())

        return shapes.GetTagValuesOutput.from_boto_dict(response)

    def tag_resources(
        self,
        _request: shapes.TagResourcesInput = None,
        *,
        resource_arn_list: typing.List[str],
        tags: typing.Dict[str, str],
    ) -> shapes.TagResourcesOutput:
        """
        Applies one or more tags to the specified resources. Note the following:

          * Not all resources can have tags. For a list of resources that support tagging, see [Supported Resources](http://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/supported-resources.html) in the _AWS Resource Groups and Tag Editor User Guide_.

          * Each resource can have up to 50 tags. For other limits, see [Tag Restrictions](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-restrictions) in the _Amazon EC2 User Guide for Linux Instances_.

          * You can only tag resources that are located in the specified region for the AWS account.

          * To add tags to a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for adding tags. For more information, see [Obtaining Permissions for Tagging](http://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/obtaining-permissions-for-tagging.html) in the _AWS Resource Groups and Tag Editor User Guide_.
        """
        if _request is None:
            _params = {}
            if resource_arn_list is not autoboto.ShapeBase._NOT_SET:
                _params['resource_arn_list'] = resource_arn_list
            if tags is not autoboto.ShapeBase._NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagResourcesInput(**_params)
        response = self._boto_client.tag_resources(**_request.to_boto_dict())

        return shapes.TagResourcesOutput.from_boto_dict(response)

    def untag_resources(
        self,
        _request: shapes.UntagResourcesInput = None,
        *,
        resource_arn_list: typing.List[str],
        tag_keys: typing.List[str],
    ) -> shapes.UntagResourcesOutput:
        """
        Removes the specified tags from the specified resources. When you specify a tag
        key, the action removes both that key and its associated value. The operation
        succeeds even if you attempt to remove tags from a resource that were already
        removed. Note the following:

          * To remove tags from a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for removing tags. For more information, see [Obtaining Permissions for Tagging](http://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/obtaining-permissions-for-tagging.html) in the _AWS Resource Groups and Tag Editor User Guide_.

          * You can only tag resources that are located in the specified region for the AWS account.
        """
        if _request is None:
            _params = {}
            if resource_arn_list is not autoboto.ShapeBase._NOT_SET:
                _params['resource_arn_list'] = resource_arn_list
            if tag_keys is not autoboto.ShapeBase._NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagResourcesInput(**_params)
        response = self._boto_client.untag_resources(**_request.to_boto_dict())

        return shapes.UntagResourcesOutput.from_boto_dict(response)
