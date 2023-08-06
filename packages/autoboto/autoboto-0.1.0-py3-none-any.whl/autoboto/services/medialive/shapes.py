import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


class AacCodingMode(Enum):
    """
    Placeholder documentation for AacCodingMode
    """
    AD_RECEIVER_MIX = "AD_RECEIVER_MIX"
    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_1_1 = "CODING_MODE_1_1"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_5_1 = "CODING_MODE_5_1"


class AacInputType(Enum):
    """
    Placeholder documentation for AacInputType
    """
    BROADCASTER_MIXED_AD = "BROADCASTER_MIXED_AD"
    NORMAL = "NORMAL"


class AacProfile(Enum):
    """
    Placeholder documentation for AacProfile
    """
    HEV1 = "HEV1"
    HEV2 = "HEV2"
    LC = "LC"


class AacRateControlMode(Enum):
    """
    Placeholder documentation for AacRateControlMode
    """
    CBR = "CBR"
    VBR = "VBR"


class AacRawFormat(Enum):
    """
    Placeholder documentation for AacRawFormat
    """
    LATM_LOAS = "LATM_LOAS"
    NONE = "NONE"


@dataclasses.dataclass
class AacSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for AacSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bitrate",
                "Bitrate",
                autoboto.TypeInfo(float),
            ),
            (
                "coding_mode",
                "CodingMode",
                autoboto.TypeInfo(AacCodingMode),
            ),
            (
                "input_type",
                "InputType",
                autoboto.TypeInfo(AacInputType),
            ),
            (
                "profile",
                "Profile",
                autoboto.TypeInfo(AacProfile),
            ),
            (
                "rate_control_mode",
                "RateControlMode",
                autoboto.TypeInfo(AacRateControlMode),
            ),
            (
                "raw_format",
                "RawFormat",
                autoboto.TypeInfo(AacRawFormat),
            ),
            (
                "sample_rate",
                "SampleRate",
                autoboto.TypeInfo(float),
            ),
            (
                "spec",
                "Spec",
                autoboto.TypeInfo(AacSpec),
            ),
            (
                "vbr_quality",
                "VbrQuality",
                autoboto.TypeInfo(AacVbrQuality),
            ),
        ]

    # Average bitrate in bits/second. Valid values depend on rate control mode
    # and profile.
    bitrate: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Mono, Stereo, or 5.1 channel layout. Valid values depend on rate control
    # mode and profile. The adReceiverMix setting receives a stereo description
    # plus control track and emits a mono AAC encode of the description track,
    # with control data emitted in the PES header as per ETSI TS 101 154 Annex E.
    coding_mode: "AacCodingMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Set to "broadcasterMixedAd" when input contains pre-mixed main audio + AD
    # (narration) as a stereo pair. The Audio Type field (audioType) will be set
    # to 3, which signals to downstream systems that this stream contains
    # "broadcaster mixed AD". Note that the input received by the encoder must
    # contain pre-mixed audio; the encoder does not perform the mixing. The
    # values in audioTypeControl and audioType (in AudioDescription) are ignored
    # when set to broadcasterMixedAd. Leave set to "normal" when input does not
    # contain pre-mixed audio + AD.
    input_type: "AacInputType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # AAC Profile.
    profile: "AacProfile" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Rate Control Mode.
    rate_control_mode: "AacRateControlMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Sets LATM / LOAS AAC output for raw containers.
    raw_format: "AacRawFormat" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Sample rate in Hz. Valid values depend on rate control mode and profile.
    sample_rate: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Use MPEG-2 AAC audio instead of MPEG-4 AAC audio for raw or MPEG-2
    # Transport Stream containers.
    spec: "AacSpec" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # VBR Quality Level - Only used if rateControlMode is VBR.
    vbr_quality: "AacVbrQuality" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class AacSpec(Enum):
    """
    Placeholder documentation for AacSpec
    """
    MPEG2 = "MPEG2"
    MPEG4 = "MPEG4"


class AacVbrQuality(Enum):
    """
    Placeholder documentation for AacVbrQuality
    """
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM_HIGH = "MEDIUM_HIGH"
    MEDIUM_LOW = "MEDIUM_LOW"


class Ac3BitstreamMode(Enum):
    """
    Placeholder documentation for Ac3BitstreamMode
    """
    COMMENTARY = "COMMENTARY"
    COMPLETE_MAIN = "COMPLETE_MAIN"
    DIALOGUE = "DIALOGUE"
    EMERGENCY = "EMERGENCY"
    HEARING_IMPAIRED = "HEARING_IMPAIRED"
    MUSIC_AND_EFFECTS = "MUSIC_AND_EFFECTS"
    VISUALLY_IMPAIRED = "VISUALLY_IMPAIRED"
    VOICE_OVER = "VOICE_OVER"


class Ac3CodingMode(Enum):
    """
    Placeholder documentation for Ac3CodingMode
    """
    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_1_1 = "CODING_MODE_1_1"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_3_2_LFE = "CODING_MODE_3_2_LFE"


class Ac3DrcProfile(Enum):
    """
    Placeholder documentation for Ac3DrcProfile
    """
    FILM_STANDARD = "FILM_STANDARD"
    NONE = "NONE"


class Ac3LfeFilter(Enum):
    """
    Placeholder documentation for Ac3LfeFilter
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Ac3MetadataControl(Enum):
    """
    Placeholder documentation for Ac3MetadataControl
    """
    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


@dataclasses.dataclass
class Ac3Settings(autoboto.ShapeBase):
    """
    Placeholder documentation for Ac3Settings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bitrate",
                "Bitrate",
                autoboto.TypeInfo(float),
            ),
            (
                "bitstream_mode",
                "BitstreamMode",
                autoboto.TypeInfo(Ac3BitstreamMode),
            ),
            (
                "coding_mode",
                "CodingMode",
                autoboto.TypeInfo(Ac3CodingMode),
            ),
            (
                "dialnorm",
                "Dialnorm",
                autoboto.TypeInfo(int),
            ),
            (
                "drc_profile",
                "DrcProfile",
                autoboto.TypeInfo(Ac3DrcProfile),
            ),
            (
                "lfe_filter",
                "LfeFilter",
                autoboto.TypeInfo(Ac3LfeFilter),
            ),
            (
                "metadata_control",
                "MetadataControl",
                autoboto.TypeInfo(Ac3MetadataControl),
            ),
        ]

    # Average bitrate in bits/second. Valid bitrates depend on the coding mode.
    bitrate: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the bitstream mode (bsmod) for the emitted AC-3 stream. See ATSC
    # A/52-2012 for background on these values.
    bitstream_mode: "Ac3BitstreamMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Dolby Digital coding mode. Determines number of channels.
    coding_mode: "Ac3CodingMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Sets the dialnorm for the output. If excluded and input audio is Dolby
    # Digital, dialnorm will be passed through.
    dialnorm: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If set to filmStandard, adds dynamic range compression signaling to the
    # output bitstream as defined in the Dolby Digital specification.
    drc_profile: "Ac3DrcProfile" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to enabled, applies a 120Hz lowpass filter to the LFE channel
    # prior to encoding. Only valid in codingMode32Lfe mode.
    lfe_filter: "Ac3LfeFilter" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to "followInput", encoder metadata will be sourced from the DD,
    # DD+, or DolbyE decoder that supplied this audio data. If audio was not
    # supplied from one of these streams, then the static metadata settings will
    # be used.
    metadata_control: "Ac3MetadataControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AccessDenied(autoboto.ShapeBase):
    """
    Placeholder documentation for AccessDenied
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

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class AfdSignaling(Enum):
    """
    Placeholder documentation for AfdSignaling
    """
    AUTO = "AUTO"
    FIXED = "FIXED"
    NONE = "NONE"


@dataclasses.dataclass
class ArchiveContainerSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for ArchiveContainerSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "m2ts_settings",
                "M2tsSettings",
                autoboto.TypeInfo(M2tsSettings),
            ),
        ]

    # Placeholder documentation for M2tsSettings
    m2ts_settings: "M2tsSettings" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ArchiveGroupSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for ArchiveGroupSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination",
                "Destination",
                autoboto.TypeInfo(OutputLocationRef),
            ),
            (
                "rollover_interval",
                "RolloverInterval",
                autoboto.TypeInfo(int),
            ),
        ]

    # A directory and base filename where archive files should be written. If the
    # base filename portion of the URI is left blank, the base filename of the
    # first input will be automatically inserted.
    destination: "OutputLocationRef" = dataclasses.field(default_factory=dict, )

    # Number of seconds to write to archive file before closing and starting a
    # new one.
    rollover_interval: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ArchiveOutputSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for ArchiveOutputSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_settings",
                "ContainerSettings",
                autoboto.TypeInfo(ArchiveContainerSettings),
            ),
            (
                "extension",
                "Extension",
                autoboto.TypeInfo(str),
            ),
            (
                "name_modifier",
                "NameModifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # Settings specific to the container type of the file.
    container_settings: "ArchiveContainerSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Output file extension. If excluded, this will be auto-selected from the
    # container type.
    extension: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # String concatenated to the end of the destination filename. Required for
    # multiple outputs of the same type.
    name_modifier: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AribDestinationSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for AribDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AribSourceSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for AribSourceSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AudioChannelMapping(autoboto.ShapeBase):
    """
    Placeholder documentation for AudioChannelMapping
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_channel_levels",
                "InputChannelLevels",
                autoboto.TypeInfo(typing.List[InputChannelLevel]),
            ),
            (
                "output_channel",
                "OutputChannel",
                autoboto.TypeInfo(int),
            ),
        ]

    # Indices and gain values for each input channel that should be remixed into
    # this output channel.
    input_channel_levels: typing.List["InputChannelLevel"] = dataclasses.field(
        default_factory=list,
    )

    # The index of the output channel being produced.
    output_channel: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AudioCodecSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for AudioCodecSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "aac_settings",
                "AacSettings",
                autoboto.TypeInfo(AacSettings),
            ),
            (
                "ac3_settings",
                "Ac3Settings",
                autoboto.TypeInfo(Ac3Settings),
            ),
            (
                "eac3_settings",
                "Eac3Settings",
                autoboto.TypeInfo(Eac3Settings),
            ),
            (
                "mp2_settings",
                "Mp2Settings",
                autoboto.TypeInfo(Mp2Settings),
            ),
            (
                "pass_through_settings",
                "PassThroughSettings",
                autoboto.TypeInfo(PassThroughSettings),
            ),
        ]

    # Placeholder documentation for AacSettings
    aac_settings: "AacSettings" = dataclasses.field(default_factory=dict, )

    # Placeholder documentation for Ac3Settings
    ac3_settings: "Ac3Settings" = dataclasses.field(default_factory=dict, )

    # Placeholder documentation for Eac3Settings
    eac3_settings: "Eac3Settings" = dataclasses.field(default_factory=dict, )

    # Placeholder documentation for Mp2Settings
    mp2_settings: "Mp2Settings" = dataclasses.field(default_factory=dict, )

    # Placeholder documentation for PassThroughSettings
    pass_through_settings: "PassThroughSettings" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class AudioDescription(autoboto.ShapeBase):
    """
    Placeholder documentation for AudioDescription
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_selector_name",
                "AudioSelectorName",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "audio_normalization_settings",
                "AudioNormalizationSettings",
                autoboto.TypeInfo(AudioNormalizationSettings),
            ),
            (
                "audio_type",
                "AudioType",
                autoboto.TypeInfo(AudioType),
            ),
            (
                "audio_type_control",
                "AudioTypeControl",
                autoboto.TypeInfo(AudioDescriptionAudioTypeControl),
            ),
            (
                "codec_settings",
                "CodecSettings",
                autoboto.TypeInfo(AudioCodecSettings),
            ),
            (
                "language_code",
                "LanguageCode",
                autoboto.TypeInfo(str),
            ),
            (
                "language_code_control",
                "LanguageCodeControl",
                autoboto.TypeInfo(AudioDescriptionLanguageCodeControl),
            ),
            (
                "remix_settings",
                "RemixSettings",
                autoboto.TypeInfo(RemixSettings),
            ),
            (
                "stream_name",
                "StreamName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the AudioSelector used as the source for this AudioDescription.
    audio_selector_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of this AudioDescription. Outputs will use this name to uniquely
    # identify this AudioDescription. Description names should be unique within
    # this Live Event.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Advanced audio normalization settings.
    audio_normalization_settings: "AudioNormalizationSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Applies only if audioTypeControl is useConfigured. The values for audioType
    # are defined in ISO-IEC 13818-1.
    audio_type: "AudioType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Determines how audio type is determined. followInput: If the input contains
    # an ISO 639 audioType, then that value is passed through to the output. If
    # the input contains no ISO 639 audioType, the value in Audio Type is
    # included in the output. useConfigured: The value in Audio Type is included
    # in the output. Note that this field and audioType are both ignored if
    # inputType is broadcasterMixedAd.
    audio_type_control: "AudioDescriptionAudioTypeControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Audio codec settings.
    codec_settings: "AudioCodecSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Indicates the language of the audio output track. Only used if
    # languageControlMode is useConfigured, or there is no ISO 639 language code
    # specified in the input.
    language_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Choosing followInput will cause the ISO 639 language code of the output to
    # follow the ISO 639 language code of the input. The languageCode will be
    # used when useConfigured is set, or when followInput is selected but there
    # is no ISO 639 language code specified by the input.
    language_code_control: "AudioDescriptionLanguageCodeControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Settings that control how input audio channels are remixed into the output
    # audio channels.
    remix_settings: "RemixSettings" = dataclasses.field(default_factory=dict, )

    # Used for MS Smooth and Apple HLS outputs. Indicates the name displayed by
    # the player (eg. English, or Director Commentary).
    stream_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class AudioDescriptionAudioTypeControl(Enum):
    """
    Placeholder documentation for AudioDescriptionAudioTypeControl
    """
    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class AudioDescriptionLanguageCodeControl(Enum):
    """
    Placeholder documentation for AudioDescriptionLanguageCodeControl
    """
    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


@dataclasses.dataclass
class AudioLanguageSelection(autoboto.ShapeBase):
    """
    Placeholder documentation for AudioLanguageSelection
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "language_code",
                "LanguageCode",
                autoboto.TypeInfo(str),
            ),
            (
                "language_selection_policy",
                "LanguageSelectionPolicy",
                autoboto.TypeInfo(AudioLanguageSelectionPolicy),
            ),
        ]

    # Selects a specific three-letter language code from within an audio source.
    language_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When set to "strict", the transport stream demux strictly identifies audio
    # streams by their language descriptor. If a PMT update occurs such that an
    # audio stream matching the initially selected language is no longer present
    # then mute will be encoded until the language returns. If "loose", then on a
    # PMT update the demux will choose another audio stream in the program with
    # the same stream type if it can't find one with the same language.
    language_selection_policy: "AudioLanguageSelectionPolicy" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class AudioLanguageSelectionPolicy(Enum):
    """
    Placeholder documentation for AudioLanguageSelectionPolicy
    """
    LOOSE = "LOOSE"
    STRICT = "STRICT"


class AudioNormalizationAlgorithm(Enum):
    """
    Placeholder documentation for AudioNormalizationAlgorithm
    """
    ITU_1770_1 = "ITU_1770_1"
    ITU_1770_2 = "ITU_1770_2"


class AudioNormalizationAlgorithmControl(Enum):
    """
    Placeholder documentation for AudioNormalizationAlgorithmControl
    """
    CORRECT_AUDIO = "CORRECT_AUDIO"


@dataclasses.dataclass
class AudioNormalizationSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for AudioNormalizationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "algorithm",
                "Algorithm",
                autoboto.TypeInfo(AudioNormalizationAlgorithm),
            ),
            (
                "algorithm_control",
                "AlgorithmControl",
                autoboto.TypeInfo(AudioNormalizationAlgorithmControl),
            ),
            (
                "target_lkfs",
                "TargetLkfs",
                autoboto.TypeInfo(float),
            ),
        ]

    # Audio normalization algorithm to use. itu17701 conforms to the CALM Act
    # specification, itu17702 conforms to the EBU R-128 specification.
    algorithm: "AudioNormalizationAlgorithm" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to correctAudio the output audio is corrected using the chosen
    # algorithm. If set to measureOnly, the audio will be measured but not
    # adjusted.
    algorithm_control: "AudioNormalizationAlgorithmControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Target LKFS(loudness) to adjust volume to. If no value is entered, a
    # default value will be used according to the chosen algorithm. The CALM Act
    # (1770-1) recommends a target of -24 LKFS. The EBU R-128 specification
    # (1770-2) recommends a target of -23 LKFS.
    target_lkfs: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AudioOnlyHlsSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for AudioOnlyHlsSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_group_id",
                "AudioGroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "audio_only_image",
                "AudioOnlyImage",
                autoboto.TypeInfo(InputLocation),
            ),
            (
                "audio_track_type",
                "AudioTrackType",
                autoboto.TypeInfo(AudioOnlyHlsTrackType),
            ),
        ]

    # Specifies the group to which the audio Rendition belongs.
    audio_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # For use with an audio only Stream. Must be a .jpg or .png file. If given,
    # this image will be used as the cover-art for the audio only output.
    # Ideally, it should be formatted for an iPhone screen for two reasons. The
    # iPhone does not resize the image, it crops a centered image on the
    # top/bottom and left/right. Additionally, this image file gets saved bit-
    # for-bit into every 10-second segment file, so will increase bandwidth by
    # {image file size} * {segment count} * {user count.}.
    audio_only_image: "InputLocation" = dataclasses.field(
        default_factory=dict,
    )

    # Four types of audio-only tracks are supported: Audio-Only Variant Stream
    # The client can play back this audio-only stream instead of video in low-
    # bandwidth scenarios. Represented as an EXT-X-STREAM-INF in the HLS
    # manifest. Alternate Audio, Auto Select, Default Alternate rendition that
    # the client should try to play back by default. Represented as an EXT-X-
    # MEDIA in the HLS manifest with DEFAULT=YES, AUTOSELECT=YES Alternate Audio,
    # Auto Select, Not Default Alternate rendition that the client may try to
    # play back by default. Represented as an EXT-X-MEDIA in the HLS manifest
    # with DEFAULT=NO, AUTOSELECT=YES Alternate Audio, not Auto Select Alternate
    # rendition that the client will not try to play back by default. Represented
    # as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=NO
    audio_track_type: "AudioOnlyHlsTrackType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class AudioOnlyHlsTrackType(Enum):
    """
    Placeholder documentation for AudioOnlyHlsTrackType
    """
    ALTERNATE_AUDIO_AUTO_SELECT = "ALTERNATE_AUDIO_AUTO_SELECT"
    ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT = "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT"
    ALTERNATE_AUDIO_NOT_AUTO_SELECT = "ALTERNATE_AUDIO_NOT_AUTO_SELECT"
    AUDIO_ONLY_VARIANT_STREAM = "AUDIO_ONLY_VARIANT_STREAM"


@dataclasses.dataclass
class AudioPidSelection(autoboto.ShapeBase):
    """
    Placeholder documentation for AudioPidSelection
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pid",
                "Pid",
                autoboto.TypeInfo(int),
            ),
        ]

    # Selects a specific PID from within a source.
    pid: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AudioSelector(autoboto.ShapeBase):
    """
    Placeholder documentation for AudioSelector
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "selector_settings",
                "SelectorSettings",
                autoboto.TypeInfo(AudioSelectorSettings),
            ),
        ]

    # The name of this AudioSelector. AudioDescriptions will use this name to
    # uniquely identify this Selector. Selector names should be unique per input.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The audio selector settings.
    selector_settings: "AudioSelectorSettings" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class AudioSelectorSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for AudioSelectorSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_language_selection",
                "AudioLanguageSelection",
                autoboto.TypeInfo(AudioLanguageSelection),
            ),
            (
                "audio_pid_selection",
                "AudioPidSelection",
                autoboto.TypeInfo(AudioPidSelection),
            ),
        ]

    # Placeholder documentation for AudioLanguageSelection
    audio_language_selection: "AudioLanguageSelection" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for AudioPidSelection
    audio_pid_selection: "AudioPidSelection" = dataclasses.field(
        default_factory=dict,
    )


class AudioType(Enum):
    """
    Placeholder documentation for AudioType
    """
    CLEAN_EFFECTS = "CLEAN_EFFECTS"
    HEARING_IMPAIRED = "HEARING_IMPAIRED"
    UNDEFINED = "UNDEFINED"
    VISUAL_IMPAIRED_COMMENTARY = "VISUAL_IMPAIRED_COMMENTARY"


class AuthenticationScheme(Enum):
    """
    Placeholder documentation for AuthenticationScheme
    """
    AKAMAI = "AKAMAI"
    COMMON = "COMMON"


@dataclasses.dataclass
class AvailBlanking(autoboto.ShapeBase):
    """
    Placeholder documentation for AvailBlanking
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "avail_blanking_image",
                "AvailBlankingImage",
                autoboto.TypeInfo(InputLocation),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(AvailBlankingState),
            ),
        ]

    # Blanking image to be used. Leave empty for solid black. Only bmp and png
    # images are supported.
    avail_blanking_image: "InputLocation" = dataclasses.field(
        default_factory=dict,
    )

    # When set to enabled, causes video, audio and captions to be blanked when
    # insertion metadata is added.
    state: "AvailBlankingState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class AvailBlankingState(Enum):
    """
    Placeholder documentation for AvailBlankingState
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


