import datetime
import typing
import autoboto
import dataclasses


@dataclasses.dataclass
class AssociateDeviceWithPlacementRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                autoboto.TypeInfo(str),
            ),
            (
                "placement_name",
                "placementName",
                autoboto.TypeInfo(str),
            ),
            (
                "device_id",
                "deviceId",
                autoboto.TypeInfo(str),
            ),
            (
                "device_template_name",
                "deviceTemplateName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the project containing the placement in which to associate the
    # device.
    project_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the placement in which to associate the device.
    placement_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the physical device to be associated with the given placement in
    # the project. Note that a mandatory 4 character prefix is required for all
    # `deviceId` values.
    device_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The device template name to associate with the device ID.
    device_template_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociateDeviceWithPlacementResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreatePlacementRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "placement_name",
                "placementName",
                autoboto.TypeInfo(str),
            ),
            (
                "project_name",
                "projectName",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the placement to be created.
    placement_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the project in which to create the placement.
    project_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Optional user-defined key/value pairs providing contextual data (such as
    # location or function) for the placement.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePlacementResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateProjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "placement_template",
                "placementTemplate",
                autoboto.TypeInfo(PlacementTemplate),
            ),
        ]

    # The name of the project to create.
    project_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional description for the project.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The schema defining the placement to be created. A placement template
    # defines placement default attributes and device templates. You cannot add
    # or remove device templates after the project has been created. However, you
    # can update `callbackOverrides` for the device templates using the
    # `UpdateProject` API.
    placement_template: "PlacementTemplate" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateProjectResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeletePlacementRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "placement_name",
                "placementName",
                autoboto.TypeInfo(str),
            ),
            (
                "project_name",
                "projectName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the empty placement to delete.
    placement_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The project containing the empty placement to delete.
    project_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletePlacementResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteProjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the empty project to delete.
    project_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProjectResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribePlacementRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "placement_name",
                "placementName",
                autoboto.TypeInfo(str),
            ),
            (
                "project_name",
                "projectName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the placement within a project.
    placement_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The project containing the placement to be described.
    project_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePlacementResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "placement",
                "placement",
                autoboto.TypeInfo(PlacementDescription),
            ),
        ]

    # An object describing the placement.
    placement: "PlacementDescription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeProjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the project to be described.
    project_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProjectResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project",
                "project",
                autoboto.TypeInfo(ProjectDescription),
            ),
        ]

    # An object describing the project.
    project: "ProjectDescription" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeviceTemplate(autoboto.ShapeBase):
    """
    An object representing a device for a placement template (see
    PlacementTemplate).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_type",
                "deviceType",
                autoboto.TypeInfo(str),
            ),
            (
                "callback_overrides",
                "callbackOverrides",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The device type, which currently must be `"button"`.
    device_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional Lambda function to invoke instead of the default Lambda
    # function provided by the placement template.
    callback_overrides: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateDeviceFromPlacementRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                autoboto.TypeInfo(str),
            ),
            (
                "placement_name",
                "placementName",
                autoboto.TypeInfo(str),
            ),
            (
                "device_template_name",
                "deviceTemplateName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the project that contains the placement.
    project_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the placement that the device should be removed from.
    placement_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The device ID that should be removed from the placement.
    device_template_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateDeviceFromPlacementResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetDevicesInPlacementRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                autoboto.TypeInfo(str),
            ),
            (
                "placement_name",
                "placementName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the project containing the placement.
    project_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the placement to get the devices from.
    placement_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDevicesInPlacementResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "devices",
                "devices",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # An object containing the devices (zero or more) within the placement.
    devices: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalFailureException(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRequestException(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPlacementsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The project containing the placements to be listed.
    project_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to return per request. If not set, a default
    # value of 100 is used.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPlacementsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "placements",
                "placements",
                autoboto.TypeInfo(typing.List[PlacementSummary]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An object listing the requested placements.
    placements: typing.List["PlacementSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The token used to retrieve the next set of results - will be effectively
    # empty if there are no further results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListProjectsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of results to return per request. If not set, a default
    # value of 100 is used.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListProjectsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "projects",
                "projects",
                autoboto.TypeInfo(typing.List[ProjectSummary]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An object containing the list of projects.
    projects: typing.List["ProjectSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The token used to retrieve the next set of results - will be effectively
    # empty if there are no further results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PlacementDescription(autoboto.ShapeBase):
    """
    An object describing a project's placement.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                autoboto.TypeInfo(str),
            ),
            (
                "placement_name",
                "placementName",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "created_date",
                "createdDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "updated_date",
                "updatedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the project containing the placement.
    project_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the placement.
    placement_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The user-defined attributes associated with the placement.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date when the placement was initially created, in UNIX epoch time
    # format.
    created_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date when the placement was last updated, in UNIX epoch time format. If
    # the placement was not updated, then `createdDate` and `updatedDate` are the
    # same.
    updated_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PlacementSummary(autoboto.ShapeBase):
    """
    An object providing summary information for a particular placement.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                autoboto.TypeInfo(str),
            ),
            (
                "placement_name",
                "placementName",
                autoboto.TypeInfo(str),
            ),
            (
                "created_date",
                "createdDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "updated_date",
                "updatedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the project containing the placement.
    project_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the placement being summarized.
    placement_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date when the placement was originally created, in UNIX epoch time
    # format.
    created_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date when the placement was last updated, in UNIX epoch time format. If
    # the placement was not updated, then `createdDate` and `updatedDate` are the
    # same.
    updated_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PlacementTemplate(autoboto.ShapeBase):
    """
    An object defining the template for a placement.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "default_attributes",
                "defaultAttributes",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "device_templates",
                "deviceTemplates",
                autoboto.TypeInfo(typing.Dict[str, DeviceTemplate]),
            ),
        ]

    # The default attributes (key/value pairs) to be applied to all placements
    # using this template.
    default_attributes: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An object specifying the DeviceTemplate for all placements using this
    # (PlacementTemplate) template.
    device_templates: typing.Dict[str, "DeviceTemplate"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ProjectDescription(autoboto.ShapeBase):
    """
    An object providing detailed information for a particular project associated
    with an AWS account and region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                autoboto.TypeInfo(str),
            ),
            (
                "created_date",
                "createdDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "updated_date",
                "updatedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "placement_template",
                "placementTemplate",
                autoboto.TypeInfo(PlacementTemplate),
            ),
        ]

    # The name of the project for which to obtain information from.
    project_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date when the project was originally created, in UNIX epoch time
    # format.
    created_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date when the project was last updated, in UNIX epoch time format. If
    # the project was not updated, then `createdDate` and `updatedDate` are the
    # same.
    updated_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description of the project.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An object describing the project's placement specifications.
    placement_template: "PlacementTemplate" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ProjectSummary(autoboto.ShapeBase):
    """
    An object providing summary information for a particular project for an
    associated AWS account and region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                autoboto.TypeInfo(str),
            ),
            (
                "created_date",
                "createdDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "updated_date",
                "updatedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the project being summarized.
    project_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date when the project was originally created, in UNIX epoch time
    # format.
    created_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date when the project was last updated, in UNIX epoch time format. If
    # the project was not updated, then `createdDate` and `updatedDate` are the
    # same.
    updated_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceConflictException(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyRequestsException(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePlacementRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "placement_name",
                "placementName",
                autoboto.TypeInfo(str),
            ),
            (
                "project_name",
                "projectName",
                autoboto.TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the placement to update.
    placement_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the project containing the placement to be updated.
    project_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user-defined object of attributes used to update the placement. The
    # maximum number of key/value pairs is 50.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdatePlacementResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateProjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "placement_template",
                "placementTemplate",
                autoboto.TypeInfo(PlacementTemplate),
            ),
        ]

    # The name of the project to be updated.
    project_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional user-defined description for the project.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An object defining the project update. Once a project has been created, you
    # cannot add device template names to the project. However, for a given
    # `placementTemplate`, you can update the associated `callbackOverrides` for
    # the device definition using this API.
    placement_template: "PlacementTemplate" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateProjectResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []
