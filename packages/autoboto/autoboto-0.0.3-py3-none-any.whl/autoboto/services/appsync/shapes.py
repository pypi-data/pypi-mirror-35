import datetime
import typing
import autoboto
from enum import Enum
import botocore.response
import dataclasses


@dataclasses.dataclass
class ApiKey(autoboto.ShapeBase):
    """
    Describes an API key.

    Customers invoke AWS AppSync GraphQL APIs with API keys as an identity
    mechanism. There are two key versions:

    **da1** : This version was introduced at launch in November 2017. These keys
    always expire after 7 days. Key expiration is managed by DynamoDB TTL. The keys
    will cease to be valid after Feb 21, 2018 and should not be used after that
    date.

      * `ListApiKeys` returns the expiration time in milliseconds.

      * `CreateApiKey` returns the expiration time in milliseconds.

      * `UpdateApiKey` is not available for this key version.

      * `DeleteApiKey` deletes the item from the table.

      * Expiration is stored in DynamoDB as milliseconds. This results in a bug where keys are not automatically deleted because DynamoDB expects the TTL to be stored in seconds. As a one-time action, we will delete these keys from the table after Feb 21, 2018.

    **da2** : This version was introduced in February 2018 when AppSync added
    support to extend key expiration.

      * `ListApiKeys` returns the expiration time in seconds.

      * `CreateApiKey` returns the expiration time in seconds and accepts a user-provided expiration time in seconds.

      * `UpdateApiKey` returns the expiration time in seconds and accepts a user-provided expiration time in seconds. Key expiration can only be updated while the key has not expired.

      * `DeleteApiKey` deletes the item from the table.

      * Expiration is stored in DynamoDB as seconds.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "expires",
                "expires",
                autoboto.TypeInfo(int),
            ),
        ]

    # The API key ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A description of the purpose of the API key.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time after which the API key expires. The date is represented as
    # seconds since the epoch, rounded down to the nearest hour.
    expires: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ApiKeyLimitExceededException(autoboto.ShapeBase):
    """
    The API key exceeded a limit. Try your request again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ApiKeyValidityOutOfBoundsException(autoboto.ShapeBase):
    """
    The API key expiration must be set to a value between 1 and 365 days from
    creation (for `CreateApiKey`) or from update (for `UpdateApiKey`).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ApiLimitExceededException(autoboto.ShapeBase):
    """
    The GraphQL API exceeded a limit. Try your request again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class AuthenticationType(Enum):
    API_KEY = "API_KEY"
    AWS_IAM = "AWS_IAM"
    AMAZON_COGNITO_USER_POOLS = "AMAZON_COGNITO_USER_POOLS"
    OPENID_CONNECT = "OPENID_CONNECT"


