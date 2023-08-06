import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AccessDeniedException(autoboto.ShapeBase):
    """
    Access to a resource was denied.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Action(autoboto.ShapeBase):
    """
    Defines an action to be initiated by a trigger.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
            (
                "arguments",
                "Arguments",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "timeout",
                "Timeout",
                autoboto.TypeInfo(int),
            ),
            (
                "notification_property",
                "NotificationProperty",
                autoboto.TypeInfo(NotificationProperty),
            ),
        ]

    # The name of a job to be executed.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Arguments to be passed to the job.

    # You can specify arguments here that your own job-execution script consumes,
    # as well as arguments that AWS Glue itself consumes.

    # For information about how to specify and consume your own Job arguments,
    # see the [Calling AWS Glue APIs in
    # Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-
    # python-calling.html) topic in the developer guide.

    # For information about the key-value pairs that AWS Glue consumes to set up
    # your job, see the [Special Parameters Used by AWS
    # Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-
    # glue-arguments.html) topic in the developer guide.
    arguments: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The job run timeout in minutes. It overrides the timeout value of the job.
    timeout: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies configuration properties of a job run notification.
    notification_property: "NotificationProperty" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class AlreadyExistsException(autoboto.ShapeBase):
    """
    A resource to be created or added already exists.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BatchCreatePartitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
            (
                "partition_input_list",
                "PartitionInputList",
                autoboto.TypeInfo(typing.List[PartitionInput]),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the metadata database in which the partition is to be created.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the metadata table in which the partition is to be created.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of `PartitionInput` structures that define the partitions to be
    # created.
    partition_input_list: typing.List["PartitionInput"] = dataclasses.field(
        default_factory=list,
    )

    # The ID of the catalog in which the partion is to be created. Currently,
    # this should be the AWS account ID.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BatchCreatePartitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "errors",
                "Errors",
                autoboto.TypeInfo(typing.List[PartitionError]),
            ),
        ]

    # Errors encountered when trying to create the requested partitions.
    errors: typing.List["PartitionError"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchDeleteConnectionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_name_list",
                "ConnectionNameList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of names of the connections to delete.
    connection_name_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The ID of the Data Catalog in which the connections reside. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BatchDeleteConnectionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "succeeded",
                "Succeeded",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "errors",
                "Errors",
                autoboto.TypeInfo(typing.Dict[str, ErrorDetail]),
            ),
        ]

    # A list of names of the connection definitions that were successfully
    # deleted.
    succeeded: typing.List[str] = dataclasses.field(default_factory=list, )

    # A map of the names of connections that were not successfully deleted to
    # error details.
    errors: typing.Dict[str, "ErrorDetail"] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class BatchDeletePartitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
            (
                "partitions_to_delete",
                "PartitionsToDelete",
                autoboto.TypeInfo(typing.List[PartitionValueList]),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the catalog database in which the table in question resides.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the table where the partitions to be deleted is located.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of `PartitionInput` structures that define the partitions to be
    # deleted.
    partitions_to_delete: typing.List["PartitionValueList"] = dataclasses.field(
        default_factory=list,
    )

    # The ID of the Data Catalog where the partition to be deleted resides. If
    # none is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BatchDeletePartitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "errors",
                "Errors",
                autoboto.TypeInfo(typing.List[PartitionError]),
            ),
        ]

    # Errors encountered when trying to delete the requested partitions.
    errors: typing.List["PartitionError"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchDeleteTableRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "tables_to_delete",
                "TablesToDelete",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the catalog database where the tables to delete reside. For
    # Hive compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of the table to delete.
    tables_to_delete: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The ID of the Data Catalog where the table resides. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BatchDeleteTableResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "errors",
                "Errors",
                autoboto.TypeInfo(typing.List[TableError]),
            ),
        ]

    # A list of errors encountered in attempting to delete the specified tables.
    errors: typing.List["TableError"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchDeleteTableVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
            (
                "version_ids",
                "VersionIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The database in the catalog in which the table resides. For Hive
    # compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the table. For Hive compatibility, this name is entirely
    # lowercase.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of the IDs of versions to be deleted.
    version_ids: typing.List[str] = dataclasses.field(default_factory=list, )

    # The ID of the Data Catalog where the tables reside. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BatchDeleteTableVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "errors",
                "Errors",
                autoboto.TypeInfo(typing.List[TableVersionError]),
            ),
        ]

    # A list of errors encountered while trying to delete the specified table
    # versions.
    errors: typing.List["TableVersionError"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchGetPartitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
            (
                "partitions_to_get",
                "PartitionsToGet",
                autoboto.TypeInfo(typing.List[PartitionValueList]),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the catalog database where the partitions reside.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the partitions' table.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of partition values identifying the partitions to retrieve.
    partitions_to_get: typing.List["PartitionValueList"] = dataclasses.field(
        default_factory=list,
    )

    # The ID of the Data Catalog where the partitions in question reside. If none
    # is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BatchGetPartitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "partitions",
                "Partitions",
                autoboto.TypeInfo(typing.List[Partition]),
            ),
            (
                "unprocessed_keys",
                "UnprocessedKeys",
                autoboto.TypeInfo(typing.List[PartitionValueList]),
            ),
        ]

    # A list of the requested partitions.
    partitions: typing.List["Partition"] = dataclasses.field(
        default_factory=list,
    )

    # A list of the partition values in the request for which partions were not
    # returned.
    unprocessed_keys: typing.List["PartitionValueList"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchStopJobRunError(autoboto.ShapeBase):
    """
    Records an error that occurred when attempting to stop a specified job run.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
            (
                "job_run_id",
                "JobRunId",
                autoboto.TypeInfo(str),
            ),
            (
                "error_detail",
                "ErrorDetail",
                autoboto.TypeInfo(ErrorDetail),
            ),
        ]

    # The name of the job definition used in the job run in question.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The JobRunId of the job run in question.
    job_run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies details about the error that was encountered.
    error_detail: "ErrorDetail" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class BatchStopJobRunRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
            (
                "job_run_ids",
                "JobRunIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the job definition for which to stop job runs.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of the JobRunIds that should be stopped for that job definition.
    job_run_ids: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class BatchStopJobRunResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "successful_submissions",
                "SuccessfulSubmissions",
                autoboto.TypeInfo(
                    typing.List[BatchStopJobRunSuccessfulSubmission]
                ),
            ),
            (
                "errors",
                "Errors",
                autoboto.TypeInfo(typing.List[BatchStopJobRunError]),
            ),
        ]

    # A list of the JobRuns that were successfully submitted for stopping.
    successful_submissions: typing.List["BatchStopJobRunSuccessfulSubmission"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )

    # A list of the errors that were encountered in tryng to stop JobRuns,
    # including the JobRunId for which each error was encountered and details
    # about the error.
    errors: typing.List["BatchStopJobRunError"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchStopJobRunSuccessfulSubmission(autoboto.ShapeBase):
    """
    Records a successful request to stop a specified JobRun.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
            (
                "job_run_id",
                "JobRunId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the job definition used in the job run that was stopped.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The JobRunId of the job run that was stopped.
    job_run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CatalogEntry(autoboto.ShapeBase):
    """
    Specifies a table definition in the Data Catalog.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The database in which the table metadata resides.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the table in question.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CatalogImportStatus(autoboto.ShapeBase):
    """
    A structure containing migration status information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "import_completed",
                "ImportCompleted",
                autoboto.TypeInfo(bool),
            ),
            (
                "import_time",
                "ImportTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "imported_by",
                "ImportedBy",
                autoboto.TypeInfo(str),
            ),
        ]

    # True if the migration has completed, or False otherwise.
    import_completed: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time that the migration was started.
    import_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the person who initiated the migration.
    imported_by: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Classifier(autoboto.ShapeBase):
    """
    Classifiers are triggered during a crawl task. A classifier checks whether a
    given file is in a format it can handle, and if it is, the classifier creates a
    schema in the form of a `StructType` object that matches that data format.

    You can use the standard classifiers that AWS Glue supplies, or you can write
    your own classifiers to best categorize your data sources and specify the
    appropriate schemas to use for them. A classifier can be a `grok` classifier, an
    `XML` classifier, or a `JSON` classifier, as specified in one of the fields in
    the `Classifier` object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "grok_classifier",
                "GrokClassifier",
                autoboto.TypeInfo(GrokClassifier),
            ),
            (
                "xml_classifier",
                "XMLClassifier",
                autoboto.TypeInfo(XMLClassifier),
            ),
            (
                "json_classifier",
                "JsonClassifier",
                autoboto.TypeInfo(JsonClassifier),
            ),
        ]

    # A `GrokClassifier` object.
    grok_classifier: "GrokClassifier" = dataclasses.field(
        default_factory=dict,
    )

    # An `XMLClassifier` object.
    xml_classifier: "XMLClassifier" = dataclasses.field(default_factory=dict, )

    # A `JsonClassifier` object.
    json_classifier: "JsonClassifier" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CodeGenEdge(autoboto.ShapeBase):
    """
    Represents a directional edge in a directed acyclic graph (DAG).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source",
                "Source",
                autoboto.TypeInfo(str),
            ),
            (
                "target",
                "Target",
                autoboto.TypeInfo(str),
            ),
            (
                "target_parameter",
                "TargetParameter",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the node at which the edge starts.
    source: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the node at which the edge ends.
    target: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The target of the edge.
    target_parameter: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CodeGenNode(autoboto.ShapeBase):
    """
    Represents a node in a directed acyclic graph (DAG)
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
                "node_type",
                "NodeType",
                autoboto.TypeInfo(str),
            ),
            (
                "args",
                "Args",
                autoboto.TypeInfo(typing.List[CodeGenNodeArg]),
            ),
            (
                "line_number",
                "LineNumber",
                autoboto.TypeInfo(int),
            ),
        ]

    # A node identifier that is unique within the node's graph.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of node this is.
    node_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Properties of the node, in the form of name-value pairs.
    args: typing.List["CodeGenNodeArg"] = dataclasses.field(
        default_factory=list,
    )

    # The line number of the node.
    line_number: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CodeGenNodeArg(autoboto.ShapeBase):
    """
    An argument or property of a node.
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
            (
                "param",
                "Param",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the argument or property.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The value of the argument or property.
    value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # True if the value is used as a parameter.
    param: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Column(autoboto.ShapeBase):
    """
    A column in a `Table`.
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
                "type",
                "Type",
                autoboto.TypeInfo(str),
            ),
            (
                "comment",
                "Comment",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the `Column`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The datatype of data in the `Column`.
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Free-form text comment.
    comment: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ConcurrentModificationException(autoboto.ShapeBase):
    """
    Two processes are trying to modify a resource simultaneously.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ConcurrentRunsExceededException(autoboto.ShapeBase):
    """
    Too many jobs are being run concurrently.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Condition(autoboto.ShapeBase):
    """
    Defines a condition under which a trigger fires.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logical_operator",
                "LogicalOperator",
                autoboto.TypeInfo(LogicalOperator),
            ),
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(JobRunState),
            ),
        ]

    # A logical operator.
    logical_operator: "LogicalOperator" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the Job to whose JobRuns this condition applies and on which
    # this trigger waits.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The condition state. Currently, the values supported are SUCCEEDED,
    # STOPPED, TIMEOUT and FAILED.
    state: "JobRunState" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Connection(autoboto.ShapeBase):
    """
    Defines a connection to a data source.
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
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "connection_type",
                "ConnectionType",
                autoboto.TypeInfo(ConnectionType),
            ),
            (
                "match_criteria",
                "MatchCriteria",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "connection_properties",
                "ConnectionProperties",
                autoboto.TypeInfo(typing.Dict[ConnectionPropertyKey, str]),
            ),
            (
                "physical_connection_requirements",
                "PhysicalConnectionRequirements",
                autoboto.TypeInfo(PhysicalConnectionRequirements),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_time",
                "LastUpdatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_by",
                "LastUpdatedBy",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the connection definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Description of the connection.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of the connection. Currently, only JDBC is supported; SFTP is not
    # supported.
    connection_type: "ConnectionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of criteria that can be used in selecting this connection.
    match_criteria: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of key-value pairs used as parameters for this connection.
    connection_properties: typing.Dict["ConnectionPropertyKey", str
                                      ] = dataclasses.field(
                                          default=autoboto.ShapeBase._NOT_SET,
                                      )

    # A map of physical connection requirements, such as VPC and SecurityGroup,
    # needed for making this connection successfully.
    physical_connection_requirements: "PhysicalConnectionRequirements" = dataclasses.field(
        default_factory=dict,
    )

    # The time this connection definition was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The last time this connection definition was updated.
    last_updated_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The user, group or role that last updated this connection definition.
    last_updated_by: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ConnectionInput(autoboto.ShapeBase):
    """
    A structure used to specify a connection to create or update.
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
                "connection_type",
                "ConnectionType",
                autoboto.TypeInfo(ConnectionType),
            ),
            (
                "connection_properties",
                "ConnectionProperties",
                autoboto.TypeInfo(typing.Dict[ConnectionPropertyKey, str]),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "match_criteria",
                "MatchCriteria",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "physical_connection_requirements",
                "PhysicalConnectionRequirements",
                autoboto.TypeInfo(PhysicalConnectionRequirements),
            ),
        ]

    # The name of the connection.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of the connection. Currently, only JDBC is supported; SFTP is not
    # supported.
    connection_type: "ConnectionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of key-value pairs used as parameters for this connection.
    connection_properties: typing.Dict["ConnectionPropertyKey", str
                                      ] = dataclasses.field(
                                          default=autoboto.ShapeBase._NOT_SET,
                                      )

    # Description of the connection.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of criteria that can be used in selecting this connection.
    match_criteria: typing.List[str] = dataclasses.field(default_factory=list, )

    # A map of physical connection requirements, such as VPC and SecurityGroup,
    # needed for making this connection successfully.
    physical_connection_requirements: "PhysicalConnectionRequirements" = dataclasses.field(
        default_factory=dict,
    )


class ConnectionPropertyKey(Enum):
    HOST = "HOST"
    PORT = "PORT"
    USERNAME = "USERNAME"
    PASSWORD = "PASSWORD"
    JDBC_DRIVER_JAR_URI = "JDBC_DRIVER_JAR_URI"
    JDBC_DRIVER_CLASS_NAME = "JDBC_DRIVER_CLASS_NAME"
    JDBC_ENGINE = "JDBC_ENGINE"
    JDBC_ENGINE_VERSION = "JDBC_ENGINE_VERSION"
    CONFIG_FILES = "CONFIG_FILES"
    INSTANCE_ID = "INSTANCE_ID"
    JDBC_CONNECTION_URL = "JDBC_CONNECTION_URL"


class ConnectionType(Enum):
    JDBC = "JDBC"
    SFTP = "SFTP"


@dataclasses.dataclass
class ConnectionsList(autoboto.ShapeBase):
    """
    Specifies the connections used by a job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connections",
                "Connections",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A list of connections used by the job.
    connections: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class Crawler(autoboto.ShapeBase):
    """
    Specifies a crawler program that examines a data source and uses classifiers to
    try to determine its schema. If successful, the crawler records metadata
    concerning the data source in the AWS Glue Data Catalog.
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
                "role",
                "Role",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(CrawlerTargets),
            ),
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "classifiers",
                "Classifiers",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "schema_change_policy",
                "SchemaChangePolicy",
                autoboto.TypeInfo(SchemaChangePolicy),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(CrawlerState),
            ),
            (
                "table_prefix",
                "TablePrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                autoboto.TypeInfo(Schedule),
            ),
            (
                "crawl_elapsed_time",
                "CrawlElapsedTime",
                autoboto.TypeInfo(int),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated",
                "LastUpdated",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_crawl",
                "LastCrawl",
                autoboto.TypeInfo(LastCrawlInfo),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
            (
                "configuration",
                "Configuration",
                autoboto.TypeInfo(str),
            ),
        ]

    # The crawler name.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The IAM role (or ARN of an IAM role) used to access customer resources,
    # such as data in Amazon S3.
    role: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A collection of targets to crawl.
    targets: "CrawlerTargets" = dataclasses.field(default_factory=dict, )

    # The database where metadata is written by this crawler.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the crawler.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of custom classifiers associated with the crawler.
    classifiers: typing.List[str] = dataclasses.field(default_factory=list, )

    # Sets the behavior when the crawler finds a changed or deleted object.
    schema_change_policy: "SchemaChangePolicy" = dataclasses.field(
        default_factory=dict,
    )

    # Indicates whether the crawler is running, or whether a run is pending.
    state: "CrawlerState" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The prefix added to the names of tables that are created.
    table_prefix: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # For scheduled crawlers, the schedule when the crawler runs.
    schedule: "Schedule" = dataclasses.field(default_factory=dict, )

    # If the crawler is running, contains the total time elapsed since the last
    # crawl began.
    crawl_elapsed_time: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time when the crawler was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time the crawler was last updated.
    last_updated: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the last crawl, and potentially error information if an error
    # occurred.
    last_crawl: "LastCrawlInfo" = dataclasses.field(default_factory=dict, )

    # The version of the crawler.
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Crawler configuration information. This versioned JSON string allows users
    # to specify aspects of a crawler's behavior. For more information, see
    # [Configuring a Crawler](http://docs.aws.amazon.com/glue/latest/dg/crawler-
    # configuration.html).
    configuration: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CrawlerMetrics(autoboto.ShapeBase):
    """
    Metrics for a specified crawler.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "crawler_name",
                "CrawlerName",
                autoboto.TypeInfo(str),
            ),
            (
                "time_left_seconds",
                "TimeLeftSeconds",
                autoboto.TypeInfo(float),
            ),
            (
                "still_estimating",
                "StillEstimating",
                autoboto.TypeInfo(bool),
            ),
            (
                "last_runtime_seconds",
                "LastRuntimeSeconds",
                autoboto.TypeInfo(float),
            ),
            (
                "median_runtime_seconds",
                "MedianRuntimeSeconds",
                autoboto.TypeInfo(float),
            ),
            (
                "tables_created",
                "TablesCreated",
                autoboto.TypeInfo(int),
            ),
            (
                "tables_updated",
                "TablesUpdated",
                autoboto.TypeInfo(int),
            ),
            (
                "tables_deleted",
                "TablesDeleted",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the crawler.
    crawler_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The estimated time left to complete a running crawl.
    time_left_seconds: float = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # True if the crawler is still estimating how long it will take to complete
    # this run.
    still_estimating: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The duration of the crawler's most recent run, in seconds.
    last_runtime_seconds: float = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The median duration of this crawler's runs, in seconds.
    median_runtime_seconds: float = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of tables created by this crawler.
    tables_created: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of tables updated by this crawler.
    tables_updated: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of tables deleted by this crawler.
    tables_deleted: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CrawlerNotRunningException(autoboto.ShapeBase):
    """
    The specified crawler is not running.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CrawlerRunningException(autoboto.ShapeBase):
    """
    The operation cannot be performed because the crawler is already running.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class CrawlerState(Enum):
    READY = "READY"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"


@dataclasses.dataclass
class CrawlerStoppingException(autoboto.ShapeBase):
    """
    The specified crawler is stopping.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CrawlerTargets(autoboto.ShapeBase):
    """
    Specifies data stores to crawl.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_targets",
                "S3Targets",
                autoboto.TypeInfo(typing.List[S3Target]),
            ),
            (
                "jdbc_targets",
                "JdbcTargets",
                autoboto.TypeInfo(typing.List[JdbcTarget]),
            ),
            (
                "dynamo_db_targets",
                "DynamoDBTargets",
                autoboto.TypeInfo(typing.List[DynamoDBTarget]),
            ),
        ]

    # Specifies Amazon S3 targets.
    s3_targets: typing.List["S3Target"] = dataclasses.field(
        default_factory=list,
    )

    # Specifies JDBC targets.
    jdbc_targets: typing.List["JdbcTarget"] = dataclasses.field(
        default_factory=list,
    )

    # Specifies DynamoDB targets.
    dynamo_db_targets: typing.List["DynamoDBTarget"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateClassifierRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "grok_classifier",
                "GrokClassifier",
                autoboto.TypeInfo(CreateGrokClassifierRequest),
            ),
            (
                "xml_classifier",
                "XMLClassifier",
                autoboto.TypeInfo(CreateXMLClassifierRequest),
            ),
            (
                "json_classifier",
                "JsonClassifier",
                autoboto.TypeInfo(CreateJsonClassifierRequest),
            ),
        ]

    # A `GrokClassifier` object specifying the classifier to create.
    grok_classifier: "CreateGrokClassifierRequest" = dataclasses.field(
        default_factory=dict,
    )

    # An `XMLClassifier` object specifying the classifier to create.
    xml_classifier: "CreateXMLClassifierRequest" = dataclasses.field(
        default_factory=dict,
    )

    # A `JsonClassifier` object specifying the classifier to create.
    json_classifier: "CreateJsonClassifierRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateClassifierResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateConnectionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_input",
                "ConnectionInput",
                autoboto.TypeInfo(ConnectionInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A `ConnectionInput` object defining the connection to create.
    connection_input: "ConnectionInput" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the Data Catalog in which to create the connection. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateConnectionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateCrawlerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "role",
                "Role",
                autoboto.TypeInfo(str),
            ),
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(CrawlerTargets),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                autoboto.TypeInfo(str),
            ),
            (
                "classifiers",
                "Classifiers",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "table_prefix",
                "TablePrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "schema_change_policy",
                "SchemaChangePolicy",
                autoboto.TypeInfo(SchemaChangePolicy),
            ),
            (
                "configuration",
                "Configuration",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the new crawler.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The IAM role (or ARN of an IAM role) used by the new crawler to access
    # customer resources.
    role: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The AWS Glue database where results are written, such as:
    # `arn:aws:daylight:us-east-1::database/sometable/*`.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of collection of targets to crawl.
    targets: "CrawlerTargets" = dataclasses.field(default_factory=dict, )

    # A description of the new crawler.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A `cron` expression used to specify the schedule (see [Time-Based Schedules
    # for Jobs and Crawlers](http://docs.aws.amazon.com/glue/latest/dg/monitor-
    # data-warehouse-schedule.html). For example, to run something every day at
    # 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
    schedule: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of custom classifiers that the user has registered. By default, all
    # built-in classifiers are included in a crawl, but these custom classifiers
    # always override the default classifiers for a given classification.
    classifiers: typing.List[str] = dataclasses.field(default_factory=list, )

    # The table prefix used for catalog tables that are created.
    table_prefix: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Policy for the crawler's update and deletion behavior.
    schema_change_policy: "SchemaChangePolicy" = dataclasses.field(
        default_factory=dict,
    )

    # Crawler configuration information. This versioned JSON string allows users
    # to specify aspects of a crawler's behavior. For more information, see
    # [Configuring a Crawler](http://docs.aws.amazon.com/glue/latest/dg/crawler-
    # configuration.html).
    configuration: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateCrawlerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateDatabaseRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_input",
                "DatabaseInput",
                autoboto.TypeInfo(DatabaseInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A `DatabaseInput` object defining the metadata database to create in the
    # catalog.
    database_input: "DatabaseInput" = dataclasses.field(default_factory=dict, )

    # The ID of the Data Catalog in which to create the database. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateDatabaseResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateDevEndpointRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "subnet_id",
                "SubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "public_key",
                "PublicKey",
                autoboto.TypeInfo(str),
            ),
            (
                "public_keys",
                "PublicKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "number_of_nodes",
                "NumberOfNodes",
                autoboto.TypeInfo(int),
            ),
            (
                "extra_python_libs_s3_path",
                "ExtraPythonLibsS3Path",
                autoboto.TypeInfo(str),
            ),
            (
                "extra_jars_s3_path",
                "ExtraJarsS3Path",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name to be assigned to the new DevEndpoint.
    endpoint_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IAM role for the DevEndpoint.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Security group IDs for the security groups to be used by the new
    # DevEndpoint.
    security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The subnet ID for the new DevEndpoint to use.
    subnet_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The public key to be used by this DevEndpoint for authentication. This
    # attribute is provided for backward compatibility, as the recommended
    # attribute to use is public keys.
    public_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of public keys to be used by the DevEndpoints for authentication.
    # The use of this attribute is preferred over a single public key because the
    # public keys allow you to have a different private key per client.

    # If you previously created an endpoint with a public key, you must remove
    # that key to be able to set a list of public keys: call the
    # `UpdateDevEndpoint` API with the public key content in the
    # `deletePublicKeys` attribute, and the list of new keys in the
    # `addPublicKeys` attribute.
    public_keys: typing.List[str] = dataclasses.field(default_factory=list, )

    # The number of AWS Glue Data Processing Units (DPUs) to allocate to this
    # DevEndpoint.
    number_of_nodes: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Path(s) to one or more Python libraries in an S3 bucket that should be
    # loaded in your DevEndpoint. Multiple values must be complete paths
    # separated by a comma.

    # Please note that only pure Python libraries can currently be used on a
    # DevEndpoint. Libraries that rely on C extensions, such as the
    # [pandas](http://pandas.pydata.org/) Python data analysis library, are not
    # yet supported.
    extra_python_libs_s3_path: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Path to one or more Java Jars in an S3 bucket that should be loaded in your
    # DevEndpoint.
    extra_jars_s3_path: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateDevEndpointResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "subnet_id",
                "SubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "yarn_endpoint_address",
                "YarnEndpointAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "zeppelin_remote_spark_interpreter_port",
                "ZeppelinRemoteSparkInterpreterPort",
                autoboto.TypeInfo(int),
            ),
            (
                "number_of_nodes",
                "NumberOfNodes",
                autoboto.TypeInfo(int),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                autoboto.TypeInfo(str),
            ),
            (
                "extra_python_libs_s3_path",
                "ExtraPythonLibsS3Path",
                autoboto.TypeInfo(str),
            ),
            (
                "extra_jars_s3_path",
                "ExtraJarsS3Path",
                autoboto.TypeInfo(str),
            ),
            (
                "failure_reason",
                "FailureReason",
                autoboto.TypeInfo(str),
            ),
            (
                "created_timestamp",
                "CreatedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The name assigned to the new DevEndpoint.
    endpoint_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The current status of the new DevEndpoint.
    status: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The security groups assigned to the new DevEndpoint.
    security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The subnet ID assigned to the new DevEndpoint.
    subnet_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The AWS ARN of the role assigned to the new DevEndpoint.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The address of the YARN endpoint used by this DevEndpoint.
    yarn_endpoint_address: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Apache Zeppelin port for the remote Apache Spark interpreter.
    zeppelin_remote_spark_interpreter_port: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of AWS Glue Data Processing Units (DPUs) allocated to this
    # DevEndpoint.
    number_of_nodes: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS availability zone where this DevEndpoint is located.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the VPC used by this DevEndpoint.
    vpc_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Path(s) to one or more Python libraries in an S3 bucket that will be loaded
    # in your DevEndpoint.
    extra_python_libs_s3_path: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Path to one or more Java Jars in an S3 bucket that will be loaded in your
    # DevEndpoint.
    extra_jars_s3_path: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The reason for a current failure in this DevEndpoint.
    failure_reason: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The point in time at which this DevEndpoint was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateGrokClassifierRequest(autoboto.ShapeBase):
    """
    Specifies a `grok` classifier for `CreateClassifier` to create.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "classification",
                "Classification",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "grok_pattern",
                "GrokPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_patterns",
                "CustomPatterns",
                autoboto.TypeInfo(str),
            ),
        ]

    # An identifier of the data format that the classifier matches, such as
    # Twitter, JSON, Omniture logs, Amazon CloudWatch Logs, and so on.
    classification: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the new classifier.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The grok pattern used by this classifier.
    grok_pattern: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Optional custom grok patterns used by this classifier.
    custom_patterns: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "role",
                "Role",
                autoboto.TypeInfo(str),
            ),
            (
                "command",
                "Command",
                autoboto.TypeInfo(JobCommand),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "log_uri",
                "LogUri",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_property",
                "ExecutionProperty",
                autoboto.TypeInfo(ExecutionProperty),
            ),
            (
                "default_arguments",
                "DefaultArguments",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "connections",
                "Connections",
                autoboto.TypeInfo(ConnectionsList),
            ),
            (
                "max_retries",
                "MaxRetries",
                autoboto.TypeInfo(int),
            ),
            (
                "allocated_capacity",
                "AllocatedCapacity",
                autoboto.TypeInfo(int),
            ),
            (
                "timeout",
                "Timeout",
                autoboto.TypeInfo(int),
            ),
            (
                "notification_property",
                "NotificationProperty",
                autoboto.TypeInfo(NotificationProperty),
            ),
        ]

    # The name you assign to this job definition. It must be unique in your
    # account.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name or ARN of the IAM role associated with this job.
    role: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The JobCommand that executes this job.
    command: "JobCommand" = dataclasses.field(default_factory=dict, )

    # Description of the job being defined.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # This field is reserved for future use.
    log_uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An ExecutionProperty specifying the maximum number of concurrent runs
    # allowed for this job.
    execution_property: "ExecutionProperty" = dataclasses.field(
        default_factory=dict,
    )

    # The default arguments for this job.

    # You can specify arguments here that your own job-execution script consumes,
    # as well as arguments that AWS Glue itself consumes.

    # For information about how to specify and consume your own Job arguments,
    # see the [Calling AWS Glue APIs in
    # Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-
    # python-calling.html) topic in the developer guide.

    # For information about the key-value pairs that AWS Glue consumes to set up
    # your job, see the [Special Parameters Used by AWS
    # Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-
    # glue-arguments.html) topic in the developer guide.
    default_arguments: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The connections used for this job.
    connections: "ConnectionsList" = dataclasses.field(default_factory=dict, )

    # The maximum number of times to retry this job if it fails.
    max_retries: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of AWS Glue data processing units (DPUs) to allocate to this
    # Job. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a
    # relative measure of processing power that consists of 4 vCPUs of compute
    # capacity and 16 GB of memory. For more information, see the [AWS Glue
    # pricing page](https://aws.amazon.com/glue/pricing/).
    allocated_capacity: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The job timeout in minutes. The default is 2880 minutes (48 hours).
    timeout: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies configuration properties of a job notification.
    notification_property: "NotificationProperty" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateJobResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique name that was provided for this job definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateJsonClassifierRequest(autoboto.ShapeBase):
    """
    Specifies a JSON classifier for `CreateClassifier` to create.
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
                "json_path",
                "JsonPath",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the classifier.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A `JsonPath` string defining the JSON data for the classifier to classify.
    # AWS Glue supports a subset of JsonPath, as described in [Writing JsonPath
    # Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-
    # classifier.html#custom-classifier-json).
    json_path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreatePartitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
            (
                "partition_input",
                "PartitionInput",
                autoboto.TypeInfo(PartitionInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the metadata database in which the partition is to be created.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the metadata table in which the partition is to be created.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A `PartitionInput` structure defining the partition to be created.
    partition_input: "PartitionInput" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the catalog in which the partion is to be created. Currently,
    # this should be the AWS account ID.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreatePartitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateScriptRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dag_nodes",
                "DagNodes",
                autoboto.TypeInfo(typing.List[CodeGenNode]),
            ),
            (
                "dag_edges",
                "DagEdges",
                autoboto.TypeInfo(typing.List[CodeGenEdge]),
            ),
            (
                "language",
                "Language",
                autoboto.TypeInfo(Language),
            ),
        ]

    # A list of the nodes in the DAG.
    dag_nodes: typing.List["CodeGenNode"] = dataclasses.field(
        default_factory=list,
    )

    # A list of the edges in the DAG.
    dag_edges: typing.List["CodeGenEdge"] = dataclasses.field(
        default_factory=list,
    )

    # The programming language of the resulting code from the DAG.
    language: "Language" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateScriptResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "python_script",
                "PythonScript",
                autoboto.TypeInfo(str),
            ),
            (
                "scala_code",
                "ScalaCode",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Python script generated from the DAG.
    python_script: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Scala code generated from the DAG.
    scala_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateTableRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_input",
                "TableInput",
                autoboto.TypeInfo(TableInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The catalog database in which to create the new table. For Hive
    # compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The `TableInput` object that defines the metadata table to create in the
    # catalog.
    table_input: "TableInput" = dataclasses.field(default_factory=dict, )

    # The ID of the Data Catalog in which to create the `Table`. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateTableResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateTriggerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(TriggerType),
            ),
            (
                "actions",
                "Actions",
                autoboto.TypeInfo(typing.List[Action]),
            ),
            (
                "schedule",
                "Schedule",
                autoboto.TypeInfo(str),
            ),
            (
                "predicate",
                "Predicate",
                autoboto.TypeInfo(Predicate),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "start_on_creation",
                "StartOnCreation",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the trigger.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of the new trigger.
    type: "TriggerType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The actions initiated by this trigger when it fires.
    actions: typing.List["Action"] = dataclasses.field(default_factory=list, )

    # A `cron` expression used to specify the schedule (see [Time-Based Schedules
    # for Jobs and Crawlers](http://docs.aws.amazon.com/glue/latest/dg/monitor-
    # data-warehouse-schedule.html). For example, to run something every day at
    # 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.

    # This field is required when the trigger type is SCHEDULED.
    schedule: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A predicate to specify when the new trigger should fire.

    # This field is required when the trigger type is CONDITIONAL.
    predicate: "Predicate" = dataclasses.field(default_factory=dict, )

    # A description of the new trigger.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Set to true to start SCHEDULED and CONDITIONAL triggers when created. True
    # not supported for ON_DEMAND triggers.
    start_on_creation: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateTriggerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the trigger.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateUserDefinedFunctionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "function_input",
                "FunctionInput",
                autoboto.TypeInfo(UserDefinedFunctionInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the catalog database in which to create the function.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A `FunctionInput` object that defines the function to create in the Data
    # Catalog.
    function_input: "UserDefinedFunctionInput" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the Data Catalog in which to create the function. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateUserDefinedFunctionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateXMLClassifierRequest(autoboto.ShapeBase):
    """
    Specifies an XML classifier for `CreateClassifier` to create.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "classification",
                "Classification",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "row_tag",
                "RowTag",
                autoboto.TypeInfo(str),
            ),
        ]

    # An identifier of the data format that the classifier matches.
    classification: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the classifier.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The XML tag designating the element that contains each record in an XML
    # document being parsed. Note that this cannot identify a self-closing
    # element (closed by `/>`). An empty row element that contains only
    # attributes can be parsed as long as it ends with a closing tag (for
    # example, `<row item_a="A" item_b="B"></row>` is okay, but `<row item_a="A"
    # item_b="B" />` is not).
    row_tag: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Database(autoboto.ShapeBase):
    """
    The `Database` object represents a logical grouping of tables that may reside in
    a Hive metastore or an RDBMS.
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
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "location_uri",
                "LocationUri",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "create_time",
                "CreateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # Name of the database. For Hive compatibility, this is folded to lowercase
    # when it is stored.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Description of the database.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The location of the database (for example, an HDFS path).
    location_uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of key-value pairs that define parameters and properties of the
    # database.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time at which the metadata database was created in the catalog.
    create_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DatabaseInput(autoboto.ShapeBase):
    """
    The structure used to create or update a database.
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
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "location_uri",
                "LocationUri",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Name of the database. For Hive compatibility, this is folded to lowercase
    # when it is stored.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Description of the database
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The location of the database (for example, an HDFS path).
    location_uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of key-value pairs that define parameters and properties of the
    # database.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class DeleteBehavior(Enum):
    LOG = "LOG"
    DELETE_FROM_DATABASE = "DELETE_FROM_DATABASE"
    DEPRECATE_IN_DATABASE = "DEPRECATE_IN_DATABASE"


@dataclasses.dataclass
class DeleteClassifierRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the classifier to remove.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteClassifierResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteConnectionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_name",
                "ConnectionName",
                autoboto.TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the connection to delete.
    connection_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the Data Catalog in which the connection resides. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteConnectionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteCrawlerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the crawler to remove.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteCrawlerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteDatabaseRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the Database to delete. For Hive compatibility, this must be
    # all lowercase.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the Data Catalog in which the database resides. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteDatabaseResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteDevEndpointRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the DevEndpoint.
    endpoint_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteDevEndpointResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the job definition to delete.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteJobResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the job definition that was deleted.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeletePartitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
            (
                "partition_values",
                "PartitionValues",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the catalog database in which the table in question resides.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the table where the partition to be deleted is located.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The values that define the partition.
    partition_values: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The ID of the Data Catalog where the partition to be deleted resides. If
    # none is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeletePartitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteTableRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the catalog database in which the table resides. For Hive
    # compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the table to be deleted. For Hive compatibility, this name is
    # entirely lowercase.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the Data Catalog where the table resides. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteTableResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteTableVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The database in the catalog in which the table resides. For Hive
    # compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the table. For Hive compatibility, this name is entirely
    # lowercase.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the table version to be deleted.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the Data Catalog where the tables reside. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteTableVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteTriggerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the trigger to delete.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteTriggerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the trigger that was deleted.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteUserDefinedFunctionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "function_name",
                "FunctionName",
                autoboto.TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the catalog database where the function is located.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the function definition to be deleted.
    function_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the Data Catalog where the function to be deleted is located. If
    # none is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteUserDefinedFunctionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DevEndpoint(autoboto.ShapeBase):
    """
    A development endpoint where a developer can remotely debug ETL scripts.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "subnet_id",
                "SubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "yarn_endpoint_address",
                "YarnEndpointAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "private_address",
                "PrivateAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "zeppelin_remote_spark_interpreter_port",
                "ZeppelinRemoteSparkInterpreterPort",
                autoboto.TypeInfo(int),
            ),
            (
                "public_address",
                "PublicAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(str),
            ),
            (
                "number_of_nodes",
                "NumberOfNodes",
                autoboto.TypeInfo(int),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                autoboto.TypeInfo(str),
            ),
            (
                "extra_python_libs_s3_path",
                "ExtraPythonLibsS3Path",
                autoboto.TypeInfo(str),
            ),
            (
                "extra_jars_s3_path",
                "ExtraJarsS3Path",
                autoboto.TypeInfo(str),
            ),
            (
                "failure_reason",
                "FailureReason",
                autoboto.TypeInfo(str),
            ),
            (
                "last_update_status",
                "LastUpdateStatus",
                autoboto.TypeInfo(str),
            ),
            (
                "created_timestamp",
                "CreatedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_timestamp",
                "LastModifiedTimestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "public_key",
                "PublicKey",
                autoboto.TypeInfo(str),
            ),
            (
                "public_keys",
                "PublicKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the DevEndpoint.
    endpoint_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS ARN of the IAM role used in this DevEndpoint.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of security group identifiers used in this DevEndpoint.
    security_group_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The subnet ID for this DevEndpoint.
    subnet_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The YARN endpoint address used by this DevEndpoint.
    yarn_endpoint_address: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A private DNS to access the DevEndpoint within a VPC, if the DevEndpoint is
    # created within one.
    private_address: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Apache Zeppelin port for the remote Apache Spark interpreter.
    zeppelin_remote_spark_interpreter_port: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The public VPC address used by this DevEndpoint.
    public_address: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The current status of this DevEndpoint.
    status: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of AWS Glue Data Processing Units (DPUs) allocated to this
    # DevEndpoint.
    number_of_nodes: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS availability zone where this DevEndpoint is located.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the virtual private cloud (VPC) used by this DevEndpoint.
    vpc_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Path(s) to one or more Python libraries in an S3 bucket that should be
    # loaded in your DevEndpoint. Multiple values must be complete paths
    # separated by a comma.

    # Please note that only pure Python libraries can currently be used on a
    # DevEndpoint. Libraries that rely on C extensions, such as the
    # [pandas](http://pandas.pydata.org/) Python data analysis library, are not
    # yet supported.
    extra_python_libs_s3_path: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Path to one or more Java Jars in an S3 bucket that should be loaded in your
    # DevEndpoint.

    # Please note that only pure Java/Scala libraries can currently be used on a
    # DevEndpoint.
    extra_jars_s3_path: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The reason for a current failure in this DevEndpoint.
    failure_reason: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The status of the last update.
    last_update_status: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The point in time at which this DevEndpoint was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The point in time at which this DevEndpoint was last modified.
    last_modified_timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The public key to be used by this DevEndpoint for authentication. This
    # attribute is provided for backward compatibility, as the recommended
    # attribute to use is public keys.
    public_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of public keys to be used by the DevEndpoints for authentication.
    # The use of this attribute is preferred over a single public key because the
    # public keys allow you to have a different private key per client.

    # If you previously created an endpoint with a public key, you must remove
    # that key to be able to set a list of public keys: call the
    # `UpdateDevEndpoint` API with the public key content in the
    # `deletePublicKeys` attribute, and the list of new keys in the
    # `addPublicKeys` attribute.
    public_keys: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DevEndpointCustomLibraries(autoboto.ShapeBase):
    """
    Custom libraries to be loaded into a DevEndpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "extra_python_libs_s3_path",
                "ExtraPythonLibsS3Path",
                autoboto.TypeInfo(str),
            ),
            (
                "extra_jars_s3_path",
                "ExtraJarsS3Path",
                autoboto.TypeInfo(str),
            ),
        ]

    # Path(s) to one or more Python libraries in an S3 bucket that should be
    # loaded in your DevEndpoint. Multiple values must be complete paths
    # separated by a comma.

    # Please note that only pure Python libraries can currently be used on a
    # DevEndpoint. Libraries that rely on C extensions, such as the
    # [pandas](http://pandas.pydata.org/) Python data analysis library, are not
    # yet supported.
    extra_python_libs_s3_path: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Path to one or more Java Jars in an S3 bucket that should be loaded in your
    # DevEndpoint.

    # Please note that only pure Java/Scala libraries can currently be used on a
    # DevEndpoint.
    extra_jars_s3_path: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DynamoDBTarget(autoboto.ShapeBase):
    """
    Specifies a DynamoDB table to crawl.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the DynamoDB table to crawl.
    path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EntityNotFoundException(autoboto.ShapeBase):
    """
    A specified entity does not exist
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ErrorDetail(autoboto.ShapeBase):
    """
    Contains details about an error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The code associated with this error.
    error_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A message describing the error.
    error_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ExecutionProperty(autoboto.ShapeBase):
    """
    An execution property of a job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_concurrent_runs",
                "MaxConcurrentRuns",
                autoboto.TypeInfo(int),
            ),
        ]

    # The maximum number of concurrent runs allowed for the job. The default is
    # 1. An error is returned when this threshold is reached. The maximum value
    # you can specify is controlled by a service limit.
    max_concurrent_runs: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetCatalogImportStatusRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the catalog to migrate. Currently, this should be the AWS account
    # ID.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCatalogImportStatusResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "import_status",
                "ImportStatus",
                autoboto.TypeInfo(CatalogImportStatus),
            ),
        ]

    # The status of the specified catalog migration.
    import_status: "CatalogImportStatus" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetClassifierRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the classifier to retrieve.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetClassifierResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "classifier",
                "Classifier",
                autoboto.TypeInfo(Classifier),
            ),
        ]

    # The requested classifier.
    classifier: "Classifier" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetClassifiersRequest(autoboto.ShapeBase):
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

    # Size of the list to return (optional).
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An optional continuation token.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetClassifiersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "classifiers",
                "Classifiers",
                autoboto.TypeInfo(typing.List[Classifier]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The requested list of classifier objects.
    classifiers: typing.List["Classifier"] = dataclasses.field(
        default_factory=list,
    )

    # A continuation token.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetConnectionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the connection definition to retrieve.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the Data Catalog in which the connection resides. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetConnectionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection",
                "Connection",
                autoboto.TypeInfo(Connection),
            ),
        ]

    # The requested connection definition.
    connection: "Connection" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetConnectionsFilter(autoboto.ShapeBase):
    """
    Filters the connection definitions returned by the `GetConnections` API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "match_criteria",
                "MatchCriteria",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "connection_type",
                "ConnectionType",
                autoboto.TypeInfo(ConnectionType),
            ),
        ]

    # A criteria string that must match the criteria recorded in the connection
    # definition for that connection definition to be returned.
    match_criteria: typing.List[str] = dataclasses.field(default_factory=list, )

    # The type of connections to return. Currently, only JDBC is supported; SFTP
    # is not supported.
    connection_type: "ConnectionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetConnectionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
            (
                "filter",
                "Filter",
                autoboto.TypeInfo(GetConnectionsFilter),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the Data Catalog in which the connections reside. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A filter that controls which connections will be returned.
    filter: "GetConnectionsFilter" = dataclasses.field(default_factory=dict, )

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of connections to return in one response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetConnectionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_list",
                "ConnectionList",
                autoboto.TypeInfo(typing.List[Connection]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of requested connection definitions.
    connection_list: typing.List["Connection"] = dataclasses.field(
        default_factory=list,
    )

    # A continuation token, if the list of connections returned does not include
    # the last of the filtered connections.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCrawlerMetricsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "crawler_name_list",
                "CrawlerNameList",
                autoboto.TypeInfo(typing.List[str]),
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

    # A list of the names of crawlers about which to retrieve metrics.
    crawler_name_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The maximum size of a list to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCrawlerMetricsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "crawler_metrics_list",
                "CrawlerMetricsList",
                autoboto.TypeInfo(typing.List[CrawlerMetrics]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of metrics for the specified crawler.
    crawler_metrics_list: typing.List["CrawlerMetrics"] = dataclasses.field(
        default_factory=list,
    )

    # A continuation token, if the returned list does not contain the last metric
    # available.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCrawlerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the crawler to retrieve metadata for.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCrawlerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "crawler",
                "Crawler",
                autoboto.TypeInfo(Crawler),
            ),
        ]

    # The metadata for the specified crawler.
    crawler: "Crawler" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetCrawlersRequest(autoboto.ShapeBase):
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

    # The number of crawlers to return on each call.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A continuation token, if this is a continuation request.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetCrawlersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "crawlers",
                "Crawlers",
                autoboto.TypeInfo(typing.List[Crawler]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of crawler metadata.
    crawlers: typing.List["Crawler"] = dataclasses.field(default_factory=list, )

    # A continuation token, if the returned list has not reached the end of those
    # defined in this customer account.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDatabaseRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the database to retrieve. For Hive compatibility, this should
    # be all lowercase.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the Data Catalog in which the database resides. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDatabaseResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database",
                "Database",
                autoboto.TypeInfo(Database),
            ),
        ]

    # The definition of the specified database in the catalog.
    database: "Database" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetDatabasesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID of the Data Catalog from which to retrieve `Databases`. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of databases to return in one response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDatabasesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_list",
                "DatabaseList",
                autoboto.TypeInfo(typing.List[Database]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of `Database` objects from the specified catalog.
    database_list: typing.List["Database"] = dataclasses.field(
        default_factory=list,
    )

    # A continuation token for paginating the returned list of tokens, returned
    # if the current segment of the list is not the last.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDataflowGraphRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "python_script",
                "PythonScript",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Python script to transform.
    python_script: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetDataflowGraphResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dag_nodes",
                "DagNodes",
                autoboto.TypeInfo(typing.List[CodeGenNode]),
            ),
            (
                "dag_edges",
                "DagEdges",
                autoboto.TypeInfo(typing.List[CodeGenEdge]),
            ),
        ]

    # A list of the nodes in the resulting DAG.
    dag_nodes: typing.List["CodeGenNode"] = dataclasses.field(
        default_factory=list,
    )

    # A list of the edges in the resulting DAG.
    dag_edges: typing.List["CodeGenEdge"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetDevEndpointRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the DevEndpoint for which to retrieve information.
    endpoint_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetDevEndpointResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dev_endpoint",
                "DevEndpoint",
                autoboto.TypeInfo(DevEndpoint),
            ),
        ]

    # A DevEndpoint definition.
    dev_endpoint: "DevEndpoint" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetDevEndpointsRequest(autoboto.ShapeBase):
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

    # The maximum size of information to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDevEndpointsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dev_endpoints",
                "DevEndpoints",
                autoboto.TypeInfo(typing.List[DevEndpoint]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of DevEndpoint definitions.
    dev_endpoints: typing.List["DevEndpoint"] = dataclasses.field(
        default_factory=list,
    )

    # A continuation token, if not all DevEndpoint definitions have yet been
    # returned.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the job definition to retrieve.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetJobResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job",
                "Job",
                autoboto.TypeInfo(Job),
            ),
        ]

    # The requested job definition.
    job: "Job" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetJobRunRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
            (
                "run_id",
                "RunId",
                autoboto.TypeInfo(str),
            ),
            (
                "predecessors_included",
                "PredecessorsIncluded",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Name of the job definition being run.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the job run.
    run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # True if a list of predecessor runs should be returned.
    predecessors_included: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetJobRunResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_run",
                "JobRun",
                autoboto.TypeInfo(JobRun),
            ),
        ]

    # The requested job-run metadata.
    job_run: "JobRun" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetJobRunsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the job definition for which to retrieve all job runs.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum size of the response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetJobRunsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_runs",
                "JobRuns",
                autoboto.TypeInfo(typing.List[JobRun]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of job-run metatdata objects.
    job_runs: typing.List["JobRun"] = dataclasses.field(default_factory=list, )

    # A continuation token, if not all reequested job runs have been returned.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetJobsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum size of the response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetJobsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "jobs",
                "Jobs",
                autoboto.TypeInfo(typing.List[Job]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of job definitions.
    jobs: typing.List["Job"] = dataclasses.field(default_factory=list, )

    # A continuation token, if not all job definitions have yet been returned.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetMappingRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source",
                "Source",
                autoboto.TypeInfo(CatalogEntry),
            ),
            (
                "sinks",
                "Sinks",
                autoboto.TypeInfo(typing.List[CatalogEntry]),
            ),
            (
                "location",
                "Location",
                autoboto.TypeInfo(Location),
            ),
        ]

    # Specifies the source table.
    source: "CatalogEntry" = dataclasses.field(default_factory=dict, )

    # A list of target tables.
    sinks: typing.List["CatalogEntry"] = dataclasses.field(
        default_factory=list,
    )

    # Parameters for the mapping.
    location: "Location" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetMappingResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "mapping",
                "Mapping",
                autoboto.TypeInfo(typing.List[MappingEntry]),
            ),
        ]

    # A list of mappings to the specified targets.
    mapping: typing.List["MappingEntry"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetPartitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
            (
                "partition_values",
                "PartitionValues",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the catalog database where the partition resides.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the partition's table.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The values that define the partition.
    partition_values: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The ID of the Data Catalog where the partition in question resides. If none
    # is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetPartitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "partition",
                "Partition",
                autoboto.TypeInfo(Partition),
            ),
        ]

    # The requested information, in the form of a `Partition` object.
    partition: "Partition" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetPartitionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
            (
                "expression",
                "Expression",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "segment",
                "Segment",
                autoboto.TypeInfo(Segment),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the catalog database where the partitions reside.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the partitions' table.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the Data Catalog where the partitions in question reside. If none
    # is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An expression filtering the partitions to be returned.
    expression: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A continuation token, if this is not the first call to retrieve these
    # partitions.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The segment of the table's partitions to scan in this request.
    segment: "Segment" = dataclasses.field(default_factory=dict, )

    # The maximum number of partitions to return in a single response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetPartitionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "partitions",
                "Partitions",
                autoboto.TypeInfo(typing.List[Partition]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of requested partitions.
    partitions: typing.List["Partition"] = dataclasses.field(
        default_factory=list,
    )

    # A continuation token, if the returned list of partitions does not does not
    # include the last one.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetPlanRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "mapping",
                "Mapping",
                autoboto.TypeInfo(typing.List[MappingEntry]),
            ),
            (
                "source",
                "Source",
                autoboto.TypeInfo(CatalogEntry),
            ),
            (
                "sinks",
                "Sinks",
                autoboto.TypeInfo(typing.List[CatalogEntry]),
            ),
            (
                "location",
                "Location",
                autoboto.TypeInfo(Location),
            ),
            (
                "language",
                "Language",
                autoboto.TypeInfo(Language),
            ),
        ]

    # The list of mappings from a source table to target tables.
    mapping: typing.List["MappingEntry"] = dataclasses.field(
        default_factory=list,
    )

    # The source table.
    source: "CatalogEntry" = dataclasses.field(default_factory=dict, )

    # The target tables.
    sinks: typing.List["CatalogEntry"] = dataclasses.field(
        default_factory=list,
    )

    # Parameters for the mapping.
    location: "Location" = dataclasses.field(default_factory=dict, )

    # The programming language of the code to perform the mapping.
    language: "Language" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetPlanResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "python_script",
                "PythonScript",
                autoboto.TypeInfo(str),
            ),
            (
                "scala_code",
                "ScalaCode",
                autoboto.TypeInfo(str),
            ),
        ]

    # A Python script to perform the mapping.
    python_script: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Scala code to perform the mapping.
    scala_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetTableRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the database in the catalog in which the table resides. For
    # Hive compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the table for which to retrieve the definition. For Hive
    # compatibility, this name is entirely lowercase.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the Data Catalog where the table resides. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetTableResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table",
                "Table",
                autoboto.TypeInfo(Table),
            ),
        ]

    # The `Table` object that defines the specified table.
    table: "Table" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetTableVersionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The database in the catalog in which the table resides. For Hive
    # compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the table. For Hive compatibility, this name is entirely
    # lowercase.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the Data Catalog where the tables reside. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID value of the table version to be retrieved.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetTableVersionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_version",
                "TableVersion",
                autoboto.TypeInfo(TableVersion),
            ),
        ]

    # The requested table version.
    table_version: "TableVersion" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetTableVersionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The database in the catalog in which the table resides. For Hive
    # compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the table. For Hive compatibility, this name is entirely
    # lowercase.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the Data Catalog where the tables reside. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A continuation token, if this is not the first call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of table versions to return in one response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetTableVersionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_versions",
                "TableVersions",
                autoboto.TypeInfo(typing.List[TableVersion]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of strings identifying available versions of the specified table.
    table_versions: typing.List["TableVersion"] = dataclasses.field(
        default_factory=list,
    )

    # A continuation token, if the list of available versions does not include
    # the last one.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetTablesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
            (
                "expression",
                "Expression",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The database in the catalog whose tables to list. For Hive compatibility,
    # this name is entirely lowercase.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the Data Catalog where the tables reside. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A regular expression pattern. If present, only those tables whose names
    # match the pattern are returned.
    expression: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A continuation token, included if this is a continuation call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of tables to return in a single response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetTablesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_list",
                "TableList",
                autoboto.TypeInfo(typing.List[Table]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of the requested `Table` objects.
    table_list: typing.List["Table"] = dataclasses.field(default_factory=list, )

    # A continuation token, present if the current list segment is not the last.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetTriggerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the trigger to retrieve.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetTriggerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trigger",
                "Trigger",
                autoboto.TypeInfo(Trigger),
            ),
        ]

    # The requested trigger definition.
    trigger: "Trigger" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetTriggersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "dependent_job_name",
                "DependentJobName",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the job for which to retrieve triggers. The trigger that can
    # start this job will be returned, and if there is no such trigger, all
    # triggers will be returned.
    dependent_job_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The maximum size of the response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetTriggersResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "triggers",
                "Triggers",
                autoboto.TypeInfo(typing.List[Trigger]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of triggers for the specified job.
    triggers: typing.List["Trigger"] = dataclasses.field(default_factory=list, )

    # A continuation token, if not all the requested triggers have yet been
    # returned.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetUserDefinedFunctionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "function_name",
                "FunctionName",
                autoboto.TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the catalog database where the function is located.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the function.
    function_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ID of the Data Catalog where the function to be retrieved is located.
    # If none is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetUserDefinedFunctionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_defined_function",
                "UserDefinedFunction",
                autoboto.TypeInfo(UserDefinedFunction),
            ),
        ]

    # The requested function definition.
    user_defined_function: "UserDefinedFunction" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetUserDefinedFunctionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "pattern",
                "Pattern",
                autoboto.TypeInfo(str),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the catalog database where the functions are located.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An optional function-name pattern string that filters the function
    # definitions returned.
    pattern: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the Data Catalog where the functions to be retrieved are located.
    # If none is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A continuation token, if this is a continuation call.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of functions to return in one response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetUserDefinedFunctionsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_defined_functions",
                "UserDefinedFunctions",
                autoboto.TypeInfo(typing.List[UserDefinedFunction]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of requested function definitions.
    user_defined_functions: typing.List["UserDefinedFunction"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )

    # A continuation token, if the list of functions returned does not include
    # the last requested function.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GrokClassifier(autoboto.ShapeBase):
    """
    A classifier that uses `grok` patterns.
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
                "classification",
                "Classification",
                autoboto.TypeInfo(str),
            ),
            (
                "grok_pattern",
                "GrokPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated",
                "LastUpdated",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
            (
                "custom_patterns",
                "CustomPatterns",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the classifier.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An identifier of the data format that the classifier matches, such as
    # Twitter, JSON, Omniture logs, and so on.
    classification: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The grok pattern applied to a data store by this classifier. For more
    # information, see built-in patterns in [Writing Custom
    # Classifers](http://docs.aws.amazon.com/glue/latest/dg/custom-
    # classifier.html).
    grok_pattern: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time this classifier was registered.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time this classifier was last updated.
    last_updated: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The version of this classifier.
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Optional custom grok patterns defined by this classifier. For more
    # information, see custom patterns in [Writing Custom
    # Classifers](http://docs.aws.amazon.com/glue/latest/dg/custom-
    # classifier.html).
    custom_patterns: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class IdempotentParameterMismatchException(autoboto.ShapeBase):
    """
    The same unique identifier was associated with two different records.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ImportCatalogToGlueRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the catalog to import. Currently, this should be the AWS account
    # ID.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ImportCatalogToGlueResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InternalServiceException(autoboto.ShapeBase):
    """
    An internal service error occurred.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidInputException(autoboto.ShapeBase):
    """
    The input provided was not valid.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class JdbcTarget(autoboto.ShapeBase):
    """
    Specifies a JDBC data store to crawl.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_name",
                "ConnectionName",
                autoboto.TypeInfo(str),
            ),
            (
                "path",
                "Path",
                autoboto.TypeInfo(str),
            ),
            (
                "exclusions",
                "Exclusions",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the connection to use to connect to the JDBC target.
    connection_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The path of the JDBC target.
    path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of glob patterns used to exclude from the crawl. For more
    # information, see [Catalog Tables with a
    # Crawler](http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html).
    exclusions: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class Job(autoboto.ShapeBase):
    """
    Specifies a job definition.
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
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "log_uri",
                "LogUri",
                autoboto.TypeInfo(str),
            ),
            (
                "role",
                "Role",
                autoboto.TypeInfo(str),
            ),
            (
                "created_on",
                "CreatedOn",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_on",
                "LastModifiedOn",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "execution_property",
                "ExecutionProperty",
                autoboto.TypeInfo(ExecutionProperty),
            ),
            (
                "command",
                "Command",
                autoboto.TypeInfo(JobCommand),
            ),
            (
                "default_arguments",
                "DefaultArguments",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "connections",
                "Connections",
                autoboto.TypeInfo(ConnectionsList),
            ),
            (
                "max_retries",
                "MaxRetries",
                autoboto.TypeInfo(int),
            ),
            (
                "allocated_capacity",
                "AllocatedCapacity",
                autoboto.TypeInfo(int),
            ),
            (
                "timeout",
                "Timeout",
                autoboto.TypeInfo(int),
            ),
            (
                "notification_property",
                "NotificationProperty",
                autoboto.TypeInfo(NotificationProperty),
            ),
        ]

    # The name you assign to this job definition.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Description of the job being defined.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # This field is reserved for future use.
    log_uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name or ARN of the IAM role associated with this job.
    role: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time and date that this job definition was created.
    created_on: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The last point in time when this job definition was modified.
    last_modified_on: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An ExecutionProperty specifying the maximum number of concurrent runs
    # allowed for this job.
    execution_property: "ExecutionProperty" = dataclasses.field(
        default_factory=dict,
    )

    # The JobCommand that executes this job.
    command: "JobCommand" = dataclasses.field(default_factory=dict, )

    # The default arguments for this job, specified as name-value pairs.

    # You can specify arguments here that your own job-execution script consumes,
    # as well as arguments that AWS Glue itself consumes.

    # For information about how to specify and consume your own Job arguments,
    # see the [Calling AWS Glue APIs in
    # Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-
    # python-calling.html) topic in the developer guide.

    # For information about the key-value pairs that AWS Glue consumes to set up
    # your job, see the [Special Parameters Used by AWS
    # Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-
    # glue-arguments.html) topic in the developer guide.
    default_arguments: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The connections used for this job.
    connections: "ConnectionsList" = dataclasses.field(default_factory=dict, )

    # The maximum number of times to retry this job after a JobRun fails.
    max_retries: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of AWS Glue data processing units (DPUs) allocated to runs of
    # this job. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is
    # a relative measure of processing power that consists of 4 vCPUs of compute
    # capacity and 16 GB of memory. For more information, see the [AWS Glue
    # pricing page](https://aws.amazon.com/glue/pricing/).
    allocated_capacity: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The job timeout in minutes.
    timeout: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies configuration properties of a job notification.
    notification_property: "NotificationProperty" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class JobBookmarkEntry(autoboto.ShapeBase):
    """
    Defines a point which a job can resume processing.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
            (
                "run",
                "Run",
                autoboto.TypeInfo(int),
            ),
            (
                "attempt",
                "Attempt",
                autoboto.TypeInfo(int),
            ),
            (
                "job_bookmark",
                "JobBookmark",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the job in question.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Version of the job.
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The run ID number.
    run: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The attempt ID number.
    attempt: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The bookmark itself.
    job_bookmark: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class JobCommand(autoboto.ShapeBase):
    """
    Specifies code executed when a job is run.
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
                "script_location",
                "ScriptLocation",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the job command: this must be `glueetl`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the S3 path to a script that executes a job (required).
    script_location: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class JobRun(autoboto.ShapeBase):
    """
    Contains information about a job run.
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
                "attempt",
                "Attempt",
                autoboto.TypeInfo(int),
            ),
            (
                "previous_run_id",
                "PreviousRunId",
                autoboto.TypeInfo(str),
            ),
            (
                "trigger_name",
                "TriggerName",
                autoboto.TypeInfo(str),
            ),
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
            (
                "started_on",
                "StartedOn",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_on",
                "LastModifiedOn",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "completed_on",
                "CompletedOn",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "job_run_state",
                "JobRunState",
                autoboto.TypeInfo(JobRunState),
            ),
            (
                "arguments",
                "Arguments",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "error_message",
                "ErrorMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "predecessor_runs",
                "PredecessorRuns",
                autoboto.TypeInfo(typing.List[Predecessor]),
            ),
            (
                "allocated_capacity",
                "AllocatedCapacity",
                autoboto.TypeInfo(int),
            ),
            (
                "execution_time",
                "ExecutionTime",
                autoboto.TypeInfo(int),
            ),
            (
                "timeout",
                "Timeout",
                autoboto.TypeInfo(int),
            ),
            (
                "notification_property",
                "NotificationProperty",
                autoboto.TypeInfo(NotificationProperty),
            ),
        ]

    # The ID of this job run.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of the attempt to run this job.
    attempt: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the previous run of this job. For example, the JobRunId specified
    # in the StartJobRun action.
    previous_run_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the trigger that started this job run.
    trigger_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the job definition being used in this run.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The date and time at which this job run was started.
    started_on: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The last time this job run was modified.
    last_modified_on: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time this job run completed.
    completed_on: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The current state of the job run.
    job_run_state: "JobRunState" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The job arguments associated with this run. These override equivalent
    # default arguments set for the job.

    # You can specify arguments here that your own job-execution script consumes,
    # as well as arguments that AWS Glue itself consumes.

    # For information about how to specify and consume your own job arguments,
    # see the [Calling AWS Glue APIs in
    # Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-
    # python-calling.html) topic in the developer guide.

    # For information about the key-value pairs that AWS Glue consumes to set up
    # your job, see the [Special Parameters Used by AWS
    # Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-
    # glue-arguments.html) topic in the developer guide.
    arguments: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An error message associated with this job run.
    error_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of predecessors to this job run.
    predecessor_runs: typing.List["Predecessor"] = dataclasses.field(
        default_factory=list,
    )

    # The number of AWS Glue data processing units (DPUs) allocated to this
    # JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a
    # relative measure of processing power that consists of 4 vCPUs of compute
    # capacity and 16 GB of memory. For more information, see the [AWS Glue
    # pricing page](https://aws.amazon.com/glue/pricing/).
    allocated_capacity: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The amount of time (in seconds) that the job run consumed resources.
    execution_time: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The job run timeout in minutes.
    timeout: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies configuration properties of a job run notification.
    notification_property: "NotificationProperty" = dataclasses.field(
        default_factory=dict,
    )


class JobRunState(Enum):
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    TIMEOUT = "TIMEOUT"


@dataclasses.dataclass
class JobUpdate(autoboto.ShapeBase):
    """
    Specifies information used to update an existing job definition. Note that the
    previous job definition will be completely overwritten by this information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "log_uri",
                "LogUri",
                autoboto.TypeInfo(str),
            ),
            (
                "role",
                "Role",
                autoboto.TypeInfo(str),
            ),
            (
                "execution_property",
                "ExecutionProperty",
                autoboto.TypeInfo(ExecutionProperty),
            ),
            (
                "command",
                "Command",
                autoboto.TypeInfo(JobCommand),
            ),
            (
                "default_arguments",
                "DefaultArguments",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "connections",
                "Connections",
                autoboto.TypeInfo(ConnectionsList),
            ),
            (
                "max_retries",
                "MaxRetries",
                autoboto.TypeInfo(int),
            ),
            (
                "allocated_capacity",
                "AllocatedCapacity",
                autoboto.TypeInfo(int),
            ),
            (
                "timeout",
                "Timeout",
                autoboto.TypeInfo(int),
            ),
            (
                "notification_property",
                "NotificationProperty",
                autoboto.TypeInfo(NotificationProperty),
            ),
        ]

    # Description of the job being defined.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # This field is reserved for future use.
    log_uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name or ARN of the IAM role associated with this job (required).
    role: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An ExecutionProperty specifying the maximum number of concurrent runs
    # allowed for this job.
    execution_property: "ExecutionProperty" = dataclasses.field(
        default_factory=dict,
    )

    # The JobCommand that executes this job (required).
    command: "JobCommand" = dataclasses.field(default_factory=dict, )

    # The default arguments for this job.

    # You can specify arguments here that your own job-execution script consumes,
    # as well as arguments that AWS Glue itself consumes.

    # For information about how to specify and consume your own Job arguments,
    # see the [Calling AWS Glue APIs in
    # Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-
    # python-calling.html) topic in the developer guide.

    # For information about the key-value pairs that AWS Glue consumes to set up
    # your job, see the [Special Parameters Used by AWS
    # Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-
    # glue-arguments.html) topic in the developer guide.
    default_arguments: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The connections used for this job.
    connections: "ConnectionsList" = dataclasses.field(default_factory=dict, )

    # The maximum number of times to retry this job if it fails.
    max_retries: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of AWS Glue data processing units (DPUs) to allocate to this
    # Job. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a
    # relative measure of processing power that consists of 4 vCPUs of compute
    # capacity and 16 GB of memory. For more information, see the [AWS Glue
    # pricing page](https://aws.amazon.com/glue/pricing/).
    allocated_capacity: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The job timeout in minutes. The default is 2880 minutes (48 hours).
    timeout: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies configuration properties of a job notification.
    notification_property: "NotificationProperty" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class JsonClassifier(autoboto.ShapeBase):
    """
    A classifier for `JSON` content.
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
                "json_path",
                "JsonPath",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated",
                "LastUpdated",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the classifier.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A `JsonPath` string defining the JSON data for the classifier to classify.
    # AWS Glue supports a subset of JsonPath, as described in [Writing JsonPath
    # Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-
    # classifier.html#custom-classifier-json).
    json_path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time this classifier was registered.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time this classifier was last updated.
    last_updated: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The version of this classifier.
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class Language(Enum):
    PYTHON = "PYTHON"
    SCALA = "SCALA"


@dataclasses.dataclass
class LastCrawlInfo(autoboto.ShapeBase):
    """
    Status and error information about the most recent crawl.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                autoboto.TypeInfo(LastCrawlStatus),
            ),
            (
                "error_message",
                "ErrorMessage",
                autoboto.TypeInfo(str),
            ),
            (
                "log_group",
                "LogGroup",
                autoboto.TypeInfo(str),
            ),
            (
                "log_stream",
                "LogStream",
                autoboto.TypeInfo(str),
            ),
            (
                "message_prefix",
                "MessagePrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "start_time",
                "StartTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # Status of the last crawl.
    status: "LastCrawlStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If an error occurred, the error information about the last crawl.
    error_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The log group for the last crawl.
    log_group: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The log stream for the last crawl.
    log_stream: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The prefix for a message about this crawl.
    message_prefix: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time at which the crawl started.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class LastCrawlStatus(Enum):
    SUCCEEDED = "SUCCEEDED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


@dataclasses.dataclass
class Location(autoboto.ShapeBase):
    """
    The location of resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "jdbc",
                "Jdbc",
                autoboto.TypeInfo(typing.List[CodeGenNodeArg]),
            ),
            (
                "s3",
                "S3",
                autoboto.TypeInfo(typing.List[CodeGenNodeArg]),
            ),
            (
                "dynamo_db",
                "DynamoDB",
                autoboto.TypeInfo(typing.List[CodeGenNodeArg]),
            ),
        ]

    # A JDBC location.
    jdbc: typing.List["CodeGenNodeArg"] = dataclasses.field(
        default_factory=list,
    )

    # An Amazon S3 location.
    s3: typing.List["CodeGenNodeArg"] = dataclasses.field(
        default_factory=list,
    )

    # A DynamoDB Table location.
    dynamo_db: typing.List["CodeGenNodeArg"] = dataclasses.field(
        default_factory=list,
    )


class Logical(Enum):
    AND = "AND"
    ANY = "ANY"


class LogicalOperator(Enum):
    EQUALS = "EQUALS"


@dataclasses.dataclass
class MappingEntry(autoboto.ShapeBase):
    """
    Defines a mapping.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_table",
                "SourceTable",
                autoboto.TypeInfo(str),
            ),
            (
                "source_path",
                "SourcePath",
                autoboto.TypeInfo(str),
            ),
            (
                "source_type",
                "SourceType",
                autoboto.TypeInfo(str),
            ),
            (
                "target_table",
                "TargetTable",
                autoboto.TypeInfo(str),
            ),
            (
                "target_path",
                "TargetPath",
                autoboto.TypeInfo(str),
            ),
            (
                "target_type",
                "TargetType",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the source table.
    source_table: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The source path.
    source_path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The source type.
    source_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The target table.
    target_table: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The target path.
    target_path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The target type.
    target_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class NoScheduleException(autoboto.ShapeBase):
    """
    There is no applicable schedule.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class NotificationProperty(autoboto.ShapeBase):
    """
    Specifies configuration properties of a notification.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notify_delay_after",
                "NotifyDelayAfter",
                autoboto.TypeInfo(int),
            ),
        ]

    # After a job run starts, the number of minutes to wait before sending a job
    # run delay notification.
    notify_delay_after: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class OperationTimeoutException(autoboto.ShapeBase):
    """
    The operation timed out.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Order(autoboto.ShapeBase):
    """
    Specifies the sort order of a sorted column.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "column",
                "Column",
                autoboto.TypeInfo(str),
            ),
            (
                "sort_order",
                "SortOrder",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the column.
    column: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Indicates that the column is sorted in ascending order (`== 1`), or in
    # descending order (`==0`).
    sort_order: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Partition(autoboto.ShapeBase):
    """
    Represents a slice of table data.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "values",
                "Values",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_access_time",
                "LastAccessTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "storage_descriptor",
                "StorageDescriptor",
                autoboto.TypeInfo(StorageDescriptor),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "last_analyzed_time",
                "LastAnalyzedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The values of the partition.
    values: typing.List[str] = dataclasses.field(default_factory=list, )

    # The name of the catalog database where the table in question is located.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the table in question.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time at which the partition was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The last time at which the partition was accessed.
    last_access_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Provides information about the physical location where the partition is
    # stored.
    storage_descriptor: "StorageDescriptor" = dataclasses.field(
        default_factory=dict,
    )

    # Partition parameters, in the form of a list of key-value pairs.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The last time at which column statistics were computed for this partition.
    last_analyzed_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PartitionError(autoboto.ShapeBase):
    """
    Contains information about a partition error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "partition_values",
                "PartitionValues",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "error_detail",
                "ErrorDetail",
                autoboto.TypeInfo(ErrorDetail),
            ),
        ]

    # The values that define the partition.
    partition_values: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Details about the partition error.
    error_detail: "ErrorDetail" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class PartitionInput(autoboto.ShapeBase):
    """
    The structure used to create and update a partion.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "values",
                "Values",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "last_access_time",
                "LastAccessTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "storage_descriptor",
                "StorageDescriptor",
                autoboto.TypeInfo(StorageDescriptor),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "last_analyzed_time",
                "LastAnalyzedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The values of the partition.
    values: typing.List[str] = dataclasses.field(default_factory=list, )

    # The last time at which the partition was accessed.
    last_access_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Provides information about the physical location where the partition is
    # stored.
    storage_descriptor: "StorageDescriptor" = dataclasses.field(
        default_factory=dict,
    )

    # Partition parameters, in the form of a list of key-value pairs.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The last time at which column statistics were computed for this partition.
    last_analyzed_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class PartitionValueList(autoboto.ShapeBase):
    """
    Contains a list of values defining partitions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "values",
                "Values",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The list of values.
    values: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class PhysicalConnectionRequirements(autoboto.ShapeBase):
    """
    Specifies the physical requirements for a connection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_id",
                "SubnetId",
                autoboto.TypeInfo(str),
            ),
            (
                "security_group_id_list",
                "SecurityGroupIdList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                autoboto.TypeInfo(str),
            ),
        ]

    # The subnet ID used by the connection.
    subnet_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The security group ID list used by the connection.
    security_group_id_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The connection's availability zone. This field is deprecated and has no
    # effect.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Predecessor(autoboto.ShapeBase):
    """
    A job run that was used in the predicate of a conditional trigger that triggered
    this job run.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
            (
                "run_id",
                "RunId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the job definition used by the predecessor job run.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The job-run ID of the predecessor job run.
    run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Predicate(autoboto.ShapeBase):
    """
    Defines the predicate of the trigger, which determines when it fires.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logical",
                "Logical",
                autoboto.TypeInfo(Logical),
            ),
            (
                "conditions",
                "Conditions",
                autoboto.TypeInfo(typing.List[Condition]),
            ),
        ]

    # Optional field if only one condition is listed. If multiple conditions are
    # listed, then this field is required.
    logical: "Logical" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of the conditions that determine when the trigger will fire.
    conditions: typing.List["Condition"] = dataclasses.field(
        default_factory=list,
    )


class PrincipalType(Enum):
    USER = "USER"
    ROLE = "ROLE"
    GROUP = "GROUP"


@dataclasses.dataclass
class ResetJobBookmarkRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the job in question.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ResetJobBookmarkResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_bookmark_entry",
                "JobBookmarkEntry",
                autoboto.TypeInfo(JobBookmarkEntry),
            ),
        ]

    # The reset bookmark entry.
    job_bookmark_entry: "JobBookmarkEntry" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ResourceNumberLimitExceededException(autoboto.ShapeBase):
    """
    A resource numerical limit was exceeded.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class ResourceType(Enum):
    JAR = "JAR"
    FILE = "FILE"
    ARCHIVE = "ARCHIVE"


@dataclasses.dataclass
class ResourceUri(autoboto.ShapeBase):
    """
    URIs for function resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "ResourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "uri",
                "Uri",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of the resource.
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The URI for accessing the resource.
    uri: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class S3Target(autoboto.ShapeBase):
    """
    Specifies a data store in Amazon S3.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                autoboto.TypeInfo(str),
            ),
            (
                "exclusions",
                "Exclusions",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The path to the Amazon S3 target.
    path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of glob patterns used to exclude from the crawl. For more
    # information, see [Catalog Tables with a
    # Crawler](http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html).
    exclusions: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class Schedule(autoboto.ShapeBase):
    """
    A scheduling object using a `cron` statement to schedule an event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schedule_expression",
                "ScheduleExpression",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(ScheduleState),
            ),
        ]

    # A `cron` expression used to specify the schedule (see [Time-Based Schedules
    # for Jobs and Crawlers](http://docs.aws.amazon.com/glue/latest/dg/monitor-
    # data-warehouse-schedule.html). For example, to run something every day at
    # 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
    schedule_expression: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The state of the schedule.
    state: "ScheduleState" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class ScheduleState(Enum):
    SCHEDULED = "SCHEDULED"
    NOT_SCHEDULED = "NOT_SCHEDULED"
    TRANSITIONING = "TRANSITIONING"


@dataclasses.dataclass
class SchedulerNotRunningException(autoboto.ShapeBase):
    """
    The specified scheduler is not running.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SchedulerRunningException(autoboto.ShapeBase):
    """
    The specified scheduler is already running.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SchedulerTransitioningException(autoboto.ShapeBase):
    """
    The specified scheduler is transitioning.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class SchemaChangePolicy(autoboto.ShapeBase):
    """
    Crawler policy for update and deletion behavior.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "update_behavior",
                "UpdateBehavior",
                autoboto.TypeInfo(UpdateBehavior),
            ),
            (
                "delete_behavior",
                "DeleteBehavior",
                autoboto.TypeInfo(DeleteBehavior),
            ),
        ]

    # The update behavior when the crawler finds a changed schema.
    update_behavior: "UpdateBehavior" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The deletion behavior when the crawler finds a deleted object.
    delete_behavior: "DeleteBehavior" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Segment(autoboto.ShapeBase):
    """
    Defines a non-overlapping region of a table's partitions, allowing multiple
    requests to be executed in parallel.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "segment_number",
                "SegmentNumber",
                autoboto.TypeInfo(int),
            ),
            (
                "total_segments",
                "TotalSegments",
                autoboto.TypeInfo(int),
            ),
        ]

    # The zero-based index number of the this segment. For example, if the total
    # number of segments is 4, SegmentNumber values will range from zero through
    # three.
    segment_number: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The total numer of segments.
    total_segments: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SerDeInfo(autoboto.ShapeBase):
    """
    Information about a serialization/deserialization program (SerDe) which serves
    as an extractor and loader.
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
                "serialization_library",
                "SerializationLibrary",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Name of the SerDe.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Usually the class that implements the SerDe. An example is:
    # `org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`.
    serialization_library: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A list of initialization parameters for the SerDe, in key-value form.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class SkewedInfo(autoboto.ShapeBase):
    """
    Specifies skewed values in a table. Skewed are ones that occur with very high
    frequency.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "skewed_column_names",
                "SkewedColumnNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "skewed_column_values",
                "SkewedColumnValues",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "skewed_column_value_location_maps",
                "SkewedColumnValueLocationMaps",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # A list of names of columns that contain skewed values.
    skewed_column_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list of values that appear so frequently as to be considered skewed.
    skewed_column_values: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A mapping of skewed values to the columns that contain them.
    skewed_column_value_location_maps: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class StartCrawlerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the crawler to start.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StartCrawlerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StartCrawlerScheduleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "crawler_name",
                "CrawlerName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the crawler to schedule.
    crawler_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StartCrawlerScheduleResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StartJobRunRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
            (
                "job_run_id",
                "JobRunId",
                autoboto.TypeInfo(str),
            ),
            (
                "arguments",
                "Arguments",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "allocated_capacity",
                "AllocatedCapacity",
                autoboto.TypeInfo(int),
            ),
            (
                "timeout",
                "Timeout",
                autoboto.TypeInfo(int),
            ),
            (
                "notification_property",
                "NotificationProperty",
                autoboto.TypeInfo(NotificationProperty),
            ),
        ]

    # The name of the job definition to use.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of a previous JobRun to retry.
    job_run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The job arguments specifically for this run. They override the equivalent
    # default arguments set for in the job definition itself.

    # You can specify arguments here that your own job-execution script consumes,
    # as well as arguments that AWS Glue itself consumes.

    # For information about how to specify and consume your own Job arguments,
    # see the [Calling AWS Glue APIs in
    # Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-
    # python-calling.html) topic in the developer guide.

    # For information about the key-value pairs that AWS Glue consumes to set up
    # your job, see the [Special Parameters Used by AWS
    # Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-
    # glue-arguments.html) topic in the developer guide.
    arguments: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of AWS Glue data processing units (DPUs) to allocate to this
    # JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a
    # relative measure of processing power that consists of 4 vCPUs of compute
    # capacity and 16 GB of memory. For more information, see the [AWS Glue
    # pricing page](https://aws.amazon.com/glue/pricing/).
    allocated_capacity: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The job run timeout in minutes. It overrides the timeout value of the job.
    timeout: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies configuration properties of a job run notification.
    notification_property: "NotificationProperty" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class StartJobRunResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_run_id",
                "JobRunId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID assigned to this job run.
    job_run_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StartTriggerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the trigger to start.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StartTriggerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the trigger that was started.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StopCrawlerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the crawler to stop.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StopCrawlerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StopCrawlerScheduleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "crawler_name",
                "CrawlerName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the crawler whose schedule state to set.
    crawler_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StopCrawlerScheduleResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StopTriggerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the trigger to stop.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StopTriggerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the trigger that was stopped.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class StorageDescriptor(autoboto.ShapeBase):
    """
    Describes the physical storage of table data.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "columns",
                "Columns",
                autoboto.TypeInfo(typing.List[Column]),
            ),
            (
                "location",
                "Location",
                autoboto.TypeInfo(str),
            ),
            (
                "input_format",
                "InputFormat",
                autoboto.TypeInfo(str),
            ),
            (
                "output_format",
                "OutputFormat",
                autoboto.TypeInfo(str),
            ),
            (
                "compressed",
                "Compressed",
                autoboto.TypeInfo(bool),
            ),
            (
                "number_of_buckets",
                "NumberOfBuckets",
                autoboto.TypeInfo(int),
            ),
            (
                "serde_info",
                "SerdeInfo",
                autoboto.TypeInfo(SerDeInfo),
            ),
            (
                "bucket_columns",
                "BucketColumns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "sort_columns",
                "SortColumns",
                autoboto.TypeInfo(typing.List[Order]),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "skewed_info",
                "SkewedInfo",
                autoboto.TypeInfo(SkewedInfo),
            ),
            (
                "stored_as_sub_directories",
                "StoredAsSubDirectories",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A list of the `Columns` in the table.
    columns: typing.List["Column"] = dataclasses.field(default_factory=list, )

    # The physical location of the table. By default this takes the form of the
    # warehouse location, followed by the database location in the warehouse,
    # followed by the table name.
    location: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The input format: `SequenceFileInputFormat` (binary), or `TextInputFormat`,
    # or a custom format.
    input_format: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The output format: `SequenceFileOutputFormat` (binary), or
    # `IgnoreKeyTextOutputFormat`, or a custom format.
    output_format: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # True if the data in the table is compressed, or False if not.
    compressed: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Must be specified if the table contains any dimension columns.
    number_of_buckets: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Serialization/deserialization (SerDe) information.
    serde_info: "SerDeInfo" = dataclasses.field(default_factory=dict, )

    # A list of reducer grouping columns, clustering columns, and bucketing
    # columns in the table.
    bucket_columns: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list specifying the sort order of each bucket in the table.
    sort_columns: typing.List["Order"] = dataclasses.field(
        default_factory=list,
    )

    # User-supplied properties in key-value form.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Information about values that appear very frequently in a column (skewed
    # values).
    skewed_info: "SkewedInfo" = dataclasses.field(default_factory=dict, )

    # True if the table data is stored in subdirectories, or False if not.
    stored_as_sub_directories: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Table(autoboto.ShapeBase):
    """
    Represents a collection of related data organized in columns and rows.
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
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(str),
            ),
            (
                "create_time",
                "CreateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "update_time",
                "UpdateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_access_time",
                "LastAccessTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_analyzed_time",
                "LastAnalyzedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "retention",
                "Retention",
                autoboto.TypeInfo(int),
            ),
            (
                "storage_descriptor",
                "StorageDescriptor",
                autoboto.TypeInfo(StorageDescriptor),
            ),
            (
                "partition_keys",
                "PartitionKeys",
                autoboto.TypeInfo(typing.List[Column]),
            ),
            (
                "view_original_text",
                "ViewOriginalText",
                autoboto.TypeInfo(str),
            ),
            (
                "view_expanded_text",
                "ViewExpandedText",
                autoboto.TypeInfo(str),
            ),
            (
                "table_type",
                "TableType",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "created_by",
                "CreatedBy",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the table. For Hive compatibility, this must be entirely lowercase.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Name of the metadata database where the table metadata resides. For Hive
    # compatibility, this must be all lowercase.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Description of the table.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Owner of the table.
    owner: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Time when the table definition was created in the Data Catalog.
    create_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Last time the table was updated.
    update_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Last time the table was accessed. This is usually taken from HDFS, and may
    # not be reliable.
    last_access_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Last time column statistics were computed for this table.
    last_analyzed_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Retention time for this table.
    retention: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A storage descriptor containing information about the physical storage of
    # this table.
    storage_descriptor: "StorageDescriptor" = dataclasses.field(
        default_factory=dict,
    )

    # A list of columns by which the table is partitioned. Only primitive types
    # are supported as partition keys.
    partition_keys: typing.List["Column"] = dataclasses.field(
        default_factory=list,
    )

    # If the table is a view, the original text of the view; otherwise `null`.
    view_original_text: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the table is a view, the expanded text of the view; otherwise `null`.
    view_expanded_text: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of this table (`EXTERNAL_TABLE`, `VIRTUAL_VIEW`, etc.).
    table_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Properties associated with this table, as a list of key-value pairs.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Person or entity who created the table.
    created_by: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TableError(autoboto.ShapeBase):
    """
    An error record for table operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
            (
                "error_detail",
                "ErrorDetail",
                autoboto.TypeInfo(ErrorDetail),
            ),
        ]

    # Name of the table. For Hive compatibility, this must be entirely lowercase.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Detail about the error.
    error_detail: "ErrorDetail" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class TableInput(autoboto.ShapeBase):
    """
    Structure used to create or update the table.
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
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "owner",
                "Owner",
                autoboto.TypeInfo(str),
            ),
            (
                "last_access_time",
                "LastAccessTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_analyzed_time",
                "LastAnalyzedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "retention",
                "Retention",
                autoboto.TypeInfo(int),
            ),
            (
                "storage_descriptor",
                "StorageDescriptor",
                autoboto.TypeInfo(StorageDescriptor),
            ),
            (
                "partition_keys",
                "PartitionKeys",
                autoboto.TypeInfo(typing.List[Column]),
            ),
            (
                "view_original_text",
                "ViewOriginalText",
                autoboto.TypeInfo(str),
            ),
            (
                "view_expanded_text",
                "ViewExpandedText",
                autoboto.TypeInfo(str),
            ),
            (
                "table_type",
                "TableType",
                autoboto.TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Name of the table. For Hive compatibility, this is folded to lowercase when
    # it is stored.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Description of the table.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Owner of the table.
    owner: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Last time the table was accessed.
    last_access_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Last time column statistics were computed for this table.
    last_analyzed_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Retention time for this table.
    retention: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A storage descriptor containing information about the physical storage of
    # this table.
    storage_descriptor: "StorageDescriptor" = dataclasses.field(
        default_factory=dict,
    )

    # A list of columns by which the table is partitioned. Only primitive types
    # are supported as partition keys.
    partition_keys: typing.List["Column"] = dataclasses.field(
        default_factory=list,
    )

    # If the table is a view, the original text of the view; otherwise `null`.
    view_original_text: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If the table is a view, the expanded text of the view; otherwise `null`.
    view_expanded_text: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The type of this table (`EXTERNAL_TABLE`, `VIRTUAL_VIEW`, etc.).
    table_type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Properties associated with this table, as a list of key-value pairs.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class TableVersion(autoboto.ShapeBase):
    """
    Specifies a version of a table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table",
                "Table",
                autoboto.TypeInfo(Table),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The table in question
    table: "Table" = dataclasses.field(default_factory=dict, )

    # The ID value that identifies this table version.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class TableVersionError(autoboto.ShapeBase):
    """
    An error record for table-version operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                autoboto.TypeInfo(str),
            ),
            (
                "error_detail",
                "ErrorDetail",
                autoboto.TypeInfo(ErrorDetail),
            ),
        ]

    # The name of the table in question.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID value of the version in question.
    version_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Detail about the error.
    error_detail: "ErrorDetail" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class Trigger(autoboto.ShapeBase):
    """
    Information about a specific trigger.
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
                "id",
                "Id",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "Type",
                autoboto.TypeInfo(TriggerType),
            ),
            (
                "state",
                "State",
                autoboto.TypeInfo(TriggerState),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                autoboto.TypeInfo(str),
            ),
            (
                "actions",
                "Actions",
                autoboto.TypeInfo(typing.List[Action]),
            ),
            (
                "predicate",
                "Predicate",
                autoboto.TypeInfo(Predicate),
            ),
        ]

    # Name of the trigger.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Reserved for future use.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of trigger that this is.
    type: "TriggerType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The current state of the trigger.
    state: "TriggerState" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of this trigger.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A `cron` expression used to specify the schedule (see [Time-Based Schedules
    # for Jobs and Crawlers](http://docs.aws.amazon.com/glue/latest/dg/monitor-
    # data-warehouse-schedule.html). For example, to run something every day at
    # 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
    schedule: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The actions initiated by this trigger.
    actions: typing.List["Action"] = dataclasses.field(default_factory=list, )

    # The predicate of this trigger, which defines when it will fire.
    predicate: "Predicate" = dataclasses.field(default_factory=dict, )


class TriggerState(Enum):
    CREATING = "CREATING"
    CREATED = "CREATED"
    ACTIVATING = "ACTIVATING"
    ACTIVATED = "ACTIVATED"
    DEACTIVATING = "DEACTIVATING"
    DEACTIVATED = "DEACTIVATED"
    DELETING = "DELETING"
    UPDATING = "UPDATING"


class TriggerType(Enum):
    SCHEDULED = "SCHEDULED"
    CONDITIONAL = "CONDITIONAL"
    ON_DEMAND = "ON_DEMAND"


@dataclasses.dataclass
class TriggerUpdate(autoboto.ShapeBase):
    """
    A structure used to provide information used to update a trigger. This object
    will update the the previous trigger definition by overwriting it completely.
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
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                autoboto.TypeInfo(str),
            ),
            (
                "actions",
                "Actions",
                autoboto.TypeInfo(typing.List[Action]),
            ),
            (
                "predicate",
                "Predicate",
                autoboto.TypeInfo(Predicate),
            ),
        ]

    # Reserved for future use.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A description of this trigger.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A `cron` expression used to specify the schedule (see [Time-Based Schedules
    # for Jobs and Crawlers](http://docs.aws.amazon.com/glue/latest/dg/monitor-
    # data-warehouse-schedule.html). For example, to run something every day at
    # 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
    schedule: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The actions initiated by this trigger.
    actions: typing.List["Action"] = dataclasses.field(default_factory=list, )

    # The predicate of this trigger, which defines when it will fire.
    predicate: "Predicate" = dataclasses.field(default_factory=dict, )


