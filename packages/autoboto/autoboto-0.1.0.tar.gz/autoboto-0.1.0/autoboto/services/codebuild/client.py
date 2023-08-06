import datetime
import typing
import boto3
import autoboto
from . import shapes


class Client:
    def __init__(self, *args, **kwargs):
        self._boto_client = boto3.client("codebuild", *args, **kwargs)

    def batch_delete_builds(
        self,
        _request: shapes.BatchDeleteBuildsInput = None,
        *,
        ids: typing.List[str],
    ) -> shapes.BatchDeleteBuildsOutput:
        """
        Deletes one or more builds.
        """
        if _request is None:
            _params = {}
            if ids is not autoboto.ShapeBase.NOT_SET:
                _params['ids'] = ids
            _request = shapes.BatchDeleteBuildsInput(**_params)
        response = self._boto_client.batch_delete_builds(
            **_request.to_boto_dict()
        )

        return shapes.BatchDeleteBuildsOutput.from_boto_dict(response)

    def batch_get_builds(
        self,
        _request: shapes.BatchGetBuildsInput = None,
        *,
        ids: typing.List[str],
    ) -> shapes.BatchGetBuildsOutput:
        """
        Gets information about builds.
        """
        if _request is None:
            _params = {}
            if ids is not autoboto.ShapeBase.NOT_SET:
                _params['ids'] = ids
            _request = shapes.BatchGetBuildsInput(**_params)
        response = self._boto_client.batch_get_builds(**_request.to_boto_dict())

        return shapes.BatchGetBuildsOutput.from_boto_dict(response)

    def batch_get_projects(
        self,
        _request: shapes.BatchGetProjectsInput = None,
        *,
        names: typing.List[str],
    ) -> shapes.BatchGetProjectsOutput:
        """
        Gets information about build projects.
        """
        if _request is None:
            _params = {}
            if names is not autoboto.ShapeBase.NOT_SET:
                _params['names'] = names
            _request = shapes.BatchGetProjectsInput(**_params)
        response = self._boto_client.batch_get_projects(
            **_request.to_boto_dict()
        )

        return shapes.BatchGetProjectsOutput.from_boto_dict(response)

    def create_project(
        self,
        _request: shapes.CreateProjectInput = None,
        *,
        name: str,
        source: shapes.ProjectSource,
        artifacts: shapes.ProjectArtifacts,
        environment: shapes.ProjectEnvironment,
        service_role: str,
        description: str = autoboto.ShapeBase.NOT_SET,
        secondary_sources: typing.List[shapes.ProjectSource
                                      ] = autoboto.ShapeBase.NOT_SET,
        secondary_artifacts: typing.List[shapes.ProjectArtifacts
                                        ] = autoboto.ShapeBase.NOT_SET,
        cache: shapes.ProjectCache = autoboto.ShapeBase.NOT_SET,
        timeout_in_minutes: int = autoboto.ShapeBase.NOT_SET,
        encryption_key: str = autoboto.ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = autoboto.ShapeBase.NOT_SET,
        vpc_config: shapes.VpcConfig = autoboto.ShapeBase.NOT_SET,
        badge_enabled: bool = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.CreateProjectOutput:
        """
        Creates a build project.
        """
        if _request is None:
            _params = {}
            if name is not autoboto.ShapeBase.NOT_SET:
                _params['name'] = name
            if source is not autoboto.ShapeBase.NOT_SET:
                _params['source'] = source
            if artifacts is not autoboto.ShapeBase.NOT_SET:
                _params['artifacts'] = artifacts
            if environment is not autoboto.ShapeBase.NOT_SET:
                _params['environment'] = environment
            if service_role is not autoboto.ShapeBase.NOT_SET:
                _params['service_role'] = service_role
            if description is not autoboto.ShapeBase.NOT_SET:
                _params['description'] = description
            if secondary_sources is not autoboto.ShapeBase.NOT_SET:
                _params['secondary_sources'] = secondary_sources
            if secondary_artifacts is not autoboto.ShapeBase.NOT_SET:
                _params['secondary_artifacts'] = secondary_artifacts
            if cache is not autoboto.ShapeBase.NOT_SET:
                _params['cache'] = cache
            if timeout_in_minutes is not autoboto.ShapeBase.NOT_SET:
                _params['timeout_in_minutes'] = timeout_in_minutes
            if encryption_key is not autoboto.ShapeBase.NOT_SET:
                _params['encryption_key'] = encryption_key
            if tags is not autoboto.ShapeBase.NOT_SET:
                _params['tags'] = tags
            if vpc_config is not autoboto.ShapeBase.NOT_SET:
                _params['vpc_config'] = vpc_config
            if badge_enabled is not autoboto.ShapeBase.NOT_SET:
                _params['badge_enabled'] = badge_enabled
            _request = shapes.CreateProjectInput(**_params)
        response = self._boto_client.create_project(**_request.to_boto_dict())

        return shapes.CreateProjectOutput.from_boto_dict(response)

    def create_webhook(
        self,
        _request: shapes.CreateWebhookInput = None,
        *,
        project_name: str,
        branch_filter: str = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.CreateWebhookOutput:
        """
        For an existing AWS CodeBuild build project that has its source code stored in a
        GitHub repository, enables AWS CodeBuild to begin automatically rebuilding the
        source code every time a code change is pushed to the repository.

        If you enable webhooks for an AWS CodeBuild project, and the project is used as
        a build step in AWS CodePipeline, then two identical builds will be created for
        each commit. One build is triggered through webhooks, and one through AWS
        CodePipeline. Because billing is on a per-build basis, you will be billed for
        both builds. Therefore, if you are using AWS CodePipeline, we recommend that you
        disable webhooks in CodeBuild. In the AWS CodeBuild console, clear the Webhook
        box. For more information, see step 5 in [Change a Build Project's
        Settings](http://docs.aws.amazon.com/codebuild/latest/userguide/change-
        project.html#change-project-console).
        """
        if _request is None:
            _params = {}
            if project_name is not autoboto.ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            if branch_filter is not autoboto.ShapeBase.NOT_SET:
                _params['branch_filter'] = branch_filter
            _request = shapes.CreateWebhookInput(**_params)
        response = self._boto_client.create_webhook(**_request.to_boto_dict())

        return shapes.CreateWebhookOutput.from_boto_dict(response)

    def delete_project(
        self,
        _request: shapes.DeleteProjectInput = None,
        *,
        name: str,
    ) -> shapes.DeleteProjectOutput:
        """
        Deletes a build project.
        """
        if _request is None:
            _params = {}
            if name is not autoboto.ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteProjectInput(**_params)
        response = self._boto_client.delete_project(**_request.to_boto_dict())

        return shapes.DeleteProjectOutput.from_boto_dict(response)

    def delete_webhook(
        self,
        _request: shapes.DeleteWebhookInput = None,
        *,
        project_name: str,
    ) -> shapes.DeleteWebhookOutput:
        """
        For an existing AWS CodeBuild build project that has its source code stored in a
        GitHub repository, stops AWS CodeBuild from automatically rebuilding the source
        code every time a code change is pushed to the repository.
        """
        if _request is None:
            _params = {}
            if project_name is not autoboto.ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            _request = shapes.DeleteWebhookInput(**_params)
        response = self._boto_client.delete_webhook(**_request.to_boto_dict())

        return shapes.DeleteWebhookOutput.from_boto_dict(response)

    def invalidate_project_cache(
        self,
        _request: shapes.InvalidateProjectCacheInput = None,
        *,
        project_name: str,
    ) -> shapes.InvalidateProjectCacheOutput:
        """
        Resets the cache for a project.
        """
        if _request is None:
            _params = {}
            if project_name is not autoboto.ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            _request = shapes.InvalidateProjectCacheInput(**_params)
        response = self._boto_client.invalidate_project_cache(
            **_request.to_boto_dict()
        )

        return shapes.InvalidateProjectCacheOutput.from_boto_dict(response)

    def list_builds(
        self,
        _request: shapes.ListBuildsInput = None,
        *,
        sort_order: shapes.SortOrderType = autoboto.ShapeBase.NOT_SET,
        next_token: str = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.ListBuildsOutput:
        """
        Gets a list of build IDs, with each build ID representing a single build.
        """
        if _request is None:
            _params = {}
            if sort_order is not autoboto.ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if next_token is not autoboto.ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListBuildsInput(**_params)
        response = self._boto_client.list_builds(**_request.to_boto_dict())

        return shapes.ListBuildsOutput.from_boto_dict(response)

    def list_builds_for_project(
        self,
        _request: shapes.ListBuildsForProjectInput = None,
        *,
        project_name: str,
        sort_order: shapes.SortOrderType = autoboto.ShapeBase.NOT_SET,
        next_token: str = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.ListBuildsForProjectOutput:
        """
        Gets a list of build IDs for the specified build project, with each build ID
        representing a single build.
        """
        if _request is None:
            _params = {}
            if project_name is not autoboto.ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            if sort_order is not autoboto.ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if next_token is not autoboto.ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListBuildsForProjectInput(**_params)
        response = self._boto_client.list_builds_for_project(
            **_request.to_boto_dict()
        )

        return shapes.ListBuildsForProjectOutput.from_boto_dict(response)

    def list_curated_environment_images(
        self,
        _request: shapes.ListCuratedEnvironmentImagesInput = None,
    ) -> shapes.ListCuratedEnvironmentImagesOutput:
        """
        Gets information about Docker images that are managed by AWS CodeBuild.
        """
        if _request is None:
            _params = {}
            _request = shapes.ListCuratedEnvironmentImagesInput(**_params)
        response = self._boto_client.list_curated_environment_images(
            **_request.to_boto_dict()
        )

        return shapes.ListCuratedEnvironmentImagesOutput.from_boto_dict(
            response
        )

    def list_projects(
        self,
        _request: shapes.ListProjectsInput = None,
        *,
        sort_by: shapes.ProjectSortByType = autoboto.ShapeBase.NOT_SET,
        sort_order: shapes.SortOrderType = autoboto.ShapeBase.NOT_SET,
        next_token: str = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.ListProjectsOutput:
        """
        Gets a list of build project names, with each build project name representing a
        single build project.
        """
        if _request is None:
            _params = {}
            if sort_by is not autoboto.ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            if sort_order is not autoboto.ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if next_token is not autoboto.ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListProjectsInput(**_params)
        response = self._boto_client.list_projects(**_request.to_boto_dict())

        return shapes.ListProjectsOutput.from_boto_dict(response)

    def start_build(
        self,
        _request: shapes.StartBuildInput = None,
        *,
        project_name: str,
        secondary_sources_override: typing.List[shapes.ProjectSource
                                               ] = autoboto.ShapeBase.NOT_SET,
        secondary_sources_version_override: typing.List[
            shapes.ProjectSourceVersion
        ] = autoboto.ShapeBase.NOT_SET,
        source_version: str = autoboto.ShapeBase.NOT_SET,
        artifacts_override: shapes.ProjectArtifacts = autoboto.ShapeBase.
        NOT_SET,
        secondary_artifacts_override: typing.List[shapes.ProjectArtifacts
                                                 ] = autoboto.ShapeBase.NOT_SET,
        environment_variables_override: typing.List[
            shapes.EnvironmentVariable
        ] = autoboto.ShapeBase.NOT_SET,
        source_type_override: shapes.SourceType = autoboto.ShapeBase.NOT_SET,
        source_location_override: str = autoboto.ShapeBase.NOT_SET,
        source_auth_override: shapes.SourceAuth = autoboto.ShapeBase.NOT_SET,
        git_clone_depth_override: int = autoboto.ShapeBase.NOT_SET,
        buildspec_override: str = autoboto.ShapeBase.NOT_SET,
        insecure_ssl_override: bool = autoboto.ShapeBase.NOT_SET,
        report_build_status_override: bool = autoboto.ShapeBase.NOT_SET,
        environment_type_override: shapes.EnvironmentType = autoboto.ShapeBase.
        NOT_SET,
        image_override: str = autoboto.ShapeBase.NOT_SET,
        compute_type_override: shapes.ComputeType = autoboto.ShapeBase.NOT_SET,
        certificate_override: str = autoboto.ShapeBase.NOT_SET,
        cache_override: shapes.ProjectCache = autoboto.ShapeBase.NOT_SET,
        service_role_override: str = autoboto.ShapeBase.NOT_SET,
        privileged_mode_override: bool = autoboto.ShapeBase.NOT_SET,
        timeout_in_minutes_override: int = autoboto.ShapeBase.NOT_SET,
        idempotency_token: str = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.StartBuildOutput:
        """
        Starts running a build.
        """
        if _request is None:
            _params = {}
            if project_name is not autoboto.ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            if secondary_sources_override is not autoboto.ShapeBase.NOT_SET:
                _params['secondary_sources_override'
                       ] = secondary_sources_override
            if secondary_sources_version_override is not autoboto.ShapeBase.NOT_SET:
                _params['secondary_sources_version_override'
                       ] = secondary_sources_version_override
            if source_version is not autoboto.ShapeBase.NOT_SET:
                _params['source_version'] = source_version
            if artifacts_override is not autoboto.ShapeBase.NOT_SET:
                _params['artifacts_override'] = artifacts_override
            if secondary_artifacts_override is not autoboto.ShapeBase.NOT_SET:
                _params['secondary_artifacts_override'
                       ] = secondary_artifacts_override
            if environment_variables_override is not autoboto.ShapeBase.NOT_SET:
                _params['environment_variables_override'
                       ] = environment_variables_override
            if source_type_override is not autoboto.ShapeBase.NOT_SET:
                _params['source_type_override'] = source_type_override
            if source_location_override is not autoboto.ShapeBase.NOT_SET:
                _params['source_location_override'] = source_location_override
            if source_auth_override is not autoboto.ShapeBase.NOT_SET:
                _params['source_auth_override'] = source_auth_override
            if git_clone_depth_override is not autoboto.ShapeBase.NOT_SET:
                _params['git_clone_depth_override'] = git_clone_depth_override
            if buildspec_override is not autoboto.ShapeBase.NOT_SET:
                _params['buildspec_override'] = buildspec_override
            if insecure_ssl_override is not autoboto.ShapeBase.NOT_SET:
                _params['insecure_ssl_override'] = insecure_ssl_override
            if report_build_status_override is not autoboto.ShapeBase.NOT_SET:
                _params['report_build_status_override'
                       ] = report_build_status_override
            if environment_type_override is not autoboto.ShapeBase.NOT_SET:
                _params['environment_type_override'] = environment_type_override
            if image_override is not autoboto.ShapeBase.NOT_SET:
                _params['image_override'] = image_override
            if compute_type_override is not autoboto.ShapeBase.NOT_SET:
                _params['compute_type_override'] = compute_type_override
            if certificate_override is not autoboto.ShapeBase.NOT_SET:
                _params['certificate_override'] = certificate_override
            if cache_override is not autoboto.ShapeBase.NOT_SET:
                _params['cache_override'] = cache_override
            if service_role_override is not autoboto.ShapeBase.NOT_SET:
                _params['service_role_override'] = service_role_override
            if privileged_mode_override is not autoboto.ShapeBase.NOT_SET:
                _params['privileged_mode_override'] = privileged_mode_override
            if timeout_in_minutes_override is not autoboto.ShapeBase.NOT_SET:
                _params['timeout_in_minutes_override'
                       ] = timeout_in_minutes_override
            if idempotency_token is not autoboto.ShapeBase.NOT_SET:
                _params['idempotency_token'] = idempotency_token
            _request = shapes.StartBuildInput(**_params)
        response = self._boto_client.start_build(**_request.to_boto_dict())

        return shapes.StartBuildOutput.from_boto_dict(response)

    def stop_build(
        self,
        _request: shapes.StopBuildInput = None,
        *,
        id: str,
    ) -> shapes.StopBuildOutput:
        """
        Attempts to stop running a build.
        """
        if _request is None:
            _params = {}
            if id is not autoboto.ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.StopBuildInput(**_params)
        response = self._boto_client.stop_build(**_request.to_boto_dict())

        return shapes.StopBuildOutput.from_boto_dict(response)

    def update_project(
        self,
        _request: shapes.UpdateProjectInput = None,
        *,
        name: str,
        description: str = autoboto.ShapeBase.NOT_SET,
        source: shapes.ProjectSource = autoboto.ShapeBase.NOT_SET,
        secondary_sources: typing.List[shapes.ProjectSource
                                      ] = autoboto.ShapeBase.NOT_SET,
        artifacts: shapes.ProjectArtifacts = autoboto.ShapeBase.NOT_SET,
        secondary_artifacts: typing.List[shapes.ProjectArtifacts
                                        ] = autoboto.ShapeBase.NOT_SET,
        cache: shapes.ProjectCache = autoboto.ShapeBase.NOT_SET,
        environment: shapes.ProjectEnvironment = autoboto.ShapeBase.NOT_SET,
        service_role: str = autoboto.ShapeBase.NOT_SET,
        timeout_in_minutes: int = autoboto.ShapeBase.NOT_SET,
        encryption_key: str = autoboto.ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = autoboto.ShapeBase.NOT_SET,
        vpc_config: shapes.VpcConfig = autoboto.ShapeBase.NOT_SET,
        badge_enabled: bool = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.UpdateProjectOutput:
        """
        Changes the settings of a build project.
        """
        if _request is None:
            _params = {}
            if name is not autoboto.ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not autoboto.ShapeBase.NOT_SET:
                _params['description'] = description
            if source is not autoboto.ShapeBase.NOT_SET:
                _params['source'] = source
            if secondary_sources is not autoboto.ShapeBase.NOT_SET:
                _params['secondary_sources'] = secondary_sources
            if artifacts is not autoboto.ShapeBase.NOT_SET:
                _params['artifacts'] = artifacts
            if secondary_artifacts is not autoboto.ShapeBase.NOT_SET:
                _params['secondary_artifacts'] = secondary_artifacts
            if cache is not autoboto.ShapeBase.NOT_SET:
                _params['cache'] = cache
            if environment is not autoboto.ShapeBase.NOT_SET:
                _params['environment'] = environment
            if service_role is not autoboto.ShapeBase.NOT_SET:
                _params['service_role'] = service_role
            if timeout_in_minutes is not autoboto.ShapeBase.NOT_SET:
                _params['timeout_in_minutes'] = timeout_in_minutes
            if encryption_key is not autoboto.ShapeBase.NOT_SET:
                _params['encryption_key'] = encryption_key
            if tags is not autoboto.ShapeBase.NOT_SET:
                _params['tags'] = tags
            if vpc_config is not autoboto.ShapeBase.NOT_SET:
                _params['vpc_config'] = vpc_config
            if badge_enabled is not autoboto.ShapeBase.NOT_SET:
                _params['badge_enabled'] = badge_enabled
            _request = shapes.UpdateProjectInput(**_params)
        response = self._boto_client.update_project(**_request.to_boto_dict())

        return shapes.UpdateProjectOutput.from_boto_dict(response)

    def update_webhook(
        self,
        _request: shapes.UpdateWebhookInput = None,
        *,
        project_name: str,
        branch_filter: str = autoboto.ShapeBase.NOT_SET,
        rotate_secret: bool = autoboto.ShapeBase.NOT_SET,
    ) -> shapes.UpdateWebhookOutput:
        """
        Updates the webhook associated with an AWS CodeBuild build project.
        """
        if _request is None:
            _params = {}
            if project_name is not autoboto.ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            if branch_filter is not autoboto.ShapeBase.NOT_SET:
                _params['branch_filter'] = branch_filter
            if rotate_secret is not autoboto.ShapeBase.NOT_SET:
                _params['rotate_secret'] = rotate_secret
            _request = shapes.UpdateWebhookInput(**_params)
        response = self._boto_client.update_webhook(**_request.to_boto_dict())

        return shapes.UpdateWebhookOutput.from_boto_dict(response)
