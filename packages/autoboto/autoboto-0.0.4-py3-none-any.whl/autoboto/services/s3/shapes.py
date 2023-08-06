import datetime
import typing
import autoboto
from enum import Enum
import botocore.response
import dataclasses


@dataclasses.dataclass
class AbortIncompleteMultipartUpload(autoboto.ShapeBase):
    """
    Specifies the days since the initiation of an Incomplete Multipart Upload that
    Lifecycle will wait before permanently removing all parts of the upload.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "days_after_initiation",
                "DaysAfterInitiation",
                autoboto.TypeInfo(int),
            ),
        ]

    # Indicates the number of days that must pass since initiation for Lifecycle
    # to abort an Incomplete Multipart Upload.
    days_after_initiation: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AbortMultipartUploadOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "request_charged",
                "RequestCharged",
                autoboto.TypeInfo(RequestCharged),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: "RequestCharged" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AbortMultipartUploadRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id",
                "UploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AccelerateConfiguration(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                autoboto.TypeInfo(BucketAccelerateStatus),
            ),
        ]

    # The accelerate configuration of the bucket.
    status: "BucketAccelerateStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AccessControlPolicy(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "grants",
                "Grants",
                autoboto.TypeInfo(typing.List[Grant]),
            ),
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(Owner),
            ),
        ]

    # A list of grants.
    grants: typing.List["Grant"] = dataclasses.field(default_factory=list, )
    owner: "Owner" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class AccessControlTranslation(autoboto.ShapeBase):
    """
    Container for information regarding the access control for replicas.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(OwnerOverride),
            ),
        ]

    # The override value for the owner of the replica object.
    owner: "OwnerOverride" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AnalyticsAndOperator(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The prefix to use when evaluating an AND predicate.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of tags to use when evaluating an AND predicate.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class AnalyticsConfiguration(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "storage_class_analysis",
                "StorageClassAnalysis",
                autoboto.TypeInfo(StorageClassAnalysis),
            ),
            (
                "filter",
                "Filter",
                autoboto.TypeInfo(AnalyticsFilter),
            ),
        ]

    # The identifier used to represent an analytics configuration.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If present, it indicates that data related to access patterns will be
    # collected and made available to analyze the tradeoffs between different
    # storage classes.
    storage_class_analysis: "StorageClassAnalysis" = dataclasses.field(
        default_factory=dict,
    )

    # The filter used to describe a set of objects for analyses. A filter must
    # have exactly one prefix, one tag, or one conjunction
    # (AnalyticsAndOperator). If no filter is provided, all objects will be
    # considered in any analysis.
    filter: "AnalyticsFilter" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class AnalyticsExportDestination(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_bucket_destination",
                "S3BucketDestination",
                autoboto.TypeInfo(AnalyticsS3BucketDestination),
            ),
        ]

    # A destination signifying output to an S3 bucket.
    s3_bucket_destination: "AnalyticsS3BucketDestination" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class AnalyticsFilter(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "tag",
                "Tag",
                autoboto.TypeInfo(Tag),
            ),
            (
                "and_",
                "And",
                autoboto.TypeInfo(AnalyticsAndOperator),
            ),
        ]

    # The prefix to use when evaluating an analytics filter.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tag to use when evaluating an analytics filter.
    tag: "Tag" = dataclasses.field(default_factory=dict, )

    # A conjunction (logical AND) of predicates, which is used in evaluating an
    # analytics filter. The operator must have at least two predicates.
    and_: "AnalyticsAndOperator" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class AnalyticsS3BucketDestination(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "format",
                "Format",
                autoboto.TypeInfo(AnalyticsS3ExportFileFormat),
            ),
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "bucket_account_id",
                "BucketAccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
        ]

    # The file format used when exporting data to Amazon S3.
    format: "AnalyticsS3ExportFileFormat" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon resource name (ARN) of the bucket to which data is exported.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The account ID that owns the destination bucket. If no account ID is
    # provided, the owner will not be validated prior to exporting data.
    bucket_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The prefix to use when exporting data. The exported data begins with this
    # prefix.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class AnalyticsS3ExportFileFormat(Enum):
    CSV = "CSV"


class Body(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class Bucket(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the bucket.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Date the bucket was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class BucketAccelerateStatus(Enum):
    Enabled = "Enabled"
    Suspended = "Suspended"


@dataclasses.dataclass
class BucketAlreadyExists(autoboto.ShapeBase):
    """
    The requested bucket name is not available. The bucket namespace is shared by
    all users of the system. Please select a different name and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BucketAlreadyOwnedByYou(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


class BucketCannedACL(Enum):
    private = "private"
    public_read = "public-read"
    public_read_write = "public-read-write"
    authenticated_read = "authenticated-read"


@dataclasses.dataclass
class BucketLifecycleConfiguration(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rules",
                "Rules",
                autoboto.TypeInfo(typing.List[LifecycleRule]),
            ),
        ]

    rules: typing.List["LifecycleRule"] = dataclasses.field(
        default_factory=list,
    )


class BucketLocationConstraint(Enum):
    EU = "EU"
    eu_west_1 = "eu-west-1"
    us_west_1 = "us-west-1"
    us_west_2 = "us-west-2"
    ap_south_1 = "ap-south-1"
    ap_southeast_1 = "ap-southeast-1"
    ap_southeast_2 = "ap-southeast-2"
    ap_northeast_1 = "ap-northeast-1"
    sa_east_1 = "sa-east-1"
    cn_north_1 = "cn-north-1"
    eu_central_1 = "eu-central-1"


@dataclasses.dataclass
class BucketLoggingStatus(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logging_enabled",
                "LoggingEnabled",
                autoboto.TypeInfo(LoggingEnabled),
            ),
        ]

    # Container for logging information. Presence of this element indicates that
    # logging is enabled. Parameters TargetBucket and TargetPrefix are required
    # in this case.
    logging_enabled: "LoggingEnabled" = dataclasses.field(
        default_factory=dict,
    )


class BucketLogsPermission(Enum):
    FULL_CONTROL = "FULL_CONTROL"
    READ = "READ"
    WRITE = "WRITE"


class BucketVersioningStatus(Enum):
    Enabled = "Enabled"
    Suspended = "Suspended"


@dataclasses.dataclass
class CORSConfiguration(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cors_rules",
                "CORSRules",
                autoboto.TypeInfo(typing.List[CORSRule]),
            ),
        ]

    cors_rules: typing.List["CORSRule"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CORSRule(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "allowed_methods",
                "AllowedMethods",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "allowed_origins",
                "AllowedOrigins",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "allowed_headers",
                "AllowedHeaders",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "expose_headers",
                "ExposeHeaders",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "max_age_seconds",
                "MaxAgeSeconds",
                autoboto.TypeInfo(int),
            ),
        ]

    # Identifies HTTP methods that the domain/origin specified in the rule is
    # allowed to execute.
    allowed_methods: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # One or more origins you want customers to be able to access the bucket
    # from.
    allowed_origins: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Specifies which headers are allowed in a pre-flight OPTIONS request.
    allowed_headers: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # One or more headers in the response that you want customers to be able to
    # access from their applications (for example, from a JavaScript
    # XMLHttpRequest object).
    expose_headers: typing.List[str] = dataclasses.field(default_factory=list, )

    # The time in seconds that your browser is to cache the preflight response
    # for the specified resource.
    max_age_seconds: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CSVInput(autoboto.ShapeBase):
    """
    Describes how a CSV-formatted input object is formatted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_header_info",
                "FileHeaderInfo",
                autoboto.TypeInfo(FileHeaderInfo),
            ),
            (
                "comments",
                "Comments",
                autoboto.TypeInfo(str),
            ),
            (
                "quote_escape_character",
                "QuoteEscapeCharacter",
                autoboto.TypeInfo(str),
            ),
            (
                "record_delimiter",
                "RecordDelimiter",
                autoboto.TypeInfo(str),
            ),
            (
                "field_delimiter",
                "FieldDelimiter",
                autoboto.TypeInfo(str),
            ),
            (
                "quote_character",
                "QuoteCharacter",
                autoboto.TypeInfo(str),
            ),
            (
                "allow_quoted_record_delimiter",
                "AllowQuotedRecordDelimiter",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Describes the first line of input. Valid values: None, Ignore, Use.
    file_header_info: "FileHeaderInfo" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Single character used to indicate a row should be ignored when present at
    # the start of a row.
    comments: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Single character used for escaping the quote character inside an already
    # escaped value.
    quote_escape_character: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Value used to separate individual records.
    record_delimiter: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Value used to separate individual fields in a record.
    field_delimiter: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Value used for escaping where the field delimiter is part of the value.
    quote_character: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies that CSV field values may contain quoted record delimiters and
    # such records should be allowed. Default value is FALSE. Setting this value
    # to TRUE may lower performance.
    allow_quoted_record_delimiter: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CSVOutput(autoboto.OutputShapeBase):
    """
    Describes how CSV-formatted results are formatted.
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
                "quote_fields",
                "QuoteFields",
                autoboto.TypeInfo(QuoteFields),
            ),
            (
                "quote_escape_character",
                "QuoteEscapeCharacter",
                autoboto.TypeInfo(str),
            ),
            (
                "record_delimiter",
                "RecordDelimiter",
                autoboto.TypeInfo(str),
            ),
            (
                "field_delimiter",
                "FieldDelimiter",
                autoboto.TypeInfo(str),
            ),
            (
                "quote_character",
                "QuoteCharacter",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether or not all output fields should be quoted.
    quote_fields: "QuoteFields" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Single character used for escaping the quote character inside an already
    # escaped value.
    quote_escape_character: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Value used to separate individual records.
    record_delimiter: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Value used to separate individual fields in a record.
    field_delimiter: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Value used for escaping where the field delimiter is part of the value.
    quote_character: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CloudFunctionConfiguration(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "event",
                "Event",
                autoboto.TypeInfo(Event),
            ),
            (
                "events",
                "Events",
                autoboto.TypeInfo(typing.List[Event]),
            ),
            (
                "cloud_function",
                "CloudFunction",
                autoboto.TypeInfo(str),
            ),
            (
                "invocation_role",
                "InvocationRole",
                autoboto.TypeInfo(str),
            ),
        ]

    # Optional unique identifier for configurations in a notification
    # configuration. If you don't provide one, Amazon S3 will assign an ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Bucket event for which to send notifications.
    event: "Event" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    events: typing.List["Event"] = dataclasses.field(default_factory=list, )
    cloud_function: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    invocation_role: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CommonPrefix(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
        ]

    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CompleteMultipartUploadOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "location",
                "Location",
                autoboto.TypeInfo(str),
            ),
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "expiration",
                "Expiration",
                autoboto.TypeInfo(str),
            ),
            (
                "e_tag",
                "ETag",
                autoboto.TypeInfo(str),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                autoboto.TypeInfo(ServerSideEncryption),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "request_charged",
                "RequestCharged",
                autoboto.TypeInfo(RequestCharged),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    location: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the object expiration is configured, this will contain the expiration
    # date (expiry-date) and rule ID (rule-id). The value of rule-id is URL
    # encoded.
    expiration: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Entity tag of the object.
    e_tag: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: "ServerSideEncryption" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Version of the object.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If present, specifies the ID of the AWS Key Management Service (KMS) master
    # encryption key that was used for the object.
    ssekms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: "RequestCharged" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CompleteMultipartUploadRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id",
                "UploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "multipart_upload",
                "MultipartUpload",
                autoboto.TypeInfo(CompletedMultipartUpload),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    multipart_upload: "CompletedMultipartUpload" = dataclasses.field(
        default_factory=dict,
    )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CompletedMultipartUpload(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parts",
                "Parts",
                autoboto.TypeInfo(typing.List[CompletedPart]),
            ),
        ]

    parts: typing.List["CompletedPart"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CompletedPart(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "e_tag",
                "ETag",
                autoboto.TypeInfo(str),
            ),
            (
                "part_number",
                "PartNumber",
                autoboto.TypeInfo(int),
            ),
        ]

    # Entity tag returned when the part was uploaded.
    e_tag: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Part number that identifies the part. This is a positive integer between 1
    # and 10,000.
    part_number: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class CompressionType(Enum):
    NONE = "NONE"
    GZIP = "GZIP"
    BZIP2 = "BZIP2"


@dataclasses.dataclass
class Condition(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "http_error_code_returned_equals",
                "HttpErrorCodeReturnedEquals",
                autoboto.TypeInfo(str),
            ),
            (
                "key_prefix_equals",
                "KeyPrefixEquals",
                autoboto.TypeInfo(str),
            ),
        ]

    # The HTTP error code when the redirect is applied. In the event of an error,
    # if the error code equals this value, then the specified redirect is
    # applied. Required when parent element Condition is specified and sibling
    # KeyPrefixEquals is not specified. If both are specified, then both must be
    # true for the redirect to be applied.
    http_error_code_returned_equals: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The object key name prefix when the redirect is applied. For example, to
    # redirect requests for ExamplePage.html, the key prefix will be
    # ExamplePage.html. To redirect request for all pages with the prefix docs/,
    # the key prefix will be /docs, which identifies all objects in the docs/
    # folder. Required when the parent element Condition is specified and sibling
    # HttpErrorCodeReturnedEquals is not specified. If both conditions are
    # specified, both must be true for the redirect to be applied.
    key_prefix_equals: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ContinuationEvent(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CopyObjectOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "copy_object_result",
                "CopyObjectResult",
                autoboto.TypeInfo(CopyObjectResult),
            ),
            (
                "expiration",
                "Expiration",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_source_version_id",
                "CopySourceVersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                autoboto.TypeInfo(ServerSideEncryption),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "request_charged",
                "RequestCharged",
                autoboto.TypeInfo(RequestCharged),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    copy_object_result: "CopyObjectResult" = dataclasses.field(
        default_factory=dict,
    )

    # If the object expiration is configured, the response includes this header.
    expiration: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    copy_source_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Version ID of the newly created copy.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: "ServerSideEncryption" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header confirming the encryption
    # algorithm used.
    sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header to provide round trip
    # message integrity verification of the customer-provided encryption key.
    sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If present, specifies the ID of the AWS Key Management Service (KMS) master
    # encryption key that was used for the object.
    ssekms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: "RequestCharged" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CopyObjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_source",
                "CopySource",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "acl",
                "ACL",
                autoboto.TypeInfo(ObjectCannedACL),
            ),
            (
                "cache_control",
                "CacheControl",
                autoboto.TypeInfo(str),
            ),
            (
                "content_disposition",
                "ContentDisposition",
                autoboto.TypeInfo(str),
            ),
            (
                "content_encoding",
                "ContentEncoding",
                autoboto.TypeInfo(str),
            ),
            (
                "content_language",
                "ContentLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "content_type",
                "ContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_source_if_match",
                "CopySourceIfMatch",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_source_if_modified_since",
                "CopySourceIfModifiedSince",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "copy_source_if_none_match",
                "CopySourceIfNoneMatch",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_source_if_unmodified_since",
                "CopySourceIfUnmodifiedSince",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "expires",
                "Expires",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "grant_full_control",
                "GrantFullControl",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_read",
                "GrantRead",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_read_acp",
                "GrantReadACP",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_write_acp",
                "GrantWriteACP",
                autoboto.TypeInfo(str),
            ),
            (
                "metadata",
                "Metadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metadata_directive",
                "MetadataDirective",
                autoboto.TypeInfo(MetadataDirective),
            ),
            (
                "tagging_directive",
                "TaggingDirective",
                autoboto.TypeInfo(TaggingDirective),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                autoboto.TypeInfo(ServerSideEncryption),
            ),
            (
                "storage_class",
                "StorageClass",
                autoboto.TypeInfo(StorageClass),
            ),
            (
                "website_redirect_location",
                "WebsiteRedirectLocation",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key",
                "SSECustomerKey",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_source_sse_customer_algorithm",
                "CopySourceSSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_source_sse_customer_key",
                "CopySourceSSECustomerKey",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_source_sse_customer_key_md5",
                "CopySourceSSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
            (
                "tagging",
                "Tagging",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the source bucket and key name of the source object, separated
    # by a slash (/). Must be URL-encoded.
    copy_source: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The canned ACL to apply to the object.
    acl: "ObjectCannedACL" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies caching behavior along the request/reply chain.
    cache_control: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies presentational information for the object.
    content_disposition: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies what content encodings have been applied to the object and thus
    # what decoding mechanisms must be applied to obtain the media-type
    # referenced by the Content-Type header field.
    content_encoding: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language the content is in.
    content_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A standard MIME type describing the format of the object data.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Copies the object if its entity tag (ETag) matches the specified tag.
    copy_source_if_match: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Copies the object if it has been modified since the specified time.
    copy_source_if_modified_since: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Copies the object if its entity tag (ETag) is different than the specified
    # ETag.
    copy_source_if_none_match: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Copies the object if it hasn't been modified since the specified time.
    copy_source_if_unmodified_since: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date and time at which the object is no longer cacheable.
    expires: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
    grant_full_control: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Allows grantee to read the object data and its metadata.
    grant_read: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Allows grantee to read the object ACL.
    grant_read_acp: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Allows grantee to write the ACL for the applicable object.
    grant_write_acp: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A map of metadata to store with the object in S3.
    metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether the metadata is copied from the source object or replaced
    # with metadata provided in the request.
    metadata_directive: "MetadataDirective" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether the object tag-set are copied from the source object or
    # replaced with tag-set provided in the request.
    tagging_directive: "TaggingDirective" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: "ServerSideEncryption" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of storage to use for the object. Defaults to 'STANDARD'.
    storage_class: "StorageClass" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the bucket is configured as a website, redirects requests for this
    # object to another object in the same bucket or to an external URL. Amazon
    # S3 stores the value of this header in the object metadata.
    website_redirect_location: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the algorithm to use to when encrypting the object (e.g.,
    # AES256).
    sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the customer-provided encryption key for Amazon S3 to use in
    # encrypting data. This value is used to store the object and then it is
    # discarded; Amazon does not store the encryption key. The key must be
    # appropriate for use with the algorithm specified in the x-amz-server-
    # side​-encryption​-customer-algorithm header.
    sse_customer_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the AWS KMS key ID to use for object encryption. All GET and PUT
    # requests for an object protected by AWS KMS will fail if not made via SSL
    # or using SigV4. Documentation on configuring any of the officially
    # supported AWS SDKs and CLI can be found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-
    # signature-version
    ssekms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the algorithm to use when decrypting the source object (e.g.,
    # AES256).
    copy_source_sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the customer-provided encryption key for Amazon S3 to use to
    # decrypt the source object. The encryption key provided in this header must
    # be one that was used when the source object was created.
    copy_source_sse_customer_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    copy_source_sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The tag-set for the object destination object this value must be used in
    # conjunction with the TaggingDirective. The tag-set must be encoded as URL
    # Query parameters
    tagging: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CopyObjectResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "e_tag",
                "ETag",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    e_tag: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    last_modified: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CopyPartResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "e_tag",
                "ETag",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # Entity tag of the object.
    e_tag: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Date and time at which the object was uploaded.
    last_modified: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateBucketConfiguration(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "location_constraint",
                "LocationConstraint",
                autoboto.TypeInfo(BucketLocationConstraint),
            ),
        ]

    # Specifies the region where the bucket will be created. If you don't specify
    # a region, the bucket will be created in US Standard.
    location_constraint: "BucketLocationConstraint" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateBucketOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "location",
                "Location",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    location: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateBucketRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "acl",
                "ACL",
                autoboto.TypeInfo(BucketCannedACL),
            ),
            (
                "create_bucket_configuration",
                "CreateBucketConfiguration",
                autoboto.TypeInfo(CreateBucketConfiguration),
            ),
            (
                "grant_full_control",
                "GrantFullControl",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_read",
                "GrantRead",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_read_acp",
                "GrantReadACP",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_write",
                "GrantWrite",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_write_acp",
                "GrantWriteACP",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The canned ACL to apply to the bucket.
    acl: "BucketCannedACL" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    create_bucket_configuration: "CreateBucketConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # Allows grantee the read, write, read ACP, and write ACP permissions on the
    # bucket.
    grant_full_control: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Allows grantee to list the objects in the bucket.
    grant_read: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Allows grantee to read the bucket ACL.
    grant_read_acp: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Allows grantee to create, overwrite, and delete any object in the bucket.
    grant_write: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Allows grantee to write the ACL for the applicable bucket.
    grant_write_acp: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateMultipartUploadOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "abort_date",
                "AbortDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "abort_rule_id",
                "AbortRuleId",
                autoboto.TypeInfo(str),
            ),
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id",
                "UploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                autoboto.TypeInfo(ServerSideEncryption),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "request_charged",
                "RequestCharged",
                autoboto.TypeInfo(RequestCharged),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Date when multipart upload will become eligible for abort operation by
    # lifecycle.
    abort_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Id of the lifecycle rule that makes a multipart upload eligible for abort
    # operation.
    abort_rule_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Name of the bucket to which the multipart upload was initiated.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Object key for which the multipart upload was initiated.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # ID for the initiated multipart upload.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: "ServerSideEncryption" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header confirming the encryption
    # algorithm used.
    sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header to provide round trip
    # message integrity verification of the customer-provided encryption key.
    sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If present, specifies the ID of the AWS Key Management Service (KMS) master
    # encryption key that was used for the object.
    ssekms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: "RequestCharged" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateMultipartUploadRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "acl",
                "ACL",
                autoboto.TypeInfo(ObjectCannedACL),
            ),
            (
                "cache_control",
                "CacheControl",
                autoboto.TypeInfo(str),
            ),
            (
                "content_disposition",
                "ContentDisposition",
                autoboto.TypeInfo(str),
            ),
            (
                "content_encoding",
                "ContentEncoding",
                autoboto.TypeInfo(str),
            ),
            (
                "content_language",
                "ContentLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "content_type",
                "ContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "expires",
                "Expires",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "grant_full_control",
                "GrantFullControl",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_read",
                "GrantRead",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_read_acp",
                "GrantReadACP",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_write_acp",
                "GrantWriteACP",
                autoboto.TypeInfo(str),
            ),
            (
                "metadata",
                "Metadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                autoboto.TypeInfo(ServerSideEncryption),
            ),
            (
                "storage_class",
                "StorageClass",
                autoboto.TypeInfo(StorageClass),
            ),
            (
                "website_redirect_location",
                "WebsiteRedirectLocation",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key",
                "SSECustomerKey",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
            (
                "tagging",
                "Tagging",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The canned ACL to apply to the object.
    acl: "ObjectCannedACL" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies caching behavior along the request/reply chain.
    cache_control: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies presentational information for the object.
    content_disposition: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies what content encodings have been applied to the object and thus
    # what decoding mechanisms must be applied to obtain the media-type
    # referenced by the Content-Type header field.
    content_encoding: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language the content is in.
    content_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A standard MIME type describing the format of the object data.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date and time at which the object is no longer cacheable.
    expires: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
    grant_full_control: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Allows grantee to read the object data and its metadata.
    grant_read: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Allows grantee to read the object ACL.
    grant_read_acp: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Allows grantee to write the ACL for the applicable object.
    grant_write_acp: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A map of metadata to store with the object in S3.
    metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: "ServerSideEncryption" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of storage to use for the object. Defaults to 'STANDARD'.
    storage_class: "StorageClass" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the bucket is configured as a website, redirects requests for this
    # object to another object in the same bucket or to an external URL. Amazon
    # S3 stores the value of this header in the object metadata.
    website_redirect_location: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the algorithm to use to when encrypting the object (e.g.,
    # AES256).
    sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the customer-provided encryption key for Amazon S3 to use in
    # encrypting data. This value is used to store the object and then it is
    # discarded; Amazon does not store the encryption key. The key must be
    # appropriate for use with the algorithm specified in the x-amz-server-
    # side​-encryption​-customer-algorithm header.
    sse_customer_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the AWS KMS key ID to use for object encryption. All GET and PUT
    # requests for an object protected by AWS KMS will fail if not made via SSL
    # or using SigV4. Documentation on configuring any of the officially
    # supported AWS SDKs and CLI can be found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-
    # signature-version
    ssekms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The tag-set for the object. The tag-set must be encoded as URL Query
    # parameters
    tagging: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Delete(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "objects",
                "Objects",
                autoboto.TypeInfo(typing.List[ObjectIdentifier]),
            ),
            (
                "quiet",
                "Quiet",
                autoboto.TypeInfo(bool),
            ),
        ]

    objects: typing.List["ObjectIdentifier"] = dataclasses.field(
        default_factory=list,
    )

    # Element to enable quiet mode for the request. When you add this element,
    # you must set its value to true.
    quiet: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketAnalyticsConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the bucket from which an analytics configuration is deleted.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier used to represent an analytics configuration.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketCorsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketEncryptionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the bucket containing the server-side encryption configuration
    # to delete.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketInventoryConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the bucket containing the inventory configuration to delete.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID used to identify the inventory configuration.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketLifecycleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketMetricsConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the bucket containing the metrics configuration to delete.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID used to identify the metrics configuration.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketPolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketReplicationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketTaggingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketWebsiteRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteMarkerEntry(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(Owner),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "is_latest",
                "IsLatest",
                autoboto.TypeInfo(bool),
            ),
            (
                "last_modified",
                "LastModified",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    owner: "Owner" = dataclasses.field(default_factory=dict, )

    # The object key.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Version ID of an object.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies whether the object is (true) or is not (false) the latest version
    # of an object.
    is_latest: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Date and time the object was last modified.
    last_modified: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteObjectOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "delete_marker",
                "DeleteMarker",
                autoboto.TypeInfo(bool),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "request_charged",
                "RequestCharged",
                autoboto.TypeInfo(RequestCharged),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether the versioned object that was permanently deleted was
    # (true) or was not (false) a delete marker.
    delete_marker: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Returns the version ID of the delete marker created as a result of the
    # DELETE operation.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: "RequestCharged" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteObjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "mfa",
                "MFA",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The concatenation of the authentication device's serial number, a space,
    # and the value that is displayed on your authentication device.
    mfa: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # VersionId used to reference a specific version of the object.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteObjectTaggingOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The versionId of the object the tag-set was removed from.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteObjectTaggingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The versionId of the object that the tag-set will be removed from.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteObjectsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "deleted",
                "Deleted",
                autoboto.TypeInfo(typing.List[DeletedObject]),
            ),
            (
                "request_charged",
                "RequestCharged",
                autoboto.TypeInfo(RequestCharged),
            ),
            (
                "errors",
                "Errors",
                autoboto.TypeInfo(typing.List[Error]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    deleted: typing.List["DeletedObject"] = dataclasses.field(
        default_factory=list,
    )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: "RequestCharged" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    errors: typing.List["Error"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DeleteObjectsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "delete",
                "Delete",
                autoboto.TypeInfo(Delete),
            ),
            (
                "mfa",
                "MFA",
                autoboto.TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    delete: "Delete" = dataclasses.field(default_factory=dict, )

    # The concatenation of the authentication device's serial number, a space,
    # and the value that is displayed on your authentication device.
    mfa: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeletedObject(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "delete_marker",
                "DeleteMarker",
                autoboto.TypeInfo(bool),
            ),
            (
                "delete_marker_version_id",
                "DeleteMarkerVersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    delete_marker: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    delete_marker_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Destination(autoboto.ShapeBase):
    """
    Container for replication destination information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "account",
                "Account",
                autoboto.TypeInfo(str),
            ),
            (
                "storage_class",
                "StorageClass",
                autoboto.TypeInfo(StorageClass),
            ),
            (
                "access_control_translation",
                "AccessControlTranslation",
                autoboto.TypeInfo(AccessControlTranslation),
            ),
            (
                "encryption_configuration",
                "EncryptionConfiguration",
                autoboto.TypeInfo(EncryptionConfiguration),
            ),
        ]

    # Amazon resource name (ARN) of the bucket where you want Amazon S3 to store
    # replicas of the object identified by the rule.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Account ID of the destination bucket. Currently this is only being verified
    # if Access Control Translation is enabled
    account: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The class of storage used to store the object.
    storage_class: "StorageClass" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Container for information regarding the access control for replicas.
    access_control_translation: "AccessControlTranslation" = dataclasses.field(
        default_factory=dict,
    )

    # Container for information regarding encryption based configuration for
    # replicas.
    encryption_configuration: "EncryptionConfiguration" = dataclasses.field(
        default_factory=dict,
    )


