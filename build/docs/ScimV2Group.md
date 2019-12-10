---
title: ScimV2Group
---
## ScimV2Group

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The ID of the SCIM resource. Set by the service provider. \&quot;caseExact\&quot; is set to \&quot;true\&quot;. \&quot;Mutability\&quot; is set to \&quot;readOnly\&quot;. \&quot;Returned\&quot; is set to \&quot;always\&quot;. | [optional] |
| **schemas** | **list[str]** | The list of supported schemas. | [optional] |
| **display_name** | **str** | The display name of the group. | [optional] |
| **members** | [**list[ScimV2MemberReference]**](ScimV2MemberReference.html) | The list of members in the group. | [optional] |
| **meta** | [**ScimMetadata**](ScimMetadata.html) | The metadata of the SCIM resource. | [optional] |
{: class="table table-striped"}


