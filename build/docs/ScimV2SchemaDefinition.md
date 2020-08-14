---
title: ScimV2SchemaDefinition
---
## ScimV2SchemaDefinition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The ID of the SCIM resource. Set by the service provider. \&quot;caseExact\&quot; is set to \&quot;true\&quot;. \&quot;mutability\&quot; is set to \&quot;readOnly\&quot;. \&quot;returned\&quot; is set to \&quot;always\&quot;. | [optional] |
| **name** | **str** | The name of the schema. | [optional] |
| **description** | **str** | The description of the schema. | [optional] |
| **attributes** | [**list[ScimV2SchemaAttribute]**](ScimV2SchemaAttribute.html) | The list of service provider attributes. | [optional] |
{: class="table table-striped"}


