# BusinessRulesSchemaUpdateRequest

## BusinessRulesSchemaUpdateRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **version** | int | The schema&#39;s version, a positive integer. Required for updates. | |
| **enabled** | bool | The schema&#39;s enabled/disabled status. A disabled schema cannot be assigned to any other entities, but the data on those entities from the schema still exists. | [optional] |
| **json_schema** | [JsonSchemaWithDefinitions](JsonSchemaWithDefinitions) | A JSON schema defining the extension to the built-in entity type. | |



_PureCloudPlatformClientV2 244.0.0_