@dataclasses.dataclass
class AvailConfiguration(autoboto.ShapeBase):
    """
    Placeholder documentation for AvailConfiguration
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "avail_settings",
                "AvailSettings",
                autoboto.TypeInfo(AvailSettings),
            ),
        ]

    # Ad avail settings.
    avail_settings: "AvailSettings" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class AvailSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for AvailSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scte35_splice_insert",
                "Scte35SpliceInsert",
                autoboto.TypeInfo(Scte35SpliceInsert),
            ),
            (
                "scte35_time_signal_apos",
                "Scte35TimeSignalApos",
                autoboto.TypeInfo(Scte35TimeSignalApos),
            ),
        ]

    # Placeholder documentation for Scte35SpliceInsert
    scte35_splice_insert: "Scte35SpliceInsert" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for Scte35TimeSignalApos
    scte35_time_signal_apos: "Scte35TimeSignalApos" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class BadGatewayException(autoboto.ShapeBase):
    """
    Placeholder documentation for BadGatewayException
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

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BadRequestException(autoboto.ShapeBase):
    """
    Placeholder documentation for BadRequestException
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

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchScheduleActionCreateRequest(autoboto.ShapeBase):
    """
    A list of schedule actions to create.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schedule_actions",
                "ScheduleActions",
                autoboto.TypeInfo(typing.List[ScheduleAction]),
            ),
        ]

    # A list of schedule actions to create.
    schedule_actions: typing.List["ScheduleAction"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchScheduleActionCreateResult(autoboto.ShapeBase):
    """
    Returned list of created schedule actions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schedule_actions",
                "ScheduleActions",
                autoboto.TypeInfo(typing.List[ScheduleAction]),
            ),
        ]

    # Returned list of created schedule actions.
    schedule_actions: typing.List["ScheduleAction"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchScheduleActionDeleteRequest(autoboto.ShapeBase):
    """
    A list of schedule actions to delete.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_names",
                "ActionNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A list of schedule actions to delete, identified by unique name.
    action_names: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class BatchScheduleActionDeleteResult(autoboto.ShapeBase):
    """
    Returned list of deleted schedule actions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schedule_actions",
                "ScheduleActions",
                autoboto.TypeInfo(typing.List[ScheduleAction]),
            ),
        ]

    # Returned list of deleted schedule actions.
    schedule_actions: typing.List["ScheduleAction"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchUpdateScheduleRequest(autoboto.ShapeBase):
    """
    List of actions to create and list of actions to delete.
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
                "creates",
                "Creates",
                autoboto.TypeInfo(BatchScheduleActionCreateRequest),
            ),
            (
                "deletes",
                "Deletes",
                autoboto.TypeInfo(BatchScheduleActionDeleteRequest),
            ),
        ]

    # Id of the channel whose schedule is being updated.
    channel_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Schedule actions to create in the schedule.
    creates: "BatchScheduleActionCreateRequest" = dataclasses.field(
        default_factory=dict,
    )

    # Schedule actions to delete from the schedule.
    deletes: "BatchScheduleActionDeleteRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class BatchUpdateScheduleResponse(autoboto.OutputShapeBase):
    """
    Response to a batch update schedule call.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "creates",
                "Creates",
                autoboto.TypeInfo(BatchScheduleActionCreateResult),
            ),
            (
                "deletes",
                "Deletes",
                autoboto.TypeInfo(BatchScheduleActionDeleteResult),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Schedule actions created in the schedule.
    creates: "BatchScheduleActionCreateResult" = dataclasses.field(
        default_factory=dict,
    )

    # Schedule actions deleted from the schedule.
    deletes: "BatchScheduleActionDeleteResult" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class BatchUpdateScheduleResult(autoboto.ShapeBase):
    """
    Results of a batch schedule update.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "creates",
                "Creates",
                autoboto.TypeInfo(BatchScheduleActionCreateResult),
            ),
            (
                "deletes",
                "Deletes",
                autoboto.TypeInfo(BatchScheduleActionDeleteResult),
            ),
        ]

    # Schedule actions created in the schedule.
    creates: "BatchScheduleActionCreateResult" = dataclasses.field(
        default_factory=dict,
    )

    # Schedule actions deleted from the schedule.
    deletes: "BatchScheduleActionDeleteResult" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class BlackoutSlate(autoboto.ShapeBase):
    """
    Placeholder documentation for BlackoutSlate
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "blackout_slate_image",
                "BlackoutSlateImage",
                autoboto.TypeInfo(InputLocation),
            ),
            (
                "network_end_blackout",
                "NetworkEndBlackout",
                autoboto.TypeInfo(BlackoutSlateNetworkEndBlackout),
            ),
            (
                "network_end_blackout_image",
                "NetworkEndBlackoutImage",
                autoboto.TypeInfo(InputLocation),
            ),
            (
                "network_id",
                "NetworkId",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(BlackoutSlateState),
            ),
        ]

    # Blackout slate image to be used. Leave empty for solid black. Only bmp and
    # png images are supported.
    blackout_slate_image: "InputLocation" = dataclasses.field(
        default_factory=dict,
    )

    # Setting to enabled causes the encoder to blackout the video, audio, and
    # captions, and raise the "Network Blackout Image" slate when an SCTE104/35
    # Network End Segmentation Descriptor is encountered. The blackout will be
    # lifted when the Network Start Segmentation Descriptor is encountered. The
    # Network End and Network Start descriptors must contain a network ID that
    # matches the value entered in "Network ID".
    network_end_blackout: "BlackoutSlateNetworkEndBlackout" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Path to local file to use as Network End Blackout image. Image will be
    # scaled to fill the entire output raster.
    network_end_blackout_image: "InputLocation" = dataclasses.field(
        default_factory=dict,
    )

    # Provides Network ID that matches EIDR ID format (e.g., "10.XXXX/XXXX-XXXX-
    # XXXX-XXXX-XXXX-C").
    network_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When set to enabled, causes video, audio and captions to be blanked when
    # indicated by program metadata.
    state: "BlackoutSlateState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class BlackoutSlateNetworkEndBlackout(Enum):
    """
    Placeholder documentation for BlackoutSlateNetworkEndBlackout
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class BlackoutSlateState(Enum):
    """
    Placeholder documentation for BlackoutSlateState
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class BurnInAlignment(Enum):
    """
    Placeholder documentation for BurnInAlignment
    """
    CENTERED = "CENTERED"
    LEFT = "LEFT"
    SMART = "SMART"


class BurnInBackgroundColor(Enum):
    """
    Placeholder documentation for BurnInBackgroundColor
    """
    BLACK = "BLACK"
    NONE = "NONE"
    WHITE = "WHITE"


@dataclasses.dataclass
class BurnInDestinationSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for BurnInDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alignment",
                "Alignment",
                autoboto.TypeInfo(BurnInAlignment),
            ),
            (
                "background_color",
                "BackgroundColor",
                autoboto.TypeInfo(BurnInBackgroundColor),
            ),
            (
                "background_opacity",
                "BackgroundOpacity",
                autoboto.TypeInfo(int),
            ),
            (
                "font",
                "Font",
                autoboto.TypeInfo(InputLocation),
            ),
            (
                "font_color",
                "FontColor",
                autoboto.TypeInfo(BurnInFontColor),
            ),
            (
                "font_opacity",
                "FontOpacity",
                autoboto.TypeInfo(int),
            ),
            (
                "font_resolution",
                "FontResolution",
                autoboto.TypeInfo(int),
            ),
            (
                "font_size",
                "FontSize",
                autoboto.TypeInfo(str),
            ),
            (
                "outline_color",
                "OutlineColor",
                autoboto.TypeInfo(BurnInOutlineColor),
            ),
            (
                "outline_size",
                "OutlineSize",
                autoboto.TypeInfo(int),
            ),
            (
                "shadow_color",
                "ShadowColor",
                autoboto.TypeInfo(BurnInShadowColor),
            ),
            (
                "shadow_opacity",
                "ShadowOpacity",
                autoboto.TypeInfo(int),
            ),
            (
                "shadow_x_offset",
                "ShadowXOffset",
                autoboto.TypeInfo(int),
            ),
            (
                "shadow_y_offset",
                "ShadowYOffset",
                autoboto.TypeInfo(int),
            ),
            (
                "teletext_grid_control",
                "TeletextGridControl",
                autoboto.TypeInfo(BurnInTeletextGridControl),
            ),
            (
                "x_position",
                "XPosition",
                autoboto.TypeInfo(int),
            ),
            (
                "y_position",
                "YPosition",
                autoboto.TypeInfo(int),
            ),
        ]

    # If no explicit xPosition or yPosition is provided, setting alignment to
    # centered will place the captions at the bottom center of the output.
    # Similarly, setting a left alignment will align captions to the bottom left
    # of the output. If x and y positions are given in conjunction with the
    # alignment parameter, the font will be justified (either left or centered)
    # relative to those coordinates. Selecting "smart" justification will left-
    # justify live subtitles and center-justify pre-recorded subtitles. All burn-
    # in and DVB-Sub font settings must match.
    alignment: "BurnInAlignment" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the color of the rectangle behind the captions. All burn-in and
    # DVB-Sub font settings must match.
    background_color: "BurnInBackgroundColor" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the opacity of the background rectangle. 255 is opaque; 0 is
    # transparent. Leaving this parameter out is equivalent to setting it to 0
    # (transparent). All burn-in and DVB-Sub font settings must match.
    background_opacity: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # External font file used for caption burn-in. File extension must be 'ttf'
    # or 'tte'. Although the user can select output fonts for many different
    # types of input captions, embedded, STL and teletext sources use a strict
    # grid system. Using external fonts with these caption sources could cause
    # unexpected display of proportional fonts. All burn-in and DVB-Sub font
    # settings must match.
    font: "InputLocation" = dataclasses.field(default_factory=dict, )

    # Specifies the color of the burned-in captions. This option is not valid for
    # source captions that are STL, 608/embedded or teletext. These source
    # settings are already pre-defined by the caption stream. All burn-in and
    # DVB-Sub font settings must match.
    font_color: "BurnInFontColor" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the opacity of the burned-in captions. 255 is opaque; 0 is
    # transparent. All burn-in and DVB-Sub font settings must match.
    font_opacity: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and
    # DVB-Sub font settings must match.
    font_resolution: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to 'auto' fontSize will scale depending on the size of the output.
    # Giving a positive integer will specify the exact font size in points. All
    # burn-in and DVB-Sub font settings must match.
    font_size: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies font outline color. This option is not valid for source captions
    # that are either 608/embedded or teletext. These source settings are already
    # pre-defined by the caption stream. All burn-in and DVB-Sub font settings
    # must match.
    outline_color: "BurnInOutlineColor" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies font outline size in pixels. This option is not valid for source
    # captions that are either 608/embedded or teletext. These source settings
    # are already pre-defined by the caption stream. All burn-in and DVB-Sub font
    # settings must match.
    outline_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the color of the shadow cast by the captions. All burn-in and
    # DVB-Sub font settings must match.
    shadow_color: "BurnInShadowColor" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the opacity of the shadow. 255 is opaque; 0 is transparent.
    # Leaving this parameter out is equivalent to setting it to 0 (transparent).
    # All burn-in and DVB-Sub font settings must match.
    shadow_opacity: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the horizontal offset of the shadow relative to the captions in
    # pixels. A value of -2 would result in a shadow offset 2 pixels to the left.
    # All burn-in and DVB-Sub font settings must match.
    shadow_x_offset: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the vertical offset of the shadow relative to the captions in
    # pixels. A value of -2 would result in a shadow offset 2 pixels above the
    # text. All burn-in and DVB-Sub font settings must match.
    shadow_y_offset: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Controls whether a fixed grid size will be used to generate the output
    # subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in
    # outputs.
    teletext_grid_control: "BurnInTeletextGridControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the horizontal position of the caption relative to the left side
    # of the output in pixels. A value of 10 would result in the captions
    # starting 10 pixels from the left of the output. If no explicit xPosition is
    # provided, the horizontal caption position will be determined by the
    # alignment parameter. All burn-in and DVB-Sub font settings must match.
    x_position: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the vertical position of the caption relative to the top of the
    # output in pixels. A value of 10 would result in the captions starting 10
    # pixels from the top of the output. If no explicit yPosition is provided,
    # the caption will be positioned towards the bottom of the output. All burn-
    # in and DVB-Sub font settings must match.
    y_position: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class BurnInFontColor(Enum):
    """
    Placeholder documentation for BurnInFontColor
    """
    BLACK = "BLACK"
    BLUE = "BLUE"
    GREEN = "GREEN"
    RED = "RED"
    WHITE = "WHITE"
    YELLOW = "YELLOW"


class BurnInOutlineColor(Enum):
    """
    Placeholder documentation for BurnInOutlineColor
    """
    BLACK = "BLACK"
    BLUE = "BLUE"
    GREEN = "GREEN"
    RED = "RED"
    WHITE = "WHITE"
    YELLOW = "YELLOW"


class BurnInShadowColor(Enum):
    """
    Placeholder documentation for BurnInShadowColor
    """
    BLACK = "BLACK"
    NONE = "NONE"
    WHITE = "WHITE"


class BurnInTeletextGridControl(Enum):
    """
    Placeholder documentation for BurnInTeletextGridControl
    """
    FIXED = "FIXED"
    SCALED = "SCALED"


@dataclasses.dataclass
class CaptionDescription(autoboto.ShapeBase):
    """
    Output groups for this Live Event. Output groups contain information about where
    streams should be distributed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "caption_selector_name",
                "CaptionSelectorName",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "destination_settings",
                "DestinationSettings",
                autoboto.TypeInfo(CaptionDestinationSettings),
            ),
            (
                "language_code",
                "LanguageCode",
                autoboto.TypeInfo(str),
            ),
            (
                "language_description",
                "LanguageDescription",
                autoboto.TypeInfo(str),
            ),
        ]

    # Specifies which input caption selector to use as a caption source when
    # generating output captions. This field should match a captionSelector name.
    caption_selector_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Name of the caption description. Used to associate a caption description
    # with an output. Names must be unique within an event.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Additional settings for captions destination that depend on the destination
    # type.
    destination_settings: "CaptionDestinationSettings" = dataclasses.field(
        default_factory=dict,
    )

    # ISO 639-2 three-digit code: http://www.loc.gov/standards/iso639-2/
    language_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Human readable information to indicate captions available for players (eg.
    # English, or Spanish).
    language_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CaptionDestinationSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for CaptionDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arib_destination_settings",
                "AribDestinationSettings",
                autoboto.TypeInfo(AribDestinationSettings),
            ),
            (
                "burn_in_destination_settings",
                "BurnInDestinationSettings",
                autoboto.TypeInfo(BurnInDestinationSettings),
            ),
            (
                "dvb_sub_destination_settings",
                "DvbSubDestinationSettings",
                autoboto.TypeInfo(DvbSubDestinationSettings),
            ),
            (
                "embedded_destination_settings",
                "EmbeddedDestinationSettings",
                autoboto.TypeInfo(EmbeddedDestinationSettings),
            ),
            (
                "embedded_plus_scte20_destination_settings",
                "EmbeddedPlusScte20DestinationSettings",
                autoboto.TypeInfo(EmbeddedPlusScte20DestinationSettings),
            ),
            (
                "rtmp_caption_info_destination_settings",
                "RtmpCaptionInfoDestinationSettings",
                autoboto.TypeInfo(RtmpCaptionInfoDestinationSettings),
            ),
            (
                "scte20_plus_embedded_destination_settings",
                "Scte20PlusEmbeddedDestinationSettings",
                autoboto.TypeInfo(Scte20PlusEmbeddedDestinationSettings),
            ),
            (
                "scte27_destination_settings",
                "Scte27DestinationSettings",
                autoboto.TypeInfo(Scte27DestinationSettings),
            ),
            (
                "smpte_tt_destination_settings",
                "SmpteTtDestinationSettings",
                autoboto.TypeInfo(SmpteTtDestinationSettings),
            ),
            (
                "teletext_destination_settings",
                "TeletextDestinationSettings",
                autoboto.TypeInfo(TeletextDestinationSettings),
            ),
            (
                "ttml_destination_settings",
                "TtmlDestinationSettings",
                autoboto.TypeInfo(TtmlDestinationSettings),
            ),
            (
                "webvtt_destination_settings",
                "WebvttDestinationSettings",
                autoboto.TypeInfo(WebvttDestinationSettings),
            ),
        ]

    # Placeholder documentation for AribDestinationSettings
    arib_destination_settings: "AribDestinationSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for BurnInDestinationSettings
    burn_in_destination_settings: "BurnInDestinationSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for DvbSubDestinationSettings
    dvb_sub_destination_settings: "DvbSubDestinationSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for EmbeddedDestinationSettings
    embedded_destination_settings: "EmbeddedDestinationSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for EmbeddedPlusScte20DestinationSettings
    embedded_plus_scte20_destination_settings: "EmbeddedPlusScte20DestinationSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for RtmpCaptionInfoDestinationSettings
    rtmp_caption_info_destination_settings: "RtmpCaptionInfoDestinationSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for Scte20PlusEmbeddedDestinationSettings
    scte20_plus_embedded_destination_settings: "Scte20PlusEmbeddedDestinationSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for Scte27DestinationSettings
    scte27_destination_settings: "Scte27DestinationSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for SmpteTtDestinationSettings
    smpte_tt_destination_settings: "SmpteTtDestinationSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for TeletextDestinationSettings
    teletext_destination_settings: "TeletextDestinationSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for TtmlDestinationSettings
    ttml_destination_settings: "TtmlDestinationSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for WebvttDestinationSettings
    webvtt_destination_settings: "WebvttDestinationSettings" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CaptionLanguageMapping(autoboto.ShapeBase):
    """
    Maps a caption channel to an ISO 693-2 language code
    (http://www.loc.gov/standards/iso639-2), with an optional description.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "caption_channel",
                "CaptionChannel",
                autoboto.TypeInfo(int),
            ),
            (
                "language_code",
                "LanguageCode",
                autoboto.TypeInfo(str),
            ),
            (
                "language_description",
                "LanguageDescription",
                autoboto.TypeInfo(str),
            ),
        ]

    # The closed caption channel being described by this CaptionLanguageMapping.
    # Each channel mapping must have a unique channel number (maximum of 4)
    caption_channel: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Three character ISO 639-2 language code (see
    # http://www.loc.gov/standards/iso639-2)
    language_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Textual description of language
    language_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CaptionSelector(autoboto.ShapeBase):
    """
    Output groups for this Live Event. Output groups contain information about where
    streams should be distributed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                autoboto.TypeInfo(str),
            ),
            (
                "selector_settings",
                "SelectorSettings",
                autoboto.TypeInfo(CaptionSelectorSettings),
            ),
        ]

    # Name identifier for a caption selector. This name is used to associate this
    # caption selector with one or more caption descriptions. Names must be
    # unique within an event.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When specified this field indicates the three letter language code of the
    # caption track to extract from the source.
    language_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Caption selector settings.
    selector_settings: "CaptionSelectorSettings" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CaptionSelectorSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for CaptionSelectorSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arib_source_settings",
                "AribSourceSettings",
                autoboto.TypeInfo(AribSourceSettings),
            ),
            (
                "dvb_sub_source_settings",
                "DvbSubSourceSettings",
                autoboto.TypeInfo(DvbSubSourceSettings),
            ),
            (
                "embedded_source_settings",
                "EmbeddedSourceSettings",
                autoboto.TypeInfo(EmbeddedSourceSettings),
            ),
            (
                "scte20_source_settings",
                "Scte20SourceSettings",
                autoboto.TypeInfo(Scte20SourceSettings),
            ),
            (
                "scte27_source_settings",
                "Scte27SourceSettings",
                autoboto.TypeInfo(Scte27SourceSettings),
            ),
            (
                "teletext_source_settings",
                "TeletextSourceSettings",
                autoboto.TypeInfo(TeletextSourceSettings),
            ),
        ]

    # Placeholder documentation for AribSourceSettings
    arib_source_settings: "AribSourceSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for DvbSubSourceSettings
    dvb_sub_source_settings: "DvbSubSourceSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for EmbeddedSourceSettings
    embedded_source_settings: "EmbeddedSourceSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for Scte20SourceSettings
    scte20_source_settings: "Scte20SourceSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for Scte27SourceSettings
    scte27_source_settings: "Scte27SourceSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for TeletextSourceSettings
    teletext_source_settings: "TeletextSourceSettings" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class Channel(autoboto.ShapeBase):
    """
    Placeholder documentation for Channel
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
                "destinations",
                "Destinations",
                autoboto.TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "egress_endpoints",
                "EgressEndpoints",
                autoboto.TypeInfo(typing.List[ChannelEgressEndpoint]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                autoboto.TypeInfo(EncoderSettings),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "input_attachments",
                "InputAttachments",
                autoboto.TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                autoboto.TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                autoboto.TypeInfo(LogLevel),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "pipelines_running_count",
                "PipelinesRunningCount",
                autoboto.TypeInfo(int),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(ChannelState),
            ),
        ]

    # The unique arn of the channel.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of destinations of the channel. For UDP outputs, there is one
    # destination per output. For other types (HLS, for example), there is one
    # destination per packager.
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default_factory=list,
    )

    # The endpoints where outgoing connections initiate from
    egress_endpoints: typing.List["ChannelEgressEndpoint"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for EncoderSettings
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default_factory=dict,
    )

    # The unique id of the channel.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # List of input attachments for channel.
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for InputSpecification
    input_specification: "InputSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # The log level being written to CloudWatch Logs.
    log_level: "LogLevel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the channel. (user-mutable)
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of currently healthy pipelines.
    pipelines_running_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the role assumed when running the
    # Channel.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placeholder documentation for ChannelState
    state: "ChannelState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ChannelConfigurationValidationError(autoboto.ShapeBase):
    """
    Placeholder documentation for ChannelConfigurationValidationError
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "validation_errors",
                "ValidationErrors",
                autoboto.TypeInfo(typing.List[ValidationError]),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A collection of validation error responses.
    validation_errors: typing.List["ValidationError"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ChannelEgressEndpoint(autoboto.ShapeBase):
    """
    Placeholder documentation for ChannelEgressEndpoint
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_ip",
                "SourceIp",
                autoboto.TypeInfo(str),
            ),
        ]

    # Public IP of where a channel's output comes from
    source_ip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ChannelState(Enum):
    """
    Placeholder documentation for ChannelState
    """
    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    IDLE = "IDLE"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    RECOVERING = "RECOVERING"
    STOPPING = "STOPPING"
    DELETING = "DELETING"
    DELETED = "DELETED"


@dataclasses.dataclass
class ChannelSummary(autoboto.ShapeBase):
    """
    Placeholder documentation for ChannelSummary
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
                "destinations",
                "Destinations",
                autoboto.TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "egress_endpoints",
                "EgressEndpoints",
                autoboto.TypeInfo(typing.List[ChannelEgressEndpoint]),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "input_attachments",
                "InputAttachments",
                autoboto.TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                autoboto.TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                autoboto.TypeInfo(LogLevel),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "pipelines_running_count",
                "PipelinesRunningCount",
                autoboto.TypeInfo(int),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(ChannelState),
            ),
        ]

    # The unique arn of the channel.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of destinations of the channel. For UDP outputs, there is one
    # destination per output. For other types (HLS, for example), there is one
    # destination per packager.
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default_factory=list,
    )

    # The endpoints where outgoing connections initiate from
    egress_endpoints: typing.List["ChannelEgressEndpoint"] = dataclasses.field(
        default_factory=list,
    )

    # The unique id of the channel.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # List of input attachments for channel.
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for InputSpecification
    input_specification: "InputSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # The log level being written to CloudWatch Logs.
    log_level: "LogLevel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the channel. (user-mutable)
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of currently healthy pipelines.
    pipelines_running_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the role assumed when running the
    # Channel.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placeholder documentation for ChannelState
    state: "ChannelState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConflictException(autoboto.ShapeBase):
    """
    Placeholder documentation for ConflictException
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

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateChannel(autoboto.ShapeBase):
    """
    Placeholder documentation for CreateChannel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destinations",
                "Destinations",
                autoboto.TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                autoboto.TypeInfo(EncoderSettings),
            ),
            (
                "input_attachments",
                "InputAttachments",
                autoboto.TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                autoboto.TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                autoboto.TypeInfo(LogLevel),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "reserved",
                "Reserved",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __listOfOutputDestination
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for EncoderSettings
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default_factory=dict,
    )

    # List of input attachments for channel.
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default_factory=list,
    )

    # Specification of input for this channel (max. bitrate, resolution, codec,
    # etc.)
    input_specification: "InputSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # The log level to write to CloudWatch Logs.
    log_level: "LogLevel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Name of channel.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Unique request ID to be specified. This is needed to prevent retries from
    # creating multiple resources.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Deprecated field that's only usable by whitelisted customers.
    reserved: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional Amazon Resource Name (ARN) of the role to assume when running
    # the Channel.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateChannelRequest(autoboto.ShapeBase):
    """
    A request to create a channel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destinations",
                "Destinations",
                autoboto.TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                autoboto.TypeInfo(EncoderSettings),
            ),
            (
                "input_attachments",
                "InputAttachments",
                autoboto.TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                autoboto.TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                autoboto.TypeInfo(LogLevel),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "reserved",
                "Reserved",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __listOfOutputDestination
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for EncoderSettings
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default_factory=dict,
    )

    # List of input attachments for channel.
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default_factory=list,
    )

    # Specification of input for this channel (max. bitrate, resolution, codec,
    # etc.)
    input_specification: "InputSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # The log level to write to CloudWatch Logs.
    log_level: "LogLevel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Name of channel.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Unique request ID to be specified. This is needed to prevent retries from
    # creating multiple resources.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Deprecated field that's only usable by whitelisted customers.
    reserved: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional Amazon Resource Name (ARN) of the role to assume when running
    # the Channel.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateChannelResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for CreateChannelResponse
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "channel",
                "Channel",
                autoboto.TypeInfo(Channel),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Placeholder documentation for Channel
    channel: "Channel" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateChannelResultModel(autoboto.ShapeBase):
    """
    Placeholder documentation for CreateChannelResultModel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel",
                "Channel",
                autoboto.TypeInfo(Channel),
            ),
        ]

    # Placeholder documentation for Channel
    channel: "Channel" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateInput(autoboto.ShapeBase):
    """
    Placeholder documentation for CreateInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destinations",
                "Destinations",
                autoboto.TypeInfo(typing.List[InputDestinationRequest]),
            ),
            (
                "input_security_groups",
                "InputSecurityGroups",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "sources",
                "Sources",
                autoboto.TypeInfo(typing.List[InputSourceRequest]),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(InputType),
            ),
        ]

    # Destination settings for PUSH type inputs.
    destinations: typing.List["InputDestinationRequest"] = dataclasses.field(
        default_factory=list,
    )

    # A list of security groups referenced by IDs to attach to the input.
    input_security_groups: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Name of the input.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Unique identifier of the request to ensure the request is handled exactly
    # once in case of retries.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The source URLs for a PULL-type input. Every PULL type input needs exactly
    # two source URLs for redundancy. Only specify sources for PULL type Inputs.
    # Leave Destinations empty.
    sources: typing.List["InputSourceRequest"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for InputType
    type: "InputType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInputRequest(autoboto.ShapeBase):
    """
    The name of the input
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destinations",
                "Destinations",
                autoboto.TypeInfo(typing.List[InputDestinationRequest]),
            ),
            (
                "input_security_groups",
                "InputSecurityGroups",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                autoboto.TypeInfo(str),
            ),
            (
                "sources",
                "Sources",
                autoboto.TypeInfo(typing.List[InputSourceRequest]),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(InputType),
            ),
        ]

    # Destination settings for PUSH type inputs.
    destinations: typing.List["InputDestinationRequest"] = dataclasses.field(
        default_factory=list,
    )

    # A list of security groups referenced by IDs to attach to the input.
    input_security_groups: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Name of the input.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Unique identifier of the request to ensure the request is handled exactly
    # once in case of retries.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The source URLs for a PULL-type input. Every PULL type input needs exactly
    # two source URLs for redundancy. Only specify sources for PULL type Inputs.
    # Leave Destinations empty.
    sources: typing.List["InputSourceRequest"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for InputType
    type: "InputType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInputResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for CreateInputResponse
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "input",
                "Input",
                autoboto.TypeInfo(Input),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Placeholder documentation for Input
    input: "Input" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateInputResultModel(autoboto.ShapeBase):
    """
    Placeholder documentation for CreateInputResultModel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input",
                "Input",
                autoboto.TypeInfo(Input),
            ),
        ]

    # Placeholder documentation for Input
    input: "Input" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateInputSecurityGroupRequest(autoboto.ShapeBase):
    """
    The IPv4 CIDRs to whitelist for this Input Security Group
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "whitelist_rules",
                "WhitelistRules",
                autoboto.TypeInfo(typing.List[InputWhitelistRuleCidr]),
            ),
        ]

    # List of IPv4 CIDR addresses to whitelist
    whitelist_rules: typing.List["InputWhitelistRuleCidr"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateInputSecurityGroupResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for CreateInputSecurityGroupResponse
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "security_group",
                "SecurityGroup",
                autoboto.TypeInfo(InputSecurityGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An Input Security Group
    security_group: "InputSecurityGroup" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateInputSecurityGroupResultModel(autoboto.ShapeBase):
    """
    Placeholder documentation for CreateInputSecurityGroupResultModel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_group",
                "SecurityGroup",
                autoboto.TypeInfo(InputSecurityGroup),
            ),
        ]

    # An Input Security Group
    security_group: "InputSecurityGroup" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteChannelRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for DeleteChannelRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Unique ID of the channel.
    channel_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteChannelResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for DeleteChannelResponse
    """

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
                "destinations",
                "Destinations",
                autoboto.TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "egress_endpoints",
                "EgressEndpoints",
                autoboto.TypeInfo(typing.List[ChannelEgressEndpoint]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                autoboto.TypeInfo(EncoderSettings),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "input_attachments",
                "InputAttachments",
                autoboto.TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                autoboto.TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                autoboto.TypeInfo(LogLevel),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "pipelines_running_count",
                "PipelinesRunningCount",
                autoboto.TypeInfo(int),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(ChannelState),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The unique arn of the channel.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of destinations of the channel. For UDP outputs, there is one
    # destination per output. For other types (HLS, for example), there is one
    # destination per packager.
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default_factory=list,
    )

    # The endpoints where outgoing connections initiate from
    egress_endpoints: typing.List["ChannelEgressEndpoint"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for EncoderSettings
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default_factory=dict,
    )

    # The unique id of the channel.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # List of input attachments for channel.
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for InputSpecification
    input_specification: "InputSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # The log level being written to CloudWatch Logs.
    log_level: "LogLevel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the channel. (user-mutable)
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of currently healthy pipelines.
    pipelines_running_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the role assumed when running the
    # Channel.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placeholder documentation for ChannelState
    state: "ChannelState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteInputRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for DeleteInputRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_id",
                "InputId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Unique ID of the input
    input_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteInputResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for DeleteInputResponse
    """

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
class DeleteInputSecurityGroupRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for DeleteInputSecurityGroupRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_security_group_id",
                "InputSecurityGroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Input Security Group to delete
    input_security_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteInputSecurityGroupResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for DeleteInputSecurityGroupResponse
    """

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
class DeleteReservationRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for DeleteReservationRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reservation_id",
                "ReservationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Unique reservation ID, e.g. '1234567'
    reservation_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteReservationResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for DeleteReservationResponse
    """

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
                "count",
                "Count",
                autoboto.TypeInfo(int),
            ),
            (
                "currency_code",
                "CurrencyCode",
                autoboto.TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(int),
            ),
            (
                "duration_units",
                "DurationUnits",
                autoboto.TypeInfo(OfferingDurationUnits),
            ),
            (
                "end",
                "End",
                autoboto.TypeInfo(str),
            ),
            (
                "fixed_price",
                "FixedPrice",
                autoboto.TypeInfo(float),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "offering_description",
                "OfferingDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "offering_id",
                "OfferingId",
                autoboto.TypeInfo(str),
            ),
            (
                "offering_type",
                "OfferingType",
                autoboto.TypeInfo(OfferingType),
            ),
            (
                "region",
                "Region",
                autoboto.TypeInfo(str),
            ),
            (
                "reservation_id",
                "ReservationId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_specification",
                "ResourceSpecification",
                autoboto.TypeInfo(ReservationResourceSpecification),
            ),
            (
                "start",
                "Start",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(ReservationState),
            ),
            (
                "usage_price",
                "UsagePrice",
                autoboto.TypeInfo(float),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique reservation ARN, e.g. 'arn:aws:medialive:us-
    # west-2:123456789012:reservation:1234567'
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Number of reserved resources
    count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'
    currency_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Lease duration, e.g. '12'
    duration: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Units for duration, e.g. 'MONTHS'
    duration_units: "OfferingDurationUnits" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Reservation UTC end date and time in ISO-8601 format, e.g.
    # '2019-03-01T00:00:00'
    end: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT
    # offering
    fixed_price: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # User specified reservation name
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and
    # standard VQ in US West (Oregon)'
    offering_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique offering ID, e.g. '87654321'
    offering_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Offering type, e.g. 'NO_UPFRONT'
    offering_type: "OfferingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # AWS region, e.g. 'us-west-2'
    region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Unique reservation ID, e.g. '1234567'
    reservation_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Resource configuration details
    resource_specification: "ReservationResourceSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # Reservation UTC start date and time in ISO-8601 format, e.g.
    # '2018-03-01T00:00:00'
    start: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Current state of reservation, e.g. 'ACTIVE'
    state: "ReservationState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Recurring usage charge for each reserved resource, e.g. '157.0'
    usage_price: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeChannelRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for DescribeChannelRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
                autoboto.TypeInfo(str),
            ),
        ]

    # channel ID
    channel_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeChannelResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for DescribeChannelResponse
    """

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
                "destinations",
                "Destinations",
                autoboto.TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "egress_endpoints",
                "EgressEndpoints",
                autoboto.TypeInfo(typing.List[ChannelEgressEndpoint]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                autoboto.TypeInfo(EncoderSettings),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "input_attachments",
                "InputAttachments",
                autoboto.TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                autoboto.TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                autoboto.TypeInfo(LogLevel),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "pipelines_running_count",
                "PipelinesRunningCount",
                autoboto.TypeInfo(int),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(ChannelState),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The unique arn of the channel.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of destinations of the channel. For UDP outputs, there is one
    # destination per output. For other types (HLS, for example), there is one
    # destination per packager.
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default_factory=list,
    )

    # The endpoints where outgoing connections initiate from
    egress_endpoints: typing.List["ChannelEgressEndpoint"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for EncoderSettings
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default_factory=dict,
    )

    # The unique id of the channel.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # List of input attachments for channel.
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for InputSpecification
    input_specification: "InputSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # The log level being written to CloudWatch Logs.
    log_level: "LogLevel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the channel. (user-mutable)
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of currently healthy pipelines.
    pipelines_running_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the role assumed when running the
    # Channel.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placeholder documentation for ChannelState
    state: "ChannelState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeInputRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for DescribeInputRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_id",
                "InputId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Unique ID of the input
    input_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInputResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for DescribeInputResponse
    """

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
                "attached_channels",
                "AttachedChannels",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "destinations",
                "Destinations",
                autoboto.TypeInfo(typing.List[InputDestination]),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "security_groups",
                "SecurityGroups",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "sources",
                "Sources",
                autoboto.TypeInfo(typing.List[InputSource]),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(InputState),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(InputType),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Unique ARN of the input (generated, immutable).
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of channel IDs that that input is attached to (currently an input
    # can only be attached to one channel).
    attached_channels: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list of the destinations of the input (PUSH-type).
    destinations: typing.List["InputDestination"] = dataclasses.field(
        default_factory=list,
    )

    # The generated ID of the input (unique for user account, immutable).
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user-assigned name (This is a mutable value).
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of IDs for all the security groups attached to the input.
    security_groups: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list of the sources of the input (PULL-type).
    sources: typing.List["InputSource"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for InputState
    state: "InputState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Placeholder documentation for InputType
    type: "InputType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInputSecurityGroupRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for DescribeInputSecurityGroupRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_security_group_id",
                "InputSecurityGroupId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The id of the Input Security Group to describe
    input_security_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeInputSecurityGroupResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for DescribeInputSecurityGroupResponse
    """

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
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "inputs",
                "Inputs",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(InputSecurityGroupState),
            ),
            (
                "whitelist_rules",
                "WhitelistRules",
                autoboto.TypeInfo(typing.List[InputWhitelistRule]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique ARN of Input Security Group
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Id of the Input Security Group
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of inputs currently using this Input Security Group.
    inputs: typing.List[str] = dataclasses.field(default_factory=list, )

    # The current state of the Input Security Group.
    state: "InputSecurityGroupState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whitelist rules and their sync status
    whitelist_rules: typing.List["InputWhitelistRule"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeOfferingRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for DescribeOfferingRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "offering_id",
                "OfferingId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Unique offering ID, e.g. '87654321'
    offering_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeOfferingResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for DescribeOfferingResponse
    """

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
                "currency_code",
                "CurrencyCode",
                autoboto.TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(int),
            ),
            (
                "duration_units",
                "DurationUnits",
                autoboto.TypeInfo(OfferingDurationUnits),
            ),
            (
                "fixed_price",
                "FixedPrice",
                autoboto.TypeInfo(float),
            ),
            (
                "offering_description",
                "OfferingDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "offering_id",
                "OfferingId",
                autoboto.TypeInfo(str),
            ),
            (
                "offering_type",
                "OfferingType",
                autoboto.TypeInfo(OfferingType),
            ),
            (
                "region",
                "Region",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_specification",
                "ResourceSpecification",
                autoboto.TypeInfo(ReservationResourceSpecification),
            ),
            (
                "usage_price",
                "UsagePrice",
                autoboto.TypeInfo(float),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique offering ARN, e.g. 'arn:aws:medialive:us-
    # west-2:123456789012:offering:87654321'
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'
    currency_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Lease duration, e.g. '12'
    duration: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Units for duration, e.g. 'MONTHS'
    duration_units: "OfferingDurationUnits" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT
    # offering
    fixed_price: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and
    # standard VQ in US West (Oregon)'
    offering_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique offering ID, e.g. '87654321'
    offering_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Offering type, e.g. 'NO_UPFRONT'
    offering_type: "OfferingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # AWS region, e.g. 'us-west-2'
    region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Resource configuration details
    resource_specification: "ReservationResourceSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # Recurring usage charge for each reserved resource, e.g. '157.0'
    usage_price: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReservationRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for DescribeReservationRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reservation_id",
                "ReservationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Unique reservation ID, e.g. '1234567'
    reservation_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeReservationResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for DescribeReservationResponse
    """

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
                "count",
                "Count",
                autoboto.TypeInfo(int),
            ),
            (
                "currency_code",
                "CurrencyCode",
                autoboto.TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(int),
            ),
            (
                "duration_units",
                "DurationUnits",
                autoboto.TypeInfo(OfferingDurationUnits),
            ),
            (
                "end",
                "End",
                autoboto.TypeInfo(str),
            ),
            (
                "fixed_price",
                "FixedPrice",
                autoboto.TypeInfo(float),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "offering_description",
                "OfferingDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "offering_id",
                "OfferingId",
                autoboto.TypeInfo(str),
            ),
            (
                "offering_type",
                "OfferingType",
                autoboto.TypeInfo(OfferingType),
            ),
            (
                "region",
                "Region",
                autoboto.TypeInfo(str),
            ),
            (
                "reservation_id",
                "ReservationId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_specification",
                "ResourceSpecification",
                autoboto.TypeInfo(ReservationResourceSpecification),
            ),
            (
                "start",
                "Start",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(ReservationState),
            ),
            (
                "usage_price",
                "UsagePrice",
                autoboto.TypeInfo(float),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique reservation ARN, e.g. 'arn:aws:medialive:us-
    # west-2:123456789012:reservation:1234567'
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Number of reserved resources
    count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'
    currency_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Lease duration, e.g. '12'
    duration: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Units for duration, e.g. 'MONTHS'
    duration_units: "OfferingDurationUnits" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Reservation UTC end date and time in ISO-8601 format, e.g.
    # '2019-03-01T00:00:00'
    end: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT
    # offering
    fixed_price: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # User specified reservation name
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and
    # standard VQ in US West (Oregon)'
    offering_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique offering ID, e.g. '87654321'
    offering_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Offering type, e.g. 'NO_UPFRONT'
    offering_type: "OfferingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # AWS region, e.g. 'us-west-2'
    region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Unique reservation ID, e.g. '1234567'
    reservation_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Resource configuration details
    resource_specification: "ReservationResourceSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # Reservation UTC start date and time in ISO-8601 format, e.g.
    # '2018-03-01T00:00:00'
    start: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Current state of reservation, e.g. 'ACTIVE'
    state: "ReservationState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Recurring usage charge for each reserved resource, e.g. '157.0'
    usage_price: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeScheduleRequest(autoboto.ShapeBase):
    """
    Request for a describe schedule call.
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

    # Id of the channel whose schedule is being updated.
    channel_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placeholder documentation for MaxResults
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeScheduleResponse(autoboto.OutputShapeBase):
    """
    Response for a describe schedule call.
    """

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
                "schedule_actions",
                "ScheduleActions",
                autoboto.TypeInfo(typing.List[ScheduleAction]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The next token; for use in pagination.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of schedule actions.
    schedule_actions: typing.List["ScheduleAction"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DvbNitSettings(autoboto.ShapeBase):
    """
    DVB Network Information Table (NIT)
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "network_id",
                "NetworkId",
                autoboto.TypeInfo(int),
            ),
            (
                "network_name",
                "NetworkName",
                autoboto.TypeInfo(str),
            ),
            (
                "rep_interval",
                "RepInterval",
                autoboto.TypeInfo(int),
            ),
        ]

    # The numeric value placed in the Network Information Table (NIT).
    network_id: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The network name text placed in the networkNameDescriptor inside the
    # Network Information Table. Maximum length is 256 characters.
    network_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of milliseconds between instances of this table in the output
    # transport stream.
    rep_interval: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class DvbSdtOutputSdt(Enum):
    """
    Placeholder documentation for DvbSdtOutputSdt
    """
    SDT_FOLLOW = "SDT_FOLLOW"
    SDT_FOLLOW_IF_PRESENT = "SDT_FOLLOW_IF_PRESENT"
    SDT_MANUAL = "SDT_MANUAL"
    SDT_NONE = "SDT_NONE"


@dataclasses.dataclass
class DvbSdtSettings(autoboto.ShapeBase):
    """
    DVB Service Description Table (SDT)
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_sdt",
                "OutputSdt",
                autoboto.TypeInfo(DvbSdtOutputSdt),
            ),
            (
                "rep_interval",
                "RepInterval",
                autoboto.TypeInfo(int),
            ),
            (
                "service_name",
                "ServiceName",
                autoboto.TypeInfo(str),
            ),
            (
                "service_provider_name",
                "ServiceProviderName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Selects method of inserting SDT information into output stream. The
    # sdtFollow setting copies SDT information from input stream to output
    # stream. The sdtFollowIfPresent setting copies SDT information from input
    # stream to output stream if SDT information is present in the input,
    # otherwise it will fall back on the user-defined values. The sdtManual
    # setting means user will enter the SDT information. The sdtNone setting
    # means output stream will not contain SDT information.
    output_sdt: "DvbSdtOutputSdt" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of milliseconds between instances of this table in the output
    # transport stream.
    rep_interval: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The service name placed in the serviceDescriptor in the Service Description
    # Table. Maximum length is 256 characters.
    service_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The service provider name placed in the serviceDescriptor in the Service
    # Description Table. Maximum length is 256 characters.
    service_provider_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class DvbSubDestinationAlignment(Enum):
    """
    Placeholder documentation for DvbSubDestinationAlignment
    """
    CENTERED = "CENTERED"
    LEFT = "LEFT"
    SMART = "SMART"


class DvbSubDestinationBackgroundColor(Enum):
    """
    Placeholder documentation for DvbSubDestinationBackgroundColor
    """
    BLACK = "BLACK"
    NONE = "NONE"
    WHITE = "WHITE"


class DvbSubDestinationFontColor(Enum):
    """
    Placeholder documentation for DvbSubDestinationFontColor
    """
    BLACK = "BLACK"
    BLUE = "BLUE"
    GREEN = "GREEN"
    RED = "RED"
    WHITE = "WHITE"
    YELLOW = "YELLOW"


class DvbSubDestinationOutlineColor(Enum):
    """
    Placeholder documentation for DvbSubDestinationOutlineColor
    """
    BLACK = "BLACK"
    BLUE = "BLUE"
    GREEN = "GREEN"
    RED = "RED"
    WHITE = "WHITE"
    YELLOW = "YELLOW"


@dataclasses.dataclass
class DvbSubDestinationSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for DvbSubDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alignment",
                "Alignment",
                autoboto.TypeInfo(DvbSubDestinationAlignment),
            ),
            (
                "background_color",
                "BackgroundColor",
                autoboto.TypeInfo(DvbSubDestinationBackgroundColor),
            ),
            (
                "background_opacity",
                "BackgroundOpacity",
                autoboto.TypeInfo(int),
            ),
            (
                "font",
                "Font",
                autoboto.TypeInfo(InputLocation),
            ),
            (
                "font_color",
                "FontColor",
                autoboto.TypeInfo(DvbSubDestinationFontColor),
            ),
            (
                "font_opacity",
                "FontOpacity",
                autoboto.TypeInfo(int),
            ),
            (
                "font_resolution",
                "FontResolution",
                autoboto.TypeInfo(int),
            ),
            (
                "font_size",
                "FontSize",
                autoboto.TypeInfo(str),
            ),
            (
                "outline_color",
                "OutlineColor",
                autoboto.TypeInfo(DvbSubDestinationOutlineColor),
            ),
            (
                "outline_size",
                "OutlineSize",
                autoboto.TypeInfo(int),
            ),
            (
                "shadow_color",
                "ShadowColor",
                autoboto.TypeInfo(DvbSubDestinationShadowColor),
            ),
            (
                "shadow_opacity",
                "ShadowOpacity",
                autoboto.TypeInfo(int),
            ),
            (
                "shadow_x_offset",
                "ShadowXOffset",
                autoboto.TypeInfo(int),
            ),
            (
                "shadow_y_offset",
                "ShadowYOffset",
                autoboto.TypeInfo(int),
            ),
            (
                "teletext_grid_control",
                "TeletextGridControl",
                autoboto.TypeInfo(DvbSubDestinationTeletextGridControl),
            ),
            (
                "x_position",
                "XPosition",
                autoboto.TypeInfo(int),
            ),
            (
                "y_position",
                "YPosition",
                autoboto.TypeInfo(int),
            ),
        ]

    # If no explicit xPosition or yPosition is provided, setting alignment to
    # centered will place the captions at the bottom center of the output.
    # Similarly, setting a left alignment will align captions to the bottom left
    # of the output. If x and y positions are given in conjunction with the
    # alignment parameter, the font will be justified (either left or centered)
    # relative to those coordinates. Selecting "smart" justification will left-
    # justify live subtitles and center-justify pre-recorded subtitles. This
    # option is not valid for source captions that are STL or 608/embedded. These
    # source settings are already pre-defined by the caption stream. All burn-in
    # and DVB-Sub font settings must match.
    alignment: "DvbSubDestinationAlignment" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the color of the rectangle behind the captions. All burn-in and
    # DVB-Sub font settings must match.
    background_color: "DvbSubDestinationBackgroundColor" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the opacity of the background rectangle. 255 is opaque; 0 is
    # transparent. Leaving this parameter blank is equivalent to setting it to 0
    # (transparent). All burn-in and DVB-Sub font settings must match.
    background_opacity: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # External font file used for caption burn-in. File extension must be 'ttf'
    # or 'tte'. Although the user can select output fonts for many different
    # types of input captions, embedded, STL and teletext sources use a strict
    # grid system. Using external fonts with these caption sources could cause
    # unexpected display of proportional fonts. All burn-in and DVB-Sub font
    # settings must match.
    font: "InputLocation" = dataclasses.field(default_factory=dict, )

    # Specifies the color of the burned-in captions. This option is not valid for
    # source captions that are STL, 608/embedded or teletext. These source
    # settings are already pre-defined by the caption stream. All burn-in and
    # DVB-Sub font settings must match.
    font_color: "DvbSubDestinationFontColor" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the opacity of the burned-in captions. 255 is opaque; 0 is
    # transparent. All burn-in and DVB-Sub font settings must match.
    font_opacity: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and
    # DVB-Sub font settings must match.
    font_resolution: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to auto fontSize will scale depending on the size of the output.
    # Giving a positive integer will specify the exact font size in points. All
    # burn-in and DVB-Sub font settings must match.
    font_size: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies font outline color. This option is not valid for source captions
    # that are either 608/embedded or teletext. These source settings are already
    # pre-defined by the caption stream. All burn-in and DVB-Sub font settings
    # must match.
    outline_color: "DvbSubDestinationOutlineColor" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies font outline size in pixels. This option is not valid for source
    # captions that are either 608/embedded or teletext. These source settings
    # are already pre-defined by the caption stream. All burn-in and DVB-Sub font
    # settings must match.
    outline_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the color of the shadow cast by the captions. All burn-in and
    # DVB-Sub font settings must match.
    shadow_color: "DvbSubDestinationShadowColor" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the opacity of the shadow. 255 is opaque; 0 is transparent.
    # Leaving this parameter blank is equivalent to setting it to 0
    # (transparent). All burn-in and DVB-Sub font settings must match.
    shadow_opacity: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the horizontal offset of the shadow relative to the captions in
    # pixels. A value of -2 would result in a shadow offset 2 pixels to the left.
    # All burn-in and DVB-Sub font settings must match.
    shadow_x_offset: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the vertical offset of the shadow relative to the captions in
    # pixels. A value of -2 would result in a shadow offset 2 pixels above the
    # text. All burn-in and DVB-Sub font settings must match.
    shadow_y_offset: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Controls whether a fixed grid size will be used to generate the output
    # subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in
    # outputs.
    teletext_grid_control: "DvbSubDestinationTeletextGridControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the horizontal position of the caption relative to the left side
    # of the output in pixels. A value of 10 would result in the captions
    # starting 10 pixels from the left of the output. If no explicit xPosition is
    # provided, the horizontal caption position will be determined by the
    # alignment parameter. This option is not valid for source captions that are
    # STL, 608/embedded or teletext. These source settings are already pre-
    # defined by the caption stream. All burn-in and DVB-Sub font settings must
    # match.
    x_position: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the vertical position of the caption relative to the top of the
    # output in pixels. A value of 10 would result in the captions starting 10
    # pixels from the top of the output. If no explicit yPosition is provided,
    # the caption will be positioned towards the bottom of the output. This
    # option is not valid for source captions that are STL, 608/embedded or
    # teletext. These source settings are already pre-defined by the caption
    # stream. All burn-in and DVB-Sub font settings must match.
    y_position: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class DvbSubDestinationShadowColor(Enum):
    """
    Placeholder documentation for DvbSubDestinationShadowColor
    """
    BLACK = "BLACK"
    NONE = "NONE"
    WHITE = "WHITE"


class DvbSubDestinationTeletextGridControl(Enum):
    """
    Placeholder documentation for DvbSubDestinationTeletextGridControl
    """
    FIXED = "FIXED"
    SCALED = "SCALED"


@dataclasses.dataclass
class DvbSubSourceSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for DvbSubSourceSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pid",
                "Pid",
                autoboto.TypeInfo(int),
            ),
        ]

    # When using DVB-Sub with Burn-In or SMPTE-TT, use this PID for the source
    # content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed
    # through, regardless of selectors.
    pid: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DvbTdtSettings(autoboto.ShapeBase):
    """
    DVB Time and Date Table (SDT)
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rep_interval",
                "RepInterval",
                autoboto.TypeInfo(int),
            ),
        ]

    # The number of milliseconds between instances of this table in the output
    # transport stream.
    rep_interval: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class Eac3AttenuationControl(Enum):
    """
    Placeholder documentation for Eac3AttenuationControl
    """
    ATTENUATE_3_DB = "ATTENUATE_3_DB"
    NONE = "NONE"


