import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AddRoleToDBClusterMessage(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the DB cluster to associate the IAM role with.
    db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the IAM role to associate with the
    # Neptune DB cluster, for example
    # `arn:aws:iam::123456789012:role/NeptuneAccessRole`.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddSourceIdentifierToSubscriptionMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_name",
                "SubscriptionName",
                autoboto.TypeInfo(str),
            ),
            (
                "source_identifier",
                "SourceIdentifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the event notification subscription you want to add a source
    # identifier to.
    subscription_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the event source to be added.

    # Constraints:

    #   * If the source type is a DB instance, then a `DBInstanceIdentifier` must be supplied.

    #   * If the source type is a DB security group, a `DBSecurityGroupName` must be supplied.

    #   * If the source type is a DB parameter group, a `DBParameterGroupName` must be supplied.

    #   * If the source type is a DB snapshot, a `DBSnapshotIdentifier` must be supplied.
    source_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddSourceIdentifierToSubscriptionResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_subscription",
                "EventSubscription",
                autoboto.TypeInfo(EventSubscription),
            ),
        ]

    # Contains the results of a successful invocation of the
    # DescribeEventSubscriptions action.
    event_subscription: "EventSubscription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class AddTagsToResourceMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_name",
                "ResourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon Neptune resource that the tags are added to. This value is an
    # Amazon Resource Name (ARN). For information about creating an ARN, see [
    # Constructing an Amazon Resource Name
    # (ARN)](http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing).
    resource_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tags to be assigned to the Amazon Neptune resource.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


class ApplyMethod(Enum):
    immediate = "immediate"
    pending_reboot = "pending-reboot"


