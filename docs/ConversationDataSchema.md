# ConversationDataSchema

## ConversationDataSchema

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the schema. | [optional] |
| **version** | int | The schema&#39;s version, a positive integer. | [optional] |
| **enabled** | bool | The schema&#39;s enabled/disabled status. A disabled schema cannot be assigned to any other entities, but the data on those entities from the schema still exists. | [optional] |
| **date_created** | datetime | The date and time this schema version was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) | The URI of the user that created this schema. | [optional] |
| **json_schema** | [ConversationJsonSchemaDocument](ConversationJsonSchemaDocument) | A JSON schema defining the extension to the built-in entity type. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 252.1.0_
