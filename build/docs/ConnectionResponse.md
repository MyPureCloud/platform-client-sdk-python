# ConnectionResponse

## ConnectionResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the connection. | [optional] |
| **type** | str | Type of the connection. | [optional] |
| **integration** | [KnowledgeIntegrationReference](KnowledgeIntegrationReference) | The reference to the integration associated with the connection. | [optional] |
| **authentication_properties** | [AuthenticationProperties](AuthenticationProperties) | Authentication properties which can be used to initiate authentication of a user. | [optional] |
| **created_by** | [UserReference](UserReference) | Reference of the creator. | [optional] |
| **modified_by** | [UserReference](UserReference) | Reference of the user whom modified the connection. | [optional] |
| **date_created** | datetime | Date of the creation of connection. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date of the last modification made to the connection. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **status** | str | Current status of the connection. | [optional] |
| **error** | [ErrorBody](ErrorBody) | Optional error message of the connection. | [optional] |
| **date_expiry** | datetime | Expiry date of the authentication credentials. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 257.0.0_