class Eac3BitstreamMode(Enum):
    """
    Placeholder documentation for Eac3BitstreamMode
    """
    COMMENTARY = "COMMENTARY"
    COMPLETE_MAIN = "COMPLETE_MAIN"
    EMERGENCY = "EMERGENCY"
    HEARING_IMPAIRED = "HEARING_IMPAIRED"
    VISUALLY_IMPAIRED = "VISUALLY_IMPAIRED"


class Eac3CodingMode(Enum):
    """
    Placeholder documentation for Eac3CodingMode
    """
    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_3_2 = "CODING_MODE_3_2"


class Eac3DcFilter(Enum):
    """
    Placeholder documentation for Eac3DcFilter
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Eac3DrcLine(Enum):
    """
    Placeholder documentation for Eac3DrcLine
    """
    FILM_LIGHT = "FILM_LIGHT"
    FILM_STANDARD = "FILM_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    NONE = "NONE"
    SPEECH = "SPEECH"


class Eac3DrcRf(Enum):
    """
    Placeholder documentation for Eac3DrcRf
    """
    FILM_LIGHT = "FILM_LIGHT"
    FILM_STANDARD = "FILM_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    NONE = "NONE"
    SPEECH = "SPEECH"


class Eac3LfeControl(Enum):
    """
    Placeholder documentation for Eac3LfeControl
    """
    LFE = "LFE"
    NO_LFE = "NO_LFE"


class Eac3LfeFilter(Enum):
    """
    Placeholder documentation for Eac3LfeFilter
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Eac3MetadataControl(Enum):
    """
    Placeholder documentation for Eac3MetadataControl
    """
    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class Eac3PassthroughControl(Enum):
    """
    Placeholder documentation for Eac3PassthroughControl
    """
    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    WHEN_POSSIBLE = "WHEN_POSSIBLE"


class Eac3PhaseControl(Enum):
    """
    Placeholder documentation for Eac3PhaseControl
    """
    NO_SHIFT = "NO_SHIFT"
    SHIFT_90_DEGREES = "SHIFT_90_DEGREES"


@dataclasses.dataclass
class Eac3Settings(autoboto.ShapeBase):
    """
    Placeholder documentation for Eac3Settings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attenuation_control",
                "AttenuationControl",
                autoboto.TypeInfo(Eac3AttenuationControl),
            ),
            (
                "bitrate",
                "Bitrate",
                autoboto.TypeInfo(float),
            ),
            (
                "bitstream_mode",
                "BitstreamMode",
                autoboto.TypeInfo(Eac3BitstreamMode),
            ),
            (
                "coding_mode",
                "CodingMode",
                autoboto.TypeInfo(Eac3CodingMode),
            ),
            (
                "dc_filter",
                "DcFilter",
                autoboto.TypeInfo(Eac3DcFilter),
            ),
            (
                "dialnorm",
                "Dialnorm",
                autoboto.TypeInfo(int),
            ),
            (
                "drc_line",
                "DrcLine",
                autoboto.TypeInfo(Eac3DrcLine),
            ),
            (
                "drc_rf",
                "DrcRf",
                autoboto.TypeInfo(Eac3DrcRf),
            ),
            (
                "lfe_control",
                "LfeControl",
                autoboto.TypeInfo(Eac3LfeControl),
            ),
            (
                "lfe_filter",
                "LfeFilter",
                autoboto.TypeInfo(Eac3LfeFilter),
            ),
            (
                "lo_ro_center_mix_level",
                "LoRoCenterMixLevel",
                autoboto.TypeInfo(float),
            ),
            (
                "lo_ro_surround_mix_level",
                "LoRoSurroundMixLevel",
                autoboto.TypeInfo(float),
            ),
            (
                "lt_rt_center_mix_level",
                "LtRtCenterMixLevel",
                autoboto.TypeInfo(float),
            ),
            (
                "lt_rt_surround_mix_level",
                "LtRtSurroundMixLevel",
                autoboto.TypeInfo(float),
            ),
            (
                "metadata_control",
                "MetadataControl",
                autoboto.TypeInfo(Eac3MetadataControl),
            ),
            (
                "passthrough_control",
                "PassthroughControl",
                autoboto.TypeInfo(Eac3PassthroughControl),
            ),
            (
                "phase_control",
                "PhaseControl",
                autoboto.TypeInfo(Eac3PhaseControl),
            ),
            (
                "stereo_downmix",
                "StereoDownmix",
                autoboto.TypeInfo(Eac3StereoDownmix),
            ),
            (
                "surround_ex_mode",
                "SurroundExMode",
                autoboto.TypeInfo(Eac3SurroundExMode),
            ),
            (
                "surround_mode",
                "SurroundMode",
                autoboto.TypeInfo(Eac3SurroundMode),
            ),
        ]

    # When set to attenuate3Db, applies a 3 dB attenuation to the surround
    # channels. Only used for 3/2 coding mode.
    attenuation_control: "Eac3AttenuationControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Average bitrate in bits/second. Valid bitrates depend on the coding mode.
    bitrate: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the bitstream mode (bsmod) for the emitted E-AC-3 stream. See
    # ATSC A/52-2012 (Annex E) for background on these values.
    bitstream_mode: "Eac3BitstreamMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Dolby Digital Plus coding mode. Determines number of channels.
    coding_mode: "Eac3CodingMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to enabled, activates a DC highpass filter for all input channels.
    dc_filter: "Eac3DcFilter" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Sets the dialnorm for the output. If blank and input audio is Dolby Digital
    # Plus, dialnorm will be passed through.
    dialnorm: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Sets the Dolby dynamic range compression profile.
    drc_line: "Eac3DrcLine" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Sets the profile for heavy Dolby dynamic range compression, ensures that
    # the instantaneous signal peaks do not exceed specified levels.
    drc_rf: "Eac3DrcRf" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When encoding 3/2 audio, setting to lfe enables the LFE channel
    lfe_control: "Eac3LfeControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to enabled, applies a 120Hz lowpass filter to the LFE channel
    # prior to encoding. Only valid with codingMode32 coding mode.
    lfe_filter: "Eac3LfeFilter" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Left only/Right only center mix level. Only used for 3/2 coding mode.
    lo_ro_center_mix_level: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Left only/Right only surround mix level. Only used for 3/2 coding mode.
    lo_ro_surround_mix_level: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Left total/Right total center mix level. Only used for 3/2 coding mode.
    lt_rt_center_mix_level: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Left total/Right total surround mix level. Only used for 3/2 coding mode.
    lt_rt_surround_mix_level: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to followInput, encoder metadata will be sourced from the DD, DD+,
    # or DolbyE decoder that supplied this audio data. If audio was not supplied
    # from one of these streams, then the static metadata settings will be used.
    metadata_control: "Eac3MetadataControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to whenPossible, input DD+ audio will be passed through if it is
    # present on the input. This detection is dynamic over the life of the
    # transcode. Inputs that alternate between DD+ and non-DD+ content will have
    # a consistent DD+ output as the system alternates between passthrough and
    # encoding.
    passthrough_control: "Eac3PassthroughControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to shift90Degrees, applies a 90-degree phase shift to the surround
    # channels. Only used for 3/2 coding mode.
    phase_control: "Eac3PhaseControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Stereo downmix preference. Only used for 3/2 coding mode.
    stereo_downmix: "Eac3StereoDownmix" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When encoding 3/2 audio, sets whether an extra center back surround channel
    # is matrix encoded into the left and right surround channels.
    surround_ex_mode: "Eac3SurroundExMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into
    # the two channels.
    surround_mode: "Eac3SurroundMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class Eac3StereoDownmix(Enum):
    """
    Placeholder documentation for Eac3StereoDownmix
    """
    DPL2 = "DPL2"
    LO_RO = "LO_RO"
    LT_RT = "LT_RT"
    NOT_INDICATED = "NOT_INDICATED"


class Eac3SurroundExMode(Enum):
    """
    Placeholder documentation for Eac3SurroundExMode
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    NOT_INDICATED = "NOT_INDICATED"


class Eac3SurroundMode(Enum):
    """
    Placeholder documentation for Eac3SurroundMode
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    NOT_INDICATED = "NOT_INDICATED"


class EmbeddedConvert608To708(Enum):
    """
    Placeholder documentation for EmbeddedConvert608To708
    """
    DISABLED = "DISABLED"
    UPCONVERT = "UPCONVERT"


@dataclasses.dataclass
class EmbeddedDestinationSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for EmbeddedDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EmbeddedPlusScte20DestinationSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for EmbeddedPlusScte20DestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class EmbeddedScte20Detection(Enum):
    """
    Placeholder documentation for EmbeddedScte20Detection
    """
    AUTO = "AUTO"
    OFF = "OFF"


@dataclasses.dataclass
class EmbeddedSourceSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for EmbeddedSourceSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "convert608_to708",
                "Convert608To708",
                autoboto.TypeInfo(EmbeddedConvert608To708),
            ),
            (
                "scte20_detection",
                "Scte20Detection",
                autoboto.TypeInfo(EmbeddedScte20Detection),
            ),
            (
                "source608_channel_number",
                "Source608ChannelNumber",
                autoboto.TypeInfo(int),
            ),
            (
                "source608_track_number",
                "Source608TrackNumber",
                autoboto.TypeInfo(int),
            ),
        ]

    # If upconvert, 608 data is both passed through via the "608 compatibility
    # bytes" fields of the 708 wrapper as well as translated into 708. 708 data
    # present in the source content will be discarded.
    convert608_to708: "EmbeddedConvert608To708" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Set to "auto" to handle streams with intermittent and/or non-aligned
    # SCTE-20 and Embedded captions.
    scte20_detection: "EmbeddedScte20Detection" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the 608/708 channel number within the video track from which to
    # extract captions. Unused for passthrough.
    source608_channel_number: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This field is unused and deprecated.
    source608_track_number: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Empty(autoboto.ShapeBase):
    """
    Placeholder documentation for Empty
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EncoderSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for EncoderSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_descriptions",
                "AudioDescriptions",
                autoboto.TypeInfo(typing.List[AudioDescription]),
            ),
            (
                "output_groups",
                "OutputGroups",
                autoboto.TypeInfo(typing.List[OutputGroup]),
            ),
            (
                "timecode_config",
                "TimecodeConfig",
                autoboto.TypeInfo(TimecodeConfig),
            ),
            (
                "video_descriptions",
                "VideoDescriptions",
                autoboto.TypeInfo(typing.List[VideoDescription]),
            ),
            (
                "avail_blanking",
                "AvailBlanking",
                autoboto.TypeInfo(AvailBlanking),
            ),
            (
                "avail_configuration",
                "AvailConfiguration",
                autoboto.TypeInfo(AvailConfiguration),
            ),
            (
                "blackout_slate",
                "BlackoutSlate",
                autoboto.TypeInfo(BlackoutSlate),
            ),
            (
                "caption_descriptions",
                "CaptionDescriptions",
                autoboto.TypeInfo(typing.List[CaptionDescription]),
            ),
            (
                "global_configuration",
                "GlobalConfiguration",
                autoboto.TypeInfo(GlobalConfiguration),
            ),
        ]

    # Placeholder documentation for __listOfAudioDescription
    audio_descriptions: typing.List["AudioDescription"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for __listOfOutputGroup
    output_groups: typing.List["OutputGroup"] = dataclasses.field(
        default_factory=list,
    )

    # Contains settings used to acquire and adjust timecode information from
    # inputs.
    timecode_config: "TimecodeConfig" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for __listOfVideoDescription
    video_descriptions: typing.List["VideoDescription"] = dataclasses.field(
        default_factory=list,
    )

    # Settings for ad avail blanking.
    avail_blanking: "AvailBlanking" = dataclasses.field(default_factory=dict, )

    # Event-wide configuration settings for ad avail insertion.
    avail_configuration: "AvailConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # Settings for blackout slate.
    blackout_slate: "BlackoutSlate" = dataclasses.field(default_factory=dict, )

    # Settings for caption decriptions
    caption_descriptions: typing.List["CaptionDescription"] = dataclasses.field(
        default_factory=list,
    )

    # Configuration settings that apply to the event as a whole.
    global_configuration: "GlobalConfiguration" = dataclasses.field(
        default_factory=dict,
    )


class FecOutputIncludeFec(Enum):
    """
    Placeholder documentation for FecOutputIncludeFec
    """
    COLUMN = "COLUMN"
    COLUMN_AND_ROW = "COLUMN_AND_ROW"


@dataclasses.dataclass
class FecOutputSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for FecOutputSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "column_depth",
                "ColumnDepth",
                autoboto.TypeInfo(int),
            ),
            (
                "include_fec",
                "IncludeFec",
                autoboto.TypeInfo(FecOutputIncludeFec),
            ),
            (
                "row_length",
                "RowLength",
                autoboto.TypeInfo(int),
            ),
        ]

    # Parameter D from SMPTE 2022-1. The height of the FEC protection matrix. The
    # number of transport stream packets per column error correction packet. Must
    # be between 4 and 20, inclusive.
    column_depth: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Enables column only or column and row based FEC
    include_fec: "FecOutputIncludeFec" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Parameter L from SMPTE 2022-1. The width of the FEC protection matrix. Must
    # be between 1 and 20, inclusive. If only Column FEC is used, then larger
    # values increase robustness. If Row FEC is used, then this is the number of
    # transport stream packets per row error correction packet, and the value
    # must be between 4 and 20, inclusive, if includeFec is columnAndRow. If
    # includeFec is column, this value must be 1 to 20, inclusive.
    row_length: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class FixedAfd(Enum):
    """
    Placeholder documentation for FixedAfd
    """
    AFD_0000 = "AFD_0000"
    AFD_0010 = "AFD_0010"
    AFD_0011 = "AFD_0011"
    AFD_0100 = "AFD_0100"
    AFD_1000 = "AFD_1000"
    AFD_1001 = "AFD_1001"
    AFD_1010 = "AFD_1010"
    AFD_1011 = "AFD_1011"
    AFD_1101 = "AFD_1101"
    AFD_1110 = "AFD_1110"
    AFD_1111 = "AFD_1111"


@dataclasses.dataclass
class FixedModeScheduleActionStartSettings(autoboto.ShapeBase):
    """
    Fixed mode schedule action start settings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "time",
                "Time",
                autoboto.TypeInfo(str),
            ),
        ]

    # Fixed timestamp action start. Conforms to ISO-8601.
    time: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ForbiddenException(autoboto.ShapeBase):
    """
    Placeholder documentation for ForbiddenException
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

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GatewayTimeoutException(autoboto.ShapeBase):
    """
    Placeholder documentation for GatewayTimeoutException
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

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GlobalConfiguration(autoboto.ShapeBase):
    """
    Placeholder documentation for GlobalConfiguration
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "initial_audio_gain",
                "InitialAudioGain",
                autoboto.TypeInfo(int),
            ),
            (
                "input_end_action",
                "InputEndAction",
                autoboto.TypeInfo(GlobalConfigurationInputEndAction),
            ),
            (
                "input_loss_behavior",
                "InputLossBehavior",
                autoboto.TypeInfo(InputLossBehavior),
            ),
            (
                "output_timing_source",
                "OutputTimingSource",
                autoboto.TypeInfo(GlobalConfigurationOutputTimingSource),
            ),
            (
                "support_low_framerate_inputs",
                "SupportLowFramerateInputs",
                autoboto.TypeInfo(GlobalConfigurationLowFramerateInputs),
            ),
        ]

    # Value to set the initial audio gain for the Live Event.
    initial_audio_gain: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates the action to take when an input completes (e.g. end-of-file.)
    # Options include immediately switching to the next sequential input (via
    # "switchInput"), switching to the next input and looping back to the first
    # input when last input ends (via "switchAndLoopInputs") or not switching
    # inputs and instead transcoding black / color / slate images per the "Input
    # Loss Behavior" configuration until an activateInput REST command is
    # received (via "none").
    input_end_action: "GlobalConfigurationInputEndAction" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Settings for system actions when input is lost.
    input_loss_behavior: "InputLossBehavior" = dataclasses.field(
        default_factory=dict,
    )

    # Indicates whether the rate of frames emitted by the Live encoder should be
    # paced by its system clock (which optionally may be locked to another source
    # via NTP) or should be locked to the clock of the source that is providing
    # the input stream.
    output_timing_source: "GlobalConfigurationOutputTimingSource" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Adjusts video input buffer for streams with very low video framerates. This
    # is commonly set to enabled for music channels with less than one video
    # frame per second.
    support_low_framerate_inputs: "GlobalConfigurationLowFramerateInputs" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class GlobalConfigurationInputEndAction(Enum):
    """
    Placeholder documentation for GlobalConfigurationInputEndAction
    """
    NONE = "NONE"
    SWITCH_AND_LOOP_INPUTS = "SWITCH_AND_LOOP_INPUTS"


