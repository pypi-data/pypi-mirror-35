import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class BatchGetNamedQueryInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "named_query_ids",
                "NamedQueryIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # An array of query IDs.
    named_query_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchGetNamedQueryOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "named_queries",
                "NamedQueries",
                autoboto.TypeInfo(typing.List[NamedQuery]),
            ),
            (
                "unprocessed_named_query_ids",
                "UnprocessedNamedQueryIds",
                autoboto.TypeInfo(typing.List[UnprocessedNamedQueryId]),
            ),
        ]

    # Information about the named query IDs submitted.
    named_queries: typing.List["NamedQuery"] = dataclasses.field(
        default_factory=list,
    )

    # Information about provided query IDs.
    unprocessed_named_query_ids: typing.List["UnprocessedNamedQueryId"
                                            ] = dataclasses.field(
                                                default_factory=list,
                                            )


@dataclasses.dataclass
class BatchGetQueryExecutionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_execution_ids",
                "QueryExecutionIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # An array of query execution IDs.
    query_execution_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class BatchGetQueryExecutionOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_executions",
                "QueryExecutions",
                autoboto.TypeInfo(typing.List[QueryExecution]),
            ),
            (
                "unprocessed_query_execution_ids",
                "UnprocessedQueryExecutionIds",
                autoboto.TypeInfo(typing.List[UnprocessedQueryExecutionId]),
            ),
        ]

    # Information about a query execution.
    query_executions: typing.List["QueryExecution"] = dataclasses.field(
        default_factory=list,
    )

    # Information about the query executions that failed to run.
    unprocessed_query_execution_ids: typing.List["UnprocessedQueryExecutionId"
                                                ] = dataclasses.field(
                                                    default_factory=list,
                                                )


