import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


class AmbiguousRoleResolutionType(Enum):
    AuthenticatedRole = "AuthenticatedRole"
    Deny = "Deny"


@dataclasses.dataclass
class CognitoIdentityProvider(autoboto.ShapeBase):
    """
    A provider representing an Amazon Cognito Identity User Pool and its client ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "provider_name",
                "ProviderName",
                autoboto.TypeInfo(str),
            ),
            (
                "client_id",
                "ClientId",
                autoboto.TypeInfo(str),
            ),
            (
                "server_side_token_check",
                "ServerSideTokenCheck",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The provider name for an Amazon Cognito Identity User Pool. For example,
    # `cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`.
    provider_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The client ID for the Amazon Cognito Identity User Pool.
    client_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # TRUE if server-side token validation is enabled for the identity provider’s
    # token.
    server_side_token_check: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConcurrentModificationException(autoboto.ShapeBase):
    """
    Thrown if there are parallel requests to modify a resource.
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

    # The message returned by a ConcurrentModificationException.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateIdentityPoolInput(autoboto.ShapeBase):
    """
    Input to the CreateIdentityPool action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_name",
                "IdentityPoolName",
                autoboto.TypeInfo(str),
            ),
            (
                "allow_unauthenticated_identities",
                "AllowUnauthenticatedIdentities",
                autoboto.TypeInfo(bool),
            ),
            (
                "supported_login_providers",
                "SupportedLoginProviders",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "developer_provider_name",
                "DeveloperProviderName",
                autoboto.TypeInfo(str),
            ),
            (
                "open_id_connect_provider_arns",
                "OpenIdConnectProviderARNs",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "cognito_identity_providers",
                "CognitoIdentityProviders",
                autoboto.TypeInfo(typing.List[CognitoIdentityProvider]),
            ),
            (
                "saml_provider_arns",
                "SamlProviderARNs",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A string that you provide.
    identity_pool_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # TRUE if the identity pool supports unauthenticated logins.
    allow_unauthenticated_identities: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional key:value pairs mapping provider names to provider app IDs.
    supported_login_providers: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The "domain" by which Cognito will refer to your users. This name acts as a
    # placeholder that allows your backend and the Cognito service to communicate
    # about the developer provider. For the `DeveloperProviderName`, you can use
    # letters as well as period (`.`), underscore (`_`), and dash (`-`).

    # Once you have set a developer provider name, you cannot change it. Please
    # take care in setting this parameter.
    developer_provider_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of OpendID Connect provider ARNs.
    open_id_connect_provider_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # An array of Amazon Cognito Identity user pools and their client IDs.
    cognito_identity_providers: typing.List["CognitoIdentityProvider"
                                           ] = dataclasses.field(
                                               default_factory=list,
                                           )

    # An array of Amazon Resource Names (ARNs) of the SAML provider for your
    # identity pool.
    saml_provider_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Credentials(autoboto.ShapeBase):
    """
    Credentials for the provided identity ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_key_id",
                "AccessKeyId",
                autoboto.TypeInfo(str),
            ),
            (
                "secret_key",
                "SecretKey",
                autoboto.TypeInfo(str),
            ),
            (
                "session_token",
                "SessionToken",
                autoboto.TypeInfo(str),
            ),
            (
                "expiration",
                "Expiration",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The Access Key portion of the credentials.
    access_key_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Secret Access Key portion of the credentials
    secret_key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Session Token portion of the credentials
    session_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date at which these credentials will expire.
    expiration: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteIdentitiesInput(autoboto.ShapeBase):
    """
    Input to the `DeleteIdentities` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_ids_to_delete",
                "IdentityIdsToDelete",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A list of 1-60 identities that you want to delete.
    identity_ids_to_delete: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DeleteIdentitiesResponse(autoboto.ShapeBase):
    """
    Returned in response to a successful `DeleteIdentities` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "unprocessed_identity_ids",
                "UnprocessedIdentityIds",
                autoboto.TypeInfo(typing.List[UnprocessedIdentityId]),
            ),
        ]

    # An array of UnprocessedIdentityId objects, each of which contains an
    # ErrorCode and IdentityId.
    unprocessed_identity_ids: typing.List["UnprocessedIdentityId"
                                         ] = dataclasses.field(
                                             default_factory=list,
                                         )


