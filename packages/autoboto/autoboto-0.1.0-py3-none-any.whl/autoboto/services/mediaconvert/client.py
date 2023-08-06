import datetime
import typing
import boto3
import autoboto
from . import shapes


class Client:
    def __init__(self, *args, **kwargs):
        self._boto_client = boto3.client("mediaconvert", *args, **kwargs)

    def cancel_job(
        self,
        _request: shapes.CancelJobRequest = None,
        *,
        id: str,
    ) -> shapes.CancelJobResponse:
        """
        Permanently remove a job from a queue. Once you have canceled a job, you can't
        start it again. You can't delete a running job.
        """
        if _request is None:
            _params = {}
            if id is not autoboto.ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.CancelJobRequest(**_params)
        response = self._boto_client.cancel_job(**_request.to_boto_dict())

        return shapes.CancelJobResponse.from_boto_dict(response)

    def create_job(
        self,
        _request: shapes.CreateJobRequest = None,
        *,
        role: str,
        settings: shapes.JobSettings,
        client_request_token: str = autoboto.ShapeBase.NOT_SET,
        job_template: str = autoboto.ShapeBase.NOT_SET,
        queue: str = autoboto.ShapeBase.NOT_SET,
        user_metadata: typing.Dict[str, str] = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.CreateJobResponse:
        """
        Create a new transcoding job. For information about jobs and job settings, see
        the User Guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html
        """
        if _request is None:
            _params = {}
            if role is not autoboto.ShapeBase.NOT_SET:
                _params['role'] = role
            if settings is not autoboto.ShapeBase.NOT_SET:
                _params['settings'] = settings
            if client_request_token is not autoboto.ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if job_template is not autoboto.ShapeBase.NOT_SET:
                _params['job_template'] = job_template
            if queue is not autoboto.ShapeBase.NOT_SET:
                _params['queue'] = queue
            if user_metadata is not autoboto.ShapeBase.NOT_SET:
                _params['user_metadata'] = user_metadata
            _request = shapes.CreateJobRequest(**_params)
        response = self._boto_client.create_job(**_request.to_boto_dict())

        return shapes.CreateJobResponse.from_boto_dict(response)

    def create_job_template(
        self,
        _request: shapes.CreateJobTemplateRequest = None,
        *,
        name: str,
        settings: shapes.JobTemplateSettings,
        category: str = autoboto.ShapeBase.NOT_SET,
        description: str = autoboto.ShapeBase.NOT_SET,
        queue: str = autoboto.ShapeBase.NOT_SET,
        tags: typing.Dict[str, str] = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.CreateJobTemplateResponse:
        """
        Create a new job template. For information about job templates see the User
        Guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html
        """
        if _request is None:
            _params = {}
            if name is not autoboto.ShapeBase.NOT_SET:
                _params['name'] = name
            if settings is not autoboto.ShapeBase.NOT_SET:
                _params['settings'] = settings
            if category is not autoboto.ShapeBase.NOT_SET:
                _params['category'] = category
            if description is not autoboto.ShapeBase.NOT_SET:
                _params['description'] = description
            if queue is not autoboto.ShapeBase.NOT_SET:
                _params['queue'] = queue
            if tags is not autoboto.ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateJobTemplateRequest(**_params)
        response = self._boto_client.create_job_template(
            **_request.to_boto_dict()
        )

        return shapes.CreateJobTemplateResponse.from_boto_dict(response)

    def create_preset(
        self,
        _request: shapes.CreatePresetRequest = None,
        *,
        name: str,
        settings: shapes.PresetSettings,
        category: str = autoboto.ShapeBase.NOT_SET,
        description: str = autoboto.ShapeBase.NOT_SET,
        tags: typing.Dict[str, str] = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.CreatePresetResponse:
        """
        Create a new preset. For information about job templates see the User Guide at
        http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html
        """
        if _request is None:
            _params = {}
            if name is not autoboto.ShapeBase.NOT_SET:
                _params['name'] = name
            if settings is not autoboto.ShapeBase.NOT_SET:
                _params['settings'] = settings
            if category is not autoboto.ShapeBase.NOT_SET:
                _params['category'] = category
            if description is not autoboto.ShapeBase.NOT_SET:
                _params['description'] = description
            if tags is not autoboto.ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreatePresetRequest(**_params)
        response = self._boto_client.create_preset(**_request.to_boto_dict())

        return shapes.CreatePresetResponse.from_boto_dict(response)

    def create_queue(
        self,
        _request: shapes.CreateQueueRequest = None,
        *,
        name: str,
        description: str = autoboto.ShapeBase.NOT_SET,
        tags: typing.Dict[str, str] = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.CreateQueueResponse:
        """
        Create a new transcoding queue. For information about job templates see the User
        Guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html
        """
        if _request is None:
            _params = {}
            if name is not autoboto.ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not autoboto.ShapeBase.NOT_SET:
                _params['description'] = description
            if tags is not autoboto.ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateQueueRequest(**_params)
        response = self._boto_client.create_queue(**_request.to_boto_dict())

        return shapes.CreateQueueResponse.from_boto_dict(response)

    def delete_job_template(
        self,
        _request: shapes.DeleteJobTemplateRequest = None,
        *,
        name: str,
    ) -> shapes.DeleteJobTemplateResponse:
        """
        Permanently delete a job template you have created.
        """
        if _request is None:
            _params = {}
            if name is not autoboto.ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteJobTemplateRequest(**_params)
        response = self._boto_client.delete_job_template(
            **_request.to_boto_dict()
        )

        return shapes.DeleteJobTemplateResponse.from_boto_dict(response)

    def delete_preset(
        self,
        _request: shapes.DeletePresetRequest = None,
        *,
        name: str,
    ) -> shapes.DeletePresetResponse:
        """
        Permanently delete a preset you have created.
        """
        if _request is None:
            _params = {}
            if name is not autoboto.ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeletePresetRequest(**_params)
        response = self._boto_client.delete_preset(**_request.to_boto_dict())

        return shapes.DeletePresetResponse.from_boto_dict(response)

    def delete_queue(
        self,
        _request: shapes.DeleteQueueRequest = None,
        *,
        name: str,
    ) -> shapes.DeleteQueueResponse:
        """
        Permanently delete a queue you have created.
        """
        if _request is None:
            _params = {}
            if name is not autoboto.ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteQueueRequest(**_params)
        response = self._boto_client.delete_queue(**_request.to_boto_dict())

        return shapes.DeleteQueueResponse.from_boto_dict(response)

    def describe_endpoints(
        self,
        _request: shapes.DescribeEndpointsRequest = None,
        *,
        max_results: int = autoboto.ShapeBase.NOT_SET,
        next_token: str = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.DescribeEndpointsResponse:
        """
        Send an request with an empty body to the regional API endpoint to get your
        account API endpoint.
        """
        if _request is None:
            _params = {}
            if max_results is not autoboto.ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not autoboto.ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeEndpointsRequest(**_params)
        response = self._boto_client.describe_endpoints(
            **_request.to_boto_dict()
        )

        return shapes.DescribeEndpointsResponse.from_boto_dict(response)

    def get_job(
        self,
        _request: shapes.GetJobRequest = None,
        *,
        id: str,
    ) -> shapes.GetJobResponse:
        """
        Retrieve the JSON for a specific completed transcoding job.
        """
        if _request is None:
            _params = {}
            if id is not autoboto.ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetJobRequest(**_params)
        response = self._boto_client.get_job(**_request.to_boto_dict())

        return shapes.GetJobResponse.from_boto_dict(response)

    def get_job_template(
        self,
        _request: shapes.GetJobTemplateRequest = None,
        *,
        name: str,
    ) -> shapes.GetJobTemplateResponse:
        """
        Retrieve the JSON for a specific job template.
        """
        if _request is None:
            _params = {}
            if name is not autoboto.ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.GetJobTemplateRequest(**_params)
        response = self._boto_client.get_job_template(**_request.to_boto_dict())

        return shapes.GetJobTemplateResponse.from_boto_dict(response)

    def get_preset(
        self,
        _request: shapes.GetPresetRequest = None,
        *,
        name: str,
    ) -> shapes.GetPresetResponse:
        """
        Retrieve the JSON for a specific preset.
        """
        if _request is None:
            _params = {}
            if name is not autoboto.ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.GetPresetRequest(**_params)
        response = self._boto_client.get_preset(**_request.to_boto_dict())

        return shapes.GetPresetResponse.from_boto_dict(response)

    def get_queue(
        self,
        _request: shapes.GetQueueRequest = None,
        *,
        name: str,
    ) -> shapes.GetQueueResponse:
        """
        Retrieve the JSON for a specific queue.
        """
        if _request is None:
            _params = {}
            if name is not autoboto.ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.GetQueueRequest(**_params)
        response = self._boto_client.get_queue(**_request.to_boto_dict())

        return shapes.GetQueueResponse.from_boto_dict(response)

    def list_job_templates(
        self,
        _request: shapes.ListJobTemplatesRequest = None,
        *,
        category: str = autoboto.ShapeBase.NOT_SET,
        list_by: shapes.JobTemplateListBy = autoboto.ShapeBase.NOT_SET,
        max_results: int = autoboto.ShapeBase.NOT_SET,
        next_token: str = autoboto.ShapeBase.NOT_SET,
        order: shapes.Order = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.ListJobTemplatesResponse:
        """
        Retrieve a JSON array of up to twenty of your job templates. This will return
        the templates themselves, not just a list of them. To retrieve the next twenty
        templates, use the nextToken string returned with the array
        """
        if _request is None:
            _params = {}
            if category is not autoboto.ShapeBase.NOT_SET:
                _params['category'] = category
            if list_by is not autoboto.ShapeBase.NOT_SET:
                _params['list_by'] = list_by
            if max_results is not autoboto.ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not autoboto.ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if order is not autoboto.ShapeBase.NOT_SET:
                _params['order'] = order
            _request = shapes.ListJobTemplatesRequest(**_params)
        response = self._boto_client.list_job_templates(
            **_request.to_boto_dict()
        )

        return shapes.ListJobTemplatesResponse.from_boto_dict(response)

    def list_jobs(
        self,
        _request: shapes.ListJobsRequest = None,
        *,
        max_results: int = autoboto.ShapeBase.NOT_SET,
        next_token: str = autoboto.ShapeBase.NOT_SET,
        order: shapes.Order = autoboto.ShapeBase.NOT_SET,
        queue: str = autoboto.ShapeBase.NOT_SET,
        status: shapes.JobStatus = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.ListJobsResponse:
        """
        Retrieve a JSON array of up to twenty of your most recently created jobs. This
        array includes in-process, completed, and errored jobs. This will return the
        jobs themselves, not just a list of the jobs. To retrieve the twenty next most
        recent jobs, use the nextToken string returned with the array.
        """
        if _request is None:
            _params = {}
            if max_results is not autoboto.ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not autoboto.ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if order is not autoboto.ShapeBase.NOT_SET:
                _params['order'] = order
            if queue is not autoboto.ShapeBase.NOT_SET:
                _params['queue'] = queue
            if status is not autoboto.ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.ListJobsRequest(**_params)
        response = self._boto_client.list_jobs(**_request.to_boto_dict())

        return shapes.ListJobsResponse.from_boto_dict(response)

    def list_presets(
        self,
        _request: shapes.ListPresetsRequest = None,
        *,
        category: str = autoboto.ShapeBase.NOT_SET,
        list_by: shapes.PresetListBy = autoboto.ShapeBase.NOT_SET,
        max_results: int = autoboto.ShapeBase.NOT_SET,
        next_token: str = autoboto.ShapeBase.NOT_SET,
        order: shapes.Order = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.ListPresetsResponse:
        """
        Retrieve a JSON array of up to twenty of your presets. This will return the
        presets themselves, not just a list of them. To retrieve the next twenty
        presets, use the nextToken string returned with the array.
        """
        if _request is None:
            _params = {}
            if category is not autoboto.ShapeBase.NOT_SET:
                _params['category'] = category
            if list_by is not autoboto.ShapeBase.NOT_SET:
                _params['list_by'] = list_by
            if max_results is not autoboto.ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not autoboto.ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if order is not autoboto.ShapeBase.NOT_SET:
                _params['order'] = order
            _request = shapes.ListPresetsRequest(**_params)
        response = self._boto_client.list_presets(**_request.to_boto_dict())

        return shapes.ListPresetsResponse.from_boto_dict(response)

    def list_queues(
        self,
        _request: shapes.ListQueuesRequest = None,
        *,
        list_by: shapes.QueueListBy = autoboto.ShapeBase.NOT_SET,
        max_results: int = autoboto.ShapeBase.NOT_SET,
        next_token: str = autoboto.ShapeBase.NOT_SET,
        order: shapes.Order = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.ListQueuesResponse:
        """
        Retrieve a JSON array of up to twenty of your queues. This will return the
        queues themselves, not just a list of them. To retrieve the next twenty queues,
        use the nextToken string returned with the array.
        """
        if _request is None:
            _params = {}
            if list_by is not autoboto.ShapeBase.NOT_SET:
                _params['list_by'] = list_by
            if max_results is not autoboto.ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not autoboto.ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if order is not autoboto.ShapeBase.NOT_SET:
                _params['order'] = order
            _request = shapes.ListQueuesRequest(**_params)
        response = self._boto_client.list_queues(**_request.to_boto_dict())

        return shapes.ListQueuesResponse.from_boto_dict(response)

    def list_tags_for_resource(
        self,
        _request: shapes.ListTagsForResourceRequest = None,
        *,
        arn: str,
    ) -> shapes.ListTagsForResourceResponse:
        """
        Retrieve the tags for a MediaConvert resource.
        """
        if _request is None:
            _params = {}
            if arn is not autoboto.ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.ListTagsForResourceRequest(**_params)
        response = self._boto_client.list_tags_for_resource(
            **_request.to_boto_dict()
        )

        return shapes.ListTagsForResourceResponse.from_boto_dict(response)

    def tag_resource(
        self,
        _request: shapes.TagResourceRequest = None,
        *,
        arn: str,
        tags: typing.Dict[str, str],
    ) -> shapes.TagResourceResponse:
        """
        Tag a MediaConvert queue, preset, or job template. For information about these
        resource types, see the User Guide at
        http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html
        """
        if _request is None:
            _params = {}
            if arn is not autoboto.ShapeBase.NOT_SET:
                _params['arn'] = arn
            if tags is not autoboto.ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagResourceRequest(**_params)
        response = self._boto_client.tag_resource(**_request.to_boto_dict())

        return shapes.TagResourceResponse.from_boto_dict(response)

    def untag_resource(
        self,
        _request: shapes.UntagResourceRequest = None,
        *,
        arn: str = autoboto.ShapeBase.NOT_SET,
        tag_keys: typing.List[str] = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.UntagResourceResponse:
        """
        Untag a MediaConvert queue, preset, or job template. For information about these
        resource types, see the User Guide at
        http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html
        """
        if _request is None:
            _params = {}
            if arn is not autoboto.ShapeBase.NOT_SET:
                _params['arn'] = arn
            if tag_keys is not autoboto.ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagResourceRequest(**_params)
        response = self._boto_client.untag_resource(**_request.to_boto_dict())

        return shapes.UntagResourceResponse.from_boto_dict(response)

    def update_job_template(
        self,
        _request: shapes.UpdateJobTemplateRequest = None,
        *,
        name: str,
        category: str = autoboto.ShapeBase.NOT_SET,
        description: str = autoboto.ShapeBase.NOT_SET,
        queue: str = autoboto.ShapeBase.NOT_SET,
        settings: shapes.JobTemplateSettings = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.UpdateJobTemplateResponse:
        """
        Modify one of your existing job templates.
        """
        if _request is None:
            _params = {}
            if name is not autoboto.ShapeBase.NOT_SET:
                _params['name'] = name
            if category is not autoboto.ShapeBase.NOT_SET:
                _params['category'] = category
            if description is not autoboto.ShapeBase.NOT_SET:
                _params['description'] = description
            if queue is not autoboto.ShapeBase.NOT_SET:
                _params['queue'] = queue
            if settings is not autoboto.ShapeBase.NOT_SET:
                _params['settings'] = settings
            _request = shapes.UpdateJobTemplateRequest(**_params)
        response = self._boto_client.update_job_template(
            **_request.to_boto_dict()
        )

        return shapes.UpdateJobTemplateResponse.from_boto_dict(response)

    def update_preset(
        self,
        _request: shapes.UpdatePresetRequest = None,
        *,
        name: str,
        category: str = autoboto.ShapeBase.NOT_SET,
        description: str = autoboto.ShapeBase.NOT_SET,
        settings: shapes.PresetSettings = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.UpdatePresetResponse:
        """
        Modify one of your existing presets.
        """
        if _request is None:
            _params = {}
            if name is not autoboto.ShapeBase.NOT_SET:
                _params['name'] = name
            if category is not autoboto.ShapeBase.NOT_SET:
                _params['category'] = category
            if description is not autoboto.ShapeBase.NOT_SET:
                _params['description'] = description
            if settings is not autoboto.ShapeBase.NOT_SET:
                _params['settings'] = settings
            _request = shapes.UpdatePresetRequest(**_params)
        response = self._boto_client.update_preset(**_request.to_boto_dict())

        return shapes.UpdatePresetResponse.from_boto_dict(response)

    def update_queue(
        self,
        _request: shapes.UpdateQueueRequest = None,
        *,
        name: str,
        description: str = autoboto.ShapeBase.NOT_SET,
        status: shapes.QueueStatus = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.UpdateQueueResponse:
        """
        Modify one of your existing queues.
        """
        if _request is None:
            _params = {}
            if name is not autoboto.ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not autoboto.ShapeBase.NOT_SET:
                _params['description'] = description
            if status is not autoboto.ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.UpdateQueueRequest(**_params)
        response = self._boto_client.update_queue(**_request.to_boto_dict())

        return shapes.UpdateQueueResponse.from_boto_dict(response)
