# ScimConfigResourceType

## ScimConfigResourceType

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the SCIM resource. Set by the service provider. \&quot;caseExact\&quot; is set to \&quot;true\&quot;. \&quot;mutability\&quot; is set to \&quot;readOnly\&quot;. \&quot;returned\&quot; is set to \&quot;always\&quot;. | [optional] |
| **schemas** | list[str] | The list of supported schemas. | [optional] |
| **name** | str | The name of the resource type. | [optional] |
| **description** | str | The description of the resource type. | [optional] |
| **schema** | str | The URI of the primary or base schema for the resource type. | [optional] |
| **schema_extensions** | [list[ScimConfigResourceTypeSchemaExtension]](ScimConfigResourceTypeSchemaExtension) | The list of schema extensions for the resource type. | [optional] |
| **endpoint** | str | The HTTP-addressable endpoint of the resource type. Appears after the base URL. | [optional] |
| **meta** | [ScimMetadata](ScimMetadata) | The metadata of the SCIM resource. Only \&quot;location\&quot; and \&quot;resourceType\&quot; are set for \&quot;ResourceType\&quot; resources. | [optional] |



_PureCloudPlatformClientV2 249.0.0_
