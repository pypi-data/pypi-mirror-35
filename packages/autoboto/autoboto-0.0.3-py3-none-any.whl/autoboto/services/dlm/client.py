import datetime
import typing
import boto3
import autoboto
from . import shapes


class Client:
    def __init__(self, *args, **kwargs):
        self._boto_client = boto3.client("dlm", *args, **kwargs)

    def create_lifecycle_policy(
        self,
        _request: shapes.CreateLifecyclePolicyRequest = None,
        *,
        execution_role_arn: str,
        description: str,
        state: shapes.SettablePolicyStateValues,
        policy_details: shapes.PolicyDetails,
    ) -> shapes.CreateLifecyclePolicyResponse:
        """
        Creates a policy to manage the lifecycle of the specified AWS resources. You can
        create up to 100 lifecycle policies.
        """
        if _request is None:
            _params = {}
            if execution_role_arn is not autoboto.ShapeBase._NOT_SET:
                _params['execution_role_arn'] = execution_role_arn
            if description is not autoboto.ShapeBase._NOT_SET:
                _params['description'] = description
            if state is not autoboto.ShapeBase._NOT_SET:
                _params['state'] = state
            if policy_details is not autoboto.ShapeBase._NOT_SET:
                _params['policy_details'] = policy_details
            _request = shapes.CreateLifecyclePolicyRequest(**_params)
        response = self._boto_client.create_lifecycle_policy(
            **_request.to_boto_dict()
        )

        return shapes.CreateLifecyclePolicyResponse.from_boto_dict(response)

    def delete_lifecycle_policy(
        self,
        _request: shapes.DeleteLifecyclePolicyRequest = None,
        *,
        policy_id: str,
    ) -> shapes.DeleteLifecyclePolicyResponse:
        """
        Deletes the specified lifecycle policy and halts the automated operations that
        the policy specified.
        """
        if _request is None:
            _params = {}
            if policy_id is not autoboto.ShapeBase._NOT_SET:
                _params['policy_id'] = policy_id
            _request = shapes.DeleteLifecyclePolicyRequest(**_params)
        response = self._boto_client.delete_lifecycle_policy(
            **_request.to_boto_dict()
        )

        return shapes.DeleteLifecyclePolicyResponse.from_boto_dict(response)

    def get_lifecycle_policies(
        self,
        _request: shapes.GetLifecyclePoliciesRequest = None,
        *,
        policy_ids: typing.List[str] = autoboto.ShapeBase._NOT_SET,
        state: shapes.GettablePolicyStateValues = autoboto.ShapeBase._NOT_SET,
        resource_types: typing.List[shapes.ResourceTypeValues
                                   ] = autoboto.ShapeBase._NOT_SET,
        target_tags: typing.List[str] = autoboto.ShapeBase._NOT_SET,
        tags_to_add: typing.List[str] = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.GetLifecyclePoliciesResponse:
        """
        Gets summary information about all or the specified data lifecycle policies.

        To get complete information about a policy, use GetLifecyclePolicy.
        """
        if _request is None:
            _params = {}
            if policy_ids is not autoboto.ShapeBase._NOT_SET:
                _params['policy_ids'] = policy_ids
            if state is not autoboto.ShapeBase._NOT_SET:
                _params['state'] = state
            if resource_types is not autoboto.ShapeBase._NOT_SET:
                _params['resource_types'] = resource_types
            if target_tags is not autoboto.ShapeBase._NOT_SET:
                _params['target_tags'] = target_tags
            if tags_to_add is not autoboto.ShapeBase._NOT_SET:
                _params['tags_to_add'] = tags_to_add
            _request = shapes.GetLifecyclePoliciesRequest(**_params)
        response = self._boto_client.get_lifecycle_policies(
            **_request.to_boto_dict()
        )

        return shapes.GetLifecyclePoliciesResponse.from_boto_dict(response)

    def get_lifecycle_policy(
        self,
        _request: shapes.GetLifecyclePolicyRequest = None,
        *,
        policy_id: str,
    ) -> shapes.GetLifecyclePolicyResponse:
        """
        Gets detailed information about the specified lifecycle policy.
        """
        if _request is None:
            _params = {}
            if policy_id is not autoboto.ShapeBase._NOT_SET:
                _params['policy_id'] = policy_id
            _request = shapes.GetLifecyclePolicyRequest(**_params)
        response = self._boto_client.get_lifecycle_policy(
            **_request.to_boto_dict()
        )

        return shapes.GetLifecyclePolicyResponse.from_boto_dict(response)

    def update_lifecycle_policy(
        self,
        _request: shapes.UpdateLifecyclePolicyRequest = None,
        *,
        policy_id: str,
        execution_role_arn: str = autoboto.ShapeBase._NOT_SET,
        state: shapes.SettablePolicyStateValues = autoboto.ShapeBase._NOT_SET,
        description: str = autoboto.ShapeBase._NOT_SET,
        policy_details: shapes.PolicyDetails = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.UpdateLifecyclePolicyResponse:
        """
        Updates the specified lifecycle policy.
        """
        if _request is None:
            _params = {}
            if policy_id is not autoboto.ShapeBase._NOT_SET:
                _params['policy_id'] = policy_id
            if execution_role_arn is not autoboto.ShapeBase._NOT_SET:
                _params['execution_role_arn'] = execution_role_arn
            if state is not autoboto.ShapeBase._NOT_SET:
                _params['state'] = state
            if description is not autoboto.ShapeBase._NOT_SET:
                _params['description'] = description
            if policy_details is not autoboto.ShapeBase._NOT_SET:
                _params['policy_details'] = policy_details
            _request = shapes.UpdateLifecyclePolicyRequest(**_params)
        response = self._boto_client.update_lifecycle_policy(
            **_request.to_boto_dict()
        )

        return shapes.UpdateLifecyclePolicyResponse.from_boto_dict(response)