@dataclasses.dataclass
class ApplyPendingMaintenanceActionMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_identifier",
                "ResourceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "apply_action",
                "ApplyAction",
                autoboto.TypeInfo(str),
            ),
            (
                "opt_in_type",
                "OptInType",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource that the pending maintenance
    # action applies to. For information about creating an ARN, see [
    # Constructing an Amazon Resource Name
    # (ARN)](http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing).
    resource_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The pending maintenance action to apply to this resource.

    # Valid values: `system-update`, `db-upgrade`
    apply_action: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A value that specifies the type of opt-in request, or undoes an opt-in
    # request. An opt-in request of type `immediate` can't be undone.

    # Valid values:

    #   * `immediate` \- Apply the maintenance action immediately.

    #   * `next-maintenance` \- Apply the maintenance action during the next maintenance window for the resource.

    #   * `undo-opt-in` \- Cancel any existing `next-maintenance` opt-in requests.
    opt_in_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ApplyPendingMaintenanceActionResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_pending_maintenance_actions",
                "ResourcePendingMaintenanceActions",
                autoboto.TypeInfo(ResourcePendingMaintenanceActions),
            ),
        ]

    # Describes the pending maintenance actions for a resource.
    resource_pending_maintenance_actions: "ResourcePendingMaintenanceActions" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class AuthorizationNotFoundFault(autoboto.ShapeBase):
    """
    Specified CIDRIP or EC2 security group is not authorized for the specified DB
    security group.

    Neptune may not also be authorized via IAM to perform necessary actions on your
    behalf.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AvailabilityZone(autoboto.ShapeBase):
    """
    Contains Availability Zone information.

    This data type is used as an element in the following data type:

      * OrderableDBInstanceOption
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the availability zone.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CertificateNotFoundFault(autoboto.ShapeBase):
    """
    _CertificateIdentifier_ does not refer to an existing certificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CharacterSet(autoboto.ShapeBase):
    """
    This data type is used as a response element in the action
    DescribeDBEngineVersions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "character_set_name",
                "CharacterSetName",
                autoboto.TypeInfo(str),
            ),
            (
                "character_set_description",
                "CharacterSetDescription",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the character set.
    character_set_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description of the character set.
    character_set_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CloudwatchLogsExportConfiguration(autoboto.ShapeBase):
    """
    The configuration setting for the log types to be enabled for export to
    CloudWatch Logs for a specific DB instance or DB cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enable_log_types",
                "EnableLogTypes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "disable_log_types",
                "DisableLogTypes",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The list of log types to enable.
    enable_log_types: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The list of log types to disable.
    disable_log_types: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CopyDBClusterParameterGroupMessage(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_db_cluster_parameter_group_identifier",
                "SourceDBClusterParameterGroupIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "target_db_cluster_parameter_group_identifier",
                "TargetDBClusterParameterGroupIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "target_db_cluster_parameter_group_description",
                "TargetDBClusterParameterGroupDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The identifier or Amazon Resource Name (ARN) for the source DB cluster
    # parameter group. For information about creating an ARN, see [ Constructing
    # an Amazon Resource Name
    # (ARN)](http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing).

    # Constraints:

    #   * Must specify a valid DB cluster parameter group.

    #   * If the source DB cluster parameter group is in the same AWS Region as the copy, specify a valid DB parameter group identifier, for example `my-db-cluster-param-group`, or a valid ARN.

    #   * If the source DB parameter group is in a different AWS Region than the copy, specify a valid DB cluster parameter group ARN, for example `arn:aws:rds:us-east-1:123456789012:cluster-pg:custom-cluster-group1`.
    source_db_cluster_parameter_group_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier for the copied DB cluster parameter group.

    # Constraints:

    #   * Cannot be null, empty, or blank

    #   * Must contain from 1 to 255 letters, numbers, or hyphens

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # Example: `my-cluster-param-group1`
    target_db_cluster_parameter_group_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A description for the copied DB cluster parameter group.
    target_db_cluster_parameter_group_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of tags. For more information, see [Tagging Amazon Neptune
    # Resources](http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html).
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CopyDBClusterParameterGroupResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group",
                "DBClusterParameterGroup",
                autoboto.TypeInfo(DBClusterParameterGroup),
            ),
        ]

    # Contains the details of an Amazon Neptune DB cluster parameter group.

    # This data type is used as a response element in the
    # DescribeDBClusterParameterGroups action.
    db_cluster_parameter_group: "DBClusterParameterGroup" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CopyDBClusterSnapshotMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_db_cluster_snapshot_identifier",
                "SourceDBClusterSnapshotIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "target_db_cluster_snapshot_identifier",
                "TargetDBClusterSnapshotIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "pre_signed_url",
                "PreSignedUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_tags",
                "CopyTags",
                autoboto.TypeInfo(bool),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The identifier of the DB cluster snapshot to copy. This parameter is not
    # case-sensitive.

    # You can't copy an encrypted, shared DB cluster snapshot from one AWS Region
    # to another.

    # Constraints:

    #   * Must specify a valid system snapshot in the "available" state.

    #   * If the source snapshot is in the same AWS Region as the copy, specify a valid DB snapshot identifier.

    #   * If the source snapshot is in a different AWS Region than the copy, specify a valid DB cluster snapshot ARN.

    # Example: `my-cluster-snapshot1`
    source_db_cluster_snapshot_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the new DB cluster snapshot to create from the source DB
    # cluster snapshot. This parameter is not case-sensitive.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    # Example: `my-cluster-snapshot2`
    target_db_cluster_snapshot_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS AWS KMS key ID for an encrypted DB cluster snapshot. The KMS key ID
    # is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias
    # for the KMS encryption key.

    # If you copy an unencrypted DB cluster snapshot and specify a value for the
    # `KmsKeyId` parameter, Amazon Neptune encrypts the target DB cluster
    # snapshot using the specified KMS encryption key.

    # If you copy an encrypted DB cluster snapshot from your AWS account, you can
    # specify a value for `KmsKeyId` to encrypt the copy with a new KMS
    # encryption key. If you don't specify a value for `KmsKeyId`, then the copy
    # of the DB cluster snapshot is encrypted with the same KMS key as the source
    # DB cluster snapshot.

    # If you copy an encrypted DB cluster snapshot that is shared from another
    # AWS account, then you must specify a value for `KmsKeyId`.

    # To copy an encrypted DB cluster snapshot to another AWS Region, you must
    # set `KmsKeyId` to the KMS key ID you want to use to encrypt the copy of the
    # DB cluster snapshot in the destination AWS Region. KMS encryption keys are
    # specific to the AWS Region that they are created in, and you can't use
    # encryption keys from one AWS Region in another AWS Region.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The URL that contains a Signature Version 4 signed request for the
    # `CopyDBClusterSnapshot` API action in the AWS Region that contains the
    # source DB cluster snapshot to copy. The `PreSignedUrl` parameter must be
    # used when copying an encrypted DB cluster snapshot from another AWS Region.

    # The pre-signed URL must be a valid request for the `CopyDBSClusterSnapshot`
    # API action that can be executed in the source AWS Region that contains the
    # encrypted DB cluster snapshot to be copied. The pre-signed URL request must
    # contain the following parameter values:

    #   * `KmsKeyId` \- The AWS KMS key identifier for the key to use to encrypt the copy of the DB cluster snapshot in the destination AWS Region. This is the same identifier for both the `CopyDBClusterSnapshot` action that is called in the destination AWS Region, and the action contained in the pre-signed URL.

    #   * `DestinationRegion` \- The name of the AWS Region that the DB cluster snapshot will be created in.

    #   * `SourceDBClusterSnapshotIdentifier` \- The DB cluster snapshot identifier for the encrypted DB cluster snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted DB cluster snapshot from the us-west-2 AWS Region, then your `SourceDBClusterSnapshotIdentifier` looks like the following example: `arn:aws:rds:us-west-2:123456789012:cluster-snapshot:neptune-cluster1-snapshot-20161115`.

    # To learn how to generate a Signature Version 4 signed request, see [
    # Authenticating Requests: Using Query Parameters (AWS Signature Version
    # 4)](http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-
    # auth.html) and [ Signature Version 4 Signing
    # Process](http://docs.aws.amazon.com/general/latest/gr/signature-
    # version-4.html).
    pre_signed_url: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # True to copy all tags from the source DB cluster snapshot to the target DB
    # cluster snapshot, and otherwise false. The default is false.
    copy_tags: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of tags. For more information, see [Tagging Amazon Neptune
    # Resources](http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html).
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CopyDBClusterSnapshotResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_snapshot",
                "DBClusterSnapshot",
                autoboto.TypeInfo(DBClusterSnapshot),
            ),
        ]

    # Contains the details for an Amazon Neptune DB cluster snapshot

    # This data type is used as a response element in the
    # DescribeDBClusterSnapshots action.
    db_cluster_snapshot: "DBClusterSnapshot" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CopyDBParameterGroupMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_db_parameter_group_identifier",
                "SourceDBParameterGroupIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "target_db_parameter_group_identifier",
                "TargetDBParameterGroupIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "target_db_parameter_group_description",
                "TargetDBParameterGroupDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The identifier or ARN for the source DB parameter group. For information
    # about creating an ARN, see [ Constructing an Amazon Resource Name
    # (ARN)](http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing).

    # Constraints:

    #   * Must specify a valid DB parameter group.

    #   * Must specify a valid DB parameter group identifier, for example `my-db-param-group`, or a valid ARN.
    source_db_parameter_group_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier for the copied DB parameter group.

    # Constraints:

    #   * Cannot be null, empty, or blank

    #   * Must contain from 1 to 255 letters, numbers, or hyphens

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # Example: `my-db-parameter-group`
    target_db_parameter_group_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A description for the copied DB parameter group.
    target_db_parameter_group_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of tags. For more information, see [Tagging Amazon Neptune
    # Resources](http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html).
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CopyDBParameterGroupResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group",
                "DBParameterGroup",
                autoboto.TypeInfo(DBParameterGroup),
            ),
        ]

    # Contains the details of an Amazon Neptune DB parameter group.

    # This data type is used as a response element in the
    # DescribeDBParameterGroups action.
    db_parameter_group: "DBParameterGroup" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateDBClusterMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                autoboto.TypeInfo(int),
            ),
            (
                "character_set_name",
                "CharacterSetName",
                autoboto.TypeInfo(str),
            ),
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "port",
                "Port",
                autoboto.TypeInfo(int),
            ),
            (
                "master_username",
                "MasterUsername",
                autoboto.TypeInfo(str),
            ),
            (
                "master_user_password",
                "MasterUserPassword",
                autoboto.TypeInfo(str),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                autoboto.TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                autoboto.TypeInfo(str),
            ),
            (
                "replication_source_identifier",
                "ReplicationSourceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "storage_encrypted",
                "StorageEncrypted",
                autoboto.TypeInfo(bool),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "pre_signed_url",
                "PreSignedUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The DB cluster identifier. This parameter is stored as a lowercase string.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    # Example: `my-cluster1`
    db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the database engine to be used for this DB cluster.

    # Valid Values: `neptune`
    engine: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of EC2 Availability Zones that instances in the DB cluster can be
    # created in.
    availability_zones: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The number of days for which automated backups are retained. You must
    # specify a minimum value of 1.

    # Default: 1

    # Constraints:

    #   * Must be a value from 1 to 35
    backup_retention_period: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A value that indicates that the DB cluster should be associated with the
    # specified CharacterSet.
    character_set_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name for your database of up to 64 alpha-numeric characters. If you do
    # not provide a name, Amazon Neptune will not create a database in the DB
    # cluster you are creating.
    database_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the DB cluster parameter group to associate with this DB
    # cluster. If this argument is omitted, the default is used.

    # Constraints:

    #   * If supplied, must match the name of an existing DBClusterParameterGroup.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of EC2 VPC security groups to associate with this DB cluster.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A DB subnet group to associate with this DB cluster.

    # Constraints: Must match the name of an existing DBSubnetGroup. Must not be
    # default.

    # Example: `mySubnetgroup`
    db_subnet_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The version number of the database engine to use.

    # Example: `1.0.1`
    engine_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The port number on which the instances in the DB cluster accept
    # connections.

    # Default: `8182`
    port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the master user for the DB cluster.

    # Constraints:

    #   * Must be 1 to 16 letters or numbers.

    #   * First character must be a letter.

    #   * Cannot be a reserved word for the chosen database engine.
    master_username: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The password for the master database user. This password can contain any
    # printable ASCII character except "/", """, or "@".

    # Constraints: Must contain from 8 to 41 characters.
    master_user_password: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A value that indicates that the DB cluster should be associated with the
    # specified option group.

    # Permanent options can't be removed from an option group. The option group
    # can't be removed from a DB cluster once it is associated with a DB cluster.
    option_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The daily time range during which automated backups are created if
    # automated backups are enabled using the `BackupRetentionPeriod` parameter.

    # The default is a 30-minute window selected at random from an 8-hour block
    # of time for each AWS Region. To see the time blocks available, see [
    # Adjusting the Preferred Maintenance
    # Window](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AdjustingTheMaintenanceWindow.html)
    # in the _Amazon Neptune User Guide._

    # Constraints:

    #   * Must be in the format `hh24:mi-hh24:mi`.

    #   * Must be in Universal Coordinated Time (UTC).

    #   * Must not conflict with the preferred maintenance window.

    #   * Must be at least 30 minutes.
    preferred_backup_window: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The weekly time range during which system maintenance can occur, in
    # Universal Coordinated Time (UTC).

    # Format: `ddd:hh24:mi-ddd:hh24:mi`

    # The default is a 30-minute window selected at random from an 8-hour block
    # of time for each AWS Region, occurring on a random day of the week. To see
    # the time blocks available, see [ Adjusting the Preferred Maintenance
    # Window](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AdjustingTheMaintenanceWindow.html)
    # in the _Amazon Neptune User Guide._

    # Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.

    # Constraints: Minimum 30-minute window.
    preferred_maintenance_window: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the source DB instance or DB cluster if
    # this DB cluster is created as a Read Replica.
    replication_source_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of tags. For more information, see [Tagging Amazon Neptune
    # Resources](http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html).
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # Specifies whether the DB cluster is encrypted.
    storage_encrypted: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS KMS key identifier for an encrypted DB cluster.

    # The KMS key identifier is the Amazon Resource Name (ARN) for the KMS
    # encryption key. If you are creating a DB cluster with the same AWS account
    # that owns the KMS encryption key used to encrypt the new DB cluster, then
    # you can use the KMS key alias instead of the ARN for the KMS encryption
    # key.

    # If an encryption key is not specified in `KmsKeyId`:

    #   * If `ReplicationSourceIdentifier` identifies an encrypted source, then Amazon Neptune will use the encryption key used to encrypt the source. Otherwise, Amazon Neptune will use your default encryption key.

    #   * If the `StorageEncrypted` parameter is true and `ReplicationSourceIdentifier` is not specified, then Amazon Neptune will use your default encryption key.

    # AWS KMS creates the default encryption key for your AWS account. Your AWS
    # account has a different default encryption key for each AWS Region.

    # If you create a Read Replica of an encrypted DB cluster in another AWS
    # Region, you must set `KmsKeyId` to a KMS key ID that is valid in the
    # destination AWS Region. This key is used to encrypt the Read Replica in
    # that AWS Region.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A URL that contains a Signature Version 4 signed request for the
    # `CreateDBCluster` action to be called in the source AWS Region where the DB
    # cluster is replicated from. You only need to specify `PreSignedUrl` when
    # you are performing cross-region replication from an encrypted DB cluster.

    # The pre-signed URL must be a valid request for the `CreateDBCluster` API
    # action that can be executed in the source AWS Region that contains the
    # encrypted DB cluster to be copied.

    # The pre-signed URL request must contain the following parameter values:

    #   * `KmsKeyId` \- The AWS KMS key identifier for the key to use to encrypt the copy of the DB cluster in the destination AWS Region. This should refer to the same KMS key for both the `CreateDBCluster` action that is called in the destination AWS Region, and the action contained in the pre-signed URL.

    #   * `DestinationRegion` \- The name of the AWS Region that Read Replica will be created in.

    #   * `ReplicationSourceIdentifier` \- The DB cluster identifier for the encrypted DB cluster to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted DB cluster from the us-west-2 AWS Region, then your `ReplicationSourceIdentifier` would look like Example: `arn:aws:rds:us-west-2:123456789012:cluster:neptune-cluster1`.

    # To learn how to generate a Signature Version 4 signed request, see [
    # Authenticating Requests: Using Query Parameters (AWS Signature Version
    # 4)](http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-
    # auth.html) and [ Signature Version 4 Signing
    # Process](http://docs.aws.amazon.com/general/latest/gr/signature-
    # version-4.html).
    pre_signed_url: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # True to enable mapping of AWS Identity and Access Management (IAM) accounts
    # to database accounts, and otherwise false.

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDBClusterParameterGroupMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "db_parameter_group_family",
                "DBParameterGroupFamily",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the DB cluster parameter group.

    # Constraints:

    #   * Must match the name of an existing DBClusterParameterGroup.

    # This value is stored as a lowercase string.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The DB cluster parameter group family name. A DB cluster parameter group
    # can be associated with one and only one DB cluster parameter group family,
    # and can be applied only to a DB cluster running a database engine and
    # engine version compatible with that DB cluster parameter group family.
    db_parameter_group_family: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description for the DB cluster parameter group.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of tags. For more information, see [Tagging Amazon Neptune
    # Resources](http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html).
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateDBClusterParameterGroupResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group",
                "DBClusterParameterGroup",
                autoboto.TypeInfo(DBClusterParameterGroup),
            ),
        ]

    # Contains the details of an Amazon Neptune DB cluster parameter group.

    # This data type is used as a response element in the
    # DescribeDBClusterParameterGroups action.
    db_cluster_parameter_group: "DBClusterParameterGroup" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateDBClusterResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster",
                "DBCluster",
                autoboto.TypeInfo(DBCluster),
            ),
        ]

    # Contains the details of an Amazon Neptune DB cluster.

    # This data type is used as a response element in the DescribeDBClusters
    # action.
    db_cluster: "DBCluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateDBClusterSnapshotMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_snapshot_identifier",
                "DBClusterSnapshotIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The identifier of the DB cluster snapshot. This parameter is stored as a
    # lowercase string.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    # Example: `my-cluster1-snapshot1`
    db_cluster_snapshot_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the DB cluster to create a snapshot for. This parameter
    # is not case-sensitive.

    # Constraints:

    #   * Must match the identifier of an existing DBCluster.

    # Example: `my-cluster1`
    db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The tags to be assigned to the DB cluster snapshot.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateDBClusterSnapshotResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_snapshot",
                "DBClusterSnapshot",
                autoboto.TypeInfo(DBClusterSnapshot),
            ),
        ]

    # Contains the details for an Amazon Neptune DB cluster snapshot

    # This data type is used as a response element in the
    # DescribeDBClusterSnapshots action.
    db_cluster_snapshot: "DBClusterSnapshot" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateDBInstanceMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "db_instance_class",
                "DBInstanceClass",
                autoboto.TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                autoboto.TypeInfo(str),
            ),
            (
                "db_name",
                "DBName",
                autoboto.TypeInfo(str),
            ),
            (
                "allocated_storage",
                "AllocatedStorage",
                autoboto.TypeInfo(int),
            ),
            (
                "master_username",
                "MasterUsername",
                autoboto.TypeInfo(str),
            ),
            (
                "master_user_password",
                "MasterUserPassword",
                autoboto.TypeInfo(str),
            ),
            (
                "db_security_groups",
                "DBSecurityGroups",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                autoboto.TypeInfo(str),
            ),
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                autoboto.TypeInfo(int),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                autoboto.TypeInfo(str),
            ),
            (
                "port",
                "Port",
                autoboto.TypeInfo(int),
            ),
            (
                "multi_az",
                "MultiAZ",
                autoboto.TypeInfo(bool),
            ),
            (
                "engine_version",
                "EngineVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                autoboto.TypeInfo(bool),
            ),
            (
                "license_model",
                "LicenseModel",
                autoboto.TypeInfo(str),
            ),
            (
                "iops",
                "Iops",
                autoboto.TypeInfo(int),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "character_set_name",
                "CharacterSetName",
                autoboto.TypeInfo(str),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                autoboto.TypeInfo(bool),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "storage_type",
                "StorageType",
                autoboto.TypeInfo(str),
            ),
            (
                "tde_credential_arn",
                "TdeCredentialArn",
                autoboto.TypeInfo(str),
            ),
            (
                "tde_credential_password",
                "TdeCredentialPassword",
                autoboto.TypeInfo(str),
            ),
            (
                "storage_encrypted",
                "StorageEncrypted",
                autoboto.TypeInfo(bool),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "domain",
                "Domain",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_tags_to_snapshot",
                "CopyTagsToSnapshot",
                autoboto.TypeInfo(bool),
            ),
            (
                "monitoring_interval",
                "MonitoringInterval",
                autoboto.TypeInfo(int),
            ),
            (
                "monitoring_role_arn",
                "MonitoringRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "domain_iam_role_name",
                "DomainIAMRoleName",
                autoboto.TypeInfo(str),
            ),
            (
                "promotion_tier",
                "PromotionTier",
                autoboto.TypeInfo(int),
            ),
            (
                "timezone",
                "Timezone",
                autoboto.TypeInfo(str),
            ),
            (
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                autoboto.TypeInfo(bool),
            ),
            (
                "enable_performance_insights",
                "EnablePerformanceInsights",
                autoboto.TypeInfo(bool),
            ),
            (
                "performance_insights_kms_key_id",
                "PerformanceInsightsKMSKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "enable_cloudwatch_logs_exports",
                "EnableCloudwatchLogsExports",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The DB instance identifier. This parameter is stored as a lowercase string.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    # Example: `mydbinstance`
    db_instance_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The compute and memory capacity of the DB instance, for example,
    # `db.m4.large`. Not all DB instance classes are available in all AWS
    # Regions.
    db_instance_class: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the database engine to be used for this instance.

    # Valid Values: `neptune`
    engine: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The database name.

    # Type: String
    db_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The amount of storage (in gibibytes) to allocate for the DB instance.

    # Type: Integer

    # Not applicable. Neptune cluster volumes automatically grow as the amount of
    # data in your database increases, though you are only charged for the space
    # that you use in a Neptune cluster volume.
    allocated_storage: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name for the master user. Not used.
    master_username: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The password for the master user. The password can include any printable
    # ASCII character except "/", """, or "@".

    # Not used.
    master_user_password: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of DB security groups to associate with this DB instance.

    # Default: The default DB security group for the database engine.
    db_security_groups: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list of EC2 VPC security groups to associate with this DB instance.

    # Not applicable. The associated list of EC2 VPC security groups is managed
    # by the DB cluster. For more information, see CreateDBCluster.

    # Default: The default EC2 VPC security group for the DB subnet group's VPC.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The EC2 Availability Zone that the DB instance is created in.

    # Default: A random, system-chosen Availability Zone in the endpoint's AWS
    # Region.

    # Example: `us-east-1d`

    # Constraint: The AvailabilityZone parameter can't be specified if the
    # MultiAZ parameter is set to `true`. The specified Availability Zone must be
    # in the same AWS Region as the current endpoint.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A DB subnet group to associate with this DB instance.

    # If there is no DB subnet group, then it is a non-VPC DB instance.
    db_subnet_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time range each week during which system maintenance can occur, in
    # Universal Coordinated Time (UTC).

    # Format: `ddd:hh24:mi-ddd:hh24:mi`

    # The default is a 30-minute window selected at random from an 8-hour block
    # of time for each AWS Region, occurring on a random day of the week.

    # Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.

    # Constraints: Minimum 30-minute window.
    preferred_maintenance_window: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the DB parameter group to associate with this DB instance. If
    # this argument is omitted, the default DBParameterGroup for the specified
    # engine is used.

    # Constraints:

    #   * Must be 1 to 255 letters, numbers, or hyphens.

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens
    db_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of days for which automated backups are retained.

    # Not applicable. The retention period for automated backups is managed by
    # the DB cluster. For more information, see CreateDBCluster.

    # Default: 1

    # Constraints:

    #   * Must be a value from 0 to 35

    #   * Cannot be set to 0 if the DB instance is a source to Read Replicas
    backup_retention_period: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The daily time range during which automated backups are created.

    # Not applicable. The daily time range for creating automated backups is
    # managed by the DB cluster. For more information, see CreateDBCluster.
    preferred_backup_window: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The port number on which the database accepts connections.

    # Not applicable. The port is managed by the DB cluster. For more
    # information, see CreateDBCluster.

    # Default: `8182`

    # Type: Integer
    port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies if the DB instance is a Multi-AZ deployment. You can't set the
    # AvailabilityZone parameter if the MultiAZ parameter is set to true.
    multi_az: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version number of the database engine to use.
    engine_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates that minor engine upgrades are applied automatically to the DB
    # instance during the maintenance window.

    # Default: `true`
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # License model information for this DB instance.

    # Valid values: `license-included` | `bring-your-own-license` | `general-
    # public-license`
    license_model: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The amount of Provisioned IOPS (input/output operations per second) to be
    # initially allocated for the DB instance.
    iops: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates that the DB instance should be associated with the specified
    # option group.

    # Permanent options, such as the TDE option for Oracle Advanced Security TDE,
    # can't be removed from an option group, and that option group can't be
    # removed from a DB instance once it is associated with a DB instance
    option_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates that the DB instance should be associated with the specified
    # CharacterSet.

    # Not applicable. The character set is managed by the DB cluster. For more
    # information, see CreateDBCluster.
    character_set_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This parameter is not supported.
    publicly_accessible: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of tags. For more information, see [Tagging Amazon Neptune
    # Resources](http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html).
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # The identifier of the DB cluster that the instance will belong to.

    # For information on creating a DB cluster, see CreateDBCluster.

    # Type: String
    db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the storage type to be associated with the DB instance.

    # Not applicable. Storage is managed by the DB Cluster.
    storage_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN from the key store with which to associate the instance for TDE
    # encryption.
    tde_credential_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The password for the given ARN from the key store in order to access the
    # device.
    tde_credential_password: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether the DB instance is encrypted.

    # Not applicable. The encryption for DB instances is managed by the DB
    # cluster. For more information, see CreateDBCluster.

    # Default: false
    storage_encrypted: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS KMS key identifier for an encrypted DB instance.

    # The KMS key identifier is the Amazon Resource Name (ARN) for the KMS
    # encryption key. If you are creating a DB instance with the same AWS account
    # that owns the KMS encryption key used to encrypt the new DB instance, then
    # you can use the KMS key alias instead of the ARN for the KM encryption key.

    # Not applicable. The KMS key identifier is managed by the DB cluster. For
    # more information, see CreateDBCluster.

    # If the `StorageEncrypted` parameter is true, and you do not specify a value
    # for the `KmsKeyId` parameter, then Amazon Neptune will use your default
    # encryption key. AWS KMS creates the default encryption key for your AWS
    # account. Your AWS account has a different default encryption key for each
    # AWS Region.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specify the Active Directory Domain to create the instance in.
    domain: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # True to copy all tags from the DB instance to snapshots of the DB instance,
    # and otherwise false. The default is false.
    copy_tags_to_snapshot: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The interval, in seconds, between points when Enhanced Monitoring metrics
    # are collected for the DB instance. To disable collecting Enhanced
    # Monitoring metrics, specify 0. The default is 0.

    # If `MonitoringRoleArn` is specified, then you must also set
    # `MonitoringInterval` to a value other than 0.

    # Valid Values: `0, 1, 5, 10, 15, 30, 60`
    monitoring_interval: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN for the IAM role that permits Neptune to send enhanced monitoring
    # metrics to Amazon CloudWatch Logs. For example,
    # `arn:aws:iam:123456789012:role/emaccess`.

    # If `MonitoringInterval` is set to a value other than 0, then you must
    # supply a `MonitoringRoleArn` value.
    monitoring_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specify the name of the IAM role to be used when making API calls to the
    # Directory Service.
    domain_iam_role_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A value that specifies the order in which an Read Replica is promoted to
    # the primary instance after a failure of the existing primary instance.

    # Default: 1

    # Valid Values: 0 - 15
    promotion_tier: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time zone of the DB instance.
    timezone: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # True to enable AWS Identity and Access Management (IAM) authentication for
    # Neptune.

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # True to enable Performance Insights for the DB instance, and otherwise
    # false.
    enable_performance_insights: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS KMS key identifier for encryption of Performance Insights data. The
    # KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the
    # KMS key alias for the KMS encryption key.
    performance_insights_kms_key_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The list of log types that need to be enabled for exporting to CloudWatch
    # Logs.
    enable_cloudwatch_logs_exports: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateDBInstanceResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance",
                "DBInstance",
                autoboto.TypeInfo(DBInstance),
            ),
        ]

    # Contains the details of an Amazon Neptune DB instance.

    # This data type is used as a response element in the DescribeDBInstances
    # action.
    db_instance: "DBInstance" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateDBParameterGroupMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "db_parameter_group_family",
                "DBParameterGroupFamily",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the DB parameter group.

    # Constraints:

    #   * Must be 1 to 255 letters, numbers, or hyphens.

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # This value is stored as a lowercase string.
    db_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The DB parameter group family name. A DB parameter group can be associated
    # with one and only one DB parameter group family, and can be applied only to
    # a DB instance running a database engine and engine version compatible with
    # that DB parameter group family.
    db_parameter_group_family: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description for the DB parameter group.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of tags. For more information, see [Tagging Amazon Neptune
    # Resources](http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html).
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateDBParameterGroupResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group",
                "DBParameterGroup",
                autoboto.TypeInfo(DBParameterGroup),
            ),
        ]

    # Contains the details of an Amazon Neptune DB parameter group.

    # This data type is used as a response element in the
    # DescribeDBParameterGroups action.
    db_parameter_group: "DBParameterGroup" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateDBSubnetGroupMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "db_subnet_group_description",
                "DBSubnetGroupDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name for the DB subnet group. This value is stored as a lowercase
    # string.

    # Constraints: Must contain no more than 255 letters, numbers, periods,
    # underscores, spaces, or hyphens. Must not be default.

    # Example: `mySubnetgroup`
    db_subnet_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description for the DB subnet group.
    db_subnet_group_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The EC2 Subnet IDs for the DB subnet group.
    subnet_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of tags. For more information, see [Tagging Amazon Neptune
    # Resources](http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html).
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateDBSubnetGroupResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_subnet_group",
                "DBSubnetGroup",
                autoboto.TypeInfo(DBSubnetGroup),
            ),
        ]

    # Contains the details of an Amazon Neptune DB subnet group.

    # This data type is used as a response element in the DescribeDBSubnetGroups
    # action.
    db_subnet_group: "DBSubnetGroup" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateEventSubscriptionMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_name",
                "SubscriptionName",
                autoboto.TypeInfo(str),
            ),
            (
                "sns_topic_arn",
                "SnsTopicArn",
                autoboto.TypeInfo(str),
            ),
            (
                "source_type",
                "SourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "event_categories",
                "EventCategories",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "source_ids",
                "SourceIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the subscription.

    # Constraints: The name must be less than 255 characters.
    subscription_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the SNS topic created for event
    # notification. The ARN is created by Amazon SNS when you create a topic and
    # subscribe to it.
    sns_topic_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of source that is generating the events. For example, if you want
    # to be notified of events generated by a DB instance, you would set this
    # parameter to db-instance. if this value is not specified, all events are
    # returned.

    # Valid values: `db-instance` | `db-cluster` | `db-parameter-group` | `db-
    # security-group` | `db-snapshot` | `db-cluster-snapshot`
    source_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of event categories for a SourceType that you want to subscribe to.
    # You can see a list of the categories for a given SourceType by using the
    # **DescribeEventCategories** action.
    event_categories: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The list of identifiers of the event sources for which events are returned.
    # If not specified, then all sources are included in the response. An
    # identifier must begin with a letter and must contain only ASCII letters,
    # digits, and hyphens; it can't end with a hyphen or contain two consecutive
    # hyphens.

    # Constraints:

    #   * If SourceIds are supplied, SourceType must also be provided.

    #   * If the source type is a DB instance, then a `DBInstanceIdentifier` must be supplied.

    #   * If the source type is a DB security group, a `DBSecurityGroupName` must be supplied.

    #   * If the source type is a DB parameter group, a `DBParameterGroupName` must be supplied.

    #   * If the source type is a DB snapshot, a `DBSnapshotIdentifier` must be supplied.
    source_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # A Boolean value; set to **true** to activate the subscription, set to
    # **false** to create the subscription but not active it.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of tags. For more information, see [Tagging Amazon Neptune
    # Resources](http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html).
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class CreateEventSubscriptionResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_subscription",
                "EventSubscription",
                autoboto.TypeInfo(EventSubscription),
            ),
        ]

    # Contains the results of a successful invocation of the
    # DescribeEventSubscriptions action.
    event_subscription: "EventSubscription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DBCluster(autoboto.ShapeBase):
    """
    Contains the details of an Amazon Neptune DB cluster.

    This data type is used as a response element in the DescribeDBClusters action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "allocated_storage",
                "AllocatedStorage",
                autoboto.TypeInfo(int),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                autoboto.TypeInfo(int),
            ),
            (
                "character_set_name",
                "CharacterSetName",
                autoboto.TypeInfo(str),
            ),
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "db_cluster_parameter_group",
                "DBClusterParameterGroup",
                autoboto.TypeInfo(str),
            ),
            (
                "db_subnet_group",
                "DBSubnetGroup",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
            (
                "percent_progress",
                "PercentProgress",
                autoboto.TypeInfo(str),
            ),
            (
                "earliest_restorable_time",
                "EarliestRestorableTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "endpoint",
                "Endpoint",
                autoboto.TypeInfo(str),
            ),
            (
                "reader_endpoint",
                "ReaderEndpoint",
                autoboto.TypeInfo(str),
            ),
            (
                "multi_az",
                "MultiAZ",
                autoboto.TypeInfo(bool),
            ),
            (
                "engine",
                "Engine",
                autoboto.TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "latest_restorable_time",
                "LatestRestorableTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "port",
                "Port",
                autoboto.TypeInfo(int),
            ),
            (
                "master_username",
                "MasterUsername",
                autoboto.TypeInfo(str),
            ),
            (
                "db_cluster_option_group_memberships",
                "DBClusterOptionGroupMemberships",
                autoboto.TypeInfo(typing.List[DBClusterOptionGroupStatus]),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                autoboto.TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                autoboto.TypeInfo(str),
            ),
            (
                "replication_source_identifier",
                "ReplicationSourceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "read_replica_identifiers",
                "ReadReplicaIdentifiers",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "db_cluster_members",
                "DBClusterMembers",
                autoboto.TypeInfo(typing.List[DBClusterMember]),
            ),
            (
                "vpc_security_groups",
                "VpcSecurityGroups",
                autoboto.TypeInfo(typing.List[VpcSecurityGroupMembership]),
            ),
            (
                "hosted_zone_id",
                "HostedZoneId",
                autoboto.TypeInfo(str),
            ),
            (
                "storage_encrypted",
                "StorageEncrypted",
                autoboto.TypeInfo(bool),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "db_cluster_resource_id",
                "DbClusterResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "db_cluster_arn",
                "DBClusterArn",
                autoboto.TypeInfo(str),
            ),
            (
                "associated_roles",
                "AssociatedRoles",
                autoboto.TypeInfo(typing.List[DBClusterRole]),
            ),
            (
                "iam_database_authentication_enabled",
                "IAMDatabaseAuthenticationEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "clone_group_id",
                "CloneGroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "cluster_create_time",
                "ClusterCreateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # `AllocatedStorage` always returns 1, because Neptune DB cluster storage
    # size is not fixed, but instead automatically adjusts as needed.
    allocated_storage: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides the list of EC2 Availability Zones that instances in the DB
    # cluster can be created in.
    availability_zones: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Specifies the number of days for which automatic DB snapshots are retained.
    backup_retention_period: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If present, specifies the name of the character set that this cluster is
    # associated with.
    character_set_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains the name of the initial database of this DB cluster that was
    # provided at create time, if one was specified when the DB cluster was
    # created. This same name is returned for the life of the DB cluster.
    database_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Contains a user-supplied DB cluster identifier. This identifier is the
    # unique key that identifies a DB cluster.
    db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the name of the DB cluster parameter group for the DB cluster.
    db_cluster_parameter_group: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies information on the subnet group associated with the DB cluster,
    # including the name, description, and subnets in the subnet group.
    db_subnet_group: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the current state of this DB cluster.
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the progress of the operation as a percentage.
    percent_progress: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the earliest time to which a database can be restored with point-
    # in-time restore.
    earliest_restorable_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the connection endpoint for the primary instance of the DB
    # cluster.
    endpoint: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The reader endpoint for the DB cluster. The reader endpoint for a DB
    # cluster load-balances connections across the Read Replicas that are
    # available in a DB cluster. As clients request new connections to the reader
    # endpoint, Neptune distributes the connection requests among the Read
    # Replicas in the DB cluster. This functionality can help balance your read
    # workload across multiple Read Replicas in your DB cluster.

    # If a failover occurs, and the Read Replica that you are connected to is
    # promoted to be the primary instance, your connection is dropped. To
    # continue sending your read workload to other Read Replicas in the cluster,
    # you can then reconnect to the reader endpoint.
    reader_endpoint: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether the DB cluster has instances in multiple Availability
    # Zones.
    multi_az: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Provides the name of the database engine to be used for this DB cluster.
    engine: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates the database engine version.
    engine_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the latest time to which a database can be restored with point-
    # in-time restore.
    latest_restorable_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the port that the database engine is listening on.
    port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Contains the master username for the DB cluster.
    master_username: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides the list of option group memberships for this DB cluster.
    db_cluster_option_group_memberships: typing.List[
        "DBClusterOptionGroupStatus"
    ] = dataclasses.field(
        default_factory=list,
    )

    # Specifies the daily time range during which automated backups are created
    # if automated backups are enabled, as determined by the
    # `BackupRetentionPeriod`.
    preferred_backup_window: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the weekly time range during which system maintenance can occur,
    # in Universal Coordinated Time (UTC).
    preferred_maintenance_window: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains the identifier of the source DB cluster if this DB cluster is a
    # Read Replica.
    replication_source_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains one or more identifiers of the Read Replicas associated with this
    # DB cluster.
    read_replica_identifiers: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Provides the list of instances that make up the DB cluster.
    db_cluster_members: typing.List["DBClusterMember"] = dataclasses.field(
        default_factory=list,
    )

    # Provides a list of VPC security groups that the DB cluster belongs to.
    vpc_security_groups: typing.List["VpcSecurityGroupMembership"
                                    ] = dataclasses.field(
                                        default_factory=list,
                                    )

    # Specifies the ID that Amazon Route 53 assigns when you create a hosted
    # zone.
    hosted_zone_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether the DB cluster is encrypted.
    storage_encrypted: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If `StorageEncrypted` is true, the AWS KMS key identifier for the encrypted
    # DB cluster.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The AWS Region-unique, immutable identifier for the DB cluster. This
    # identifier is found in AWS CloudTrail log entries whenever the AWS KMS key
    # for the DB cluster is accessed.
    db_cluster_resource_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) for the DB cluster.
    db_cluster_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides a list of the AWS Identity and Access Management (IAM) roles that
    # are associated with the DB cluster. IAM roles that are associated with a DB
    # cluster grant permission for the DB cluster to access other AWS services on
    # your behalf.
    associated_roles: typing.List["DBClusterRole"] = dataclasses.field(
        default_factory=list,
    )

    # True if mapping of AWS Identity and Access Management (IAM) accounts to
    # database accounts is enabled, and otherwise false.
    iam_database_authentication_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Identifies the clone group to which the DB cluster is associated.
    clone_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the time when the DB cluster was created, in Universal
    # Coordinated Time (UTC).
    cluster_create_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBClusterAlreadyExistsFault(autoboto.ShapeBase):
    """
    User already has a DB cluster with the given identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterMember(autoboto.ShapeBase):
    """
    Contains information about an instance that is part of a DB cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "is_cluster_writer",
                "IsClusterWriter",
                autoboto.TypeInfo(bool),
            ),
            (
                "db_cluster_parameter_group_status",
                "DBClusterParameterGroupStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "promotion_tier",
                "PromotionTier",
                autoboto.TypeInfo(int),
            ),
        ]

    # Specifies the instance identifier for this member of the DB cluster.
    db_instance_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Value that is `true` if the cluster member is the primary instance for the
    # DB cluster and `false` otherwise.
    is_cluster_writer: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the status of the DB cluster parameter group for this member of
    # the DB cluster.
    db_cluster_parameter_group_status: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A value that specifies the order in which a Read Replica is promoted to the
    # primary instance after a failure of the existing primary instance.
    promotion_tier: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBClusterMessage(autoboto.ShapeBase):
    """
    Contains the result of a successful invocation of the DescribeDBClusters action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "db_clusters",
                "DBClusters",
                autoboto.TypeInfo(typing.List[DBCluster]),
            ),
        ]

    # A pagination token that can be used in a subsequent DescribeDBClusters
    # request.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Contains a list of DB clusters for the user.
    db_clusters: typing.List["DBCluster"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DBClusterNotFoundFault(autoboto.ShapeBase):
    """
    _DBClusterIdentifier_ does not refer to an existing DB cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterOptionGroupStatus(autoboto.ShapeBase):
    """
    Contains status information for a DB cluster option group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_option_group_name",
                "DBClusterOptionGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
        ]

    # Specifies the name of the DB cluster option group.
    db_cluster_option_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the status of the DB cluster option group.
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBClusterParameterGroup(autoboto.ShapeBase):
    """
    Contains the details of an Amazon Neptune DB cluster parameter group.

    This data type is used as a response element in the
    DescribeDBClusterParameterGroups action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "db_parameter_group_family",
                "DBParameterGroupFamily",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "db_cluster_parameter_group_arn",
                "DBClusterParameterGroupArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # Provides the name of the DB cluster parameter group.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides the name of the DB parameter group family that this DB cluster
    # parameter group is compatible with.
    db_parameter_group_family: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides the customer-specified description for this DB cluster parameter
    # group.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the DB cluster parameter group.
    db_cluster_parameter_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBClusterParameterGroupDetails(autoboto.ShapeBase):
    """
    Provides details about a DB cluster parameter group including the parameters in
    the DB cluster parameter group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.List[Parameter]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # Provides a list of parameters for the DB cluster parameter group.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default_factory=list,
    )

    # An optional pagination token provided by a previous
    # DescribeDBClusterParameters request. If this parameter is specified, the
    # response includes only records beyond the marker, up to the value specified
    # by `MaxRecords` .
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBClusterParameterGroupNameMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the DB cluster parameter group.

    # Constraints:

    #   * Must be 1 to 255 letters or numbers.

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # This value is stored as a lowercase string.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBClusterParameterGroupNotFoundFault(autoboto.ShapeBase):
    """
    _DBClusterParameterGroupName_ does not refer to an existing DB Cluster parameter
    group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterParameterGroupsMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "db_cluster_parameter_groups",
                "DBClusterParameterGroups",
                autoboto.TypeInfo(typing.List[DBClusterParameterGroup]),
            ),
        ]

    # An optional pagination token provided by a previous
    # `DescribeDBClusterParameterGroups` request. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of DB cluster parameter groups.
    db_cluster_parameter_groups: typing.List["DBClusterParameterGroup"
                                            ] = dataclasses.field(
                                                default_factory=list,
                                            )


@dataclasses.dataclass
class DBClusterQuotaExceededFault(autoboto.ShapeBase):
    """
    User attempted to create a new DB cluster and the user has already reached the
    maximum allowed DB cluster quota.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterRole(autoboto.ShapeBase):
    """
    Describes an AWS Identity and Access Management (IAM) role that is associated
    with a DB cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM role that is associated with the
    # DB cluster.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Describes the state of association between the IAM role and the DB cluster.
    # The Status property returns one of the following values:

    #   * `ACTIVE` \- the IAM role ARN is associated with the DB cluster and can be used to access other AWS services on your behalf.

    #   * `PENDING` \- the IAM role ARN is being associated with the DB cluster.

    #   * `INVALID` \- the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other AWS services on your behalf.
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBClusterRoleAlreadyExistsFault(autoboto.ShapeBase):
    """
    The specified IAM role Amazon Resource Name (ARN) is already associated with the
    specified DB cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterRoleNotFoundFault(autoboto.ShapeBase):
    """
    The specified IAM role Amazon Resource Name (ARN) is not associated with the
    specified DB cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterRoleQuotaExceededFault(autoboto.ShapeBase):
    """
    You have exceeded the maximum number of IAM roles that can be associated with
    the specified DB cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterSnapshot(autoboto.ShapeBase):
    """
    Contains the details for an Amazon Neptune DB cluster snapshot

    This data type is used as a response element in the DescribeDBClusterSnapshots
    action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "availability_zones",
                "AvailabilityZones",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "db_cluster_snapshot_identifier",
                "DBClusterSnapshotIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "snapshot_create_time",
                "SnapshotCreateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "engine",
                "Engine",
                autoboto.TypeInfo(str),
            ),
            (
                "allocated_storage",
                "AllocatedStorage",
                autoboto.TypeInfo(int),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
            (
                "port",
                "Port",
                autoboto.TypeInfo(int),
            ),
            (
                "vpc_id",
                "VpcId",
                autoboto.TypeInfo(str),
            ),
            (
                "cluster_create_time",
                "ClusterCreateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "master_username",
                "MasterUsername",
                autoboto.TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "license_model",
                "LicenseModel",
                autoboto.TypeInfo(str),
            ),
            (
                "snapshot_type",
                "SnapshotType",
                autoboto.TypeInfo(str),
            ),
            (
                "percent_progress",
                "PercentProgress",
                autoboto.TypeInfo(int),
            ),
            (
                "storage_encrypted",
                "StorageEncrypted",
                autoboto.TypeInfo(bool),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "db_cluster_snapshot_arn",
                "DBClusterSnapshotArn",
                autoboto.TypeInfo(str),
            ),
            (
                "source_db_cluster_snapshot_arn",
                "SourceDBClusterSnapshotArn",
                autoboto.TypeInfo(str),
            ),
            (
                "iam_database_authentication_enabled",
                "IAMDatabaseAuthenticationEnabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Provides the list of EC2 Availability Zones that instances in the DB
    # cluster snapshot can be restored in.
    availability_zones: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Specifies the identifier for the DB cluster snapshot.
    db_cluster_snapshot_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the DB cluster identifier of the DB cluster that this DB cluster
    # snapshot was created from.
    db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides the time when the snapshot was taken, in Universal Coordinated
    # Time (UTC).
    snapshot_create_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the name of the database engine.
    engine: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the allocated storage size in gibibytes (GiB).
    allocated_storage: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the status of this DB cluster snapshot.
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the port that the DB cluster was listening on at the time of the
    # snapshot.
    port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Provides the VPC ID associated with the DB cluster snapshot.
    vpc_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the time when the DB cluster was created, in Universal
    # Coordinated Time (UTC).
    cluster_create_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides the master username for the DB cluster snapshot.
    master_username: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides the version of the database engine for this DB cluster snapshot.
    engine_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides the license model information for this DB cluster snapshot.
    license_model: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Provides the type of the DB cluster snapshot.
    snapshot_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the percentage of the estimated data that has been transferred.
    percent_progress: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether the DB cluster snapshot is encrypted.
    storage_encrypted: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If `StorageEncrypted` is true, the AWS KMS key identifier for the encrypted
    # DB cluster snapshot.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the DB cluster snapshot.
    db_cluster_snapshot_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the DB cluster snapshot was copied from a source DB cluster snapshot,
    # the Amazon Resource Name (ARN) for the source DB cluster snapshot,
    # otherwise, a null value.
    source_db_cluster_snapshot_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # True if mapping of AWS Identity and Access Management (IAM) accounts to
    # database accounts is enabled, and otherwise false.
    iam_database_authentication_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBClusterSnapshotAlreadyExistsFault(autoboto.ShapeBase):
    """
    User already has a DB cluster snapshot with the given identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterSnapshotAttribute(autoboto.ShapeBase):
    """
    Contains the name and values of a manual DB cluster snapshot attribute.

    Manual DB cluster snapshot attributes are used to authorize other AWS accounts
    to restore a manual DB cluster snapshot. For more information, see the
    ModifyDBClusterSnapshotAttribute API action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_name",
                "AttributeName",
                autoboto.TypeInfo(str),
            ),
            (
                "attribute_values",
                "AttributeValues",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the manual DB cluster snapshot attribute.

    # The attribute named `restore` refers to the list of AWS accounts that have
    # permission to copy or restore the manual DB cluster snapshot. For more
    # information, see the ModifyDBClusterSnapshotAttribute API action.
    attribute_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The value(s) for the manual DB cluster snapshot attribute.

    # If the `AttributeName` field is set to `restore`, then this element returns
    # a list of IDs of the AWS accounts that are authorized to copy or restore
    # the manual DB cluster snapshot. If a value of `all` is in the list, then
    # the manual DB cluster snapshot is public and available for any AWS account
    # to copy or restore.
    attribute_values: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DBClusterSnapshotAttributesResult(autoboto.ShapeBase):
    """
    Contains the results of a successful call to the
    DescribeDBClusterSnapshotAttributes API action.

    Manual DB cluster snapshot attributes are used to authorize other AWS accounts
    to copy or restore a manual DB cluster snapshot. For more information, see the
    ModifyDBClusterSnapshotAttribute API action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_snapshot_identifier",
                "DBClusterSnapshotIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "db_cluster_snapshot_attributes",
                "DBClusterSnapshotAttributes",
                autoboto.TypeInfo(typing.List[DBClusterSnapshotAttribute]),
            ),
        ]

    # The identifier of the manual DB cluster snapshot that the attributes apply
    # to.
    db_cluster_snapshot_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The list of attributes and values for the manual DB cluster snapshot.
    db_cluster_snapshot_attributes: typing.List["DBClusterSnapshotAttribute"
                                               ] = dataclasses.field(
                                                   default_factory=list,
                                               )


