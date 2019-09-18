---
title: ScimConfigResourceType
---
## ScimConfigResourceType

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The ID of the SCIM resource. Set by the service provider. caseExact is set to true. Mutability is set to readOnly. Returned is set to always. | [optional] |
| **schemas** | **list[str]** | schemas supported | [optional] |
| **name** | **str** | Resource name. | [optional] |
| **description** | **str** | Resource description. | [optional] |
| **schema** | **str** | The resource type&#39;s primary/base schema URI. | [optional] |
| **schema_extensions** | [**list[ScimConfigResourceTypeSchemaExtension]**](ScimConfigResourceTypeSchemaExtension.html) | Resource extension schemas | [optional] |
| **endpoint** | **str** | Resource HTTP endpoint. | [optional] |
| **meta** | [**ScimMetadata**](ScimMetadata.html) | Resource SCIM meta | [optional] |
{: class="table table-striped"}