class EncodingType(Enum):
    """
    Requests Amazon S3 to encode the object keys in the response and specifies the
    encoding method to use. An object key may contain any Unicode character;
    however, XML 1.0 parser cannot parse some characters, such as characters with an
    ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you
    can add this parameter to request that Amazon S3 encode the keys in the
    response.
    """
    url = "url"


@dataclasses.dataclass
class Encryption(autoboto.ShapeBase):
    """
    Describes the server-side encryption that will be applied to the restore
    results.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption_type",
                "EncryptionType",
                autoboto.TypeInfo(ServerSideEncryption),
            ),
            (
                "kms_key_id",
                "KMSKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "kms_context",
                "KMSContext",
                autoboto.TypeInfo(str),
            ),
        ]

    # The server-side encryption algorithm used when storing job results in
    # Amazon S3 (e.g., AES256, aws:kms).
    encryption_type: "ServerSideEncryption" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the encryption type is aws:kms, this optional value specifies the AWS
    # KMS key ID to use for encryption of job results.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the encryption type is aws:kms, this optional value can be used to
    # specify the encryption context for the restore results.
    kms_context: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EncryptionConfiguration(autoboto.ShapeBase):
    """
    Container for information regarding encryption based configuration for replicas.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replica_kms_key_id",
                "ReplicaKmsKeyID",
                autoboto.TypeInfo(str),
            ),
        ]

    # The id of the KMS key used to encrypt the replica object.
    replica_kms_key_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EndEvent(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Error(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "code",
                "Code",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ErrorDocument(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
        ]

    # The object key name to use when a 4XX class error occurs.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class Event(Enum):
    """
    Bucket event for which to send notifications.
    """
    s3_ReducedRedundancyLostObject = "s3:ReducedRedundancyLostObject"
    s3_ObjectCreated_Wildcard = "s3:ObjectCreated:*"
    s3_ObjectCreated_Put = "s3:ObjectCreated:Put"
    s3_ObjectCreated_Post = "s3:ObjectCreated:Post"
    s3_ObjectCreated_Copy = "s3:ObjectCreated:Copy"
    s3_ObjectCreated_CompleteMultipartUpload = "s3:ObjectCreated:CompleteMultipartUpload"
    s3_ObjectRemoved_Wildcard = "s3:ObjectRemoved:*"
    s3_ObjectRemoved_Delete = "s3:ObjectRemoved:Delete"
    s3_ObjectRemoved_DeleteMarkerCreated = "s3:ObjectRemoved:DeleteMarkerCreated"


class ExpirationStatus(Enum):
    Enabled = "Enabled"
    Disabled = "Disabled"


class ExpressionType(Enum):
    SQL = "SQL"


class FileHeaderInfo(Enum):
    USE = "USE"
    IGNORE = "IGNORE"
    NONE = "NONE"


@dataclasses.dataclass
class FilterRule(autoboto.ShapeBase):
    """
    Container for key value pair that defines the criteria for the filter rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(FilterRuleName),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
        ]

    # Object key name prefix or suffix identifying one or more objects to which
    # the filtering rule applies. Maximum prefix length can be up to 1,024
    # characters. Overlapping prefixes and suffixes are not supported. For more
    # information, go to [Configuring Event
    # Notifications](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html)
    # in the Amazon Simple Storage Service Developer Guide.
    name: "FilterRuleName" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class FilterRuleName(Enum):
    prefix = "prefix"
    suffix = "suffix"


@dataclasses.dataclass
class GetBucketAccelerateConfigurationOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(BucketAccelerateStatus),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The accelerate configuration of the bucket.
    status: "BucketAccelerateStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBucketAccelerateConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the bucket for which the accelerate configuration is retrieved.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketAclOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(Owner),
            ),
            (
                "grants",
                "Grants",
                autoboto.TypeInfo(typing.List[Grant]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    owner: "Owner" = dataclasses.field(default_factory=dict, )

    # A list of grants.
    grants: typing.List["Grant"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class GetBucketAclRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketAnalyticsConfigurationOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "analytics_configuration",
                "AnalyticsConfiguration",
                autoboto.TypeInfo(AnalyticsConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The configuration and any analyses for the analytics filter.
    analytics_configuration: "AnalyticsConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetBucketAnalyticsConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the bucket from which an analytics configuration is retrieved.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier used to represent an analytics configuration.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketCorsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cors_rules",
                "CORSRules",
                autoboto.TypeInfo(typing.List[CORSRule]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    cors_rules: typing.List["CORSRule"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetBucketCorsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketEncryptionOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "server_side_encryption_configuration",
                "ServerSideEncryptionConfiguration",
                autoboto.TypeInfo(ServerSideEncryptionConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Container for server-side encryption configuration rules. Currently S3
    # supports one rule only.
    server_side_encryption_configuration: "ServerSideEncryptionConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetBucketEncryptionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the bucket from which the server-side encryption configuration
    # is retrieved.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketInventoryConfigurationOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "inventory_configuration",
                "InventoryConfiguration",
                autoboto.TypeInfo(InventoryConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the inventory configuration.
    inventory_configuration: "InventoryConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetBucketInventoryConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the bucket containing the inventory configuration to retrieve.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID used to identify the inventory configuration.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketLifecycleConfigurationOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rules",
                "Rules",
                autoboto.TypeInfo(typing.List[LifecycleRule]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    rules: typing.List["LifecycleRule"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetBucketLifecycleConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketLifecycleOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rules",
                "Rules",
                autoboto.TypeInfo(typing.List[Rule]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    rules: typing.List["Rule"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class GetBucketLifecycleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketLocationOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "location_constraint",
                "LocationConstraint",
                autoboto.TypeInfo(BucketLocationConstraint),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    location_constraint: "BucketLocationConstraint" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBucketLocationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketLoggingOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "logging_enabled",
                "LoggingEnabled",
                autoboto.TypeInfo(LoggingEnabled),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Container for logging information. Presence of this element indicates that
    # logging is enabled. Parameters TargetBucket and TargetPrefix are required
    # in this case.
    logging_enabled: "LoggingEnabled" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetBucketLoggingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketMetricsConfigurationOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metrics_configuration",
                "MetricsConfiguration",
                autoboto.TypeInfo(MetricsConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the metrics configuration.
    metrics_configuration: "MetricsConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetBucketMetricsConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the bucket containing the metrics configuration to retrieve.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID used to identify the metrics configuration.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketNotificationConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the bucket to get the notification configuration for.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketPolicyOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "policy",
                "Policy",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The bucket policy as a JSON document.
    policy: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketPolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketReplicationOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_configuration",
                "ReplicationConfiguration",
                autoboto.TypeInfo(ReplicationConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Container for replication rules. You can add as many as 1,000 rules. Total
    # replication configuration size can be up to 2 MB.
    replication_configuration: "ReplicationConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetBucketReplicationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketRequestPaymentOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "payer",
                "Payer",
                autoboto.TypeInfo(Payer),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies who pays for the download and request fees.
    payer: "Payer" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketRequestPaymentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketTaggingOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tag_set",
                "TagSet",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    tag_set: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class GetBucketTaggingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketVersioningOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(BucketVersioningStatus),
            ),
            (
                "mfa_delete",
                "MFADelete",
                autoboto.TypeInfo(MFADeleteStatus),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The versioning state of the bucket.
    status: "BucketVersioningStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether MFA delete is enabled in the bucket versioning
    # configuration. This element is only returned if the bucket has been
    # configured with MFA delete. If the bucket has never been so configured,
    # this element is not returned.
    mfa_delete: "MFADeleteStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBucketVersioningRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketWebsiteOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "redirect_all_requests_to",
                "RedirectAllRequestsTo",
                autoboto.TypeInfo(RedirectAllRequestsTo),
            ),
            (
                "index_document",
                "IndexDocument",
                autoboto.TypeInfo(IndexDocument),
            ),
            (
                "error_document",
                "ErrorDocument",
                autoboto.TypeInfo(ErrorDocument),
            ),
            (
                "routing_rules",
                "RoutingRules",
                autoboto.TypeInfo(typing.List[RoutingRule]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    redirect_all_requests_to: "RedirectAllRequestsTo" = dataclasses.field(
        default_factory=dict,
    )
    index_document: "IndexDocument" = dataclasses.field(default_factory=dict, )
    error_document: "ErrorDocument" = dataclasses.field(default_factory=dict, )
    routing_rules: typing.List["RoutingRule"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetBucketWebsiteRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetObjectAclOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(Owner),
            ),
            (
                "grants",
                "Grants",
                autoboto.TypeInfo(typing.List[Grant]),
            ),
            (
                "request_charged",
                "RequestCharged",
                autoboto.TypeInfo(RequestCharged),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    owner: "Owner" = dataclasses.field(default_factory=dict, )

    # A list of grants.
    grants: typing.List["Grant"] = dataclasses.field(default_factory=list, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: "RequestCharged" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetObjectAclRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # VersionId used to reference a specific version of the object.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetObjectOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "body",
                "Body",
                autoboto.TypeInfo(typing.Any),
            ),
            (
                "delete_marker",
                "DeleteMarker",
                autoboto.TypeInfo(bool),
            ),
            (
                "accept_ranges",
                "AcceptRanges",
                autoboto.TypeInfo(str),
            ),
            (
                "expiration",
                "Expiration",
                autoboto.TypeInfo(str),
            ),
            (
                "restore",
                "Restore",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "content_length",
                "ContentLength",
                autoboto.TypeInfo(int),
            ),
            (
                "e_tag",
                "ETag",
                autoboto.TypeInfo(str),
            ),
            (
                "missing_meta",
                "MissingMeta",
                autoboto.TypeInfo(int),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "cache_control",
                "CacheControl",
                autoboto.TypeInfo(str),
            ),
            (
                "content_disposition",
                "ContentDisposition",
                autoboto.TypeInfo(str),
            ),
            (
                "content_encoding",
                "ContentEncoding",
                autoboto.TypeInfo(str),
            ),
            (
                "content_language",
                "ContentLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "content_range",
                "ContentRange",
                autoboto.TypeInfo(str),
            ),
            (
                "content_type",
                "ContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "expires",
                "Expires",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "website_redirect_location",
                "WebsiteRedirectLocation",
                autoboto.TypeInfo(str),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                autoboto.TypeInfo(ServerSideEncryption),
            ),
            (
                "metadata",
                "Metadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "storage_class",
                "StorageClass",
                autoboto.TypeInfo(StorageClass),
            ),
            (
                "request_charged",
                "RequestCharged",
                autoboto.TypeInfo(RequestCharged),
            ),
            (
                "replication_status",
                "ReplicationStatus",
                autoboto.TypeInfo(ReplicationStatus),
            ),
            (
                "parts_count",
                "PartsCount",
                autoboto.TypeInfo(int),
            ),
            (
                "tag_count",
                "TagCount",
                autoboto.TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Object data.
    body: typing.Any = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies whether the object retrieved was (true) or was not (false) a
    # Delete Marker. If false, this response header does not appear in the
    # response.
    delete_marker: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    accept_ranges: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the object expiration is configured (see PUT Bucket lifecycle), the
    # response includes this header. It includes the expiry-date and rule-id key
    # value pairs providing object expiration information. The value of the rule-
    # id is URL encoded.
    expiration: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Provides information about object restoration operation and expiration time
    # of the restored object copy.
    restore: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Last modified date of the object
    last_modified: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Size of the body in bytes.
    content_length: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An ETag is an opaque identifier assigned by a web server to a specific
    # version of a resource found at a URL
    e_tag: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This is set to the number of metadata entries not returned in x-amz-meta
    # headers. This can happen if you create metadata using an API like SOAP that
    # supports more flexible metadata than the REST API. For example, using SOAP,
    # you can create metadata whose values are not legal HTTP headers.
    missing_meta: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Version of the object.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies caching behavior along the request/reply chain.
    cache_control: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies presentational information for the object.
    content_disposition: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies what content encodings have been applied to the object and thus
    # what decoding mechanisms must be applied to obtain the media-type
    # referenced by the Content-Type header field.
    content_encoding: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language the content is in.
    content_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The portion of the object returned in the response.
    content_range: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A standard MIME type describing the format of the object data.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date and time at which the object is no longer cacheable.
    expires: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the bucket is configured as a website, redirects requests for this
    # object to another object in the same bucket or to an external URL. Amazon
    # S3 stores the value of this header in the object metadata.
    website_redirect_location: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: "ServerSideEncryption" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A map of metadata to store with the object in S3.
    metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header confirming the encryption
    # algorithm used.
    sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header to provide round trip
    # message integrity verification of the customer-provided encryption key.
    sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If present, specifies the ID of the AWS Key Management Service (KMS) master
    # encryption key that was used for the object.
    ssekms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    storage_class: "StorageClass" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: "RequestCharged" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    replication_status: "ReplicationStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The count of parts this object has.
    parts_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of tags, if any, on the object.
    tag_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetObjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "if_match",
                "IfMatch",
                autoboto.TypeInfo(str),
            ),
            (
                "if_modified_since",
                "IfModifiedSince",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "if_none_match",
                "IfNoneMatch",
                autoboto.TypeInfo(str),
            ),
            (
                "if_unmodified_since",
                "IfUnmodifiedSince",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "range",
                "Range",
                autoboto.TypeInfo(str),
            ),
            (
                "response_cache_control",
                "ResponseCacheControl",
                autoboto.TypeInfo(str),
            ),
            (
                "response_content_disposition",
                "ResponseContentDisposition",
                autoboto.TypeInfo(str),
            ),
            (
                "response_content_encoding",
                "ResponseContentEncoding",
                autoboto.TypeInfo(str),
            ),
            (
                "response_content_language",
                "ResponseContentLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "response_content_type",
                "ResponseContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "response_expires",
                "ResponseExpires",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key",
                "SSECustomerKey",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
            (
                "part_number",
                "PartNumber",
                autoboto.TypeInfo(int),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Return the object only if its entity tag (ETag) is the same as the one
    # specified, otherwise return a 412 (precondition failed).
    if_match: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Return the object only if it has been modified since the specified time,
    # otherwise return a 304 (not modified).
    if_modified_since: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Return the object only if its entity tag (ETag) is different from the one
    # specified, otherwise return a 304 (not modified).
    if_none_match: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Return the object only if it has not been modified since the specified
    # time, otherwise return a 412 (precondition failed).
    if_unmodified_since: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Downloads the specified range bytes of an object. For more information
    # about the HTTP Range header, go to
    # http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.
    range: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Sets the Cache-Control header of the response.
    response_cache_control: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Sets the Content-Disposition header of the response
    response_content_disposition: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Sets the Content-Encoding header of the response.
    response_content_encoding: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Sets the Content-Language header of the response.
    response_content_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Sets the Content-Type header of the response.
    response_content_type: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Sets the Expires header of the response.
    response_expires: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # VersionId used to reference a specific version of the object.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the algorithm to use to when encrypting the object (e.g.,
    # AES256).
    sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the customer-provided encryption key for Amazon S3 to use in
    # encrypting data. This value is used to store the object and then it is
    # discarded; Amazon does not store the encryption key. The key must be
    # appropriate for use with the algorithm specified in the x-amz-server-
    # side​-encryption​-customer-algorithm header.
    sse_customer_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Part number of the object being read. This is a positive integer between 1
    # and 10,000. Effectively performs a 'ranged' GET request for the part
    # specified. Useful for downloading just a part of an object.
    part_number: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetObjectTaggingOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tag_set",
                "TagSet",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    tag_set: typing.List["Tag"] = dataclasses.field(default_factory=list, )
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetObjectTaggingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetObjectTorrentOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "body",
                "Body",
                autoboto.TypeInfo(typing.Any),
            ),
            (
                "request_charged",
                "RequestCharged",
                autoboto.TypeInfo(RequestCharged),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    body: typing.Any = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: "RequestCharged" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetObjectTorrentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GlacierJobParameters(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tier",
                "Tier",
                autoboto.TypeInfo(Tier),
            ),
        ]

    # Glacier retrieval tier at which the restore will be processed.
    tier: "Tier" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Grant(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "grantee",
                "Grantee",
                autoboto.TypeInfo(Grantee),
            ),
            (
                "permission",
                "Permission",
                autoboto.TypeInfo(Permission),
            ),
        ]

    grantee: "Grantee" = dataclasses.field(default_factory=dict, )

    # Specifies the permission given to the grantee.
    permission: "Permission" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Grantee(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(Type),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "email_address",
                "EmailAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "ID",
                autoboto.TypeInfo(str),
            ),
            (
                "uri",
                "URI",
                autoboto.TypeInfo(str),
            ),
        ]

    # Type of grantee
    type: "Type" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Screen name of the grantee.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Email address of the grantee.
    email_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The canonical user ID of the grantee.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # URI of the grantee group.
    uri: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HeadBucketRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HeadObjectOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "delete_marker",
                "DeleteMarker",
                autoboto.TypeInfo(bool),
            ),
            (
                "accept_ranges",
                "AcceptRanges",
                autoboto.TypeInfo(str),
            ),
            (
                "expiration",
                "Expiration",
                autoboto.TypeInfo(str),
            ),
            (
                "restore",
                "Restore",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "content_length",
                "ContentLength",
                autoboto.TypeInfo(int),
            ),
            (
                "e_tag",
                "ETag",
                autoboto.TypeInfo(str),
            ),
            (
                "missing_meta",
                "MissingMeta",
                autoboto.TypeInfo(int),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "cache_control",
                "CacheControl",
                autoboto.TypeInfo(str),
            ),
            (
                "content_disposition",
                "ContentDisposition",
                autoboto.TypeInfo(str),
            ),
            (
                "content_encoding",
                "ContentEncoding",
                autoboto.TypeInfo(str),
            ),
            (
                "content_language",
                "ContentLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "content_type",
                "ContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "expires",
                "Expires",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "website_redirect_location",
                "WebsiteRedirectLocation",
                autoboto.TypeInfo(str),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                autoboto.TypeInfo(ServerSideEncryption),
            ),
            (
                "metadata",
                "Metadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "storage_class",
                "StorageClass",
                autoboto.TypeInfo(StorageClass),
            ),
            (
                "request_charged",
                "RequestCharged",
                autoboto.TypeInfo(RequestCharged),
            ),
            (
                "replication_status",
                "ReplicationStatus",
                autoboto.TypeInfo(ReplicationStatus),
            ),
            (
                "parts_count",
                "PartsCount",
                autoboto.TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether the object retrieved was (true) or was not (false) a
    # Delete Marker. If false, this response header does not appear in the
    # response.
    delete_marker: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    accept_ranges: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If the object expiration is configured (see PUT Bucket lifecycle), the
    # response includes this header. It includes the expiry-date and rule-id key
    # value pairs providing object expiration information. The value of the rule-
    # id is URL encoded.
    expiration: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Provides information about object restoration operation and expiration time
    # of the restored object copy.
    restore: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Last modified date of the object
    last_modified: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Size of the body in bytes.
    content_length: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An ETag is an opaque identifier assigned by a web server to a specific
    # version of a resource found at a URL
    e_tag: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This is set to the number of metadata entries not returned in x-amz-meta
    # headers. This can happen if you create metadata using an API like SOAP that
    # supports more flexible metadata than the REST API. For example, using SOAP,
    # you can create metadata whose values are not legal HTTP headers.
    missing_meta: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Version of the object.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies caching behavior along the request/reply chain.
    cache_control: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies presentational information for the object.
    content_disposition: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies what content encodings have been applied to the object and thus
    # what decoding mechanisms must be applied to obtain the media-type
    # referenced by the Content-Type header field.
    content_encoding: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language the content is in.
    content_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A standard MIME type describing the format of the object data.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date and time at which the object is no longer cacheable.
    expires: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the bucket is configured as a website, redirects requests for this
    # object to another object in the same bucket or to an external URL. Amazon
    # S3 stores the value of this header in the object metadata.
    website_redirect_location: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: "ServerSideEncryption" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A map of metadata to store with the object in S3.
    metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header confirming the encryption
    # algorithm used.
    sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header to provide round trip
    # message integrity verification of the customer-provided encryption key.
    sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If present, specifies the ID of the AWS Key Management Service (KMS) master
    # encryption key that was used for the object.
    ssekms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    storage_class: "StorageClass" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: "RequestCharged" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    replication_status: "ReplicationStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The count of parts this object has.
    parts_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HeadObjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "if_match",
                "IfMatch",
                autoboto.TypeInfo(str),
            ),
            (
                "if_modified_since",
                "IfModifiedSince",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "if_none_match",
                "IfNoneMatch",
                autoboto.TypeInfo(str),
            ),
            (
                "if_unmodified_since",
                "IfUnmodifiedSince",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "range",
                "Range",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key",
                "SSECustomerKey",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
            (
                "part_number",
                "PartNumber",
                autoboto.TypeInfo(int),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Return the object only if its entity tag (ETag) is the same as the one
    # specified, otherwise return a 412 (precondition failed).
    if_match: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Return the object only if it has been modified since the specified time,
    # otherwise return a 304 (not modified).
    if_modified_since: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Return the object only if its entity tag (ETag) is different from the one
    # specified, otherwise return a 304 (not modified).
    if_none_match: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Return the object only if it has not been modified since the specified
    # time, otherwise return a 412 (precondition failed).
    if_unmodified_since: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Downloads the specified range bytes of an object. For more information
    # about the HTTP Range header, go to
    # http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.
    range: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # VersionId used to reference a specific version of the object.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the algorithm to use to when encrypting the object (e.g.,
    # AES256).
    sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the customer-provided encryption key for Amazon S3 to use in
    # encrypting data. This value is used to store the object and then it is
    # discarded; Amazon does not store the encryption key. The key must be
    # appropriate for use with the algorithm specified in the x-amz-server-
    # side​-encryption​-customer-algorithm header.
    sse_customer_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Part number of the object being read. This is a positive integer between 1
    # and 10,000. Effectively performs a 'ranged' HEAD request for the part
    # specified. Useful querying about the size of the part and the number of
    # parts in this object.
    part_number: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IndexDocument(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "suffix",
                "Suffix",
                autoboto.TypeInfo(str),
            ),
        ]

    # A suffix that is appended to a request that is for a directory on the
    # website endpoint (e.g. if the suffix is index.html and you make a request
    # to samplebucket/images/ the data that is returned will be for the object
    # with the key name images/index.html) The suffix must not be empty and must
    # not include a slash character.
    suffix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Initiator(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "ID",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
        ]

    # If the principal is an AWS account, it provides the Canonical User ID. If
    # the principal is an IAM User, it provides a user ARN value.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Name of the Principal.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InputSerialization(autoboto.ShapeBase):
    """
    Describes the serialization format of the object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "csv",
                "CSV",
                autoboto.TypeInfo(CSVInput),
            ),
            (
                "compression_type",
                "CompressionType",
                autoboto.TypeInfo(CompressionType),
            ),
            (
                "json",
                "JSON",
                autoboto.TypeInfo(JSONInput),
            ),
        ]

    # Describes the serialization of a CSV-encoded object.
    csv: "CSVInput" = dataclasses.field(default_factory=dict, )

    # Specifies object's compression format. Valid values: NONE, GZIP, BZIP2.
    # Default Value: NONE.
    compression_type: "CompressionType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies JSON as object's input serialization format.
    json: "JSONInput" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class InventoryConfiguration(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination",
                "Destination",
                autoboto.TypeInfo(InventoryDestination),
            ),
            (
                "is_enabled",
                "IsEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "included_object_versions",
                "IncludedObjectVersions",
                autoboto.TypeInfo(InventoryIncludedObjectVersions),
            ),
            (
                "schedule",
                "Schedule",
                autoboto.TypeInfo(InventorySchedule),
            ),
            (
                "filter",
                "Filter",
                autoboto.TypeInfo(InventoryFilter),
            ),
            (
                "optional_fields",
                "OptionalFields",
                autoboto.TypeInfo(typing.List[InventoryOptionalField]),
            ),
        ]

    # Contains information about where to publish the inventory results.
    destination: "InventoryDestination" = dataclasses.field(
        default_factory=dict,
    )

    # Specifies whether the inventory is enabled or disabled.
    is_enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID used to identify the inventory configuration.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies which object version(s) to included in the inventory results.
    included_object_versions: "InventoryIncludedObjectVersions" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the schedule for generating inventory results.
    schedule: "InventorySchedule" = dataclasses.field(default_factory=dict, )

    # Specifies an inventory filter. The inventory only includes objects that
    # meet the filter's criteria.
    filter: "InventoryFilter" = dataclasses.field(default_factory=dict, )

    # Contains the optional fields that are included in the inventory results.
    optional_fields: typing.List["InventoryOptionalField"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class InventoryDestination(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_bucket_destination",
                "S3BucketDestination",
                autoboto.TypeInfo(InventoryS3BucketDestination),
            ),
        ]

    # Contains the bucket name, file format, bucket owner (optional), and prefix
    # (optional) where inventory results are published.
    s3_bucket_destination: "InventoryS3BucketDestination" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class InventoryEncryption(autoboto.ShapeBase):
    """
    Contains the type of server-side encryption used to encrypt the inventory
    results.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sses3",
                "SSES3",
                autoboto.TypeInfo(SSES3),
            ),
            (
                "ssekms",
                "SSEKMS",
                autoboto.TypeInfo(SSEKMS),
            ),
        ]

    # Specifies the use of SSE-S3 to encrypt delievered Inventory reports.
    sses3: "SSES3" = dataclasses.field(default_factory=dict, )

    # Specifies the use of SSE-KMS to encrypt delievered Inventory reports.
    ssekms: "SSEKMS" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class InventoryFilter(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
        ]

    # The prefix that an object must have to be included in the inventory
    # results.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class InventoryFormat(Enum):
    CSV = "CSV"
    ORC = "ORC"


class InventoryFrequency(Enum):
    Daily = "Daily"
    Weekly = "Weekly"


class InventoryIncludedObjectVersions(Enum):
    All = "All"
    Current = "Current"


class InventoryOptionalField(Enum):
    Size = "Size"
    LastModifiedDate = "LastModifiedDate"
    StorageClass = "StorageClass"
    ETag = "ETag"
    IsMultipartUploaded = "IsMultipartUploaded"
    ReplicationStatus = "ReplicationStatus"
    EncryptionStatus = "EncryptionStatus"


@dataclasses.dataclass
class InventoryS3BucketDestination(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "format",
                "Format",
                autoboto.TypeInfo(InventoryFormat),
            ),
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "encryption",
                "Encryption",
                autoboto.TypeInfo(InventoryEncryption),
            ),
        ]

    # The Amazon resource name (ARN) of the bucket where inventory results will
    # be published.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the output format of the inventory results.
    format: "InventoryFormat" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID of the account that owns the destination bucket.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The prefix that is prepended to all inventory results.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Contains the type of server-side encryption used to encrypt the inventory
    # results.
    encryption: "InventoryEncryption" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class InventorySchedule(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "frequency",
                "Frequency",
                autoboto.TypeInfo(InventoryFrequency),
            ),
        ]

    # Specifies how frequently inventory results are produced.
    frequency: "InventoryFrequency" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class JSONInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(JSONType),
            ),
        ]

    # The type of JSON. Valid values: Document, Lines.
    type: "JSONType" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class JSONOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "record_delimiter",
                "RecordDelimiter",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The value used to separate individual records in the output.
    record_delimiter: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class JSONType(Enum):
    DOCUMENT = "DOCUMENT"
    LINES = "LINES"


@dataclasses.dataclass
class LambdaFunctionConfiguration(autoboto.ShapeBase):
    """
    Container for specifying the AWS Lambda notification configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lambda_function_arn",
                "LambdaFunctionArn",
                autoboto.TypeInfo(str),
            ),
            (
                "events",
                "Events",
                autoboto.TypeInfo(typing.List[Event]),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "filter",
                "Filter",
                autoboto.TypeInfo(NotificationConfigurationFilter),
            ),
        ]

    # Lambda cloud function ARN that Amazon S3 can invoke when it detects events
    # of the specified type.
    lambda_function_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    events: typing.List["Event"] = dataclasses.field(default_factory=list, )

    # Optional unique identifier for configurations in a notification
    # configuration. If you don't provide one, Amazon S3 will assign an ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Container for object key name filtering rules. For information about key
    # name filtering, go to [Configuring Event
    # Notifications](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html)
    # in the Amazon Simple Storage Service Developer Guide.
    filter: "NotificationConfigurationFilter" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class LifecycleConfiguration(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rules",
                "Rules",
                autoboto.TypeInfo(typing.List[Rule]),
            ),
        ]

    rules: typing.List["Rule"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class LifecycleExpiration(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "date",
                "Date",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "days",
                "Days",
                autoboto.TypeInfo(int),
            ),
            (
                "expired_object_delete_marker",
                "ExpiredObjectDeleteMarker",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Indicates at what date the object is to be moved or deleted. Should be in
    # GMT ISO 8601 Format.
    date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates the lifetime, in days, of the objects that are subject to the
    # rule. The value must be a non-zero positive integer.
    days: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether Amazon S3 will remove a delete marker with no noncurrent
    # versions. If set to true, the delete marker will be expired; if set to
    # false the policy takes no action. This cannot be specified with Days or
    # Date in a Lifecycle Expiration Policy.
    expired_object_delete_marker: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LifecycleRule(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                autoboto.TypeInfo(ExpirationStatus),
            ),
            (
                "expiration",
                "Expiration",
                autoboto.TypeInfo(LifecycleExpiration),
            ),
            (
                "id",
                "ID",
                autoboto.TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "filter",
                "Filter",
                autoboto.TypeInfo(LifecycleRuleFilter),
            ),
            (
                "transitions",
                "Transitions",
                autoboto.TypeInfo(typing.List[Transition]),
            ),
            (
                "noncurrent_version_transitions",
                "NoncurrentVersionTransitions",
                autoboto.TypeInfo(typing.List[NoncurrentVersionTransition]),
            ),
            (
                "noncurrent_version_expiration",
                "NoncurrentVersionExpiration",
                autoboto.TypeInfo(NoncurrentVersionExpiration),
            ),
            (
                "abort_incomplete_multipart_upload",
                "AbortIncompleteMultipartUpload",
                autoboto.TypeInfo(AbortIncompleteMultipartUpload),
            ),
        ]

    # If 'Enabled', the rule is currently being applied. If 'Disabled', the rule
    # is not currently being applied.
    status: "ExpirationStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    expiration: "LifecycleExpiration" = dataclasses.field(
        default_factory=dict,
    )

    # Unique identifier for the rule. The value cannot be longer than 255
    # characters.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Prefix identifying one or more objects to which the rule applies. This is
    # deprecated; use Filter instead.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Filter is used to identify objects that a Lifecycle Rule applies to. A
    # Filter must have exactly one of Prefix, Tag, or And specified.
    filter: "LifecycleRuleFilter" = dataclasses.field(default_factory=dict, )
    transitions: typing.List["Transition"] = dataclasses.field(
        default_factory=list,
    )
    noncurrent_version_transitions: typing.List["NoncurrentVersionTransition"
                                               ] = dataclasses.field(
                                                   default_factory=list,
                                               )

    # Specifies when noncurrent object versions expire. Upon expiration, Amazon
    # S3 permanently deletes the noncurrent object versions. You set this
    # lifecycle configuration action on a bucket that has versioning enabled (or
    # suspended) to request that Amazon S3 delete noncurrent object versions at a
    # specific period in the object's lifetime.
    noncurrent_version_expiration: "NoncurrentVersionExpiration" = dataclasses.field(
        default_factory=dict,
    )

    # Specifies the days since the initiation of an Incomplete Multipart Upload
    # that Lifecycle will wait before permanently removing all parts of the
    # upload.
    abort_incomplete_multipart_upload: "AbortIncompleteMultipartUpload" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class LifecycleRuleAndOperator(autoboto.ShapeBase):
    """
    This is used in a Lifecycle Rule Filter to apply a logical AND to two or more
    predicates. The Lifecycle Rule will apply to any object matching all of the
    predicates configured inside the And operator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # All of these tags must exist in the object's tag set in order for the rule
    # to apply.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class LifecycleRuleFilter(autoboto.ShapeBase):
    """
    The Filter is used to identify objects that a Lifecycle Rule applies to. A
    Filter must have exactly one of Prefix, Tag, or And specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "tag",
                "Tag",
                autoboto.TypeInfo(Tag),
            ),
            (
                "and_",
                "And",
                autoboto.TypeInfo(LifecycleRuleAndOperator),
            ),
        ]

    # Prefix identifying one or more objects to which the rule applies.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This tag must exist in the object's tag set in order for the rule to apply.
    tag: "Tag" = dataclasses.field(default_factory=dict, )

    # This is used in a Lifecycle Rule Filter to apply a logical AND to two or
    # more predicates. The Lifecycle Rule will apply to any object matching all
    # of the predicates configured inside the And operator.
    and_: "LifecycleRuleAndOperator" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ListBucketAnalyticsConfigurationsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                autoboto.TypeInfo(bool),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "next_continuation_token",
                "NextContinuationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "analytics_configuration_list",
                "AnalyticsConfigurationList",
                autoboto.TypeInfo(typing.List[AnalyticsConfiguration]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the returned list of analytics configurations is
    # complete. A value of true indicates that the list is not complete and the
    # NextContinuationToken will be provided for a subsequent request.
    is_truncated: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ContinuationToken that represents where this request began.
    continuation_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # NextContinuationToken is sent when isTruncated is true, which indicates
    # that there are more analytics configurations to list. The next request must
    # include this NextContinuationToken. The token is obfuscated and is not a
    # usable value.
    next_continuation_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The list of analytics configurations for a bucket.
    analytics_configuration_list: typing.List["AnalyticsConfiguration"
                                             ] = dataclasses.field(
                                                 default_factory=list,
                                             )


@dataclasses.dataclass
class ListBucketAnalyticsConfigurationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the bucket from which analytics configurations are retrieved.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ContinuationToken that represents a placeholder from where this request
    # should begin.
    continuation_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListBucketInventoryConfigurationsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "inventory_configuration_list",
                "InventoryConfigurationList",
                autoboto.TypeInfo(typing.List[InventoryConfiguration]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                autoboto.TypeInfo(bool),
            ),
            (
                "next_continuation_token",
                "NextContinuationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If sent in the request, the marker that is used as a starting point for
    # this inventory configuration list response.
    continuation_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The list of inventory configurations for a bucket.
    inventory_configuration_list: typing.List["InventoryConfiguration"
                                             ] = dataclasses.field(
                                                 default_factory=list,
                                             )

    # Indicates whether the returned list of inventory configurations is
    # truncated in this response. A value of true indicates that the list is
    # truncated.
    is_truncated: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The marker used to continue this inventory configuration listing. Use the
    # NextContinuationToken from this response to continue the listing in a
    # subsequent request. The continuation token is an opaque value that Amazon
    # S3 understands.
    next_continuation_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListBucketInventoryConfigurationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the bucket containing the inventory configurations to retrieve.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The marker used to continue an inventory configuration listing that has
    # been truncated. Use the NextContinuationToken from a previously truncated
    # list response to continue the listing. The continuation token is an opaque
    # value that Amazon S3 understands.
    continuation_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListBucketMetricsConfigurationsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                autoboto.TypeInfo(bool),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "next_continuation_token",
                "NextContinuationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "metrics_configuration_list",
                "MetricsConfigurationList",
                autoboto.TypeInfo(typing.List[MetricsConfiguration]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the returned list of metrics configurations is complete.
    # A value of true indicates that the list is not complete and the
    # NextContinuationToken will be provided for a subsequent request.
    is_truncated: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The marker that is used as a starting point for this metrics configuration
    # list response. This value is present if it was sent in the request.
    continuation_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The marker used to continue a metrics configuration listing that has been
    # truncated. Use the NextContinuationToken from a previously truncated list
    # response to continue the listing. The continuation token is an opaque value
    # that Amazon S3 understands.
    next_continuation_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The list of metrics configurations for a bucket.
    metrics_configuration_list: typing.List["MetricsConfiguration"
                                           ] = dataclasses.field(
                                               default_factory=list,
                                           )


@dataclasses.dataclass
class ListBucketMetricsConfigurationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the bucket containing the metrics configurations to retrieve.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The marker that is used to continue a metrics configuration listing that
    # has been truncated. Use the NextContinuationToken from a previously
    # truncated list response to continue the listing. The continuation token is
    # an opaque value that Amazon S3 understands.
    continuation_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListBucketsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "buckets",
                "Buckets",
                autoboto.TypeInfo(typing.List[Bucket]),
            ),
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(Owner),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    buckets: typing.List["Bucket"] = dataclasses.field(default_factory=list, )
    owner: "Owner" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ListMultipartUploadsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key_marker",
                "KeyMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id_marker",
                "UploadIdMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "next_key_marker",
                "NextKeyMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "delimiter",
                "Delimiter",
                autoboto.TypeInfo(str),
            ),
            (
                "next_upload_id_marker",
                "NextUploadIdMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "max_uploads",
                "MaxUploads",
                autoboto.TypeInfo(int),
            ),
            (
                "is_truncated",
                "IsTruncated",
                autoboto.TypeInfo(bool),
            ),
            (
                "uploads",
                "Uploads",
                autoboto.TypeInfo(typing.List[MultipartUpload]),
            ),
            (
                "common_prefixes",
                "CommonPrefixes",
                autoboto.TypeInfo(typing.List[CommonPrefix]),
            ),
            (
                "encoding_type",
                "EncodingType",
                autoboto.TypeInfo(EncodingType),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Name of the bucket to which the multipart upload was initiated.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The key at or after which the listing began.
    key_marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Upload ID after which listing began.
    upload_id_marker: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When a list is truncated, this element specifies the value that should be
    # used for the key-marker request parameter in a subsequent request.
    next_key_marker: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When a prefix is provided in the request, this field contains the specified
    # prefix. The result contains only keys starting with the specified prefix.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    delimiter: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When a list is truncated, this element specifies the value that should be
    # used for the upload-id-marker request parameter in a subsequent request.
    next_upload_id_marker: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Maximum number of multipart uploads that could have been included in the
    # response.
    max_uploads: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether the returned list of multipart uploads is truncated. A
    # value of true indicates that the list was truncated. The list can be
    # truncated if the number of multipart uploads exceeds the limit allowed or
    # specified by max uploads.
    is_truncated: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    uploads: typing.List["MultipartUpload"] = dataclasses.field(
        default_factory=list,
    )
    common_prefixes: typing.List["CommonPrefix"] = dataclasses.field(
        default_factory=list,
    )

    # Encoding type used by Amazon S3 to encode object keys in the response.
    encoding_type: "EncodingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListMultipartUploadsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "delimiter",
                "Delimiter",
                autoboto.TypeInfo(str),
            ),
            (
                "encoding_type",
                "EncodingType",
                autoboto.TypeInfo(EncodingType),
            ),
            (
                "key_marker",
                "KeyMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "max_uploads",
                "MaxUploads",
                autoboto.TypeInfo(int),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id_marker",
                "UploadIdMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Character you use to group keys.
    delimiter: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Requests Amazon S3 to encode the object keys in the response and specifies
    # the encoding method to use. An object key may contain any Unicode
    # character; however, XML 1.0 parser cannot parse some characters, such as
    # characters with an ASCII value from 0 to 10. For characters that are not
    # supported in XML 1.0, you can add this parameter to request that Amazon S3
    # encode the keys in the response.
    encoding_type: "EncodingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Together with upload-id-marker, this parameter specifies the multipart
    # upload after which listing should begin.
    key_marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Sets the maximum number of multipart uploads, from 1 to 1,000, to return in
    # the response body. 1,000 is the maximum number of uploads that can be
    # returned in a response.
    max_uploads: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Lists in-progress uploads only for those keys that begin with the specified
    # prefix.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Together with key-marker, specifies the multipart upload after which
    # listing should begin. If key-marker is not specified, the upload-id-marker
    # parameter is ignored.
    upload_id_marker: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListObjectVersionsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                autoboto.TypeInfo(bool),
            ),
            (
                "key_marker",
                "KeyMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id_marker",
                "VersionIdMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "next_key_marker",
                "NextKeyMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "next_version_id_marker",
                "NextVersionIdMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "versions",
                "Versions",
                autoboto.TypeInfo(typing.List[ObjectVersion]),
            ),
            (
                "delete_markers",
                "DeleteMarkers",
                autoboto.TypeInfo(typing.List[DeleteMarkerEntry]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "delimiter",
                "Delimiter",
                autoboto.TypeInfo(str),
            ),
            (
                "max_keys",
                "MaxKeys",
                autoboto.TypeInfo(int),
            ),
            (
                "common_prefixes",
                "CommonPrefixes",
                autoboto.TypeInfo(typing.List[CommonPrefix]),
            ),
            (
                "encoding_type",
                "EncodingType",
                autoboto.TypeInfo(EncodingType),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A flag that indicates whether or not Amazon S3 returned all of the results
    # that satisfied the search criteria. If your results were truncated, you can
    # make a follow-up paginated request using the NextKeyMarker and
    # NextVersionIdMarker response parameters as a starting place in another
    # request to return the rest of the results.
    is_truncated: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Marks the last Key returned in a truncated response.
    key_marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    version_id_marker: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Use this value for the key marker request parameter in a subsequent
    # request.
    next_key_marker: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Use this value for the next version id marker parameter in a subsequent
    # request.
    next_version_id_marker: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    versions: typing.List["ObjectVersion"] = dataclasses.field(
        default_factory=list,
    )
    delete_markers: typing.List["DeleteMarkerEntry"] = dataclasses.field(
        default_factory=list,
    )
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    delimiter: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    max_keys: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    common_prefixes: typing.List["CommonPrefix"] = dataclasses.field(
        default_factory=list,
    )

    # Encoding type used by Amazon S3 to encode object keys in the response.
    encoding_type: "EncodingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListObjectVersionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "delimiter",
                "Delimiter",
                autoboto.TypeInfo(str),
            ),
            (
                "encoding_type",
                "EncodingType",
                autoboto.TypeInfo(EncodingType),
            ),
            (
                "key_marker",
                "KeyMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "max_keys",
                "MaxKeys",
                autoboto.TypeInfo(int),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id_marker",
                "VersionIdMarker",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A delimiter is a character you use to group keys.
    delimiter: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Requests Amazon S3 to encode the object keys in the response and specifies
    # the encoding method to use. An object key may contain any Unicode
    # character; however, XML 1.0 parser cannot parse some characters, such as
    # characters with an ASCII value from 0 to 10. For characters that are not
    # supported in XML 1.0, you can add this parameter to request that Amazon S3
    # encode the keys in the response.
    encoding_type: "EncodingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the key to start with when listing objects in a bucket.
    key_marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Sets the maximum number of keys returned in the response. The response
    # might contain fewer keys but will never contain more.
    max_keys: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Limits the response to keys that begin with the specified prefix.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the object version you want to start listing from.
    version_id_marker: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListObjectsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                autoboto.TypeInfo(bool),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "next_marker",
                "NextMarker",
                autoboto.TypeInfo(str),
            ),
            (
                "contents",
                "Contents",
                autoboto.TypeInfo(typing.List[Object]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "delimiter",
                "Delimiter",
                autoboto.TypeInfo(str),
            ),
            (
                "max_keys",
                "MaxKeys",
                autoboto.TypeInfo(int),
            ),
            (
                "common_prefixes",
                "CommonPrefixes",
                autoboto.TypeInfo(typing.List[CommonPrefix]),
            ),
            (
                "encoding_type",
                "EncodingType",
                autoboto.TypeInfo(EncodingType),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A flag that indicates whether or not Amazon S3 returned all of the results
    # that satisfied the search criteria.
    is_truncated: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When response is truncated (the IsTruncated element value in the response
    # is true), you can use the key name in this field as marker in the
    # subsequent request to get next set of objects. Amazon S3 lists objects in
    # alphabetical order Note: This element is returned only if you have
    # delimiter request parameter specified. If response does not include the
    # NextMaker and it is truncated, you can use the value of the last Key in the
    # response as the marker in the subsequent request to get the next set of
    # object keys.
    next_marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    contents: typing.List["Object"] = dataclasses.field(default_factory=list, )
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    delimiter: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    max_keys: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    common_prefixes: typing.List["CommonPrefix"] = dataclasses.field(
        default_factory=list,
    )

    # Encoding type used by Amazon S3 to encode object keys in the response.
    encoding_type: "EncodingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListObjectsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "delimiter",
                "Delimiter",
                autoboto.TypeInfo(str),
            ),
            (
                "encoding_type",
                "EncodingType",
                autoboto.TypeInfo(EncodingType),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "max_keys",
                "MaxKeys",
                autoboto.TypeInfo(int),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A delimiter is a character you use to group keys.
    delimiter: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Requests Amazon S3 to encode the object keys in the response and specifies
    # the encoding method to use. An object key may contain any Unicode
    # character; however, XML 1.0 parser cannot parse some characters, such as
    # characters with an ASCII value from 0 to 10. For characters that are not
    # supported in XML 1.0, you can add this parameter to request that Amazon S3
    # encode the keys in the response.
    encoding_type: "EncodingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the key to start with when listing objects in a bucket.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Sets the maximum number of keys returned in the response. The response
    # might contain fewer keys but will never contain more.
    max_keys: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Limits the response to keys that begin with the specified prefix.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # list objects request. Bucket owners need not specify this parameter in
    # their requests.
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListObjectsV2Output(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                autoboto.TypeInfo(bool),
            ),
            (
                "contents",
                "Contents",
                autoboto.TypeInfo(typing.List[Object]),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "delimiter",
                "Delimiter",
                autoboto.TypeInfo(str),
            ),
            (
                "max_keys",
                "MaxKeys",
                autoboto.TypeInfo(int),
            ),
            (
                "common_prefixes",
                "CommonPrefixes",
                autoboto.TypeInfo(typing.List[CommonPrefix]),
            ),
            (
                "encoding_type",
                "EncodingType",
                autoboto.TypeInfo(EncodingType),
            ),
            (
                "key_count",
                "KeyCount",
                autoboto.TypeInfo(int),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "next_continuation_token",
                "NextContinuationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "start_after",
                "StartAfter",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A flag that indicates whether or not Amazon S3 returned all of the results
    # that satisfied the search criteria.
    is_truncated: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Metadata about each object returned.
    contents: typing.List["Object"] = dataclasses.field(default_factory=list, )

    # Name of the bucket to list.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Limits the response to keys that begin with the specified prefix.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A delimiter is a character you use to group keys.
    delimiter: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Sets the maximum number of keys returned in the response. The response
    # might contain fewer keys but will never contain more.
    max_keys: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # CommonPrefixes contains all (if there are any) keys between Prefix and the
    # next occurrence of the string specified by delimiter
    common_prefixes: typing.List["CommonPrefix"] = dataclasses.field(
        default_factory=list,
    )

    # Encoding type used by Amazon S3 to encode object keys in the response.
    encoding_type: "EncodingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # KeyCount is the number of keys returned with this request. KeyCount will
    # always be less than equals to MaxKeys field. Say you ask for 50 keys, your
    # result will include less than equals 50 keys
    key_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # ContinuationToken indicates Amazon S3 that the list is being continued on
    # this bucket with a token. ContinuationToken is obfuscated and is not a real
    # key
    continuation_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # NextContinuationToken is sent when isTruncated is true which means there
    # are more keys in the bucket that can be listed. The next list requests to
    # Amazon S3 can be continued with this NextContinuationToken.
    # NextContinuationToken is obfuscated and is not a real key
    next_continuation_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # StartAfter is where you want Amazon S3 to start listing from. Amazon S3
    # starts listing after this specified key. StartAfter can be any key in the
    # bucket
    start_after: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListObjectsV2Request(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "delimiter",
                "Delimiter",
                autoboto.TypeInfo(str),
            ),
            (
                "encoding_type",
                "EncodingType",
                autoboto.TypeInfo(EncodingType),
            ),
            (
                "max_keys",
                "MaxKeys",
                autoboto.TypeInfo(int),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                autoboto.TypeInfo(str),
            ),
            (
                "fetch_owner",
                "FetchOwner",
                autoboto.TypeInfo(bool),
            ),
            (
                "start_after",
                "StartAfter",
                autoboto.TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
        ]

    # Name of the bucket to list.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A delimiter is a character you use to group keys.
    delimiter: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Encoding type used by Amazon S3 to encode object keys in the response.
    encoding_type: "EncodingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Sets the maximum number of keys returned in the response. The response
    # might contain fewer keys but will never contain more.
    max_keys: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Limits the response to keys that begin with the specified prefix.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # ContinuationToken indicates Amazon S3 that the list is being continued on
    # this bucket with a token. ContinuationToken is obfuscated and is not a real
    # key
    continuation_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The owner field is not present in listV2 by default, if you want to return
    # owner field with each key in the result then set the fetch owner field to
    # true
    fetch_owner: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # StartAfter is where you want Amazon S3 to start listing from. Amazon S3
    # starts listing after this specified key. StartAfter can be any key in the
    # bucket
    start_after: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # list objects request in V2 style. Bucket owners need not specify this
    # parameter in their requests.
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListPartsOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "abort_date",
                "AbortDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "abort_rule_id",
                "AbortRuleId",
                autoboto.TypeInfo(str),
            ),
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id",
                "UploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "part_number_marker",
                "PartNumberMarker",
                autoboto.TypeInfo(int),
            ),
            (
                "next_part_number_marker",
                "NextPartNumberMarker",
                autoboto.TypeInfo(int),
            ),
            (
                "max_parts",
                "MaxParts",
                autoboto.TypeInfo(int),
            ),
            (
                "is_truncated",
                "IsTruncated",
                autoboto.TypeInfo(bool),
            ),
            (
                "parts",
                "Parts",
                autoboto.TypeInfo(typing.List[Part]),
            ),
            (
                "initiator",
                "Initiator",
                autoboto.TypeInfo(Initiator),
            ),
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(Owner),
            ),
            (
                "storage_class",
                "StorageClass",
                autoboto.TypeInfo(StorageClass),
            ),
            (
                "request_charged",
                "RequestCharged",
                autoboto.TypeInfo(RequestCharged),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Date when multipart upload will become eligible for abort operation by
    # lifecycle.
    abort_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Id of the lifecycle rule that makes a multipart upload eligible for abort
    # operation.
    abort_rule_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Name of the bucket to which the multipart upload was initiated.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Object key for which the multipart upload was initiated.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Upload ID identifying the multipart upload whose parts are being listed.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Part number after which listing begins.
    part_number_marker: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When a list is truncated, this element specifies the last part in the list,
    # as well as the value to use for the part-number-marker request parameter in
    # a subsequent request.
    next_part_number_marker: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Maximum number of parts that were allowed in the response.
    max_parts: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether the returned list of parts is truncated.
    is_truncated: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    parts: typing.List["Part"] = dataclasses.field(default_factory=list, )

    # Identifies who initiated the multipart upload.
    initiator: "Initiator" = dataclasses.field(default_factory=dict, )
    owner: "Owner" = dataclasses.field(default_factory=dict, )

    # The class of storage used to store the object.
    storage_class: "StorageClass" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: "RequestCharged" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListPartsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id",
                "UploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "max_parts",
                "MaxParts",
                autoboto.TypeInfo(int),
            ),
            (
                "part_number_marker",
                "PartNumberMarker",
                autoboto.TypeInfo(int),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Upload ID identifying the multipart upload whose parts are being listed.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Sets the maximum number of parts to return.
    max_parts: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the part after which listing should begin. Only parts with higher
    # part numbers will be listed.
    part_number_marker: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LoggingEnabled(autoboto.ShapeBase):
    """
    Container for logging information. Presence of this element indicates that
    logging is enabled. Parameters TargetBucket and TargetPrefix are required in
    this case.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_bucket",
                "TargetBucket",
                autoboto.TypeInfo(str),
            ),
            (
                "target_prefix",
                "TargetPrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "target_grants",
                "TargetGrants",
                autoboto.TypeInfo(typing.List[TargetGrant]),
            ),
        ]

    # Specifies the bucket where you want Amazon S3 to store server access logs.
    # You can have your logs delivered to any bucket that you own, including the
    # same bucket that is being logged. You can also configure multiple buckets
    # to deliver their logs to the same target bucket. In this case you should
    # choose a different TargetPrefix for each source bucket so that the
    # delivered log files can be distinguished by key.
    target_bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This element lets you specify a prefix for the keys that the log files will
    # be stored under.
    target_prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    target_grants: typing.List["TargetGrant"] = dataclasses.field(
        default_factory=list,
    )


class MFADelete(Enum):
    Enabled = "Enabled"
    Disabled = "Disabled"


class MFADeleteStatus(Enum):
    Enabled = "Enabled"
    Disabled = "Disabled"


class MetadataDirective(Enum):
    COPY = "COPY"
    REPLACE = "REPLACE"


@dataclasses.dataclass
class MetadataEntry(autoboto.ShapeBase):
    """
    A metadata key-value pair to store with an object.
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
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
        ]

    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricsAndOperator(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The prefix used when evaluating an AND predicate.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The list of tags used when evaluating an AND predicate.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class MetricsConfiguration(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "filter",
                "Filter",
                autoboto.TypeInfo(MetricsFilter),
            ),
        ]

    # The ID used to identify the metrics configuration.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies a metrics configuration filter. The metrics configuration will
    # only include objects that meet the filter's criteria. A filter must be a
    # prefix, a tag, or a conjunction (MetricsAndOperator).
    filter: "MetricsFilter" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class MetricsFilter(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "tag",
                "Tag",
                autoboto.TypeInfo(Tag),
            ),
            (
                "and_",
                "And",
                autoboto.TypeInfo(MetricsAndOperator),
            ),
        ]

    # The prefix used when evaluating a metrics filter.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tag used when evaluating a metrics filter.
    tag: "Tag" = dataclasses.field(default_factory=dict, )

    # A conjunction (logical AND) of predicates, which is used in evaluating a
    # metrics filter. The operator must have at least two predicates, and an
    # object must match all of the predicates in order for the filter to apply.
    and_: "MetricsAndOperator" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class MultipartUpload(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "upload_id",
                "UploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "initiated",
                "Initiated",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "storage_class",
                "StorageClass",
                autoboto.TypeInfo(StorageClass),
            ),
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(Owner),
            ),
            (
                "initiator",
                "Initiator",
                autoboto.TypeInfo(Initiator),
            ),
        ]

    # Upload ID that identifies the multipart upload.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Key of the object for which the multipart upload was initiated.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Date and time at which the multipart upload was initiated.
    initiated: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The class of storage used to store the object.
    storage_class: "StorageClass" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    owner: "Owner" = dataclasses.field(default_factory=dict, )

    # Identifies who initiated the multipart upload.
    initiator: "Initiator" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class NoSuchBucket(autoboto.ShapeBase):
    """
    The specified bucket does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NoSuchKey(autoboto.ShapeBase):
    """
    The specified key does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NoSuchUpload(autoboto.ShapeBase):
    """
    The specified multipart upload does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NoncurrentVersionExpiration(autoboto.ShapeBase):
    """
    Specifies when noncurrent object versions expire. Upon expiration, Amazon S3
    permanently deletes the noncurrent object versions. You set this lifecycle
    configuration action on a bucket that has versioning enabled (or suspended) to
    request that Amazon S3 delete noncurrent object versions at a specific period in
    the object's lifetime.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "noncurrent_days",
                "NoncurrentDays",
                autoboto.TypeInfo(int),
            ),
        ]

    # Specifies the number of days an object is noncurrent before Amazon S3 can
    # perform the associated action. For information about the noncurrent days
    # calculations, see [How Amazon S3 Calculates When an Object Became
    # Noncurrent](http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-
    # control.html) in the Amazon Simple Storage Service Developer Guide.
    noncurrent_days: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NoncurrentVersionTransition(autoboto.ShapeBase):
    """
    Container for the transition rule that describes when noncurrent objects
    transition to the STANDARD_IA, ONEZONE_IA or GLACIER storage class. If your
    bucket is versioning-enabled (or versioning is suspended), you can set this
    action to request that Amazon S3 transition noncurrent object versions to the
    STANDARD_IA, ONEZONE_IA or GLACIER storage class at a specific period in the
    object's lifetime.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "noncurrent_days",
                "NoncurrentDays",
                autoboto.TypeInfo(int),
            ),
            (
                "storage_class",
                "StorageClass",
                autoboto.TypeInfo(TransitionStorageClass),
            ),
        ]

    # Specifies the number of days an object is noncurrent before Amazon S3 can
    # perform the associated action. For information about the noncurrent days
    # calculations, see [How Amazon S3 Calculates When an Object Became
    # Noncurrent](http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-
    # control.html) in the Amazon Simple Storage Service Developer Guide.
    noncurrent_days: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The class of storage used to store the object.
    storage_class: "TransitionStorageClass" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NotificationConfiguration(autoboto.ShapeBase):
    """
    Container for specifying the notification configuration of the bucket. If this
    element is empty, notifications are turned off on the bucket.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "topic_configurations",
                "TopicConfigurations",
                autoboto.TypeInfo(typing.List[TopicConfiguration]),
            ),
            (
                "queue_configurations",
                "QueueConfigurations",
                autoboto.TypeInfo(typing.List[QueueConfiguration]),
            ),
            (
                "lambda_function_configurations",
                "LambdaFunctionConfigurations",
                autoboto.TypeInfo(typing.List[LambdaFunctionConfiguration]),
            ),
        ]

    topic_configurations: typing.List["TopicConfiguration"] = dataclasses.field(
        default_factory=list,
    )
    queue_configurations: typing.List["QueueConfiguration"] = dataclasses.field(
        default_factory=list,
    )
    lambda_function_configurations: typing.List["LambdaFunctionConfiguration"
                                               ] = dataclasses.field(
                                                   default_factory=list,
                                               )