@dataclasses.dataclass
class DBClusterSnapshotMessage(autoboto.ShapeBase):
    """
    Provides a list of DB cluster snapshots for the user as the result of a call to
    the DescribeDBClusterSnapshots action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "db_cluster_snapshots",
                "DBClusterSnapshots",
                autoboto.TypeInfo(typing.List[DBClusterSnapshot]),
            ),
        ]

    # An optional pagination token provided by a previous
    # DescribeDBClusterSnapshots request. If this parameter is specified, the
    # response includes only records beyond the marker, up to the value specified
    # by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Provides a list of DB cluster snapshots for the user.
    db_cluster_snapshots: typing.List["DBClusterSnapshot"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DBClusterSnapshotNotFoundFault(autoboto.ShapeBase):
    """
    _DBClusterSnapshotIdentifier_ does not refer to an existing DB cluster snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBEngineVersion(autoboto.ShapeBase):
    """
    This data type is used as a response element in the action
    DescribeDBEngineVersions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "engine",
                "Engine",
                autoboto.TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "db_parameter_group_family",
                "DBParameterGroupFamily",
                autoboto.TypeInfo(str),
            ),
            (
                "db_engine_description",
                "DBEngineDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "db_engine_version_description",
                "DBEngineVersionDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "default_character_set",
                "DefaultCharacterSet",
                autoboto.TypeInfo(CharacterSet),
            ),
            (
                "supported_character_sets",
                "SupportedCharacterSets",
                autoboto.TypeInfo(typing.List[CharacterSet]),
            ),
            (
                "valid_upgrade_target",
                "ValidUpgradeTarget",
                autoboto.TypeInfo(typing.List[UpgradeTarget]),
            ),
            (
                "supported_timezones",
                "SupportedTimezones",
                autoboto.TypeInfo(typing.List[Timezone]),
            ),
            (
                "exportable_log_types",
                "ExportableLogTypes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "supports_log_exports_to_cloudwatch_logs",
                "SupportsLogExportsToCloudwatchLogs",
                autoboto.TypeInfo(bool),
            ),
            (
                "supports_read_replica",
                "SupportsReadReplica",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the database engine.
    engine: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version number of the database engine.
    engine_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the DB parameter group family for the database engine.
    db_parameter_group_family: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description of the database engine.
    db_engine_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description of the database engine version.
    db_engine_version_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The default character set for new instances of this engine version, if the
    # `CharacterSetName` parameter of the CreateDBInstance API is not specified.
    default_character_set: "CharacterSet" = dataclasses.field(
        default_factory=dict,
    )

    # A list of the character sets supported by this engine for the
    # `CharacterSetName` parameter of the `CreateDBInstance` action.
    supported_character_sets: typing.List["CharacterSet"] = dataclasses.field(
        default_factory=list,
    )

    # A list of engine versions that this database engine version can be upgraded
    # to.
    valid_upgrade_target: typing.List["UpgradeTarget"] = dataclasses.field(
        default_factory=list,
    )

    # A list of the time zones supported by this engine for the `Timezone`
    # parameter of the `CreateDBInstance` action.
    supported_timezones: typing.List["Timezone"] = dataclasses.field(
        default_factory=list,
    )

    # The types of logs that the database engine has available for export to
    # CloudWatch Logs.
    exportable_log_types: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A value that indicates whether the engine version supports exporting the
    # log types specified by ExportableLogTypes to CloudWatch Logs.
    supports_log_exports_to_cloudwatch_logs: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether the database engine version supports read replicas.
    supports_read_replica: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBEngineVersionMessage(autoboto.ShapeBase):
    """
    Contains the result of a successful invocation of the DescribeDBEngineVersions
    action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "db_engine_versions",
                "DBEngineVersions",
                autoboto.TypeInfo(typing.List[DBEngineVersion]),
            ),
        ]

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of `DBEngineVersion` elements.
    db_engine_versions: typing.List["DBEngineVersion"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DBInstance(autoboto.ShapeBase):
    """
    Contains the details of an Amazon Neptune DB instance.

    This data type is used as a response element in the DescribeDBInstances action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "db_instance_class",
                "DBInstanceClass",
                autoboto.TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                autoboto.TypeInfo(str),
            ),
            (
                "db_instance_status",
                "DBInstanceStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "master_username",
                "MasterUsername",
                autoboto.TypeInfo(str),
            ),
            (
                "db_name",
                "DBName",
                autoboto.TypeInfo(str),
            ),
            (
                "endpoint",
                "Endpoint",
                autoboto.TypeInfo(Endpoint),
            ),
            (
                "allocated_storage",
                "AllocatedStorage",
                autoboto.TypeInfo(int),
            ),
            (
                "instance_create_time",
                "InstanceCreateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                autoboto.TypeInfo(str),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                autoboto.TypeInfo(int),
            ),
            (
                "db_security_groups",
                "DBSecurityGroups",
                autoboto.TypeInfo(typing.List[DBSecurityGroupMembership]),
            ),
            (
                "vpc_security_groups",
                "VpcSecurityGroups",
                autoboto.TypeInfo(typing.List[VpcSecurityGroupMembership]),
            ),
            (
                "db_parameter_groups",
                "DBParameterGroups",
                autoboto.TypeInfo(typing.List[DBParameterGroupStatus]),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "db_subnet_group",
                "DBSubnetGroup",
                autoboto.TypeInfo(DBSubnetGroup),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                autoboto.TypeInfo(str),
            ),
            (
                "pending_modified_values",
                "PendingModifiedValues",
                autoboto.TypeInfo(PendingModifiedValues),
            ),
            (
                "latest_restorable_time",
                "LatestRestorableTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "multi_az",
                "MultiAZ",
                autoboto.TypeInfo(bool),
            ),
            (
                "engine_version",
                "EngineVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                autoboto.TypeInfo(bool),
            ),
            (
                "read_replica_source_db_instance_identifier",
                "ReadReplicaSourceDBInstanceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "read_replica_db_instance_identifiers",
                "ReadReplicaDBInstanceIdentifiers",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "read_replica_db_cluster_identifiers",
                "ReadReplicaDBClusterIdentifiers",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "license_model",
                "LicenseModel",
                autoboto.TypeInfo(str),
            ),
            (
                "iops",
                "Iops",
                autoboto.TypeInfo(int),
            ),
            (
                "option_group_memberships",
                "OptionGroupMemberships",
                autoboto.TypeInfo(typing.List[OptionGroupMembership]),
            ),
            (
                "character_set_name",
                "CharacterSetName",
                autoboto.TypeInfo(str),
            ),
            (
                "secondary_availability_zone",
                "SecondaryAvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                autoboto.TypeInfo(bool),
            ),
            (
                "status_infos",
                "StatusInfos",
                autoboto.TypeInfo(typing.List[DBInstanceStatusInfo]),
            ),
            (
                "storage_type",
                "StorageType",
                autoboto.TypeInfo(str),
            ),
            (
                "tde_credential_arn",
                "TdeCredentialArn",
                autoboto.TypeInfo(str),
            ),
            (
                "db_instance_port",
                "DbInstancePort",
                autoboto.TypeInfo(int),
            ),
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "storage_encrypted",
                "StorageEncrypted",
                autoboto.TypeInfo(bool),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "dbi_resource_id",
                "DbiResourceId",
                autoboto.TypeInfo(str),
            ),
            (
                "ca_certificate_identifier",
                "CACertificateIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "domain_memberships",
                "DomainMemberships",
                autoboto.TypeInfo(typing.List[DomainMembership]),
            ),
            (
                "copy_tags_to_snapshot",
                "CopyTagsToSnapshot",
                autoboto.TypeInfo(bool),
            ),
            (
                "monitoring_interval",
                "MonitoringInterval",
                autoboto.TypeInfo(int),
            ),
            (
                "enhanced_monitoring_resource_arn",
                "EnhancedMonitoringResourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "monitoring_role_arn",
                "MonitoringRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "promotion_tier",
                "PromotionTier",
                autoboto.TypeInfo(int),
            ),
            (
                "db_instance_arn",
                "DBInstanceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                autoboto.TypeInfo(str),
            ),
            (
                "iam_database_authentication_enabled",
                "IAMDatabaseAuthenticationEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "performance_insights_enabled",
                "PerformanceInsightsEnabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "performance_insights_kms_key_id",
                "PerformanceInsightsKMSKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "enabled_cloudwatch_logs_exports",
                "EnabledCloudwatchLogsExports",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # Contains a user-supplied database identifier. This identifier is the unique
    # key that identifies a DB instance.
    db_instance_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains the name of the compute and memory capacity class of the DB
    # instance.
    db_instance_class: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides the name of the database engine to be used for this DB instance.
    engine: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the current state of this database.
    db_instance_status: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains the master username for the DB instance.
    master_username: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The database name.
    db_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the connection endpoint.
    endpoint: "Endpoint" = dataclasses.field(default_factory=dict, )

    # Specifies the allocated storage size specified in gibibytes.
    allocated_storage: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides the date and time the DB instance was created.
    instance_create_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the daily time range during which automated backups are created
    # if automated backups are enabled, as determined by the
    # `BackupRetentionPeriod`.
    preferred_backup_window: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the number of days for which automatic DB snapshots are retained.
    backup_retention_period: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides List of DB security group elements containing only
    # `DBSecurityGroup.Name` and `DBSecurityGroup.Status` subelements.
    db_security_groups: typing.List["DBSecurityGroupMembership"
                                   ] = dataclasses.field(
                                       default_factory=list,
                                   )

    # Provides a list of VPC security group elements that the DB instance belongs
    # to.
    vpc_security_groups: typing.List["VpcSecurityGroupMembership"
                                    ] = dataclasses.field(
                                        default_factory=list,
                                    )

    # Provides the list of DB parameter groups applied to this DB instance.
    db_parameter_groups: typing.List["DBParameterGroupStatus"
                                    ] = dataclasses.field(
                                        default_factory=list,
                                    )

    # Specifies the name of the Availability Zone the DB instance is located in.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies information on the subnet group associated with the DB instance,
    # including the name, description, and subnets in the subnet group.
    db_subnet_group: "DBSubnetGroup" = dataclasses.field(default_factory=dict, )

    # Specifies the weekly time range during which system maintenance can occur,
    # in Universal Coordinated Time (UTC).
    preferred_maintenance_window: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies that changes to the DB instance are pending. This element is only
    # included when changes are pending. Specific changes are identified by
    # subelements.
    pending_modified_values: "PendingModifiedValues" = dataclasses.field(
        default_factory=dict,
    )

    # Specifies the latest time to which a database can be restored with point-
    # in-time restore.
    latest_restorable_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies if the DB instance is a Multi-AZ deployment.
    multi_az: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates the database engine version.
    engine_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates that minor version patches are applied automatically.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains the identifier of the source DB instance if this DB instance is a
    # Read Replica.
    read_replica_source_db_instance_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains one or more identifiers of the Read Replicas associated with this
    # DB instance.
    read_replica_db_instance_identifiers: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Contains one or more identifiers of DB clusters that are Read Replicas of
    # this DB instance.
    read_replica_db_cluster_identifiers: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # License model information for this DB instance.
    license_model: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the Provisioned IOPS (I/O operations per second) value.
    iops: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Provides the list of option group memberships for this DB instance.
    option_group_memberships: typing.List["OptionGroupMembership"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )

    # If present, specifies the name of the character set that this instance is
    # associated with.
    character_set_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If present, specifies the name of the secondary Availability Zone for a DB
    # instance with multi-AZ support.
    secondary_availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This parameter is not supported.
    publicly_accessible: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of a Read Replica. If the instance is not a Read Replica, this
    # is blank.
    status_infos: typing.List["DBInstanceStatusInfo"] = dataclasses.field(
        default_factory=list,
    )

    # Specifies the storage type associated with DB instance.
    storage_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN from the key store with which the instance is associated for TDE
    # encryption.
    tde_credential_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the port that the DB instance listens on. If the DB instance is
    # part of a DB cluster, this can be a different port than the DB cluster
    # port.
    db_instance_port: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If the DB instance is a member of a DB cluster, contains the name of the DB
    # cluster that the DB instance is a member of.
    db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether the DB instance is encrypted.
    storage_encrypted: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If `StorageEncrypted` is true, the AWS KMS key identifier for the encrypted
    # DB instance.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The AWS Region-unique, immutable identifier for the DB instance. This
    # identifier is found in AWS CloudTrail log entries whenever the AWS KMS key
    # for the DB instance is accessed.
    dbi_resource_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the CA certificate for this DB instance.
    ca_certificate_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Not supported
    domain_memberships: typing.List["DomainMembership"] = dataclasses.field(
        default_factory=list,
    )

    # Specifies whether tags are copied from the DB instance to snapshots of the
    # DB instance.
    copy_tags_to_snapshot: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The interval, in seconds, between points when Enhanced Monitoring metrics
    # are collected for the DB instance.
    monitoring_interval: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream
    # that receives the Enhanced Monitoring metrics data for the DB instance.
    enhanced_monitoring_resource_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN for the IAM role that permits Neptune to send Enhanced Monitoring
    # metrics to Amazon CloudWatch Logs.
    monitoring_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A value that specifies the order in which a Read Replica is promoted to the
    # primary instance after a failure of the existing primary instance.
    promotion_tier: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) for the DB instance.
    db_instance_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Not supported.
    timezone: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # True if AWS Identity and Access Management (IAM) authentication is enabled,
    # and otherwise false.
    iam_database_authentication_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # True if Performance Insights is enabled for the DB instance, and otherwise
    # false.
    performance_insights_enabled: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS KMS key identifier for encryption of Performance Insights data. The
    # KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the
    # KMS key alias for the KMS encryption key.
    performance_insights_kms_key_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of log types that this DB instance is configured to export to
    # CloudWatch Logs.
    enabled_cloudwatch_logs_exports: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DBInstanceAlreadyExistsFault(autoboto.ShapeBase):
    """
    User already has a DB instance with the given identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBInstanceMessage(autoboto.ShapeBase):
    """
    Contains the result of a successful invocation of the DescribeDBInstances
    action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "db_instances",
                "DBInstances",
                autoboto.TypeInfo(typing.List[DBInstance]),
            ),
        ]

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords` .
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of DBInstance instances.
    db_instances: typing.List["DBInstance"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DBInstanceNotFoundFault(autoboto.ShapeBase):
    """
    _DBInstanceIdentifier_ does not refer to an existing DB instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBInstanceStatusInfo(autoboto.ShapeBase):
    """
    Provides a list of status information for a DB instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status_type",
                "StatusType",
                autoboto.TypeInfo(str),
            ),
            (
                "normal",
                "Normal",
                autoboto.TypeInfo(bool),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # This value is currently "read replication."
    status_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Boolean value that is true if the instance is operating normally, or false
    # if the instance is in an error state.
    normal: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Status of the DB instance. For a StatusType of read replica, the values can
    # be replicating, error, stopped, or terminated.
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Details of the error if there is an error for the instance. If the instance
    # is not in an error state, this value is blank.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBParameterGroup(autoboto.ShapeBase):
    """
    Contains the details of an Amazon Neptune DB parameter group.

    This data type is used as a response element in the DescribeDBParameterGroups
    action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "db_parameter_group_family",
                "DBParameterGroupFamily",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "db_parameter_group_arn",
                "DBParameterGroupArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # Provides the name of the DB parameter group.
    db_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides the name of the DB parameter group family that this DB parameter
    # group is compatible with.
    db_parameter_group_family: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides the customer-specified description for this DB parameter group.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the DB parameter group.
    db_parameter_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBParameterGroupAlreadyExistsFault(autoboto.ShapeBase):
    """
    A DB parameter group with the same name exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBParameterGroupDetails(autoboto.ShapeBase):
    """
    Contains the result of a successful invocation of the DescribeDBParameters
    action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.List[Parameter]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of Parameter values.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default_factory=list,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBParameterGroupNameMessage(autoboto.ShapeBase):
    """
    Contains the result of a successful invocation of the ModifyDBParameterGroup or
    ResetDBParameterGroup action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Provides the name of the DB parameter group.
    db_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBParameterGroupNotFoundFault(autoboto.ShapeBase):
    """
    _DBParameterGroupName_ does not refer to an existing DB parameter group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBParameterGroupQuotaExceededFault(autoboto.ShapeBase):
    """
    Request would result in user exceeding the allowed number of DB parameter
    groups.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBParameterGroupStatus(autoboto.ShapeBase):
    """
    The status of the DB parameter group.

    This data type is used as a response element in the following actions:

      * CreateDBInstance

      * DeleteDBInstance

      * ModifyDBInstance

      * RebootDBInstance
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_apply_status",
                "ParameterApplyStatus",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the DP parameter group.
    db_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of parameter updates.
    parameter_apply_status: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBParameterGroupsMessage(autoboto.ShapeBase):
    """
    Contains the result of a successful invocation of the DescribeDBParameterGroups
    action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "db_parameter_groups",
                "DBParameterGroups",
                autoboto.TypeInfo(typing.List[DBParameterGroup]),
            ),
        ]

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of DBParameterGroup instances.
    db_parameter_groups: typing.List["DBParameterGroup"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DBSecurityGroupMembership(autoboto.ShapeBase):
    """
    This data type is used as a response element in the following actions:

      * ModifyDBInstance

      * RebootDBInstance
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_security_group_name",
                "DBSecurityGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the DB security group.
    db_security_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the DB security group.
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBSecurityGroupNotFoundFault(autoboto.ShapeBase):
    """
    _DBSecurityGroupName_ does not refer to an existing DB security group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSnapshotAlreadyExistsFault(autoboto.ShapeBase):
    """
    _DBSnapshotIdentifier_ is already used by an existing snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSnapshotNotFoundFault(autoboto.ShapeBase):
    """
    _DBSnapshotIdentifier_ does not refer to an existing DB snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSubnetGroup(autoboto.ShapeBase):
    """
    Contains the details of an Amazon Neptune DB subnet group.

    This data type is used as a response element in the DescribeDBSubnetGroups
    action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "db_subnet_group_description",
                "DBSubnetGroupDescription",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_group_status",
                "SubnetGroupStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "subnets",
                "Subnets",
                autoboto.TypeInfo(typing.List[Subnet]),
            ),
            (
                "db_subnet_group_arn",
                "DBSubnetGroupArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the DB subnet group.
    db_subnet_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides the description of the DB subnet group.
    db_subnet_group_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides the VpcId of the DB subnet group.
    vpc_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Provides the status of the DB subnet group.
    subnet_group_status: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains a list of Subnet elements.
    subnets: typing.List["Subnet"] = dataclasses.field(default_factory=list, )

    # The Amazon Resource Name (ARN) for the DB subnet group.
    db_subnet_group_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBSubnetGroupAlreadyExistsFault(autoboto.ShapeBase):
    """
    _DBSubnetGroupName_ is already used by an existing DB subnet group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSubnetGroupDoesNotCoverEnoughAZs(autoboto.ShapeBase):
    """
    Subnets in the DB subnet group should cover at least two Availability Zones
    unless there is only one Availability Zone.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSubnetGroupMessage(autoboto.ShapeBase):
    """
    Contains the result of a successful invocation of the DescribeDBSubnetGroups
    action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "db_subnet_groups",
                "DBSubnetGroups",
                autoboto.TypeInfo(typing.List[DBSubnetGroup]),
            ),
        ]

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of DBSubnetGroup instances.
    db_subnet_groups: typing.List["DBSubnetGroup"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DBSubnetGroupNotFoundFault(autoboto.ShapeBase):
    """
    _DBSubnetGroupName_ does not refer to an existing DB subnet group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSubnetGroupQuotaExceededFault(autoboto.ShapeBase):
    """
    Request would result in user exceeding the allowed number of DB subnet groups.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSubnetQuotaExceededFault(autoboto.ShapeBase):
    """
    Request would result in user exceeding the allowed number of subnets in a DB
    subnet groups.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBUpgradeDependencyFailureFault(autoboto.ShapeBase):
    """
    The DB upgrade failed because a resource the DB depends on could not be
    modified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteDBClusterMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "skip_final_snapshot",
                "SkipFinalSnapshot",
                autoboto.TypeInfo(bool),
            ),
            (
                "final_db_snapshot_identifier",
                "FinalDBSnapshotIdentifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # The DB cluster identifier for the DB cluster to be deleted. This parameter
    # isn't case-sensitive.

    # Constraints:

    #   * Must match an existing DBClusterIdentifier.
    db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Determines whether a final DB cluster snapshot is created before the DB
    # cluster is deleted. If `true` is specified, no DB cluster snapshot is
    # created. If `false` is specified, a DB cluster snapshot is created before
    # the DB cluster is deleted.

    # You must specify a `FinalDBSnapshotIdentifier` parameter if
    # `SkipFinalSnapshot` is `false`.

    # Default: `false`
    skip_final_snapshot: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The DB cluster snapshot identifier of the new DB cluster snapshot created
    # when `SkipFinalSnapshot` is set to `false`.

    # Specifying this parameter and also setting the `SkipFinalShapshot`
    # parameter to true results in an error.

    # Constraints:

    #   * Must be 1 to 255 letters, numbers, or hyphens.

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens
    final_db_snapshot_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDBClusterParameterGroupMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the DB cluster parameter group.

    # Constraints:

    #   * Must be the name of an existing DB cluster parameter group.

    #   * You can't delete a default DB cluster parameter group.

    #   * Cannot be associated with any DB clusters.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDBClusterResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster",
                "DBCluster",
                autoboto.TypeInfo(DBCluster),
            ),
        ]

    # Contains the details of an Amazon Neptune DB cluster.

    # This data type is used as a response element in the DescribeDBClusters
    # action.
    db_cluster: "DBCluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteDBClusterSnapshotMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_snapshot_identifier",
                "DBClusterSnapshotIdentifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier of the DB cluster snapshot to delete.

    # Constraints: Must be the name of an existing DB cluster snapshot in the
    # `available` state.
    db_cluster_snapshot_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDBClusterSnapshotResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_snapshot",
                "DBClusterSnapshot",
                autoboto.TypeInfo(DBClusterSnapshot),
            ),
        ]

    # Contains the details for an Amazon Neptune DB cluster snapshot

    # This data type is used as a response element in the
    # DescribeDBClusterSnapshots action.
    db_cluster_snapshot: "DBClusterSnapshot" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DeleteDBInstanceMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "skip_final_snapshot",
                "SkipFinalSnapshot",
                autoboto.TypeInfo(bool),
            ),
            (
                "final_db_snapshot_identifier",
                "FinalDBSnapshotIdentifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # The DB instance identifier for the DB instance to be deleted. This
    # parameter isn't case-sensitive.

    # Constraints:

    #   * Must match the name of an existing DB instance.
    db_instance_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Determines whether a final DB snapshot is created before the DB instance is
    # deleted. If `true` is specified, no DBSnapshot is created. If `false` is
    # specified, a DB snapshot is created before the DB instance is deleted.

    # Note that when a DB instance is in a failure state and has a status of
    # 'failed', 'incompatible-restore', or 'incompatible-network', it can only be
    # deleted when the SkipFinalSnapshot parameter is set to "true".

    # Specify `true` when deleting a Read Replica.

    # The FinalDBSnapshotIdentifier parameter must be specified if
    # SkipFinalSnapshot is `false`.

    # Default: `false`
    skip_final_snapshot: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The DBSnapshotIdentifier of the new DBSnapshot created when
    # SkipFinalSnapshot is set to `false`.

    # Specifying this parameter and also setting the SkipFinalShapshot parameter
    # to true results in an error.

    # Constraints:

    #   * Must be 1 to 255 letters or numbers.

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    #   * Cannot be specified when deleting a Read Replica.
    final_db_snapshot_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDBInstanceResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance",
                "DBInstance",
                autoboto.TypeInfo(DBInstance),
            ),
        ]

    # Contains the details of an Amazon Neptune DB instance.

    # This data type is used as a response element in the DescribeDBInstances
    # action.
    db_instance: "DBInstance" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteDBParameterGroupMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the DB parameter group.

    # Constraints:

    #   * Must be the name of an existing DB parameter group

    #   * You can't delete a default DB parameter group

    #   * Cannot be associated with any DB instances
    db_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDBSubnetGroupMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the database subnet group to delete.

    # You can't delete the default subnet group.

    # Constraints:

    # Constraints: Must match the name of an existing DBSubnetGroup. Must not be
    # default.

    # Example: `mySubnetgroup`
    db_subnet_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteEventSubscriptionMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_name",
                "SubscriptionName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the event notification subscription you want to delete.
    subscription_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteEventSubscriptionResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_subscription",
                "EventSubscription",
                autoboto.TypeInfo(EventSubscription),
            ),
        ]

    # Contains the results of a successful invocation of the
    # DescribeEventSubscriptions action.
    event_subscription: "EventSubscription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeDBClusterParameterGroupsMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "max_records",
                "MaxRecords",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of a specific DB cluster parameter group to return details for.

    # Constraints:

    #   * If supplied, must match the name of an existing DBClusterParameterGroup.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # `DescribeDBClusterParameterGroups` request. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBClusterParametersMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "source",
                "Source",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "max_records",
                "MaxRecords",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of a specific DB cluster parameter group to return parameter
    # details for.

    # Constraints:

    #   * If supplied, must match the name of an existing DBClusterParameterGroup.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A value that indicates to return only parameters for a specific source.
    # Parameter sources can be `engine`, `service`, or `customer`.
    source: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # `DescribeDBClusterParameters` request. If this parameter is specified, the
    # response includes only records beyond the marker, up to the value specified
    # by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBClusterSnapshotAttributesMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_snapshot_identifier",
                "DBClusterSnapshotIdentifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier for the DB cluster snapshot to describe the attributes for.
    db_cluster_snapshot_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeDBClusterSnapshotAttributesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_snapshot_attributes_result",
                "DBClusterSnapshotAttributesResult",
                autoboto.TypeInfo(DBClusterSnapshotAttributesResult),
            ),
        ]

    # Contains the results of a successful call to the
    # DescribeDBClusterSnapshotAttributes API action.

    # Manual DB cluster snapshot attributes are used to authorize other AWS
    # accounts to copy or restore a manual DB cluster snapshot. For more
    # information, see the ModifyDBClusterSnapshotAttribute API action.
    db_cluster_snapshot_attributes_result: "DBClusterSnapshotAttributesResult" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeDBClusterSnapshotsMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "db_cluster_snapshot_identifier",
                "DBClusterSnapshotIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "snapshot_type",
                "SnapshotType",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "max_records",
                "MaxRecords",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "include_shared",
                "IncludeShared",
                autoboto.TypeInfo(bool),
            ),
            (
                "include_public",
                "IncludePublic",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The ID of the DB cluster to retrieve the list of DB cluster snapshots for.
    # This parameter can't be used in conjunction with the
    # `DBClusterSnapshotIdentifier` parameter. This parameter is not case-
    # sensitive.

    # Constraints:

    #   * If supplied, must match the identifier of an existing DBCluster.
    db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A specific DB cluster snapshot identifier to describe. This parameter can't
    # be used in conjunction with the `DBClusterIdentifier` parameter. This value
    # is stored as a lowercase string.

    # Constraints:

    #   * If supplied, must match the identifier of an existing DBClusterSnapshot.

    #   * If this identifier is for an automated snapshot, the `SnapshotType` parameter must also be specified.
    db_cluster_snapshot_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of DB cluster snapshots to be returned. You can specify one of the
    # following values:

    #   * `automated` \- Return all DB cluster snapshots that have been automatically taken by Amazon Neptune for my AWS account.

    #   * `manual` \- Return all DB cluster snapshots that have been taken by my AWS account.

    #   * `shared` \- Return all manual DB cluster snapshots that have been shared to my AWS account.

    #   * `public` \- Return all DB cluster snapshots that have been marked as public.

    # If you don't specify a `SnapshotType` value, then both automated and manual
    # DB cluster snapshots are returned. You can include shared DB cluster
    # snapshots with these results by setting the `IncludeShared` parameter to
    # `true`. You can include public DB cluster snapshots with these results by
    # setting the `IncludePublic` parameter to `true`.

    # The `IncludeShared` and `IncludePublic` parameters don't apply for
    # `SnapshotType` values of `manual` or `automated`. The `IncludePublic`
    # parameter doesn't apply when `SnapshotType` is set to `shared`. The
    # `IncludeShared` parameter doesn't apply when `SnapshotType` is set to
    # `public`.
    snapshot_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # `DescribeDBClusterSnapshots` request. If this parameter is specified, the
    # response includes only records beyond the marker, up to the value specified
    # by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # True to include shared manual DB cluster snapshots from other AWS accounts
    # that this AWS account has been given permission to copy or restore, and
    # otherwise false. The default is `false`.

    # You can give an AWS account permission to restore a manual DB cluster
    # snapshot from another AWS account by the ModifyDBClusterSnapshotAttribute
    # API action.
    include_shared: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # True to include manual DB cluster snapshots that are public and can be
    # copied or restored by any AWS account, and otherwise false. The default is
    # `false`. The default is false.

    # You can share a manual DB cluster snapshot as public by using the
    # ModifyDBClusterSnapshotAttribute API action.
    include_public: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeDBClustersMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "max_records",
                "MaxRecords",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user-supplied DB cluster identifier. If this parameter is specified,
    # information from only the specific DB cluster is returned. This parameter
    # isn't case-sensitive.

    # Constraints:

    #   * If supplied, must match an existing DBClusterIdentifier.
    db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that specifies one or more DB clusters to describe.

    # Supported filters:

    #   * `db-cluster-id` \- Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB clusters identified by these ARNs.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous DescribeDBClusters
    # request. If this parameter is specified, the response includes only records
    # beyond the marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBEngineVersionsMessage(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "engine",
                "Engine",
                autoboto.TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "db_parameter_group_family",
                "DBParameterGroupFamily",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "max_records",
                "MaxRecords",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "default_only",
                "DefaultOnly",
                autoboto.TypeInfo(bool),
            ),
            (
                "list_supported_character_sets",
                "ListSupportedCharacterSets",
                autoboto.TypeInfo(bool),
            ),
            (
                "list_supported_timezones",
                "ListSupportedTimezones",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The database engine to return.
    engine: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The database engine version to return.

    # Example: `5.1.49`
    engine_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of a specific DB parameter group family to return details for.

    # Constraints:

    #   * If supplied, must match an existing DBParameterGroupFamily.
    db_parameter_group_family: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The maximum number of records to include in the response. If more than the
    # `MaxRecords` value is available, a pagination token called a marker is
    # included in the response so that the following results can be retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates that only the default version of the specified engine or engine
    # and major version combination is returned.
    default_only: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # If this parameter is specified and the requested engine supports the
    # `CharacterSetName` parameter for `CreateDBInstance`, the response includes
    # a list of supported character sets for each engine version.
    list_supported_character_sets: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If this parameter is specified and the requested engine supports the
    # `TimeZone` parameter for `CreateDBInstance`, the response includes a list
    # of supported time zones for each engine version.
    list_supported_timezones: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeDBInstancesMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "max_records",
                "MaxRecords",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user-supplied instance identifier. If this parameter is specified,
    # information from only the specific DB instance is returned. This parameter
    # isn't case-sensitive.

    # Constraints:

    #   * If supplied, must match the identifier of an existing DBInstance.
    db_instance_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that specifies one or more DB instances to describe.

    # Supported filters:

    #   * `db-cluster-id` \- Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB instances associated with the DB clusters identified by these ARNs.

    #   * `db-instance-id` \- Accepts DB instance identifiers and DB instance Amazon Resource Names (ARNs). The results list will only include information about the DB instances identified by these ARNs.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous `DescribeDBInstances`
    # request. If this parameter is specified, the response includes only records
    # beyond the marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBParameterGroupsMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "max_records",
                "MaxRecords",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of a specific DB parameter group to return details for.

    # Constraints:

    #   * If supplied, must match the name of an existing DBClusterParameterGroup.
    db_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # `DescribeDBParameterGroups` request. If this parameter is specified, the
    # response includes only records beyond the marker, up to the value specified
    # by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBParametersMessage(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "source",
                "Source",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "max_records",
                "MaxRecords",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of a specific DB parameter group to return details for.

    # Constraints:

    #   * If supplied, must match the name of an existing DBParameterGroup.
    db_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The parameter types to return.

    # Default: All parameter types returned

    # Valid Values: `user | system | engine-default`
    source: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous `DescribeDBParameters`
    # request. If this parameter is specified, the response includes only records
    # beyond the marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBSubnetGroupsMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "max_records",
                "MaxRecords",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the DB subnet group to return details for.
    db_subnet_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous DescribeDBSubnetGroups
    # request. If this parameter is specified, the response includes only records
    # beyond the marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEngineDefaultClusterParametersMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_family",
                "DBParameterGroupFamily",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "max_records",
                "MaxRecords",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the DB cluster parameter group family to return engine
    # parameter information for.
    db_parameter_group_family: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # `DescribeEngineDefaultClusterParameters` request. If this parameter is
    # specified, the response includes only records beyond the marker, up to the
    # value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEngineDefaultClusterParametersResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "engine_defaults",
                "EngineDefaults",
                autoboto.TypeInfo(EngineDefaults),
            ),
        ]

    # Contains the result of a successful invocation of the
    # DescribeEngineDefaultParameters action.
    engine_defaults: "EngineDefaults" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeEngineDefaultParametersMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_family",
                "DBParameterGroupFamily",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "max_records",
                "MaxRecords",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the DB parameter group family.
    db_parameter_group_family: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # `DescribeEngineDefaultParameters` request. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEngineDefaultParametersResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "engine_defaults",
                "EngineDefaults",
                autoboto.TypeInfo(EngineDefaults),
            ),
        ]

    # Contains the result of a successful invocation of the
    # DescribeEngineDefaultParameters action.
    engine_defaults: "EngineDefaults" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DescribeEventCategoriesMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_type",
                "SourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
        ]

    # The type of source that is generating the events.

    # Valid values: db-instance | db-parameter-group | db-security-group | db-
    # snapshot
    source_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeEventSubscriptionsMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_name",
                "SubscriptionName",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "max_records",
                "MaxRecords",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the event notification subscription you want to describe.
    subscription_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # DescribeOrderableDBInstanceOptions request. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords` .
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEventsMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_identifier",
                "SourceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "source_type",
                "SourceType",
                autoboto.TypeInfo(SourceType),
            ),
            (
                "start_time",
                "StartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "duration",
                "Duration",
                autoboto.TypeInfo(int),
            ),
            (
                "event_categories",
                "EventCategories",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "max_records",
                "MaxRecords",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier of the event source for which events are returned. If not
    # specified, then all sources are included in the response.

    # Constraints:

    #   * If SourceIdentifier is supplied, SourceType must also be provided.

    #   * If the source type is `DBInstance`, then a `DBInstanceIdentifier` must be supplied.

    #   * If the source type is `DBSecurityGroup`, a `DBSecurityGroupName` must be supplied.

    #   * If the source type is `DBParameterGroup`, a `DBParameterGroupName` must be supplied.

    #   * If the source type is `DBSnapshot`, a `DBSnapshotIdentifier` must be supplied.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.
    source_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The event source to retrieve events for. If no value is specified, all
    # events are returned.
    source_type: "SourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The beginning of the time interval to retrieve events for, specified in ISO
    # 8601 format. For more information about ISO 8601, go to the [ISO8601
    # Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)

    # Example: 2009-07-08T18:00Z
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The end of the time interval for which to retrieve events, specified in ISO
    # 8601 format. For more information about ISO 8601, go to the [ISO8601
    # Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)

    # Example: 2009-07-08T18:00Z
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of minutes to retrieve events for.

    # Default: 60
    duration: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of event categories that trigger notifications for a event
    # notification subscription.
    event_categories: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous DescribeEvents request.
    # If this parameter is specified, the response includes only records beyond
    # the marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeOrderableDBInstanceOptionsMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "engine",
                "Engine",
                autoboto.TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "db_instance_class",
                "DBInstanceClass",
                autoboto.TypeInfo(str),
            ),
            (
                "license_model",
                "LicenseModel",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc",
                "Vpc",
                autoboto.TypeInfo(bool),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "max_records",
                "MaxRecords",
                autoboto.TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the engine to retrieve DB instance options for.
    engine: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The engine version filter value. Specify this parameter to show only the
    # available offerings matching the specified engine version.
    engine_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The DB instance class filter value. Specify this parameter to show only the
    # available offerings matching the specified DB instance class.
    db_instance_class: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The license model filter value. Specify this parameter to show only the
    # available offerings matching the specified license model.
    license_model: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The VPC filter value. Specify this parameter to show only the available VPC
    # or non-VPC offerings.
    vpc: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # DescribeOrderableDBInstanceOptions request. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords` .
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePendingMaintenanceActionsMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_identifier",
                "ResourceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ARN of a resource to return pending maintenance actions for.
    resource_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A filter that specifies one or more resources to return pending maintenance
    # actions for.

    # Supported filters:

    #   * `db-cluster-id` \- Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include pending maintenance actions for the DB clusters identified by these ARNs.

    #   * `db-instance-id` \- Accepts DB instance identifiers and DB instance ARNs. The results list will only include pending maintenance actions for the DB instances identified by these ARNs.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )

    # An optional pagination token provided by a previous
    # `DescribePendingMaintenanceActions` request. If this parameter is
    # specified, the response includes only records beyond the marker, up to a
    # number of records specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeValidDBInstanceModificationsMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # The customer identifier or the ARN of your DB instance.
    db_instance_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeValidDBInstanceModificationsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "valid_db_instance_modifications_message",
                "ValidDBInstanceModificationsMessage",
                autoboto.TypeInfo(ValidDBInstanceModificationsMessage),
            ),
        ]

    # Information about valid modifications that you can make to your DB
    # instance. Contains the result of a successful call to the
    # DescribeValidDBInstanceModifications action. You can use this information
    # when you call ModifyDBInstance.
    valid_db_instance_modifications_message: "ValidDBInstanceModificationsMessage" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class DomainMembership(autoboto.ShapeBase):
    """
    An Active Directory Domain membership record associated with the DB instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "Domain",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
            (
                "fqdn",
                "FQDN",
                autoboto.TypeInfo(str),
            ),
            (
                "iam_role_name",
                "IAMRoleName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier of the Active Directory Domain.
    domain: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the DB instance's Active Directory Domain membership, such as
    # joined, pending-join, failed etc).
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The fully qualified domain name of the Active Directory Domain.
    fqdn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the IAM role to be used when making API calls to the Directory
    # Service.
    iam_role_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DomainNotFoundFault(autoboto.ShapeBase):
    """
    _Domain_ does not refer to an existing Active Directory Domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DoubleRange(autoboto.ShapeBase):
    """
    A range of double values.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "from_",
                "From",
                autoboto.TypeInfo(float),
            ),
            (
                "to",
                "To",
                autoboto.TypeInfo(float),
            ),
        ]

    # The minimum value in the range.
    from_: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum value in the range.
    to: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Endpoint(autoboto.ShapeBase):
    """
    This data type is used as a response element in the following actions:

      * CreateDBInstance

      * DescribeDBInstances

      * DeleteDBInstance
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address",
                "Address",
                autoboto.TypeInfo(str),
            ),
            (
                "port",
                "Port",
                autoboto.TypeInfo(int),
            ),
            (
                "hosted_zone_id",
                "HostedZoneId",
                autoboto.TypeInfo(str),
            ),
        ]

    # Specifies the DNS address of the DB instance.
    address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the port that the database engine is listening on.
    port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the ID that Amazon Route 53 assigns when you create a hosted
    # zone.
    hosted_zone_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EngineDefaults(autoboto.ShapeBase):
    """
    Contains the result of a successful invocation of the
    DescribeEngineDefaultParameters action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_family",
                "DBParameterGroupFamily",
                autoboto.TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.List[Parameter]),
            ),
        ]

    # Specifies the name of the DB parameter group family that the engine default
    # parameters apply to.
    db_parameter_group_family: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous EngineDefaults request.
    # If this parameter is specified, the response includes only records beyond
    # the marker, up to the value specified by `MaxRecords` .
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Contains a list of engine default parameters.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Event(autoboto.ShapeBase):
    """
    This data type is used as a response element in the DescribeEvents action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_identifier",
                "SourceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "source_type",
                "SourceType",
                autoboto.TypeInfo(SourceType),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
            (
                "event_categories",
                "EventCategories",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "date",
                "Date",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "source_arn",
                "SourceArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # Provides the identifier for the source of the event.
    source_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the source type for this event.
    source_type: "SourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides the text of this event.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the category for the event.
    event_categories: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Specifies the date and time of the event.
    date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) for the event.
    source_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventCategoriesMap(autoboto.ShapeBase):
    """
    Contains the results of a successful invocation of the DescribeEventCategories
    action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_type",
                "SourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "event_categories",
                "EventCategories",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The source type that the returned categories belong to
    source_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The event categories for the specified source type
    event_categories: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class EventCategoriesMessage(autoboto.ShapeBase):
    """
    Data returned from the **DescribeEventCategories** action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_categories_map_list",
                "EventCategoriesMapList",
                autoboto.TypeInfo(typing.List[EventCategoriesMap]),
            ),
        ]

    # A list of EventCategoriesMap data types.
    event_categories_map_list: typing.List["EventCategoriesMap"
                                          ] = dataclasses.field(
                                              default_factory=list,
                                          )


@dataclasses.dataclass
class EventSubscription(autoboto.ShapeBase):
    """
    Contains the results of a successful invocation of the
    DescribeEventSubscriptions action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "customer_aws_id",
                "CustomerAwsId",
                autoboto.TypeInfo(str),
            ),
            (
                "cust_subscription_id",
                "CustSubscriptionId",
                autoboto.TypeInfo(str),
            ),
            (
                "sns_topic_arn",
                "SnsTopicArn",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
            (
                "subscription_creation_time",
                "SubscriptionCreationTime",
                autoboto.TypeInfo(str),
            ),
            (
                "source_type",
                "SourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "source_ids_list",
                "SourceIdsList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "event_categories_list",
                "EventCategoriesList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
            (
                "event_subscription_arn",
                "EventSubscriptionArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The AWS customer account associated with the event notification
    # subscription.
    customer_aws_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The event notification subscription Id.
    cust_subscription_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The topic ARN of the event notification subscription.
    sns_topic_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the event notification subscription.

    # Constraints:

    # Can be one of the following: creating | modifying | deleting | active | no-
    # permission | topic-not-exist

    # The status "no-permission" indicates that Neptune no longer has permission
    # to post to the SNS topic. The status "topic-not-exist" indicates that the
    # topic was deleted after the subscription was created.
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time the event notification subscription was created.
    subscription_creation_time: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The source type for the event notification subscription.
    source_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of source IDs for the event notification subscription.
    source_ids_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list of event categories for the event notification subscription.
    event_categories_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A Boolean value indicating if the subscription is enabled. True indicates
    # the subscription is enabled.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the event subscription.
    event_subscription_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EventSubscriptionQuotaExceededFault(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EventSubscriptionsMessage(autoboto.ShapeBase):
    """
    Data returned by the **DescribeEventSubscriptions** action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "event_subscriptions_list",
                "EventSubscriptionsList",
                autoboto.TypeInfo(typing.List[EventSubscription]),
            ),
        ]

    # An optional pagination token provided by a previous
    # DescribeOrderableDBInstanceOptions request. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of EventSubscriptions data types.
    event_subscriptions_list: typing.List["EventSubscription"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )


@dataclasses.dataclass
class EventsMessage(autoboto.ShapeBase):
    """
    Contains the result of a successful invocation of the DescribeEvents action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
            (
                "events",
                "Events",
                autoboto.TypeInfo(typing.List[Event]),
            ),
        ]

    # An optional pagination token provided by a previous Events request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords` .
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of Event instances.
    events: typing.List["Event"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class FailoverDBClusterMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "target_db_instance_identifier",
                "TargetDBInstanceIdentifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # A DB cluster identifier to force a failover for. This parameter is not
    # case-sensitive.

    # Constraints:

    #   * Must match the identifier of an existing DBCluster.
    db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the instance to promote to the primary instance.

    # You must specify the instance identifier for an Read Replica in the DB
    # cluster. For example, `mydbcluster-replica1`.
    target_db_instance_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FailoverDBClusterResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster",
                "DBCluster",
                autoboto.TypeInfo(DBCluster),
            ),
        ]

    # Contains the details of an Amazon Neptune DB cluster.

    # This data type is used as a response element in the DescribeDBClusters
    # action.
    db_cluster: "DBCluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class Filter(autoboto.ShapeBase):
    """
    This type is not currently supported.
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
                "values",
                "Values",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # This parameter is not currently supported.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class InstanceQuotaExceededFault(autoboto.ShapeBase):
    """
    Request would result in user exceeding the allowed number of DB instances.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InsufficientDBClusterCapacityFault(autoboto.ShapeBase):
    """
    The DB cluster does not have enough capacity for the current operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InsufficientDBInstanceCapacityFault(autoboto.ShapeBase):
    """
    Specified DB instance class is not available in the specified Availability Zone.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InsufficientStorageClusterCapacityFault(autoboto.ShapeBase):
    """
    There is insufficient storage available for the current action. You may be able
    to resolve this error by updating your subnet group to use different
    Availability Zones that have more storage available.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBClusterSnapshotStateFault(autoboto.ShapeBase):
    """
    The supplied value is not a valid DB cluster snapshot state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBClusterStateFault(autoboto.ShapeBase):
    """
    The DB cluster is not in a valid state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBInstanceStateFault(autoboto.ShapeBase):
    """
    The specified DB instance is not in the _available_ state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBParameterGroupStateFault(autoboto.ShapeBase):
    """
    The DB parameter group is in use or is in an invalid state. If you are
    attempting to delete the parameter group, you cannot delete it when the
    parameter group is in this state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBSecurityGroupStateFault(autoboto.ShapeBase):
    """
    The state of the DB security group does not allow deletion.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBSnapshotStateFault(autoboto.ShapeBase):
    """
    The state of the DB snapshot does not allow deletion.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBSubnetGroupStateFault(autoboto.ShapeBase):
    """
    The DB subnet group cannot be deleted because it is in use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBSubnetStateFault(autoboto.ShapeBase):
    """
    The DB subnet is not in the _available_ state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidEventSubscriptionStateFault(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRestoreFault(autoboto.ShapeBase):
    """
    Cannot restore from vpc backup to non-vpc DB instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSubnet(autoboto.ShapeBase):
    """
    The requested subnet is invalid, or multiple subnets were requested that are not
    all in a common VPC.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidVPCNetworkStateFault(autoboto.ShapeBase):
    """
    DB subnet group does not cover all Availability Zones after it is created
    because users' change.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class KMSKeyNotAccessibleFault(autoboto.ShapeBase):
    """
    Error accessing KMS key.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListTagsForResourceMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_name",
                "ResourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                autoboto.TypeInfo(typing.List[Filter]),
            ),
        ]

    # The Amazon Neptune resource with tags to be listed. This value is an Amazon
    # Resource Name (ARN). For information about creating an ARN, see [
    # Constructing an Amazon Resource Name
    # (ARN)](http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing).
    resource_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class ModifyDBClusterMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "new_db_cluster_identifier",
                "NewDBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "apply_immediately",
                "ApplyImmediately",
                autoboto.TypeInfo(bool),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                autoboto.TypeInfo(int),
            ),
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "port",
                "Port",
                autoboto.TypeInfo(int),
            ),
            (
                "master_user_password",
                "MasterUserPassword",
                autoboto.TypeInfo(str),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                autoboto.TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                autoboto.TypeInfo(str),
            ),
            (
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                autoboto.TypeInfo(bool),
            ),
            (
                "engine_version",
                "EngineVersion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The DB cluster identifier for the cluster being modified. This parameter is
    # not case-sensitive.

    # Constraints:

    #   * Must match the identifier of an existing DBCluster.
    db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The new DB cluster identifier for the DB cluster when renaming a DB
    # cluster. This value is stored as a lowercase string.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens

    #   * The first character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # Example: `my-cluster2`
    new_db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A value that specifies whether the modifications in this request and any
    # pending modifications are asynchronously applied as soon as possible,
    # regardless of the `PreferredMaintenanceWindow` setting for the DB cluster.
    # If this parameter is set to `false`, changes to the DB cluster are applied
    # during the next maintenance window.

    # The `ApplyImmediately` parameter only affects the `NewDBClusterIdentifier`
    # and `MasterUserPassword` values. If you set the `ApplyImmediately`
    # parameter value to false, then changes to the `NewDBClusterIdentifier` and
    # `MasterUserPassword` values are applied during the next maintenance window.
    # All other changes are applied immediately, regardless of the value of the
    # `ApplyImmediately` parameter.

    # Default: `false`
    apply_immediately: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of days for which automated backups are retained. You must
    # specify a minimum value of 1.

    # Default: 1

    # Constraints:

    #   * Must be a value from 1 to 35
    backup_retention_period: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the DB cluster parameter group to use for the DB cluster.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of VPC security groups that the DB cluster will belong to.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The port number on which the DB cluster accepts connections.

    # Constraints: Value must be `1150-65535`

    # Default: The same port as the original DB cluster.
    port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The new password for the master database user. This password can contain
    # any printable ASCII character except "/", """, or "@".

    # Constraints: Must contain from 8 to 41 characters.
    master_user_password: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A value that indicates that the DB cluster should be associated with the
    # specified option group. Changing this parameter doesn't result in an outage
    # except in the following case, and the change is applied during the next
    # maintenance window unless the `ApplyImmediately` parameter is set to `true`
    # for this request. If the parameter change results in an option group that
    # enables OEM, this change can cause a brief (sub-second) period during which
    # new connections are rejected but existing connections are not interrupted.

    # Permanent options can't be removed from an option group. The option group
    # can't be removed from a DB cluster once it is associated with a DB cluster.
    option_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The daily time range during which automated backups are created if
    # automated backups are enabled, using the `BackupRetentionPeriod` parameter.

    # The default is a 30-minute window selected at random from an 8-hour block
    # of time for each AWS Region.

    # Constraints:

    #   * Must be in the format `hh24:mi-hh24:mi`.

    #   * Must be in Universal Coordinated Time (UTC).

    #   * Must not conflict with the preferred maintenance window.

    #   * Must be at least 30 minutes.
    preferred_backup_window: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The weekly time range during which system maintenance can occur, in
    # Universal Coordinated Time (UTC).

    # Format: `ddd:hh24:mi-ddd:hh24:mi`

    # The default is a 30-minute window selected at random from an 8-hour block
    # of time for each AWS Region, occurring on a random day of the week.

    # Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.

    # Constraints: Minimum 30-minute window.
    preferred_maintenance_window: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # True to enable mapping of AWS Identity and Access Management (IAM) accounts
    # to database accounts, and otherwise false.

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The version number of the database engine to which you want to upgrade.
    # Changing this parameter results in an outage. The change is applied during
    # the next maintenance window unless the ApplyImmediately parameter is set to
    # true.

    # For a list of valid engine versions, see CreateDBInstance, or call
    # DescribeDBEngineVersions.
    engine_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyDBClusterParameterGroupMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.List[Parameter]),
            ),
        ]

    # The name of the DB cluster parameter group to modify.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of parameters in the DB cluster parameter group to modify.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ModifyDBClusterResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster",
                "DBCluster",
                autoboto.TypeInfo(DBCluster),
            ),
        ]

    # Contains the details of an Amazon Neptune DB cluster.

    # This data type is used as a response element in the DescribeDBClusters
    # action.
    db_cluster: "DBCluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ModifyDBClusterSnapshotAttributeMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_snapshot_identifier",
                "DBClusterSnapshotIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "attribute_name",
                "AttributeName",
                autoboto.TypeInfo(str),
            ),
            (
                "values_to_add",
                "ValuesToAdd",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "values_to_remove",
                "ValuesToRemove",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The identifier for the DB cluster snapshot to modify the attributes for.
    db_cluster_snapshot_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the DB cluster snapshot attribute to modify.

    # To manage authorization for other AWS accounts to copy or restore a manual
    # DB cluster snapshot, set this value to `restore`.
    attribute_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of DB cluster snapshot attributes to add to the attribute specified
    # by `AttributeName`.

    # To authorize other AWS accounts to copy or restore a manual DB cluster
    # snapshot, set this list to include one or more AWS account IDs, or `all` to
    # make the manual DB cluster snapshot restorable by any AWS account. Do not
    # add the `all` value for any manual DB cluster snapshots that contain
    # private information that you don't want available to all AWS accounts.
    values_to_add: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of DB cluster snapshot attributes to remove from the attribute
    # specified by `AttributeName`.

    # To remove authorization for other AWS accounts to copy or restore a manual
    # DB cluster snapshot, set this list to include one or more AWS account
    # identifiers, or `all` to remove authorization for any AWS account to copy
    # or restore the DB cluster snapshot. If you specify `all`, an AWS account
    # whose account ID is explicitly added to the `restore` attribute can still
    # copy or restore a manual DB cluster snapshot.
    values_to_remove: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ModifyDBClusterSnapshotAttributeResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_snapshot_attributes_result",
                "DBClusterSnapshotAttributesResult",
                autoboto.TypeInfo(DBClusterSnapshotAttributesResult),
            ),
        ]

    # Contains the results of a successful call to the
    # DescribeDBClusterSnapshotAttributes API action.

    # Manual DB cluster snapshot attributes are used to authorize other AWS
    # accounts to copy or restore a manual DB cluster snapshot. For more
    # information, see the ModifyDBClusterSnapshotAttribute API action.
    db_cluster_snapshot_attributes_result: "DBClusterSnapshotAttributesResult" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ModifyDBInstanceMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "allocated_storage",
                "AllocatedStorage",
                autoboto.TypeInfo(int),
            ),
            (
                "db_instance_class",
                "DBInstanceClass",
                autoboto.TypeInfo(str),
            ),
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "db_security_groups",
                "DBSecurityGroups",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "apply_immediately",
                "ApplyImmediately",
                autoboto.TypeInfo(bool),
            ),
            (
                "master_user_password",
                "MasterUserPassword",
                autoboto.TypeInfo(str),
            ),
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                autoboto.TypeInfo(int),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                autoboto.TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                autoboto.TypeInfo(str),
            ),
            (
                "multi_az",
                "MultiAZ",
                autoboto.TypeInfo(bool),
            ),
            (
                "engine_version",
                "EngineVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "allow_major_version_upgrade",
                "AllowMajorVersionUpgrade",
                autoboto.TypeInfo(bool),
            ),
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                autoboto.TypeInfo(bool),
            ),
            (
                "license_model",
                "LicenseModel",
                autoboto.TypeInfo(str),
            ),
            (
                "iops",
                "Iops",
                autoboto.TypeInfo(int),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "new_db_instance_identifier",
                "NewDBInstanceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "storage_type",
                "StorageType",
                autoboto.TypeInfo(str),
            ),
            (
                "tde_credential_arn",
                "TdeCredentialArn",
                autoboto.TypeInfo(str),
            ),
            (
                "tde_credential_password",
                "TdeCredentialPassword",
                autoboto.TypeInfo(str),
            ),
            (
                "ca_certificate_identifier",
                "CACertificateIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "domain",
                "Domain",
                autoboto.TypeInfo(str),
            ),
            (
                "copy_tags_to_snapshot",
                "CopyTagsToSnapshot",
                autoboto.TypeInfo(bool),
            ),
            (
                "monitoring_interval",
                "MonitoringInterval",
                autoboto.TypeInfo(int),
            ),
            (
                "db_port_number",
                "DBPortNumber",
                autoboto.TypeInfo(int),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                autoboto.TypeInfo(bool),
            ),
            (
                "monitoring_role_arn",
                "MonitoringRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "domain_iam_role_name",
                "DomainIAMRoleName",
                autoboto.TypeInfo(str),
            ),
            (
                "promotion_tier",
                "PromotionTier",
                autoboto.TypeInfo(int),
            ),
            (
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                autoboto.TypeInfo(bool),
            ),
            (
                "enable_performance_insights",
                "EnablePerformanceInsights",
                autoboto.TypeInfo(bool),
            ),
            (
                "performance_insights_kms_key_id",
                "PerformanceInsightsKMSKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "cloudwatch_logs_export_configuration",
                "CloudwatchLogsExportConfiguration",
                autoboto.TypeInfo(CloudwatchLogsExportConfiguration),
            ),
        ]

    # The DB instance identifier. This value is stored as a lowercase string.

    # Constraints:

    #   * Must match the identifier of an existing DBInstance.
    db_instance_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The new amount of storage (in gibibytes) to allocate for the DB instance.

    # Not applicable. Storage is managed by the DB Cluster.
    allocated_storage: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The new compute and memory capacity of the DB instance, for example,
    # `db.m4.large`. Not all DB instance classes are available in all AWS
    # Regions.

    # If you modify the DB instance class, an outage occurs during the change.
    # The change is applied during the next maintenance window, unless
    # `ApplyImmediately` is specified as `true` for this request.

    # Default: Uses existing setting
    db_instance_class: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The new DB subnet group for the DB instance. You can use this parameter to
    # move your DB instance to a different VPC.

    # Changing the subnet group causes an outage during the change. The change is
    # applied during the next maintenance window, unless you specify `true` for
    # the `ApplyImmediately` parameter.

    # Constraints: If supplied, must match the name of an existing DBSubnetGroup.

    # Example: `mySubnetGroup`
    db_subnet_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of DB security groups to authorize on this DB instance. Changing
    # this setting doesn't result in an outage and the change is asynchronously
    # applied as soon as possible.

    # Constraints:

    #   * If supplied, must match existing DBSecurityGroups.
    db_security_groups: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list of EC2 VPC security groups to authorize on this DB instance. This
    # change is asynchronously applied as soon as possible.

    # Not applicable. The associated list of EC2 VPC security groups is managed
    # by the DB cluster. For more information, see ModifyDBCluster.

    # Constraints:

    #   * If supplied, must match existing VpcSecurityGroupIds.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Specifies whether the modifications in this request and any pending
    # modifications are asynchronously applied as soon as possible, regardless of
    # the `PreferredMaintenanceWindow` setting for the DB instance.

    # If this parameter is set to `false`, changes to the DB instance are applied
    # during the next maintenance window. Some parameter changes can cause an
    # outage and are applied on the next call to RebootDBInstance, or the next
    # failure reboot.

    # Default: `false`
    apply_immediately: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The new password for the master user. The password can include any
    # printable ASCII character except "/", """, or "@".

    # Not applicable.

    # Default: Uses existing setting
    master_user_password: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the DB parameter group to apply to the DB instance. Changing
    # this setting doesn't result in an outage. The parameter group name itself
    # is changed immediately, but the actual parameter changes are not applied
    # until you reboot the instance without failover. The db instance will NOT be
    # rebooted automatically and the parameter changes will NOT be applied during
    # the next maintenance window.

    # Default: Uses existing setting

    # Constraints: The DB parameter group must be in the same DB parameter group
    # family as this DB instance.
    db_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The number of days to retain automated backups. Setting this parameter to a
    # positive number enables backups. Setting this parameter to 0 disables
    # automated backups.

    # Not applicable. The retention period for automated backups is managed by
    # the DB cluster. For more information, see ModifyDBCluster.

    # Default: Uses existing setting
    backup_retention_period: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The daily time range during which automated backups are created if
    # automated backups are enabled.

    # Not applicable. The daily time range for creating automated backups is
    # managed by the DB cluster. For more information, see ModifyDBCluster.

    # Constraints:

    #   * Must be in the format hh24:mi-hh24:mi

    #   * Must be in Universal Time Coordinated (UTC)

    #   * Must not conflict with the preferred maintenance window

    #   * Must be at least 30 minutes
    preferred_backup_window: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The weekly time range (in UTC) during which system maintenance can occur,
    # which might result in an outage. Changing this parameter doesn't result in
    # an outage, except in the following situation, and the change is
    # asynchronously applied as soon as possible. If there are pending actions
    # that cause a reboot, and the maintenance window is changed to include the
    # current time, then changing this parameter will cause a reboot of the DB
    # instance. If moving this window to the current time, there must be at least
    # 30 minutes between the current time and end of the window to ensure pending
    # changes are applied.

    # Default: Uses existing setting

    # Format: ddd:hh24:mi-ddd:hh24:mi

    # Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun

    # Constraints: Must be at least 30 minutes
    preferred_maintenance_window: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies if the DB instance is a Multi-AZ deployment. Changing this
    # parameter doesn't result in an outage and the change is applied during the
    # next maintenance window unless the `ApplyImmediately` parameter is set to
    # `true` for this request.
    multi_az: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version number of the database engine to upgrade to. Changing this
    # parameter results in an outage and the change is applied during the next
    # maintenance window unless the `ApplyImmediately` parameter is set to `true`
    # for this request.

    # For major version upgrades, if a nondefault DB parameter group is currently
    # in use, a new DB parameter group in the DB parameter group family for the
    # new engine version must be specified. The new DB parameter group can be the
    # default for that DB parameter group family.
    engine_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates that major version upgrades are allowed. Changing this parameter
    # doesn't result in an outage and the change is asynchronously applied as
    # soon as possible.

    # Constraints: This parameter must be set to true when specifying a value for
    # the EngineVersion parameter that is a different major version than the DB
    # instance's current version.
    allow_major_version_upgrade: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates that minor version upgrades are applied automatically to the DB
    # instance during the maintenance window. Changing this parameter doesn't
    # result in an outage except in the following case and the change is
    # asynchronously applied as soon as possible. An outage will result if this
    # parameter is set to `true` during the maintenance window, and a newer minor
    # version is available, and Neptune has enabled auto patching for that engine
    # version.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The license model for the DB instance.

    # Valid values: `license-included` | `bring-your-own-license` | `general-
    # public-license`
    license_model: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The new Provisioned IOPS (I/O operations per second) value for the
    # instance.

    # Changing this setting doesn't result in an outage and the change is applied
    # during the next maintenance window unless the `ApplyImmediately` parameter
    # is set to `true` for this request.

    # Default: Uses existing setting
    iops: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates that the DB instance should be associated with the specified
    # option group. Changing this parameter doesn't result in an outage except in
    # the following case and the change is applied during the next maintenance
    # window unless the `ApplyImmediately` parameter is set to `true` for this
    # request. If the parameter change results in an option group that enables
    # OEM, this change can cause a brief (sub-second) period during which new
    # connections are rejected but existing connections are not interrupted.

    # Permanent options, such as the TDE option for Oracle Advanced Security TDE,
    # can't be removed from an option group, and that option group can't be
    # removed from a DB instance once it is associated with a DB instance
    option_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The new DB instance identifier for the DB instance when renaming a DB
    # instance. When you change the DB instance identifier, an instance reboot
    # will occur immediately if you set `Apply Immediately` to true, or will
    # occur during the next maintenance window if `Apply Immediately` to false.
    # This value is stored as a lowercase string.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens.

    #   * The first character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    # Example: `mydbinstance`
    new_db_instance_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the storage type to be associated with the DB instance.

    # If you specify Provisioned IOPS (`io1`), you must also include a value for
    # the `Iops` parameter.

    # If you choose to migrate your DB instance from using standard storage to
    # using Provisioned IOPS, or from using Provisioned IOPS to using standard
    # storage, the process can take time. The duration of the migration depends
    # on several factors such as database load, storage size, storage type
    # (standard or Provisioned IOPS), amount of IOPS provisioned (if any), and
    # the number of prior scale storage operations. Typical migration times are
    # under 24 hours, but the process can take up to several days in some cases.
    # During the migration, the DB instance is available for use, but might
    # experience performance degradation. While the migration takes place,
    # nightly backups for the instance are suspended. No other Amazon Neptune
    # operations can take place for the instance, including modifying the
    # instance, rebooting the instance, deleting the instance, creating a Read
    # Replica for the instance, and creating a DB snapshot of the instance.

    # Valid values: `standard | gp2 | io1`

    # Default: `io1` if the `Iops` parameter is specified, otherwise `standard`
    storage_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The ARN from the key store with which to associate the instance for TDE
    # encryption.
    tde_credential_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The password for the given ARN from the key store in order to access the
    # device.
    tde_credential_password: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates the certificate that needs to be associated with the instance.
    ca_certificate_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Not supported.
    domain: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # True to copy all tags from the DB instance to snapshots of the DB instance,
    # and otherwise false. The default is false.
    copy_tags_to_snapshot: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The interval, in seconds, between points when Enhanced Monitoring metrics
    # are collected for the DB instance. To disable collecting Enhanced
    # Monitoring metrics, specify 0. The default is 0.

    # If `MonitoringRoleArn` is specified, then you must also set
    # `MonitoringInterval` to a value other than 0.

    # Valid Values: `0, 1, 5, 10, 15, 30, 60`
    monitoring_interval: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The port number on which the database accepts connections.

    # The value of the `DBPortNumber` parameter must not match any of the port
    # values specified for options in the option group for the DB instance.

    # Your database will restart when you change the `DBPortNumber` value
    # regardless of the value of the `ApplyImmediately` parameter.

    # Default: `8182`
    db_port_number: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # This parameter is not supported.
    publicly_accessible: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ARN for the IAM role that permits Neptune to send enhanced monitoring
    # metrics to Amazon CloudWatch Logs. For example,
    # `arn:aws:iam:123456789012:role/emaccess`.

    # If `MonitoringInterval` is set to a value other than 0, then you must
    # supply a `MonitoringRoleArn` value.
    monitoring_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Not supported
    domain_iam_role_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A value that specifies the order in which a Read Replica is promoted to the
    # primary instance after a failure of the existing primary instance.

    # Default: 1

    # Valid Values: 0 - 15
    promotion_tier: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # True to enable mapping of AWS Identity and Access Management (IAM) accounts
    # to database accounts, and otherwise false.

    # You can enable IAM database authentication for the following database
    # engines

    # Not applicable. Mapping AWS IAM accounts to database accounts is managed by
    # the DB cluster. For more information, see ModifyDBCluster.

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # True to enable Performance Insights for the DB instance, and otherwise
    # false.
    enable_performance_insights: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS KMS key identifier for encryption of Performance Insights data. The
    # KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the
    # KMS key alias for the KMS encryption key.
    performance_insights_kms_key_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The configuration setting for the log types to be enabled for export to
    # CloudWatch Logs for a specific DB instance or DB cluster.
    cloudwatch_logs_export_configuration: "CloudwatchLogsExportConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ModifyDBInstanceResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance",
                "DBInstance",
                autoboto.TypeInfo(DBInstance),
            ),
        ]

    # Contains the details of an Amazon Neptune DB instance.

    # This data type is used as a response element in the DescribeDBInstances
    # action.
    db_instance: "DBInstance" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ModifyDBParameterGroupMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.List[Parameter]),
            ),
        ]

    # The name of the DB parameter group.

    # Constraints:

    #   * If supplied, must match the name of an existing DBParameterGroup.
    db_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of parameter names, values, and the apply method for the parameter
    # update. At least one parameter name, value, and apply method must be
    # supplied; subsequent arguments are optional. A maximum of 20 parameters can
    # be modified in a single request.

    # Valid Values (for the application method): `immediate | pending-reboot`

    # You can use the immediate value with dynamic parameters only. You can use
    # the pending-reboot value for both dynamic and static parameters, and
    # changes are applied when you reboot the DB instance without failover.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ModifyDBSubnetGroupMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "db_subnet_group_description",
                "DBSubnetGroupDescription",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name for the DB subnet group. This value is stored as a lowercase
    # string. You can't modify the default subnet group.

    # Constraints: Must match the name of an existing DBSubnetGroup. Must not be
    # default.

    # Example: `mySubnetgroup`
    db_subnet_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The EC2 subnet IDs for the DB subnet group.
    subnet_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The description for the DB subnet group.
    db_subnet_group_description: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyDBSubnetGroupResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_subnet_group",
                "DBSubnetGroup",
                autoboto.TypeInfo(DBSubnetGroup),
            ),
        ]

    # Contains the details of an Amazon Neptune DB subnet group.

    # This data type is used as a response element in the DescribeDBSubnetGroups
    # action.
    db_subnet_group: "DBSubnetGroup" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ModifyEventSubscriptionMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_name",
                "SubscriptionName",
                autoboto.TypeInfo(str),
            ),
            (
                "sns_topic_arn",
                "SnsTopicArn",
                autoboto.TypeInfo(str),
            ),
            (
                "source_type",
                "SourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "event_categories",
                "EventCategories",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "enabled",
                "Enabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the event notification subscription.
    subscription_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the SNS topic created for event
    # notification. The ARN is created by Amazon SNS when you create a topic and
    # subscribe to it.
    sns_topic_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of source that is generating the events. For example, if you want
    # to be notified of events generated by a DB instance, you would set this
    # parameter to db-instance. if this value is not specified, all events are
    # returned.

    # Valid values: db-instance | db-parameter-group | db-security-group | db-
    # snapshot
    source_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of event categories for a SourceType that you want to subscribe to.
    # You can see a list of the categories for a given SourceType by using the
    # **DescribeEventCategories** action.
    event_categories: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A Boolean value; set to **true** to activate the subscription.
    enabled: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyEventSubscriptionResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_subscription",
                "EventSubscription",
                autoboto.TypeInfo(EventSubscription),
            ),
        ]

    # Contains the results of a successful invocation of the
    # DescribeEventSubscriptions action.
    event_subscription: "EventSubscription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class OptionGroupMembership(autoboto.ShapeBase):
    """
    Provides information on the option groups the DB instance is a member of.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "option_group_name",
                "OptionGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the option group that the instance belongs to.
    option_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the DB instance's option group membership. Valid values are:
    # `in-sync`, `pending-apply`, `pending-removal`, `pending-maintenance-apply`,
    # `pending-maintenance-removal`, `applying`, `removing`, and `failed`.
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OptionGroupNotFoundFault(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class OrderableDBInstanceOption(autoboto.ShapeBase):
    """
    Contains a list of available options for a DB instance.

    This data type is used as a response element in the
    DescribeOrderableDBInstanceOptions action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "engine",
                "Engine",
                autoboto.TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "db_instance_class",
                "DBInstanceClass",
                autoboto.TypeInfo(str),
            ),
            (
                "license_model",
                "LicenseModel",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                autoboto.TypeInfo(typing.List[AvailabilityZone]),
            ),
            (
                "multi_az_capable",
                "MultiAZCapable",
                autoboto.TypeInfo(bool),
            ),
            (
                "read_replica_capable",
                "ReadReplicaCapable",
                autoboto.TypeInfo(bool),
            ),
            (
                "vpc",
                "Vpc",
                autoboto.TypeInfo(bool),
            ),
            (
                "supports_storage_encryption",
                "SupportsStorageEncryption",
                autoboto.TypeInfo(bool),
            ),
            (
                "storage_type",
                "StorageType",
                autoboto.TypeInfo(str),
            ),
            (
                "supports_iops",
                "SupportsIops",
                autoboto.TypeInfo(bool),
            ),
            (
                "supports_enhanced_monitoring",
                "SupportsEnhancedMonitoring",
                autoboto.TypeInfo(bool),
            ),
            (
                "supports_iam_database_authentication",
                "SupportsIAMDatabaseAuthentication",
                autoboto.TypeInfo(bool),
            ),
            (
                "supports_performance_insights",
                "SupportsPerformanceInsights",
                autoboto.TypeInfo(bool),
            ),
            (
                "min_storage_size",
                "MinStorageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "max_storage_size",
                "MaxStorageSize",
                autoboto.TypeInfo(int),
            ),
            (
                "min_iops_per_db_instance",
                "MinIopsPerDbInstance",
                autoboto.TypeInfo(int),
            ),
            (
                "max_iops_per_db_instance",
                "MaxIopsPerDbInstance",
                autoboto.TypeInfo(int),
            ),
            (
                "min_iops_per_gib",
                "MinIopsPerGib",
                autoboto.TypeInfo(float),
            ),
            (
                "max_iops_per_gib",
                "MaxIopsPerGib",
                autoboto.TypeInfo(float),
            ),
        ]

    # The engine type of a DB instance.
    engine: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The engine version of a DB instance.
    engine_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The DB instance class for a DB instance.
    db_instance_class: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The license model for a DB instance.
    license_model: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A list of Availability Zones for a DB instance.
    availability_zones: typing.List["AvailabilityZone"] = dataclasses.field(
        default_factory=list,
    )

    # Indicates whether a DB instance is Multi-AZ capable.
    multi_az_capable: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether a DB instance can have a Read Replica.
    read_replica_capable: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether a DB instance is in a VPC.
    vpc: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether a DB instance supports encrypted storage.
    supports_storage_encryption: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates the storage type for a DB instance.
    storage_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates whether a DB instance supports provisioned IOPS.
    supports_iops: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether a DB instance supports Enhanced Monitoring at intervals
    # from 1 to 60 seconds.
    supports_enhanced_monitoring: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether a DB instance supports IAM database authentication.
    supports_iam_database_authentication: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # True if a DB instance supports Performance Insights, otherwise false.
    supports_performance_insights: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Minimum storage size for a DB instance.
    min_storage_size: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Maximum storage size for a DB instance.
    max_storage_size: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Minimum total provisioned IOPS for a DB instance.
    min_iops_per_db_instance: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Maximum total provisioned IOPS for a DB instance.
    max_iops_per_db_instance: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Minimum provisioned IOPS per GiB for a DB instance.
    min_iops_per_gib: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Maximum provisioned IOPS per GiB for a DB instance.
    max_iops_per_gib: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OrderableDBInstanceOptionsMessage(autoboto.ShapeBase):
    """
    Contains the result of a successful invocation of the
    DescribeOrderableDBInstanceOptions action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "orderable_db_instance_options",
                "OrderableDBInstanceOptions",
                autoboto.TypeInfo(typing.List[OrderableDBInstanceOption]),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # An OrderableDBInstanceOption structure containing information about
    # orderable options for the DB instance.
    orderable_db_instance_options: typing.List["OrderableDBInstanceOption"
                                              ] = dataclasses.field(
                                                  default_factory=list,
                                              )

    # An optional pagination token provided by a previous
    # OrderableDBInstanceOptions request. If this parameter is specified, the
    # response includes only records beyond the marker, up to the value specified
    # by `MaxRecords` .
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Parameter(autoboto.ShapeBase):
    """
    This data type is used as a request parameter in the ModifyDBParameterGroup and
    ResetDBParameterGroup actions.

    This data type is used as a response element in the
    DescribeEngineDefaultParameters and DescribeDBParameters actions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_name",
                "ParameterName",
                autoboto.TypeInfo(str),
            ),
            (
                "parameter_value",
                "ParameterValue",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "source",
                "Source",
                autoboto.TypeInfo(str),
            ),
            (
                "apply_type",
                "ApplyType",
                autoboto.TypeInfo(str),
            ),
            (
                "data_type",
                "DataType",
                autoboto.TypeInfo(str),
            ),
            (
                "allowed_values",
                "AllowedValues",
                autoboto.TypeInfo(str),
            ),
            (
                "is_modifiable",
                "IsModifiable",
                autoboto.TypeInfo(bool),
            ),
            (
                "minimum_engine_version",
                "MinimumEngineVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "apply_method",
                "ApplyMethod",
                autoboto.TypeInfo(ApplyMethod),
            ),
        ]

    # Specifies the name of the parameter.
    parameter_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the value of the parameter.
    parameter_value: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provides a description of the parameter.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates the source of the parameter value.
    source: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the engine specific parameters type.
    apply_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the valid data type for the parameter.
    data_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the valid range of values for the parameter.
    allowed_values: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates whether (`true`) or not (`false`) the parameter can be modified.
    # Some parameters have security or operational implications that prevent them
    # from being changed.
    is_modifiable: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The earliest engine version to which the parameter can apply.
    minimum_engine_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates when to apply parameter updates.
    apply_method: "ApplyMethod" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PendingCloudwatchLogsExports(autoboto.ShapeBase):
    """
    A list of the log types whose configuration is still pending. In other words,
    these log types are in the process of being activated or deactivated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_types_to_enable",
                "LogTypesToEnable",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "log_types_to_disable",
                "LogTypesToDisable",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # Log types that are in the process of being deactivated. After they are
    # deactivated, these log types aren't exported to CloudWatch Logs.
    log_types_to_enable: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Log types that are in the process of being enabled. After they are enabled,
    # these log types are exported to CloudWatch Logs.
    log_types_to_disable: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class PendingMaintenanceAction(autoboto.ShapeBase):
    """
    Provides information about a pending maintenance action for a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                autoboto.TypeInfo(str),
            ),
            (
                "auto_applied_after_date",
                "AutoAppliedAfterDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "forced_apply_date",
                "ForcedApplyDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "opt_in_status",
                "OptInStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "current_apply_date",
                "CurrentApplyDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of pending maintenance action that is available for the resource.
    action: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date of the maintenance window when the action is applied. The
    # maintenance action is applied to the resource during its first maintenance
    # window after this date. If this date is specified, any `next-maintenance`
    # opt-in requests are ignored.
    auto_applied_after_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The date when the maintenance action is automatically applied. The
    # maintenance action is applied to the resource on this date regardless of
    # the maintenance window for the resource. If this date is specified, any
    # `immediate` opt-in requests are ignored.
    forced_apply_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates the type of opt-in request that has been received for the
    # resource.
    opt_in_status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The effective date when the pending maintenance action is applied to the
    # resource. This date takes into account opt-in requests received from the
    # ApplyPendingMaintenanceAction API, the `AutoAppliedAfterDate`, and the
    # `ForcedApplyDate`. This value is blank if an opt-in request has not been
    # received and nothing has been specified as `AutoAppliedAfterDate` or
    # `ForcedApplyDate`.
    current_apply_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A description providing more detail about the maintenance action.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PendingMaintenanceActionsMessage(autoboto.ShapeBase):
    """
    Data returned from the **DescribePendingMaintenanceActions** action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pending_maintenance_actions",
                "PendingMaintenanceActions",
                autoboto.TypeInfo(
                    typing.List[ResourcePendingMaintenanceActions]
                ),
            ),
            (
                "marker",
                "Marker",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of the pending maintenance actions for the resource.
    pending_maintenance_actions: typing.List["ResourcePendingMaintenanceActions"
                                            ] = dataclasses.field(
                                                default_factory=list,
                                            )

    # An optional pagination token provided by a previous
    # `DescribePendingMaintenanceActions` request. If this parameter is
    # specified, the response includes only records beyond the marker, up to a
    # number of records specified by `MaxRecords`.
    marker: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PendingModifiedValues(autoboto.ShapeBase):
    """
    This data type is used as a response element in the ModifyDBInstance action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_class",
                "DBInstanceClass",
                autoboto.TypeInfo(str),
            ),
            (
                "allocated_storage",
                "AllocatedStorage",
                autoboto.TypeInfo(int),
            ),
            (
                "master_user_password",
                "MasterUserPassword",
                autoboto.TypeInfo(str),
            ),
            (
                "port",
                "Port",
                autoboto.TypeInfo(int),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                autoboto.TypeInfo(int),
            ),
            (
                "multi_az",
                "MultiAZ",
                autoboto.TypeInfo(bool),
            ),
            (
                "engine_version",
                "EngineVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "license_model",
                "LicenseModel",
                autoboto.TypeInfo(str),
            ),
            (
                "iops",
                "Iops",
                autoboto.TypeInfo(int),
            ),
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "storage_type",
                "StorageType",
                autoboto.TypeInfo(str),
            ),
            (
                "ca_certificate_identifier",
                "CACertificateIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "pending_cloudwatch_logs_exports",
                "PendingCloudwatchLogsExports",
                autoboto.TypeInfo(PendingCloudwatchLogsExports),
            ),
        ]

    # Contains the new `DBInstanceClass` for the DB instance that will be applied
    # or is currently being applied.
    db_instance_class: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains the new `AllocatedStorage` size for the DB instance that will be
    # applied or is currently being applied.
    allocated_storage: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains the pending or currently-in-progress change of the master
    # credentials for the DB instance.
    master_user_password: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the pending port for the DB instance.
    port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the pending number of days for which automated backups are
    # retained.
    backup_retention_period: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Indicates that the Single-AZ DB instance is to change to a Multi-AZ
    # deployment.
    multi_az: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Indicates the database engine version.
    engine_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The license model for the DB instance.

    # Valid values: `license-included` | `bring-your-own-license` | `general-
    # public-license`
    license_model: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the new Provisioned IOPS value for the DB instance that will be
    # applied or is currently being applied.
    iops: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Contains the new `DBInstanceIdentifier` for the DB instance that will be
    # applied or is currently being applied.
    db_instance_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies the storage type to be associated with the DB instance.
    storage_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Specifies the identifier of the CA certificate for the DB instance.
    ca_certificate_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The new DB subnet group for the DB instance.
    db_subnet_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of the log types whose configuration is still pending. In other
    # words, these log types are in the process of being activated or
    # deactivated.
    pending_cloudwatch_logs_exports: "PendingCloudwatchLogsExports" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PromoteReadReplicaDBClusterMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identifier of the DB cluster Read Replica to promote. This parameter is
    # not case-sensitive.

    # Constraints:

    #   * Must match the identifier of an existing DBCluster Read Replica.

    # Example: `my-cluster-replica1`
    db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PromoteReadReplicaDBClusterResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster",
                "DBCluster",
                autoboto.TypeInfo(DBCluster),
            ),
        ]

    # Contains the details of an Amazon Neptune DB cluster.

    # This data type is used as a response element in the DescribeDBClusters
    # action.
    db_cluster: "DBCluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class ProvisionedIopsNotAvailableInAZFault(autoboto.ShapeBase):
    """
    Provisioned IOPS not available in the specified Availability Zone.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Range(autoboto.ShapeBase):
    """
    A range of integer values.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "from_",
                "From",
                autoboto.TypeInfo(int),
            ),
            (
                "to",
                "To",
                autoboto.TypeInfo(int),
            ),
            (
                "step",
                "Step",
                autoboto.TypeInfo(int),
            ),
        ]

    # The minimum value in the range.
    from_: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum value in the range.
    to: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The step value for the range. For example, if you have a range of 5,000 to
    # 10,000, with a step value of 1,000, the valid values start at 5,000 and
    # step up by 1,000. Even though 7,500 is within the range, it isn't a valid
    # value for the range. The valid values are 5,000, 6,000, 7,000, 8,000...
    step: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RebootDBInstanceMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "force_failover",
                "ForceFailover",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The DB instance identifier. This parameter is stored as a lowercase string.

    # Constraints:

    #   * Must match the identifier of an existing DBInstance.
    db_instance_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When `true`, the reboot is conducted through a MultiAZ failover.

    # Constraint: You can't specify `true` if the instance is not configured for
    # MultiAZ.
    force_failover: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RebootDBInstanceResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance",
                "DBInstance",
                autoboto.TypeInfo(DBInstance),
            ),
        ]

    # Contains the details of an Amazon Neptune DB instance.

    # This data type is used as a response element in the DescribeDBInstances
    # action.
    db_instance: "DBInstance" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class RemoveRoleFromDBClusterMessage(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the DB cluster to disassociate the IAM role from.
    db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the IAM role to disassociate from the DB
    # cluster, for example `arn:aws:iam::123456789012:role/NeptuneAccessRole`.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveSourceIdentifierFromSubscriptionMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_name",
                "SubscriptionName",
                autoboto.TypeInfo(str),
            ),
            (
                "source_identifier",
                "SourceIdentifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the event notification subscription you want to remove a source
    # identifier from.
    subscription_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The source identifier to be removed from the subscription, such as the **DB
    # instance identifier** for a DB instance or the name of a security group.
    source_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveSourceIdentifierFromSubscriptionResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_subscription",
                "EventSubscription",
                autoboto.TypeInfo(EventSubscription),
            ),
        ]

    # Contains the results of a successful invocation of the
    # DescribeEventSubscriptions action.
    event_subscription: "EventSubscription" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class RemoveTagsFromResourceMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_name",
                "ResourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Neptune resource that the tags are removed from. This value is
    # an Amazon Resource Name (ARN). For information about creating an ARN, see [
    # Constructing an Amazon Resource Name
    # (ARN)](http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing).
    resource_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The tag key (name) of the tag to be removed.
    tag_keys: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class ResetDBClusterParameterGroupMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "reset_all_parameters",
                "ResetAllParameters",
                autoboto.TypeInfo(bool),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.List[Parameter]),
            ),
        ]

    # The name of the DB cluster parameter group to reset.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A value that is set to `true` to reset all parameters in the DB cluster
    # parameter group to their default values, and `false` otherwise. You can't
    # use this parameter if there is a list of parameter names specified for the
    # `Parameters` parameter.
    reset_all_parameters: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of parameter names in the DB cluster parameter group to reset to the
    # default values. You can't use this parameter if the `ResetAllParameters`
    # parameter is set to `true`.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ResetDBParameterGroupMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "reset_all_parameters",
                "ResetAllParameters",
                autoboto.TypeInfo(bool),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.List[Parameter]),
            ),
        ]

    # The name of the DB parameter group.

    # Constraints:

    #   * Must match the name of an existing DBParameterGroup.
    db_parameter_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether (`true`) or not (`false`) to reset all parameters in the
    # DB parameter group to default values.

    # Default: `true`
    reset_all_parameters: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # To reset the entire DB parameter group, specify the `DBParameterGroup` name
    # and `ResetAllParameters` parameters. To reset specific parameters, provide
    # a list of the following: `ParameterName` and `ApplyMethod`. A maximum of 20
    # parameters can be modified in a single request.

    # Valid Values (for Apply method): `pending-reboot`
    parameters: typing.List["Parameter"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ResourceNotFoundFault(autoboto.ShapeBase):
    """
    The specified resource ID was not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResourcePendingMaintenanceActions(autoboto.ShapeBase):
    """
    Describes the pending maintenance actions for a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_identifier",
                "ResourceIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "pending_maintenance_action_details",
                "PendingMaintenanceActionDetails",
                autoboto.TypeInfo(typing.List[PendingMaintenanceAction]),
            ),
        ]

    # The ARN of the resource that has pending maintenance actions.
    resource_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list that provides details about the pending maintenance actions for the
    # resource.
    pending_maintenance_action_details: typing.List["PendingMaintenanceAction"
                                                   ] = dataclasses.field(
                                                       default_factory=list,
                                                   )


