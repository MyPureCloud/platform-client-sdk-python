---
title: ScimV2SchemaDefinition
---
## ScimV2SchemaDefinition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The ID of the SCIM resource. Set by the service provider. \&quot;caseExact\&quot; is set to \&quot;true\&quot;. \&quot;Mutability\&quot; is set to \&quot;readOnly\&quot;. \&quot;Returned\&quot; is set to \&quot;always\&quot;. | [optional] |
| **name** | **str** | Schema name. | [optional] |
| **description** | **str** | Schema description. | [optional] |
| **attributes** | [**list[ScimV2SchemaAttribute]**](ScimV2SchemaAttribute.html) | A complex type that defines service provider attributes and their qualities. | [optional] |
| **meta** | [**ScimMetadata**](ScimMetadata.html) | The metadata of the SCIM resource. | [optional] |
{: class="table table-striped"}


