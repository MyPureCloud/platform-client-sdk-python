# TokenInfo

## TokenInfo

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **organization** | [NamedEntity](NamedEntity) | The current organization | [optional] |
| **home_organization** | [NamedEntity](NamedEntity) | The token&#39;s home organization | [optional] |
| **authorized_scope** | list[str] | The list of scopes authorized for the OAuth client | [optional] |
| **cloned_user** | [TokenInfoClonedUser](TokenInfoClonedUser) | Only present when a user is a clone of trustee user in the trustor org. | [optional] |
| **o_auth_client** | [OrgOAuthClient](OrgOAuthClient) |  | [optional] |



_PureCloudPlatformClientV2 223.0.0_