@dataclasses.dataclass
class RestoreDBClusterFromSnapshotMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "snapshot_identifier",
                "SnapshotIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "engine_version",
                "EngineVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "port",
                "Port",
                autoboto.TypeInfo(int),
            ),
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the DB cluster to create from the DB snapshot or DB cluster
    # snapshot. This parameter isn't case-sensitive.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # Example: `my-snapshot-id`
    db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier for the DB snapshot or DB cluster snapshot to restore from.

    # You can use either the name or the Amazon Resource Name (ARN) to specify a
    # DB cluster snapshot. However, you can use only the ARN to specify a DB
    # snapshot.

    # Constraints:

    #   * Must match the identifier of an existing Snapshot.
    snapshot_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The database engine to use for the new DB cluster.

    # Default: The same as source

    # Constraint: Must be compatible with the engine of the source
    engine: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Provides the list of EC2 Availability Zones that instances in the restored
    # DB cluster can be created in.
    availability_zones: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The version of the database engine to use for the new DB cluster.
    engine_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The port number on which the new DB cluster accepts connections.

    # Constraints: Value must be `1150-65535`

    # Default: The same port as the original DB cluster.
    port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the DB subnet group to use for the new DB cluster.

    # Constraints: If supplied, must match the name of an existing DBSubnetGroup.

    # Example: `mySubnetgroup`
    db_subnet_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The database name for the restored DB cluster.
    database_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the option group to use for the restored DB cluster.
    option_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of VPC security groups that the new DB cluster will belong to.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The tags to be assigned to the restored DB cluster.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # The AWS KMS key identifier to use when restoring an encrypted DB cluster
    # from a DB snapshot or DB cluster snapshot.

    # The KMS key identifier is the Amazon Resource Name (ARN) for the KMS
    # encryption key. If you are restoring a DB cluster with the same AWS account
    # that owns the KMS encryption key used to encrypt the new DB cluster, then
    # you can use the KMS key alias instead of the ARN for the KMS encryption
    # key.

    # If you do not specify a value for the `KmsKeyId` parameter, then the
    # following will occur:

    #   * If the DB snapshot or DB cluster snapshot in `SnapshotIdentifier` is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the DB snapshot or DB cluster snapshot.

    #   * If the DB snapshot or DB cluster snapshot in `SnapshotIdentifier` is not encrypted, then the restored DB cluster is not encrypted.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # True to enable mapping of AWS Identity and Access Management (IAM) accounts
    # to database accounts, and otherwise false.

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RestoreDBClusterFromSnapshotResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster",
                "DBCluster",
                autoboto.TypeInfo(DBCluster),
            ),
        ]

    # Contains the details of an Amazon Neptune DB cluster.

    # This data type is used as a response element in the DescribeDBClusters
    # action.
    db_cluster: "DBCluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class RestoreDBClusterToPointInTimeMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "source_db_cluster_identifier",
                "SourceDBClusterIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "restore_type",
                "RestoreType",
                autoboto.TypeInfo(str),
            ),
            (
                "restore_to_time",
                "RestoreToTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "use_latest_restorable_time",
                "UseLatestRestorableTime",
                autoboto.TypeInfo(bool),
            ),
            (
                "port",
                "Port",
                autoboto.TypeInfo(int),
            ),
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "Tags",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the new DB cluster to be created.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens
    db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The identifier of the source DB cluster from which to restore.

    # Constraints:

    #   * Must match the identifier of an existing DBCluster.
    source_db_cluster_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of restore to be performed. You can specify one of the following
    # values:

    #   * `full-copy` \- The new DB cluster is restored as a full copy of the source DB cluster.

    #   * `copy-on-write` \- The new DB cluster is restored as a clone of the source DB cluster.

    # Constraints: You can't specify `copy-on-write` if the engine version of the
    # source DB cluster is earlier than 1.11.

    # If you don't specify a `RestoreType` value, then the new DB cluster is
    # restored as a full copy of the source DB cluster.
    restore_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date and time to restore the DB cluster to.

    # Valid Values: Value must be a time in Universal Coordinated Time (UTC)
    # format

    # Constraints:

    #   * Must be before the latest restorable time for the DB instance

    #   * Must be specified if `UseLatestRestorableTime` parameter is not provided

    #   * Cannot be specified if `UseLatestRestorableTime` parameter is true

    #   * Cannot be specified if `RestoreType` parameter is `copy-on-write`

    # Example: `2015-03-07T23:45:00Z`
    restore_to_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A value that is set to `true` to restore the DB cluster to the latest
    # restorable backup time, and `false` otherwise.

    # Default: `false`

    # Constraints: Cannot be specified if `RestoreToTime` parameter is provided.
    use_latest_restorable_time: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The port number on which the new DB cluster accepts connections.

    # Constraints: Value must be `1150-65535`

    # Default: The same port as the original DB cluster.
    port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The DB subnet group name to use for the new DB cluster.

    # Constraints: If supplied, must match the name of an existing DBSubnetGroup.

    # Example: `mySubnetgroup`
    db_subnet_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the option group for the new DB cluster.
    option_group_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of VPC security groups that the new DB cluster belongs to.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list of tags. For more information, see [Tagging Amazon Neptune
    # Resources](http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html).
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    # The AWS KMS key identifier to use when restoring an encrypted DB cluster
    # from an encrypted DB cluster.

    # The KMS key identifier is the Amazon Resource Name (ARN) for the KMS
    # encryption key. If you are restoring a DB cluster with the same AWS account
    # that owns the KMS encryption key used to encrypt the new DB cluster, then
    # you can use the KMS key alias instead of the ARN for the KMS encryption
    # key.

    # You can restore to a new DB cluster and encrypt the new DB cluster with a
    # KMS key that is different than the KMS key used to encrypt the source DB
    # cluster. The new DB cluster is encrypted with the KMS key identified by the
    # `KmsKeyId` parameter.

    # If you do not specify a value for the `KmsKeyId` parameter, then the
    # following will occur:

    #   * If the DB cluster is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the source DB cluster.

    #   * If the DB cluster is not encrypted, then the restored DB cluster is not encrypted.

    # If `DBClusterIdentifier` refers to a DB cluster that is not encrypted, then
    # the restore request is rejected.
    kms_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # True to enable mapping of AWS Identity and Access Management (IAM) accounts
    # to database accounts, and otherwise false.

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RestoreDBClusterToPointInTimeResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster",
                "DBCluster",
                autoboto.TypeInfo(DBCluster),
            ),
        ]

    # Contains the details of an Amazon Neptune DB cluster.

    # This data type is used as a response element in the DescribeDBClusters
    # action.
    db_cluster: "DBCluster" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class SNSInvalidTopicFault(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SNSNoAuthorizationFault(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SNSTopicArnNotFoundFault(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SharedSnapshotQuotaExceededFault(autoboto.ShapeBase):
    """
    You have exceeded the maximum number of accounts that you can share a manual DB
    snapshot with.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SnapshotQuotaExceededFault(autoboto.ShapeBase):
    """
    Request would result in user exceeding the allowed number of DB snapshots.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SourceNotFoundFault(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


class SourceType(Enum):
    db_instance = "db-instance"
    db_parameter_group = "db-parameter-group"
    db_security_group = "db-security-group"
    db_snapshot = "db-snapshot"
    db_cluster = "db-cluster"
    db_cluster_snapshot = "db-cluster-snapshot"


@dataclasses.dataclass
class StorageQuotaExceededFault(autoboto.ShapeBase):
    """
    Request would result in user exceeding the allowed amount of storage available
    across all DB instances.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StorageTypeNotSupportedFault(autoboto.ShapeBase):
    """
    _StorageType_ specified cannot be associated with the DB Instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Subnet(autoboto.ShapeBase):
    """
    This data type is used as a response element in the DescribeDBSubnetGroups
    action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_identifier",
                "SubnetIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "subnet_availability_zone",
                "SubnetAvailabilityZone",
                autoboto.TypeInfo(AvailabilityZone),
            ),
            (
                "subnet_status",
                "SubnetStatus",
                autoboto.TypeInfo(str),
            ),
        ]

    # Specifies the identifier of the subnet.
    subnet_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains Availability Zone information.

    # This data type is used as an element in the following data type:

    #   * OrderableDBInstanceOption
    subnet_availability_zone: "AvailabilityZone" = dataclasses.field(
        default_factory=dict,
    )

    # Specifies the status of the subnet.
    subnet_status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubnetAlreadyInUse(autoboto.ShapeBase):
    """
    The DB subnet is already in use in the Availability Zone.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubscriptionAlreadyExistFault(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubscriptionCategoryNotFoundFault(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubscriptionNotFoundFault(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Tag(autoboto.ShapeBase):
    """
    Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
    """

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

    # A key is the required name of the tag. The string value can be from 1 to
    # 128 Unicode characters in length and can't be prefixed with "aws:" or
    # "rds:". The string can only contain only the set of Unicode letters,
    # digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex:
    # "^([\\\p{L}\\\p{Z}\\\p{N}_.:/=+\\\\-]*)$").
    key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A value is the optional value of the tag. The string value can be from 1 to
    # 256 Unicode characters in length and can't be prefixed with "aws:" or
    # "rds:". The string can only contain only the set of Unicode letters,
    # digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex:
    # "^([\\\p{L}\\\p{Z}\\\p{N}_.:/=+\\\\-]*)$").
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagListMessage(autoboto.ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_list",
                "TagList",
                autoboto.TypeInfo(typing.List[Tag]),
            ),
        ]

    # List of tags returned by the ListTagsForResource operation.
    tag_list: typing.List["Tag"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class Timezone(autoboto.ShapeBase):
    """
    A time zone associated with a DBInstance. This data type is an element in the
    response to the DescribeDBInstances, and the DescribeDBEngineVersions actions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timezone_name",
                "TimezoneName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the time zone.
    timezone_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpgradeTarget(autoboto.ShapeBase):
    """
    The version of the database engine that a DB instance can be upgraded to.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "engine",
                "Engine",
                autoboto.TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "auto_upgrade",
                "AutoUpgrade",
                autoboto.TypeInfo(bool),
            ),
            (
                "is_major_version_upgrade",
                "IsMajorVersionUpgrade",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the upgrade target database engine.
    engine: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version number of the upgrade target database engine.
    engine_version: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The version of the database engine that a DB instance can be upgraded to.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A value that indicates whether the target version is applied to any source
    # DB instances that have AutoMinorVersionUpgrade set to true.
    auto_upgrade: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A value that indicates whether a database engine is upgraded to a major
    # version.
    is_major_version_upgrade: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ValidDBInstanceModificationsMessage(autoboto.ShapeBase):
    """
    Information about valid modifications that you can make to your DB instance.
    Contains the result of a successful call to the
    DescribeValidDBInstanceModifications action. You can use this information when
    you call ModifyDBInstance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "storage",
                "Storage",
                autoboto.TypeInfo(typing.List[ValidStorageOptions]),
            ),
        ]

    # Valid storage options for your DB instance.
    storage: typing.List["ValidStorageOptions"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ValidStorageOptions(autoboto.ShapeBase):
    """
    Information about valid modifications that you can make to your DB instance.
    Contains the result of a successful call to the
    DescribeValidDBInstanceModifications action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "storage_type",
                "StorageType",
                autoboto.TypeInfo(str),
            ),
            (
                "storage_size",
                "StorageSize",
                autoboto.TypeInfo(typing.List[Range]),
            ),
            (
                "provisioned_iops",
                "ProvisionedIops",
                autoboto.TypeInfo(typing.List[Range]),
            ),
            (
                "iops_to_storage_ratio",
                "IopsToStorageRatio",
                autoboto.TypeInfo(typing.List[DoubleRange]),
            ),
        ]

    # The valid storage types for your DB instance. For example, gp2, io1.
    storage_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The valid range of storage in gibibytes. For example, 100 to 16384.
    storage_size: typing.List["Range"] = dataclasses.field(
        default_factory=list,
    )

    # The valid range of provisioned IOPS. For example, 1000-20000.
    provisioned_iops: typing.List["Range"] = dataclasses.field(
        default_factory=list,
    )

    # The valid range of Provisioned IOPS to gibibytes of storage multiplier. For
    # example, 3-10, which means that provisioned IOPS can be between 3 and 10
    # times storage.
    iops_to_storage_ratio: typing.List["DoubleRange"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class VpcSecurityGroupMembership(autoboto.ShapeBase):
    """
    This data type is used as a response element for queries on VPC security group
    membership.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vpc_security_group_id",
                "VpcSecurityGroupId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the VPC security group.
    vpc_security_group_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the VPC security group.
    status: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
