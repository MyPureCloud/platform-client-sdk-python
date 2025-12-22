# ActionInput

## ActionInput

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **input_schema** | [JsonSchemaDocument](JsonSchemaDocument) | JSON Schema that defines the body of the request that the client (edge/architect/postman) is sending to the service, on the /execute path. If the &#39;flatten&#39; query parameter is omitted or false, this field will be returned. Either inputSchema or inputSchemaFlattened will be returned, not both. | [optional] |
| **input_schema_flattened** | [JsonSchemaDocument](JsonSchemaDocument) | JSON Schema that defines the body of the request that the client (edge/architect/postman) is sending to the service, on the /execute path. The schema is transformed based on Architect&#39;s flattened format. If the &#39;flatten&#39; query parameter is supplied as true, this field will be returned. Either inputSchema or inputSchemaFlattened will be returned, not both. | [optional] |
| **input_schema_uri** | str | The URI of the input schema | [optional] |



_PureCloudPlatformClientV2 246.1.0_
