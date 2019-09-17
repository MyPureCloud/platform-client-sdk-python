---
title: ScimV2Group
---
## ScimV2Group

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The ID of the SCIM resource. Set by the service provider. caseExact is set to true. Mutability is set to readOnly. Returned is set to always. | [optional] |
| **schemas** | **list[str]** | The list of supported schemas. | [optional] |
| **display_name** | **str** | The display name for the group. | [optional] |
| **members** | [**list[ScimV2MemberReference]**](ScimV2MemberReference.html) | A list of members in a SCIM group. | [optional] |
| **meta** | [**ScimMetadata**](ScimMetadata.html) | Resource SCIM meta | [optional] |
{: class="table table-striped"}


