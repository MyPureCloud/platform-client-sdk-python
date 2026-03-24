# GoogleAuthToken

## GoogleAuthToken

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | ID of the Google OAuth 2 access token. The token cannot be accessed via Genesys API, only referenced by this property. When the token is not referenced by any integration, it is deleted after 24 hours. | |
| **client_id** | str | ID of the Genesys-owned Google API client | |
| **scopes** | list[str] | Google API authorization scopes that have been granted to the Genesys-owned Google API client | |
| **date_created** | datetime | Date this token was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **created_by** | [DomainEntityRef](DomainEntityRef) | User reference that created this Integration | |



_PureCloudPlatformClientV2 254.0.0_