@dataclasses.dataclass
class DeleteIdentityPoolInput(autoboto.ShapeBase):
    """
    Input to the DeleteIdentityPool action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                autoboto.TypeInfo(str),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeIdentityInput(autoboto.ShapeBase):
    """
    Input to the `DescribeIdentity` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeIdentityPoolInput(autoboto.ShapeBase):
    """
    Input to the DescribeIdentityPool action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                autoboto.TypeInfo(str),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeveloperUserAlreadyRegisteredException(autoboto.ShapeBase):
    """
    The provided developer user identifier is already registered with Cognito under
    a different identity ID.
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

    # This developer user identifier is already registered with Cognito.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class ErrorCode(Enum):
    AccessDenied = "AccessDenied"
    InternalServerError = "InternalServerError"


@dataclasses.dataclass
class ExternalServiceException(autoboto.ShapeBase):
    """
    An exception thrown when a dependent service such as Facebook or Twitter is not
    responding
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

    # The message returned by an ExternalServiceException
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCredentialsForIdentityInput(autoboto.ShapeBase):
    """
    Input to the `GetCredentialsForIdentity` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                autoboto.TypeInfo(str),
            ),
            (
                "logins",
                "Logins",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "custom_role_arn",
                "CustomRoleArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A set of optional name-value pairs that map provider names to provider
    # tokens.
    logins: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the role to be assumed when multiple
    # roles were received in the token from the identity provider. For example, a
    # SAML-based identity provider. This parameter is optional for identity
    # providers that do not support role customization.
    custom_role_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetCredentialsForIdentityResponse(autoboto.ShapeBase):
    """
    Returned in response to a successful `GetCredentialsForIdentity` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                autoboto.TypeInfo(str),
            ),
            (
                "credentials",
                "Credentials",
                autoboto.TypeInfo(Credentials),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Credentials for the provided identity ID.
    credentials: "Credentials" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetIdInput(autoboto.ShapeBase):
    """
    Input to the GetId action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "logins",
                "Logins",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A standard AWS account ID (9+ digits).
    account_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A set of optional name-value pairs that map provider names to provider
    # tokens. The available provider names for `Logins` are as follows:

    #   * Facebook: `graph.facebook.com`

    #   * Amazon Cognito Identity Provider: `cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`

    #   * Google: `accounts.google.com`

    #   * Amazon: `www.amazon.com`

    #   * Twitter: `api.twitter.com`

    #   * Digits: `www.digits.com`
    logins: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetIdResponse(autoboto.ShapeBase):
    """
    Returned in response to a GetId request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetIdentityPoolRolesInput(autoboto.ShapeBase):
    """
    Input to the `GetIdentityPoolRoles` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                autoboto.TypeInfo(str),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetIdentityPoolRolesResponse(autoboto.ShapeBase):
    """
    Returned in response to a successful `GetIdentityPoolRoles` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "roles",
                "Roles",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "role_mappings",
                "RoleMappings",
                autoboto.TypeInfo(typing.Dict[str, RoleMapping]),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The map of roles associated with this pool. Currently only authenticated
    # and unauthenticated roles are supported.
    roles: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # How users for a specific identity provider are to mapped to roles. This is
    # a String-to-RoleMapping object map. The string identifies the identity
    # provider, for example, "graph.facebook.com" or "cognito-idp-
    # east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id".
    role_mappings: typing.Dict[str, "RoleMapping"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetOpenIdTokenForDeveloperIdentityInput(autoboto.ShapeBase):
    """
    Input to the `GetOpenIdTokenForDeveloperIdentity` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "logins",
                "Logins",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "identity_id",
                "IdentityId",
                autoboto.TypeInfo(str),
            ),
            (
                "token_duration",
                "TokenDuration",
                autoboto.TypeInfo(int),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A set of optional name-value pairs that map provider names to provider
    # tokens. Each name-value pair represents a user from a public provider or
    # developer provider. If the user is from a developer provider, the name-
    # value pair will follow the syntax `"developer_provider_name":
    # "developer_user_identifier"`. The developer provider is the "domain" by
    # which Cognito will refer to your users; you provided this domain while
    # creating/updating the identity pool. The developer user identifier is an
    # identifier from your backend that uniquely identifies a user. When you
    # create an identity pool, you can specify the supported logins.
    logins: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The expiration time of the token, in seconds. You can specify a custom
    # expiration time for the token so that you can cache it. If you don't
    # provide an expiration time, the token is valid for 15 minutes. You can
    # exchange the token with Amazon STS for temporary AWS credentials, which are
    # valid for a maximum of one hour. The maximum token duration you can set is
    # 24 hours. You should take care in setting the expiration time for a token,
    # as there are significant security implications: an attacker could use a
    # leaked token to access your AWS resources for the token's duration.
    token_duration: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetOpenIdTokenForDeveloperIdentityResponse(autoboto.ShapeBase):
    """
    Returned in response to a successful `GetOpenIdTokenForDeveloperIdentity`
    request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                autoboto.TypeInfo(str),
            ),
            (
                "token",
                "Token",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An OpenID token.
    token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOpenIdTokenInput(autoboto.ShapeBase):
    """
    Input to the GetOpenIdToken action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                autoboto.TypeInfo(str),
            ),
            (
                "logins",
                "Logins",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A set of optional name-value pairs that map provider names to provider
    # tokens. When using graph.facebook.com and www.amazon.com, supply the
    # access_token returned from the provider's authflow. For
    # accounts.google.com, an Amazon Cognito Identity Provider, or any other
    # OpenId Connect provider, always include the `id_token`.
    logins: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetOpenIdTokenResponse(autoboto.ShapeBase):
    """
    Returned in response to a successful GetOpenIdToken request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                autoboto.TypeInfo(str),
            ),
            (
                "token",
                "Token",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier in the format REGION:GUID. Note that the IdentityId
    # returned may not match the one passed on input.
    identity_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An OpenID token, valid for 15 minutes.
    token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IdentityDescription(autoboto.ShapeBase):
    """
    A description of the identity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                autoboto.TypeInfo(str),
            ),
            (
                "logins",
                "Logins",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "creation_date",
                "CreationDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A set of optional name-value pairs that map provider names to provider
    # tokens.
    logins: typing.List[str] = dataclasses.field(default_factory=list, )

    # Date on which the identity was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Date on which the identity was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class IdentityPool(autoboto.ShapeBase):
    """
    An object representing an Amazon Cognito identity pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "identity_pool_name",
                "IdentityPoolName",
                autoboto.TypeInfo(str),
            ),
            (
                "allow_unauthenticated_identities",
                "AllowUnauthenticatedIdentities",
                autoboto.TypeInfo(bool),
            ),
            (
                "supported_login_providers",
                "SupportedLoginProviders",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "developer_provider_name",
                "DeveloperProviderName",
                autoboto.TypeInfo(str),
            ),
            (
                "open_id_connect_provider_arns",
                "OpenIdConnectProviderARNs",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "cognito_identity_providers",
                "CognitoIdentityProviders",
                autoboto.TypeInfo(typing.List[CognitoIdentityProvider]),
            ),
            (
                "saml_provider_arns",
                "SamlProviderARNs",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string that you provide.
    identity_pool_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # TRUE if the identity pool supports unauthenticated logins.
    allow_unauthenticated_identities: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Optional key:value pairs mapping provider names to provider app IDs.
    supported_login_providers: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The "domain" by which Cognito will refer to your users.
    developer_provider_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of OpendID Connect provider ARNs.
    open_id_connect_provider_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list representing an Amazon Cognito Identity User Pool and its client ID.
    cognito_identity_providers: typing.List["CognitoIdentityProvider"
                                           ] = dataclasses.field(
                                               default_factory=list,
                                           )

    # An array of Amazon Resource Names (ARNs) of the SAML provider for your
    # identity pool.
    saml_provider_arns: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class IdentityPoolShortDescription(autoboto.ShapeBase):
    """
    A description of the identity pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "identity_pool_name",
                "IdentityPoolName",
                autoboto.TypeInfo(str),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A string that you provide.
    identity_pool_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalErrorException(autoboto.ShapeBase):
    """
    Thrown when the service encounters an error during processing the request.
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

    # The message returned by an InternalErrorException.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidIdentityPoolConfigurationException(autoboto.ShapeBase):
    """
    Thrown if the identity pool has no role associated for the given auth type
    (auth/unauth) or if the AssumeRole fails.
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

    # The message returned for an `InvalidIdentityPoolConfigurationException`
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterException(autoboto.ShapeBase):
    """
    Thrown for missing or bad input parameter(s).
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

    # The message returned by an InvalidParameterException.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(autoboto.ShapeBase):
    """
    Thrown when the total number of user pools has exceeded a preset limit.
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

    # The message returned by a LimitExceededException.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListIdentitiesInput(autoboto.ShapeBase):
    """
    Input to the ListIdentities action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
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
            (
                "hide_disabled",
                "HideDisabled",
                autoboto.TypeInfo(bool),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of identities to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A pagination token.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An optional boolean parameter that allows you to hide disabled identities.
    # If omitted, the ListIdentities API will include disabled identities in the
    # response.
    hide_disabled: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListIdentitiesResponse(autoboto.ShapeBase):
    """
    The response to a ListIdentities request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "identities",
                "Identities",
                autoboto.TypeInfo(typing.List[IdentityDescription]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An object containing a set of identities and associated mappings.
    identities: typing.List["IdentityDescription"] = dataclasses.field(
        default_factory=list,
    )

    # A pagination token.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListIdentityPoolsInput(autoboto.ShapeBase):
    """
    Input to the ListIdentityPools action.
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

    # The maximum number of identities to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A pagination token.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListIdentityPoolsResponse(autoboto.ShapeBase):
    """
    The result of a successful ListIdentityPools action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pools",
                "IdentityPools",
                autoboto.TypeInfo(typing.List[IdentityPoolShortDescription]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The identity pools returned by the ListIdentityPools action.
    identity_pools: typing.List["IdentityPoolShortDescription"
                               ] = dataclasses.field(
                                   default_factory=list,
                               )

    # A pagination token.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LookupDeveloperIdentityInput(autoboto.ShapeBase):
    """
    Input to the `LookupDeveloperIdentityInput` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "identity_id",
                "IdentityId",
                autoboto.TypeInfo(str),
            ),
            (
                "developer_user_identifier",
                "DeveloperUserIdentifier",
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

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A unique ID used by your backend authentication process to identify a user.
    # Typically, a developer identity provider would issue many developer user
    # identifiers, in keeping with the number of users.
    developer_user_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The maximum number of identities to return.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A pagination token. The first call you make will have `NextToken` set to
    # null. After that the service will return `NextToken` values as needed. For
    # example, let's say you make a request with `MaxResults` set to 10, and
    # there are 20 matches in the database. The service will return a pagination
    # token as a part of the response. This token can be used to call the API
    # again and get results starting from the 11th match.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LookupDeveloperIdentityResponse(autoboto.ShapeBase):
    """
    Returned in response to a successful `LookupDeveloperIdentity` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                autoboto.TypeInfo(str),
            ),
            (
                "developer_user_identifier_list",
                "DeveloperUserIdentifierList",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # This is the list of developer user identifiers associated with an identity
    # ID. Cognito supports the association of multiple developer user identifiers
    # with an identity ID.
    developer_user_identifier_list: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A pagination token. The first call you make will have `NextToken` set to
    # null. After that the service will return `NextToken` values as needed. For
    # example, let's say you make a request with `MaxResults` set to 10, and
    # there are 20 matches in the database. The service will return a pagination
    # token as a part of the response. This token can be used to call the API
    # again and get results starting from the 11th match.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MappingRule(autoboto.ShapeBase):
    """
    A rule that maps a claim name, a claim value, and a match type to a role ARN.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "claim",
                "Claim",
                autoboto.TypeInfo(str),
            ),
            (
                "match_type",
                "MatchType",
                autoboto.TypeInfo(MappingRuleMatchType),
            ),
            (
                "value",
                "Value",
                autoboto.TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                autoboto.TypeInfo(str),
            ),
        ]

    # The claim name that must be present in the token, for example, "isAdmin" or
    # "paid".
    claim: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The match condition that specifies how closely the claim value in the IdP
    # token must match `Value`.
    match_type: "MappingRuleMatchType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A brief string that the claim must match, for example, "paid" or "yes".
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The role ARN.
    role_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class MappingRuleMatchType(Enum):
    Equals = "Equals"
    Contains = "Contains"
    StartsWith = "StartsWith"
    NotEqual = "NotEqual"


@dataclasses.dataclass
class MergeDeveloperIdentitiesInput(autoboto.ShapeBase):
    """
    Input to the `MergeDeveloperIdentities` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_user_identifier",
                "SourceUserIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "destination_user_identifier",
                "DestinationUserIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "developer_provider_name",
                "DeveloperProviderName",
                autoboto.TypeInfo(str),
            ),
            (
                "identity_pool_id",
                "IdentityPoolId",
                autoboto.TypeInfo(str),
            ),
        ]

    # User identifier for the source user. The value should be a
    # `DeveloperUserIdentifier`.
    source_user_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # User identifier for the destination user. The value should be a
    # `DeveloperUserIdentifier`.
    destination_user_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The "domain" by which Cognito will refer to your users. This is a (pseudo)
    # domain name that you provide while creating an identity pool. This name
    # acts as a placeholder that allows your backend and the Cognito service to
    # communicate about the developer provider. For the `DeveloperProviderName`,
    # you can use letters as well as period (.), underscore (_), and dash (-).
    developer_provider_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MergeDeveloperIdentitiesResponse(autoboto.ShapeBase):
    """
    Returned in response to a successful `MergeDeveloperIdentities` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotAuthorizedException(autoboto.ShapeBase):
    """
    Thrown when a user is not authorized to access the requested resource.
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

    # The message returned by a NotAuthorizedException
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceConflictException(autoboto.ShapeBase):
    """
    Thrown when a user tries to use a login which is already linked to another
    account.
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

    # The message returned by a ResourceConflictException.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(autoboto.ShapeBase):
    """
    Thrown when the requested resource (for example, a dataset or record) does not
    exist.
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

    # The message returned by a ResourceNotFoundException.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RoleMapping(autoboto.ShapeBase):
    """
    A role mapping.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                autoboto.TypeInfo(RoleMappingType),
            ),
            (
                "ambiguous_role_resolution",
                "AmbiguousRoleResolution",
                autoboto.TypeInfo(AmbiguousRoleResolutionType),
            ),
            (
                "rules_configuration",
                "RulesConfiguration",
                autoboto.TypeInfo(RulesConfigurationType),
            ),
        ]

    # The role mapping type. Token will use `cognito:roles` and
    # `cognito:preferred_role` claims from the Cognito identity provider token to
    # map groups to roles. Rules will attempt to match claims from the token to
    # map to a role.
    type: "RoleMappingType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # If you specify Token or Rules as the `Type`, `AmbiguousRoleResolution` is
    # required.

    # Specifies the action to be taken if either no rules match the claim value
    # for the `Rules` type, or there is no `cognito:preferred_role` claim and
    # there are multiple `cognito:roles` matches for the `Token` type.
    ambiguous_role_resolution: "AmbiguousRoleResolutionType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The rules to be used for mapping users to roles.

    # If you specify Rules as the role mapping type, `RulesConfiguration` is
    # required.
    rules_configuration: "RulesConfigurationType" = dataclasses.field(
        default_factory=dict,
    )


class RoleMappingType(Enum):
    Token = "Token"
    Rules = "Rules"


@dataclasses.dataclass
class RulesConfigurationType(autoboto.ShapeBase):
    """
    A container for rules.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rules",
                "Rules",
                autoboto.TypeInfo(typing.List[MappingRule]),
            ),
        ]

    # An array of rules. You can specify up to 25 rules per identity provider.

    # Rules are evaluated in order. The first one to match specifies the role.
    rules: typing.List["MappingRule"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class SetIdentityPoolRolesInput(autoboto.ShapeBase):
    """
    Input to the `SetIdentityPoolRoles` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "roles",
                "Roles",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "role_mappings",
                "RoleMappings",
                autoboto.TypeInfo(typing.Dict[str, RoleMapping]),
            ),
        ]

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The map of roles associated with this pool. For a given role, the key will
    # be either "authenticated" or "unauthenticated" and the value will be the
    # Role ARN.
    roles: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # How users for a specific identity provider are to mapped to roles. This is
    # a string to RoleMapping object map. The string identifies the identity
    # provider, for example, "graph.facebook.com" or "cognito-idp-
    # east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id".

    # Up to 25 rules can be specified per identity provider.
    role_mappings: typing.Dict[str, "RoleMapping"] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TooManyRequestsException(autoboto.ShapeBase):
    """
    Thrown when a request is throttled.
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

    # Message returned by a TooManyRequestsException
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnlinkDeveloperIdentityInput(autoboto.ShapeBase):
    """
    Input to the `UnlinkDeveloperIdentity` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                autoboto.TypeInfo(str),
            ),
            (
                "identity_pool_id",
                "IdentityPoolId",
                autoboto.TypeInfo(str),
            ),
            (
                "developer_provider_name",
                "DeveloperProviderName",
                autoboto.TypeInfo(str),
            ),
            (
                "developer_user_identifier",
                "DeveloperUserIdentifier",
                autoboto.TypeInfo(str),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An identity pool ID in the format REGION:GUID.
    identity_pool_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The "domain" by which Cognito will refer to your users.
    developer_provider_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A unique ID used by your backend authentication process to identify a user.
    developer_user_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UnlinkIdentityInput(autoboto.ShapeBase):
    """
    Input to the UnlinkIdentity action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                autoboto.TypeInfo(str),
            ),
            (
                "logins",
                "Logins",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
            (
                "logins_to_remove",
                "LoginsToRemove",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A set of optional name-value pairs that map provider names to provider
    # tokens.
    logins: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Provider names to unlink from this identity.
    logins_to_remove: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UnprocessedIdentityId(autoboto.ShapeBase):
    """
    An array of UnprocessedIdentityId objects, each of which contains an ErrorCode
    and IdentityId.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                autoboto.TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                autoboto.TypeInfo(ErrorCode),
            ),
        ]

    # A unique identifier in the format REGION:GUID.
    identity_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The error code indicating the type of error that occurred.
    error_code: "ErrorCode" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )
