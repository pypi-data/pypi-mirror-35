import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


class AdMarkers(Enum):
    NONE = "NONE"
    SCTE35_ENHANCED = "SCTE35_ENHANCED"
    PASSTHROUGH = "PASSTHROUGH"


@dataclasses.dataclass
class Channel(autoboto.ShapeBase):
    """
    A Channel resource configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "hls_ingest",
                "HlsIngest",
                autoboto.TypeInfo(HlsIngest),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) assigned to the Channel.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) ingest resource configuration.
    hls_ingest: "HlsIngest" = dataclasses.field(default_factory=dict, )

    # The ID of the Channel.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ChannelCreateParameters(autoboto.ShapeBase):
    """
    Configuration parameters for a new Channel.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Channel. The ID must be unique within the region and it
    # cannot be changed after a Channel is created.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ChannelList(autoboto.ShapeBase):
    """
    A collection of Channel records.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channels",
                "Channels",
                autoboto.TypeInfo(typing.List[Channel]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of Channel records.
    channels: typing.List["Channel"] = dataclasses.field(default_factory=list, )

    # A token that can be used to resume pagination from the end of the
    # collection.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ChannelUpdateParameters(autoboto.ShapeBase):
    """
    Configuration parameters for updating an existing Channel.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # A short text description of the Channel.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CmafEncryption(autoboto.ShapeBase):
    """
    A Common Media Application Format (CMAF) encryption configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "speke_key_provider",
                "SpekeKeyProvider",
                autoboto.TypeInfo(SpekeKeyProvider),
            ),
            (
                "key_rotation_interval_seconds",
                "KeyRotationIntervalSeconds",
                autoboto.TypeInfo(int),
            ),
        ]

    # A configuration for accessing an external Secure Packager and Encoder Key
    # Exchange (SPEKE) service that will provide encryption keys.
    speke_key_provider: "SpekeKeyProvider" = dataclasses.field(
        default_factory=dict,
    )

    # Time (in seconds) between each encryption key rotation.
    key_rotation_interval_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CmafPackage(autoboto.ShapeBase):
    """
    A Common Media Application Format (CMAF) packaging configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption",
                "Encryption",
                autoboto.TypeInfo(CmafEncryption),
            ),
            (
                "hls_manifests",
                "HlsManifests",
                autoboto.TypeInfo(typing.List[HlsManifest]),
            ),
            (
                "segment_duration_seconds",
                "SegmentDurationSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "segment_prefix",
                "SegmentPrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "stream_selection",
                "StreamSelection",
                autoboto.TypeInfo(StreamSelection),
            ),
        ]

    # A Common Media Application Format (CMAF) encryption configuration.
    encryption: "CmafEncryption" = dataclasses.field(default_factory=dict, )

    # A list of HLS manifest configurations
    hls_manifests: typing.List["HlsManifest"] = dataclasses.field(
        default_factory=list,
    )

    # Duration (in seconds) of each segment. Actual segments will be rounded to
    # the nearest multiple of the source segment duration.
    segment_duration_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An optional custom string that is prepended to the name of each segment. If
    # not specified, it defaults to the ChannelId.
    segment_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A StreamSelection configuration.
    stream_selection: "StreamSelection" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CmafPackageCreateOrUpdateParameters(autoboto.ShapeBase):
    """
    A Common Media Application Format (CMAF) packaging configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption",
                "Encryption",
                autoboto.TypeInfo(CmafEncryption),
            ),
            (
                "hls_manifests",
                "HlsManifests",
                autoboto.TypeInfo(
                    typing.List[HlsManifestCreateOrUpdateParameters]
                ),
            ),
            (
                "segment_duration_seconds",
                "SegmentDurationSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "segment_prefix",
                "SegmentPrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "stream_selection",
                "StreamSelection",
                autoboto.TypeInfo(StreamSelection),
            ),
        ]

    # A Common Media Application Format (CMAF) encryption configuration.
    encryption: "CmafEncryption" = dataclasses.field(default_factory=dict, )

    # A list of HLS manifest configurations
    hls_manifests: typing.List["HlsManifestCreateOrUpdateParameters"
                              ] = dataclasses.field(
                                  default_factory=list,
                              )

    # Duration (in seconds) of each segment. Actual segments will be rounded to
    # the nearest multiple of the source segment duration.
    segment_duration_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An optional custom string that is prepended to the name of each segment. If
    # not specified, it defaults to the ChannelId.
    segment_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A StreamSelection configuration.
    stream_selection: "StreamSelection" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateChannelRequest(autoboto.ShapeBase):
    """
    A new Channel configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Channel. The ID must be unique within the region and it
    # cannot be changed after a Channel is created.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateChannelResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "hls_ingest",
                "HlsIngest",
                autoboto.TypeInfo(HlsIngest),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the Channel.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) ingest resource configuration.
    hls_ingest: "HlsIngest" = dataclasses.field(default_factory=dict, )

    # The ID of the Channel.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateOriginEndpointRequest(autoboto.ShapeBase):
    """
    Configuration parameters used to create a new OriginEndpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "cmaf_package",
                "CmafPackage",
                autoboto.TypeInfo(CmafPackageCreateOrUpdateParameters),
            ),
            (
                "dash_package",
                "DashPackage",
                autoboto.TypeInfo(DashPackage),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "hls_package",
                "HlsPackage",
                autoboto.TypeInfo(HlsPackage),
            ),
            (
                "manifest_name",
                "ManifestName",
                autoboto.TypeInfo(str),
            ),
            (
                "mss_package",
                "MssPackage",
                autoboto.TypeInfo(MssPackage),
            ),
            (
                "startover_window_seconds",
                "StartoverWindowSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "time_delay_seconds",
                "TimeDelaySeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "whitelist",
                "Whitelist",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the Channel that the OriginEndpoint will be associated with. This
    # cannot be changed after the OriginEndpoint is created.
    channel_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the OriginEndpoint. The ID must be unique within the region and
    # it cannot be changed after the OriginEndpoint is created.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Common Media Application Format (CMAF) packaging configuration.
    cmaf_package: "CmafPackageCreateOrUpdateParameters" = dataclasses.field(
        default_factory=dict,
    )

    # A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    dash_package: "DashPackage" = dataclasses.field(default_factory=dict, )

    # A short text description of the OriginEndpoint.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) packaging configuration.
    hls_package: "HlsPackage" = dataclasses.field(default_factory=dict, )

    # A short string that will be used as the filename of the OriginEndpoint URL
    # (defaults to "index").
    manifest_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Microsoft Smooth Streaming (MSS) packaging configuration.
    mss_package: "MssPackage" = dataclasses.field(default_factory=dict, )

    # Maximum duration (seconds) of content to retain for startover playback. If
    # not specified, startover playback will be disabled for the OriginEndpoint.
    startover_window_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Amount of delay (seconds) to enforce on the playback of live content. If
    # not specified, there will be no time delay in effect for the
    # OriginEndpoint.
    time_delay_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of source IP CIDR blocks that will be allowed to access the
    # OriginEndpoint.
    whitelist: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateOriginEndpointResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "channel_id",
                "ChannelId",
                autoboto.TypeInfo(str),
            ),
            (
                "cmaf_package",
                "CmafPackage",
                autoboto.TypeInfo(CmafPackage),
            ),
            (
                "dash_package",
                "DashPackage",
                autoboto.TypeInfo(DashPackage),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "hls_package",
                "HlsPackage",
                autoboto.TypeInfo(HlsPackage),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "manifest_name",
                "ManifestName",
                autoboto.TypeInfo(str),
            ),
            (
                "mss_package",
                "MssPackage",
                autoboto.TypeInfo(MssPackage),
            ),
            (
                "startover_window_seconds",
                "StartoverWindowSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "time_delay_seconds",
                "TimeDelaySeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
            (
                "whitelist",
                "Whitelist",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the Channel the OriginEndpoint is associated with.
    channel_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Common Media Application Format (CMAF) packaging configuration.
    cmaf_package: "CmafPackage" = dataclasses.field(default_factory=dict, )

    # A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    dash_package: "DashPackage" = dataclasses.field(default_factory=dict, )

    # A short text description of the OriginEndpoint.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) packaging configuration.
    hls_package: "HlsPackage" = dataclasses.field(default_factory=dict, )

    # The ID of the OriginEndpoint.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A short string appended to the end of the OriginEndpoint URL.
    manifest_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Microsoft Smooth Streaming (MSS) packaging configuration.
    mss_package: "MssPackage" = dataclasses.field(default_factory=dict, )

    # Maximum duration (seconds) of content to retain for startover playback. If
    # not specified, startover playback will be disabled for the OriginEndpoint.
    startover_window_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Amount of delay (seconds) to enforce on the playback of live content. If
    # not specified, there will be no time delay in effect for the
    # OriginEndpoint.
    time_delay_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL of the packaged OriginEndpoint for consumption.
    url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of source IP CIDR blocks that will be allowed to access the
    # OriginEndpoint.
    whitelist: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DashEncryption(autoboto.ShapeBase):
    """
    A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "speke_key_provider",
                "SpekeKeyProvider",
                autoboto.TypeInfo(SpekeKeyProvider),
            ),
            (
                "key_rotation_interval_seconds",
                "KeyRotationIntervalSeconds",
                autoboto.TypeInfo(int),
            ),
        ]

    # A configuration for accessing an external Secure Packager and Encoder Key
    # Exchange (SPEKE) service that will provide encryption keys.
    speke_key_provider: "SpekeKeyProvider" = dataclasses.field(
        default_factory=dict,
    )

    # Time (in seconds) between each encryption key rotation.
    key_rotation_interval_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DashPackage(autoboto.ShapeBase):
    """
    A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption",
                "Encryption",
                autoboto.TypeInfo(DashEncryption),
            ),
            (
                "manifest_window_seconds",
                "ManifestWindowSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "min_buffer_time_seconds",
                "MinBufferTimeSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "min_update_period_seconds",
                "MinUpdatePeriodSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "period_triggers",
                "PeriodTriggers",
                autoboto.TypeInfo(typing.List[__PeriodTriggersElement]),
            ),
            (
                "profile",
                "Profile",
                autoboto.TypeInfo(Profile),
            ),
            (
                "segment_duration_seconds",
                "SegmentDurationSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "stream_selection",
                "StreamSelection",
                autoboto.TypeInfo(StreamSelection),
            ),
            (
                "suggested_presentation_delay_seconds",
                "SuggestedPresentationDelaySeconds",
                autoboto.TypeInfo(int),
            ),
        ]

    # A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
    encryption: "DashEncryption" = dataclasses.field(default_factory=dict, )

    # Time window (in seconds) contained in each manifest.
    manifest_window_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Minimum duration (in seconds) that a player will buffer media before
    # starting the presentation.
    min_buffer_time_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Minimum duration (in seconds) between potential changes to the Dynamic
    # Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).
    min_update_period_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of triggers that controls when the outgoing Dynamic Adaptive
    # Streaming over HTTP (DASH) Media Presentation Description (MPD) will be
    # partitioned into multiple periods. If empty, the content will not be
    # partitioned into more than one period. If the list contains "ADS", new
    # periods will be created where the Channel source contains SCTE-35 ad
    # markers.
    period_triggers: typing.List["__PeriodTriggersElement"] = dataclasses.field(
        default_factory=list,
    )

    # The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to
    # "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
    profile: "Profile" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Duration (in seconds) of each segment. Actual segments will be rounded to
    # the nearest multiple of the source segment duration.
    segment_duration_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A StreamSelection configuration.
    stream_selection: "StreamSelection" = dataclasses.field(
        default_factory=dict,
    )

    # Duration (in seconds) to delay live content before presentation.
    suggested_presentation_delay_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Channel to delete.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteChannelResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteOriginEndpointRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the OriginEndpoint to delete.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteOriginEndpointResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeChannelRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of a Channel.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeChannelResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "hls_ingest",
                "HlsIngest",
                autoboto.TypeInfo(HlsIngest),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the Channel.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) ingest resource configuration.
    hls_ingest: "HlsIngest" = dataclasses.field(default_factory=dict, )

    # The ID of the Channel.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeOriginEndpointRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the OriginEndpoint.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeOriginEndpointResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "channel_id",
                "ChannelId",
                autoboto.TypeInfo(str),
            ),
            (
                "cmaf_package",
                "CmafPackage",
                autoboto.TypeInfo(CmafPackage),
            ),
            (
                "dash_package",
                "DashPackage",
                autoboto.TypeInfo(DashPackage),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "hls_package",
                "HlsPackage",
                autoboto.TypeInfo(HlsPackage),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "manifest_name",
                "ManifestName",
                autoboto.TypeInfo(str),
            ),
            (
                "mss_package",
                "MssPackage",
                autoboto.TypeInfo(MssPackage),
            ),
            (
                "startover_window_seconds",
                "StartoverWindowSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "time_delay_seconds",
                "TimeDelaySeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
            (
                "whitelist",
                "Whitelist",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the Channel the OriginEndpoint is associated with.
    channel_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Common Media Application Format (CMAF) packaging configuration.
    cmaf_package: "CmafPackage" = dataclasses.field(default_factory=dict, )

    # A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    dash_package: "DashPackage" = dataclasses.field(default_factory=dict, )

    # A short text description of the OriginEndpoint.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) packaging configuration.
    hls_package: "HlsPackage" = dataclasses.field(default_factory=dict, )

    # The ID of the OriginEndpoint.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A short string appended to the end of the OriginEndpoint URL.
    manifest_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Microsoft Smooth Streaming (MSS) packaging configuration.
    mss_package: "MssPackage" = dataclasses.field(default_factory=dict, )

    # Maximum duration (seconds) of content to retain for startover playback. If
    # not specified, startover playback will be disabled for the OriginEndpoint.
    startover_window_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Amount of delay (seconds) to enforce on the playback of live content. If
    # not specified, there will be no time delay in effect for the
    # OriginEndpoint.
    time_delay_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL of the packaged OriginEndpoint for consumption.
    url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of source IP CIDR blocks that will be allowed to access the
    # OriginEndpoint.
    whitelist: typing.List[str] = dataclasses.field(default_factory=list, )


class EncryptionMethod(Enum):
    AES_128 = "AES_128"
    SAMPLE_AES = "SAMPLE_AES"


@dataclasses.dataclass
class ForbiddenException(autoboto.ShapeBase):
    """
    The client is not authorized to access the requested resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HlsEncryption(autoboto.ShapeBase):
    """
    An HTTP Live Streaming (HLS) encryption configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "speke_key_provider",
                "SpekeKeyProvider",
                autoboto.TypeInfo(SpekeKeyProvider),
            ),
            (
                "constant_initialization_vector",
                "ConstantInitializationVector",
                autoboto.TypeInfo(str),
            ),
            (
                "encryption_method",
                "EncryptionMethod",
                autoboto.TypeInfo(EncryptionMethod),
            ),
            (
                "key_rotation_interval_seconds",
                "KeyRotationIntervalSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "repeat_ext_x_key",
                "RepeatExtXKey",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A configuration for accessing an external Secure Packager and Encoder Key
    # Exchange (SPEKE) service that will provide encryption keys.
    speke_key_provider: "SpekeKeyProvider" = dataclasses.field(
        default_factory=dict,
    )

    # A constant initialization vector for encryption (optional). When not
    # specified the initialization vector will be periodically rotated.
    constant_initialization_vector: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The encryption method to use.
    encryption_method: "EncryptionMethod" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Interval (in seconds) between each encryption key rotation.
    key_rotation_interval_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When enabled, the EXT-X-KEY tag will be repeated in output manifests.
    repeat_ext_x_key: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class HlsIngest(autoboto.ShapeBase):
    """
    An HTTP Live Streaming (HLS) ingest resource configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ingest_endpoints",
                "IngestEndpoints",
                autoboto.TypeInfo(typing.List[IngestEndpoint]),
            ),
        ]

    # A list of endpoints to which the source stream should be sent.
    ingest_endpoints: typing.List["IngestEndpoint"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class HlsManifest(autoboto.ShapeBase):
    """
    A HTTP Live Streaming (HLS) manifest configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "ad_markers",
                "AdMarkers",
                autoboto.TypeInfo(AdMarkers),
            ),
            (
                "include_iframe_only_stream",
                "IncludeIframeOnlyStream",
                autoboto.TypeInfo(bool),
            ),
            (
                "manifest_name",
                "ManifestName",
                autoboto.TypeInfo(str),
            ),
            (
                "playlist_type",
                "PlaylistType",
                autoboto.TypeInfo(PlaylistType),
            ),
            (
                "playlist_window_seconds",
                "PlaylistWindowSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "program_date_time_interval_seconds",
                "ProgramDateTimeIntervalSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the manifest. The ID must be unique within the OriginEndpoint and
    # it cannot be changed after it is created.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This setting controls how ad markers are included in the packaged
    # OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output.
    # "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad
    # markers (comments) taken directly from the input HTTP Live Streaming (HLS)
    # manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on
    # SCTE-35 messages in the input source.
    ad_markers: "AdMarkers" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When enabled, an I-Frame only stream will be included in the output.
    include_iframe_only_stream: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An optional short string appended to the end of the OriginEndpoint URL. If
    # not specified, defaults to the manifestName for the OriginEndpoint.
    manifest_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD"
    # is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in
    # the media playlist.
    playlist_type: "PlaylistType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Time window (in seconds) contained in each parent manifest.
    playlist_window_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted
    # into manifests. Additionally, when an interval is specified ID3Timed
    # Metadata messages will be generated every 5 seconds using the ingest time
    # of the content. If the interval is not specified, or set to 0, then no EXT-
    # X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed
    # Metadata messages will be generated. Note that irrespective of this
    # parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS)
    # input, it will be passed through to HLS output.
    program_date_time_interval_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL of the packaged OriginEndpoint for consumption.
    url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HlsManifestCreateOrUpdateParameters(autoboto.ShapeBase):
    """
    A HTTP Live Streaming (HLS) manifest configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "ad_markers",
                "AdMarkers",
                autoboto.TypeInfo(AdMarkers),
            ),
            (
                "include_iframe_only_stream",
                "IncludeIframeOnlyStream",
                autoboto.TypeInfo(bool),
            ),
            (
                "manifest_name",
                "ManifestName",
                autoboto.TypeInfo(str),
            ),
            (
                "playlist_type",
                "PlaylistType",
                autoboto.TypeInfo(PlaylistType),
            ),
            (
                "playlist_window_seconds",
                "PlaylistWindowSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "program_date_time_interval_seconds",
                "ProgramDateTimeIntervalSeconds",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the manifest. The ID must be unique within the OriginEndpoint and
    # it cannot be changed after it is created.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This setting controls how ad markers are included in the packaged
    # OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output.
    # "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad
    # markers (comments) taken directly from the input HTTP Live Streaming (HLS)
    # manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on
    # SCTE-35 messages in the input source.
    ad_markers: "AdMarkers" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When enabled, an I-Frame only stream will be included in the output.
    include_iframe_only_stream: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An optional short string appended to the end of the OriginEndpoint URL. If
    # not specified, defaults to the manifestName for the OriginEndpoint.
    manifest_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD"
    # is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in
    # the media playlist.
    playlist_type: "PlaylistType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Time window (in seconds) contained in each parent manifest.
    playlist_window_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted
    # into manifests. Additionally, when an interval is specified ID3Timed
    # Metadata messages will be generated every 5 seconds using the ingest time
    # of the content. If the interval is not specified, or set to 0, then no EXT-
    # X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed
    # Metadata messages will be generated. Note that irrespective of this
    # parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS)
    # input, it will be passed through to HLS output.
    program_date_time_interval_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class HlsPackage(autoboto.ShapeBase):
    """
    An HTTP Live Streaming (HLS) packaging configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ad_markers",
                "AdMarkers",
                autoboto.TypeInfo(AdMarkers),
            ),
            (
                "encryption",
                "Encryption",
                autoboto.TypeInfo(HlsEncryption),
            ),
            (
                "include_iframe_only_stream",
                "IncludeIframeOnlyStream",
                autoboto.TypeInfo(bool),
            ),
            (
                "playlist_type",
                "PlaylistType",
                autoboto.TypeInfo(PlaylistType),
            ),
            (
                "playlist_window_seconds",
                "PlaylistWindowSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "program_date_time_interval_seconds",
                "ProgramDateTimeIntervalSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "segment_duration_seconds",
                "SegmentDurationSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "stream_selection",
                "StreamSelection",
                autoboto.TypeInfo(StreamSelection),
            ),
            (
                "use_audio_rendition_group",
                "UseAudioRenditionGroup",
                autoboto.TypeInfo(bool),
            ),
        ]

    # This setting controls how ad markers are included in the packaged
    # OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output.
    # "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad
    # markers (comments) taken directly from the input HTTP Live Streaming (HLS)
    # manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on
    # SCTE-35 messages in the input source.
    ad_markers: "AdMarkers" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An HTTP Live Streaming (HLS) encryption configuration.
    encryption: "HlsEncryption" = dataclasses.field(default_factory=dict, )

    # When enabled, an I-Frame only stream will be included in the output.
    include_iframe_only_stream: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD"
    # is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in
    # the media playlist.
    playlist_type: "PlaylistType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Time window (in seconds) contained in each parent manifest.
    playlist_window_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted
    # into manifests. Additionally, when an interval is specified ID3Timed
    # Metadata messages will be generated every 5 seconds using the ingest time
    # of the content. If the interval is not specified, or set to 0, then no EXT-
    # X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed
    # Metadata messages will be generated. Note that irrespective of this
    # parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS)
    # input, it will be passed through to HLS output.
    program_date_time_interval_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Duration (in seconds) of each fragment. Actual fragments will be rounded to
    # the nearest multiple of the source fragment duration.
    segment_duration_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A StreamSelection configuration.
    stream_selection: "StreamSelection" = dataclasses.field(
        default_factory=dict,
    )

    # When enabled, audio streams will be placed in rendition groups in the
    # output.
    use_audio_rendition_group: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class IngestEndpoint(autoboto.ShapeBase):
    """
    An endpoint for ingesting source content for a Channel.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "password",
                "Password",
                autoboto.TypeInfo(str),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
        ]

    # The system generated unique identifier for the IngestEndpoint
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The system generated password for ingest authentication.
    password: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ingest URL to which the source stream should be sent.
    url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The system generated username for ingest authentication.
    username: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServerErrorException(autoboto.ShapeBase):
    """
    An unexpected error occurred.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListChannelsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Upper bound on number of records to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A token used to resume pagination from the end of a previous request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListChannelsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "channels",
                "Channels",
                autoboto.TypeInfo(typing.List[Channel]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of Channel records.
    channels: typing.List["Channel"] = dataclasses.field(default_factory=list, )

    # A token that can be used to resume pagination from the end of the
    # collection.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOriginEndpointsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # When specified, the request will return only OriginEndpoints associated
    # with the given Channel ID.
    channel_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The upper bound on the number of records to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A token used to resume pagination from the end of a previous request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOriginEndpointsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "origin_endpoints",
                "OriginEndpoints",
                autoboto.TypeInfo(typing.List[OriginEndpoint]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A token that can be used to resume pagination from the end of the
    # collection.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of OriginEndpoint records.
    origin_endpoints: typing.List["OriginEndpoint"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class MssEncryption(autoboto.ShapeBase):
    """
    A Microsoft Smooth Streaming (MSS) encryption configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "speke_key_provider",
                "SpekeKeyProvider",
                autoboto.TypeInfo(SpekeKeyProvider),
            ),
        ]

    # A configuration for accessing an external Secure Packager and Encoder Key
    # Exchange (SPEKE) service that will provide encryption keys.
    speke_key_provider: "SpekeKeyProvider" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class MssPackage(autoboto.ShapeBase):
    """
    A Microsoft Smooth Streaming (MSS) packaging configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption",
                "Encryption",
                autoboto.TypeInfo(MssEncryption),
            ),
            (
                "manifest_window_seconds",
                "ManifestWindowSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "segment_duration_seconds",
                "SegmentDurationSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "stream_selection",
                "StreamSelection",
                autoboto.TypeInfo(StreamSelection),
            ),
        ]

    # A Microsoft Smooth Streaming (MSS) encryption configuration.
    encryption: "MssEncryption" = dataclasses.field(default_factory=dict, )

    # The time window (in seconds) contained in each manifest.
    manifest_window_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The duration (in seconds) of each segment.
    segment_duration_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A StreamSelection configuration.
    stream_selection: "StreamSelection" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class NotFoundException(autoboto.ShapeBase):
    """
    The requested resource does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OriginEndpoint(autoboto.ShapeBase):
    """
    An OriginEndpoint resource configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "channel_id",
                "ChannelId",
                autoboto.TypeInfo(str),
            ),
            (
                "cmaf_package",
                "CmafPackage",
                autoboto.TypeInfo(CmafPackage),
            ),
            (
                "dash_package",
                "DashPackage",
                autoboto.TypeInfo(DashPackage),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "hls_package",
                "HlsPackage",
                autoboto.TypeInfo(HlsPackage),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "manifest_name",
                "ManifestName",
                autoboto.TypeInfo(str),
            ),
            (
                "mss_package",
                "MssPackage",
                autoboto.TypeInfo(MssPackage),
            ),
            (
                "startover_window_seconds",
                "StartoverWindowSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "time_delay_seconds",
                "TimeDelaySeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
            (
                "whitelist",
                "Whitelist",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the Channel the OriginEndpoint is associated with.
    channel_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Common Media Application Format (CMAF) packaging configuration.
    cmaf_package: "CmafPackage" = dataclasses.field(default_factory=dict, )

    # A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    dash_package: "DashPackage" = dataclasses.field(default_factory=dict, )

    # A short text description of the OriginEndpoint.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) packaging configuration.
    hls_package: "HlsPackage" = dataclasses.field(default_factory=dict, )

    # The ID of the OriginEndpoint.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A short string appended to the end of the OriginEndpoint URL.
    manifest_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Microsoft Smooth Streaming (MSS) packaging configuration.
    mss_package: "MssPackage" = dataclasses.field(default_factory=dict, )

    # Maximum duration (seconds) of content to retain for startover playback. If
    # not specified, startover playback will be disabled for the OriginEndpoint.
    startover_window_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Amount of delay (seconds) to enforce on the playback of live content. If
    # not specified, there will be no time delay in effect for the
    # OriginEndpoint.
    time_delay_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL of the packaged OriginEndpoint for consumption.
    url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of source IP CIDR blocks that will be allowed to access the
    # OriginEndpoint.
    whitelist: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class OriginEndpointCreateParameters(autoboto.ShapeBase):
    """
    Configuration parameters for a new OriginEndpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "cmaf_package",
                "CmafPackage",
                autoboto.TypeInfo(CmafPackageCreateOrUpdateParameters),
            ),
            (
                "dash_package",
                "DashPackage",
                autoboto.TypeInfo(DashPackage),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "hls_package",
                "HlsPackage",
                autoboto.TypeInfo(HlsPackage),
            ),
            (
                "manifest_name",
                "ManifestName",
                autoboto.TypeInfo(str),
            ),
            (
                "mss_package",
                "MssPackage",
                autoboto.TypeInfo(MssPackage),
            ),
            (
                "startover_window_seconds",
                "StartoverWindowSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "time_delay_seconds",
                "TimeDelaySeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "whitelist",
                "Whitelist",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the Channel that the OriginEndpoint will be associated with. This
    # cannot be changed after the OriginEndpoint is created.
    channel_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the OriginEndpoint. The ID must be unique within the region and
    # it cannot be changed after the OriginEndpoint is created.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Common Media Application Format (CMAF) packaging configuration.
    cmaf_package: "CmafPackageCreateOrUpdateParameters" = dataclasses.field(
        default_factory=dict,
    )

    # A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    dash_package: "DashPackage" = dataclasses.field(default_factory=dict, )

    # A short text description of the OriginEndpoint.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) packaging configuration.
    hls_package: "HlsPackage" = dataclasses.field(default_factory=dict, )

    # A short string that will be used as the filename of the OriginEndpoint URL
    # (defaults to "index").
    manifest_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Microsoft Smooth Streaming (MSS) packaging configuration.
    mss_package: "MssPackage" = dataclasses.field(default_factory=dict, )

    # Maximum duration (seconds) of content to retain for startover playback. If
    # not specified, startover playback will be disabled for the OriginEndpoint.
    startover_window_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Amount of delay (seconds) to enforce on the playback of live content. If
    # not specified, there will be no time delay in effect for the
    # OriginEndpoint.
    time_delay_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of source IP CIDR blocks that will be allowed to access the
    # OriginEndpoint.
    whitelist: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class OriginEndpointList(autoboto.ShapeBase):
    """
    A collection of OriginEndpoint records.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "origin_endpoints",
                "OriginEndpoints",
                autoboto.TypeInfo(typing.List[OriginEndpoint]),
            ),
        ]

    # A token that can be used to resume pagination from the end of the
    # collection.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of OriginEndpoint records.
    origin_endpoints: typing.List["OriginEndpoint"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class OriginEndpointUpdateParameters(autoboto.ShapeBase):
    """
    Configuration parameters for updating an existing OriginEndpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cmaf_package",
                "CmafPackage",
                autoboto.TypeInfo(CmafPackageCreateOrUpdateParameters),
            ),
            (
                "dash_package",
                "DashPackage",
                autoboto.TypeInfo(DashPackage),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "hls_package",
                "HlsPackage",
                autoboto.TypeInfo(HlsPackage),
            ),
            (
                "manifest_name",
                "ManifestName",
                autoboto.TypeInfo(str),
            ),
            (
                "mss_package",
                "MssPackage",
                autoboto.TypeInfo(MssPackage),
            ),
            (
                "startover_window_seconds",
                "StartoverWindowSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "time_delay_seconds",
                "TimeDelaySeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "whitelist",
                "Whitelist",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A Common Media Application Format (CMAF) packaging configuration.
    cmaf_package: "CmafPackageCreateOrUpdateParameters" = dataclasses.field(
        default_factory=dict,
    )

    # A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    dash_package: "DashPackage" = dataclasses.field(default_factory=dict, )

    # A short text description of the OriginEndpoint.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) packaging configuration.
    hls_package: "HlsPackage" = dataclasses.field(default_factory=dict, )

    # A short string that will be appended to the end of the Endpoint URL.
    manifest_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Microsoft Smooth Streaming (MSS) packaging configuration.
    mss_package: "MssPackage" = dataclasses.field(default_factory=dict, )

    # Maximum duration (in seconds) of content to retain for startover playback.
    # If not specified, startover playback will be disabled for the
    # OriginEndpoint.
    startover_window_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Amount of delay (in seconds) to enforce on the playback of live content. If
    # not specified, there will be no time delay in effect for the
    # OriginEndpoint.
    time_delay_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of source IP CIDR blocks that will be allowed to access the
    # OriginEndpoint.
    whitelist: typing.List[str] = dataclasses.field(default_factory=list, )


class PlaylistType(Enum):
    NONE = "NONE"
    EVENT = "EVENT"
    VOD = "VOD"


class Profile(Enum):
    NONE = "NONE"
    HBBTV_1_5 = "HBBTV_1_5"


@dataclasses.dataclass
class RotateChannelCredentialsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the channel to update.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RotateChannelCredentialsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "hls_ingest",
                "HlsIngest",
                autoboto.TypeInfo(HlsIngest),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the Channel.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) ingest resource configuration.
    hls_ingest: "HlsIngest" = dataclasses.field(default_factory=dict, )

    # The ID of the Channel.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RotateIngestEndpointCredentialsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "ingest_endpoint_id",
                "IngestEndpointId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the channel the IngestEndpoint is on.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The id of the IngestEndpoint whose credentials should be rotated
    ingest_endpoint_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RotateIngestEndpointCredentialsResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "hls_ingest",
                "HlsIngest",
                autoboto.TypeInfo(HlsIngest),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the Channel.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) ingest resource configuration.
    hls_ingest: "HlsIngest" = dataclasses.field(default_factory=dict, )

    # The ID of the Channel.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceUnavailableException(autoboto.ShapeBase):
    """
    An unexpected error occurred.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SpekeKeyProvider(autoboto.ShapeBase):
    """
    A configuration for accessing an external Secure Packager and Encoder Key
    Exchange (SPEKE) service that will provide encryption keys.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "system_ids",
                "SystemIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
        ]

    # The resource ID to include in key requests.
    resource_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
    # MediaPackage will assume when accessing the key provider service.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The system IDs to include in key requests.
    system_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The URL of the external key provider service.
    url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class StreamOrder(Enum):
    ORIGINAL = "ORIGINAL"
    VIDEO_BITRATE_ASCENDING = "VIDEO_BITRATE_ASCENDING"
    VIDEO_BITRATE_DESCENDING = "VIDEO_BITRATE_DESCENDING"