@dataclasses.dataclass
class NotificationConfigurationDeprecated(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "topic_configuration",
                "TopicConfiguration",
                autoboto.TypeInfo(TopicConfigurationDeprecated),
            ),
            (
                "queue_configuration",
                "QueueConfiguration",
                autoboto.TypeInfo(QueueConfigurationDeprecated),
            ),
            (
                "cloud_function_configuration",
                "CloudFunctionConfiguration",
                autoboto.TypeInfo(CloudFunctionConfiguration),
            ),
        ]

    topic_configuration: "TopicConfigurationDeprecated" = dataclasses.field(
        default_factory=dict,
    )
    queue_configuration: "QueueConfigurationDeprecated" = dataclasses.field(
        default_factory=dict,
    )
    cloud_function_configuration: "CloudFunctionConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class NotificationConfigurationFilter(autoboto.ShapeBase):
    """
    Container for object key name filtering rules. For information about key name
    filtering, go to [Configuring Event
    Notifications](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html)
    in the Amazon Simple Storage Service Developer Guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(S3KeyFilter),
            ),
        ]

    # Container for object key name prefix and suffix filtering rules.
    key: "S3KeyFilter" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class Object(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "e_tag",
                "ETag",
                autoboto.TypeInfo(str),
            ),
            (
                "size",
                "Size",
                autoboto.TypeInfo(int),
            ),
            (
                "storage_class",
                "StorageClass",
                autoboto.TypeInfo(ObjectStorageClass),
            ),
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(Owner),
            ),
        ]

    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    last_modified: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    e_tag: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The class of storage used to store the object.
    storage_class: "ObjectStorageClass" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    owner: "Owner" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ObjectAlreadyInActiveTierError(autoboto.ShapeBase):
    """
    This operation is not allowed against this storage tier
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class ObjectCannedACL(Enum):
    private = "private"
    public_read = "public-read"
    public_read_write = "public-read-write"
    authenticated_read = "authenticated-read"
    aws_exec_read = "aws-exec-read"
    bucket_owner_read = "bucket-owner-read"
    bucket_owner_full_control = "bucket-owner-full-control"