@dataclasses.dataclass
class BadRequestException(autoboto.ShapeBase):
    """
    The request is not well formed. For example, a value is invalid or a required
    field is missing. Check the field values, and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class Blob(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class ConcurrentModificationException(autoboto.ShapeBase):
    """
    Another modification is being made. That modification must complete before you
    can make your change.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateApiKeyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "expires",
                "expires",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID for your GraphQL API.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A description of the purpose of the API key.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time from creation time after which the API key expires. The date is
    # represented as seconds since the epoch, rounded down to the nearest hour.
    # The default value for this parameter is 7 days from creation time. For more
    # information, see .
    expires: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class CreateApiKeyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_key",
                "apiKey",
                autoboto.TypeInfo(ApiKey),
            ),
        ]

    # The API key.
    api_key: "ApiKey" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateDataSourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "type",
                autoboto.TypeInfo(DataSourceType),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "service_role_arn",
                "serviceRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "dynamodb_config",
                "dynamodbConfig",
                autoboto.TypeInfo(DynamodbDataSourceConfig),
            ),
            (
                "lambda_config",
                "lambdaConfig",
                autoboto.TypeInfo(LambdaDataSourceConfig),
            ),
            (
                "elasticsearch_config",
                "elasticsearchConfig",
                autoboto.TypeInfo(ElasticsearchDataSourceConfig),
            ),
            (
                "http_config",
                "httpConfig",
                autoboto.TypeInfo(HttpDataSourceConfig),
            ),
        ]

    # The API ID for the GraphQL API for the `DataSource`.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A user-supplied name for the `DataSource`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of the `DataSource`.
    type: "DataSourceType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A description of the `DataSource`.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The IAM service role ARN for the data source. The system assumes this role
    # when accessing the data source.
    service_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # DynamoDB settings.
    dynamodb_config: "DynamodbDataSourceConfig" = dataclasses.field(
        default_factory=dict,
    )

    # AWS Lambda settings.
    lambda_config: "LambdaDataSourceConfig" = dataclasses.field(
        default_factory=dict,
    )

    # Amazon Elasticsearch settings.
    elasticsearch_config: "ElasticsearchDataSourceConfig" = dataclasses.field(
        default_factory=dict,
    )

    # Http endpoint settings.
    http_config: "HttpDataSourceConfig" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateDataSourceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source",
                "dataSource",
                autoboto.TypeInfo(DataSource),
            ),
        ]

    # The `DataSource` object.
    data_source: "DataSource" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateGraphqlApiRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_type",
                "authenticationType",
                autoboto.TypeInfo(AuthenticationType),
            ),
            (
                "log_config",
                "logConfig",
                autoboto.TypeInfo(LogConfig),
            ),
            (
                "user_pool_config",
                "userPoolConfig",
                autoboto.TypeInfo(UserPoolConfig),
            ),
            (
                "open_id_connect_config",
                "openIDConnectConfig",
                autoboto.TypeInfo(OpenIDConnectConfig),
            ),
        ]

    # A user-supplied name for the `GraphqlApi`.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The authentication type: API key, IAM, or Amazon Cognito User Pools.
    authentication_type: "AuthenticationType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon CloudWatch logs configuration.
    log_config: "LogConfig" = dataclasses.field(default_factory=dict, )

    # The Amazon Cognito User Pool configuration.
    user_pool_config: "UserPoolConfig" = dataclasses.field(
        default_factory=dict,
    )

    # The Open Id Connect configuration configuration.
    open_id_connect_config: "OpenIDConnectConfig" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class CreateGraphqlApiResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "graphql_api",
                "graphqlApi",
                autoboto.TypeInfo(GraphqlApi),
            ),
        ]

    # The `GraphqlApi`.
    graphql_api: "GraphqlApi" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateResolverRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "type_name",
                "typeName",
                autoboto.TypeInfo(str),
            ),
            (
                "field_name",
                "fieldName",
                autoboto.TypeInfo(str),
            ),
            (
                "data_source_name",
                "dataSourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "request_mapping_template",
                "requestMappingTemplate",
                autoboto.TypeInfo(str),
            ),
            (
                "response_mapping_template",
                "responseMappingTemplate",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID for the GraphQL API for which the resolver is being created.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the `Type`.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the field to attach the resolver to.
    field_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the data source for which the resolver is being created.
    data_source_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The mapping template to be used for requests.

    # A resolver uses a request mapping template to convert a GraphQL expression
    # into a format that a data source can understand. Mapping templates are
    # written in Apache Velocity Template Language (VTL).
    request_mapping_template: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The mapping template to be used for responses from the data source.
    response_mapping_template: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateResolverResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resolver",
                "resolver",
                autoboto.TypeInfo(Resolver),
            ),
        ]

    # The `Resolver` object.
    resolver: "Resolver" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateTypeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "definition",
                "definition",
                autoboto.TypeInfo(str),
            ),
            (
                "format",
                "format",
                autoboto.TypeInfo(TypeDefinitionFormat),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type definition, in GraphQL Schema Definition Language (SDL) format.

    # For more information, see the [GraphQL SDL
    # documentation](http://graphql.org/learn/schema/).
    definition: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type format: SDL or JSON.
    format: "TypeDefinitionFormat" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateTypeResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(Type),
            ),
        ]

    # The `Type` object.
    type: "Type" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DataSource(autoboto.ShapeBase):
    """
    Describes a data source.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source_arn",
                "dataSourceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "type",
                autoboto.TypeInfo(DataSourceType),
            ),
            (
                "service_role_arn",
                "serviceRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "dynamodb_config",
                "dynamodbConfig",
                autoboto.TypeInfo(DynamodbDataSourceConfig),
            ),
            (
                "lambda_config",
                "lambdaConfig",
                autoboto.TypeInfo(LambdaDataSourceConfig),
            ),
            (
                "elasticsearch_config",
                "elasticsearchConfig",
                autoboto.TypeInfo(ElasticsearchDataSourceConfig),
            ),
            (
                "http_config",
                "httpConfig",
                autoboto.TypeInfo(HttpDataSourceConfig),
            ),
        ]

    # The data source ARN.
    data_source_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The name of the data source.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The description of the data source.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of the data source.

    #   * **AMAZON_DYNAMODB** : The data source is an Amazon DynamoDB table.

    #   * **AMAZON_ELASTICSEARCH** : The data source is an Amazon Elasticsearch Service domain.

    #   * **AWS_LAMBDA** : The data source is an AWS Lambda function.

    #   * **NONE** : There is no data source. This type is used when when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.

    #   * **HTTP** : The data source is an HTTP endpoint.
    type: "DataSourceType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The IAM service role ARN for the data source. The system assumes this role
    # when accessing the data source.
    service_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # DynamoDB settings.
    dynamodb_config: "DynamodbDataSourceConfig" = dataclasses.field(
        default_factory=dict,
    )

    # Lambda settings.
    lambda_config: "LambdaDataSourceConfig" = dataclasses.field(
        default_factory=dict,
    )

    # Amazon Elasticsearch settings.
    elasticsearch_config: "ElasticsearchDataSourceConfig" = dataclasses.field(
        default_factory=dict,
    )

    # Http endpoint settings.
    http_config: "HttpDataSourceConfig" = dataclasses.field(
        default_factory=dict,
    )


class DataSourceType(Enum):
    AWS_LAMBDA = "AWS_LAMBDA"
    AMAZON_DYNAMODB = "AMAZON_DYNAMODB"
    AMAZON_ELASTICSEARCH = "AMAZON_ELASTICSEARCH"
    NONE = "NONE"
    HTTP = "HTTP"


class DefaultAction(Enum):
    ALLOW = "ALLOW"
    DENY = "DENY"


@dataclasses.dataclass
class DeleteApiKeyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID for the API key.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteApiKeyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteDataSourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the data source.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteDataSourceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteGraphqlApiRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteGraphqlApiResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteResolverRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "type_name",
                "typeName",
                autoboto.TypeInfo(str),
            ),
            (
                "field_name",
                "fieldName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the resolver type.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The resolver field name.
    field_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteResolverResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteTypeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "type_name",
                "typeName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type name.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteTypeResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DynamodbDataSourceConfig(autoboto.ShapeBase):
    """
    Describes a DynamoDB data source configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "tableName",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_region",
                "awsRegion",
                autoboto.TypeInfo(str),
            ),
            (
                "use_caller_credentials",
                "useCallerCredentials",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The table name.
    table_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The AWS region.
    aws_region: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Set to TRUE to use Amazon Cognito credentials with this data source.
    use_caller_credentials: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ElasticsearchDataSourceConfig(autoboto.ShapeBase):
    """
    Describes an Elasticsearch data source configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint",
                "endpoint",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_region",
                "awsRegion",
                autoboto.TypeInfo(str),
            ),
        ]

    # The endpoint.
    endpoint: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The AWS region.
    aws_region: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class FieldLogLevel(Enum):
    NONE = "NONE"
    ERROR = "ERROR"
    ALL = "ALL"


@dataclasses.dataclass
class GetDataSourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the data source.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetDataSourceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source",
                "dataSource",
                autoboto.TypeInfo(DataSource),
            ),
        ]

    # The `DataSource` object.
    data_source: "DataSource" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetGraphqlApiRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The API ID for the GraphQL API.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetGraphqlApiResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "graphql_api",
                "graphqlApi",
                autoboto.TypeInfo(GraphqlApi),
            ),
        ]

    # The `GraphqlApi` object.
    graphql_api: "GraphqlApi" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetIntrospectionSchemaRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "format",
                "format",
                autoboto.TypeInfo(OutputType),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The schema format: SDL or JSON.
    format: "OutputType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetIntrospectionSchemaResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema",
                "schema",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # The schema, in GraphQL Schema Definition Language (SDL) format.

    # For more information, see the [GraphQL SDL
    # documentation](http://graphql.org/learn/schema/).
    schema: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetResolverRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "type_name",
                "typeName",
                autoboto.TypeInfo(str),
            ),
            (
                "field_name",
                "fieldName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The resolver type name.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The resolver field name.
    field_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetResolverResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resolver",
                "resolver",
                autoboto.TypeInfo(Resolver),
            ),
        ]

    # The `Resolver` object.
    resolver: "Resolver" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetSchemaCreationStatusRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetSchemaCreationStatusResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "status",
                autoboto.TypeInfo(SchemaStatus),
            ),
            (
                "details",
                "details",
                autoboto.TypeInfo(str),
            ),
        ]

    # The current state of the schema (PROCESSING, ACTIVE, or DELETING). Once the
    # schema is in the ACTIVE state, you can add data.
    status: "SchemaStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Detailed information about the status of the schema creation operation.
    details: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GetTypeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "type_name",
                "typeName",
                autoboto.TypeInfo(str),
            ),
            (
                "format",
                "format",
                autoboto.TypeInfo(TypeDefinitionFormat),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type name.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type format: SDL or JSON.
    format: "TypeDefinitionFormat" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class GetTypeResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(Type),
            ),
        ]

    # The `Type` object.
    type: "Type" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GraphQLSchemaException(autoboto.ShapeBase):
    """
    The GraphQL schema is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class GraphqlApi(autoboto.ShapeBase):
    """
    Describes a GraphQL API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "authentication_type",
                "authenticationType",
                autoboto.TypeInfo(AuthenticationType),
            ),
            (
                "log_config",
                "logConfig",
                autoboto.TypeInfo(LogConfig),
            ),
            (
                "user_pool_config",
                "userPoolConfig",
                autoboto.TypeInfo(UserPoolConfig),
            ),
            (
                "open_id_connect_config",
                "openIDConnectConfig",
                autoboto.TypeInfo(OpenIDConnectConfig),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "uris",
                "uris",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The API name.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The authentication type.
    authentication_type: "AuthenticationType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The Amazon CloudWatch Logs configuration.
    log_config: "LogConfig" = dataclasses.field(default_factory=dict, )

    # The Amazon Cognito User Pool configuration.
    user_pool_config: "UserPoolConfig" = dataclasses.field(
        default_factory=dict,
    )

    # The Open Id Connect configuration.
    open_id_connect_config: "OpenIDConnectConfig" = dataclasses.field(
        default_factory=dict,
    )

    # The ARN.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The URIs.
    uris: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class HttpDataSourceConfig(autoboto.ShapeBase):
    """
    Describes a Http data source configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint",
                "endpoint",
                autoboto.TypeInfo(str),
            ),
        ]

    # The Http url endpoint. You can either specify the domain name or ip and
    # port combination and the url scheme must be http(s). If the port is not
    # specified, AWS AppSync will use the default port 80 for http endpoint and
    # port 443 for https endpoints.
    endpoint: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InternalFailureException(autoboto.ShapeBase):
    """
    An internal AWS AppSync error occurred. Try your request again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LambdaDataSourceConfig(autoboto.ShapeBase):
    """
    Describes a Lambda data source configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lambda_function_arn",
                "lambdaFunctionArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ARN for the Lambda function.
    lambda_function_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    The request exceeded a limit. Try your request again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListApiKeysRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
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

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results you want the request to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListApiKeysResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_keys",
                "apiKeys",
                autoboto.TypeInfo(typing.List[ApiKey]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `ApiKey` objects.
    api_keys: typing.List["ApiKey"] = dataclasses.field(default_factory=list, )

    # An identifier to be passed in the next request to this operation to return
    # the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListDataSourcesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
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

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results you want the request to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListDataSourcesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_sources",
                "dataSources",
                autoboto.TypeInfo(typing.List[DataSource]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `DataSource` objects.
    data_sources: typing.List["DataSource"] = dataclasses.field(
        default_factory=list,
    )

    # An identifier to be passed in the next request to this operation to return
    # the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListGraphqlApisRequest(autoboto.ShapeBase):
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

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results you want the request to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListGraphqlApisResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "graphql_apis",
                "graphqlApis",
                autoboto.TypeInfo(typing.List[GraphqlApi]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `GraphqlApi` objects.
    graphql_apis: typing.List["GraphqlApi"] = dataclasses.field(
        default_factory=list,
    )

    # An identifier to be passed in the next request to this operation to return
    # the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListResolversRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "type_name",
                "typeName",
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

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type name.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results you want the request to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListResolversResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resolvers",
                "resolvers",
                autoboto.TypeInfo(typing.List[Resolver]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `Resolver` objects.
    resolvers: typing.List["Resolver"] = dataclasses.field(
        default_factory=list,
    )

    # An identifier to be passed in the next request to this operation to return
    # the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListTypesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "format",
                "format",
                autoboto.TypeInfo(TypeDefinitionFormat),
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

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type format: SDL or JSON.
    format: "TypeDefinitionFormat" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of results you want the request to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ListTypesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "types",
                "types",
                autoboto.TypeInfo(typing.List[Type]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `Type` objects.
    types: typing.List["Type"] = dataclasses.field(default_factory=list, )

    # An identifier to be passed in the next request to this operation to return
    # the next set of items in the list.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class LogConfig(autoboto.ShapeBase):
    """
    The CloudWatch Logs configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_log_level",
                "fieldLogLevel",
                autoboto.TypeInfo(FieldLogLevel),
            ),
            (
                "cloud_watch_logs_role_arn",
                "cloudWatchLogsRoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The field logging level. Values can be NONE, ERROR, ALL.

    #   * **NONE** : No field-level logs are captured.

    #   * **ERROR** : Logs the following information only for the fields that are in error:

    #     * The error section in the server response.

    #     * Field-level errors.

    #     * The generated request/response functions that got resolved for error fields.

    #   * **ALL** : The following information is logged for all fields in the query:

    #     * Field-level tracing information.

    #     * The generated request/response functions that got resolved for each field.
    field_log_level: "FieldLogLevel" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The service role that AWS AppSync will assume to publish to Amazon
    # CloudWatch logs in your account.
    cloud_watch_logs_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class NotFoundException(autoboto.ShapeBase):
    """
    The resource specified in the request was not found. Check the resource and try
    again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class OpenIDConnectConfig(autoboto.ShapeBase):
    """
    Describes an Open Id Connect configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "issuer",
                "issuer",
                autoboto.TypeInfo(str),
            ),
            (
                "client_id",
                "clientId",
                autoboto.TypeInfo(str),
            ),
            (
                "iat_ttl",
                "iatTTL",
                autoboto.TypeInfo(int),
            ),
            (
                "auth_ttl",
                "authTTL",
                autoboto.TypeInfo(int),
            ),
        ]

    # The issuer for the open id connect configuration. The issuer returned by
    # discovery MUST exactly match the value of iss in the ID Token.
    issuer: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The client identifier of the Relying party at the OpenID Provider. This
    # identifier is typically obtained when the Relying party is registered with
    # the OpenID Provider. You can specify a regular expression so the AWS
    # AppSync can validate against multiple client identifiers at a time
    client_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of milliseconds a token is valid after being issued to a user.
    iat_ttl: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number of milliseconds a token is valid after being authenticated.
    auth_ttl: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class OutputType(Enum):
    SDL = "SDL"
    JSON = "JSON"


@dataclasses.dataclass
class Resolver(autoboto.ShapeBase):
    """
    Describes a resolver.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "typeName",
                autoboto.TypeInfo(str),
            ),
            (
                "field_name",
                "fieldName",
                autoboto.TypeInfo(str),
            ),
            (
                "data_source_name",
                "dataSourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "resolver_arn",
                "resolverArn",
                autoboto.TypeInfo(str),
            ),
            (
                "request_mapping_template",
                "requestMappingTemplate",
                autoboto.TypeInfo(str),
            ),
            (
                "response_mapping_template",
                "responseMappingTemplate",
                autoboto.TypeInfo(str),
            ),
        ]

    # The resolver type name.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The resolver field name.
    field_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The resolver data source name.
    data_source_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The resolver ARN.
    resolver_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The request mapping template.
    request_mapping_template: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The response mapping template.
    response_mapping_template: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class SchemaStatus(Enum):
    PROCESSING = "PROCESSING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


@dataclasses.dataclass
class StartSchemaCreationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "definition",
                "definition",
                autoboto.TypeInfo(typing.Any),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The schema definition, in GraphQL schema language format.
    definition: typing.Any = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class StartSchemaCreationResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "status",
                autoboto.TypeInfo(SchemaStatus),
            ),
        ]

    # The current state of the schema (PROCESSING, ACTIVE, or DELETING). Once the
    # schema is in the ACTIVE state, you can add data.
    status: "SchemaStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class Type(autoboto.ShapeBase):
    """
    Describes a type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "definition",
                "definition",
                autoboto.TypeInfo(str),
            ),
            (
                "format",
                "format",
                autoboto.TypeInfo(TypeDefinitionFormat),
            ),
        ]

    # The type name.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type description.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type ARN.
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type definition.
    definition: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type format: SDL or JSON.
    format: "TypeDefinitionFormat" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class TypeDefinitionFormat(Enum):
    SDL = "SDL"
    JSON = "JSON"


@dataclasses.dataclass
class UnauthorizedException(autoboto.ShapeBase):
    """
    You are not authorized to perform this operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateApiKeyRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "expires",
                "expires",
                autoboto.TypeInfo(int),
            ),
        ]

    # The ID for the GraphQL API
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The API key ID.
    id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A description of the purpose of the API key.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The time from update time after which the API key expires. The date is
    # represented as seconds since the epoch. For more information, see .
    expires: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateApiKeyResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_key",
                "apiKey",
                autoboto.TypeInfo(ApiKey),
            ),
        ]

    # The API key.
    api_key: "ApiKey" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateDataSourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "type",
                autoboto.TypeInfo(DataSourceType),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "service_role_arn",
                "serviceRoleArn",
                autoboto.TypeInfo(str),
            ),
            (
                "dynamodb_config",
                "dynamodbConfig",
                autoboto.TypeInfo(DynamodbDataSourceConfig),
            ),
            (
                "lambda_config",
                "lambdaConfig",
                autoboto.TypeInfo(LambdaDataSourceConfig),
            ),
            (
                "elasticsearch_config",
                "elasticsearchConfig",
                autoboto.TypeInfo(ElasticsearchDataSourceConfig),
            ),
            (
                "http_config",
                "httpConfig",
                autoboto.TypeInfo(HttpDataSourceConfig),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new name for the data source.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new data source type.
    type: "DataSourceType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The new description for the data source.
    description: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new service role ARN for the data source.
    service_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The new DynamoDB configuration.
    dynamodb_config: "DynamodbDataSourceConfig" = dataclasses.field(
        default_factory=dict,
    )

    # The new Lambda configuration.
    lambda_config: "LambdaDataSourceConfig" = dataclasses.field(
        default_factory=dict,
    )

    # The new Elasticsearch configuration.
    elasticsearch_config: "ElasticsearchDataSourceConfig" = dataclasses.field(
        default_factory=dict,
    )

    # The new http endpoint configuration
    http_config: "HttpDataSourceConfig" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateDataSourceResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source",
                "dataSource",
                autoboto.TypeInfo(DataSource),
            ),
        ]

    # The updated `DataSource` object.
    data_source: "DataSource" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateGraphqlApiRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "log_config",
                "logConfig",
                autoboto.TypeInfo(LogConfig),
            ),
            (
                "authentication_type",
                "authenticationType",
                autoboto.TypeInfo(AuthenticationType),
            ),
            (
                "user_pool_config",
                "userPoolConfig",
                autoboto.TypeInfo(UserPoolConfig),
            ),
            (
                "open_id_connect_config",
                "openIDConnectConfig",
                autoboto.TypeInfo(OpenIDConnectConfig),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new name for the `GraphqlApi` object.
    name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The Amazon CloudWatch logs configuration for the `GraphqlApi` object.
    log_config: "LogConfig" = dataclasses.field(default_factory=dict, )

    # The new authentication type for the `GraphqlApi` object.
    authentication_type: "AuthenticationType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The new Amazon Cognito User Pool configuration for the `GraphqlApi` object.
    user_pool_config: "UserPoolConfig" = dataclasses.field(
        default_factory=dict,
    )

    # The Open Id Connect configuration configuration for the `GraphqlApi`
    # object.
    open_id_connect_config: "OpenIDConnectConfig" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class UpdateGraphqlApiResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "graphql_api",
                "graphqlApi",
                autoboto.TypeInfo(GraphqlApi),
            ),
        ]

    # The updated `GraphqlApi` object.
    graphql_api: "GraphqlApi" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateResolverRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "type_name",
                "typeName",
                autoboto.TypeInfo(str),
            ),
            (
                "field_name",
                "fieldName",
                autoboto.TypeInfo(str),
            ),
            (
                "data_source_name",
                "dataSourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "request_mapping_template",
                "requestMappingTemplate",
                autoboto.TypeInfo(str),
            ),
            (
                "response_mapping_template",
                "responseMappingTemplate",
                autoboto.TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new type name.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new field name.
    field_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new data source name.
    data_source_name: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The new request mapping template.
    request_mapping_template: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The new response mapping template.
    response_mapping_template: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class UpdateResolverResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resolver",
                "resolver",
                autoboto.TypeInfo(Resolver),
            ),
        ]

    # The updated `Resolver` object.
    resolver: "Resolver" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateTypeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_id",
                "apiId",
                autoboto.TypeInfo(str),
            ),
            (
                "type_name",
                "typeName",
                autoboto.TypeInfo(str),
            ),
            (
                "format",
                "format",
                autoboto.TypeInfo(TypeDefinitionFormat),
            ),
            (
                "definition",
                "definition",
                autoboto.TypeInfo(str),
            ),
        ]

    # The API ID.
    api_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new type name.
    type_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The new type format: SDL or JSON.
    format: "TypeDefinitionFormat" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The new definition.
    definition: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UpdateTypeResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                autoboto.TypeInfo(Type),
            ),
        ]

    # The updated `Type` object.
    type: "Type" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UserPoolConfig(autoboto.ShapeBase):
    """
    Describes an Amazon Cognito User Pool configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_id",
                "userPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_region",
                "awsRegion",
                autoboto.TypeInfo(str),
            ),
            (
                "default_action",
                "defaultAction",
                autoboto.TypeInfo(DefaultAction),
            ),
            (
                "app_id_client_regex",
                "appIdClientRegex",
                autoboto.TypeInfo(str),
            ),
        ]

    # The user pool ID.
    user_pool_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The AWS region in which the user pool was created.
    aws_region: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The action that you want your GraphQL API to take when a request that uses
    # Amazon Cognito User Pool authentication doesn't match the Amazon Cognito
    # User Pool configuration.
    default_action: "DefaultAction" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A regular expression for validating the incoming Amazon Cognito User Pool
    # app client ID.
    app_id_client_regex: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )
