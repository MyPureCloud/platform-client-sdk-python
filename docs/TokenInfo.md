# TokenInfo

## TokenInfo

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **organization** | [NamedEntity](NamedEntity) | The current organization | [optional] |
| **home_organization** | [NamedEntity](NamedEntity) | The token&#39;s home organization | [optional] |
| **authorized_scope** | list[str] | The list of scopes authorized for the OAuth client | [optional] |
| **cloned_user** | [TokenInfoClonedUser](TokenInfoClonedUser) | Only present when a user is a clone of trustee user in the trustor org. | [optional] |
| **date_token_idles** | datetime | Date/Time when token is due to expire. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **o_auth_client** | [OrgOAuthClient](OrgOAuthClient) |  | [optional] |



_PureCloudPlatformClientV2 234.0.0_
