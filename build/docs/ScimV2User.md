---
title: ScimV2User
---
## ScimV2User

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The ID of the SCIM resource. Set by the service provider. \&quot;caseExact\&quot; is set to \&quot;true\&quot;. \&quot;Mutability\&quot; is set to \&quot;readOnly\&quot;. \&quot;Returned\&quot; is set to \&quot;always\&quot;. | [optional] |
| **schemas** | **list[str]** | The list of supported schemas. | [optional] |
| **active** | **bool** | Indicates whether the user&#39;s administrative status is active. | [optional] |
| **user_name** | **str** | The user&#39;s PureCloud email address. Must be unique. | [optional] |
| **display_name** | **str** | The display name of the user. | [optional] |
| **password** | **str** | The new password for the PureCloud user. Does not return an existing password. | [optional] |
| **title** | **str** | The user&#39;s title. | [optional] |
| **phone_numbers** | [**list[ScimPhoneNumber]**](ScimPhoneNumber.html) | The list of the user&#39;s phone numbers. | [optional] |
| **emails** | [**list[ScimEmail]**](ScimEmail.html) | The list of the user&#39;s email addresses. | [optional] |
| **photos** | [**list[Photo]**](Photo.html) | The list of the user&#39;s photos. | [optional] |
| **external_id** | **str** | The external ID of the user. Set by the provisioning client. \&quot;caseExact\&quot; is set to \&quot;true\&quot;. \&quot;mutability\&quot; is set to \&quot;readWrite\&quot;. | [optional] |
| **groups** | [**list[ScimV2GroupReference]**](ScimV2GroupReference.html) | The list of groups that the user is a member of. | [optional] |
| **roles** | **list[str]** | The list of roles assigned to the user. | [optional] |
| **urnietfparamsscimschemasextensionenterprise2_0_user** | [**ScimV2EnterpriseUser**](ScimV2EnterpriseUser.html) |  | [optional] |
| **meta** | [**ScimMetadata**](ScimMetadata.html) | Resource SCIM meta | [optional] |
{: class="table table-striped"}