class GlobalConfigurationLowFramerateInputs(Enum):
    """
    Placeholder documentation for GlobalConfigurationLowFramerateInputs
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class GlobalConfigurationOutputTimingSource(Enum):
    """
    Placeholder documentation for GlobalConfigurationOutputTimingSource
    """
    INPUT_CLOCK = "INPUT_CLOCK"
    SYSTEM_CLOCK = "SYSTEM_CLOCK"


class H264AdaptiveQuantization(Enum):
    """
    Placeholder documentation for H264AdaptiveQuantization
    """
    HIGH = "HIGH"
    HIGHER = "HIGHER"
    LOW = "LOW"
    MAX = "MAX"
    MEDIUM = "MEDIUM"
    OFF = "OFF"


class H264ColorMetadata(Enum):
    """
    Placeholder documentation for H264ColorMetadata
    """
    IGNORE = "IGNORE"
    INSERT = "INSERT"


class H264EntropyEncoding(Enum):
    """
    Placeholder documentation for H264EntropyEncoding
    """
    CABAC = "CABAC"
    CAVLC = "CAVLC"


class H264FlickerAq(Enum):
    """
    Placeholder documentation for H264FlickerAq
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264FramerateControl(Enum):
    """
    Placeholder documentation for H264FramerateControl
    """
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H264GopBReference(Enum):
    """
    Placeholder documentation for H264GopBReference
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264GopSizeUnits(Enum):
    """
    Placeholder documentation for H264GopSizeUnits
    """
    FRAMES = "FRAMES"
    SECONDS = "SECONDS"


class H264Level(Enum):
    """
    Placeholder documentation for H264Level
    """
    H264_LEVEL_1 = "H264_LEVEL_1"
    H264_LEVEL_1_1 = "H264_LEVEL_1_1"
    H264_LEVEL_1_2 = "H264_LEVEL_1_2"
    H264_LEVEL_1_3 = "H264_LEVEL_1_3"
    H264_LEVEL_2 = "H264_LEVEL_2"
    H264_LEVEL_2_1 = "H264_LEVEL_2_1"
    H264_LEVEL_2_2 = "H264_LEVEL_2_2"
    H264_LEVEL_3 = "H264_LEVEL_3"
    H264_LEVEL_3_1 = "H264_LEVEL_3_1"
    H264_LEVEL_3_2 = "H264_LEVEL_3_2"
    H264_LEVEL_4 = "H264_LEVEL_4"
    H264_LEVEL_4_1 = "H264_LEVEL_4_1"
    H264_LEVEL_4_2 = "H264_LEVEL_4_2"
    H264_LEVEL_5 = "H264_LEVEL_5"
    H264_LEVEL_5_1 = "H264_LEVEL_5_1"
    H264_LEVEL_5_2 = "H264_LEVEL_5_2"
    H264_LEVEL_AUTO = "H264_LEVEL_AUTO"


class H264LookAheadRateControl(Enum):
    """
    Placeholder documentation for H264LookAheadRateControl
    """
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"


class H264ParControl(Enum):
    """
    Placeholder documentation for H264ParControl
    """
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H264Profile(Enum):
    """
    Placeholder documentation for H264Profile
    """
    BASELINE = "BASELINE"
    HIGH = "HIGH"
    HIGH_10BIT = "HIGH_10BIT"
    HIGH_422 = "HIGH_422"
    HIGH_422_10BIT = "HIGH_422_10BIT"
    MAIN = "MAIN"


class H264RateControlMode(Enum):
    """
    Placeholder documentation for H264RateControlMode
    """
    CBR = "CBR"
    VBR = "VBR"


class H264ScanType(Enum):
    """
    Placeholder documentation for H264ScanType
    """
    INTERLACED = "INTERLACED"
    PROGRESSIVE = "PROGRESSIVE"


class H264SceneChangeDetect(Enum):
    """
    Placeholder documentation for H264SceneChangeDetect
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


@dataclasses.dataclass
class H264Settings(autoboto.ShapeBase):
    """
    Placeholder documentation for H264Settings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "adaptive_quantization",
                "AdaptiveQuantization",
                autoboto.TypeInfo(H264AdaptiveQuantization),
            ),
            (
                "afd_signaling",
                "AfdSignaling",
                autoboto.TypeInfo(AfdSignaling),
            ),
            (
                "bitrate",
                "Bitrate",
                autoboto.TypeInfo(int),
            ),
            (
                "buf_fill_pct",
                "BufFillPct",
                autoboto.TypeInfo(int),
            ),
            (
                "buf_size",
                "BufSize",
                autoboto.TypeInfo(int),
            ),
            (
                "color_metadata",
                "ColorMetadata",
                autoboto.TypeInfo(H264ColorMetadata),
            ),
            (
                "entropy_encoding",
                "EntropyEncoding",
                autoboto.TypeInfo(H264EntropyEncoding),
            ),
            (
                "fixed_afd",
                "FixedAfd",
                autoboto.TypeInfo(FixedAfd),
            ),
            (
                "flicker_aq",
                "FlickerAq",
                autoboto.TypeInfo(H264FlickerAq),
            ),
            (
                "framerate_control",
                "FramerateControl",
                autoboto.TypeInfo(H264FramerateControl),
            ),
            (
                "framerate_denominator",
                "FramerateDenominator",
                autoboto.TypeInfo(int),
            ),
            (
                "framerate_numerator",
                "FramerateNumerator",
                autoboto.TypeInfo(int),
            ),
            (
                "gop_b_reference",
                "GopBReference",
                autoboto.TypeInfo(H264GopBReference),
            ),
            (
                "gop_closed_cadence",
                "GopClosedCadence",
                autoboto.TypeInfo(int),
            ),
            (
                "gop_num_b_frames",
                "GopNumBFrames",
                autoboto.TypeInfo(int),
            ),
            (
                "gop_size",
                "GopSize",
                autoboto.TypeInfo(float),
            ),
            (
                "gop_size_units",
                "GopSizeUnits",
                autoboto.TypeInfo(H264GopSizeUnits),
            ),
            (
                "level",
                "Level",
                autoboto.TypeInfo(H264Level),
            ),
            (
                "look_ahead_rate_control",
                "LookAheadRateControl",
                autoboto.TypeInfo(H264LookAheadRateControl),
            ),
            (
                "max_bitrate",
                "MaxBitrate",
                autoboto.TypeInfo(int),
            ),
            (
                "min_i_interval",
                "MinIInterval",
                autoboto.TypeInfo(int),
            ),
            (
                "num_ref_frames",
                "NumRefFrames",
                autoboto.TypeInfo(int),
            ),
            (
                "par_control",
                "ParControl",
                autoboto.TypeInfo(H264ParControl),
            ),
            (
                "par_denominator",
                "ParDenominator",
                autoboto.TypeInfo(int),
            ),
            (
                "par_numerator",
                "ParNumerator",
                autoboto.TypeInfo(int),
            ),
            (
                "profile",
                "Profile",
                autoboto.TypeInfo(H264Profile),
            ),
            (
                "rate_control_mode",
                "RateControlMode",
                autoboto.TypeInfo(H264RateControlMode),
            ),
            (
                "scan_type",
                "ScanType",
                autoboto.TypeInfo(H264ScanType),
            ),
            (
                "scene_change_detect",
                "SceneChangeDetect",
                autoboto.TypeInfo(H264SceneChangeDetect),
            ),
            (
                "slices",
                "Slices",
                autoboto.TypeInfo(int),
            ),
            (
                "softness",
                "Softness",
                autoboto.TypeInfo(int),
            ),
            (
                "spatial_aq",
                "SpatialAq",
                autoboto.TypeInfo(H264SpatialAq),
            ),
            (
                "syntax",
                "Syntax",
                autoboto.TypeInfo(H264Syntax),
            ),
            (
                "temporal_aq",
                "TemporalAq",
                autoboto.TypeInfo(H264TemporalAq),
            ),
            (
                "timecode_insertion",
                "TimecodeInsertion",
                autoboto.TypeInfo(H264TimecodeInsertionBehavior),
            ),
        ]

    # Adaptive quantization. Allows intra-frame quantizers to vary to improve
    # visual quality.
    adaptive_quantization: "H264AdaptiveQuantization" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates that AFD values will be written into the output stream. If
    # afdSignaling is "auto", the system will try to preserve the input AFD value
    # (in cases where multiple AFD values are valid). If set to "fixed", the AFD
    # value will be the value configured in the fixedAfd parameter.
    afd_signaling: "AfdSignaling" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Average bitrate in bits/second. Required for VBR, CBR, and ABR. For MS
    # Smooth outputs, bitrates must be unique when rounded down to the nearest
    # multiple of 1000.
    bitrate: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Percentage of the buffer that should initially be filled (HRD buffer
    # model).
    buf_fill_pct: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Size of buffer (HRD buffer model) in bits/second.
    buf_size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Includes colorspace metadata in the output.
    color_metadata: "H264ColorMetadata" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Entropy encoding mode. Use cabac (must be in Main or High profile) or
    # cavlc.
    entropy_encoding: "H264EntropyEncoding" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Four bit AFD value to write on all frames of video in the output stream.
    # Only valid when afdSignaling is set to 'Fixed'.
    fixed_afd: "FixedAfd" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If set to enabled, adjust quantization within each frame to reduce flicker
    # or 'pop' on I-frames.
    flicker_aq: "H264FlickerAq" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This field indicates how the output video frame rate is specified. If
    # "specified" is selected then the output video frame rate is determined by
    # framerateNumerator and framerateDenominator, else if "initializeFromSource"
    # is selected then the output video frame rate will be set equal to the input
    # video frame rate of the first input.
    framerate_control: "H264FramerateControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Framerate denominator.
    framerate_denominator: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976
    # fps.
    framerate_numerator: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Documentation update needed
    gop_b_reference: "H264GopBReference" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Frequency of closed GOPs. In streaming applications, it is recommended that
    # this be set to 1 so a decoder joining mid-stream will receive an IDR frame
    # as quickly as possible. Setting this value to 0 will break output
    # segmenting.
    gop_closed_cadence: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Number of B-frames between reference frames.
    gop_num_b_frames: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # GOP size (keyframe interval) in units of either frames or seconds per
    # gopSizeUnits. Must be greater than zero.
    gop_size: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates if the gopSize is specified in frames or seconds. If seconds the
    # system will convert the gopSize into a frame count at run time.
    gop_size_units: "H264GopSizeUnits" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # H.264 Level.
    level: "H264Level" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amount of lookahead. A value of low can decrease latency and memory usage,
    # while high can produce better quality for certain content.
    look_ahead_rate_control: "H264LookAheadRateControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Maximum bitrate in bits/second (for VBR mode only).
    max_bitrate: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Only meaningful if sceneChangeDetect is set to enabled. Enforces separation
    # between repeated (cadence) I-frames and I-frames inserted by Scene Change
    # Detection. If a scene change I-frame is within I-interval frames of a
    # cadence I-frame, the GOP is shrunk and/or stretched to the scene change
    # I-frame. GOP stretch requires enabling lookahead as well as setting
    # I-interval. The normal cadence resumes for the next GOP. Note: Maximum GOP
    # stretch = GOP size + Min-I-interval - 1
    min_i_interval: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Number of reference frames to use. The encoder may use more than requested
    # if using B-frames and/or interlaced encoding.
    num_ref_frames: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This field indicates how the output pixel aspect ratio is specified. If
    # "specified" is selected then the output video pixel aspect ratio is
    # determined by parNumerator and parDenominator, else if
    # "initializeFromSource" is selected then the output pixsel aspect ratio will
    # be set equal to the input video pixel aspect ratio of the first input.
    par_control: "H264ParControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Pixel Aspect Ratio denominator.
    par_denominator: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Pixel Aspect Ratio numerator.
    par_numerator: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # H.264 Profile.
    profile: "H264Profile" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Rate control mode.
    rate_control_mode: "H264RateControlMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Sets the scan type of the output to progressive or top-field-first
    # interlaced.
    scan_type: "H264ScanType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Scene change detection. Inserts I-frames on scene changes when enabled.
    scene_change_detect: "H264SceneChangeDetect" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Number of slices per picture. Must be less than or equal to the number of
    # macroblock rows for progressive pictures, and less than or equal to half
    # the number of macroblock rows for interlaced pictures. This field is
    # optional; when no value is specified the encoder will choose the number of
    # slices based on encode resolution.
    slices: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Softness. Selects quantizer matrix, larger values reduce high-frequency
    # content in the encoded image.
    softness: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If set to enabled, adjust quantization within each frame based on spatial
    # variation of content complexity.
    spatial_aq: "H264SpatialAq" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Produces a bitstream compliant with SMPTE RP-2027.
    syntax: "H264Syntax" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If set to enabled, adjust quantization within each frame based on temporal
    # variation of content complexity.
    temporal_aq: "H264TemporalAq" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Determines how timecodes should be inserted into the video elementary
    # stream. \- 'disabled': Do not include timecodes \- 'picTimingSei': Pass
    # through picture timing SEI messages from the source specified in Timecode
    # Config
    timecode_insertion: "H264TimecodeInsertionBehavior" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class H264SpatialAq(Enum):
    """
    Placeholder documentation for H264SpatialAq
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264Syntax(Enum):
    """
    Placeholder documentation for H264Syntax
    """
    DEFAULT = "DEFAULT"
    RP2027 = "RP2027"


class H264TemporalAq(Enum):
    """
    Placeholder documentation for H264TemporalAq
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264TimecodeInsertionBehavior(Enum):
    """
    Placeholder documentation for H264TimecodeInsertionBehavior
    """
    DISABLED = "DISABLED"
    PIC_TIMING_SEI = "PIC_TIMING_SEI"


class HlsAdMarkers(Enum):
    """
    Placeholder documentation for HlsAdMarkers
    """
    ADOBE = "ADOBE"
    ELEMENTAL = "ELEMENTAL"
    ELEMENTAL_SCTE35 = "ELEMENTAL_SCTE35"


class HlsAkamaiHttpTransferMode(Enum):
    """
    Placeholder documentation for HlsAkamaiHttpTransferMode
    """
    CHUNKED = "CHUNKED"
    NON_CHUNKED = "NON_CHUNKED"


@dataclasses.dataclass
class HlsAkamaiSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for HlsAkamaiSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_retry_interval",
                "ConnectionRetryInterval",
                autoboto.TypeInfo(int),
            ),
            (
                "filecache_duration",
                "FilecacheDuration",
                autoboto.TypeInfo(int),
            ),
            (
                "http_transfer_mode",
                "HttpTransferMode",
                autoboto.TypeInfo(HlsAkamaiHttpTransferMode),
            ),
            (
                "num_retries",
                "NumRetries",
                autoboto.TypeInfo(int),
            ),
            (
                "restart_delay",
                "RestartDelay",
                autoboto.TypeInfo(int),
            ),
            (
                "salt",
                "Salt",
                autoboto.TypeInfo(str),
            ),
            (
                "token",
                "Token",
                autoboto.TypeInfo(str),
            ),
        ]

    # Number of seconds to wait before retrying connection to the CDN if the
    # connection is lost.
    connection_retry_interval: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Size in seconds of file cache for streaming outputs.
    filecache_duration: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specify whether or not to use chunked transfer encoding to Akamai. User
    # should contact Akamai to enable this feature.
    http_transfer_mode: "HlsAkamaiHttpTransferMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Number of retry attempts that will be made before the Live Event is put
    # into an error state.
    num_retries: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If a streaming output fails, number of seconds to wait until a restart is
    # initiated. A value of 0 means never restart.
    restart_delay: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Salt for authenticated Akamai.
    salt: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Token parameter for authenticated akamai. If not specified, _gda_ is used.
    token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HlsBasicPutSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for HlsBasicPutSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_retry_interval",
                "ConnectionRetryInterval",
                autoboto.TypeInfo(int),
            ),
            (
                "filecache_duration",
                "FilecacheDuration",
                autoboto.TypeInfo(int),
            ),
            (
                "num_retries",
                "NumRetries",
                autoboto.TypeInfo(int),
            ),
            (
                "restart_delay",
                "RestartDelay",
                autoboto.TypeInfo(int),
            ),
        ]

    # Number of seconds to wait before retrying connection to the CDN if the
    # connection is lost.
    connection_retry_interval: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Size in seconds of file cache for streaming outputs.
    filecache_duration: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Number of retry attempts that will be made before the Live Event is put
    # into an error state.
    num_retries: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If a streaming output fails, number of seconds to wait until a restart is
    # initiated. A value of 0 means never restart.
    restart_delay: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class HlsCaptionLanguageSetting(Enum):
    """
    Placeholder documentation for HlsCaptionLanguageSetting
    """
    INSERT = "INSERT"
    NONE = "NONE"
    OMIT = "OMIT"


@dataclasses.dataclass
class HlsCdnSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for HlsCdnSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hls_akamai_settings",
                "HlsAkamaiSettings",
                autoboto.TypeInfo(HlsAkamaiSettings),
            ),
            (
                "hls_basic_put_settings",
                "HlsBasicPutSettings",
                autoboto.TypeInfo(HlsBasicPutSettings),
            ),
            (
                "hls_media_store_settings",
                "HlsMediaStoreSettings",
                autoboto.TypeInfo(HlsMediaStoreSettings),
            ),
            (
                "hls_webdav_settings",
                "HlsWebdavSettings",
                autoboto.TypeInfo(HlsWebdavSettings),
            ),
        ]

    # Placeholder documentation for HlsAkamaiSettings
    hls_akamai_settings: "HlsAkamaiSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for HlsBasicPutSettings
    hls_basic_put_settings: "HlsBasicPutSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for HlsMediaStoreSettings
    hls_media_store_settings: "HlsMediaStoreSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for HlsWebdavSettings
    hls_webdav_settings: "HlsWebdavSettings" = dataclasses.field(
        default_factory=dict,
    )


class HlsClientCache(Enum):
    """
    Placeholder documentation for HlsClientCache
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class HlsCodecSpecification(Enum):
    """
    Placeholder documentation for HlsCodecSpecification
    """
    RFC_4281 = "RFC_4281"
    RFC_6381 = "RFC_6381"


class HlsDirectoryStructure(Enum):
    """
    Placeholder documentation for HlsDirectoryStructure
    """
    SINGLE_DIRECTORY = "SINGLE_DIRECTORY"
    SUBDIRECTORY_PER_STREAM = "SUBDIRECTORY_PER_STREAM"


class HlsEncryptionType(Enum):
    """
    Placeholder documentation for HlsEncryptionType
    """
    AES128 = "AES128"
    SAMPLE_AES = "SAMPLE_AES"


@dataclasses.dataclass
class HlsGroupSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for HlsGroupSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination",
                "Destination",
                autoboto.TypeInfo(OutputLocationRef),
            ),
            (
                "ad_markers",
                "AdMarkers",
                autoboto.TypeInfo(typing.List[HlsAdMarkers]),
            ),
            (
                "base_url_content",
                "BaseUrlContent",
                autoboto.TypeInfo(str),
            ),
            (
                "base_url_manifest",
                "BaseUrlManifest",
                autoboto.TypeInfo(str),
            ),
            (
                "caption_language_mappings",
                "CaptionLanguageMappings",
                autoboto.TypeInfo(typing.List[CaptionLanguageMapping]),
            ),
            (
                "caption_language_setting",
                "CaptionLanguageSetting",
                autoboto.TypeInfo(HlsCaptionLanguageSetting),
            ),
            (
                "client_cache",
                "ClientCache",
                autoboto.TypeInfo(HlsClientCache),
            ),
            (
                "codec_specification",
                "CodecSpecification",
                autoboto.TypeInfo(HlsCodecSpecification),
            ),
            (
                "constant_iv",
                "ConstantIv",
                autoboto.TypeInfo(str),
            ),
            (
                "directory_structure",
                "DirectoryStructure",
                autoboto.TypeInfo(HlsDirectoryStructure),
            ),
            (
                "encryption_type",
                "EncryptionType",
                autoboto.TypeInfo(HlsEncryptionType),
            ),
            (
                "hls_cdn_settings",
                "HlsCdnSettings",
                autoboto.TypeInfo(HlsCdnSettings),
            ),
            (
                "index_n_segments",
                "IndexNSegments",
                autoboto.TypeInfo(int),
            ),
            (
                "input_loss_action",
                "InputLossAction",
                autoboto.TypeInfo(InputLossActionForHlsOut),
            ),
            (
                "iv_in_manifest",
                "IvInManifest",
                autoboto.TypeInfo(HlsIvInManifest),
            ),
            (
                "iv_source",
                "IvSource",
                autoboto.TypeInfo(HlsIvSource),
            ),
            (
                "keep_segments",
                "KeepSegments",
                autoboto.TypeInfo(int),
            ),
            (
                "key_format",
                "KeyFormat",
                autoboto.TypeInfo(str),
            ),
            (
                "key_format_versions",
                "KeyFormatVersions",
                autoboto.TypeInfo(str),
            ),
            (
                "key_provider_settings",
                "KeyProviderSettings",
                autoboto.TypeInfo(KeyProviderSettings),
            ),
            (
                "manifest_compression",
                "ManifestCompression",
                autoboto.TypeInfo(HlsManifestCompression),
            ),
            (
                "manifest_duration_format",
                "ManifestDurationFormat",
                autoboto.TypeInfo(HlsManifestDurationFormat),
            ),
            (
                "min_segment_length",
                "MinSegmentLength",
                autoboto.TypeInfo(int),
            ),
            (
                "mode",
                "Mode",
                autoboto.TypeInfo(HlsMode),
            ),
            (
                "output_selection",
                "OutputSelection",
                autoboto.TypeInfo(HlsOutputSelection),
            ),
            (
                "program_date_time",
                "ProgramDateTime",
                autoboto.TypeInfo(HlsProgramDateTime),
            ),
            (
                "program_date_time_period",
                "ProgramDateTimePeriod",
                autoboto.TypeInfo(int),
            ),
            (
                "segment_length",
                "SegmentLength",
                autoboto.TypeInfo(int),
            ),
            (
                "segmentation_mode",
                "SegmentationMode",
                autoboto.TypeInfo(HlsSegmentationMode),
            ),
            (
                "segments_per_subdirectory",
                "SegmentsPerSubdirectory",
                autoboto.TypeInfo(int),
            ),
            (
                "stream_inf_resolution",
                "StreamInfResolution",
                autoboto.TypeInfo(HlsStreamInfResolution),
            ),
            (
                "timed_metadata_id3_frame",
                "TimedMetadataId3Frame",
                autoboto.TypeInfo(HlsTimedMetadataId3Frame),
            ),
            (
                "timed_metadata_id3_period",
                "TimedMetadataId3Period",
                autoboto.TypeInfo(int),
            ),
            (
                "timestamp_delta_milliseconds",
                "TimestampDeltaMilliseconds",
                autoboto.TypeInfo(int),
            ),
            (
                "ts_file_mode",
                "TsFileMode",
                autoboto.TypeInfo(HlsTsFileMode),
            ),
        ]

    # A directory or HTTP destination for the HLS segments, manifest files, and
    # encryption keys (if enabled).
    destination: "OutputLocationRef" = dataclasses.field(default_factory=dict, )

    # Choose one or more ad marker types to pass SCTE35 signals through to this
    # group of Apple HLS outputs.
    ad_markers: typing.List["HlsAdMarkers"] = dataclasses.field(
        default_factory=list,
    )

    # A partial URI prefix that will be prepended to each output in the media
    # .m3u8 file. Can be used if base manifest is delivered from a different URL
    # than the main .m3u8 file.
    base_url_content: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A partial URI prefix that will be prepended to each output in the media
    # .m3u8 file. Can be used if base manifest is delivered from a different URL
    # than the main .m3u8 file.
    base_url_manifest: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Mapping of up to 4 caption channels to caption languages. Is only
    # meaningful if captionLanguageSetting is set to "insert".
    caption_language_mappings: typing.List["CaptionLanguageMapping"
                                          ] = dataclasses.field(
                                              default_factory=list,
                                          )

    # Applies only to 608 Embedded output captions. insert: Include CLOSED-
    # CAPTIONS lines in the manifest. Specify at least one language in the CC1
    # Language Code field. One CLOSED-CAPTION line is added for each Language
    # Code you specify. Make sure to specify the languages in the order in which
    # they appear in the original source (if the source is embedded format) or
    # the order of the caption selectors (if the source is other than embedded).
    # Otherwise, languages in the manifest will not match up properly with the
    # output captions. none: Include CLOSED-CAPTIONS=NONE line in the manifest.
    # omit: Omit any CLOSED-CAPTIONS line from the manifest.
    caption_language_setting: "HlsCaptionLanguageSetting" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to "disabled", sets the #EXT-X-ALLOW-CACHE:no tag in the manifest,
    # which prevents clients from saving media segments for later replay.
    client_cache: "HlsClientCache" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specification to use (RFC-6381 or the default RFC-4281) during m3u8
    # playlist generation.
    codec_specification: "HlsCodecSpecification" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # For use with encryptionType. This is a 128-bit, 16-byte hex value
    # represented by a 32-character text string. If ivSource is set to "explicit"
    # then this parameter is required and is used as the IV for encryption.
    constant_iv: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Place segments in subdirectories.
    directory_structure: "HlsDirectoryStructure" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Encrypts the segments with the given encryption scheme. Exclude this
    # parameter if no encryption is desired.
    encryption_type: "HlsEncryptionType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Parameters that control interactions with the CDN.
    hls_cdn_settings: "HlsCdnSettings" = dataclasses.field(
        default_factory=dict,
    )

    # If mode is "live", the number of segments to retain in the manifest (.m3u8)
    # file. This number must be less than or equal to keepSegments. If mode is
    # "vod", this parameter has no effect.
    index_n_segments: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Parameter that control output group behavior on input loss.
    input_loss_action: "InputLossActionForHlsOut" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # For use with encryptionType. The IV (Initialization Vector) is a 128-bit
    # number used in conjunction with the key for encrypting blocks. If set to
    # "include", IV is listed in the manifest, otherwise the IV is not in the
    # manifest.
    iv_in_manifest: "HlsIvInManifest" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # For use with encryptionType. The IV (Initialization Vector) is a 128-bit
    # number used in conjunction with the key for encrypting blocks. If this
    # setting is "followsSegmentNumber", it will cause the IV to change every
    # segment (to match the segment number). If this is set to "explicit", you
    # must enter a constantIv value.
    iv_source: "HlsIvSource" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If mode is "live", the number of TS segments to retain in the destination
    # directory. If mode is "vod", this parameter has no effect.
    keep_segments: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value specifies how the key is represented in the resource identified
    # by the URI. If parameter is absent, an implicit value of "identity" is
    # used. A reverse DNS string can also be given.
    key_format: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Either a single positive integer version value or a slash delimited list of
    # version values (1/2/3).
    key_format_versions: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The key provider settings.
    key_provider_settings: "KeyProviderSettings" = dataclasses.field(
        default_factory=dict,
    )

    # When set to gzip, compresses HLS playlist.
    manifest_compression: "HlsManifestCompression" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the output manifest should use floating point or integer
    # values for segment duration.
    manifest_duration_format: "HlsManifestDurationFormat" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set, minimumSegmentLength is enforced by looking ahead and back within
    # the specified range for a nearby avail and extending the segment size if
    # needed.
    min_segment_length: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If "vod", all segments are indexed and kept permanently in the destination
    # and manifest. If "live", only the number segments specified in keepSegments
    # and indexNSegments are kept; newer segments replace older segments, which
    # may prevent players from rewinding all the way to the beginning of the
    # event. VOD mode uses HLS EXT-X-PLAYLIST-TYPE of EVENT while the channel is
    # running, converting it to a "VOD" type manifest on completion of the
    # stream.
    mode: "HlsMode" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Generates the .m3u8 playlist file for this HLS output group. The
    # segmentsOnly option will output segments without the .m3u8 file.
    output_selection: "HlsOutputSelection" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files.
    # The value is calculated as follows: either the program date and time are
    # initialized using the input timecode source, or the time is initialized
    # using the input timecode source and the date is initialized using the
    # timestampOffset.
    program_date_time: "HlsProgramDateTime" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Period of insertion of EXT-X-PROGRAM-DATE-TIME entry, in seconds.
    program_date_time_period: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Length of MPEG-2 Transport Stream segments to create (in seconds). Note
    # that segments will end on the next keyframe after this number of seconds,
    # so actual segment length may be longer.
    segment_length: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to useInputSegmentation, the output segment or fragment points are
    # set by the RAI markers from the input streams.
    segmentation_mode: "HlsSegmentationMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Number of segments to write to a subdirectory before starting a new one.
    # directoryStructure must be subdirectoryPerStream for this setting to have
    # an effect.
    segments_per_subdirectory: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag
    # of variant manifest.
    stream_inf_resolution: "HlsStreamInfResolution" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates ID3 frame that has the timecode.
    timed_metadata_id3_frame: "HlsTimedMetadataId3Frame" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Timed Metadata interval in seconds.
    timed_metadata_id3_period: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides an extra millisecond delta offset to fine tune the timestamps.
    timestamp_delta_milliseconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to "singleFile", emits the program as a single media resource
    # (.ts) file, and uses #EXT-X-BYTERANGE tags to index segment for playback.
    # Playback of VOD mode content during event is not guaranteed due to HTTP
    # server caching.
    ts_file_mode: "HlsTsFileMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class HlsInputSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for HlsInputSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bandwidth",
                "Bandwidth",
                autoboto.TypeInfo(int),
            ),
            (
                "buffer_segments",
                "BufferSegments",
                autoboto.TypeInfo(int),
            ),
            (
                "retries",
                "Retries",
                autoboto.TypeInfo(int),
            ),
            (
                "retry_interval",
                "RetryInterval",
                autoboto.TypeInfo(int),
            ),
        ]

    # When specified the HLS stream with the m3u8 BANDWIDTH that most closely
    # matches this value will be chosen, otherwise the highest bandwidth stream
    # in the m3u8 will be chosen. The bitrate is specified in bits per second, as
    # in an HLS manifest.
    bandwidth: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When specified, reading of the HLS input will begin this many buffer
    # segments from the end (most recently written segment). When not specified,
    # the HLS input will begin with the first segment specified in the m3u8.
    buffer_segments: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of consecutive times that attempts to read a manifest or segment
    # must fail before the input is considered unavailable.
    retries: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of seconds between retries when an attempt to read a manifest or
    # segment fails.
    retry_interval: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class HlsIvInManifest(Enum):
    """
    Placeholder documentation for HlsIvInManifest
    """
    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"


class HlsIvSource(Enum):
    """
    Placeholder documentation for HlsIvSource
    """
    EXPLICIT = "EXPLICIT"
    FOLLOWS_SEGMENT_NUMBER = "FOLLOWS_SEGMENT_NUMBER"


class HlsManifestCompression(Enum):
    """
    Placeholder documentation for HlsManifestCompression
    """
    GZIP = "GZIP"
    NONE = "NONE"


class HlsManifestDurationFormat(Enum):
    """
    Placeholder documentation for HlsManifestDurationFormat
    """
    FLOATING_POINT = "FLOATING_POINT"
    INTEGER = "INTEGER"


@dataclasses.dataclass
class HlsMediaStoreSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for HlsMediaStoreSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_retry_interval",
                "ConnectionRetryInterval",
                autoboto.TypeInfo(int),
            ),
            (
                "filecache_duration",
                "FilecacheDuration",
                autoboto.TypeInfo(int),
            ),
            (
                "media_store_storage_class",
                "MediaStoreStorageClass",
                autoboto.TypeInfo(HlsMediaStoreStorageClass),
            ),
            (
                "num_retries",
                "NumRetries",
                autoboto.TypeInfo(int),
            ),
            (
                "restart_delay",
                "RestartDelay",
                autoboto.TypeInfo(int),
            ),
        ]

    # Number of seconds to wait before retrying connection to the CDN if the
    # connection is lost.
    connection_retry_interval: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Size in seconds of file cache for streaming outputs.
    filecache_duration: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to temporal, output files are stored in non-persistent memory for
    # faster reading and writing.
    media_store_storage_class: "HlsMediaStoreStorageClass" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Number of retry attempts that will be made before the Live Event is put
    # into an error state.
    num_retries: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If a streaming output fails, number of seconds to wait until a restart is
    # initiated. A value of 0 means never restart.
    restart_delay: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class HlsMediaStoreStorageClass(Enum):
    """
    Placeholder documentation for HlsMediaStoreStorageClass
    """
    TEMPORAL = "TEMPORAL"


class HlsMode(Enum):
    """
    Placeholder documentation for HlsMode
    """
    LIVE = "LIVE"
    VOD = "VOD"


class HlsOutputSelection(Enum):
    """
    Placeholder documentation for HlsOutputSelection
    """
    MANIFESTS_AND_SEGMENTS = "MANIFESTS_AND_SEGMENTS"
    SEGMENTS_ONLY = "SEGMENTS_ONLY"


@dataclasses.dataclass
class HlsOutputSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for HlsOutputSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hls_settings",
                "HlsSettings",
                autoboto.TypeInfo(HlsSettings),
            ),
            (
                "name_modifier",
                "NameModifier",
                autoboto.TypeInfo(str),
            ),
            (
                "segment_modifier",
                "SegmentModifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # Settings regarding the underlying stream. These settings are different for
    # audio-only outputs.
    hls_settings: "HlsSettings" = dataclasses.field(default_factory=dict, )

    # String concatenated to the end of the destination filename. Accepts
    # \"Format Identifiers\":#formatIdentifierParameters.
    name_modifier: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # String concatenated to end of segment filenames.
    segment_modifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class HlsProgramDateTime(Enum):
    """
    Placeholder documentation for HlsProgramDateTime
    """
    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"


class HlsSegmentationMode(Enum):
    """
    Placeholder documentation for HlsSegmentationMode
    """
    USE_INPUT_SEGMENTATION = "USE_INPUT_SEGMENTATION"
    USE_SEGMENT_DURATION = "USE_SEGMENT_DURATION"


@dataclasses.dataclass
class HlsSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for HlsSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_only_hls_settings",
                "AudioOnlyHlsSettings",
                autoboto.TypeInfo(AudioOnlyHlsSettings),
            ),
            (
                "standard_hls_settings",
                "StandardHlsSettings",
                autoboto.TypeInfo(StandardHlsSettings),
            ),
        ]

    # Placeholder documentation for AudioOnlyHlsSettings
    audio_only_hls_settings: "AudioOnlyHlsSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for StandardHlsSettings
    standard_hls_settings: "StandardHlsSettings" = dataclasses.field(
        default_factory=dict,
    )


class HlsStreamInfResolution(Enum):
    """
    Placeholder documentation for HlsStreamInfResolution
    """
    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"


class HlsTimedMetadataId3Frame(Enum):
    """
    Placeholder documentation for HlsTimedMetadataId3Frame
    """
    NONE = "NONE"
    PRIV = "PRIV"
    TDRL = "TDRL"


class HlsTsFileMode(Enum):
    """
    Placeholder documentation for HlsTsFileMode
    """
    SEGMENTED_FILES = "SEGMENTED_FILES"
    SINGLE_FILE = "SINGLE_FILE"


class HlsWebdavHttpTransferMode(Enum):
    """
    Placeholder documentation for HlsWebdavHttpTransferMode
    """
    CHUNKED = "CHUNKED"
    NON_CHUNKED = "NON_CHUNKED"


@dataclasses.dataclass
class HlsWebdavSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for HlsWebdavSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_retry_interval",
                "ConnectionRetryInterval",
                autoboto.TypeInfo(int),
            ),
            (
                "filecache_duration",
                "FilecacheDuration",
                autoboto.TypeInfo(int),
            ),
            (
                "http_transfer_mode",
                "HttpTransferMode",
                autoboto.TypeInfo(HlsWebdavHttpTransferMode),
            ),
            (
                "num_retries",
                "NumRetries",
                autoboto.TypeInfo(int),
            ),
            (
                "restart_delay",
                "RestartDelay",
                autoboto.TypeInfo(int),
            ),
        ]

    # Number of seconds to wait before retrying connection to the CDN if the
    # connection is lost.
    connection_retry_interval: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Size in seconds of file cache for streaming outputs.
    filecache_duration: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specify whether or not to use chunked transfer encoding to WebDAV.
    http_transfer_mode: "HlsWebdavHttpTransferMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Number of retry attempts that will be made before the Live Event is put
    # into an error state.
    num_retries: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If a streaming output fails, number of seconds to wait until a restart is
    # initiated. A value of 0 means never restart.
    restart_delay: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Input(autoboto.ShapeBase):
    """
    Placeholder documentation for Input
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
                "attached_channels",
                "AttachedChannels",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "destinations",
                "Destinations",
                autoboto.TypeInfo(typing.List[InputDestination]),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "security_groups",
                "SecurityGroups",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "sources",
                "Sources",
                autoboto.TypeInfo(typing.List[InputSource]),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(InputState),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(InputType),
            ),
        ]

    # The Unique ARN of the input (generated, immutable).
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of channel IDs that that input is attached to (currently an input
    # can only be attached to one channel).
    attached_channels: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list of the destinations of the input (PUSH-type).
    destinations: typing.List["InputDestination"] = dataclasses.field(
        default_factory=list,
    )

    # The generated ID of the input (unique for user account, immutable).
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user-assigned name (This is a mutable value).
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of IDs for all the security groups attached to the input.
    security_groups: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list of the sources of the input (PULL-type).
    sources: typing.List["InputSource"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for InputState
    state: "InputState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Placeholder documentation for InputType
    type: "InputType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InputAttachment(autoboto.ShapeBase):
    """
    Placeholder documentation for InputAttachment
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_id",
                "InputId",
                autoboto.TypeInfo(str),
            ),
            (
                "input_settings",
                "InputSettings",
                autoboto.TypeInfo(InputSettings),
            ),
        ]

    # The ID of the input
    input_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Settings of an input (caption selector, etc.)
    input_settings: "InputSettings" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class InputChannelLevel(autoboto.ShapeBase):
    """
    Placeholder documentation for InputChannelLevel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gain",
                "Gain",
                autoboto.TypeInfo(int),
            ),
            (
                "input_channel",
                "InputChannel",
                autoboto.TypeInfo(int),
            ),
        ]

    # Remixing value. Units are in dB and acceptable values are within the range
    # from -60 (mute) and 6 dB.
    gain: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The index of the input channel used as a source.
    input_channel: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class InputCodec(Enum):
    """
    codec in increasing order of complexity
    """
    MPEG2 = "MPEG2"
    AVC = "AVC"
    HEVC = "HEVC"


class InputDeblockFilter(Enum):
    """
    Placeholder documentation for InputDeblockFilter
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class InputDenoiseFilter(Enum):
    """
    Placeholder documentation for InputDenoiseFilter
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


@dataclasses.dataclass
class InputDestination(autoboto.ShapeBase):
    """
    The settings for a PUSH type input.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip",
                "Ip",
                autoboto.TypeInfo(str),
            ),
            (
                "port",
                "Port",
                autoboto.TypeInfo(str),
            ),
            (
                "url",
                "Url",
                autoboto.TypeInfo(str),
            ),
        ]

    # The system-generated static IP address of endpoint. It remains fixed for
    # the lifetime of the input.
    ip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The port number for the input.
    port: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This represents the endpoint that the customer stream will be pushed to.
    url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InputDestinationRequest(autoboto.ShapeBase):
    """
    Endpoint settings for a PUSH type input.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique name for the location the RTMP stream is being pushed to.
    stream_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class InputFilter(Enum):
    """
    Placeholder documentation for InputFilter
    """
    AUTO = "AUTO"
    DISABLED = "DISABLED"
    FORCED = "FORCED"


@dataclasses.dataclass
class InputLocation(autoboto.ShapeBase):
    """
    Placeholder documentation for InputLocation
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "uri",
                "Uri",
                autoboto.TypeInfo(str),
            ),
            (
                "password_param",
                "PasswordParam",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "Username",
                autoboto.TypeInfo(str),
            ),
        ]

    # Uniform Resource Identifier - This should be a path to a file accessible to
    # the Live system (eg. a http:// URI) depending on the output type. For
    # example, a RTMP destination should have a uri simliar to:
    # "rtmp://fmsserver/live".
    uri: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # key used to extract the password from EC2 Parameter store
    password_param: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Documentation update needed
    username: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class InputLossActionForHlsOut(Enum):
    """
    Placeholder documentation for InputLossActionForHlsOut
    """
    EMIT_OUTPUT = "EMIT_OUTPUT"
    PAUSE_OUTPUT = "PAUSE_OUTPUT"


class InputLossActionForMsSmoothOut(Enum):
    """
    Placeholder documentation for InputLossActionForMsSmoothOut
    """
    EMIT_OUTPUT = "EMIT_OUTPUT"
    PAUSE_OUTPUT = "PAUSE_OUTPUT"


class InputLossActionForUdpOut(Enum):
    """
    Placeholder documentation for InputLossActionForUdpOut
    """
    DROP_PROGRAM = "DROP_PROGRAM"
    DROP_TS = "DROP_TS"
    EMIT_PROGRAM = "EMIT_PROGRAM"


@dataclasses.dataclass
class InputLossBehavior(autoboto.ShapeBase):
    """
    Placeholder documentation for InputLossBehavior
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "black_frame_msec",
                "BlackFrameMsec",
                autoboto.TypeInfo(int),
            ),
            (
                "input_loss_image_color",
                "InputLossImageColor",
                autoboto.TypeInfo(str),
            ),
            (
                "input_loss_image_slate",
                "InputLossImageSlate",
                autoboto.TypeInfo(InputLocation),
            ),
            (
                "input_loss_image_type",
                "InputLossImageType",
                autoboto.TypeInfo(InputLossImageType),
            ),
            (
                "repeat_frame_msec",
                "RepeatFrameMsec",
                autoboto.TypeInfo(int),
            ),
        ]

    # Documentation update needed
    black_frame_msec: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When input loss image type is "color" this field specifies the color to
    # use. Value: 6 hex characters representing the values of RGB.
    input_loss_image_color: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When input loss image type is "slate" these fields specify the parameters
    # for accessing the slate.
    input_loss_image_slate: "InputLocation" = dataclasses.field(
        default_factory=dict,
    )

    # Indicates whether to substitute a solid color or a slate into the output
    # after input loss exceeds blackFrameMsec.
    input_loss_image_type: "InputLossImageType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Documentation update needed
    repeat_frame_msec: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class InputLossImageType(Enum):
    """
    Placeholder documentation for InputLossImageType
    """
    COLOR = "COLOR"
    SLATE = "SLATE"


class InputMaximumBitrate(Enum):
    """
    Maximum input bitrate in megabits per second. Bitrates up to 50 Mbps are
    supported currently.
    """
    MAX_10_MBPS = "MAX_10_MBPS"
    MAX_20_MBPS = "MAX_20_MBPS"
    MAX_50_MBPS = "MAX_50_MBPS"


class InputResolution(Enum):
    """
    Input resolution based on lines of vertical resolution in the input; SD is less
    than 720 lines, HD is 720 to 1080 lines, UHD is greater than 1080 lines
    """
    SD = "SD"
    HD = "HD"
    UHD = "UHD"


@dataclasses.dataclass
class InputSecurityGroup(autoboto.ShapeBase):
    """
    An Input Security Group
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
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "inputs",
                "Inputs",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(InputSecurityGroupState),
            ),
            (
                "whitelist_rules",
                "WhitelistRules",
                autoboto.TypeInfo(typing.List[InputWhitelistRule]),
            ),
        ]

    # Unique ARN of Input Security Group
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Id of the Input Security Group
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of inputs currently using this Input Security Group.
    inputs: typing.List[str] = dataclasses.field(default_factory=list, )

    # The current state of the Input Security Group.
    state: "InputSecurityGroupState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Whitelist rules and their sync status
    whitelist_rules: typing.List["InputWhitelistRule"] = dataclasses.field(
        default_factory=list,
    )


class InputSecurityGroupState(Enum):
    """
    Placeholder documentation for InputSecurityGroupState
    """
    IDLE = "IDLE"
    IN_USE = "IN_USE"
    UPDATING = "UPDATING"
    DELETED = "DELETED"