@dataclasses.dataclass
class StreamSelection(autoboto.ShapeBase):
    """
    A StreamSelection configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_video_bits_per_second",
                "MaxVideoBitsPerSecond",
                autoboto.TypeInfo(int),
            ),
            (
                "min_video_bits_per_second",
                "MinVideoBitsPerSecond",
                autoboto.TypeInfo(int),
            ),
            (
                "stream_order",
                "StreamOrder",
                autoboto.TypeInfo(StreamOrder),
            ),
        ]

    # The maximum video bitrate (bps) to include in output.
    max_video_bits_per_second: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The minimum video bitrate (bps) to include in output.
    min_video_bits_per_second: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A directive that determines the order of streams in the output.
    stream_order: "StreamOrder" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TooManyRequestsException(autoboto.ShapeBase):
    """
    The client has exceeded their resource or throttling limits.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnprocessableEntityException(autoboto.ShapeBase):
    """
    The parameters sent in the request are not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateChannelRequest(autoboto.ShapeBase):
    """
    Configuration parameters used to update the Channel.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the Channel to update.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateChannelResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "hls_ingest",
                "HlsIngest",
                autoboto.TypeInfo(HlsIngest),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the Channel.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A short text description of the Channel.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) ingest resource configuration.
    hls_ingest: "HlsIngest" = dataclasses.field(default_factory=dict, )

    # The ID of the Channel.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateOriginEndpointRequest(autoboto.ShapeBase):
    """
    Configuration parameters used to update an existing OriginEndpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "cmaf_package",
                "CmafPackage",
                autoboto.TypeInfo(CmafPackageCreateOrUpdateParameters),
            ),
            (
                "dash_package",
                "DashPackage",
                autoboto.TypeInfo(DashPackage),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "hls_package",
                "HlsPackage",
                autoboto.TypeInfo(HlsPackage),
            ),
            (
                "manifest_name",
                "ManifestName",
                autoboto.TypeInfo(str),
            ),
            (
                "mss_package",
                "MssPackage",
                autoboto.TypeInfo(MssPackage),
            ),
            (
                "startover_window_seconds",
                "StartoverWindowSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "time_delay_seconds",
                "TimeDelaySeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "whitelist",
                "Whitelist",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the OriginEndpoint to update.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Common Media Application Format (CMAF) packaging configuration.
    cmaf_package: "CmafPackageCreateOrUpdateParameters" = dataclasses.field(
        default_factory=dict,
    )

    # A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    dash_package: "DashPackage" = dataclasses.field(default_factory=dict, )

    # A short text description of the OriginEndpoint.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) packaging configuration.
    hls_package: "HlsPackage" = dataclasses.field(default_factory=dict, )

    # A short string that will be appended to the end of the Endpoint URL.
    manifest_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Microsoft Smooth Streaming (MSS) packaging configuration.
    mss_package: "MssPackage" = dataclasses.field(default_factory=dict, )

    # Maximum duration (in seconds) of content to retain for startover playback.
    # If not specified, startover playback will be disabled for the
    # OriginEndpoint.
    startover_window_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Amount of delay (in seconds) to enforce on the playback of live content. If
    # not specified, there will be no time delay in effect for the
    # OriginEndpoint.
    time_delay_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of source IP CIDR blocks that will be allowed to access the
    # OriginEndpoint.
    whitelist: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class UpdateOriginEndpointResponse(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                autoboto.TypeInfo(str),
            ),
            (
                "channel_id",
                "ChannelId",
                autoboto.TypeInfo(str),
            ),
            (
                "cmaf_package",
                "CmafPackage",
                autoboto.TypeInfo(CmafPackage),
            ),
            (
                "dash_package",
                "DashPackage",
                autoboto.TypeInfo(DashPackage),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "hls_package",
                "HlsPackage",
                autoboto.TypeInfo(HlsPackage),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "manifest_name",
                "ManifestName",
                autoboto.TypeInfo(str),
            ),
            (
                "mss_package",
                "MssPackage",
                autoboto.TypeInfo(MssPackage),
            ),
            (
                "startover_window_seconds",
                "StartoverWindowSeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "time_delay_seconds",
                "TimeDelaySeconds",
                autoboto.TypeInfo(int),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
            (
                "whitelist",
                "Whitelist",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID of the Channel the OriginEndpoint is associated with.
    channel_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Common Media Application Format (CMAF) packaging configuration.
    cmaf_package: "CmafPackage" = dataclasses.field(default_factory=dict, )

    # A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    dash_package: "DashPackage" = dataclasses.field(default_factory=dict, )

    # A short text description of the OriginEndpoint.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An HTTP Live Streaming (HLS) packaging configuration.
    hls_package: "HlsPackage" = dataclasses.field(default_factory=dict, )

    # The ID of the OriginEndpoint.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A short string appended to the end of the OriginEndpoint URL.
    manifest_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Microsoft Smooth Streaming (MSS) packaging configuration.
    mss_package: "MssPackage" = dataclasses.field(default_factory=dict, )

    # Maximum duration (seconds) of content to retain for startover playback. If
    # not specified, startover playback will be disabled for the OriginEndpoint.
    startover_window_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Amount of delay (seconds) to enforce on the playback of live content. If
    # not specified, there will be no time delay in effect for the
    # OriginEndpoint.
    time_delay_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL of the packaged OriginEndpoint for consumption.
    url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of source IP CIDR blocks that will be allowed to access the
    # OriginEndpoint.
    whitelist: typing.List[str] = dataclasses.field(default_factory=list, )


class __PeriodTriggersElement(Enum):
    ADS = "ADS"
