# ActionOutput

## ActionOutput

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **success_schema** | [JsonSchemaDocument](JsonSchemaDocument) | JSON schema that defines the transformed, successful result that will be sent back to the caller. If the &#39;flatten&#39; query parameter is omitted or false, this field will be returned. Either successSchema or successSchemaFlattened will be returned, not both. | [optional] |
| **success_schema_uri** | str | URI to retrieve success schema | [optional] |
| **error_schema** | [JsonSchemaDocument](JsonSchemaDocument) | JSON schema that defines the body of response when request is not successful. If the &#39;flatten&#39; query parameter is omitted or false, this field will be returned. Either errorSchema or errorSchemaFlattened will be returned, not both. | [optional] |
| **error_schema_uri** | str | URI to retrieve error schema | [optional] |
| **success_schema_flattened** | [JsonSchemaDocument](JsonSchemaDocument) | JSON schema that defines the transformed, successful result that will be sent back to the caller. The schema is transformed based on Architect&#39;s flattened format. If the &#39;flatten&#39; query parameter is supplied as true, this field will be returned. Either successSchema or successSchemaFlattened will be returned, not both. | [optional] |
| **error_schema_flattened** | object | JSON schema that defines the body of response when request is not successful. The schema is transformed based on Architect&#39;s flattened format. If the &#39;flatten&#39; query parameter is supplied as true, this field will be returned. Either errorSchema or errorSchemaFlattened will be returned, not both. | [optional] |



_PureCloudPlatformClientV2 215.0.0_
