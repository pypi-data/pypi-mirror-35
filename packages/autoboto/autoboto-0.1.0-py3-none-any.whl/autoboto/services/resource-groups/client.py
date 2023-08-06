import datetime
import typing
import boto3
import autoboto
from . import shapes


class Client:
    def __init__(self, *args, **kwargs):
        self._boto_client = boto3.client("resource-groups", *args, **kwargs)

    def create_group(
        self,
        _request: shapes.CreateGroupInput = None,
        *,
        name: str,
        resource_query: shapes.ResourceQuery,
        description: str = autoboto.ShapeBase.NOT_SET,
        tags: typing.Dict[str, str] = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.CreateGroupOutput:
        """
        Creates a group with a specified name, description, and resource query.
        """
        if _request is None:
            _params = {}
            if name is not autoboto.ShapeBase.NOT_SET:
                _params['name'] = name
            if resource_query is not autoboto.ShapeBase.NOT_SET:
                _params['resource_query'] = resource_query
            if description is not autoboto.ShapeBase.NOT_SET:
                _params['description'] = description
            if tags is not autoboto.ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateGroupInput(**_params)
        response = self._boto_client.create_group(**_request.to_boto_dict())

        return shapes.CreateGroupOutput.from_boto_dict(response)

    def delete_group(
        self,
        _request: shapes.DeleteGroupInput = None,
        *,
        group_name: str,
    ) -> shapes.DeleteGroupOutput:
        """
        Deletes a specified resource group. Deleting a resource group does not delete
        resources that are members of the group; it only deletes the group structure.
        """
        if _request is None:
            _params = {}
            if group_name is not autoboto.ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            _request = shapes.DeleteGroupInput(**_params)
        response = self._boto_client.delete_group(**_request.to_boto_dict())

        return shapes.DeleteGroupOutput.from_boto_dict(response)

    def get_group(
        self,
        _request: shapes.GetGroupInput = None,
        *,
        group_name: str,
    ) -> shapes.GetGroupOutput:
        """
        Returns information about a specified resource group.
        """
        if _request is None:
            _params = {}
            if group_name is not autoboto.ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            _request = shapes.GetGroupInput(**_params)
        response = self._boto_client.get_group(**_request.to_boto_dict())

        return shapes.GetGroupOutput.from_boto_dict(response)

    def get_group_query(
        self,
        _request: shapes.GetGroupQueryInput = None,
        *,
        group_name: str,
    ) -> shapes.GetGroupQueryOutput:
        """
        Returns the resource query associated with the specified resource group.
        """
        if _request is None:
            _params = {}
            if group_name is not autoboto.ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            _request = shapes.GetGroupQueryInput(**_params)
        response = self._boto_client.get_group_query(**_request.to_boto_dict())

        return shapes.GetGroupQueryOutput.from_boto_dict(response)

    def get_tags(
        self,
        _request: shapes.GetTagsInput = None,
        *,
        arn: str,
    ) -> shapes.GetTagsOutput:
        """
        Returns a list of tags that are associated with a resource, specified by an ARN.
        """
        if _request is None:
            _params = {}
            if arn is not autoboto.ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.GetTagsInput(**_params)
        response = self._boto_client.get_tags(**_request.to_boto_dict())

        return shapes.GetTagsOutput.from_boto_dict(response)

    def list_group_resources(
        self,
        _request: shapes.ListGroupResourcesInput = None,
        *,
        group_name: str,
        filters: typing.List[shapes.ResourceFilter
                            ] = autoboto.ShapeBase.NOT_SET,
        max_results: int = autoboto.ShapeBase.NOT_SET,
        next_token: str = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.ListGroupResourcesOutput:
        """
        Returns a list of ARNs of resources that are members of a specified resource
        group.
        """
        if _request is None:
            _params = {}
            if group_name is not autoboto.ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if filters is not autoboto.ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not autoboto.ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not autoboto.ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListGroupResourcesInput(**_params)
        response = self._boto_client.list_group_resources(
            **_request.to_boto_dict()
        )

        return shapes.ListGroupResourcesOutput.from_boto_dict(response)

    def list_groups(
        self,
        _request: shapes.ListGroupsInput = None,
        *,
        max_results: int = autoboto.ShapeBase.NOT_SET,
        next_token: str = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.ListGroupsOutput:
        """
        Returns a list of existing resource groups in your account.
        """
        if _request is None:
            _params = {}
            if max_results is not autoboto.ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not autoboto.ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListGroupsInput(**_params)
        response = self._boto_client.list_groups(**_request.to_boto_dict())

        return shapes.ListGroupsOutput.from_boto_dict(response)

    def search_resources(
        self,
        _request: shapes.SearchResourcesInput = None,
        *,
        resource_query: shapes.ResourceQuery,
        max_results: int = autoboto.ShapeBase.NOT_SET,
        next_token: str = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.SearchResourcesOutput:
        """
        Returns a list of AWS resource identifiers that matches a specified query. The
        query uses the same format as a resource query in a CreateGroup or
        UpdateGroupQuery operation.
        """
        if _request is None:
            _params = {}
            if resource_query is not autoboto.ShapeBase.NOT_SET:
                _params['resource_query'] = resource_query
            if max_results is not autoboto.ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not autoboto.ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.SearchResourcesInput(**_params)
        response = self._boto_client.search_resources(**_request.to_boto_dict())

        return shapes.SearchResourcesOutput.from_boto_dict(response)

    def tag(
        self,
        _request: shapes.TagInput = None,
        *,
        arn: str,
        tags: typing.Dict[str, str],
    ) -> shapes.TagOutput:
        """
        Adds specified tags to a resource with the specified ARN. Existing tags on a
        resource are not changed if they are not specified in the request parameters.
        """
        if _request is None:
            _params = {}
            if arn is not autoboto.ShapeBase.NOT_SET:
                _params['arn'] = arn
            if tags is not autoboto.ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagInput(**_params)
        response = self._boto_client.tag(**_request.to_boto_dict())

        return shapes.TagOutput.from_boto_dict(response)

    def untag(
        self,
        _request: shapes.UntagInput = None,
        *,
        arn: str,
        keys: typing.List[str],
    ) -> shapes.UntagOutput:
        """
        Deletes specified tags from a specified resource.
        """
        if _request is None:
            _params = {}
            if arn is not autoboto.ShapeBase.NOT_SET:
                _params['arn'] = arn
            if keys is not autoboto.ShapeBase.NOT_SET:
                _params['keys'] = keys
            _request = shapes.UntagInput(**_params)
        response = self._boto_client.untag(**_request.to_boto_dict())

        return shapes.UntagOutput.from_boto_dict(response)

    def update_group(
        self,
        _request: shapes.UpdateGroupInput = None,
        *,
        group_name: str,
        description: str = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.UpdateGroupOutput:
        """
        Updates an existing group with a new or changed description. You cannot update
        the name of a resource group.
        """
        if _request is None:
            _params = {}
            if group_name is not autoboto.ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if description is not autoboto.ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.UpdateGroupInput(**_params)
        response = self._boto_client.update_group(**_request.to_boto_dict())

        return shapes.UpdateGroupOutput.from_boto_dict(response)

    def update_group_query(
        self,
        _request: shapes.UpdateGroupQueryInput = None,
        *,
        group_name: str,
        resource_query: shapes.ResourceQuery,
    ) -> shapes.UpdateGroupQueryOutput:
        """
        Updates the resource query of a group.
        """
        if _request is None:
            _params = {}
            if group_name is not autoboto.ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if resource_query is not autoboto.ShapeBase.NOT_SET:
                _params['resource_query'] = resource_query
            _request = shapes.UpdateGroupQueryInput(**_params)
        response = self._boto_client.update_group_query(
            **_request.to_boto_dict()
        )

        return shapes.UpdateGroupQueryOutput.from_boto_dict(response)
