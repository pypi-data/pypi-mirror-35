import datetime
import typing
import autoboto
from enum import Enum
import botocore.response
import dataclasses


@dataclasses.dataclass
class AbortMultipartUploadInput(autoboto.ShapeBase):
    """
    Provides options to abort a multipart upload identified by the upload ID.

    For information about the underlying REST API, see [Abort Multipart
    Upload](http://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-abort-
    upload.html). For conceptual information, see [Working with Archives in Amazon
    Glacier](http://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-
    archives.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id",
                "uploadId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The upload ID of the multipart upload to delete.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class AbortVaultLockInput(autoboto.ShapeBase):
    """
    The input values for `AbortVaultLock`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID. This value must match the AWS
    # account ID associated with the credentials used to sign the request. You
    # can either specify an AWS account ID or optionally a single '`-`' (hyphen),
    # in which case Amazon Glacier uses the AWS account ID associated with the
    # credentials used to sign the request. If you specify your account ID, do
    # not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class ActionCode(Enum):
    ArchiveRetrieval = "ArchiveRetrieval"
    InventoryRetrieval = "InventoryRetrieval"
    Select = "Select"


@dataclasses.dataclass
class AddTagsToVaultInput(autoboto.ShapeBase):
    """
    The input values for `AddTagsToVault`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The tags to add to the vault. Each tag is composed of a key and a value.
    # The value can be an empty string.
    tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ArchiveCreationOutput(autoboto.ShapeBase):
    """
    Contains the Amazon Glacier response to your request.

    For information about the underlying REST API, see [Upload
    Archive](http://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-
    post.html). For conceptual information, see [Working with Archives in Amazon
    Glacier](http://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-
    archives.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "location",
                "location",
                autoboto.TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                autoboto.TypeInfo(str),
            ),
            (
                "archive_id",
                "archiveId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The relative URI path of the newly added archive resource.
    location: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The checksum of the archive computed by Amazon Glacier.
    checksum: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the archive. This value is also included as part of the location.
    archive_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CSVInput(autoboto.ShapeBase):
    """
    Contains information about the comma-separated value (CSV) file to select from.
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
        ]

    # Describes the first line of input. Valid values are `None`, `Ignore`, and
    # `Use`.
    file_header_info: "FileHeaderInfo" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A single character used to indicate that a row should be ignored when the
    # character is present at the start of that row.
    comments: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A single character used for escaping the quotation-mark character inside an
    # already escaped value.
    quote_escape_character: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A value used to separate individual records from each other.
    record_delimiter: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A value used to separate individual fields from each other within a record.
    field_delimiter: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A value used as an escape character where the field delimiter is part of
    # the value.
    quote_character: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CSVOutput(autoboto.ShapeBase):
    """
    Contains information about the comma-separated value (CSV) file that the job
    results are stored in.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # A value that indicates whether all output fields should be contained within
    # quotation marks.
    quote_fields: "QuoteFields" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A single character used for escaping the quotation-mark character inside an
    # already escaped value.
    quote_escape_character: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A value used to separate individual records from each other.
    record_delimiter: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A value used to separate individual fields from each other within a record.
    field_delimiter: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A value used as an escape character where the field delimiter is part of
    # the value.
    quote_character: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class CannedACL(Enum):
    private = "private"
    public_read = "public-read"
    public_read_write = "public-read-write"
    aws_exec_read = "aws-exec-read"
    authenticated_read = "authenticated-read"
    bucket_owner_read = "bucket-owner-read"
    bucket_owner_full_control = "bucket-owner-full-control"


@dataclasses.dataclass
class CompleteMultipartUploadInput(autoboto.ShapeBase):
    """
    Provides options to complete a multipart upload operation. This informs Amazon
    Glacier that all the archive parts have been uploaded and Amazon Glacier can now
    assemble the archive from the uploaded parts. After assembling and saving the
    archive to the vault, Amazon Glacier returns the URI path of the newly created
    archive resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id",
                "uploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "archive_size",
                "archiveSize",
                autoboto.TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The upload ID of the multipart upload.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The total size, in bytes, of the entire archive. This value should be the
    # sum of all the sizes of the individual parts that you uploaded.
    archive_size: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The SHA256 tree hash of the entire archive. It is the tree hash of SHA256
    # tree hash of the individual parts. If the value you specify in the request
    # does not match the SHA256 tree hash of the final assembled archive as
    # computed by Amazon Glacier, Amazon Glacier returns an error and the request
    # fails.
    checksum: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CompleteVaultLockInput(autoboto.ShapeBase):
    """
    The input values for `CompleteVaultLock`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "lock_id",
                "lockId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID. This value must match the AWS
    # account ID associated with the credentials used to sign the request. You
    # can either specify an AWS account ID or optionally a single '`-`' (hyphen),
    # in which case Amazon Glacier uses the AWS account ID associated with the
    # credentials used to sign the request. If you specify your account ID, do
    # not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The `lockId` value is the lock ID obtained from a InitiateVaultLock
    # request.
    lock_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateVaultInput(autoboto.ShapeBase):
    """
    Provides options to create a vault.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID. This value must match the AWS
    # account ID associated with the credentials used to sign the request. You
    # can either specify an AWS account ID or optionally a single '`-`' (hyphen),
    # in which case Amazon Glacier uses the AWS account ID associated with the
    # credentials used to sign the request. If you specify your account ID, do
    # not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateVaultOutput(autoboto.ShapeBase):
    """
    Contains the Amazon Glacier response to your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "location",
                "location",
                autoboto.TypeInfo(str),
            ),
        ]

    # The URI of the vault that was created.
    location: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DataRetrievalPolicy(autoboto.ShapeBase):
    """
    Data retrieval policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rules",
                "Rules",
                autoboto.TypeInfo(typing.List[DataRetrievalRule]),
            ),
        ]

    # The policy rule. Although this is a list type, currently there must be only
    # one rule, which contains a Strategy field and optionally a BytesPerHour
    # field.
    rules: typing.List["DataRetrievalRule"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DataRetrievalRule(autoboto.ShapeBase):
    """
    Data retrieval policy rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "strategy",
                "Strategy",
                autoboto.TypeInfo(str),
            ),
            (
                "bytes_per_hour",
                "BytesPerHour",
                autoboto.TypeInfo(int),
            ),
        ]

    # The type of data retrieval policy to set.

    # Valid values: BytesPerHour|FreeTier|None
    strategy: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of bytes that can be retrieved in an hour.

    # This field is required only if the value of the Strategy field is
    # `BytesPerHour`. Your PUT operation will be rejected if the Strategy field
    # is not set to `BytesPerHour` and you set this field.
    bytes_per_hour: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteArchiveInput(autoboto.ShapeBase):
    """
    Provides options for deleting an archive from an Amazon Glacier vault.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "archive_id",
                "archiveId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the archive to delete.
    archive_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteVaultAccessPolicyInput(autoboto.ShapeBase):
    """
    DeleteVaultAccessPolicy input.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteVaultInput(autoboto.ShapeBase):
    """
    Provides options for deleting a vault from Amazon Glacier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteVaultNotificationsInput(autoboto.ShapeBase):
    """
    Provides options for deleting a vault notification configuration from an Amazon
    Glacier vault.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeJobInput(autoboto.ShapeBase):
    """
    Provides options for retrieving a job description.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the job to describe.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeVaultInput(autoboto.ShapeBase):
    """
    Provides options for retrieving metadata for a specific vault in Amazon Glacier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeVaultOutput(autoboto.ShapeBase):
    """
    Contains the Amazon Glacier response to your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vault_arn",
                "VaultARN",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "VaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "last_inventory_date",
                "LastInventoryDate",
                autoboto.TypeInfo(str),
            ),
            (
                "number_of_archives",
                "NumberOfArchives",
                autoboto.TypeInfo(int),
            ),
            (
                "size_in_bytes",
                "SizeInBytes",
                autoboto.TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the vault.
    vault_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Universal Coordinated Time (UTC) date when the vault was created. This
    # value should be a string in the ISO 8601 date format, for example
    # `2012-03-20T17:03:43.221Z`.
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Universal Coordinated Time (UTC) date when Amazon Glacier completed the
    # last vault inventory. This value should be a string in the ISO 8601 date
    # format, for example `2012-03-20T17:03:43.221Z`.
    last_inventory_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of archives in the vault as of the last inventory date. This
    # field will return `null` if an inventory has not yet run on the vault, for
    # example if you just created the vault.
    number_of_archives: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Total size, in bytes, of the archives in the vault as of the last inventory
    # date. This field will return null if an inventory has not yet run on the
    # vault, for example if you just created the vault.
    size_in_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Encryption(autoboto.ShapeBase):
    """
    Contains information about the encryption used to store the job results in
    Amazon S3.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption_type",
                "EncryptionType",
                autoboto.TypeInfo(EncryptionType),
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
    # Amazon S3, for example `AES256` or `aws:kms`.
    encryption_type: "EncryptionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS KMS key ID to use for object encryption. All GET and PUT requests
    # for an object protected by AWS KMS fail if not made by using Secure Sockets
    # Layer (SSL) or Signature Version 4.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Optional. If the encryption type is `aws:kms`, you can use this value to
    # specify the encryption context for the job results.
    kms_context: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class EncryptionType(Enum):
    aws_kms = "aws:kms"
    AES256 = "AES256"


