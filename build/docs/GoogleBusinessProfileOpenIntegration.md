# GoogleBusinessProfileOpenIntegration

## GoogleBusinessProfileOpenIntegration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A unique Integration Id. | |
| **name** | str | The name of the Google Business Profile Open Integration. | |
| **supported_content** | [SupportedContentReference](SupportedContentReference) | Defines the SupportedContent profile configured for an integration | [optional] |
| **messaging_setting** | [MessagingSettingReference](MessagingSettingReference) |  | [optional] |
| **status** | str | The status of the Google Business Profile Open Integration | [optional] |
| **recipient** | [DomainEntityRef](DomainEntityRef) | The recipient associated to the Google Business Profile Open Integration. This recipient is used to associate a flow to an integration | [optional] |
| **date_created** | datetime | Date this Integration was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date this Integration was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) | User reference that created this Integration | [optional] |
| **modified_by** | [DomainEntityRef](DomainEntityRef) | User reference that last modified this Integration | [optional] |
| **create_status** | str | Status of asynchronous create operation | [optional] |
| **create_error** | [ErrorBody](ErrorBody) | Error information returned, if createStatus is set to Error | [optional] |
| **token** | [GoogleAuthTokenReference](GoogleAuthTokenReference) | Google OAuth 2 access token reference. The actual token cannot be accessed via Genesys API, only referenced by this property by its ID. When the token is not referenced by any integration, it is deleted after 24 hours. | |
| **account** | [GoogleBusinessProfileAccountReference](GoogleBusinessProfileAccountReference) | Google Business Profile account accessible with the authorization token | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 257.0.0_