class UpdateBehavior(Enum):
    LOG = "LOG"
    UPDATE_IN_DATABASE = "UPDATE_IN_DATABASE"


@dataclasses.dataclass
class UpdateClassifierRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "grok_classifier",
                "GrokClassifier",
                autoboto.TypeInfo(UpdateGrokClassifierRequest),
            ),
            (
                "xml_classifier",
                "XMLClassifier",
                autoboto.TypeInfo(UpdateXMLClassifierRequest),
            ),
            (
                "json_classifier",
                "JsonClassifier",
                autoboto.TypeInfo(UpdateJsonClassifierRequest),
            ),
        ]

    # A `GrokClassifier` object with updated fields.
    grok_classifier: "UpdateGrokClassifierRequest" = dataclasses.field(
        default_factory=dict,
    )

    # An `XMLClassifier` object with updated fields.
    xml_classifier: "UpdateXMLClassifierRequest" = dataclasses.field(
        default_factory=dict,
    )

    # A `JsonClassifier` object with updated fields.
    json_classifier: "UpdateJsonClassifierRequest" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateClassifierResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateConnectionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "connection_input",
                "ConnectionInput",
                autoboto.TypeInfo(ConnectionInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the connection definition to update.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A `ConnectionInput` object that redefines the connection in question.
    connection_input: "ConnectionInput" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the Data Catalog in which the connection resides. If none is
    # supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateConnectionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateCrawlerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "role",
                "Role",
                autoboto.TypeInfo(str),
            ),
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                autoboto.TypeInfo(CrawlerTargets),
            ),
            (
                "schedule",
                "Schedule",
                autoboto.TypeInfo(str),
            ),
            (
                "classifiers",
                "Classifiers",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "table_prefix",
                "TablePrefix",
                autoboto.TypeInfo(str),
            ),
            (
                "schema_change_policy",
                "SchemaChangePolicy",
                autoboto.TypeInfo(SchemaChangePolicy),
            ),
            (
                "configuration",
                "Configuration",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the new crawler.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The IAM role (or ARN of an IAM role) used by the new crawler to access
    # customer resources.
    role: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The AWS Glue database where results are stored, such as:
    # `arn:aws:daylight:us-east-1::database/sometable/*`.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the new crawler.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of targets to crawl.
    targets: "CrawlerTargets" = dataclasses.field(default_factory=dict, )

    # A `cron` expression used to specify the schedule (see [Time-Based Schedules
    # for Jobs and Crawlers](http://docs.aws.amazon.com/glue/latest/dg/monitor-
    # data-warehouse-schedule.html). For example, to run something every day at
    # 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
    schedule: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of custom classifiers that the user has registered. By default, all
    # built-in classifiers are included in a crawl, but these custom classifiers
    # always override the default classifiers for a given classification.
    classifiers: typing.List[str] = dataclasses.field(default_factory=list, )

    # The table prefix used for catalog tables that are created.
    table_prefix: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Policy for the crawler's update and deletion behavior.
    schema_change_policy: "SchemaChangePolicy" = dataclasses.field(
        default_factory=dict,
    )

    # Crawler configuration information. This versioned JSON string allows users
    # to specify aspects of a crawler's behavior. For more information, see
    # [Configuring a Crawler](http://docs.aws.amazon.com/glue/latest/dg/crawler-
    # configuration.html).
    configuration: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateCrawlerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateCrawlerScheduleRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "crawler_name",
                "CrawlerName",
                autoboto.TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                autoboto.TypeInfo(str),
            ),
        ]

    # Name of the crawler whose schedule to update.
    crawler_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The updated `cron` expression used to specify the schedule (see [Time-Based
    # Schedules for Jobs and
    # Crawlers](http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-
    # schedule.html). For example, to run something every day at 12:15 UTC, you
    # would specify: `cron(15 12 * * ? *)`.
    schedule: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateCrawlerScheduleResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateDatabaseRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "database_input",
                "DatabaseInput",
                autoboto.TypeInfo(DatabaseInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the database to update in the catalog. For Hive compatibility,
    # this is folded to lowercase.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A `DatabaseInput` object specifying the new definition of the metadata
    # database in the catalog.
    database_input: "DatabaseInput" = dataclasses.field(default_factory=dict, )

    # The ID of the Data Catalog in which the metadata database resides. If none
    # is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateDatabaseResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateDevEndpointRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                autoboto.TypeInfo(str),
            ),
            (
                "public_key",
                "PublicKey",
                autoboto.TypeInfo(str),
            ),
            (
                "add_public_keys",
                "AddPublicKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "delete_public_keys",
                "DeletePublicKeys",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "custom_libraries",
                "CustomLibraries",
                autoboto.TypeInfo(DevEndpointCustomLibraries),
            ),
            (
                "update_etl_libraries",
                "UpdateEtlLibraries",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the DevEndpoint to be updated.
    endpoint_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The public key for the DevEndpoint to use.
    public_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The list of public keys for the DevEndpoint to use.
    add_public_keys: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The list of public keys to be deleted from the DevEndpoint.
    delete_public_keys: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # Custom Python or Java libraries to be loaded in the DevEndpoint.
    custom_libraries: "DevEndpointCustomLibraries" = dataclasses.field(
        default_factory=dict,
    )

    # True if the list of custom libraries to be loaded in the development
    # endpoint needs to be updated, or False otherwise.
    update_etl_libraries: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateDevEndpointResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateGrokClassifierRequest(autoboto.ShapeBase):
    """
    Specifies a grok classifier to update when passed to `UpdateClassifier`.
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
                "classification",
                "Classification",
                autoboto.TypeInfo(str),
            ),
            (
                "grok_pattern",
                "GrokPattern",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_patterns",
                "CustomPatterns",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the `GrokClassifier`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An identifier of the data format that the classifier matches, such as
    # Twitter, JSON, Omniture logs, Amazon CloudWatch Logs, and so on.
    classification: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The grok pattern used by this classifier.
    grok_pattern: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Optional custom grok patterns used by this classifier.
    custom_patterns: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateJobRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
            (
                "job_update",
                "JobUpdate",
                autoboto.TypeInfo(JobUpdate),
            ),
        ]

    # Name of the job definition to update.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies the values with which to update the job definition.
    job_update: "JobUpdate" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateJobResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "JobName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Returns the name of the updated job definition.
    job_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateJsonClassifierRequest(autoboto.ShapeBase):
    """
    Specifies a JSON classifier to be updated.
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
                "json_path",
                "JsonPath",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the classifier.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A `JsonPath` string defining the JSON data for the classifier to classify.
    # AWS Glue supports a subset of JsonPath, as described in [Writing JsonPath
    # Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-
    # classifier.html#custom-classifier-json).
    json_path: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdatePartitionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
            (
                "partition_value_list",
                "PartitionValueList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "partition_input",
                "PartitionInput",
                autoboto.TypeInfo(PartitionInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the catalog database in which the table in question resides.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the table where the partition to be updated is located.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of the values defining the partition.
    partition_value_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The new partition object to which to update the partition.
    partition_input: "PartitionInput" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the Data Catalog where the partition to be updated resides. If
    # none is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdatePartitionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateTableRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_input",
                "TableInput",
                autoboto.TypeInfo(TableInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
            (
                "skip_archive",
                "SkipArchive",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the catalog database in which the table resides. For Hive
    # compatibility, this name is entirely lowercase.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An updated `TableInput` object to define the metadata table in the catalog.
    table_input: "TableInput" = dataclasses.field(default_factory=dict, )

    # The ID of the Data Catalog where the table resides. If none is supplied,
    # the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # By default, `UpdateTable` always creates an archived version of the table
    # before updating it. If `skipArchive` is set to true, however, `UpdateTable`
    # does not create the archived version.
    skip_archive: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateTableResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateTriggerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "trigger_update",
                "TriggerUpdate",
                autoboto.TypeInfo(TriggerUpdate),
            ),
        ]

    # The name of the trigger to update.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new values with which to update the trigger.
    trigger_update: "TriggerUpdate" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateTriggerResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trigger",
                "Trigger",
                autoboto.TypeInfo(Trigger),
            ),
        ]

    # The resulting trigger definition.
    trigger: "Trigger" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateUserDefinedFunctionRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_name",
                "DatabaseName",
                autoboto.TypeInfo(str),
            ),
            (
                "function_name",
                "FunctionName",
                autoboto.TypeInfo(str),
            ),
            (
                "function_input",
                "FunctionInput",
                autoboto.TypeInfo(UserDefinedFunctionInput),
            ),
            (
                "catalog_id",
                "CatalogId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the catalog database where the function to be updated is
    # located.
    database_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the function.
    function_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A `FunctionInput` object that re-defines the function in the Data Catalog.
    function_input: "UserDefinedFunctionInput" = dataclasses.field(
        default_factory=dict,
    )

    # The ID of the Data Catalog where the function to be updated is located. If
    # none is supplied, the AWS account ID is used by default.
    catalog_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateUserDefinedFunctionResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateXMLClassifierRequest(autoboto.ShapeBase):
    """
    Specifies an XML classifier to be updated.
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
                "classification",
                "Classification",
                autoboto.TypeInfo(str),
            ),
            (
                "row_tag",
                "RowTag",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the classifier.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An identifier of the data format that the classifier matches.
    classification: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The XML tag designating the element that contains each record in an XML
    # document being parsed. Note that this cannot identify a self-closing
    # element (closed by `/>`). An empty row element that contains only
    # attributes can be parsed as long as it ends with a closing tag (for
    # example, `<row item_a="A" item_b="B"></row>` is okay, but `<row item_a="A"
    # item_b="B" />` is not).
    row_tag: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UserDefinedFunction(autoboto.ShapeBase):
    """
    Represents the equivalent of a Hive user-defined function (`UDF`) definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                autoboto.TypeInfo(str),
            ),
            (
                "class_name",
                "ClassName",
                autoboto.TypeInfo(str),
            ),
            (
                "owner_name",
                "OwnerName",
                autoboto.TypeInfo(str),
            ),
            (
                "owner_type",
                "OwnerType",
                autoboto.TypeInfo(PrincipalType),
            ),
            (
                "create_time",
                "CreateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "resource_uris",
                "ResourceUris",
                autoboto.TypeInfo(typing.List[ResourceUri]),
            ),
        ]

    # The name of the function.
    function_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Java class that contains the function code.
    class_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The owner of the function.
    owner_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The owner type.
    owner_type: "PrincipalType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time at which the function was created.
    create_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The resource URIs for the function.
    resource_uris: typing.List["ResourceUri"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UserDefinedFunctionInput(autoboto.ShapeBase):
    """
    A structure used to create or updata a user-defined function.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                autoboto.TypeInfo(str),
            ),
            (
                "class_name",
                "ClassName",
                autoboto.TypeInfo(str),
            ),
            (
                "owner_name",
                "OwnerName",
                autoboto.TypeInfo(str),
            ),
            (
                "owner_type",
                "OwnerType",
                autoboto.TypeInfo(PrincipalType),
            ),
            (
                "resource_uris",
                "ResourceUris",
                autoboto.TypeInfo(typing.List[ResourceUri]),
            ),
        ]

    # The name of the function.
    function_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Java class that contains the function code.
    class_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The owner of the function.
    owner_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The owner type.
    owner_type: "PrincipalType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The resource URIs for the function.
    resource_uris: typing.List["ResourceUri"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ValidationException(autoboto.ShapeBase):
    """
    A value could not be validated.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class VersionMismatchException(autoboto.ShapeBase):
    """
    There was a version conflict.
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

    # A message describing the problem.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class XMLClassifier(autoboto.ShapeBase):
    """
    A classifier for `XML` content.
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
                "classification",
                "Classification",
                autoboto.TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated",
                "LastUpdated",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "Version",
                autoboto.TypeInfo(int),
            ),
            (
                "row_tag",
                "RowTag",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the classifier.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An identifier of the data format that the classifier matches.
    classification: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time this classifier was registered.
    creation_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The time this classifier was last updated.
    last_updated: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The version of this classifier.
    version: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The XML tag designating the element that contains each record in an XML
    # document being parsed. Note that this cannot identify a self-closing
    # element (closed by `/>`). An empty row element that contains only
    # attributes can be parsed as long as it ends with a closing tag (for
    # example, `<row item_a="A" item_b="B"></row>` is okay, but `<row item_a="A"
    # item_b="B" />` is not).
    row_tag: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
