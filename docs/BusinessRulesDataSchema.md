# BusinessRulesDataSchema

## BusinessRulesDataSchema

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the schema.  Only required if a schema is used for custom fields during external entity creation or updates. | [optional] |
| **name** | str |  | [optional] |
| **version** | int | The schema&#39;s version, a positive integer. Required for updates. | |
| **applies_to** | list[str] | Indicates the built-in entity type to which this schema applies. | [optional] |
| **enabled** | bool | The schema&#39;s enabled/disabled status. A disabled schema cannot be assigned to any other entities, but the data on those entities from the schema still exists. | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) | The URI of the user that created this schema. | [optional] |
| **date_created** | datetime | The date and time this schema was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **json_schema** | [JsonSchemaDocument](JsonSchemaDocument) | A JSON schema defining the extension to the built-in entity type. | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 240.0.0_