@dataclasses.dataclass
class InputSecurityGroupWhitelistRequest(autoboto.ShapeBase):
    """
    Request of IPv4 CIDR addresses to whitelist in a security group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "whitelist_rules",
                "WhitelistRules",
                autoboto.TypeInfo(typing.List[InputWhitelistRuleCidr]),
            ),
        ]

    # List of IPv4 CIDR addresses to whitelist
    whitelist_rules: typing.List["InputWhitelistRuleCidr"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class InputSettings(autoboto.ShapeBase):
    """
    Live Event input parameters. There can be multiple inputs in a single Live
    Event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_selectors",
                "AudioSelectors",
                autoboto.TypeInfo(typing.List[AudioSelector]),
            ),
            (
                "caption_selectors",
                "CaptionSelectors",
                autoboto.TypeInfo(typing.List[CaptionSelector]),
            ),
            (
                "deblock_filter",
                "DeblockFilter",
                autoboto.TypeInfo(InputDeblockFilter),
            ),
            (
                "denoise_filter",
                "DenoiseFilter",
                autoboto.TypeInfo(InputDenoiseFilter),
            ),
            (
                "filter_strength",
                "FilterStrength",
                autoboto.TypeInfo(int),
            ),
            (
                "input_filter",
                "InputFilter",
                autoboto.TypeInfo(InputFilter),
            ),
            (
                "network_input_settings",
                "NetworkInputSettings",
                autoboto.TypeInfo(NetworkInputSettings),
            ),
            (
                "source_end_behavior",
                "SourceEndBehavior",
                autoboto.TypeInfo(InputSourceEndBehavior),
            ),
            (
                "video_selector",
                "VideoSelector",
                autoboto.TypeInfo(VideoSelector),
            ),
        ]

    # Used to select the audio stream to decode for inputs that have multiple
    # available.
    audio_selectors: typing.List["AudioSelector"] = dataclasses.field(
        default_factory=list,
    )

    # Used to select the caption input to use for inputs that have multiple
    # available.
    caption_selectors: typing.List["CaptionSelector"] = dataclasses.field(
        default_factory=list,
    )

    # Enable or disable the deblock filter when filtering.
    deblock_filter: "InputDeblockFilter" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Enable or disable the denoise filter when filtering.
    denoise_filter: "InputDenoiseFilter" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Adjusts the magnitude of filtering from 1 (minimal) to 5 (strongest).
    filter_strength: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Turns on the filter for this input. MPEG-2 inputs have the deblocking
    # filter enabled by default. 1) auto - filtering will be applied depending on
    # input type/quality 2) disabled - no filtering will be applied to the input
    # 3) forced - filtering will be applied regardless of input type
    input_filter: "InputFilter" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Input settings.
    network_input_settings: "NetworkInputSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Loop input if it is a file. This allows a file input to be streamed
    # indefinitely.
    source_end_behavior: "InputSourceEndBehavior" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Informs which video elementary stream to decode for input types that have
    # multiple available.
    video_selector: "VideoSelector" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class InputSource(autoboto.ShapeBase):
    """
    The settings for a PULL type input.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "password_param",
                "PasswordParam",
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

    # The key used to extract the password from EC2 Parameter store.
    password_param: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This represents the customer's source URL where stream is pulled from.
    url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The username for the input source.
    username: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class InputSourceEndBehavior(Enum):
    """
    Placeholder documentation for InputSourceEndBehavior
    """
    CONTINUE = "CONTINUE"
    LOOP = "LOOP"


@dataclasses.dataclass
class InputSourceRequest(autoboto.ShapeBase):
    """
    Settings for for a PULL type input.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "password_param",
                "PasswordParam",
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

    # The key used to extract the password from EC2 Parameter store.
    password_param: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This represents the customer's source URL where stream is pulled from.
    url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The username for the input source.
    username: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InputSpecification(autoboto.ShapeBase):
    """
    Placeholder documentation for InputSpecification
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "codec",
                "Codec",
                autoboto.TypeInfo(InputCodec),
            ),
            (
                "maximum_bitrate",
                "MaximumBitrate",
                autoboto.TypeInfo(InputMaximumBitrate),
            ),
            (
                "resolution",
                "Resolution",
                autoboto.TypeInfo(InputResolution),
            ),
        ]

    # Input codec
    codec: "InputCodec" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Maximum input bitrate, categorized coarsely
    maximum_bitrate: "InputMaximumBitrate" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Input resolution, categorized coarsely
    resolution: "InputResolution" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class InputState(Enum):
    """
    Placeholder documentation for InputState
    """
    CREATING = "CREATING"
    DETACHED = "DETACHED"
    ATTACHED = "ATTACHED"
    DELETING = "DELETING"
    DELETED = "DELETED"


class InputType(Enum):
    """
    Placeholder documentation for InputType
    """
    UDP_PUSH = "UDP_PUSH"
    RTP_PUSH = "RTP_PUSH"
    RTMP_PUSH = "RTMP_PUSH"
    RTMP_PULL = "RTMP_PULL"
    URL_PULL = "URL_PULL"


@dataclasses.dataclass
class InputWhitelistRule(autoboto.ShapeBase):
    """
    Whitelist rule
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cidr",
                "Cidr",
                autoboto.TypeInfo(str),
            ),
        ]

    # The IPv4 CIDR that's whitelisted.
    cidr: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InputWhitelistRuleCidr(autoboto.ShapeBase):
    """
    An IPv4 CIDR to whitelist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cidr",
                "Cidr",
                autoboto.TypeInfo(str),
            ),
        ]

    # The IPv4 CIDR to whitelist.
    cidr: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServerErrorException(autoboto.ShapeBase):
    """
    Placeholder documentation for InternalServerErrorException
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

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServiceError(autoboto.ShapeBase):
    """
    Placeholder documentation for InternalServiceError
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

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for InvalidRequest
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

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KeyProviderSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for KeyProviderSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "static_key_settings",
                "StaticKeySettings",
                autoboto.TypeInfo(StaticKeySettings),
            ),
        ]

    # Placeholder documentation for StaticKeySettings
    static_key_settings: "StaticKeySettings" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class LimitExceeded(autoboto.ShapeBase):
    """
    Placeholder documentation for LimitExceeded
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

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListChannelsRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for ListChannelsRequest
    """

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

    # Placeholder documentation for MaxResults
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListChannelsResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for ListChannelsResponse
    """

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
                autoboto.TypeInfo(typing.List[ChannelSummary]),
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

    # Placeholder documentation for __listOfChannelSummary
    channels: typing.List["ChannelSummary"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListChannelsResultModel(autoboto.ShapeBase):
    """
    Placeholder documentation for ListChannelsResultModel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channels",
                "Channels",
                autoboto.TypeInfo(typing.List[ChannelSummary]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __listOfChannelSummary
    channels: typing.List["ChannelSummary"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInputSecurityGroupsRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for ListInputSecurityGroupsRequest
    """

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

    # Placeholder documentation for MaxResults
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInputSecurityGroupsResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for ListInputSecurityGroupsResponse
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "input_security_groups",
                "InputSecurityGroups",
                autoboto.TypeInfo(typing.List[InputSecurityGroup]),
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

    # List of input security groups
    input_security_groups: typing.List["InputSecurityGroup"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInputSecurityGroupsResultModel(autoboto.ShapeBase):
    """
    Result of input security group list request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_security_groups",
                "InputSecurityGroups",
                autoboto.TypeInfo(typing.List[InputSecurityGroup]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # List of input security groups
    input_security_groups: typing.List["InputSecurityGroup"
                                      ] = dataclasses.field(
                                          default_factory=list,
                                      )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInputsRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for ListInputsRequest
    """

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

    # Placeholder documentation for MaxResults
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInputsResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for ListInputsResponse
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "inputs",
                "Inputs",
                autoboto.TypeInfo(typing.List[Input]),
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

    # Placeholder documentation for __listOfInput
    inputs: typing.List["Input"] = dataclasses.field(default_factory=list, )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInputsResultModel(autoboto.ShapeBase):
    """
    Placeholder documentation for ListInputsResultModel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "inputs",
                "Inputs",
                autoboto.TypeInfo(typing.List[Input]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __listOfInput
    inputs: typing.List["Input"] = dataclasses.field(default_factory=list, )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOfferingsRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for ListOfferingsRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_configuration",
                "ChannelConfiguration",
                autoboto.TypeInfo(str),
            ),
            (
                "codec",
                "Codec",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "maximum_bitrate",
                "MaximumBitrate",
                autoboto.TypeInfo(str),
            ),
            (
                "maximum_framerate",
                "MaximumFramerate",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "resolution",
                "Resolution",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "special_feature",
                "SpecialFeature",
                autoboto.TypeInfo(str),
            ),
            (
                "video_quality",
                "VideoQuality",
                autoboto.TypeInfo(str),
            ),
        ]

    # Filter to offerings that match the configuration of an existing channel,
    # e.g. '2345678' (a channel ID)
    channel_configuration: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Filter by codec, 'AVC', 'HEVC', 'MPEG2', or 'AUDIO'
    codec: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placeholder documentation for MaxResults
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filter by bitrate, 'MAX_10_MBPS', 'MAX_20_MBPS', or 'MAX_50_MBPS'
    maximum_bitrate: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Filter by framerate, 'MAX_30_FPS' or 'MAX_60_FPS'
    maximum_framerate: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filter by resolution, 'SD', 'HD', or 'UHD'
    resolution: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filter by resource type, 'INPUT', 'OUTPUT', or 'CHANNEL'
    resource_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filter by special feature, 'ADVANCED_AUDIO' or 'AUDIO_NORMALIZATION'
    special_feature: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Filter by video quality, 'STANDARD', 'ENHANCED', or 'PREMIUM'
    video_quality: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOfferingsResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for ListOfferingsResponse
    """

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
                "offerings",
                "Offerings",
                autoboto.TypeInfo(typing.List[Offering]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Token to retrieve the next page of results
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # List of offerings
    offerings: typing.List["Offering"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListOfferingsResultModel(autoboto.ShapeBase):
    """
    ListOfferings response
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
                "offerings",
                "Offerings",
                autoboto.TypeInfo(typing.List[Offering]),
            ),
        ]

    # Token to retrieve the next page of results
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # List of offerings
    offerings: typing.List["Offering"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListReservationsRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for ListReservationsRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "codec",
                "Codec",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "maximum_bitrate",
                "MaximumBitrate",
                autoboto.TypeInfo(str),
            ),
            (
                "maximum_framerate",
                "MaximumFramerate",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "resolution",
                "Resolution",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "special_feature",
                "SpecialFeature",
                autoboto.TypeInfo(str),
            ),
            (
                "video_quality",
                "VideoQuality",
                autoboto.TypeInfo(str),
            ),
        ]

    # Filter by codec, 'AVC', 'HEVC', 'MPEG2', or 'AUDIO'
    codec: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placeholder documentation for MaxResults
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filter by bitrate, 'MAX_10_MBPS', 'MAX_20_MBPS', or 'MAX_50_MBPS'
    maximum_bitrate: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Filter by framerate, 'MAX_30_FPS' or 'MAX_60_FPS'
    maximum_framerate: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filter by resolution, 'SD', 'HD', or 'UHD'
    resolution: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filter by resource type, 'INPUT', 'OUTPUT', or 'CHANNEL'
    resource_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Filter by special feature, 'ADVANCED_AUDIO' or 'AUDIO_NORMALIZATION'
    special_feature: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Filter by video quality, 'STANDARD', 'ENHANCED', or 'PREMIUM'
    video_quality: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListReservationsResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for ListReservationsResponse
    """

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
                "reservations",
                "Reservations",
                autoboto.TypeInfo(typing.List[Reservation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Token to retrieve the next page of results
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # List of reservations
    reservations: typing.List["Reservation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ListReservationsResultModel(autoboto.ShapeBase):
    """
    ListReservations response
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
                "reservations",
                "Reservations",
                autoboto.TypeInfo(typing.List[Reservation]),
            ),
        ]

    # Token to retrieve the next page of results
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # List of reservations
    reservations: typing.List["Reservation"] = dataclasses.field(
        default_factory=list,
    )


class LogLevel(Enum):
    """
    The log level the user wants for their channel.
    """
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"
    DISABLED = "DISABLED"


class M2tsAbsentInputAudioBehavior(Enum):
    """
    Placeholder documentation for M2tsAbsentInputAudioBehavior
    """
    DROP = "DROP"
    ENCODE_SILENCE = "ENCODE_SILENCE"


class M2tsArib(Enum):
    """
    Placeholder documentation for M2tsArib
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class M2tsAribCaptionsPidControl(Enum):
    """
    Placeholder documentation for M2tsAribCaptionsPidControl
    """
    AUTO = "AUTO"
    USE_CONFIGURED = "USE_CONFIGURED"


class M2tsAudioBufferModel(Enum):
    """
    Placeholder documentation for M2tsAudioBufferModel
    """
    ATSC = "ATSC"
    DVB = "DVB"


class M2tsAudioInterval(Enum):
    """
    Placeholder documentation for M2tsAudioInterval
    """
    VIDEO_AND_FIXED_INTERVALS = "VIDEO_AND_FIXED_INTERVALS"
    VIDEO_INTERVAL = "VIDEO_INTERVAL"


class M2tsAudioStreamType(Enum):
    """
    Placeholder documentation for M2tsAudioStreamType
    """
    ATSC = "ATSC"
    DVB = "DVB"


class M2tsBufferModel(Enum):
    """
    Placeholder documentation for M2tsBufferModel
    """
    MULTIPLEX = "MULTIPLEX"
    NONE = "NONE"


class M2tsCcDescriptor(Enum):
    """
    Placeholder documentation for M2tsCcDescriptor
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class M2tsEbifControl(Enum):
    """
    Placeholder documentation for M2tsEbifControl
    """
    NONE = "NONE"
    PASSTHROUGH = "PASSTHROUGH"


class M2tsEbpPlacement(Enum):
    """
    Placeholder documentation for M2tsEbpPlacement
    """
    VIDEO_AND_AUDIO_PIDS = "VIDEO_AND_AUDIO_PIDS"
    VIDEO_PID = "VIDEO_PID"


class M2tsEsRateInPes(Enum):
    """
    Placeholder documentation for M2tsEsRateInPes
    """
    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"


class M2tsKlv(Enum):
    """
    Placeholder documentation for M2tsKlv
    """
    NONE = "NONE"
    PASSTHROUGH = "PASSTHROUGH"


class M2tsPcrControl(Enum):
    """
    Placeholder documentation for M2tsPcrControl
    """
    CONFIGURED_PCR_PERIOD = "CONFIGURED_PCR_PERIOD"
    PCR_EVERY_PES_PACKET = "PCR_EVERY_PES_PACKET"


class M2tsRateMode(Enum):
    """
    Placeholder documentation for M2tsRateMode
    """
    CBR = "CBR"
    VBR = "VBR"


class M2tsScte35Control(Enum):
    """
    Placeholder documentation for M2tsScte35Control
    """
    NONE = "NONE"
    PASSTHROUGH = "PASSTHROUGH"


class M2tsSegmentationMarkers(Enum):
    """
    Placeholder documentation for M2tsSegmentationMarkers
    """
    EBP = "EBP"
    EBP_LEGACY = "EBP_LEGACY"
    NONE = "NONE"
    PSI_SEGSTART = "PSI_SEGSTART"
    RAI_ADAPT = "RAI_ADAPT"
    RAI_SEGSTART = "RAI_SEGSTART"


class M2tsSegmentationStyle(Enum):
    """
    Placeholder documentation for M2tsSegmentationStyle
    """
    MAINTAIN_CADENCE = "MAINTAIN_CADENCE"
    RESET_CADENCE = "RESET_CADENCE"


@dataclasses.dataclass
class M2tsSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for M2tsSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "absent_input_audio_behavior",
                "AbsentInputAudioBehavior",
                autoboto.TypeInfo(M2tsAbsentInputAudioBehavior),
            ),
            (
                "arib",
                "Arib",
                autoboto.TypeInfo(M2tsArib),
            ),
            (
                "arib_captions_pid",
                "AribCaptionsPid",
                autoboto.TypeInfo(str),
            ),
            (
                "arib_captions_pid_control",
                "AribCaptionsPidControl",
                autoboto.TypeInfo(M2tsAribCaptionsPidControl),
            ),
            (
                "audio_buffer_model",
                "AudioBufferModel",
                autoboto.TypeInfo(M2tsAudioBufferModel),
            ),
            (
                "audio_frames_per_pes",
                "AudioFramesPerPes",
                autoboto.TypeInfo(int),
            ),
            (
                "audio_pids",
                "AudioPids",
                autoboto.TypeInfo(str),
            ),
            (
                "audio_stream_type",
                "AudioStreamType",
                autoboto.TypeInfo(M2tsAudioStreamType),
            ),
            (
                "bitrate",
                "Bitrate",
                autoboto.TypeInfo(int),
            ),
            (
                "buffer_model",
                "BufferModel",
                autoboto.TypeInfo(M2tsBufferModel),
            ),
            (
                "cc_descriptor",
                "CcDescriptor",
                autoboto.TypeInfo(M2tsCcDescriptor),
            ),
            (
                "dvb_nit_settings",
                "DvbNitSettings",
                autoboto.TypeInfo(DvbNitSettings),
            ),
            (
                "dvb_sdt_settings",
                "DvbSdtSettings",
                autoboto.TypeInfo(DvbSdtSettings),
            ),
            (
                "dvb_sub_pids",
                "DvbSubPids",
                autoboto.TypeInfo(str),
            ),
            (
                "dvb_tdt_settings",
                "DvbTdtSettings",
                autoboto.TypeInfo(DvbTdtSettings),
            ),
            (
                "dvb_teletext_pid",
                "DvbTeletextPid",
                autoboto.TypeInfo(str),
            ),
            (
                "ebif",
                "Ebif",
                autoboto.TypeInfo(M2tsEbifControl),
            ),
            (
                "ebp_audio_interval",
                "EbpAudioInterval",
                autoboto.TypeInfo(M2tsAudioInterval),
            ),
            (
                "ebp_lookahead_ms",
                "EbpLookaheadMs",
                autoboto.TypeInfo(int),
            ),
            (
                "ebp_placement",
                "EbpPlacement",
                autoboto.TypeInfo(M2tsEbpPlacement),
            ),
            (
                "ecm_pid",
                "EcmPid",
                autoboto.TypeInfo(str),
            ),
            (
                "es_rate_in_pes",
                "EsRateInPes",
                autoboto.TypeInfo(M2tsEsRateInPes),
            ),
            (
                "etv_platform_pid",
                "EtvPlatformPid",
                autoboto.TypeInfo(str),
            ),
            (
                "etv_signal_pid",
                "EtvSignalPid",
                autoboto.TypeInfo(str),
            ),
            (
                "fragment_time",
                "FragmentTime",
                autoboto.TypeInfo(float),
            ),
            (
                "klv",
                "Klv",
                autoboto.TypeInfo(M2tsKlv),
            ),
            (
                "klv_data_pids",
                "KlvDataPids",
                autoboto.TypeInfo(str),
            ),
            (
                "null_packet_bitrate",
                "NullPacketBitrate",
                autoboto.TypeInfo(float),
            ),
            (
                "pat_interval",
                "PatInterval",
                autoboto.TypeInfo(int),
            ),
            (
                "pcr_control",
                "PcrControl",
                autoboto.TypeInfo(M2tsPcrControl),
            ),
            (
                "pcr_period",
                "PcrPeriod",
                autoboto.TypeInfo(int),
            ),
            (
                "pcr_pid",
                "PcrPid",
                autoboto.TypeInfo(str),
            ),
            (
                "pmt_interval",
                "PmtInterval",
                autoboto.TypeInfo(int),
            ),
            (
                "pmt_pid",
                "PmtPid",
                autoboto.TypeInfo(str),
            ),
            (
                "program_num",
                "ProgramNum",
                autoboto.TypeInfo(int),
            ),
            (
                "rate_mode",
                "RateMode",
                autoboto.TypeInfo(M2tsRateMode),
            ),
            (
                "scte27_pids",
                "Scte27Pids",
                autoboto.TypeInfo(str),
            ),
            (
                "scte35_control",
                "Scte35Control",
                autoboto.TypeInfo(M2tsScte35Control),
            ),
            (
                "scte35_pid",
                "Scte35Pid",
                autoboto.TypeInfo(str),
            ),
            (
                "segmentation_markers",
                "SegmentationMarkers",
                autoboto.TypeInfo(M2tsSegmentationMarkers),
            ),
            (
                "segmentation_style",
                "SegmentationStyle",
                autoboto.TypeInfo(M2tsSegmentationStyle),
            ),
            (
                "segmentation_time",
                "SegmentationTime",
                autoboto.TypeInfo(float),
            ),
            (
                "timed_metadata_behavior",
                "TimedMetadataBehavior",
                autoboto.TypeInfo(M2tsTimedMetadataBehavior),
            ),
            (
                "timed_metadata_pid",
                "TimedMetadataPid",
                autoboto.TypeInfo(str),
            ),
            (
                "transport_stream_id",
                "TransportStreamId",
                autoboto.TypeInfo(int),
            ),
            (
                "video_pid",
                "VideoPid",
                autoboto.TypeInfo(str),
            ),
        ]

    # When set to drop, output audio streams will be removed from the program if
    # the selected input audio stream is removed from the input. This allows the
    # output audio configuration to dynamically change based on input
    # configuration. If this is set to encodeSilence, all output audio streams
    # will output encoded silence when not connected to an active input stream.
    absent_input_audio_behavior: "M2tsAbsentInputAudioBehavior" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to enabled, uses ARIB-compliant field muxing and removes video
    # descriptor.
    arib: "M2tsArib" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Packet Identifier (PID) for ARIB Captions in the transport stream. Can be
    # entered as a decimal or hexadecimal value. Valid values are 32 (or
    # 0x20)..8182 (or 0x1ff6).
    arib_captions_pid: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If set to auto, pid number used for ARIB Captions will be auto-selected
    # from unused pids. If set to useConfigured, ARIB Captions will be on the
    # configured pid number.
    arib_captions_pid_control: "M2tsAribCaptionsPidControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to
    # atsc, the ATSC model is used.
    audio_buffer_model: "M2tsAudioBufferModel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of audio frames to insert for each PES packet.
    audio_frames_per_pes: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) of the elementary audio stream(s) in the transport
    # stream. Multiple values are accepted, and can be entered in ranges and/or
    # by comma separation. Can be entered as decimal or hexadecimal values. Each
    # PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    audio_pids: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87
    # for EAC3. When set to dvb, uses stream type = 0x06.
    audio_stream_type: "M2tsAudioStreamType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The output bitrate of the transport stream in bits per second. Setting to 0
    # lets the muxer automatically determine the appropriate bitrate.
    bitrate: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If set to multiplex, use multiplex buffer model for accurate interleaving.
    # Setting to bufferModel to none can lead to lower latency, but low-memory
    # devices may not be able to play back the stream without interruptions.
    buffer_model: "M2tsBufferModel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to enabled, generates captionServiceDescriptor in PMT.
    cc_descriptor: "M2tsCcDescriptor" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Inserts DVB Network Information Table (NIT) at the specified table
    # repetition interval.
    dvb_nit_settings: "DvbNitSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Inserts DVB Service Description Table (SDT) at the specified table
    # repetition interval.
    dvb_sdt_settings: "DvbSdtSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Packet Identifier (PID) for input source DVB Subtitle data to this output.
    # Multiple values are accepted, and can be entered in ranges and/or by comma
    # separation. Can be entered as decimal or hexadecimal values. Each PID
    # specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    dvb_sub_pids: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Inserts DVB Time and Date Table (TDT) at the specified table repetition
    # interval.
    dvb_tdt_settings: "DvbTdtSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Packet Identifier (PID) for input source DVB Teletext data to this output.
    # Can be entered as a decimal or hexadecimal value. Valid values are 32 (or
    # 0x20)..8182 (or 0x1ff6).
    dvb_teletext_pid: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If set to passthrough, passes any EBIF data from the input source to this
    # output.
    ebif: "M2tsEbifControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When videoAndFixedIntervals is selected, audio EBP markers will be added to
    # partitions 3 and 4. The interval between these additional markers will be
    # fixed, and will be slightly shorter than the video EBP marker interval.
    # Only available when EBP Cablelabs segmentation markers are selected.
    # Partitions 1 and 2 will always follow the video interval.
    ebp_audio_interval: "M2tsAudioInterval" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set, enforces that Encoder Boundary Points do not come within the
    # specified time interval of each other by looking ahead at input video. If
    # another EBP is going to come in within the specified time interval, the
    # current EBP is not emitted, and the segment is "stretched" to the next
    # marker. The lookahead value does not add latency to the system. The Live
    # Event must be configured elsewhere to create sufficient latency to make the
    # lookahead accurate.
    ebp_lookahead_ms: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Controls placement of EBP on Audio PIDs. If set to videoAndAudioPids, EBP
    # markers will be placed on the video PID and all audio PIDs. If set to
    # videoPid, EBP markers will be placed on only the video PID.
    ebp_placement: "M2tsEbpPlacement" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This field is unused and deprecated.
    ecm_pid: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Include or exclude the ES Rate field in the PES header.
    es_rate_in_pes: "M2tsEsRateInPes" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) for input source ETV Platform data to this output.
    # Can be entered as a decimal or hexadecimal value. Valid values are 32 (or
    # 0x20)..8182 (or 0x1ff6).
    etv_platform_pid: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) for input source ETV Signal data to this output.
    # Can be entered as a decimal or hexadecimal value. Valid values are 32 (or
    # 0x20)..8182 (or 0x1ff6).
    etv_signal_pid: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The length in seconds of each fragment. Only used with EBP markers.
    fragment_time: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If set to passthrough, passes any KLV data from the input source to this
    # output.
    klv: "M2tsKlv" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Packet Identifier (PID) for input source KLV data to this output. Multiple
    # values are accepted, and can be entered in ranges and/or by comma
    # separation. Can be entered as decimal or hexadecimal values. Each PID
    # specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    klv_data_pids: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Value in bits per second of extra null packets to insert into the transport
    # stream. This can be used if a downstream encryption system requires
    # periodic null packets.
    null_packet_bitrate: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of milliseconds between instances of this table in the output
    # transport stream. Valid values are 0, 10..1000.
    pat_interval: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When set to pcrEveryPesPacket, a Program Clock Reference value is inserted
    # for every Packetized Elementary Stream (PES) header. This parameter is
    # effective only when the PCR PID is the same as the video or audio
    # elementary stream.
    pcr_control: "M2tsPcrControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Maximum time in milliseconds between Program Clock Reference (PCRs)
    # inserted into the transport stream.
    pcr_period: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Packet Identifier (PID) of the Program Clock Reference (PCR) in the
    # transport stream. When no value is given, the encoder will assign the same
    # value as the Video PID. Can be entered as a decimal or hexadecimal value.
    # Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    pcr_pid: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of milliseconds between instances of this table in the output
    # transport stream. Valid values are 0, 10..1000.
    pmt_interval: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Packet Identifier (PID) for the Program Map Table (PMT) in the transport
    # stream. Can be entered as a decimal or hexadecimal value. Valid values are
    # 32 (or 0x20)..8182 (or 0x1ff6).
    pmt_pid: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value of the program number field in the Program Map Table.
    program_num: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When vbr, does not insert null packets into transport stream to fill
    # specified bitrate. The bitrate setting acts as the maximum bitrate when vbr
    # is set.
    rate_mode: "M2tsRateMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) for input source SCTE-27 data to this output.
    # Multiple values are accepted, and can be entered in ranges and/or by comma
    # separation. Can be entered as decimal or hexadecimal values. Each PID
    # specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    scte27_pids: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Optionally pass SCTE-35 signals from the input source to this output.
    scte35_control: "M2tsScte35Control" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can
    # be entered as a decimal or hexadecimal value. Valid values are 32 (or
    # 0x20)..8182 (or 0x1ff6).
    scte35_pid: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Inserts segmentation markers at each segmentationTime period. raiSegstart
    # sets the Random Access Indicator bit in the adaptation field. raiAdapt sets
    # the RAI bit and adds the current timecode in the private data bytes.
    # psiSegstart inserts PAT and PMT tables at the start of segments. ebp adds
    # Encoder Boundary Point information to the adaptation field as per OpenCable
    # specification OC-SP-EBP-I01-130118. ebpLegacy adds Encoder Boundary Point
    # information to the adaptation field using a legacy proprietary format.
    segmentation_markers: "M2tsSegmentationMarkers" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The segmentation style parameter controls how segmentation markers are
    # inserted into the transport stream. With avails, it is possible that
    # segments may be truncated, which can influence where future segmentation
    # markers are inserted. When a segmentation style of "resetCadence" is
    # selected and a segment is truncated due to an avail, we will reset the
    # segmentation cadence. This means the subsequent segment will have a
    # duration of $segmentationTime seconds. When a segmentation style of
    # "maintainCadence" is selected and a segment is truncated due to an avail,
    # we will not reset the segmentation cadence. This means the subsequent
    # segment will likely be truncated as well. However, all segments after that
    # will have a duration of $segmentationTime seconds. Note that EBP lookahead
    # is a slight exception to this rule.
    segmentation_style: "M2tsSegmentationStyle" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The length in seconds of each segment. Required unless markers is set to
    # None_.
    segmentation_time: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to passthrough, timed metadata will be passed through from input
    # to output.
    timed_metadata_behavior: "M2tsTimedMetadataBehavior" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) of the timed metadata stream in the transport
    # stream. Can be entered as a decimal or hexadecimal value. Valid values are
    # 32 (or 0x20)..8182 (or 0x1ff6).
    timed_metadata_pid: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The value of the transport stream ID field in the Program Map Table.
    transport_stream_id: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) of the elementary video stream in the transport
    # stream. Can be entered as a decimal or hexadecimal value. Valid values are
    # 32 (or 0x20)..8182 (or 0x1ff6).
    video_pid: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class M2tsTimedMetadataBehavior(Enum):
    """
    Placeholder documentation for M2tsTimedMetadataBehavior
    """
    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    PASSTHROUGH = "PASSTHROUGH"


class M3u8PcrControl(Enum):
    """
    Placeholder documentation for M3u8PcrControl
    """
    CONFIGURED_PCR_PERIOD = "CONFIGURED_PCR_PERIOD"
    PCR_EVERY_PES_PACKET = "PCR_EVERY_PES_PACKET"


class M3u8Scte35Behavior(Enum):
    """
    Placeholder documentation for M3u8Scte35Behavior
    """
    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    PASSTHROUGH = "PASSTHROUGH"


@dataclasses.dataclass
class M3u8Settings(autoboto.ShapeBase):
    """
    Settings information for the .m3u8 container
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_frames_per_pes",
                "AudioFramesPerPes",
                autoboto.TypeInfo(int),
            ),
            (
                "audio_pids",
                "AudioPids",
                autoboto.TypeInfo(str),
            ),
            (
                "ecm_pid",
                "EcmPid",
                autoboto.TypeInfo(str),
            ),
            (
                "pat_interval",
                "PatInterval",
                autoboto.TypeInfo(int),
            ),
            (
                "pcr_control",
                "PcrControl",
                autoboto.TypeInfo(M3u8PcrControl),
            ),
            (
                "pcr_period",
                "PcrPeriod",
                autoboto.TypeInfo(int),
            ),
            (
                "pcr_pid",
                "PcrPid",
                autoboto.TypeInfo(str),
            ),
            (
                "pmt_interval",
                "PmtInterval",
                autoboto.TypeInfo(int),
            ),
            (
                "pmt_pid",
                "PmtPid",
                autoboto.TypeInfo(str),
            ),
            (
                "program_num",
                "ProgramNum",
                autoboto.TypeInfo(int),
            ),
            (
                "scte35_behavior",
                "Scte35Behavior",
                autoboto.TypeInfo(M3u8Scte35Behavior),
            ),
            (
                "scte35_pid",
                "Scte35Pid",
                autoboto.TypeInfo(str),
            ),
            (
                "timed_metadata_behavior",
                "TimedMetadataBehavior",
                autoboto.TypeInfo(M3u8TimedMetadataBehavior),
            ),
            (
                "timed_metadata_pid",
                "TimedMetadataPid",
                autoboto.TypeInfo(str),
            ),
            (
                "transport_stream_id",
                "TransportStreamId",
                autoboto.TypeInfo(int),
            ),
            (
                "video_pid",
                "VideoPid",
                autoboto.TypeInfo(str),
            ),
        ]

    # The number of audio frames to insert for each PES packet.
    audio_frames_per_pes: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) of the elementary audio stream(s) in the transport
    # stream. Multiple values are accepted, and can be entered in ranges and/or
    # by comma separation. Can be entered as decimal or hexadecimal values.
    audio_pids: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This parameter is unused and deprecated.
    ecm_pid: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of milliseconds between instances of this table in the output
    # transport stream. A value of \"0\" writes out the PMT once per segment
    # file.
    pat_interval: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When set to pcrEveryPesPacket, a Program Clock Reference value is inserted
    # for every Packetized Elementary Stream (PES) header. This parameter is
    # effective only when the PCR PID is the same as the video or audio
    # elementary stream.
    pcr_control: "M3u8PcrControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Maximum time in milliseconds between Program Clock References (PCRs)
    # inserted into the transport stream.
    pcr_period: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Packet Identifier (PID) of the Program Clock Reference (PCR) in the
    # transport stream. When no value is given, the encoder will assign the same
    # value as the Video PID. Can be entered as a decimal or hexadecimal value.
    pcr_pid: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of milliseconds between instances of this table in the output
    # transport stream. A value of \"0\" writes out the PMT once per segment
    # file.
    pmt_interval: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Packet Identifier (PID) for the Program Map Table (PMT) in the transport
    # stream. Can be entered as a decimal or hexadecimal value.
    pmt_pid: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value of the program number field in the Program Map Table.
    program_num: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If set to passthrough, passes any SCTE-35 signals from the input source to
    # this output.
    scte35_behavior: "M3u8Scte35Behavior" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can
    # be entered as a decimal or hexadecimal value.
    scte35_pid: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When set to passthrough, timed metadata is passed through from input to
    # output.
    timed_metadata_behavior: "M3u8TimedMetadataBehavior" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) of the timed metadata stream in the transport
    # stream. Can be entered as a decimal or hexadecimal value. Valid values are
    # 32 (or 0x20)..8182 (or 0x1ff6).
    timed_metadata_pid: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The value of the transport stream ID field in the Program Map Table.
    transport_stream_id: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) of the elementary video stream in the transport
    # stream. Can be entered as a decimal or hexadecimal value.
    video_pid: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class M3u8TimedMetadataBehavior(Enum):
    """
    Placeholder documentation for M3u8TimedMetadataBehavior
    """
    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    PASSTHROUGH = "PASSTHROUGH"


class Mp2CodingMode(Enum):
    """
    Placeholder documentation for Mp2CodingMode
    """
    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_2_0 = "CODING_MODE_2_0"


@dataclasses.dataclass
class Mp2Settings(autoboto.ShapeBase):
    """
    Placeholder documentation for Mp2Settings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bitrate",
                "Bitrate",
                autoboto.TypeInfo(float),
            ),
            (
                "coding_mode",
                "CodingMode",
                autoboto.TypeInfo(Mp2CodingMode),
            ),
            (
                "sample_rate",
                "SampleRate",
                autoboto.TypeInfo(float),
            ),
        ]

    # Average bitrate in bits/second.
    bitrate: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The MPEG2 Audio coding mode. Valid values are codingMode10 (for mono) or
    # codingMode20 (for stereo).
    coding_mode: "Mp2CodingMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Sample rate in Hz.
    sample_rate: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MsSmoothGroupSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for MsSmoothGroupSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination",
                "Destination",
                autoboto.TypeInfo(OutputLocationRef),
            ),
            (
                "acquisition_point_id",
                "AcquisitionPointId",
                autoboto.TypeInfo(str),
            ),
            (
                "audio_only_timecode_control",
                "AudioOnlyTimecodeControl",
                autoboto.TypeInfo(SmoothGroupAudioOnlyTimecodeControl),
            ),
            (
                "certificate_mode",
                "CertificateMode",
                autoboto.TypeInfo(SmoothGroupCertificateMode),
            ),
            (
                "connection_retry_interval",
                "ConnectionRetryInterval",
                autoboto.TypeInfo(int),
            ),
            (
                "event_id",
                "EventId",
                autoboto.TypeInfo(str),
            ),
            (
                "event_id_mode",
                "EventIdMode",
                autoboto.TypeInfo(SmoothGroupEventIdMode),
            ),
            (
                "event_stop_behavior",
                "EventStopBehavior",
                autoboto.TypeInfo(SmoothGroupEventStopBehavior),
            ),
            (
                "filecache_duration",
                "FilecacheDuration",
                autoboto.TypeInfo(int),
            ),
            (
                "fragment_length",
                "FragmentLength",
                autoboto.TypeInfo(int),
            ),
            (
                "input_loss_action",
                "InputLossAction",
                autoboto.TypeInfo(InputLossActionForMsSmoothOut),
            ),
            (
                "num_retries",
                "NumRetries",
                autoboto.TypeInfo(int),
            ),
            (
                "restart_delay",
                "RestartDelay",
                autoboto.TypeInfo(int),
            ),
            (
                "segmentation_mode",
                "SegmentationMode",
                autoboto.TypeInfo(SmoothGroupSegmentationMode),
            ),
            (
                "send_delay_ms",
                "SendDelayMs",
                autoboto.TypeInfo(int),
            ),
            (
                "sparse_track_type",
                "SparseTrackType",
                autoboto.TypeInfo(SmoothGroupSparseTrackType),
            ),
            (
                "stream_manifest_behavior",
                "StreamManifestBehavior",
                autoboto.TypeInfo(SmoothGroupStreamManifestBehavior),
            ),
            (
                "timestamp_offset",
                "TimestampOffset",
                autoboto.TypeInfo(str),
            ),
            (
                "timestamp_offset_mode",
                "TimestampOffsetMode",
                autoboto.TypeInfo(SmoothGroupTimestampOffsetMode),
            ),
        ]

    # Smooth Streaming publish point on an IIS server. Elemental Live acts as a
    # "Push" encoder to IIS.
    destination: "OutputLocationRef" = dataclasses.field(default_factory=dict, )

    # The value of the "Acquisition Point Identity" element used in each message
    # placed in the sparse track. Only enabled if sparseTrackType is not "none".
    acquisition_point_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If set to passthrough for an audio-only MS Smooth output, the fragment
    # absolute time will be set to the current timecode. This option does not
    # write timecodes to the audio elementary stream.
    audio_only_timecode_control: "SmoothGroupAudioOnlyTimecodeControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If set to verifyAuthenticity, verify the https certificate chain to a
    # trusted Certificate Authority (CA). This will cause https outputs to self-
    # signed certificates to fail.
    certificate_mode: "SmoothGroupCertificateMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Number of seconds to wait before retrying connection to the IIS server if
    # the connection is lost. Content will be cached during this time and the
    # cache will be be delivered to the IIS server once the connection is re-
    # established.
    connection_retry_interval: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # MS Smooth event ID to be sent to the IIS server. Should only be specified
    # if eventIdMode is set to useConfigured.
    event_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies whether or not to send an event ID to the IIS server. If no event
    # ID is sent and the same Live Event is used without changing the publishing
    # point, clients might see cached video from the previous run. Options: \-
    # "useConfigured" - use the value provided in eventId \- "useTimestamp" -
    # generate and send an event ID based on the current timestamp \- "noEventId"
    # - do not send an event ID to the IIS server.
    event_id_mode: "SmoothGroupEventIdMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to sendEos, send EOS signal to IIS server when stopping the event
    event_stop_behavior: "SmoothGroupEventStopBehavior" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Size in seconds of file cache for streaming outputs.
    filecache_duration: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Length of mp4 fragments to generate (in seconds). Fragment length must be
    # compatible with GOP size and framerate.
    fragment_length: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Parameter that control output group behavior on input loss.
    input_loss_action: "InputLossActionForMsSmoothOut" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Number of retry attempts.
    num_retries: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Number of seconds before initiating a restart due to output failure, due to
    # exhausting the numRetries on one segment, or exceeding filecacheDuration.
    restart_delay: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When set to useInputSegmentation, the output segment or fragment points are
    # set by the RAI markers from the input streams.
    segmentation_mode: "SmoothGroupSegmentationMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Outputs that are "output locked" can use this delay. Assign a delay to the
    # output that is "secondary". Do not assign a delay to the "primary" output.
    # The delay means that the primary output will always reach the downstream
    # system before the secondary, which helps ensure that the downstream system
    # always uses the primary output. (If there were no delay, the downstream
    # system might flip-flop between whichever output happens to arrive first.)
    # If the primary fails, the downstream system will switch to the secondary
    # output. When the primary is restarted, the downstream system will switch
    # back to the primary (because once again it is always arriving first)
    send_delay_ms: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If set to scte35, use incoming SCTE-35 messages to generate a sparse track
    # in this group of MS-Smooth outputs.
    sparse_track_type: "SmoothGroupSparseTrackType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to send, send stream manifest so publishing point doesn't start
    # until all streams start.
    stream_manifest_behavior: "SmoothGroupStreamManifestBehavior" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Timestamp offset for the event. Only used if timestampOffsetMode is set to
    # useConfiguredOffset.
    timestamp_offset: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Type of timestamp date offset to use. \- useEventStartDate: Use the date
    # the event was started as the offset \- useConfiguredOffset: Use an
    # explicitly configured date as the offset
    timestamp_offset_mode: "SmoothGroupTimestampOffsetMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MsSmoothOutputSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for MsSmoothOutputSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name_modifier",
                "NameModifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # String concatenated to the end of the destination filename. Required for
    # multiple outputs of the same type.
    name_modifier: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class NetworkInputServerValidation(Enum):
    """
    Placeholder documentation for NetworkInputServerValidation
    """
    CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME = "CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME"
    CHECK_CRYPTOGRAPHY_ONLY = "CHECK_CRYPTOGRAPHY_ONLY"


@dataclasses.dataclass
class NetworkInputSettings(autoboto.ShapeBase):
    """
    Network source to transcode. Must be accessible to the Elemental Live node that
    is running the live event through a network connection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hls_input_settings",
                "HlsInputSettings",
                autoboto.TypeInfo(HlsInputSettings),
            ),
            (
                "server_validation",
                "ServerValidation",
                autoboto.TypeInfo(NetworkInputServerValidation),
            ),
        ]

    # Specifies HLS input settings when the uri is for a HLS manifest.
    hls_input_settings: "HlsInputSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Check HTTPS server certificates. When set to checkCryptographyOnly,
    # cryptography in the certificate will be checked, but not the server's name.
    # Certain subdomains (notably S3 buckets that use dots in the bucket name) do
    # not strictly match the corresponding certificate's wildcard pattern and
    # would otherwise cause the event to error. This setting is ignored for
    # protocols that do not use https.
    server_validation: "NetworkInputServerValidation" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NotFoundException(autoboto.ShapeBase):
    """
    Placeholder documentation for NotFoundException
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

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Offering(autoboto.ShapeBase):
    """
    Reserved resources available for purchase
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
                "currency_code",
                "CurrencyCode",
                autoboto.TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(int),
            ),
            (
                "duration_units",
                "DurationUnits",
                autoboto.TypeInfo(OfferingDurationUnits),
            ),
            (
                "fixed_price",
                "FixedPrice",
                autoboto.TypeInfo(float),
            ),
            (
                "offering_description",
                "OfferingDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "offering_id",
                "OfferingId",
                autoboto.TypeInfo(str),
            ),
            (
                "offering_type",
                "OfferingType",
                autoboto.TypeInfo(OfferingType),
            ),
            (
                "region",
                "Region",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_specification",
                "ResourceSpecification",
                autoboto.TypeInfo(ReservationResourceSpecification),
            ),
            (
                "usage_price",
                "UsagePrice",
                autoboto.TypeInfo(float),
            ),
        ]

    # Unique offering ARN, e.g. 'arn:aws:medialive:us-
    # west-2:123456789012:offering:87654321'
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'
    currency_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Lease duration, e.g. '12'
    duration: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Units for duration, e.g. 'MONTHS'
    duration_units: "OfferingDurationUnits" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT
    # offering
    fixed_price: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and
    # standard VQ in US West (Oregon)'
    offering_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique offering ID, e.g. '87654321'
    offering_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Offering type, e.g. 'NO_UPFRONT'
    offering_type: "OfferingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # AWS region, e.g. 'us-west-2'
    region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Resource configuration details
    resource_specification: "ReservationResourceSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # Recurring usage charge for each reserved resource, e.g. '157.0'
    usage_price: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class OfferingDurationUnits(Enum):
    """
    Units for duration, e.g. 'MONTHS'
    """
    MONTHS = "MONTHS"