class ExpressionType(Enum):
    SQL = "SQL"


class FileHeaderInfo(Enum):
    USE = "USE"
    IGNORE = "IGNORE"
    NONE = "NONE"


@dataclasses.dataclass
class GetDataRetrievalPolicyInput(autoboto.ShapeBase):
    """
    Input for GetDataRetrievalPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID. This value must match the AWS
    # account ID associated with the credentials used to sign the request. You
    # can either specify an AWS account ID or optionally a single '`-`' (hyphen),
    # in which case Amazon Glacier uses the AWS account ID associated with the
    # credentials used to sign the request. If you specify your account ID, do
    # not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDataRetrievalPolicyOutput(autoboto.ShapeBase):
    """
    Contains the Amazon Glacier response to the `GetDataRetrievalPolicy` request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy",
                "Policy",
                autoboto.TypeInfo(DataRetrievalPolicy),
            ),
        ]

    # Contains the returned data retrieval policy in JSON format.
    policy: "DataRetrievalPolicy" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetJobOutputInput(autoboto.ShapeBase):
    """
    Provides options for downloading output of an Amazon Glacier job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "range",
                "range",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The job ID whose data is downloaded.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The range of bytes to retrieve from the output. For example, if you want to
    # download the first 1,048,576 bytes, specify the range as `bytes=0-1048575`.
    # By default, this operation downloads the entire output.

    # If the job output is large, then you can use a range to retrieve a portion
    # of the output. This allows you to download the entire output in smaller
    # chunks of bytes. For example, suppose you have 1 GB of job output you want
    # to download and you decide to download 128 MB chunks of data at a time,
    # which is a total of eight Get Job Output requests. You use the following
    # process to download the job output:

    #   1. Download a 128 MB chunk of output by specifying the appropriate byte range. Verify that all 128 MB of data was received.

    #   2. Along with the data, the response includes a SHA256 tree hash of the payload. You compute the checksum of the payload on the client and compare it with the checksum you received in the response to ensure you received all the expected data.

    #   3. Repeat steps 1 and 2 for all the eight 128 MB chunks of output data, each time specifying the appropriate byte range.

    #   4. After downloading all the parts of the job output, you have a list of eight checksum values. Compute the tree hash of these values to find the checksum of the entire output. Using the DescribeJob API, obtain job information of the job that provided you the output. The response includes the checksum of the entire archive stored in Amazon Glacier. You compare this value with the checksum you computed to ensure you have downloaded the entire archive content with no errors.
    range: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetJobOutputOutput(autoboto.ShapeBase):
    """
    Contains the Amazon Glacier response to your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body",
                "body",
                autoboto.TypeInfo(typing.Any),
            ),
            (
                "checksum",
                "checksum",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(int),
            ),
            (
                "content_range",
                "contentRange",
                autoboto.TypeInfo(str),
            ),
            (
                "accept_ranges",
                "acceptRanges",
                autoboto.TypeInfo(str),
            ),
            (
                "content_type",
                "contentType",
                autoboto.TypeInfo(str),
            ),
            (
                "archive_description",
                "archiveDescription",
                autoboto.TypeInfo(str),
            ),
        ]

    # The job data, either archive data or inventory data.
    body: typing.Any = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The checksum of the data in the response. This header is returned only when
    # retrieving the output for an archive retrieval job. Furthermore, this
    # header appears only under the following conditions:

    #   * You get the entire range of the archive.

    #   * You request a range to return of the archive that starts and ends on a multiple of 1 MB. For example, if you have an 3.1 MB archive and you specify a range to return that starts at 1 MB and ends at 2 MB, then the x-amz-sha256-tree-hash is returned as a response header.

    #   * You request a range of the archive to return that starts on a multiple of 1 MB and goes to the end of the archive. For example, if you have a 3.1 MB archive and you specify a range that starts at 2 MB and ends at 3.1 MB (the end of the archive), then the x-amz-sha256-tree-hash is returned as a response header.
    checksum: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The HTTP response code for a job output request. The value depends on
    # whether a range was specified in the request.
    status: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The range of bytes returned by Amazon Glacier. If only partial output is
    # downloaded, the response provides the range of bytes Amazon Glacier
    # returned. For example, bytes 0-1048575/8388608 returns the first 1 MB from
    # 8 MB.
    content_range: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates the range units accepted. For more information, see
    # [RFC2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
    accept_ranges: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Content-Type depends on whether the job output is an archive or a vault
    # inventory. For archive data, the Content-Type is application/octet-stream.
    # For vault inventory, if you requested CSV format when you initiated the
    # job, the Content-Type is text/csv. Otherwise, by default, vault inventory
    # is returned as JSON, and the Content-Type is application/json.
    content_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The description of an archive.
    archive_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetVaultAccessPolicyInput(autoboto.ShapeBase):
    """
    Input for GetVaultAccessPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetVaultAccessPolicyOutput(autoboto.ShapeBase):
    """
    Output for GetVaultAccessPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy",
                "policy",
                autoboto.TypeInfo(VaultAccessPolicy),
            ),
        ]

    # Contains the returned vault access policy as a JSON string.
    policy: "VaultAccessPolicy" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetVaultLockInput(autoboto.ShapeBase):
    """
    The input values for `GetVaultLock`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetVaultLockOutput(autoboto.ShapeBase):
    """
    Contains the Amazon Glacier response to your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy",
                "Policy",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(str),
            ),
            (
                "expiration_date",
                "ExpirationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
        ]

    # The vault lock policy as a JSON string, which uses "\" as an escape
    # character.
    policy: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The state of the vault lock. `InProgress` or `Locked`.
    state: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The UTC date and time at which the lock ID expires. This value can be
    # `null` if the vault lock is in a `Locked` state.
    expiration_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The UTC date and time at which the vault lock was put into the `InProgress`
    # state.
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetVaultNotificationsInput(autoboto.ShapeBase):
    """
    Provides options for retrieving the notification configuration set on an Amazon
    Glacier vault.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetVaultNotificationsOutput(autoboto.ShapeBase):
    """
    Contains the Amazon Glacier response to your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vault_notification_config",
                "vaultNotificationConfig",
                autoboto.TypeInfo(VaultNotificationConfig),
            ),
        ]

    # Returns the notification configuration set on the vault.
    vault_notification_config: "VaultNotificationConfig" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GlacierJobDescription(autoboto.ShapeBase):
    """
    Contains the description of an Amazon Glacier job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                autoboto.TypeInfo(str),
            ),
            (
                "job_description",
                "JobDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "action",
                "Action",
                autoboto.TypeInfo(ActionCode),
            ),
            (
                "archive_id",
                "ArchiveId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_arn",
                "VaultARN",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "completed",
                "Completed",
                autoboto.TypeInfo(bool),
            ),
            (
                "status_code",
                "StatusCode",
                autoboto.TypeInfo(StatusCode),
            ),
            (
                "status_message",
                "StatusMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "archive_size_in_bytes",
                "ArchiveSizeInBytes",
                autoboto.TypeInfo(int),
            ),
            (
                "inventory_size_in_bytes",
                "InventorySizeInBytes",
                autoboto.TypeInfo(int),
            ),
            (
                "sns_topic",
                "SNSTopic",
                autoboto.TypeInfo(str),
            ),
            (
                "completion_date",
                "CompletionDate",
                autoboto.TypeInfo(str),
            ),
            (
                "sha256_tree_hash",
                "SHA256TreeHash",
                autoboto.TypeInfo(str),
            ),
            (
                "archive_sha256_tree_hash",
                "ArchiveSHA256TreeHash",
                autoboto.TypeInfo(str),
            ),
            (
                "retrieval_byte_range",
                "RetrievalByteRange",
                autoboto.TypeInfo(str),
            ),
            (
                "tier",
                "Tier",
                autoboto.TypeInfo(str),
            ),
            (
                "inventory_retrieval_parameters",
                "InventoryRetrievalParameters",
                autoboto.TypeInfo(InventoryRetrievalJobDescription),
            ),
            (
                "job_output_path",
                "JobOutputPath",
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

    # An opaque string that identifies an Amazon Glacier job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The job description provided when initiating the job.
    job_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The job type. This value is either `ArchiveRetrieval`,
    # `InventoryRetrieval`, or `Select`.
    action: "ActionCode" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The archive ID requested for a select job or archive retrieval. Otherwise,
    # this field is null.
    archive_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon Resource Name (ARN) of the vault from which an archive retrieval
    # was requested.
    vault_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The UTC date when the job was created. This value is a string
    # representation of ISO 8601 date format, for example
    # `"2012-03-20T17:03:43.221Z"`.
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The job status. When a job is completed, you get the job's output using Get
    # Job Output (GET output).
    completed: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The status code can be `InProgress`, `Succeeded`, or `Failed`, and
    # indicates the status of the job.
    status_code: "StatusCode" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A friendly message that describes the job status.
    status_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # For an archive retrieval job, this value is the size in bytes of the
    # archive being requested for download. For an inventory retrieval or select
    # job, this value is null.
    archive_size_in_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # For an inventory retrieval job, this value is the size in bytes of the
    # inventory requested for download. For an archive retrieval or select job,
    # this value is null.
    inventory_size_in_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An Amazon SNS topic that receives notification.
    sns_topic: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The UTC time that the job request completed. While the job is in progress,
    # the value is null.
    completion_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # For an archive retrieval job, this value is the checksum of the archive.
    # Otherwise, this value is null.

    # The SHA256 tree hash value for the requested range of an archive. If the
    # **InitiateJob** request for an archive specified a tree-hash aligned range,
    # then this field returns a value.

    # If the whole archive is retrieved, this value is the same as the
    # ArchiveSHA256TreeHash value.

    # This field is null for the following:

    #   * Archive retrieval jobs that specify a range that is not tree-hash aligned

    #   * Archival jobs that specify a range that is equal to the whole archive, when the job status is `InProgress`

    #   * Inventory jobs

    #   * Select jobs
    sha256_tree_hash: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The SHA256 tree hash of the entire archive for an archive retrieval. For
    # inventory retrieval or select jobs, this field is null.
    archive_sha256_tree_hash: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The retrieved byte range for archive retrieval jobs in the form
    # _StartByteValue_ - _EndByteValue_. If no range was specified in the archive
    # retrieval, then the whole archive is retrieved. In this case,
    # _StartByteValue_ equals 0 and _EndByteValue_ equals the size of the archive
    # minus 1. For inventory retrieval or select jobs, this field is null.
    retrieval_byte_range: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The tier to use for a select or an archive retrieval. Valid values are
    # `Expedited`, `Standard`, or `Bulk`. `Standard` is the default.
    tier: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Parameters used for range inventory retrieval.
    inventory_retrieval_parameters: "InventoryRetrievalJobDescription" = dataclasses.field(
        default_factory=dict,
    )

    # Contains the job output location.
    job_output_path: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Contains the parameters used for a select.
    select_parameters: "SelectParameters" = dataclasses.field(
        default_factory=dict,
    )

    # Contains the location where the data from the select job is stored.
    output_location: "OutputLocation" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class Grant(autoboto.ShapeBase):
    """
    Contains information about a grant.
    """

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

    # The grantee.
    grantee: "Grantee" = dataclasses.field(default_factory=dict, )

    # Specifies the permission given to the grantee.
    permission: "Permission" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Grantee(autoboto.ShapeBase):
    """
    Contains information about the grantee.
    """

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
                "uri",
                "URI",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "ID",
                autoboto.TypeInfo(str),
            ),
            (
                "email_address",
                "EmailAddress",
                autoboto.TypeInfo(str),
            ),
        ]

    # Type of grantee
    type: "Type" = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Screen name of the grantee.
    display_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # URI of the grantee group.
    uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The canonical user ID of the grantee.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Email address of the grantee.
    email_address: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class InitiateJobInput(autoboto.ShapeBase):
    """
    Provides options for initiating an Amazon Glacier job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "job_parameters",
                "jobParameters",
                autoboto.TypeInfo(JobParameters),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Provides options for specifying job information.
    job_parameters: "JobParameters" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class InitiateJobOutput(autoboto.ShapeBase):
    """
    Contains the Amazon Glacier response to your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "location",
                "location",
                autoboto.TypeInfo(str),
            ),
            (
                "job_id",
                "jobId",
                autoboto.TypeInfo(str),
            ),
            (
                "job_output_path",
                "jobOutputPath",
                autoboto.TypeInfo(str),
            ),
        ]

    # The relative URI path of the job.
    location: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the job.
    job_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The path to the location of where the select results are stored.
    job_output_path: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class InitiateMultipartUploadInput(autoboto.ShapeBase):
    """
    Provides options for initiating a multipart upload to an Amazon Glacier vault.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "archive_description",
                "archiveDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "part_size",
                "partSize",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The archive description that you are uploading in parts.

    # The part size must be a megabyte (1024 KB) multiplied by a power of 2, for
    # example 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and
    # so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB
    # (4096 MB).
    archive_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The size of each part except the last, in bytes. The last part can be
    # smaller than this part size.
    part_size: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InitiateMultipartUploadOutput(autoboto.ShapeBase):
    """
    The Amazon Glacier response to your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "location",
                "location",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id",
                "uploadId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The relative URI path of the multipart upload ID Amazon Glacier created.
    location: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the multipart upload. This value is also included as part of the
    # location.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InitiateVaultLockInput(autoboto.ShapeBase):
    """
    The input values for `InitiateVaultLock`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy",
                "policy",
                autoboto.TypeInfo(VaultLockPolicy),
            ),
        ]

    # The `AccountId` value is the AWS account ID. This value must match the AWS
    # account ID associated with the credentials used to sign the request. You
    # can either specify an AWS account ID or optionally a single '`-`' (hyphen),
    # in which case Amazon Glacier uses the AWS account ID associated with the
    # credentials used to sign the request. If you specify your account ID, do
    # not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The vault lock policy as a JSON string, which uses "\" as an escape
    # character.
    policy: "VaultLockPolicy" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class InitiateVaultLockOutput(autoboto.ShapeBase):
    """
    Contains the Amazon Glacier response to your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lock_id",
                "lockId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The lock ID, which is used to complete the vault locking process.
    lock_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InputSerialization(autoboto.ShapeBase):
    """
    Describes how the archive is serialized.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "csv",
                "csv",
                autoboto.TypeInfo(CSVInput),
            ),
        ]

    # Describes the serialization of a CSV-encoded object.
    csv: "CSVInput" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class InsufficientCapacityException(autoboto.ShapeBase):
    """
    Returned if there is insufficient capacity to process this expedited request.
    This error only applies to expedited retrievals and not to standard or bulk
    retrievals.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(str),
            ),
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

    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
    code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidParameterValueException(autoboto.ShapeBase):
    """
    Returned if a parameter of the request is incorrectly specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(str),
            ),
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

    # Client
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # 400 Bad Request
    code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Returned if a parameter of the request is incorrectly specified.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InventoryRetrievalJobDescription(autoboto.ShapeBase):
    """
    Describes the options for a range inventory retrieval job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "format",
                "Format",
                autoboto.TypeInfo(str),
            ),
            (
                "start_date",
                "StartDate",
                autoboto.TypeInfo(str),
            ),
            (
                "end_date",
                "EndDate",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The output format for the vault inventory list, which is set by the
    # **InitiateJob** request when initiating a job to retrieve a vault
    # inventory. Valid values are `CSV` and `JSON`.
    format: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The start of the date range in Universal Coordinated Time (UTC) for vault
    # inventory retrieval that includes archives created on or after this date.
    # This value should be a string in the ISO 8601 date format, for example
    # `2013-03-20T17:03:43Z`.
    start_date: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The end of the date range in UTC for vault inventory retrieval that
    # includes archives created before this date. This value should be a string
    # in the ISO 8601 date format, for example `2013-03-20T17:03:43Z`.
    end_date: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of inventory items returned per vault inventory
    # retrieval request. This limit is set when initiating the job with the a
    # **InitiateJob** request.
    limit: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An opaque string that represents where to continue pagination of the vault
    # inventory retrieval results. You use the marker in a new **InitiateJob**
    # request to obtain additional inventory items. If there are no more
    # inventory items, this value is `null`. For more information, see [ Range
    # Inventory
    # Retrieval](http://docs.aws.amazon.com/amazonglacier/latest/dev/api-
    # initiate-job-post.html#api-initiate-job-post-vault-inventory-list-
    # filtering).
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InventoryRetrievalJobInput(autoboto.ShapeBase):
    """
    Provides options for specifying a range inventory retrieval job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start_date",
                "StartDate",
                autoboto.TypeInfo(str),
            ),
            (
                "end_date",
                "EndDate",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                autoboto.TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The start of the date range in UTC for vault inventory retrieval that
    # includes archives created on or after this date. This value should be a
    # string in the ISO 8601 date format, for example `2013-03-20T17:03:43Z`.
    start_date: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The end of the date range in UTC for vault inventory retrieval that
    # includes archives created before this date. This value should be a string
    # in the ISO 8601 date format, for example `2013-03-20T17:03:43Z`.
    end_date: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the maximum number of inventory items returned per vault
    # inventory retrieval request. Valid values are greater than or equal to 1.
    limit: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An opaque string that represents where to continue pagination of the vault
    # inventory retrieval results. You use the marker in a new **InitiateJob**
    # request to obtain additional inventory items. If there are no more
    # inventory items, this value is `null`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class JobParameters(autoboto.ShapeBase):
    """
    Provides options for defining a job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "format",
                "Format",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
            (
                "archive_id",
                "ArchiveId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "sns_topic",
                "SNSTopic",
                autoboto.TypeInfo(str),
            ),
            (
                "retrieval_byte_range",
                "RetrievalByteRange",
                autoboto.TypeInfo(str),
            ),
            (
                "tier",
                "Tier",
                autoboto.TypeInfo(str),
            ),
            (
                "inventory_retrieval_parameters",
                "InventoryRetrievalParameters",
                autoboto.TypeInfo(InventoryRetrievalJobInput),
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

    # When initiating a job to retrieve a vault inventory, you can optionally add
    # this parameter to your request to specify the output format. If you are
    # initiating an inventory job and do not specify a Format field, JSON is the
    # default format. Valid values are "CSV" and "JSON".
    format: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The job type. You can initiate a job to perform a select query on an
    # archive, retrieve an archive, or get an inventory of a vault. Valid values
    # are "select", "archive-retrieval" and "inventory-retrieval".
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the archive that you want to retrieve. This field is required
    # only if `Type` is set to `select` or `archive-retrieval`code>. An error
    # occurs if you specify this request parameter for an inventory retrieval job
    # request.
    archive_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The optional description for the job. The description must be less than or
    # equal to 1,024 bytes. The allowable characters are 7-bit ASCII without
    # control codes-specifically, ASCII values 32-126 decimal or 0x20-0x7E
    # hexadecimal.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon SNS topic ARN to which Amazon Glacier sends a notification when
    # the job is completed and the output is ready for you to download. The
    # specified topic publishes the notification to its subscribers. The SNS
    # topic must exist.
    sns_topic: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The byte range to retrieve for an archive retrieval. in the form "
    # _StartByteValue_ - _EndByteValue_ " If not specified, the whole archive is
    # retrieved. If specified, the byte range must be megabyte (1024*1024)
    # aligned which means that _StartByteValue_ must be divisible by 1 MB and
    # _EndByteValue_ plus 1 must be divisible by 1 MB or be the end of the
    # archive specified as the archive byte size value minus 1. If
    # RetrievalByteRange is not megabyte aligned, this operation returns a 400
    # response.

    # An error occurs if you specify this field for an inventory retrieval job
    # request.
    retrieval_byte_range: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The tier to use for a select or an archive retrieval job. Valid values are
    # `Expedited`, `Standard`, or `Bulk`. `Standard` is the default.
    tier: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Input parameters used for range inventory retrieval.
    inventory_retrieval_parameters: "InventoryRetrievalJobInput" = dataclasses.field(
        default_factory=dict,
    )

    # Contains the parameters that define a job.
    select_parameters: "SelectParameters" = dataclasses.field(
        default_factory=dict,
    )

    # Contains information about the location where the select job results are
    # stored.
    output_location: "OutputLocation" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    Returned if the request results in a vault or account limit being exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(str),
            ),
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

    # Client
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # 400 Bad Request
    code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Returned if the request results in a vault limit or tags limit being
    # exceeded.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListJobsInput(autoboto.ShapeBase):
    """
    Provides options for retrieving a job list for an Amazon Glacier vault.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(str),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "statuscode",
                "statuscode",
                autoboto.TypeInfo(str),
            ),
            (
                "completed",
                "completed",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of jobs to be returned. The default limit is 50. The
    # number of jobs returned might be fewer than the specified limit, but the
    # number of returned jobs never exceeds the limit.
    limit: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An opaque string used for pagination. This value specifies the job at which
    # the listing of jobs should begin. Get the marker value from a previous List
    # Jobs response. You only need to include the marker if you are continuing
    # the pagination of results started in a previous List Jobs request.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of job status to return. You can specify the following values:
    # `InProgress`, `Succeeded`, or `Failed`.
    statuscode: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The state of the jobs to return. You can specify `true` or `false`.
    completed: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListJobsOutput(autoboto.ShapeBase):
    """
    Contains the Amazon Glacier response to your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_list",
                "JobList",
                autoboto.TypeInfo(typing.List[GlacierJobDescription]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of job objects. Each job object contains metadata describing the
    # job.
    job_list: typing.List["GlacierJobDescription"] = dataclasses.field(
        default_factory=list,
    )

    # An opaque string used for pagination that specifies the job at which the
    # listing of jobs should begin. You get the `marker` value from a previous
    # List Jobs response. You only need to include the marker if you are
    # continuing the pagination of the results started in a previous List Jobs
    # request.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListMultipartUploadsInput(autoboto.ShapeBase):
    """
    Provides options for retrieving list of in-progress multipart uploads for an
    Amazon Glacier vault.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An opaque string used for pagination. This value specifies the upload at
    # which the listing of uploads should begin. Get the marker value from a
    # previous List Uploads response. You need only include the marker if you are
    # continuing the pagination of results started in a previous List Uploads
    # request.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the maximum number of uploads returned in the response body. If
    # this value is not specified, the List Uploads operation returns up to 50
    # uploads.
    limit: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListMultipartUploadsOutput(autoboto.ShapeBase):
    """
    Contains the Amazon Glacier response to your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "uploads_list",
                "UploadsList",
                autoboto.TypeInfo(typing.List[UploadListElement]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of in-progress multipart uploads.
    uploads_list: typing.List["UploadListElement"] = dataclasses.field(
        default_factory=list,
    )

    # An opaque string that represents where to continue pagination of the
    # results. You use the marker in a new List Multipart Uploads request to
    # obtain more uploads in the list. If there are no more uploads, this value
    # is `null`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListPartsInput(autoboto.ShapeBase):
    """
    Provides options for retrieving a list of parts of an archive that have been
    uploaded in a specific multipart upload.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id",
                "uploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The upload ID of the multipart upload.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An opaque string used for pagination. This value specifies the part at
    # which the listing of parts should begin. Get the marker value from the
    # response of a previous List Parts response. You need only include the
    # marker if you are continuing the pagination of results started in a
    # previous List Parts request.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of parts to be returned. The default limit is 50. The
    # number of parts returned might be fewer than the specified limit, but the
    # number of returned parts never exceeds the limit.
    limit: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListPartsOutput(autoboto.ShapeBase):
    """
    Contains the Amazon Glacier response to your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "multipart_upload_id",
                "MultipartUploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_arn",
                "VaultARN",
                autoboto.TypeInfo(str),
            ),
            (
                "archive_description",
                "ArchiveDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "part_size_in_bytes",
                "PartSizeInBytes",
                autoboto.TypeInfo(int),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
            (
                "parts",
                "Parts",
                autoboto.TypeInfo(typing.List[PartListElement]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the upload to which the parts are associated.
    multipart_upload_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the vault to which the multipart upload
    # was initiated.
    vault_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The description of the archive that was specified in the Initiate Multipart
    # Upload request.
    archive_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The part size in bytes. This is the same value that you specified in the
    # Initiate Multipart Upload request.
    part_size_in_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The UTC time at which the multipart upload was initiated.
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of the part sizes of the multipart upload. Each object in the array
    # contains a `RangeBytes` and `sha256-tree-hash` name/value pair.
    parts: typing.List["PartListElement"] = dataclasses.field(
        default_factory=list,
    )

    # An opaque string that represents where to continue pagination of the
    # results. You use the marker in a new List Parts request to obtain more jobs
    # in the list. If there are no more parts, this value is `null`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListProvisionedCapacityInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The AWS account ID of the account that owns the vault. You can either
    # specify an AWS account ID or optionally a single '-' (hyphen), in which
    # case Amazon Glacier uses the AWS account ID associated with the credentials
    # used to sign the request. If you use an account ID, don't include any
    # hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListProvisionedCapacityOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "provisioned_capacity_list",
                "ProvisionedCapacityList",
                autoboto.TypeInfo(typing.List[ProvisionedCapacityDescription]),
            ),
        ]

    # The response body contains the following JSON fields.
    provisioned_capacity_list: typing.List["ProvisionedCapacityDescription"
                                          ] = dataclasses.field(
                                              default_factory=list,
                                          )


@dataclasses.dataclass
class ListTagsForVaultInput(autoboto.ShapeBase):
    """
    The input value for `ListTagsForVaultInput`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListTagsForVaultOutput(autoboto.ShapeBase):
    """
    Contains the Amazon Glacier response to your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The tags attached to the vault. Each tag is composed of a key and a value.
    tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ListVaultsInput(autoboto.ShapeBase):
    """
    Provides options to retrieve the vault list owned by the calling user's account.
    The list provides metadata information for each vault.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "marker",
                "marker",
                autoboto.TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `AccountId` value is the AWS account ID. This value must match the AWS
    # account ID associated with the credentials used to sign the request. You
    # can either specify an AWS account ID or optionally a single '`-`' (hyphen),
    # in which case Amazon Glacier uses the AWS account ID associated with the
    # credentials used to sign the request. If you specify your account ID, do
    # not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A string used for pagination. The marker specifies the vault ARN after
    # which the listing of vaults should begin.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of vaults to be returned. The default limit is 10. The
    # number of vaults returned might be fewer than the specified limit, but the
    # number of returned vaults never exceeds the limit.
    limit: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListVaultsOutput(autoboto.ShapeBase):
    """
    Contains the Amazon Glacier response to your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vault_list",
                "VaultList",
                autoboto.TypeInfo(typing.List[DescribeVaultOutput]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # List of vaults.
    vault_list: typing.List["DescribeVaultOutput"] = dataclasses.field(
        default_factory=list,
    )

    # The vault ARN at which to continue pagination of the results. You use the
    # marker in another List Vaults request to obtain more vaults in the list.
    marker: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class MissingParameterValueException(autoboto.ShapeBase):
    """
    Returned if a required header or parameter is missing from the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(str),
            ),
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

    # Client.
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # 400 Bad Request
    code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Returned if no authentication data is found for the request.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class OutputLocation(autoboto.ShapeBase):
    """
    Contains information about the location where the select job results are stored.
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

    # Describes an S3 location that will receive the results of the job request.
    s3: "S3Location" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class OutputSerialization(autoboto.ShapeBase):
    """
    Describes how the select output is serialized.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "csv",
                "csv",
                autoboto.TypeInfo(CSVOutput),
            ),
        ]

    # Describes the serialization of CSV-encoded query results.
    csv: "CSVOutput" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PartListElement(autoboto.ShapeBase):
    """
    A list of the part sizes of the multipart upload.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "range_in_bytes",
                "RangeInBytes",
                autoboto.TypeInfo(str),
            ),
            (
                "sha256_tree_hash",
                "SHA256TreeHash",
                autoboto.TypeInfo(str),
            ),
        ]

    # The byte range of a part, inclusive of the upper value of the range.
    range_in_bytes: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The SHA256 tree hash value that Amazon Glacier calculated for the part.
    # This field is never `null`.
    sha256_tree_hash: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class Permission(Enum):
    FULL_CONTROL = "FULL_CONTROL"
    WRITE = "WRITE"
    WRITE_ACP = "WRITE_ACP"
    READ = "READ"
    READ_ACP = "READ_ACP"


@dataclasses.dataclass
class PolicyEnforcedException(autoboto.ShapeBase):
    """
    Returned if a retrieval job would exceed the current data policy's retrieval
    rate limit. For more information about data retrieval policies,
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(str),
            ),
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

    # Client
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # PolicyEnforcedException
    code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # InitiateJob request denied by current data retrieval policy.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ProvisionedCapacityDescription(autoboto.ShapeBase):
    """
    The definition for a provisioned capacity unit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "capacity_id",
                "CapacityId",
                autoboto.TypeInfo(str),
            ),
            (
                "start_date",
                "StartDate",
                autoboto.TypeInfo(str),
            ),
            (
                "expiration_date",
                "ExpirationDate",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID that identifies the provisioned capacity unit.
    capacity_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date that the provisioned capacity unit was purchased, in Universal
    # Coordinated Time (UTC).
    start_date: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date that the provisioned capacity unit expires, in Universal
    # Coordinated Time (UTC).
    expiration_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PurchaseProvisionedCapacityInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The AWS account ID of the account that owns the vault. You can either
    # specify an AWS account ID or optionally a single '-' (hyphen), in which
    # case Amazon Glacier uses the AWS account ID associated with the credentials
    # used to sign the request. If you use an account ID, don't include any
    # hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class PurchaseProvisionedCapacityOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "capacity_id",
                "capacityId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID that identifies the provisioned capacity unit.
    capacity_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class QuoteFields(Enum):
    ALWAYS = "ALWAYS"
    ASNEEDED = "ASNEEDED"


@dataclasses.dataclass
class RemoveTagsFromVaultInput(autoboto.ShapeBase):
    """
    The input value for `RemoveTagsFromVaultInput`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of tag keys. Each corresponding tag is removed from the vault.
    tag_keys: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class RequestTimeoutException(autoboto.ShapeBase):
    """
    Returned if, when uploading an archive, Amazon Glacier times out while receiving
    the upload.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(str),
            ),
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

    # Client
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # 408 Request Timeout
    code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Returned if, when uploading an archive, Amazon Glacier times out while
    # receiving the upload.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    Returned if the specified resource (such as a vault, upload ID, or job ID)
    doesn't exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(str),
            ),
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

    # Client
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # 404 Not Found
    code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Returned if the specified resource (such as a vault, upload ID, or job ID)
    # doesn't exist.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class S3Location(autoboto.ShapeBase):
    """
    Contains information about the location in Amazon S3 where the select job
    results are stored.
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
                autoboto.TypeInfo(CannedACL),
            ),
            (
                "access_control_list",
                "AccessControlList",
                autoboto.TypeInfo(typing.List[Grant]),
            ),
            (
                "tagging",
                "Tagging",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "user_metadata",
                "UserMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "storage_class",
                "StorageClass",
                autoboto.TypeInfo(StorageClass),
            ),
        ]

    # The name of the Amazon S3 bucket where the job results are stored.
    bucket_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The prefix that is prepended to the results for this request.
    prefix: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Contains information about the encryption used to store the job results in
    # Amazon S3.
    encryption: "Encryption" = dataclasses.field(default_factory=dict, )

    # The canned access control list (ACL) to apply to the job results.
    canned_acl: "CannedACL" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of grants that control access to the staged results.
    access_control_list: typing.List["Grant"] = dataclasses.field(
        default_factory=list,
    )

    # The tag-set that is applied to the job results.
    tagging: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A map of metadata to store with the job results in Amazon S3.
    user_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The storage class used to store the job results.
    storage_class: "StorageClass" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SelectParameters(autoboto.ShapeBase):
    """
    Contains information about the parameters used for a select.
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

    # The type of the provided expression, for example `SQL`.
    expression_type: "ExpressionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The expression that is used to select the object.
    expression: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Describes how the results of the select job are serialized.
    output_serialization: "OutputSerialization" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ServiceUnavailableException(autoboto.ShapeBase):
    """
    Returned if the service cannot complete the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(str),
            ),
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

    # Server
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # 500 Internal Server Error
    code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Returned if the service cannot complete the request.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SetDataRetrievalPolicyInput(autoboto.ShapeBase):
    """
    SetDataRetrievalPolicy input.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "policy",
                "Policy",
                autoboto.TypeInfo(DataRetrievalPolicy),
            ),
        ]

    # The `AccountId` value is the AWS account ID. This value must match the AWS
    # account ID associated with the credentials used to sign the request. You
    # can either specify an AWS account ID or optionally a single '`-`' (hyphen),
    # in which case Amazon Glacier uses the AWS account ID associated with the
    # credentials used to sign the request. If you specify your account ID, do
    # not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The data retrieval policy in JSON format.
    policy: "DataRetrievalPolicy" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class SetVaultAccessPolicyInput(autoboto.ShapeBase):
    """
    SetVaultAccessPolicy input.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "policy",
                "policy",
                autoboto.TypeInfo(VaultAccessPolicy),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The vault access policy as a JSON string.
    policy: "VaultAccessPolicy" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class SetVaultNotificationsInput(autoboto.ShapeBase):
    """
    Provides options to configure notifications that will be sent when specific
    events happen to a vault.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_notification_config",
                "vaultNotificationConfig",
                autoboto.TypeInfo(VaultNotificationConfig),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Provides options for specifying notification configuration.
    vault_notification_config: "VaultNotificationConfig" = dataclasses.field(
        default_factory=dict,
    )


class StatusCode(Enum):
    InProgress = "InProgress"
    Succeeded = "Succeeded"
    Failed = "Failed"


class StorageClass(Enum):
    STANDARD = "STANDARD"
    REDUCED_REDUNDANCY = "REDUCED_REDUNDANCY"
    STANDARD_IA = "STANDARD_IA"


class Stream(botocore.response.StreamingBody):
    pass


class Type(Enum):
    AmazonCustomerByEmail = "AmazonCustomerByEmail"
    CanonicalUser = "CanonicalUser"
    Group = "Group"


@dataclasses.dataclass
class UploadArchiveInput(autoboto.ShapeBase):
    """
    Provides options to add an archive to a vault.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "archive_description",
                "archiveDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                autoboto.TypeInfo(str),
            ),
            (
                "body",
                "body",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The optional description of the archive you are uploading.
    archive_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The SHA256 tree hash of the data being uploaded.
    checksum: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The data to upload.
    body: typing.Any = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UploadListElement(autoboto.ShapeBase):
    """
    A list of in-progress multipart uploads for a vault.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "multipart_upload_id",
                "MultipartUploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_arn",
                "VaultARN",
                autoboto.TypeInfo(str),
            ),
            (
                "archive_description",
                "ArchiveDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "part_size_in_bytes",
                "PartSizeInBytes",
                autoboto.TypeInfo(int),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of a multipart upload.
    multipart_upload_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the vault that contains the archive.
    vault_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The description of the archive that was specified in the Initiate Multipart
    # Upload request.
    archive_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The part size, in bytes, specified in the Initiate Multipart Upload
    # request. This is the size of all the parts in the upload except the last
    # part, which may be smaller than this size.
    part_size_in_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The UTC time at which the multipart upload was initiated.
    creation_date: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UploadMultipartPartInput(autoboto.ShapeBase):
    """
    Provides options to upload a part of an archive in a multipart upload operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "accountId",
                autoboto.TypeInfo(str),
            ),
            (
                "vault_name",
                "vaultName",
                autoboto.TypeInfo(str),
            ),
            (
                "upload_id",
                "uploadId",
                autoboto.TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                autoboto.TypeInfo(str),
            ),
            (
                "range",
                "range",
                autoboto.TypeInfo(str),
            ),
            (
                "body",
                "body",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # The `AccountId` value is the AWS account ID of the account that owns the
    # vault. You can either specify an AWS account ID or optionally a single
    # '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID
    # associated with the credentials used to sign the request. If you use an
    # account ID, do not include any hyphens ('-') in the ID.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the vault.
    vault_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The upload ID of the multipart upload.
    upload_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The SHA256 tree hash of the data being uploaded.
    checksum: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Identifies the range of bytes in the assembled archive that will be
    # uploaded in this part. Amazon Glacier uses this information to assemble the
    # archive in the proper sequence. The format of this header follows RFC 2616.
    # An example header is Content-Range:bytes 0-4194303/*.
    range: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The data to upload.
    body: typing.Any = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UploadMultipartPartOutput(autoboto.ShapeBase):
    """
    Contains the Amazon Glacier response to your request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "checksum",
                "checksum",
                autoboto.TypeInfo(str),
            ),
        ]

    # The SHA256 tree hash that Amazon Glacier computed for the uploaded part.
    checksum: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class VaultAccessPolicy(autoboto.ShapeBase):
    """
    Contains the vault access policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy",
                "Policy",
                autoboto.TypeInfo(str),
            ),
        ]

    # The vault access policy.
    policy: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class VaultLockPolicy(autoboto.ShapeBase):
    """
    Contains the vault lock policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy",
                "Policy",
                autoboto.TypeInfo(str),
            ),
        ]

    # The vault lock policy.
    policy: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class VaultNotificationConfig(autoboto.ShapeBase):
    """
    Represents a vault's notification configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sns_topic",
                "SNSTopic",
                autoboto.TypeInfo(str),
            ),
            (
                "events",
                "Events",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource
    # Name (ARN).
    sns_topic: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of one or more events for which Amazon Glacier will send a
    # notification to the specified Amazon SNS topic.
    events: typing.List[str] = dataclasses.field(default_factory=list, )