@dataclasses.dataclass
class ObjectIdentifier(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Key name of the object to delete.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # VersionId for the specific version of the object to delete.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ObjectNotInActiveTierError(autoboto.ShapeBase):
    """
    The source object of the COPY operation is not in the active tier and is only
    stored in Amazon Glacier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class ObjectStorageClass(Enum):
    STANDARD = "STANDARD"
    REDUCED_REDUNDANCY = "REDUCED_REDUNDANCY"
    GLACIER = "GLACIER"
    STANDARD_IA = "STANDARD_IA"
    ONEZONE_IA = "ONEZONE_IA"


@dataclasses.dataclass
class ObjectVersion(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "e_tag",
                "ETag",
                autoboto.TypeInfo(str),
            ),
            (
                "size",
                "Size",
                autoboto.TypeInfo(int),
            ),
            (
                "storage_class",
                "StorageClass",
                autoboto.TypeInfo(ObjectVersionStorageClass),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "is_latest",
                "IsLatest",
                autoboto.TypeInfo(bool),
            ),
            (
                "last_modified",
                "LastModified",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(Owner),
            ),
        ]

    e_tag: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Size in bytes of the object.
    size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The class of storage used to store the object.
    storage_class: "ObjectVersionStorageClass" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The object key.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Version ID of an object.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies whether the object is (true) or is not (false) the latest version
    # of an object.
    is_latest: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Date and time the object was last modified.
    last_modified: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    owner: "Owner" = dataclasses.field(default_factory=dict, )


class ObjectVersionStorageClass(Enum):
    STANDARD = "STANDARD"


@dataclasses.dataclass
class OutputLocation(autoboto.ShapeBase):
    """
    Describes the location where the restore job's output is stored.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3",
                "S3",
                autoboto.TypeInfo(S3Location),
            ),
        ]

    # Describes an S3 location that will receive the results of the restore
    # request.
    s3: "S3Location" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class OutputSerialization(autoboto.ShapeBase):
    """
    Describes how results of the Select job are serialized.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "csv",
                "CSV",
                autoboto.TypeInfo(CSVOutput),
            ),
            (
                "json",
                "JSON",
                autoboto.TypeInfo(JSONOutput),
            ),
        ]

    # Describes the serialization of CSV-encoded Select results.
    csv: "CSVOutput" = dataclasses.field(default_factory=dict, )

    # Specifies JSON as request's output serialization format.
    json: "JSONOutput" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class Owner(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "display_name",
                "DisplayName",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "ID",
                autoboto.TypeInfo(str),
            ),
        ]

    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class OwnerOverride(Enum):
    Destination = "Destination"


@dataclasses.dataclass
class Part(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "part_number",
                "PartNumber",
                autoboto.TypeInfo(int),
            ),
            (
                "last_modified",
                "LastModified",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "e_tag",
                "ETag",
                autoboto.TypeInfo(str),
            ),
            (
                "size",
                "Size",
                autoboto.TypeInfo(int),
            ),
        ]

    # Part number identifying the part. This is a positive integer between 1 and
    # 10,000.
    part_number: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Date and time at which the part was uploaded.
    last_modified: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Entity tag returned when the part was uploaded.
    e_tag: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Size of the uploaded part data.
    size: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class Payer(Enum):
    Requester = "Requester"
    BucketOwner = "BucketOwner"


class Permission(Enum):
    FULL_CONTROL = "FULL_CONTROL"
    WRITE = "WRITE"
    WRITE_ACP = "WRITE_ACP"
    READ = "READ"
    READ_ACP = "READ_ACP"


@dataclasses.dataclass
class Progress(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bytes_scanned",
                "BytesScanned",
                autoboto.TypeInfo(int),
            ),
            (
                "bytes_processed",
                "BytesProcessed",
                autoboto.TypeInfo(int),
            ),
            (
                "bytes_returned",
                "BytesReturned",
                autoboto.TypeInfo(int),
            ),
        ]

    # Current number of object bytes scanned.
    bytes_scanned: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Current number of uncompressed object bytes processed.
    bytes_processed: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Current number of bytes of records payload data returned.
    bytes_returned: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ProgressEvent(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "details",
                "Details",
                autoboto.TypeInfo(Progress),
            ),
        ]

    # The Progress event details.
    details: "Progress" = dataclasses.field(default_factory=dict, )


class Protocol(Enum):
    http = "http"
    https = "https"


@dataclasses.dataclass
class PutBucketAccelerateConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "accelerate_configuration",
                "AccelerateConfiguration",
                autoboto.TypeInfo(AccelerateConfiguration),
            ),
        ]

    # Name of the bucket for which the accelerate configuration is set.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the Accelerate Configuration you want to set for the bucket.
    accelerate_configuration: "AccelerateConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutBucketAclRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "acl",
                "ACL",
                autoboto.TypeInfo(BucketCannedACL),
            ),
            (
                "access_control_policy",
                "AccessControlPolicy",
                autoboto.TypeInfo(AccessControlPolicy),
            ),
            (
                "content_md5",
                "ContentMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_full_control",
                "GrantFullControl",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_read",
                "GrantRead",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_read_acp",
                "GrantReadACP",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_write",
                "GrantWrite",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_write_acp",
                "GrantWriteACP",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The canned ACL to apply to the bucket.
    acl: "BucketCannedACL" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    access_control_policy: "AccessControlPolicy" = dataclasses.field(
        default_factory=dict,
    )
    content_md5: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Allows grantee the read, write, read ACP, and write ACP permissions on the
    # bucket.
    grant_full_control: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Allows grantee to list the objects in the bucket.
    grant_read: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Allows grantee to read the bucket ACL.
    grant_read_acp: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Allows grantee to create, overwrite, and delete any object in the bucket.
    grant_write: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Allows grantee to write the ACL for the applicable bucket.
    grant_write_acp: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutBucketAnalyticsConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "analytics_configuration",
                "AnalyticsConfiguration",
                autoboto.TypeInfo(AnalyticsConfiguration),
            ),
        ]

    # The name of the bucket to which an analytics configuration is stored.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The identifier used to represent an analytics configuration.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The configuration and any analyses for the analytics filter.
    analytics_configuration: "AnalyticsConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutBucketCorsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "cors_configuration",
                "CORSConfiguration",
                autoboto.TypeInfo(CORSConfiguration),
            ),
            (
                "content_md5",
                "ContentMD5",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    cors_configuration: "CORSConfiguration" = dataclasses.field(
        default_factory=dict,
    )
    content_md5: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketEncryptionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "server_side_encryption_configuration",
                "ServerSideEncryptionConfiguration",
                autoboto.TypeInfo(ServerSideEncryptionConfiguration),
            ),
            (
                "content_md5",
                "ContentMD5",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the bucket for which the server-side encryption configuration
    # is set.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Container for server-side encryption configuration rules. Currently S3
    # supports one rule only.
    server_side_encryption_configuration: "ServerSideEncryptionConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The base64-encoded 128-bit MD5 digest of the server-side encryption
    # configuration.
    content_md5: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketInventoryConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "inventory_configuration",
                "InventoryConfiguration",
                autoboto.TypeInfo(InventoryConfiguration),
            ),
        ]

    # The name of the bucket where the inventory configuration will be stored.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID used to identify the inventory configuration.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the inventory configuration.
    inventory_configuration: "InventoryConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutBucketLifecycleConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "lifecycle_configuration",
                "LifecycleConfiguration",
                autoboto.TypeInfo(BucketLifecycleConfiguration),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    lifecycle_configuration: "BucketLifecycleConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutBucketLifecycleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "content_md5",
                "ContentMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "lifecycle_configuration",
                "LifecycleConfiguration",
                autoboto.TypeInfo(LifecycleConfiguration),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    content_md5: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    lifecycle_configuration: "LifecycleConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutBucketLoggingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "bucket_logging_status",
                "BucketLoggingStatus",
                autoboto.TypeInfo(BucketLoggingStatus),
            ),
            (
                "content_md5",
                "ContentMD5",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    bucket_logging_status: "BucketLoggingStatus" = dataclasses.field(
        default_factory=dict,
    )
    content_md5: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketMetricsConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "metrics_configuration",
                "MetricsConfiguration",
                autoboto.TypeInfo(MetricsConfiguration),
            ),
        ]

    # The name of the bucket for which the metrics configuration is set.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ID used to identify the metrics configuration.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the metrics configuration.
    metrics_configuration: "MetricsConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutBucketNotificationConfigurationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "notification_configuration",
                "NotificationConfiguration",
                autoboto.TypeInfo(NotificationConfiguration),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Container for specifying the notification configuration of the bucket. If
    # this element is empty, notifications are turned off on the bucket.
    notification_configuration: "NotificationConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutBucketNotificationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "notification_configuration",
                "NotificationConfiguration",
                autoboto.TypeInfo(NotificationConfigurationDeprecated),
            ),
            (
                "content_md5",
                "ContentMD5",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    notification_configuration: "NotificationConfigurationDeprecated" = dataclasses.field(
        default_factory=dict,
    )
    content_md5: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketPolicyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "policy",
                "Policy",
                autoboto.TypeInfo(str),
            ),
            (
                "content_md5",
                "ContentMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "confirm_remove_self_bucket_access",
                "ConfirmRemoveSelfBucketAccess",
                autoboto.TypeInfo(bool),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The bucket policy as a JSON document.
    policy: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    content_md5: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Set this parameter to true to confirm that you want to remove your
    # permissions to change this bucket policy in the future.
    confirm_remove_self_bucket_access: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutBucketReplicationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "replication_configuration",
                "ReplicationConfiguration",
                autoboto.TypeInfo(ReplicationConfiguration),
            ),
            (
                "content_md5",
                "ContentMD5",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Container for replication rules. You can add as many as 1,000 rules. Total
    # replication configuration size can be up to 2 MB.
    replication_configuration: "ReplicationConfiguration" = dataclasses.field(
        default_factory=dict,
    )
    content_md5: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketRequestPaymentRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "request_payment_configuration",
                "RequestPaymentConfiguration",
                autoboto.TypeInfo(RequestPaymentConfiguration),
            ),
            (
                "content_md5",
                "ContentMD5",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    request_payment_configuration: "RequestPaymentConfiguration" = dataclasses.field(
        default_factory=dict,
    )
    content_md5: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketTaggingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "tagging",
                "Tagging",
                autoboto.TypeInfo(Tagging),
            ),
            (
                "content_md5",
                "ContentMD5",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    tagging: "Tagging" = dataclasses.field(default_factory=dict, )
    content_md5: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketVersioningRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "versioning_configuration",
                "VersioningConfiguration",
                autoboto.TypeInfo(VersioningConfiguration),
            ),
            (
                "content_md5",
                "ContentMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "mfa",
                "MFA",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    versioning_configuration: "VersioningConfiguration" = dataclasses.field(
        default_factory=dict,
    )
    content_md5: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The concatenation of the authentication device's serial number, a space,
    # and the value that is displayed on your authentication device.
    mfa: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketWebsiteRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "website_configuration",
                "WebsiteConfiguration",
                autoboto.TypeInfo(WebsiteConfiguration),
            ),
            (
                "content_md5",
                "ContentMD5",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    website_configuration: "WebsiteConfiguration" = dataclasses.field(
        default_factory=dict,
    )
    content_md5: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutObjectAclOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "request_charged",
                "RequestCharged",
                autoboto.TypeInfo(RequestCharged),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: "RequestCharged" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutObjectAclRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "acl",
                "ACL",
                autoboto.TypeInfo(ObjectCannedACL),
            ),
            (
                "access_control_policy",
                "AccessControlPolicy",
                autoboto.TypeInfo(AccessControlPolicy),
            ),
            (
                "content_md5",
                "ContentMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_full_control",
                "GrantFullControl",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_read",
                "GrantRead",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_read_acp",
                "GrantReadACP",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_write",
                "GrantWrite",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_write_acp",
                "GrantWriteACP",
                autoboto.TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The canned ACL to apply to the object.
    acl: "ObjectCannedACL" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    access_control_policy: "AccessControlPolicy" = dataclasses.field(
        default_factory=dict,
    )
    content_md5: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Allows grantee the read, write, read ACP, and write ACP permissions on the
    # bucket.
    grant_full_control: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Allows grantee to list the objects in the bucket.
    grant_read: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Allows grantee to read the bucket ACL.
    grant_read_acp: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Allows grantee to create, overwrite, and delete any object in the bucket.
    grant_write: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Allows grantee to write the ACL for the applicable bucket.
    grant_write_acp: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # VersionId used to reference a specific version of the object.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutObjectOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "expiration",
                "Expiration",
                autoboto.TypeInfo(str),
            ),
            (
                "e_tag",
                "ETag",
                autoboto.TypeInfo(str),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                autoboto.TypeInfo(ServerSideEncryption),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "request_charged",
                "RequestCharged",
                autoboto.TypeInfo(RequestCharged),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the object expiration is configured, this will contain the expiration
    # date (expiry-date) and rule ID (rule-id). The value of rule-id is URL
    # encoded.
    expiration: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Entity tag for the uploaded object.
    e_tag: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: "ServerSideEncryption" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Version of the object.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header confirming the encryption
    # algorithm used.
    sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header to provide round trip
    # message integrity verification of the customer-provided encryption key.
    sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If present, specifies the ID of the AWS Key Management Service (KMS) master
    # encryption key that was used for the object.
    ssekms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: "RequestCharged" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutObjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "acl",
                "ACL",
                autoboto.TypeInfo(ObjectCannedACL),
            ),
            (
                "body",
                "Body",
                autoboto.TypeInfo(typing.Any),
            ),
            (
                "cache_control",
                "CacheControl",
                autoboto.TypeInfo(str),
            ),
            (
                "content_disposition",
                "ContentDisposition",
                autoboto.TypeInfo(str),
            ),
            (
                "content_encoding",
                "ContentEncoding",
                autoboto.TypeInfo(str),
            ),
            (
                "content_language",
                "ContentLanguage",
                autoboto.TypeInfo(str),
            ),
            (
                "content_length",
                "ContentLength",
                autoboto.TypeInfo(int),
            ),
            (
                "content_md5",
                "ContentMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "content_type",
                "ContentType",
                autoboto.TypeInfo(str),
            ),
            (
                "expires",
                "Expires",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "grant_full_control",
                "GrantFullControl",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_read",
                "GrantRead",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_read_acp",
                "GrantReadACP",
                autoboto.TypeInfo(str),
            ),
            (
                "grant_write_acp",
                "GrantWriteACP",
                autoboto.TypeInfo(str),
            ),
            (
                "metadata",
                "Metadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                autoboto.TypeInfo(ServerSideEncryption),
            ),
            (
                "storage_class",
                "StorageClass",
                autoboto.TypeInfo(StorageClass),
            ),
            (
                "website_redirect_location",
                "WebsiteRedirectLocation",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key",
                "SSECustomerKey",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
            (
                "tagging",
                "Tagging",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the bucket to which the PUT operation was initiated.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Object key for which the PUT operation was initiated.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The canned ACL to apply to the object.
    acl: "ObjectCannedACL" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Object data.
    body: typing.Any = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies caching behavior along the request/reply chain.
    cache_control: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies presentational information for the object.
    content_disposition: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies what content encodings have been applied to the object and thus
    # what decoding mechanisms must be applied to obtain the media-type
    # referenced by the Content-Type header field.
    content_encoding: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The language the content is in.
    content_language: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Size of the body in bytes. This parameter is useful when the size of the
    # body cannot be determined automatically.
    content_length: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The base64-encoded 128-bit MD5 digest of the part data.
    content_md5: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A standard MIME type describing the format of the object data.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date and time at which the object is no longer cacheable.
    expires: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
    grant_full_control: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Allows grantee to read the object data and its metadata.
    grant_read: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Allows grantee to read the object ACL.
    grant_read_acp: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Allows grantee to write the ACL for the applicable object.
    grant_write_acp: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A map of metadata to store with the object in S3.
    metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: "ServerSideEncryption" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of storage to use for the object. Defaults to 'STANDARD'.
    storage_class: "StorageClass" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the bucket is configured as a website, redirects requests for this
    # object to another object in the same bucket or to an external URL. Amazon
    # S3 stores the value of this header in the object metadata.
    website_redirect_location: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the algorithm to use to when encrypting the object (e.g.,
    # AES256).
    sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the customer-provided encryption key for Amazon S3 to use in
    # encrypting data. This value is used to store the object and then it is
    # discarded; Amazon does not store the encryption key. The key must be
    # appropriate for use with the algorithm specified in the x-amz-server-
    # side​-encryption​-customer-algorithm header.
    sse_customer_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the AWS KMS key ID to use for object encryption. All GET and PUT
    # requests for an object protected by AWS KMS will fail if not made via SSL
    # or using SigV4. Documentation on configuring any of the officially
    # supported AWS SDKs and CLI can be found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-
    # signature-version
    ssekms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The tag-set for the object. The tag-set must be encoded as URL Query
    # parameters
    tagging: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutObjectTaggingOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutObjectTaggingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "tagging",
                "Tagging",
                autoboto.TypeInfo(Tagging),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "content_md5",
                "ContentMD5",
                autoboto.TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    tagging: "Tagging" = dataclasses.field(default_factory=dict, )
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    content_md5: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class QueueConfiguration(autoboto.ShapeBase):
    """
    Container for specifying an configuration when you want Amazon S3 to publish
    events to an Amazon Simple Queue Service (Amazon SQS) queue.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_arn",
                "QueueArn",
                autoboto.TypeInfo(str),
            ),
            (
                "events",
                "Events",
                autoboto.TypeInfo(typing.List[Event]),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "filter",
                "Filter",
                autoboto.TypeInfo(NotificationConfigurationFilter),
            ),
        ]

    # Amazon SQS queue ARN to which Amazon S3 will publish a message when it
    # detects events of specified type.
    queue_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    events: typing.List["Event"] = dataclasses.field(default_factory=list, )

    # Optional unique identifier for configurations in a notification
    # configuration. If you don't provide one, Amazon S3 will assign an ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Container for object key name filtering rules. For information about key
    # name filtering, go to [Configuring Event
    # Notifications](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html)
    # in the Amazon Simple Storage Service Developer Guide.
    filter: "NotificationConfigurationFilter" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class QueueConfigurationDeprecated(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "event",
                "Event",
                autoboto.TypeInfo(Event),
            ),
            (
                "events",
                "Events",
                autoboto.TypeInfo(typing.List[Event]),
            ),
            (
                "queue",
                "Queue",
                autoboto.TypeInfo(str),
            ),
        ]

    # Optional unique identifier for configurations in a notification
    # configuration. If you don't provide one, Amazon S3 will assign an ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Bucket event for which to send notifications.
    event: "Event" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    events: typing.List["Event"] = dataclasses.field(default_factory=list, )
    queue: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class QuoteFields(Enum):
    ALWAYS = "ALWAYS"
    ASNEEDED = "ASNEEDED"