class OfferingType(Enum):
    """
    Offering type, e.g. 'NO_UPFRONT'
    """
    NO_UPFRONT = "NO_UPFRONT"


@dataclasses.dataclass
class Output(autoboto.ShapeBase):
    """
    Output settings. There can be multiple outputs within a group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_settings",
                "OutputSettings",
                autoboto.TypeInfo(OutputSettings),
            ),
            (
                "audio_description_names",
                "AudioDescriptionNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "caption_description_names",
                "CaptionDescriptionNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "output_name",
                "OutputName",
                autoboto.TypeInfo(str),
            ),
            (
                "video_description_name",
                "VideoDescriptionName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Output type-specific settings.
    output_settings: "OutputSettings" = dataclasses.field(
        default_factory=dict,
    )

    # The names of the AudioDescriptions used as audio sources for this output.
    audio_description_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The names of the CaptionDescriptions used as caption sources for this
    # output.
    caption_description_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The name used to identify an output.
    output_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the VideoDescription used as the source for this output.
    video_description_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OutputDestination(autoboto.ShapeBase):
    """
    Placeholder documentation for OutputDestination
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
                "settings",
                "Settings",
                autoboto.TypeInfo(typing.List[OutputDestinationSettings]),
            ),
        ]

    # User-specified id. This is used in an output group or an output.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Destination settings for output; one for each redundant encoder.
    settings: typing.List["OutputDestinationSettings"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class OutputDestinationSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for OutputDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "password_param",
                "PasswordParam",
                autoboto.TypeInfo(str),
            ),
            (
                "stream_name",
                "StreamName",
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

    # key used to extract the password from EC2 Parameter store
    password_param: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Stream name for RTMP destinations (URLs of type rtmp://)
    stream_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A URL specifying a destination
    url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # username for destination
    username: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OutputGroup(autoboto.ShapeBase):
    """
    Output groups for this Live Event. Output groups contain information about where
    streams should be distributed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_group_settings",
                "OutputGroupSettings",
                autoboto.TypeInfo(OutputGroupSettings),
            ),
            (
                "outputs",
                "Outputs",
                autoboto.TypeInfo(typing.List[Output]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # Settings associated with the output group.
    output_group_settings: "OutputGroupSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for __listOfOutput
    outputs: typing.List["Output"] = dataclasses.field(default_factory=list, )

    # Custom output group name optionally defined by the user. Only letters,
    # numbers, and the underscore character allowed; only 32 characters allowed.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OutputGroupSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for OutputGroupSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "archive_group_settings",
                "ArchiveGroupSettings",
                autoboto.TypeInfo(ArchiveGroupSettings),
            ),
            (
                "hls_group_settings",
                "HlsGroupSettings",
                autoboto.TypeInfo(HlsGroupSettings),
            ),
            (
                "ms_smooth_group_settings",
                "MsSmoothGroupSettings",
                autoboto.TypeInfo(MsSmoothGroupSettings),
            ),
            (
                "rtmp_group_settings",
                "RtmpGroupSettings",
                autoboto.TypeInfo(RtmpGroupSettings),
            ),
            (
                "udp_group_settings",
                "UdpGroupSettings",
                autoboto.TypeInfo(UdpGroupSettings),
            ),
        ]

    # Placeholder documentation for ArchiveGroupSettings
    archive_group_settings: "ArchiveGroupSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for HlsGroupSettings
    hls_group_settings: "HlsGroupSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for MsSmoothGroupSettings
    ms_smooth_group_settings: "MsSmoothGroupSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for RtmpGroupSettings
    rtmp_group_settings: "RtmpGroupSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for UdpGroupSettings
    udp_group_settings: "UdpGroupSettings" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class OutputLocationRef(autoboto.ShapeBase):
    """
    Reference to an OutputDestination ID defined in the channel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_ref_id",
                "DestinationRefId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    destination_ref_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OutputSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for OutputSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "archive_output_settings",
                "ArchiveOutputSettings",
                autoboto.TypeInfo(ArchiveOutputSettings),
            ),
            (
                "hls_output_settings",
                "HlsOutputSettings",
                autoboto.TypeInfo(HlsOutputSettings),
            ),
            (
                "ms_smooth_output_settings",
                "MsSmoothOutputSettings",
                autoboto.TypeInfo(MsSmoothOutputSettings),
            ),
            (
                "rtmp_output_settings",
                "RtmpOutputSettings",
                autoboto.TypeInfo(RtmpOutputSettings),
            ),
            (
                "udp_output_settings",
                "UdpOutputSettings",
                autoboto.TypeInfo(UdpOutputSettings),
            ),
        ]

    # Placeholder documentation for ArchiveOutputSettings
    archive_output_settings: "ArchiveOutputSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for HlsOutputSettings
    hls_output_settings: "HlsOutputSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for MsSmoothOutputSettings
    ms_smooth_output_settings: "MsSmoothOutputSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for RtmpOutputSettings
    rtmp_output_settings: "RtmpOutputSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for UdpOutputSettings
    udp_output_settings: "UdpOutputSettings" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PassThroughSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for PassThroughSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PurchaseOffering(autoboto.ShapeBase):
    """
    PurchaseOffering request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "count",
                "Count",
                autoboto.TypeInfo(int),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Number of resources
    count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Name for the new reservation
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Unique request ID to be specified. This is needed to prevent retries from
    # creating multiple resources.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PurchaseOfferingRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for PurchaseOfferingRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "offering_id",
                "OfferingId",
                autoboto.TypeInfo(str),
            ),
            (
                "count",
                "Count",
                autoboto.TypeInfo(int),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Offering to purchase, e.g. '87654321'
    offering_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Number of resources
    count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Name for the new reservation
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Unique request ID to be specified. This is needed to prevent retries from
    # creating multiple resources.
    request_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PurchaseOfferingResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for PurchaseOfferingResponse
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "reservation",
                "Reservation",
                autoboto.TypeInfo(Reservation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Reserved resources available to use
    reservation: "Reservation" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PurchaseOfferingResultModel(autoboto.ShapeBase):
    """
    PurchaseOffering response
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reservation",
                "Reservation",
                autoboto.TypeInfo(Reservation),
            ),
        ]

    # Reserved resources available to use
    reservation: "Reservation" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class RemixSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for RemixSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_mappings",
                "ChannelMappings",
                autoboto.TypeInfo(typing.List[AudioChannelMapping]),
            ),
            (
                "channels_in",
                "ChannelsIn",
                autoboto.TypeInfo(int),
            ),
            (
                "channels_out",
                "ChannelsOut",
                autoboto.TypeInfo(int),
            ),
        ]

    # Mapping of input channels to output channels, with appropriate gain
    # adjustments.
    channel_mappings: typing.List["AudioChannelMapping"] = dataclasses.field(
        default_factory=list,
    )

    # Number of input channels to be used.
    channels_in: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Number of output channels to be produced. Valid values: 1, 2, 4, 6, 8
    channels_out: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Reservation(autoboto.ShapeBase):
    """
    Reserved resources available to use
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
                "count",
                "Count",
                autoboto.TypeInfo(int),
            ),
            (
                "currency_code",
                "CurrencyCode",
                autoboto.TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(int),
            ),
            (
                "duration_units",
                "DurationUnits",
                autoboto.TypeInfo(OfferingDurationUnits),
            ),
            (
                "end",
                "End",
                autoboto.TypeInfo(str),
            ),
            (
                "fixed_price",
                "FixedPrice",
                autoboto.TypeInfo(float),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "offering_description",
                "OfferingDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "offering_id",
                "OfferingId",
                autoboto.TypeInfo(str),
            ),
            (
                "offering_type",
                "OfferingType",
                autoboto.TypeInfo(OfferingType),
            ),
            (
                "region",
                "Region",
                autoboto.TypeInfo(str),
            ),
            (
                "reservation_id",
                "ReservationId",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_specification",
                "ResourceSpecification",
                autoboto.TypeInfo(ReservationResourceSpecification),
            ),
            (
                "start",
                "Start",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(ReservationState),
            ),
            (
                "usage_price",
                "UsagePrice",
                autoboto.TypeInfo(float),
            ),
        ]

    # Unique reservation ARN, e.g. 'arn:aws:medialive:us-
    # west-2:123456789012:reservation:1234567'
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Number of reserved resources
    count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'
    currency_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Lease duration, e.g. '12'
    duration: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Units for duration, e.g. 'MONTHS'
    duration_units: "OfferingDurationUnits" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Reservation UTC end date and time in ISO-8601 format, e.g.
    # '2019-03-01T00:00:00'
    end: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT
    # offering
    fixed_price: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # User specified reservation name
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and
    # standard VQ in US West (Oregon)'
    offering_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Unique offering ID, e.g. '87654321'
    offering_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Offering type, e.g. 'NO_UPFRONT'
    offering_type: "OfferingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # AWS region, e.g. 'us-west-2'
    region: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Unique reservation ID, e.g. '1234567'
    reservation_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Resource configuration details
    resource_specification: "ReservationResourceSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # Reservation UTC start date and time in ISO-8601 format, e.g.
    # '2018-03-01T00:00:00'
    start: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Current state of reservation, e.g. 'ACTIVE'
    state: "ReservationState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Recurring usage charge for each reserved resource, e.g. '157.0'
    usage_price: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ReservationCodec(Enum):
    """
    Codec, 'MPEG2', 'AVC', 'HEVC', or 'AUDIO'
    """
    MPEG2 = "MPEG2"
    AVC = "AVC"
    HEVC = "HEVC"
    AUDIO = "AUDIO"


class ReservationMaximumBitrate(Enum):
    """
    Maximum bitrate in megabits per second
    """
    MAX_10_MBPS = "MAX_10_MBPS"
    MAX_20_MBPS = "MAX_20_MBPS"
    MAX_50_MBPS = "MAX_50_MBPS"


class ReservationMaximumFramerate(Enum):
    """
    Maximum framerate in frames per second (Outputs only)
    """
    MAX_30_FPS = "MAX_30_FPS"
    MAX_60_FPS = "MAX_60_FPS"


class ReservationResolution(Enum):
    """
    Resolution based on lines of vertical resolution; SD is less than 720 lines, HD
    is 720 to 1080 lines, UHD is greater than 1080 lines
    """
    SD = "SD"
    HD = "HD"
    UHD = "UHD"


@dataclasses.dataclass
class ReservationResourceSpecification(autoboto.ShapeBase):
    """
    Resource configuration (codec, resolution, bitrate, ...)
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "codec",
                "Codec",
                autoboto.TypeInfo(ReservationCodec),
            ),
            (
                "maximum_bitrate",
                "MaximumBitrate",
                autoboto.TypeInfo(ReservationMaximumBitrate),
            ),
            (
                "maximum_framerate",
                "MaximumFramerate",
                autoboto.TypeInfo(ReservationMaximumFramerate),
            ),
            (
                "resolution",
                "Resolution",
                autoboto.TypeInfo(ReservationResolution),
            ),
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(ReservationResourceType),
            ),
            (
                "special_feature",
                "SpecialFeature",
                autoboto.TypeInfo(ReservationSpecialFeature),
            ),
            (
                "video_quality",
                "VideoQuality",
                autoboto.TypeInfo(ReservationVideoQuality),
            ),
        ]

    # Codec, e.g. 'AVC'
    codec: "ReservationCodec" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Maximum bitrate, e.g. 'MAX_20_MBPS'
    maximum_bitrate: "ReservationMaximumBitrate" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Maximum framerate, e.g. 'MAX_30_FPS' (Outputs only)
    maximum_framerate: "ReservationMaximumFramerate" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Resolution, e.g. 'HD'
    resolution: "ReservationResolution" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Resource type, 'INPUT', 'OUTPUT', or 'CHANNEL'
    resource_type: "ReservationResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Special feature, e.g. 'AUDIO_NORMALIZATION' (Channels only)
    special_feature: "ReservationSpecialFeature" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Video quality, e.g. 'STANDARD' (Outputs only)
    video_quality: "ReservationVideoQuality" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ReservationResourceType(Enum):
    """
    Resource type, 'INPUT', 'OUTPUT', or 'CHANNEL'
    """
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"
    CHANNEL = "CHANNEL"


class ReservationSpecialFeature(Enum):
    """
    Special features, 'ADVANCED_AUDIO' or 'AUDIO_NORMALIZATION'
    """
    ADVANCED_AUDIO = "ADVANCED_AUDIO"
    AUDIO_NORMALIZATION = "AUDIO_NORMALIZATION"


class ReservationState(Enum):
    """
    Current reservation state
    """
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    CANCELED = "CANCELED"
    DELETED = "DELETED"


class ReservationVideoQuality(Enum):
    """
    Video quality, e.g. 'STANDARD' (Outputs only)
    """
    STANDARD = "STANDARD"
    ENHANCED = "ENHANCED"
    PREMIUM = "PREMIUM"


@dataclasses.dataclass
class ResourceConflict(autoboto.ShapeBase):
    """
    Placeholder documentation for ResourceConflict
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

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFound(autoboto.ShapeBase):
    """
    Placeholder documentation for ResourceNotFound
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

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class RtmpCacheFullBehavior(Enum):
    """
    Placeholder documentation for RtmpCacheFullBehavior
    """
    DISCONNECT_IMMEDIATELY = "DISCONNECT_IMMEDIATELY"
    WAIT_FOR_SERVER = "WAIT_FOR_SERVER"


class RtmpCaptionData(Enum):
    """
    Placeholder documentation for RtmpCaptionData
    """
    ALL = "ALL"
    FIELD1_608 = "FIELD1_608"
    FIELD1_AND_FIELD2_608 = "FIELD1_AND_FIELD2_608"


@dataclasses.dataclass
class RtmpCaptionInfoDestinationSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for RtmpCaptionInfoDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RtmpGroupSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for RtmpGroupSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authentication_scheme",
                "AuthenticationScheme",
                autoboto.TypeInfo(AuthenticationScheme),
            ),
            (
                "cache_full_behavior",
                "CacheFullBehavior",
                autoboto.TypeInfo(RtmpCacheFullBehavior),
            ),
            (
                "cache_length",
                "CacheLength",
                autoboto.TypeInfo(int),
            ),
            (
                "caption_data",
                "CaptionData",
                autoboto.TypeInfo(RtmpCaptionData),
            ),
            (
                "restart_delay",
                "RestartDelay",
                autoboto.TypeInfo(int),
            ),
        ]

    # Authentication scheme to use when connecting with CDN
    authentication_scheme: "AuthenticationScheme" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Controls behavior when content cache fills up. If remote origin server
    # stalls the RTMP connection and does not accept content fast enough the
    # 'Media Cache' will fill up. When the cache reaches the duration specified
    # by cacheLength the cache will stop accepting new content. If set to
    # disconnectImmediately, the RTMP output will force a disconnect. Clear the
    # media cache, and reconnect after restartDelay seconds. If set to
    # waitForServer, the RTMP output will wait up to 5 minutes to allow the
    # origin server to begin accepting data again.
    cache_full_behavior: "RtmpCacheFullBehavior" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Cache length, in seconds, is used to calculate buffer size.
    cache_length: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Controls the types of data that passes to onCaptionInfo outputs. If set to
    # 'all' then 608 and 708 carried DTVCC data will be passed. If set to
    # 'field1AndField2608' then DTVCC data will be stripped out, but 608 data
    # from both fields will be passed. If set to 'field1608' then only the data
    # carried in 608 from field 1 video will be passed.
    caption_data: "RtmpCaptionData" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If a streaming output fails, number of seconds to wait until a restart is
    # initiated. A value of 0 means never restart.
    restart_delay: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class RtmpOutputCertificateMode(Enum):
    """
    Placeholder documentation for RtmpOutputCertificateMode
    """
    SELF_SIGNED = "SELF_SIGNED"
    VERIFY_AUTHENTICITY = "VERIFY_AUTHENTICITY"


@dataclasses.dataclass
class RtmpOutputSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for RtmpOutputSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination",
                "Destination",
                autoboto.TypeInfo(OutputLocationRef),
            ),
            (
                "certificate_mode",
                "CertificateMode",
                autoboto.TypeInfo(RtmpOutputCertificateMode),
            ),
            (
                "connection_retry_interval",
                "ConnectionRetryInterval",
                autoboto.TypeInfo(int),
            ),
            (
                "num_retries",
                "NumRetries",
                autoboto.TypeInfo(int),
            ),
        ]

    # The RTMP endpoint excluding the stream name (eg. rtmp://host/appname). For
    # connection to Akamai, a username and password must be supplied. URI fields
    # accept format identifiers.
    destination: "OutputLocationRef" = dataclasses.field(default_factory=dict, )

    # If set to verifyAuthenticity, verify the tls certificate chain to a trusted
    # Certificate Authority (CA). This will cause rtmps outputs with self-signed
    # certificates to fail.
    certificate_mode: "RtmpOutputCertificateMode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Number of seconds to wait before retrying a connection to the Flash Media
    # server if the connection is lost.
    connection_retry_interval: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Number of retry attempts.
    num_retries: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ScheduleAction(autoboto.ShapeBase):
    """
    A single schedule action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_name",
                "ActionName",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule_action_settings",
                "ScheduleActionSettings",
                autoboto.TypeInfo(ScheduleActionSettings),
            ),
            (
                "schedule_action_start_settings",
                "ScheduleActionStartSettings",
                autoboto.TypeInfo(ScheduleActionStartSettings),
            ),
        ]

    # The name of the action, must be unique within the schedule.
    action_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Settings for this schedule action.
    schedule_action_settings: "ScheduleActionSettings" = dataclasses.field(
        default_factory=dict,
    )

    # When the action takes effect.
    schedule_action_start_settings: "ScheduleActionStartSettings" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ScheduleActionSettings(autoboto.ShapeBase):
    """
    Settings for a single schedule action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scte35_return_to_network_settings",
                "Scte35ReturnToNetworkSettings",
                autoboto.TypeInfo(Scte35ReturnToNetworkScheduleActionSettings),
            ),
            (
                "scte35_splice_insert_settings",
                "Scte35SpliceInsertSettings",
                autoboto.TypeInfo(Scte35SpliceInsertScheduleActionSettings),
            ),
            (
                "scte35_time_signal_settings",
                "Scte35TimeSignalSettings",
                autoboto.TypeInfo(Scte35TimeSignalScheduleActionSettings),
            ),
            (
                "static_image_activate_settings",
                "StaticImageActivateSettings",
                autoboto.TypeInfo(StaticImageActivateScheduleActionSettings),
            ),
            (
                "static_image_deactivate_settings",
                "StaticImageDeactivateSettings",
                autoboto.TypeInfo(StaticImageDeactivateScheduleActionSettings),
            ),
        ]

    # SCTE-35 Return to Network Settings
    scte35_return_to_network_settings: "Scte35ReturnToNetworkScheduleActionSettings" = dataclasses.field(
        default_factory=dict,
    )

    # SCTE-35 Splice Insert Settings
    scte35_splice_insert_settings: "Scte35SpliceInsertScheduleActionSettings" = dataclasses.field(
        default_factory=dict,
    )

    # SCTE-35 Time Signal Settings
    scte35_time_signal_settings: "Scte35TimeSignalScheduleActionSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Static Image Activate
    static_image_activate_settings: "StaticImageActivateScheduleActionSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Static Image Deactivate
    static_image_deactivate_settings: "StaticImageDeactivateScheduleActionSettings" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ScheduleActionStartSettings(autoboto.ShapeBase):
    """
    When the schedule action starts.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fixed_mode_schedule_action_start_settings",
                "FixedModeScheduleActionStartSettings",
                autoboto.TypeInfo(FixedModeScheduleActionStartSettings),
            ),
        ]

    # Fixed timestamp action start. Conforms to ISO-8601.
    fixed_mode_schedule_action_start_settings: "FixedModeScheduleActionStartSettings" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ScheduleDescribeResultModel(autoboto.ShapeBase):
    """
    A complete schedule description.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schedule_actions",
                "ScheduleActions",
                autoboto.TypeInfo(typing.List[ScheduleAction]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of schedule actions.
    schedule_actions: typing.List["ScheduleAction"] = dataclasses.field(
        default_factory=list,
    )

    # The next token; for use in pagination.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class Scte20Convert608To708(Enum):
    """
    Placeholder documentation for Scte20Convert608To708
    """
    DISABLED = "DISABLED"
    UPCONVERT = "UPCONVERT"


@dataclasses.dataclass
class Scte20PlusEmbeddedDestinationSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for Scte20PlusEmbeddedDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Scte20SourceSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for Scte20SourceSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "convert608_to708",
                "Convert608To708",
                autoboto.TypeInfo(Scte20Convert608To708),
            ),
            (
                "source608_channel_number",
                "Source608ChannelNumber",
                autoboto.TypeInfo(int),
            ),
        ]

    # If upconvert, 608 data is both passed through via the "608 compatibility
    # bytes" fields of the 708 wrapper as well as translated into 708. 708 data
    # present in the source content will be discarded.
    convert608_to708: "Scte20Convert608To708" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the 608/708 channel number within the video track from which to
    # extract captions. Unused for passthrough.
    source608_channel_number: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Scte27DestinationSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for Scte27DestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Scte27SourceSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for Scte27SourceSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pid",
                "Pid",
                autoboto.TypeInfo(int),
            ),
        ]

    # The pid field is used in conjunction with the caption selector languageCode
    # field as follows: \- Specify PID and Language: Extracts captions from that
    # PID; the language is "informational". \- Specify PID and omit Language:
    # Extracts the specified PID. \- Omit PID and specify Language: Extracts the
    # specified language, whichever PID that happens to be. \- Omit PID and omit
    # Language: Valid only if source is DVB-Sub that is being passed through; all
    # languages will be passed through.
    pid: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class Scte35AposNoRegionalBlackoutBehavior(Enum):
    """
    Placeholder documentation for Scte35AposNoRegionalBlackoutBehavior
    """
    FOLLOW = "FOLLOW"
    IGNORE = "IGNORE"


class Scte35AposWebDeliveryAllowedBehavior(Enum):
    """
    Placeholder documentation for Scte35AposWebDeliveryAllowedBehavior
    """
    FOLLOW = "FOLLOW"
    IGNORE = "IGNORE"


class Scte35ArchiveAllowedFlag(Enum):
    """
    SCTE-35 segmentation_descriptor archive_allowed_flag.
    """
    ARCHIVE_NOT_ALLOWED = "ARCHIVE_NOT_ALLOWED"
    ARCHIVE_ALLOWED = "ARCHIVE_ALLOWED"


@dataclasses.dataclass
class Scte35DeliveryRestrictions(autoboto.ShapeBase):
    """
    SCTE-35 Delivery Restrictions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "archive_allowed_flag",
                "ArchiveAllowedFlag",
                autoboto.TypeInfo(Scte35ArchiveAllowedFlag),
            ),
            (
                "device_restrictions",
                "DeviceRestrictions",
                autoboto.TypeInfo(Scte35DeviceRestrictions),
            ),
            (
                "no_regional_blackout_flag",
                "NoRegionalBlackoutFlag",
                autoboto.TypeInfo(Scte35NoRegionalBlackoutFlag),
            ),
            (
                "web_delivery_allowed_flag",
                "WebDeliveryAllowedFlag",
                autoboto.TypeInfo(Scte35WebDeliveryAllowedFlag),
            ),
        ]

    # SCTE-35 segmentation_descriptor archive_allowed_flag.
    archive_allowed_flag: "Scte35ArchiveAllowedFlag" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # SCTE-35 segmentation_descriptor web_delivery_allowed_flag.
    device_restrictions: "Scte35DeviceRestrictions" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # SCTE-35 segmentation_descriptor no_regional_blackout_flag.
    no_regional_blackout_flag: "Scte35NoRegionalBlackoutFlag" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # SCTE-35 segmentation_descriptor web_delivery_allowed_flag.
    web_delivery_allowed_flag: "Scte35WebDeliveryAllowedFlag" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Scte35Descriptor(autoboto.ShapeBase):
    """
    SCTE-35 Descriptor.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scte35_descriptor_settings",
                "Scte35DescriptorSettings",
                autoboto.TypeInfo(Scte35DescriptorSettings),
            ),
        ]

    # SCTE-35 Descriptor Settings.
    scte35_descriptor_settings: "Scte35DescriptorSettings" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class Scte35DescriptorSettings(autoboto.ShapeBase):
    """
    SCTE-35 Descriptor settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "segmentation_descriptor_scte35_descriptor_settings",
                "SegmentationDescriptorScte35DescriptorSettings",
                autoboto.TypeInfo(Scte35SegmentationDescriptor),
            ),
        ]

    # SCTE-35 Segmentation Descriptor.
    segmentation_descriptor_scte35_descriptor_settings: "Scte35SegmentationDescriptor" = dataclasses.field(
        default_factory=dict,
    )


class Scte35DeviceRestrictions(Enum):
    """
    SCTE-35 Device Restrictions.
    """
    NONE = "NONE"
    RESTRICT_GROUP0 = "RESTRICT_GROUP0"
    RESTRICT_GROUP1 = "RESTRICT_GROUP1"
    RESTRICT_GROUP2 = "RESTRICT_GROUP2"


class Scte35NoRegionalBlackoutFlag(Enum):
    """
    SCTE-35 segmentation_descriptor no_regional_blackout_flag.
    """
    REGIONAL_BLACKOUT = "REGIONAL_BLACKOUT"
    NO_REGIONAL_BLACKOUT = "NO_REGIONAL_BLACKOUT"


@dataclasses.dataclass
class Scte35ReturnToNetworkScheduleActionSettings(autoboto.ShapeBase):
    """
    SCTE-35 Return to Network Settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "splice_event_id",
                "SpliceEventId",
                autoboto.TypeInfo(int),
            ),
        ]

    # The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.
    splice_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class Scte35SegmentationCancelIndicator(Enum):
    """
    SCTE-35 segmentation_descriptor segmentation_event_cancel_indicator.
    """
    SEGMENTATION_EVENT_NOT_CANCELED = "SEGMENTATION_EVENT_NOT_CANCELED"
    SEGMENTATION_EVENT_CANCELED = "SEGMENTATION_EVENT_CANCELED"


@dataclasses.dataclass
class Scte35SegmentationDescriptor(autoboto.ShapeBase):
    """
    SCTE-35 Segmentation Descriptor.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "segmentation_cancel_indicator",
                "SegmentationCancelIndicator",
                autoboto.TypeInfo(Scte35SegmentationCancelIndicator),
            ),
            (
                "segmentation_event_id",
                "SegmentationEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "delivery_restrictions",
                "DeliveryRestrictions",
                autoboto.TypeInfo(Scte35DeliveryRestrictions),
            ),
            (
                "segment_num",
                "SegmentNum",
                autoboto.TypeInfo(int),
            ),
            (
                "segmentation_duration",
                "SegmentationDuration",
                autoboto.TypeInfo(int),
            ),
            (
                "segmentation_type_id",
                "SegmentationTypeId",
                autoboto.TypeInfo(int),
            ),
            (
                "segmentation_upid",
                "SegmentationUpid",
                autoboto.TypeInfo(str),
            ),
            (
                "segmentation_upid_type",
                "SegmentationUpidType",
                autoboto.TypeInfo(int),
            ),
            (
                "segments_expected",
                "SegmentsExpected",
                autoboto.TypeInfo(int),
            ),
            (
                "sub_segment_num",
                "SubSegmentNum",
                autoboto.TypeInfo(int),
            ),
            (
                "sub_segments_expected",
                "SubSegmentsExpected",
                autoboto.TypeInfo(int),
            ),
        ]

    # SCTE-35 segmentation_descriptor segmentation_event_cancel_indicator.
    segmentation_cancel_indicator: "Scte35SegmentationCancelIndicator" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # SCTE-35 segmentation_descriptor segmentation_event_id.
    segmentation_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # SCTE-35 delivery restrictions.
    delivery_restrictions: "Scte35DeliveryRestrictions" = dataclasses.field(
        default_factory=dict,
    )

    # SCTE-35 segmentation_descriptor segment_num.
    segment_num: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # SCTE-35 segmentation_descriptor segmentation_duration specified in 90 KHz
    # clock ticks.
    segmentation_duration: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # SCTE-35 segmentation_descriptor segmentation_type_id.
    segmentation_type_id: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # SCTE-35 segmentation_descriptor segmentation_upid as a hex string.
    segmentation_upid: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # SCTE-35 segmentation_descriptor segmentation_upid_type.
    segmentation_upid_type: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # SCTE-35 segmentation_descriptor segments_expected.
    segments_expected: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # SCTE-35 segmentation_descriptor sub_segment_num.
    sub_segment_num: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # SCTE-35 segmentation_descriptor sub_segments_expected.
    sub_segments_expected: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Scte35SpliceInsert(autoboto.ShapeBase):
    """
    Placeholder documentation for Scte35SpliceInsert
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ad_avail_offset",
                "AdAvailOffset",
                autoboto.TypeInfo(int),
            ),
            (
                "no_regional_blackout_flag",
                "NoRegionalBlackoutFlag",
                autoboto.TypeInfo(Scte35SpliceInsertNoRegionalBlackoutBehavior),
            ),
            (
                "web_delivery_allowed_flag",
                "WebDeliveryAllowedFlag",
                autoboto.TypeInfo(Scte35SpliceInsertWebDeliveryAllowedBehavior),
            ),
        ]

    # When specified, this offset (in milliseconds) is added to the input Ad
    # Avail PTS time. This only applies to embedded SCTE 104/35 messages and does
    # not apply to OOB messages.
    ad_avail_offset: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to
    # 0 will no longer trigger blackouts or Ad Avail slates
    no_regional_blackout_flag: "Scte35SpliceInsertNoRegionalBlackoutBehavior" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to
    # 0 will no longer trigger blackouts or Ad Avail slates
    web_delivery_allowed_flag: "Scte35SpliceInsertWebDeliveryAllowedBehavior" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class Scte35SpliceInsertNoRegionalBlackoutBehavior(Enum):
    """
    Placeholder documentation for Scte35SpliceInsertNoRegionalBlackoutBehavior
    """
    FOLLOW = "FOLLOW"
    IGNORE = "IGNORE"