@dataclasses.dataclass
class ColumnInfo(autoboto.ShapeBase):
    """
    Information about the columns in a query execution result.
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
                "catalog_name",
                "CatalogName",
                autoboto.TypeInfo(str),
            ),
            (
                "schema_name",
                "SchemaName",
                autoboto.TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                autoboto.TypeInfo(str),
            ),
            (
                "label",
                "Label",
                autoboto.TypeInfo(str),
            ),
            (
                "precision",
                "Precision",
                autoboto.TypeInfo(int),
            ),
            (
                "scale",
                "Scale",
                autoboto.TypeInfo(int),
            ),
            (
                "nullable",
                "Nullable",
                autoboto.TypeInfo(ColumnNullable),
            ),
            (
                "case_sensitive",
                "CaseSensitive",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the column.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The data type of the column.
    type: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The catalog to which the query results belong.
    catalog_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The schema name (database name) to which the query results belong.
    schema_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The table name for the query results.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A column label.
    label: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # For `DECIMAL` data types, specifies the total number of digits, up to 38.
    # For performance reasons, we recommend up to 18 digits.
    precision: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # For `DECIMAL` data types, specifies the total number of digits in the
    # fractional part of the value. Defaults to 0.
    scale: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Indicates the column's nullable status.
    nullable: "ColumnNullable" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Indicates whether values in the column are case-sensitive.
    case_sensitive: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class ColumnNullable(Enum):
    NOT_NULL = "NOT_NULL"
    NULLABLE = "NULLABLE"
    UNKNOWN = "UNKNOWN"


@dataclasses.dataclass
class CreateNamedQueryInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                autoboto.TypeInfo(str),
            ),
            (
                "database",
                "Database",
                autoboto.TypeInfo(str),
            ),
            (
                "query_string",
                "QueryString",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The plain language name for the query.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The database to which the query belongs.
    database: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The text of the query itself. In other words, all query statements.
    query_string: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A brief explanation of the query.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A unique case-sensitive string used to ensure the request to create the
    # query is idempotent (executes only once). If another `CreateNamedQuery`
    # request is received, the same response is returned and another query is not
    # created. If a parameter has changed, for example, the `QueryString`, an
    # error is returned.

    # This token is listed as not required because AWS SDKs (for example the AWS
    # SDK for Java) auto-generate the token for users. If you are not using the
    # AWS SDK or the AWS CLI, you must provide this token or the action will
    # fail.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateNamedQueryOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "named_query_id",
                "NamedQueryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the query.
    named_query_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Datum(autoboto.ShapeBase):
    """
    A piece of data (a field in the table).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "var_char_value",
                "VarCharValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The value of the datum.
    var_char_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteNamedQueryInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "named_query_id",
                "NamedQueryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the query to delete.
    named_query_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DeleteNamedQueryOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EncryptionConfiguration(autoboto.ShapeBase):
    """
    If query results are encrypted in Amazon S3, indicates the Amazon S3 encryption
    option used.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption_option",
                "EncryptionOption",
                autoboto.TypeInfo(EncryptionOption),
            ),
            (
                "kms_key",
                "KmsKey",
                autoboto.TypeInfo(str),
            ),
        ]

    # Indicates whether Amazon S3 server-side encryption with Amazon S3-managed
    # keys (`SSE-S3`), server-side encryption with KMS-managed keys (`SSE-KMS`),
    # or client-side encryption with KMS-managed keys (CSE-KMS) is used.
    encryption_option: "EncryptionOption" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # For `SSE-KMS` and `CSE-KMS`, this is the KMS key ARN or ID.
    kms_key: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class EncryptionOption(Enum):
    SSE_S3 = "SSE_S3"
    SSE_KMS = "SSE_KMS"
    CSE_KMS = "CSE_KMS"


@dataclasses.dataclass
class GetNamedQueryInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "named_query_id",
                "NamedQueryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the query. Use ListNamedQueries to get query IDs.
    named_query_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetNamedQueryOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "named_query",
                "NamedQuery",
                autoboto.TypeInfo(NamedQuery),
            ),
        ]

    # Information about the query.
    named_query: "NamedQuery" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetQueryExecutionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_execution_id",
                "QueryExecutionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the query execution.
    query_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetQueryExecutionOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_execution",
                "QueryExecution",
                autoboto.TypeInfo(QueryExecution),
            ),
        ]

    # Information about the query execution.
    query_execution: "QueryExecution" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetQueryResultsInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_execution_id",
                "QueryExecutionId",
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

    # The unique ID of the query execution.
    query_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The token that specifies where to start pagination if a previous request
    # was truncated.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results (rows) to return in this request.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetQueryResultsOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "result_set",
                "ResultSet",
                autoboto.TypeInfo(ResultSet),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The results of the query execution.
    result_set: "ResultSet" = dataclasses.field(default_factory=dict, )

    # A token to be used by the next request if this request is truncated.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InternalServerException(autoboto.ShapeBase):
    """
    Indicates a platform issue, which may be due to a transient condition or outage.
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

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidRequestException(autoboto.ShapeBase):
    """
    Indicates that something is wrong with the input to the request. For example, a
    required parameter may be missing or out of range.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "athena_error_code",
                "AthenaErrorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    athena_error_code: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListNamedQueriesInput(autoboto.ShapeBase):
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

    # The token that specifies where to start pagination if a previous request
    # was truncated.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of queries to return in this request.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListNamedQueriesOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "named_query_ids",
                "NamedQueryIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of unique query IDs.
    named_query_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A token to be used by the next request if this request is truncated.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListQueryExecutionsInput(autoboto.ShapeBase):
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

    # The token that specifies where to start pagination if a previous request
    # was truncated.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of query executions to return in this request.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListQueryExecutionsOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_execution_ids",
                "QueryExecutionIds",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique IDs of each query execution as an array of strings.
    query_execution_ids: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A token to be used by the next request if this request is truncated.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class NamedQuery(autoboto.ShapeBase):
    """
    A query, where `QueryString` is the SQL query statements that comprise the
    query.
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
                "database",
                "Database",
                autoboto.TypeInfo(str),
            ),
            (
                "query_string",
                "QueryString",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "Description",
                autoboto.TypeInfo(str),
            ),
            (
                "named_query_id",
                "NamedQueryId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The plain-language name of the query.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The database to which the query belongs.
    database: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The SQL query statements that comprise the query.
    query_string: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A brief description of the query.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique identifier of the query.
    named_query_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class QueryExecution(autoboto.ShapeBase):
    """
    Information about a single instance of a query execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_execution_id",
                "QueryExecutionId",
                autoboto.TypeInfo(str),
            ),
            (
                "query",
                "Query",
                autoboto.TypeInfo(str),
            ),
            (
                "result_configuration",
                "ResultConfiguration",
                autoboto.TypeInfo(ResultConfiguration),
            ),
            (
                "query_execution_context",
                "QueryExecutionContext",
                autoboto.TypeInfo(QueryExecutionContext),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(QueryExecutionStatus),
            ),
            (
                "statistics",
                "Statistics",
                autoboto.TypeInfo(QueryExecutionStatistics),
            ),
        ]

    # The unique identifier for each query execution.
    query_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The SQL query statements which the query execution ran.
    query: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The location in Amazon S3 where query results were stored and the
    # encryption option, if any, used for query results.
    result_configuration: "ResultConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The database in which the query execution occurred.
    query_execution_context: "QueryExecutionContext" = dataclasses.field(
        default_factory=dict,
    )

    # The completion date, current state, submission time, and state change
    # reason (if applicable) for the query execution.
    status: "QueryExecutionStatus" = dataclasses.field(default_factory=dict, )

    # The amount of data scanned during the query execution and the amount of
    # time that it took to execute.
    statistics: "QueryExecutionStatistics" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class QueryExecutionContext(autoboto.ShapeBase):
    """
    The database in which the query execution occurs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database",
                "Database",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the database.
    database: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class QueryExecutionState(Enum):
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


@dataclasses.dataclass
class QueryExecutionStatistics(autoboto.ShapeBase):
    """
    The amount of data scanned during the query execution and the amount of time
    that it took to execute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "engine_execution_time_in_millis",
                "EngineExecutionTimeInMillis",
                autoboto.TypeInfo(int),
            ),
            (
                "data_scanned_in_bytes",
                "DataScannedInBytes",
                autoboto.TypeInfo(int),
            ),
        ]

    # The number of milliseconds that the query took to execute.
    engine_execution_time_in_millis: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of bytes in the data that was queried.
    data_scanned_in_bytes: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class QueryExecutionStatus(autoboto.ShapeBase):
    """
    The completion date, current state, submission time, and state change reason (if
    applicable) for the query execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "State",
                autoboto.TypeInfo(QueryExecutionState),
            ),
            (
                "state_change_reason",
                "StateChangeReason",
                autoboto.TypeInfo(str),
            ),
            (
                "submission_date_time",
                "SubmissionDateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "completion_date_time",
                "CompletionDateTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The state of query execution. `SUBMITTED` indicates that the query is
    # queued for execution. `RUNNING` indicates that the query is scanning data
    # and returning results. `SUCCEEDED` indicates that the query completed
    # without error. `FAILED` indicates that the query experienced an error and
    # did not complete processing. `CANCELLED` indicates that user input
    # interrupted query execution.
    state: "QueryExecutionState" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Further detail about the status of the query.
    state_change_reason: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time that the query was submitted.
    submission_date_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time that the query completed.
    completion_date_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ResultConfiguration(autoboto.ShapeBase):
    """
    The location in Amazon S3 where query results are stored and the encryption
    option, if any, used for query results.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_location",
                "OutputLocation",
                autoboto.TypeInfo(str),
            ),
            (
                "encryption_configuration",
                "EncryptionConfiguration",
                autoboto.TypeInfo(EncryptionConfiguration),
            ),
        ]

    # The location in S3 where query results are stored.
    output_location: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # If query results are encrypted in S3, indicates the S3 encryption option
    # used (for example, `SSE-KMS` or `CSE-KMS` and key information.
    encryption_configuration: "EncryptionConfiguration" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ResultSet(autoboto.ShapeBase):
    """
    The metadata and rows that comprise a query result set. The metadata describes
    the column structure and data types.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rows",
                "Rows",
                autoboto.TypeInfo(typing.List[Row]),
            ),
            (
                "result_set_metadata",
                "ResultSetMetadata",
                autoboto.TypeInfo(ResultSetMetadata),
            ),
        ]

    # The rows in the table.
    rows: typing.List["Row"] = dataclasses.field(default_factory=list, )

    # The metadata that describes the column structure and data types of a table
    # of query results.
    result_set_metadata: "ResultSetMetadata" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class ResultSetMetadata(autoboto.ShapeBase):
    """
    The metadata that describes the column structure and data types of a table of
    query results.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "column_info",
                "ColumnInfo",
                autoboto.TypeInfo(typing.List[ColumnInfo]),
            ),
        ]

    # Information about the columns in a query execution result.
    column_info: typing.List["ColumnInfo"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Row(autoboto.ShapeBase):
    """
    The rows that comprise a query result table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data",
                "Data",
                autoboto.TypeInfo(typing.List[Datum]),
            ),
        ]

    # The data that populates a row in a query result table.
    data: typing.List["Datum"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class StartQueryExecutionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_string",
                "QueryString",
                autoboto.TypeInfo(str),
            ),
            (
                "result_configuration",
                "ResultConfiguration",
                autoboto.TypeInfo(ResultConfiguration),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                autoboto.TypeInfo(str),
            ),
            (
                "query_execution_context",
                "QueryExecutionContext",
                autoboto.TypeInfo(QueryExecutionContext),
            ),
        ]

    # The SQL query statements to be executed.
    query_string: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies information about where and how to save the results of the query
    # execution.
    result_configuration: "ResultConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # A unique case-sensitive string used to ensure the request to create the
    # query is idempotent (executes only once). If another `StartQueryExecution`
    # request is received, the same response is returned and another query is not
    # created. If a parameter has changed, for example, the `QueryString`, an
    # error is returned.

    # This token is listed as not required because AWS SDKs (for example the AWS
    # SDK for Java) auto-generate the token for users. If you are not using the
    # AWS SDK or the AWS CLI, you must provide this token or the action will
    # fail.
    client_request_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The database within which the query executes.
    query_execution_context: "QueryExecutionContext" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class StartQueryExecutionOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_execution_id",
                "QueryExecutionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the query that ran as a result of this request.
    query_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class StopQueryExecutionInput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_execution_id",
                "QueryExecutionId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique ID of the query execution to stop.
    query_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class StopQueryExecutionOutput(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


class ThrottleReason(Enum):
    CONCURRENT_QUERY_LIMIT_EXCEEDED = "CONCURRENT_QUERY_LIMIT_EXCEEDED"


@dataclasses.dataclass
class TooManyRequestsException(autoboto.ShapeBase):
    """
    Indicates that the request was throttled.
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
                "reason",
                "Reason",
                autoboto.TypeInfo(ThrottleReason),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )
    reason: "ThrottleReason" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UnprocessedNamedQueryId(autoboto.ShapeBase):
    """
    Information about a named query ID that could not be processed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "named_query_id",
                "NamedQueryId",
                autoboto.TypeInfo(str),
            ),
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

    # The unique identifier of the named query.
    named_query_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The error code returned when the processing request for the named query
    # failed, if applicable.
    error_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The error message returned when the processing request for the named query
    # failed, if applicable.
    error_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UnprocessedQueryExecutionId(autoboto.ShapeBase):
    """
    Describes a query execution that failed to process.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_execution_id",
                "QueryExecutionId",
                autoboto.TypeInfo(str),
            ),
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

    # The unique identifier of the query execution.
    query_execution_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The error code returned when the query execution failed to process, if
    # applicable.
    error_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The error message returned when the query execution failed to process, if
    # applicable.
    error_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