@dataclasses.dataclass
class RecordsEvent(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "payload",
                "Payload",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # The byte array of partial, one or more result records.
    payload: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Redirect(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "host_name",
                "HostName",
                autoboto.TypeInfo(str),
            ),
            (
                "http_redirect_code",
                "HttpRedirectCode",
                autoboto.TypeInfo(str),
            ),
            (
                "protocol",
                "Protocol",
                autoboto.TypeInfo(Protocol),
            ),
            (
                "replace_key_prefix_with",
                "ReplaceKeyPrefixWith",
                autoboto.TypeInfo(str),
            ),
            (
                "replace_key_with",
                "ReplaceKeyWith",
                autoboto.TypeInfo(str),
            ),
        ]

    # The host name to use in the redirect request.
    host_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The HTTP redirect code to use on the response. Not required if one of the
    # siblings is present.
    http_redirect_code: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Protocol to use (http, https) when redirecting requests. The default is the
    # protocol that is used in the original request.
    protocol: "Protocol" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The object key prefix to use in the redirect request. For example, to
    # redirect requests for all pages with prefix docs/ (objects in the docs/
    # folder) to documents/, you can set a condition block with KeyPrefixEquals
    # set to docs/ and in the Redirect set ReplaceKeyPrefixWith to /documents.
    # Not required if one of the siblings is present. Can be present only if
    # ReplaceKeyWith is not provided.
    replace_key_prefix_with: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The specific object key to use in the redirect request. For example,
    # redirect request to error.html. Not required if one of the sibling is
    # present. Can be present only if ReplaceKeyPrefixWith is not provided.
    replace_key_with: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RedirectAllRequestsTo(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "host_name",
                "HostName",
                autoboto.TypeInfo(str),
            ),
            (
                "protocol",
                "Protocol",
                autoboto.TypeInfo(Protocol),
            ),
        ]

    # Name of the host where requests will be redirected.
    host_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Protocol to use (http, https) when redirecting requests. The default is the
    # protocol that is used in the original request.
    protocol: "Protocol" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReplicationConfiguration(autoboto.ShapeBase):
    """
    Container for replication rules. You can add as many as 1,000 rules. Total
    replication configuration size can be up to 2 MB.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role",
                "Role",
                autoboto.TypeInfo(str),
            ),
            (
                "rules",
                "Rules",
                autoboto.TypeInfo(typing.List[ReplicationRule]),
            ),
        ]

    # Amazon Resource Name (ARN) of an IAM role for Amazon S3 to assume when
    # replicating the objects.
    role: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Container for information about a particular replication rule. Replication
    # configuration must have at least one rule and can contain up to 1,000
    # rules.
    rules: typing.List["ReplicationRule"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ReplicationRule(autoboto.ShapeBase):
    """
    Container for information about a particular replication rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(ReplicationRuleStatus),
            ),
            (
                "destination",
                "Destination",
                autoboto.TypeInfo(Destination),
            ),
            (
                "id",
                "ID",
                autoboto.TypeInfo(str),
            ),
            (
                "source_selection_criteria",
                "SourceSelectionCriteria",
                autoboto.TypeInfo(SourceSelectionCriteria),
            ),
        ]

    # Object keyname prefix identifying one or more objects to which the rule
    # applies. Maximum prefix length can be up to 1,024 characters. Overlapping
    # prefixes are not supported.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The rule is ignored if status is not Enabled.
    status: "ReplicationRuleStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Container for replication destination information.
    destination: "Destination" = dataclasses.field(default_factory=dict, )

    # Unique identifier for the rule. The value cannot be longer than 255
    # characters.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Container for filters that define which source objects should be
    # replicated.
    source_selection_criteria: "SourceSelectionCriteria" = dataclasses.field(
        default_factory=dict,
    )