@dataclasses.dataclass
class Scte35SpliceInsertScheduleActionSettings(autoboto.ShapeBase):
    """
    SCTE-35 Splice Insert Settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "splice_event_id",
                "SpliceEventId",
                autoboto.TypeInfo(int),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(int),
            ),
        ]

    # The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.
    splice_event_id: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The duration for the SCTE-35 splice_insert specified in 90KHz clock ticks.
    # When duration is not specified the expectation is that a
    # Scte35ReturnToNetwork action will be scheduled.
    duration: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class Scte35SpliceInsertWebDeliveryAllowedBehavior(Enum):
    """
    Placeholder documentation for Scte35SpliceInsertWebDeliveryAllowedBehavior
    """
    FOLLOW = "FOLLOW"
    IGNORE = "IGNORE"


@dataclasses.dataclass
class Scte35TimeSignalApos(autoboto.ShapeBase):
    """
    Placeholder documentation for Scte35TimeSignalApos
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ad_avail_offset",
                "AdAvailOffset",
                autoboto.TypeInfo(int),
            ),
            (
                "no_regional_blackout_flag",
                "NoRegionalBlackoutFlag",
                autoboto.TypeInfo(Scte35AposNoRegionalBlackoutBehavior),
            ),
            (
                "web_delivery_allowed_flag",
                "WebDeliveryAllowedFlag",
                autoboto.TypeInfo(Scte35AposWebDeliveryAllowedBehavior),
            ),
        ]

    # When specified, this offset (in milliseconds) is added to the input Ad
    # Avail PTS time. This only applies to embedded SCTE 104/35 messages and does
    # not apply to OOB messages.
    ad_avail_offset: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to
    # 0 will no longer trigger blackouts or Ad Avail slates
    no_regional_blackout_flag: "Scte35AposNoRegionalBlackoutBehavior" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to
    # 0 will no longer trigger blackouts or Ad Avail slates
    web_delivery_allowed_flag: "Scte35AposWebDeliveryAllowedBehavior" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Scte35TimeSignalScheduleActionSettings(autoboto.ShapeBase):
    """
    SCTE-35 Time Signal Settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scte35_descriptors",
                "Scte35Descriptors",
                autoboto.TypeInfo(typing.List[Scte35Descriptor]),
            ),
        ]

    # The list of SCTE-35 descriptors accompanying the SCTE-35 time_signal.
    scte35_descriptors: typing.List["Scte35Descriptor"] = dataclasses.field(
        default_factory=list,
    )


class Scte35WebDeliveryAllowedFlag(Enum):
    """
    SCTE-35 segmentation_descriptor web_delivery_allowed_flag.
    """
    WEB_DELIVERY_NOT_ALLOWED = "WEB_DELIVERY_NOT_ALLOWED"
    WEB_DELIVERY_ALLOWED = "WEB_DELIVERY_ALLOWED"


class SmoothGroupAudioOnlyTimecodeControl(Enum):
    """
    Placeholder documentation for SmoothGroupAudioOnlyTimecodeControl
    """
    PASSTHROUGH = "PASSTHROUGH"
    USE_CONFIGURED_CLOCK = "USE_CONFIGURED_CLOCK"


class SmoothGroupCertificateMode(Enum):
    """
    Placeholder documentation for SmoothGroupCertificateMode
    """
    SELF_SIGNED = "SELF_SIGNED"
    VERIFY_AUTHENTICITY = "VERIFY_AUTHENTICITY"


class SmoothGroupEventIdMode(Enum):
    """
    Placeholder documentation for SmoothGroupEventIdMode
    """
    NO_EVENT_ID = "NO_EVENT_ID"
    USE_CONFIGURED = "USE_CONFIGURED"
    USE_TIMESTAMP = "USE_TIMESTAMP"


class SmoothGroupEventStopBehavior(Enum):
    """
    Placeholder documentation for SmoothGroupEventStopBehavior
    """
    NONE = "NONE"
    SEND_EOS = "SEND_EOS"


class SmoothGroupSegmentationMode(Enum):
    """
    Placeholder documentation for SmoothGroupSegmentationMode
    """
    USE_INPUT_SEGMENTATION = "USE_INPUT_SEGMENTATION"
    USE_SEGMENT_DURATION = "USE_SEGMENT_DURATION"


class SmoothGroupSparseTrackType(Enum):
    """
    Placeholder documentation for SmoothGroupSparseTrackType
    """
    NONE = "NONE"
    SCTE_35 = "SCTE_35"


class SmoothGroupStreamManifestBehavior(Enum):
    """
    Placeholder documentation for SmoothGroupStreamManifestBehavior
    """
    DO_NOT_SEND = "DO_NOT_SEND"
    SEND = "SEND"


class SmoothGroupTimestampOffsetMode(Enum):
    """
    Placeholder documentation for SmoothGroupTimestampOffsetMode
    """
    USE_CONFIGURED_OFFSET = "USE_CONFIGURED_OFFSET"
    USE_EVENT_START_DATE = "USE_EVENT_START_DATE"


@dataclasses.dataclass
class SmpteTtDestinationSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for SmpteTtDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StandardHlsSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for StandardHlsSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "m3u8_settings",
                "M3u8Settings",
                autoboto.TypeInfo(M3u8Settings),
            ),
            (
                "audio_rendition_sets",
                "AudioRenditionSets",
                autoboto.TypeInfo(str),
            ),
        ]

    # Settings information for the .m3u8 container
    m3u8_settings: "M3u8Settings" = dataclasses.field(default_factory=dict, )

    # List all the audio groups that are used with the video output stream. Input
    # all the audio GROUP-IDs that are associated to the video, separate by ','.
    audio_rendition_sets: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartChannelRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for StartChannelRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A request to start a channel
    channel_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartChannelResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for StartChannelResponse
    """

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
                "destinations",
                "Destinations",
                autoboto.TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "egress_endpoints",
                "EgressEndpoints",
                autoboto.TypeInfo(typing.List[ChannelEgressEndpoint]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                autoboto.TypeInfo(EncoderSettings),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "input_attachments",
                "InputAttachments",
                autoboto.TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                autoboto.TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                autoboto.TypeInfo(LogLevel),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "pipelines_running_count",
                "PipelinesRunningCount",
                autoboto.TypeInfo(int),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(ChannelState),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The unique arn of the channel.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of destinations of the channel. For UDP outputs, there is one
    # destination per output. For other types (HLS, for example), there is one
    # destination per packager.
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default_factory=list,
    )

    # The endpoints where outgoing connections initiate from
    egress_endpoints: typing.List["ChannelEgressEndpoint"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for EncoderSettings
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default_factory=dict,
    )

    # The unique id of the channel.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # List of input attachments for channel.
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for InputSpecification
    input_specification: "InputSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # The log level being written to CloudWatch Logs.
    log_level: "LogLevel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the channel. (user-mutable)
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of currently healthy pipelines.
    pipelines_running_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the role assumed when running the
    # Channel.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placeholder documentation for ChannelState
    state: "ChannelState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StaticImageActivateScheduleActionSettings(autoboto.ShapeBase):
    """
    Static image activate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image",
                "Image",
                autoboto.TypeInfo(InputLocation),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(int),
            ),
            (
                "fade_in",
                "FadeIn",
                autoboto.TypeInfo(int),
            ),
            (
                "fade_out",
                "FadeOut",
                autoboto.TypeInfo(int),
            ),
            (
                "height",
                "Height",
                autoboto.TypeInfo(int),
            ),
            (
                "image_x",
                "ImageX",
                autoboto.TypeInfo(int),
            ),
            (
                "image_y",
                "ImageY",
                autoboto.TypeInfo(int),
            ),
            (
                "layer",
                "Layer",
                autoboto.TypeInfo(int),
            ),
            (
                "opacity",
                "Opacity",
                autoboto.TypeInfo(int),
            ),
            (
                "width",
                "Width",
                autoboto.TypeInfo(int),
            ),
        ]

    # The image to overlay on the video. Must be a 32 bit BMP, PNG, or TGA file.
    # Must not be larger than the input video.
    image: "InputLocation" = dataclasses.field(default_factory=dict, )

    # The duration in milliseconds for the image to remain in the video. If
    # omitted or set to 0, duration is infinite and image will remain until
    # explicitly deactivated.
    duration: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time in milliseconds for the image to fade in. Defaults to 0.
    fade_in: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time in milliseconds for the image to fade out. Defaults to 0.
    fade_out: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The height of the image when inserted into the video. Defaults to the
    # native height of the image.
    height: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placement of the left edge of the image on the horizontal axis in pixels. 0
    # is the left edge of the frame. Defaults to 0.
    image_x: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placement of the top edge of the image on the vertical axis in pixels. 0 is
    # the top edge of the frame. Defaults to 0.
    image_y: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Z order of the inserted image. Images with higher layer values will be
    # inserted on top of images with lower layer values. Permitted values are 0-7
    # inclusive. Defaults to 0.
    layer: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Opacity of image where 0 is transparent and 100 is fully opaque. Defaults
    # to 100.
    opacity: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The width of the image when inserted into the video. Defaults to the native
    # width of the image.
    width: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StaticImageDeactivateScheduleActionSettings(autoboto.ShapeBase):
    """
    Static image deactivate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fade_out",
                "FadeOut",
                autoboto.TypeInfo(int),
            ),
            (
                "layer",
                "Layer",
                autoboto.TypeInfo(int),
            ),
        ]

    # The time in milliseconds for the image to fade out. Defaults to 0.
    fade_out: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Z order of the inserted image. Images with higher layer values will be
    # inserted on top of images with lower layer values. Permitted values are 0-7
    # inclusive. Defaults to 0.
    layer: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StaticKeySettings(autoboto.ShapeBase):
    """
    Placeholder documentation for StaticKeySettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "static_key_value",
                "StaticKeyValue",
                autoboto.TypeInfo(str),
            ),
            (
                "key_provider_server",
                "KeyProviderServer",
                autoboto.TypeInfo(InputLocation),
            ),
        ]

    # Static key value as a 32 character hexadecimal string.
    static_key_value: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The URL of the license server used for protecting content.
    key_provider_server: "InputLocation" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class StopChannelRequest(autoboto.ShapeBase):
    """
    Placeholder documentation for StopChannelRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A request to stop a running channel
    channel_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopChannelResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for StopChannelResponse
    """

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
                "destinations",
                "Destinations",
                autoboto.TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "egress_endpoints",
                "EgressEndpoints",
                autoboto.TypeInfo(typing.List[ChannelEgressEndpoint]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                autoboto.TypeInfo(EncoderSettings),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "input_attachments",
                "InputAttachments",
                autoboto.TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                autoboto.TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                autoboto.TypeInfo(LogLevel),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "pipelines_running_count",
                "PipelinesRunningCount",
                autoboto.TypeInfo(int),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(ChannelState),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The unique arn of the channel.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of destinations of the channel. For UDP outputs, there is one
    # destination per output. For other types (HLS, for example), there is one
    # destination per packager.
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default_factory=list,
    )

    # The endpoints where outgoing connections initiate from
    egress_endpoints: typing.List["ChannelEgressEndpoint"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for EncoderSettings
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default_factory=dict,
    )

    # The unique id of the channel.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # List of input attachments for channel.
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default_factory=list,
    )

    # Placeholder documentation for InputSpecification
    input_specification: "InputSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # The log level being written to CloudWatch Logs.
    log_level: "LogLevel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the channel. (user-mutable)
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of currently healthy pipelines.
    pipelines_running_count: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the role assumed when running the
    # Channel.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placeholder documentation for ChannelState
    state: "ChannelState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TeletextDestinationSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for TeletextDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TeletextSourceSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for TeletextSourceSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_number",
                "PageNumber",
                autoboto.TypeInfo(str),
            ),
        ]

    # Specifies the teletext page number within the data stream from which to
    # extract captions. Range of 0x100 (256) to 0x8FF (2303). Unused for
    # passthrough. Should be specified as a hexadecimal string with no "0x"
    # prefix.
    page_number: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TimecodeConfig(autoboto.ShapeBase):
    """
    Placeholder documentation for TimecodeConfig
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source",
                "Source",
                autoboto.TypeInfo(TimecodeConfigSource),
            ),
            (
                "sync_threshold",
                "SyncThreshold",
                autoboto.TypeInfo(int),
            ),
        ]

    # Identifies the source for the timecode that will be associated with the
    # events outputs. -Embedded (embedded): Initialize the output timecode with
    # timecode from the the source. If no embedded timecode is detected in the
    # source, the system falls back to using "Start at 0" (zerobased). -System
    # Clock (systemclock): Use the UTC time. -Start at 0 (zerobased): The time of
    # the first frame of the event will be 00:00:00:00.
    source: "TimecodeConfigSource" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Threshold in frames beyond which output timecode is resynchronized to the
    # input timecode. Discrepancies below this threshold are permitted to avoid
    # unnecessary discontinuities in the output timecode. No timecode sync when
    # this is not specified.
    sync_threshold: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class TimecodeConfigSource(Enum):
    """
    Placeholder documentation for TimecodeConfigSource
    """
    EMBEDDED = "EMBEDDED"
    SYSTEMCLOCK = "SYSTEMCLOCK"
    ZEROBASED = "ZEROBASED"


@dataclasses.dataclass
class TooManyRequestsException(autoboto.ShapeBase):
    """
    Placeholder documentation for TooManyRequestsException
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

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TtmlDestinationSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for TtmlDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "style_control",
                "StyleControl",
                autoboto.TypeInfo(TtmlDestinationStyleControl),
            ),
        ]

    # When set to passthrough, passes through style and position information from
    # a TTML-like input source (TTML, SMPTE-TT, CFF-TT) to the CFF-TT output or
    # TTML output.
    style_control: "TtmlDestinationStyleControl" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class TtmlDestinationStyleControl(Enum):
    """
    Placeholder documentation for TtmlDestinationStyleControl
    """
    PASSTHROUGH = "PASSTHROUGH"
    USE_CONFIGURED = "USE_CONFIGURED"


@dataclasses.dataclass
class UdpContainerSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for UdpContainerSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "m2ts_settings",
                "M2tsSettings",
                autoboto.TypeInfo(M2tsSettings),
            ),
        ]

    # Placeholder documentation for M2tsSettings
    m2ts_settings: "M2tsSettings" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UdpGroupSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for UdpGroupSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_loss_action",
                "InputLossAction",
                autoboto.TypeInfo(InputLossActionForUdpOut),
            ),
            (
                "timed_metadata_id3_frame",
                "TimedMetadataId3Frame",
                autoboto.TypeInfo(UdpTimedMetadataId3Frame),
            ),
            (
                "timed_metadata_id3_period",
                "TimedMetadataId3Period",
                autoboto.TypeInfo(int),
            ),
        ]

    # Specifies behavior of last resort when input video is lost, and no more
    # backup inputs are available. When dropTs is selected the entire transport
    # stream will stop being emitted. When dropProgram is selected the program
    # can be dropped from the transport stream (and replaced with null packets to
    # meet the TS bitrate requirement). Or, when emitProgram is chosen the
    # transport stream will continue to be produced normally with repeat frames,
    # black frames, or slate frames substituted for the absent input video.
    input_loss_action: "InputLossActionForUdpOut" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates ID3 frame that has the timecode.
    timed_metadata_id3_frame: "UdpTimedMetadataId3Frame" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Timed Metadata interval in seconds.
    timed_metadata_id3_period: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UdpOutputSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for UdpOutputSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_settings",
                "ContainerSettings",
                autoboto.TypeInfo(UdpContainerSettings),
            ),
            (
                "destination",
                "Destination",
                autoboto.TypeInfo(OutputLocationRef),
            ),
            (
                "buffer_msec",
                "BufferMsec",
                autoboto.TypeInfo(int),
            ),
            (
                "fec_output_settings",
                "FecOutputSettings",
                autoboto.TypeInfo(FecOutputSettings),
            ),
        ]

    # Placeholder documentation for UdpContainerSettings
    container_settings: "UdpContainerSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Destination address and port number for RTP or UDP packets. Can be unicast
    # or multicast RTP or UDP (eg. rtp://239.10.10.10:5001 or
    # udp://10.100.100.100:5002).
    destination: "OutputLocationRef" = dataclasses.field(default_factory=dict, )

    # UDP output buffering in milliseconds. Larger values increase latency
    # through the transcoder but simultaneously assist the transcoder in
    # maintaining a constant, low-jitter UDP/RTP output while accommodating clock
    # recovery, input switching, input disruptions, picture reordering, etc.
    buffer_msec: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Settings for enabling and adjusting Forward Error Correction on UDP
    # outputs.
    fec_output_settings: "FecOutputSettings" = dataclasses.field(
        default_factory=dict,
    )


class UdpTimedMetadataId3Frame(Enum):
    """
    Placeholder documentation for UdpTimedMetadataId3Frame
    """
    NONE = "NONE"
    PRIV = "PRIV"
    TDRL = "TDRL"


@dataclasses.dataclass
class UnprocessableEntityException(autoboto.ShapeBase):
    """
    Placeholder documentation for UnprocessableEntityException
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "validation_errors",
                "ValidationErrors",
                autoboto.TypeInfo(typing.List[ValidationError]),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A collection of validation error responses.
    validation_errors: typing.List["ValidationError"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateChannel(autoboto.ShapeBase):
    """
    Placeholder documentation for UpdateChannel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destinations",
                "Destinations",
                autoboto.TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                autoboto.TypeInfo(EncoderSettings),
            ),
            (
                "input_attachments",
                "InputAttachments",
                autoboto.TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                autoboto.TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                autoboto.TypeInfo(LogLevel),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of output destinations for this channel.
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default_factory=list,
    )

    # The encoder settings for this channel.
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for __listOfInputAttachment
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default_factory=list,
    )

    # Specification of input for this channel (max. bitrate, resolution, codec,
    # etc.)
    input_specification: "InputSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # The log level to write to CloudWatch Logs.
    log_level: "LogLevel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the channel.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional Amazon Resource Name (ARN) of the role to assume when running
    # the Channel. If you do not specify this on an update call but the role was
    # previously set that role will be removed.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateChannelRequest(autoboto.ShapeBase):
    """
    A request to update a channel.
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
                "destinations",
                "Destinations",
                autoboto.TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                autoboto.TypeInfo(EncoderSettings),
            ),
            (
                "input_attachments",
                "InputAttachments",
                autoboto.TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                autoboto.TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                autoboto.TypeInfo(LogLevel),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # channel ID
    channel_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of output destinations for this channel.
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default_factory=list,
    )

    # The encoder settings for this channel.
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for __listOfInputAttachment
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default_factory=list,
    )

    # Specification of input for this channel (max. bitrate, resolution, codec,
    # etc.)
    input_specification: "InputSpecification" = dataclasses.field(
        default_factory=dict,
    )

    # The log level to write to CloudWatch Logs.
    log_level: "LogLevel" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the channel.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional Amazon Resource Name (ARN) of the role to assume when running
    # the Channel. If you do not specify this on an update call but the role was
    # previously set that role will be removed.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateChannelResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for UpdateChannelResponse
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "channel",
                "Channel",
                autoboto.TypeInfo(Channel),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Placeholder documentation for Channel
    channel: "Channel" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateChannelResultModel(autoboto.ShapeBase):
    """
    The updated channel's description.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel",
                "Channel",
                autoboto.TypeInfo(Channel),
            ),
        ]

    # Placeholder documentation for Channel
    channel: "Channel" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateInput(autoboto.ShapeBase):
    """
    Placeholder documentation for UpdateInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destinations",
                "Destinations",
                autoboto.TypeInfo(typing.List[InputDestinationRequest]),
            ),
            (
                "input_security_groups",
                "InputSecurityGroups",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "sources",
                "Sources",
                autoboto.TypeInfo(typing.List[InputSourceRequest]),
            ),
        ]

    # Destination settings for PUSH type inputs.
    destinations: typing.List["InputDestinationRequest"] = dataclasses.field(
        default_factory=list,
    )

    # A list of security groups referenced by IDs to attach to the input.
    input_security_groups: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Name of the input.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The source URLs for a PULL-type input. Every PULL type input needs exactly
    # two source URLs for redundancy. Only specify sources for PULL type Inputs.
    # Leave Destinations empty.
    sources: typing.List["InputSourceRequest"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateInputRequest(autoboto.ShapeBase):
    """
    A request to update an input.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_id",
                "InputId",
                autoboto.TypeInfo(str),
            ),
            (
                "destinations",
                "Destinations",
                autoboto.TypeInfo(typing.List[InputDestinationRequest]),
            ),
            (
                "input_security_groups",
                "InputSecurityGroups",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "sources",
                "Sources",
                autoboto.TypeInfo(typing.List[InputSourceRequest]),
            ),
        ]

    # Unique ID of the input.
    input_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Destination settings for PUSH type inputs.
    destinations: typing.List["InputDestinationRequest"] = dataclasses.field(
        default_factory=list,
    )

    # A list of security groups referenced by IDs to attach to the input.
    input_security_groups: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Name of the input.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The source URLs for a PULL-type input. Every PULL type input needs exactly
    # two source URLs for redundancy. Only specify sources for PULL type Inputs.
    # Leave Destinations empty.
    sources: typing.List["InputSourceRequest"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateInputResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for UpdateInputResponse
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "input",
                "Input",
                autoboto.TypeInfo(Input),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Placeholder documentation for Input
    input: "Input" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateInputResultModel(autoboto.ShapeBase):
    """
    Placeholder documentation for UpdateInputResultModel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input",
                "Input",
                autoboto.TypeInfo(Input),
            ),
        ]

    # Placeholder documentation for Input
    input: "Input" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateInputSecurityGroupRequest(autoboto.ShapeBase):
    """
    The request to update some combination of the Input Security Group name and the
    IPv4 CIDRs the Input Security Group should allow.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_security_group_id",
                "InputSecurityGroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "whitelist_rules",
                "WhitelistRules",
                autoboto.TypeInfo(typing.List[InputWhitelistRuleCidr]),
            ),
        ]

    # The id of the Input Security Group to update.
    input_security_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # List of IPv4 CIDR addresses to whitelist
    whitelist_rules: typing.List["InputWhitelistRuleCidr"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateInputSecurityGroupResponse(autoboto.OutputShapeBase):
    """
    Placeholder documentation for UpdateInputSecurityGroupResponse
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "security_group",
                "SecurityGroup",
                autoboto.TypeInfo(InputSecurityGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An Input Security Group
    security_group: "InputSecurityGroup" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateInputSecurityGroupResultModel(autoboto.ShapeBase):
    """
    Placeholder documentation for UpdateInputSecurityGroupResultModel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_group",
                "SecurityGroup",
                autoboto.TypeInfo(InputSecurityGroup),
            ),
        ]

    # An Input Security Group
    security_group: "InputSecurityGroup" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ValidationError(autoboto.ShapeBase):
    """
    Placeholder documentation for ValidationError
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "element_path",
                "ElementPath",
                autoboto.TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    element_path: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Placeholder documentation for __string
    error_message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VideoCodecSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for VideoCodecSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "h264_settings",
                "H264Settings",
                autoboto.TypeInfo(H264Settings),
            ),
        ]

    # Placeholder documentation for H264Settings
    h264_settings: "H264Settings" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class VideoDescription(autoboto.ShapeBase):
    """
    Video settings for this stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "codec_settings",
                "CodecSettings",
                autoboto.TypeInfo(VideoCodecSettings),
            ),
            (
                "height",
                "Height",
                autoboto.TypeInfo(int),
            ),
            (
                "respond_to_afd",
                "RespondToAfd",
                autoboto.TypeInfo(VideoDescriptionRespondToAfd),
            ),
            (
                "scaling_behavior",
                "ScalingBehavior",
                autoboto.TypeInfo(VideoDescriptionScalingBehavior),
            ),
            (
                "sharpness",
                "Sharpness",
                autoboto.TypeInfo(int),
            ),
            (
                "width",
                "Width",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of this VideoDescription. Outputs will use this name to uniquely
    # identify this Description. Description names should be unique within this
    # Live Event.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Video codec settings.
    codec_settings: "VideoCodecSettings" = dataclasses.field(
        default_factory=dict,
    )

    # Output video height (in pixels). Leave blank to use source video height. If
    # left blank, width must also be unspecified.
    height: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates how to respond to the AFD values in the input stream. Setting to
    # "respond" causes input video to be clipped, depending on AFD value, input
    # display aspect ratio and output display aspect ratio.
    respond_to_afd: "VideoDescriptionRespondToAfd" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When set to "stretchToOutput", automatically configures the output position
    # to stretch the video to the specified output resolution. This option will
    # override any position value.
    scaling_behavior: "VideoDescriptionScalingBehavior" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Changes the width of the anti-alias filter kernel used for scaling. Only
    # applies if scaling is being performed and antiAlias is set to true. 0 is
    # the softest setting, 100 the sharpest, and 50 recommended for most content.
    sharpness: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Output video width (in pixels). Leave out to use source video width. If
    # left out, height must also be left out. Display aspect ratio is always
    # preserved by letterboxing or pillarboxing when necessary.
    width: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class VideoDescriptionRespondToAfd(Enum):
    """
    Placeholder documentation for VideoDescriptionRespondToAfd
    """
    NONE = "NONE"
    PASSTHROUGH = "PASSTHROUGH"
    RESPOND = "RESPOND"


class VideoDescriptionScalingBehavior(Enum):
    """
    Placeholder documentation for VideoDescriptionScalingBehavior
    """
    DEFAULT = "DEFAULT"
    STRETCH_TO_OUTPUT = "STRETCH_TO_OUTPUT"


@dataclasses.dataclass
class VideoSelector(autoboto.ShapeBase):
    """
    Specifies a particular video stream within an input source. An input may have
    only a single video selector.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "color_space",
                "ColorSpace",
                autoboto.TypeInfo(VideoSelectorColorSpace),
            ),
            (
                "color_space_usage",
                "ColorSpaceUsage",
                autoboto.TypeInfo(VideoSelectorColorSpaceUsage),
            ),
            (
                "selector_settings",
                "SelectorSettings",
                autoboto.TypeInfo(VideoSelectorSettings),
            ),
        ]

    # Specifies the colorspace of an input. This setting works in tandem with
    # colorSpaceConversion to determine if any conversion will be performed.
    color_space: "VideoSelectorColorSpace" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Applies only if colorSpace is a value other than follow. This field
    # controls how the value in the colorSpace field will be used. fallback means
    # that when the input does include color space data, that data will be used,
    # but when the input has no color space data, the value in colorSpace will be
    # used. Choose fallback if your input is sometimes missing color space data,
    # but when it does have color space data, that data is correct. force means
    # to always use the value in colorSpace. Choose force if your input usually
    # has no color space data or might have unreliable color space data.
    color_space_usage: "VideoSelectorColorSpaceUsage" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The video selector settings.
    selector_settings: "VideoSelectorSettings" = dataclasses.field(
        default_factory=dict,
    )


class VideoSelectorColorSpace(Enum):
    """
    Placeholder documentation for VideoSelectorColorSpace
    """
    FOLLOW = "FOLLOW"
    REC_601 = "REC_601"
    REC_709 = "REC_709"


class VideoSelectorColorSpaceUsage(Enum):
    """
    Placeholder documentation for VideoSelectorColorSpaceUsage
    """
    FALLBACK = "FALLBACK"
    FORCE = "FORCE"


@dataclasses.dataclass
class VideoSelectorPid(autoboto.ShapeBase):
    """
    Placeholder documentation for VideoSelectorPid
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pid",
                "Pid",
                autoboto.TypeInfo(int),
            ),
        ]

    # Selects a specific PID from within a video source.
    pid: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VideoSelectorProgramId(autoboto.ShapeBase):
    """
    Placeholder documentation for VideoSelectorProgramId
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "program_id",
                "ProgramId",
                autoboto.TypeInfo(int),
            ),
        ]

    # Selects a specific program from within a multi-program transport stream. If
    # the program doesn't exist, the first program within the transport stream
    # will be selected by default.
    program_id: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VideoSelectorSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for VideoSelectorSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "video_selector_pid",
                "VideoSelectorPid",
                autoboto.TypeInfo(VideoSelectorPid),
            ),
            (
                "video_selector_program_id",
                "VideoSelectorProgramId",
                autoboto.TypeInfo(VideoSelectorProgramId),
            ),
        ]

    # Placeholder documentation for VideoSelectorPid
    video_selector_pid: "VideoSelectorPid" = dataclasses.field(
        default_factory=dict,
    )

    # Placeholder documentation for VideoSelectorProgramId
    video_selector_program_id: "VideoSelectorProgramId" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class WebvttDestinationSettings(autoboto.ShapeBase):
    """
    Placeholder documentation for WebvttDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []
