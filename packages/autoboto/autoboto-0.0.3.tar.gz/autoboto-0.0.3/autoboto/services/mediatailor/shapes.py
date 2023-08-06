import datetime
import typing
import autoboto
import dataclasses


@dataclasses.dataclass
class CdnConfiguration(autoboto.ShapeBase):
    """
    The configuration for using a content delivery network (CDN), like Amazon
    CloudFront, for content and ad segment management.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ad_segment_url_prefix",
                "AdSegmentUrlPrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "content_segment_url_prefix",
                "ContentSegmentUrlPrefix",
                autoboto.TypeInfo(str),
            ),
        ]

    # A non-default content delivery network (CDN) to serve ad segments. By
    # default, AWS Elemental MediaTailor uses Amazon CloudFront with default
    # cache settings as its CDN for ad segments. To set up an alternate CDN,
    # create a rule in your CDN for the following origin:
    # ads.mediatailor.<region>.amazonaws.com. Then specify the rule's name in
    # this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest,
    # it reports your CDN as the source for ad segments.
    ad_segment_url_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A content delivery network (CDN) to cache content segments, so that content
    # requests don’t always have to go to the origin server. First, create a rule
    # in your CDN for the content segment origin server. Then specify the rule's
    # name in this ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves
    # a manifest, it reports your CDN as the source for content segments.
    content_segment_url_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class HlsConfiguration(autoboto.ShapeBase):
    """
    The configuration for HLS content.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "manifest_endpoint_prefix",
                "ManifestEndpointPrefix",
                autoboto.TypeInfo(str),
            ),
        ]

    # The URL that is used to initiate a playback session for devices that
    # support Apple HLS. The session uses server-side reporting.
    manifest_endpoint_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeletePlaybackConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier for the configuration.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeletePlaybackConfigurationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Empty(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetPlaybackConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier for the configuration.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetPlaybackConfigurationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ad_decision_server_url",
                "AdDecisionServerUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "cdn_configuration",
                "CdnConfiguration",
                autoboto.TypeInfo(CdnConfiguration),
            ),
            (
                "hls_configuration",
                "HlsConfiguration",
                autoboto.TypeInfo(HlsConfiguration),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "playback_endpoint_prefix",
                "PlaybackEndpointPrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "session_initialization_endpoint_prefix",
                "SessionInitializationEndpointPrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "slate_ad_url",
                "SlateAdUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "video_content_source_url",
                "VideoContentSourceUrl",
                autoboto.TypeInfo(str),
            ),
        ]

    # The URL for the ad decision server (ADS). This includes the specification
    # of static parameters and placeholders for dynamic parameters. AWS Elemental
    # MediaTailor substitutes player-specific and session-specific parameters as
    # needed when calling the ADS. Alternately, for testing, you can provide a
    # static VAST URL. The maximum length is 25000 characters.
    ad_decision_server_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The configuration for using a content delivery network (CDN), like Amazon
    # CloudFront, for content and ad segment management.
    cdn_configuration: "CdnConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The configuration for HLS content.
    hls_configuration: "HlsConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The identifier for the configuration.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL that the player accesses to get a manifest from AWS Elemental
    # MediaTailor. This session will use server-side reporting.
    playback_endpoint_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URL that the player uses to initialize a session that uses client-side
    # reporting.
    session_initialization_endpoint_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # URL for a high-quality video asset to transcode and use to fill in time
    # that's not used by ads. AWS Elemental MediaTailor shows the slate to fill
    # in gaps in media content. Configuring the slate is optional for non-VPAID
    # configurations. For VPAID, the slate is required because AWS Elemental
    # MediaTailor provides it in the slots designated for dynamic ad content. The
    # slate must be a high-quality asset that contains both audio and video.
    slate_ad_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL prefix for the master playlist for the stream, minus the asset ID.
    # The maximum length is 512 characters.
    video_content_source_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PlaybackConfiguration(autoboto.ShapeBase):
    """
    The AWSMediaTailor configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ad_decision_server_url",
                "AdDecisionServerUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "cdn_configuration",
                "CdnConfiguration",
                autoboto.TypeInfo(CdnConfiguration),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "slate_ad_url",
                "SlateAdUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "video_content_source_url",
                "VideoContentSourceUrl",
                autoboto.TypeInfo(str),
            ),
        ]

    # The URL for the ad decision server (ADS). This includes the specification
    # of static parameters and placeholders for dynamic parameters. AWS Elemental
    # MediaTailor substitutes player-specific and session-specific parameters as
    # needed when calling the ADS. Alternately, for testing, you can provide a
    # static VAST URL. The maximum length is 25000 characters.
    ad_decision_server_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The configuration for using a content delivery network (CDN), like Amazon
    # CloudFront, for content and ad segment management.
    cdn_configuration: "CdnConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The identifier for the configuration.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # URL for a high-quality video asset to transcode and use to fill in time
    # that's not used by ads. AWS Elemental MediaTailor shows the slate to fill
    # in gaps in media content. Configuring the slate is optional for non-VPAID
    # configurations. For VPAID, the slate is required because AWS Elemental
    # MediaTailor provides it in the slots designated for dynamic ad content. The
    # slate must be a high-quality asset that contains both audio and video.
    slate_ad_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL prefix for the master playlist for the stream, minus the asset ID.
    # The maximum length is 512 characters.
    video_content_source_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListPlaybackConfigurationsRequest(autoboto.ShapeBase):
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

    # Maximum number of records to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Pagination token returned by the GET list request when results overrun the
    # meximum allowed. Use the token to fetch the next page of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListPlaybackConfigurationsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "items",
                "Items",
                autoboto.TypeInfo(typing.List[PlaybackConfiguration]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Array of playback configurations. This may be all of the available
    # configurations or a subset, depending on the settings you provide and on
    # the total number of configurations stored.
    items: typing.List["PlaybackConfiguration"] = dataclasses.field(
        default_factory=list,
    )

    # Pagination token returned by the GET list request when results overrun the
    # meximum allowed. Use the token to fetch the next page of results.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PutPlaybackConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ad_decision_server_url",
                "AdDecisionServerUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "cdn_configuration",
                "CdnConfiguration",
                autoboto.TypeInfo(CdnConfiguration),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "slate_ad_url",
                "SlateAdUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "video_content_source_url",
                "VideoContentSourceUrl",
                autoboto.TypeInfo(str),
            ),
        ]

    # The URL for the ad decision server (ADS). This includes the specification
    # of static parameters and placeholders for dynamic parameters. AWS Elemental
    # MediaTailor substitutes player-specific and session-specific parameters as
    # needed when calling the ADS. Alternately, for testing you can provide a
    # static VAST URL. The maximum length is 25000 characters.
    ad_decision_server_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The configuration for using a content delivery network (CDN), like Amazon
    # CloudFront, for content and ad segment management.
    cdn_configuration: "CdnConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The identifier for the configuration.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL for a high-quality video asset to transcode and use to fill in time
    # that's not used by ads. AWS Elemental MediaTailor shows the slate to fill
    # in gaps in media content. Configuring the slate is optional for non-VPAID
    # configurations. For VPAID, the slate is required because AWS Elemental
    # MediaTailor provides it in the slots that are designated for dynamic ad
    # content. The slate must be a high-quality asset that contains both audio
    # and video.
    slate_ad_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL prefix for the master playlist for the stream, minus the asset ID.
    # The maximum length is 512 characters.
    video_content_source_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PutPlaybackConfigurationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ad_decision_server_url",
                "AdDecisionServerUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "cdn_configuration",
                "CdnConfiguration",
                autoboto.TypeInfo(CdnConfiguration),
            ),
            (
                "hls_configuration",
                "HlsConfiguration",
                autoboto.TypeInfo(HlsConfiguration),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "playback_endpoint_prefix",
                "PlaybackEndpointPrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "session_initialization_endpoint_prefix",
                "SessionInitializationEndpointPrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "slate_ad_url",
                "SlateAdUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "video_content_source_url",
                "VideoContentSourceUrl",
                autoboto.TypeInfo(str),
            ),
        ]

    # The URL for the ad decision server (ADS). This includes the specification
    # of static parameters and placeholders for dynamic parameters. AWS Elemental
    # MediaTailor substitutes player-specific and session-specific parameters as
    # needed when calling the ADS. Alternately, for testing, you can provide a
    # static VAST URL. The maximum length is 25000 characters.
    ad_decision_server_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The configuration for using a content delivery network (CDN), like Amazon
    # CloudFront, for content and ad segment management.
    cdn_configuration: "CdnConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The configuration for HLS content.
    hls_configuration: "HlsConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The identifier for the configuration.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL that the player accesses to get a manifest from AWS Elemental
    # MediaTailor. This session will use server-side reporting.
    playback_endpoint_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URL that the player uses to initialize a session that uses client-side
    # reporting.
    session_initialization_endpoint_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # URL for a high-quality video asset to transcode and use to fill in time
    # that's not used by ads. AWS Elemental MediaTailor shows the slate to fill
    # in gaps in media content. Configuring the slate is optional for non-VPAID
    # configurations. For VPAID, the slate is required because AWS Elemental
    # MediaTailor provides it in the slots designated for dynamic ad content. The
    # slate must be a high-quality asset that contains both audio and video.
    slate_ad_url: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URL prefix for the master playlist for the stream, minus the asset ID.
    # The maximum length is 512 characters.
    video_content_source_url: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