class ReplicationRuleStatus(Enum):
    Enabled = "Enabled"
    Disabled = "Disabled"


class ReplicationStatus(Enum):
    COMPLETE = "COMPLETE"
    PENDING = "PENDING"
    FAILED = "FAILED"
    REPLICA = "REPLICA"


class RequestCharged(Enum):
    """
    If present, indicates that the requester was successfully charged for the
    request.
    """
    requester = "requester"


class RequestPayer(Enum):
    """
    Confirms that the requester knows that she or he will be charged for the
    request. Bucket owners need not specify this parameter in their requests.
    Documentation on downloading objects from requester pays buckets can be found at
    http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    """
    requester = "requester"


@dataclasses.dataclass
class RequestPaymentConfiguration(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "payer",
                "Payer",
                autoboto.TypeInfo(Payer),
            ),
        ]

    # Specifies who pays for the download and request fees.
    payer: "Payer" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RequestProgress(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Specifies whether periodic QueryProgress frames should be sent. Valid
    # values: TRUE, FALSE. Default value: FALSE.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreObjectOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "request_charged",
                "RequestCharged",
                autoboto.TypeInfo(RequestCharged),
            ),
            (
                "restore_output_path",
                "RestoreOutputPath",
                autoboto.TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: "RequestCharged" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates the path in the provided S3 output location where Select results
    # will be restored to.
    restore_output_path: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RestoreObjectRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "restore_request",
                "RestoreRequest",
                autoboto.TypeInfo(RestoreRequest),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    version_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Container for restore job parameters.
    restore_request: "RestoreRequest" = dataclasses.field(
        default_factory=dict,
    )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RestoreRequest(autoboto.ShapeBase):
    """
    Container for restore job parameters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "days",
                "Days",
                autoboto.TypeInfo(int),
            ),
            (
                "glacier_job_parameters",
                "GlacierJobParameters",
                autoboto.TypeInfo(GlacierJobParameters),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(RestoreRequestType),
            ),
            (
                "tier",
                "Tier",
                autoboto.TypeInfo(Tier),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "select_parameters",
                "SelectParameters",
                autoboto.TypeInfo(SelectParameters),
            ),
            (
                "output_location",
                "OutputLocation",
                autoboto.TypeInfo(OutputLocation),
            ),
        ]

    # Lifetime of the active copy in days. Do not use with restores that specify
    # OutputLocation.
    days: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Glacier related parameters pertaining to this job. Do not use with restores
    # that specify OutputLocation.
    glacier_job_parameters: "GlacierJobParameters" = dataclasses.field(
        default_factory=dict,
    )

    # Type of restore request.
    type: "RestoreRequestType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Glacier retrieval tier at which the restore will be processed.
    tier: "Tier" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The optional description for the job.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Describes the parameters for Select job types.
    select_parameters: "SelectParameters" = dataclasses.field(
        default_factory=dict,
    )

    # Describes the location where the restore job's output is stored.
    output_location: "OutputLocation" = dataclasses.field(
        default_factory=dict,
    )


class RestoreRequestType(Enum):
    SELECT = "SELECT"


@dataclasses.dataclass
class RoutingRule(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "redirect",
                "Redirect",
                autoboto.TypeInfo(Redirect),
            ),
            (
                "condition",
                "Condition",
                autoboto.TypeInfo(Condition),
            ),
        ]

    # Container for redirect information. You can redirect requests to another
    # host, to another page, or with another protocol. In the event of an error,
    # you can can specify a different error code to return.
    redirect: "Redirect" = dataclasses.field(default_factory=dict, )

    # A container for describing a condition that must be met for the specified
    # redirect to apply. For example, 1. If request is for pages in the /docs
    # folder, redirect to the /documents folder. 2. If request results in HTTP
    # error 4xx, redirect request to another host where you might process the
    # error.
    condition: "Condition" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class Rule(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(ExpirationStatus),
            ),
            (
                "expiration",
                "Expiration",
                autoboto.TypeInfo(LifecycleExpiration),
            ),
            (
                "id",
                "ID",
                autoboto.TypeInfo(str),
            ),
            (
                "transition",
                "Transition",
                autoboto.TypeInfo(Transition),
            ),
            (
                "noncurrent_version_transition",
                "NoncurrentVersionTransition",
                autoboto.TypeInfo(NoncurrentVersionTransition),
            ),
            (
                "noncurrent_version_expiration",
                "NoncurrentVersionExpiration",
                autoboto.TypeInfo(NoncurrentVersionExpiration),
            ),
            (
                "abort_incomplete_multipart_upload",
                "AbortIncompleteMultipartUpload",
                autoboto.TypeInfo(AbortIncompleteMultipartUpload),
            ),
        ]

    # Prefix identifying one or more objects to which the rule applies.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If 'Enabled', the rule is currently being applied. If 'Disabled', the rule
    # is not currently being applied.
    status: "ExpirationStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    expiration: "LifecycleExpiration" = dataclasses.field(
        default_factory=dict,
    )

    # Unique identifier for the rule. The value cannot be longer than 255
    # characters.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    transition: "Transition" = dataclasses.field(default_factory=dict, )

    # Container for the transition rule that describes when noncurrent objects
    # transition to the STANDARD_IA, ONEZONE_IA or GLACIER storage class. If your
    # bucket is versioning-enabled (or versioning is suspended), you can set this
    # action to request that Amazon S3 transition noncurrent object versions to
    # the STANDARD_IA, ONEZONE_IA or GLACIER storage class at a specific period
    # in the object's lifetime.
    noncurrent_version_transition: "NoncurrentVersionTransition" = dataclasses.field(
        default_factory=dict,
    )

    # Specifies when noncurrent object versions expire. Upon expiration, Amazon
    # S3 permanently deletes the noncurrent object versions. You set this
    # lifecycle configuration action on a bucket that has versioning enabled (or
    # suspended) to request that Amazon S3 delete noncurrent object versions at a
    # specific period in the object's lifetime.
    noncurrent_version_expiration: "NoncurrentVersionExpiration" = dataclasses.field(
        default_factory=dict,
    )

    # Specifies the days since the initiation of an Incomplete Multipart Upload
    # that Lifecycle will wait before permanently removing all parts of the
    # upload.
    abort_incomplete_multipart_upload: "AbortIncompleteMultipartUpload" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class S3KeyFilter(autoboto.ShapeBase):
    """
    Container for object key name prefix and suffix filtering rules.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter_rules",
                "FilterRules",
                autoboto.TypeInfo(typing.List[FilterRule]),
            ),
        ]

    # A list of containers for key value pair that defines the criteria for the
    # filter rule.
    filter_rules: typing.List["FilterRule"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class S3Location(autoboto.ShapeBase):
    """
    Describes an S3 location that will receive the results of the restore request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket_name",
                "BucketName",
                autoboto.TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "encryption",
                "Encryption",
                autoboto.TypeInfo(Encryption),
            ),
            (
                "canned_acl",
                "CannedACL",
                autoboto.TypeInfo(ObjectCannedACL),
            ),
            (
                "access_control_list",
                "AccessControlList",
                autoboto.TypeInfo(typing.List[Grant]),
            ),
            (
                "tagging",
                "Tagging",
                autoboto.TypeInfo(Tagging),
            ),
            (
                "user_metadata",
                "UserMetadata",
                autoboto.TypeInfo(typing.List[MetadataEntry]),
            ),
            (
                "storage_class",
                "StorageClass",
                autoboto.TypeInfo(StorageClass),
            ),
        ]

    # The name of the bucket where the restore results will be placed.
    bucket_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The prefix that is prepended to the restore results for this request.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Describes the server-side encryption that will be applied to the restore
    # results.
    encryption: "Encryption" = dataclasses.field(default_factory=dict, )

    # The canned ACL to apply to the restore results.
    canned_acl: "ObjectCannedACL" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of grants that control access to the staged results.
    access_control_list: typing.List["Grant"] = dataclasses.field(
        default_factory=list,
    )

    # The tag-set that is applied to the restore results.
    tagging: "Tagging" = dataclasses.field(default_factory=dict, )

    # A list of metadata to store with the restore results in S3.
    user_metadata: typing.List["MetadataEntry"] = dataclasses.field(
        default_factory=list,
    )

    # The class of storage used to store the restore results.
    storage_class: "StorageClass" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SSEKMS(autoboto.ShapeBase):
    """
    Specifies the use of SSE-KMS to encrypt delievered Inventory reports.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Specifies the ID of the AWS Key Management Service (KMS) master encryption
    # key to use for encrypting Inventory reports.
    key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SSES3(autoboto.ShapeBase):
    """
    Specifies the use of SSE-S3 to encrypt delievered Inventory reports.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SelectObjectContentEventStream(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "records",
                "Records",
                autoboto.TypeInfo(RecordsEvent),
            ),
            (
                "stats",
                "Stats",
                autoboto.TypeInfo(StatsEvent),
            ),
            (
                "progress",
                "Progress",
                autoboto.TypeInfo(ProgressEvent),
            ),
            (
                "cont",
                "Cont",
                autoboto.TypeInfo(ContinuationEvent),
            ),
            (
                "end",
                "End",
                autoboto.TypeInfo(EndEvent),
            ),
        ]

    # The Records Event.
    records: "RecordsEvent" = dataclasses.field(default_factory=dict, )

    # The Stats Event.
    stats: "StatsEvent" = dataclasses.field(default_factory=dict, )

    # The Progress Event.
    progress: "ProgressEvent" = dataclasses.field(default_factory=dict, )

    # The Continuation Event.
    cont: "ContinuationEvent" = dataclasses.field(default_factory=dict, )

    # The End Event.
    end: "EndEvent" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class SelectObjectContentOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "payload",
                "Payload",
                autoboto.TypeInfo(SelectObjectContentEventStream),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    payload: "SelectObjectContentEventStream" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SelectObjectContentRequest(autoboto.ShapeBase):
    """
    Request to filter the contents of an Amazon S3 object based on a simple
    Structured Query Language (SQL) statement. In the request, along with the SQL
    expression, you must also specify a data serialization format (JSON or CSV) of
    the object. Amazon S3 uses this to parse object data into records, and returns
    only records that match the specified SQL expression. You must also specify the
    data serialization format for the response. For more information, go to
    [S3Select API
    Documentation](http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectSELECTContent.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "expression",
                "Expression",
                autoboto.TypeInfo(str),
            ),
            (
                "expression_type",
                "ExpressionType",
                autoboto.TypeInfo(ExpressionType),
            ),
            (
                "input_serialization",
                "InputSerialization",
                autoboto.TypeInfo(InputSerialization),
            ),
            (
                "output_serialization",
                "OutputSerialization",
                autoboto.TypeInfo(OutputSerialization),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key",
                "SSECustomerKey",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "request_progress",
                "RequestProgress",
                autoboto.TypeInfo(RequestProgress),
            ),
        ]

    # The S3 Bucket.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Object Key.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The expression that is used to query the object.
    expression: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of the provided expression (e.g., SQL).
    expression_type: "ExpressionType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Describes the format of the data in the object that is being queried.
    input_serialization: "InputSerialization" = dataclasses.field(
        default_factory=dict,
    )

    # Describes the format of the data that you want Amazon S3 to return in
    # response.
    output_serialization: "OutputSerialization" = dataclasses.field(
        default_factory=dict,
    )

    # The SSE Algorithm used to encrypt the object. For more information, go to [
    # Server-Side Encryption (Using Customer-Provided Encryption
    # Keys](http://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html).
    sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The SSE Customer Key. For more information, go to [ Server-Side Encryption
    # (Using Customer-Provided Encryption
    # Keys](http://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html).
    sse_customer_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The SSE Customer Key MD5. For more information, go to [ Server-Side
    # Encryption (Using Customer-Provided Encryption
    # Keys](http://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html).
    sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies if periodic request progress information should be enabled.
    request_progress: "RequestProgress" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SelectParameters(autoboto.ShapeBase):
    """
    Describes the parameters for Select job types.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_serialization",
                "InputSerialization",
                autoboto.TypeInfo(InputSerialization),
            ),
            (
                "expression_type",
                "ExpressionType",
                autoboto.TypeInfo(ExpressionType),
            ),
            (
                "expression",
                "Expression",
                autoboto.TypeInfo(str),
            ),
            (
                "output_serialization",
                "OutputSerialization",
                autoboto.TypeInfo(OutputSerialization),
            ),
        ]

    # Describes the serialization format of the object.
    input_serialization: "InputSerialization" = dataclasses.field(
        default_factory=dict,
    )

    # The type of the provided expression (e.g., SQL).
    expression_type: "ExpressionType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The expression that is used to query the object.
    expression: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Describes how the results of the Select job are serialized.
    output_serialization: "OutputSerialization" = dataclasses.field(
        default_factory=dict,
    )


class ServerSideEncryption(Enum):
    AES256 = "AES256"
    aws_kms = "aws:kms"


@dataclasses.dataclass
class ServerSideEncryptionByDefault(autoboto.ShapeBase):
    """
    Describes the default server-side encryption to apply to new objects in the
    bucket. If Put Object request does not specify any server-side encryption, this
    default encryption will be applied.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sse_algorithm",
                "SSEAlgorithm",
                autoboto.TypeInfo(ServerSideEncryption),
            ),
            (
                "kms_master_key_id",
                "KMSMasterKeyID",
                autoboto.TypeInfo(str),
            ),
        ]

    # Server-side encryption algorithm to use for the default encryption.
    sse_algorithm: "ServerSideEncryption" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # KMS master key ID to use for the default encryption. This parameter is
    # allowed if SSEAlgorithm is aws:kms.
    kms_master_key_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServerSideEncryptionConfiguration(autoboto.ShapeBase):
    """
    Container for server-side encryption configuration rules. Currently S3 supports
    one rule only.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rules",
                "Rules",
                autoboto.TypeInfo(typing.List[ServerSideEncryptionRule]),
            ),
        ]

    # Container for information about a particular server-side encryption
    # configuration rule.
    rules: typing.List["ServerSideEncryptionRule"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ServerSideEncryptionRule(autoboto.ShapeBase):
    """
    Container for information about a particular server-side encryption
    configuration rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apply_server_side_encryption_by_default",
                "ApplyServerSideEncryptionByDefault",
                autoboto.TypeInfo(ServerSideEncryptionByDefault),
            ),
        ]

    # Describes the default server-side encryption to apply to new objects in the
    # bucket. If Put Object request does not specify any server-side encryption,
    # this default encryption will be applied.
    apply_server_side_encryption_by_default: "ServerSideEncryptionByDefault" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SourceSelectionCriteria(autoboto.ShapeBase):
    """
    Container for filters that define which source objects should be replicated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sse_kms_encrypted_objects",
                "SseKmsEncryptedObjects",
                autoboto.TypeInfo(SseKmsEncryptedObjects),
            ),
        ]

    # Container for filter information of selection of KMS Encrypted S3 objects.
    sse_kms_encrypted_objects: "SseKmsEncryptedObjects" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class SseKmsEncryptedObjects(autoboto.ShapeBase):
    """
    Container for filter information of selection of KMS Encrypted S3 objects.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                autoboto.TypeInfo(SseKmsEncryptedObjectsStatus),
            ),
        ]

    # The replication for KMS encrypted S3 objects is disabled if status is not
    # Enabled.
    status: "SseKmsEncryptedObjectsStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class SseKmsEncryptedObjectsStatus(Enum):
    Enabled = "Enabled"
    Disabled = "Disabled"


@dataclasses.dataclass
class Stats(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bytes_scanned",
                "BytesScanned",
                autoboto.TypeInfo(int),
            ),
            (
                "bytes_processed",
                "BytesProcessed",
                autoboto.TypeInfo(int),
            ),
            (
                "bytes_returned",
                "BytesReturned",
                autoboto.TypeInfo(int),
            ),
        ]

    # Total number of object bytes scanned.
    bytes_scanned: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Total number of uncompressed object bytes processed.
    bytes_processed: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Total number of bytes of records payload data returned.
    bytes_returned: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StatsEvent(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "details",
                "Details",
                autoboto.TypeInfo(Stats),
            ),
        ]

    # The Stats event details.
    details: "Stats" = dataclasses.field(default_factory=dict, )


class StorageClass(Enum):
    STANDARD = "STANDARD"
    REDUCED_REDUNDANCY = "REDUCED_REDUNDANCY"
    STANDARD_IA = "STANDARD_IA"
    ONEZONE_IA = "ONEZONE_IA"


@dataclasses.dataclass
class StorageClassAnalysis(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_export",
                "DataExport",
                autoboto.TypeInfo(StorageClassAnalysisDataExport),
            ),
        ]

    # A container used to describe how data related to the storage class analysis
    # should be exported.
    data_export: "StorageClassAnalysisDataExport" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class StorageClassAnalysisDataExport(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_schema_version",
                "OutputSchemaVersion",
                autoboto.TypeInfo(StorageClassAnalysisSchemaVersion),
            ),
            (
                "destination",
                "Destination",
                autoboto.TypeInfo(AnalyticsExportDestination),
            ),
        ]

    # The version of the output schema to use when exporting data. Must be V_1.
    output_schema_version: "StorageClassAnalysisSchemaVersion" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The place to store the data for an analysis.
    destination: "AnalyticsExportDestination" = dataclasses.field(
        default_factory=dict,
    )


class StorageClassAnalysisSchemaVersion(Enum):
    V_1 = "V_1"


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the tag.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Value of the tag.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tagging(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_set",
                "TagSet",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    tag_set: typing.List["Tag"] = dataclasses.field(default_factory=list, )


class TaggingDirective(Enum):
    COPY = "COPY"
    REPLACE = "REPLACE"


@dataclasses.dataclass
class TargetGrant(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "grantee",
                "Grantee",
                autoboto.TypeInfo(Grantee),
            ),
            (
                "permission",
                "Permission",
                autoboto.TypeInfo(BucketLogsPermission),
            ),
        ]

    grantee: "Grantee" = dataclasses.field(default_factory=dict, )

    # Logging permissions assigned to the Grantee for the bucket.
    permission: "BucketLogsPermission" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class Tier(Enum):
    Standard = "Standard"
    Bulk = "Bulk"
    Expedited = "Expedited"


@dataclasses.dataclass
class TopicConfiguration(autoboto.ShapeBase):
    """
    Container for specifying the configuration when you want Amazon S3 to publish
    events to an Amazon Simple Notification Service (Amazon SNS) topic.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "topic_arn",
                "TopicArn",
                autoboto.TypeInfo(str),
            ),
            (
                "events",
                "Events",
                autoboto.TypeInfo(typing.List[Event]),
            ),
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "filter",
                "Filter",
                autoboto.TypeInfo(NotificationConfigurationFilter),
            ),
        ]

    # Amazon SNS topic ARN to which Amazon S3 will publish a message when it
    # detects events of specified type.
    topic_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    events: typing.List["Event"] = dataclasses.field(default_factory=list, )

    # Optional unique identifier for configurations in a notification
    # configuration. If you don't provide one, Amazon S3 will assign an ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Container for object key name filtering rules. For information about key
    # name filtering, go to [Configuring Event
    # Notifications](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html)
    # in the Amazon Simple Storage Service Developer Guide.
    filter: "NotificationConfigurationFilter" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class TopicConfigurationDeprecated(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "events",
                "Events",
                autoboto.TypeInfo(typing.List[Event]),
            ),
            (
                "event",
                "Event",
                autoboto.TypeInfo(Event),
            ),
            (
                "topic",
                "Topic",
                autoboto.TypeInfo(str),
            ),
        ]

    # Optional unique identifier for configurations in a notification
    # configuration. If you don't provide one, Amazon S3 will assign an ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    events: typing.List["Event"] = dataclasses.field(default_factory=list, )

    # Bucket event for which to send notifications.
    event: "Event" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Amazon SNS topic to which Amazon S3 will publish a message to report the
    # specified events for the bucket.
    topic: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Transition(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "date",
                "Date",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "days",
                "Days",
                autoboto.TypeInfo(int),
            ),
            (
                "storage_class",
                "StorageClass",
                autoboto.TypeInfo(TransitionStorageClass),
            ),
        ]

    # Indicates at what date the object is to be moved or deleted. Should be in
    # GMT ISO 8601 Format.
    date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates the lifetime, in days, of the objects that are subject to the
    # rule. The value must be a non-zero positive integer.
    days: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The class of storage used to store the object.
    storage_class: "TransitionStorageClass" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class TransitionStorageClass(Enum):
    GLACIER = "GLACIER"
    STANDARD_IA = "STANDARD_IA"
    ONEZONE_IA = "ONEZONE_IA"


class Type(Enum):
    CanonicalUser = "CanonicalUser"
    AmazonCustomerByEmail = "AmazonCustomerByEmail"
    Group = "Group"


@dataclasses.dataclass
class UploadPartCopyOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "copy_source_version_id",
                "CopySourceVersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_part_result",
                "CopyPartResult",
                autoboto.TypeInfo(CopyPartResult),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                autoboto.TypeInfo(ServerSideEncryption),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "request_charged",
                "RequestCharged",
                autoboto.TypeInfo(RequestCharged),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The version of the source object that was copied, if you have enabled
    # versioning on the source bucket.
    copy_source_version_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
    copy_part_result: "CopyPartResult" = dataclasses.field(
        default_factory=dict,
    )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: "ServerSideEncryption" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header confirming the encryption
    # algorithm used.
    sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header to provide round trip
    # message integrity verification of the customer-provided encryption key.
    sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If present, specifies the ID of the AWS Key Management Service (KMS) master
    # encryption key that was used for the object.
    ssekms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: "RequestCharged" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UploadPartCopyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_source",
                "CopySource",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "part_number",
                "PartNumber",
                autoboto.TypeInfo(int),
            ),
            (
                "upload_id",
                "UploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_source_if_match",
                "CopySourceIfMatch",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_source_if_modified_since",
                "CopySourceIfModifiedSince",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "copy_source_if_none_match",
                "CopySourceIfNoneMatch",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_source_if_unmodified_since",
                "CopySourceIfUnmodifiedSince",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "copy_source_range",
                "CopySourceRange",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key",
                "SSECustomerKey",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_source_sse_customer_algorithm",
                "CopySourceSSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_source_sse_customer_key",
                "CopySourceSSECustomerKey",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_source_sse_customer_key_md5",
                "CopySourceSSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
        ]

    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the source bucket and key name of the source object, separated
    # by a slash (/). Must be URL-encoded.
    copy_source: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Part number of part being copied. This is a positive integer between 1 and
    # 10,000.
    part_number: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Upload ID identifying the multipart upload whose part is being copied.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Copies the object if its entity tag (ETag) matches the specified tag.
    copy_source_if_match: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Copies the object if it has been modified since the specified time.
    copy_source_if_modified_since: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Copies the object if its entity tag (ETag) is different than the specified
    # ETag.
    copy_source_if_none_match: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Copies the object if it hasn't been modified since the specified time.
    copy_source_if_unmodified_since: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The range of bytes to copy from the source object. The range value must use
    # the form bytes=first-last, where the first and last are the zero-based byte
    # offsets to copy. For example, bytes=0-9 indicates that you want to copy the
    # first ten bytes of the source. You can copy a range only if the source
    # object is greater than 5 GB.
    copy_source_range: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the algorithm to use to when encrypting the object (e.g.,
    # AES256).
    sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the customer-provided encryption key for Amazon S3 to use in
    # encrypting data. This value is used to store the object and then it is
    # discarded; Amazon does not store the encryption key. The key must be
    # appropriate for use with the algorithm specified in the x-amz-server-
    # side​-encryption​-customer-algorithm header. This must be the same
    # encryption key specified in the initiate multipart upload request.
    sse_customer_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the algorithm to use when decrypting the source object (e.g.,
    # AES256).
    copy_source_sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the customer-provided encryption key for Amazon S3 to use to
    # decrypt the source object. The encryption key provided in this header must
    # be one that was used when the source object was created.
    copy_source_sse_customer_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    copy_source_sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UploadPartOutput(autoboto.OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                autoboto.TypeInfo(ServerSideEncryption),
            ),
            (
                "e_tag",
                "ETag",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "request_charged",
                "RequestCharged",
                autoboto.TypeInfo(RequestCharged),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: "ServerSideEncryption" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Entity tag for the uploaded object.
    e_tag: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header confirming the encryption
    # algorithm used.
    sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header to provide round trip
    # message integrity verification of the customer-provided encryption key.
    sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If present, specifies the ID of the AWS Key Management Service (KMS) master
    # encryption key that was used for the object.
    ssekms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: "RequestCharged" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UploadPartRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "key",
                "Key",
                autoboto.TypeInfo(str),
            ),
            (
                "part_number",
                "PartNumber",
                autoboto.TypeInfo(int),
            ),
            (
                "upload_id",
                "UploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "body",
                "Body",
                autoboto.TypeInfo(typing.Any),
            ),
            (
                "content_length",
                "ContentLength",
                autoboto.TypeInfo(int),
            ),
            (
                "content_md5",
                "ContentMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key",
                "SSECustomerKey",
                autoboto.TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                autoboto.TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                autoboto.TypeInfo(RequestPayer),
            ),
        ]

    # Name of the bucket to which the multipart upload was initiated.
    bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Object key for which the multipart upload was initiated.
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Part number of part being uploaded. This is a positive integer between 1
    # and 10,000.
    part_number: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Upload ID identifying the multipart upload whose part is being uploaded.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Object data.
    body: typing.Any = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Size of the body in bytes. This parameter is useful when the size of the
    # body cannot be determined automatically.
    content_length: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The base64-encoded 128-bit MD5 digest of the part data.
    content_md5: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the algorithm to use to when encrypting the object (e.g.,
    # AES256).
    sse_customer_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the customer-provided encryption key for Amazon S3 to use in
    # encrypting data. This value is used to store the object and then it is
    # discarded; Amazon does not store the encryption key. The key must be
    # appropriate for use with the algorithm specified in the x-amz-server-
    # side​-encryption​-customer-algorithm header. This must be the same
    # encryption key specified in the initiate multipart upload request.
    sse_customer_key: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    sse_customer_key_md5: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: "RequestPayer" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class VersioningConfiguration(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "mfa_delete",
                "MFADelete",
                autoboto.TypeInfo(MFADelete),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(BucketVersioningStatus),
            ),
        ]

    # Specifies whether MFA delete is enabled in the bucket versioning
    # configuration. This element is only returned if the bucket has been
    # configured with MFA delete. If the bucket has never been so configured,
    # this element is not returned.
    mfa_delete: "MFADelete" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The versioning state of the bucket.
    status: "BucketVersioningStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class WebsiteConfiguration(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_document",
                "ErrorDocument",
                autoboto.TypeInfo(ErrorDocument),
            ),
            (
                "index_document",
                "IndexDocument",
                autoboto.TypeInfo(IndexDocument),
            ),
            (
                "redirect_all_requests_to",
                "RedirectAllRequestsTo",
                autoboto.TypeInfo(RedirectAllRequestsTo),
            ),
            (
                "routing_rules",
                "RoutingRules",
                autoboto.TypeInfo(typing.List[RoutingRule]),
            ),
        ]

    error_document: "ErrorDocument" = dataclasses.field(default_factory=dict, )
    index_document: "IndexDocument" = dataclasses.field(default_factory=dict, )
    redirect_all_requests_to: "RedirectAllRequestsTo" = dataclasses.field(
        default_factory=dict,
    )
    routing_rules: typing.List["RoutingRule"] = dataclasses.field(
        default_factory=list,
    )
