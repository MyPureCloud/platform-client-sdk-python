# OrgOAuthClient

## OrgOAuthClient

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the OAuth client. | |
| **date_created** | datetime | Date this client was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date this client was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) | User that created this client | [optional] |
| **modified_by** | [DomainEntityRef](DomainEntityRef) | User that last modified this client | [optional] |
| **authorized_grant_type** | str | The OAuth Grant/Client type supported by this client. Code Authorization Grant/Client type - Preferred client type where the Client ID and Secret are required to create tokens. Used where the secret can be secured. PKCE-Enabled Code Authorization grant type - Code grant type which requires PKCE challenge and verifier to create tokens. Used in public clients for increased security. Implicit grant type - Client ID only is required to create tokens. Used in browser and mobile apps where the secret can not be secured. SAML2-Bearer extension grant type - SAML2 assertion provider for user authentication at the token endpoint. Client Credential grant type - Used to created access tokens that are tied only to the client.  | |
| **scope** | list[str] | The scope requested by this client. Scopes only apply to clients not using the client_credential grant | [optional] |
| **role_divisions** | [list[RoleDivision]](RoleDivision) | Set of roles and their corresponding divisions associated with this client. Roles and divisions only apply to clients using the client_credential grant | [optional] |
| **state** | str | The state of the OAuth client. Active: The OAuth client can be used to create access tokens. This is the default state. Disabled: Access tokens created by the client are invalid and new ones cannot be created. Inactive: Access tokens cannot be created with this OAuth client and it will be deleted. | [optional] |
| **date_to_delete** | datetime | The time at which this client will be deleted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **organization** | [NamedEntity](NamedEntity) | The  oauth client&#39;s organization. | [optional] |



_PureCloudPlatformClientV2 225.0.0_
